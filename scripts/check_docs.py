#!/usr/bin/env python3
"""Validate the repository's Markdown structure without third-party packages."""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
SOURCE_ID_RE = re.compile(r"SRC-[A-Z0-9]+(?:-[A-Z0-9]+)*")
SOURCE_ID_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_])SRC-[A-Za-z0-9_-]+")
STATUS_RE = re.compile(r"\*\*状态：([^*]+)\*\*")
TOPIC_FILE_RE = re.compile(r"^\d{2}_[a-z0-9]+(?:_[a-z0-9]+)*\.md$")

ALLOWED_STATUSES = {
    "Governance / Normative",
    "Normative",
    "Navigation / Non-normative",
    "Learning / Navigation",
    "Learning / Non-normative",
    "Training / Derived",
    "Reference / Non-normative",
    "Evidence Registry / Non-normative",
    "Evidence Audit / Non-normative",
}

AUDIT_STATUSES = {
    "已核对",
    "部分核对",
    "待核对",
    "内部执行政策",
    "内部治理",
}

LEARNING_DIRS = [
    "00_method",
    "01_market_cycle",
    "02_context",
    "03_order_flow",
    "04_patterns",
    "05_setups",
    "06_trade_management",
]

REQUIRED_PATHS = [
    "README.md",
    "LEARNING_PATH.md",
    "EXECUTION_MANUAL.md",
    "DOCUMENTATION_GOVERNANCE.md",
    "training/README.md",
    "reference/README.md",
    "reference/glossary.md",
    "reference/official_sources.md",
    "reference/audit_matrix.md",
]

REQUIRED_DIRS = [
    "learning",
    "training",
    "reference",
    "scripts",
]

FORBIDDEN_OLD_PATHS = [
    "00_method",
    "01_market_cycle",
    "02_context",
    "03_order_flow",
    "04_setups",
    "05_patterns",
    "06_trade_management",
    "07_scenarios",
    "synthesis",
    "research",
]

INTERNAL_FIELD_RE = re.compile(
    r"(?<![A-Za-z0-9_])(?:M[1-6]|K[1-4]|T[1-4]|P[0-4]|G[1-3]|PT[12]|MaxLoss|PlannedLoss)(?![A-Za-z0-9_])"
)

INTERNAL_FLOW_RE = re.compile(
    r"(?<![A-Za-z0-9_])[MKCTDQPG](?:\s*(?:/|→|->)\s*[MKCTDQPG])+(?![A-Za-z0-9_])"
)

INTERNAL_LABEL_RE = re.compile(
    r"(?m)^(?:#{1,6}\s+|[-*]\s+|\|\s*)?`?[MKCTDQPG]`?\s*[：:]"
)

ATLAS_RE = re.compile(
    r"al-brooks-pattern-atlas|pattern atlas|88\s*个图形|价格行为图谱",
    re.IGNORECASE,
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def github_slug(title: str) -> str:
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)
    title = re.sub(r"[`*_~]", "", title).strip().lower()
    chars: list[str] = []
    for char in title:
        if char.isspace():
            chars.append("-")
        elif char == "-" or not unicodedata.category(char).startswith(("P", "S")):
            chars.append(char)
    return re.sub(r"-+", "-", "".join(chars)).strip("-")


def heading_slugs(text: str) -> set[str]:
    counts: Counter[str] = Counter()
    slugs: set[str] = set()
    for match in HEADING_RE.finditer(text):
        base = github_slug(match.group(2))
        index = counts[base]
        counts[base] += 1
        slugs.add(base if index == 0 else f"{base}-{index}")
    return slugs


def markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def expected_status(path: Path) -> str | None:
    relative = rel(path)
    fixed = {
        "LEARNING_PATH.md": "Navigation / Non-normative",
        "EXECUTION_MANUAL.md": "Normative",
        "DOCUMENTATION_GOVERNANCE.md": "Governance / Normative",
        "reference/README.md": "Reference / Non-normative",
        "reference/glossary.md": "Reference / Non-normative",
        "reference/official_sources.md": "Evidence Registry / Non-normative",
        "reference/audit_matrix.md": "Evidence Audit / Non-normative",
    }
    if relative in fixed:
        return fixed[relative]

    parts = path.relative_to(ROOT).parts
    if parts[0] == "learning":
        return "Learning / Navigation" if path.name == "README.md" else "Learning / Non-normative"
    if parts[0] == "training":
        return "Training / Derived"
    return None


def markdown_section(text: str, heading: str) -> str | None:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return None
    following = re.search(r"^##\s+", text[match.end() :], re.MULTILINE)
    end = match.end() + following.start() if following else len(text)
    return text[match.end() : end]


def markdown_table_rows(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows[1:] if rows else []


def check_required_structure(errors: list[str]) -> None:
    for item in REQUIRED_DIRS:
        if not (ROOT / item).is_dir():
            errors.append(f"missing required directory: {item}/")

    for item in REQUIRED_PATHS:
        if not (ROOT / item).exists():
            errors.append(f"missing required path: {item}")

    learning_root = ROOT / "learning"
    if learning_root.is_dir():
        actual_learning = sorted(path.name for path in learning_root.iterdir() if path.is_dir())
        if actual_learning != LEARNING_DIRS:
            errors.append(
                "learning chapter order mismatch: "
                f"expected {LEARNING_DIRS}, found {actual_learning}"
            )

    for old_path in FORBIDDEN_OLD_PATHS:
        if (ROOT / old_path).exists():
            errors.append(f"legacy top-level path still exists: {old_path}/")

    if (ROOT / "al-brooks-pattern-atlas.html").exists():
        errors.append("removed atlas artifact has returned: al-brooks-pattern-atlas.html")

    manual = ROOT / "EXECUTION_MANUAL.md"
    if manual.is_file() and not re.search(
        r"^##\s+高级执行附录\s*$", manual.read_text(encoding="utf-8"), re.MULTILINE
    ):
        errors.append("EXECUTION_MANUAL.md: missing '高级执行附录' section")


def check_markdown_structure(files: list[Path], errors: list[str]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        headings = [(len(match.group(1)), match.group(2)) for match in HEADING_RE.finditer(text)]

        if sum(level == 1 for level, _ in headings) != 1:
            errors.append(f"{rel(path)}: expected exactly one H1")

        previous = 0
        for level, title in headings:
            if previous and level > previous + 1:
                errors.append(
                    f"{rel(path)}: heading jump H{previous}->H{level} at {title!r}"
                )
            previous = level

        fence_count = sum(line.lstrip().startswith("```") for line in text.splitlines())
        if fence_count % 2:
            errors.append(f"{rel(path)}: unbalanced fenced code block")

        for number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{rel(path)}:{number}: trailing whitespace")

        if path != ROOT / "README.md":
            expected = expected_status(path)
            status_match = STATUS_RE.search("\n".join(text.splitlines()[:10]))
            if not status_match:
                errors.append(f"{rel(path)}: missing status declaration near the top")
            else:
                actual = status_match.group(1).strip()
                if actual not in ALLOWED_STATUSES:
                    errors.append(f"{rel(path)}: unsupported status {actual!r}")
                elif expected is None:
                    errors.append(f"{rel(path)}: path has no governed status mapping")
                elif actual != expected:
                    errors.append(
                        f"{rel(path)}: expected status {expected!r}, found {actual!r}"
                    )


def check_file_names(files: list[Path], errors: list[str]) -> None:
    for path in files:
        parts = path.relative_to(ROOT).parts
        if parts[0] == "learning":
            if len(parts) != 3 or parts[1] not in LEARNING_DIRS:
                errors.append(
                    f"{rel(path)}: learning documents must live directly in a governed chapter"
                )
        elif parts[0] == "training" and len(parts) != 2:
            errors.append(f"{rel(path)}: {parts[0]} documents must use a flat directory")

        if parts[0] in {"learning", "training"}:
            if path.name != "README.md" and not TOPIC_FILE_RE.fullmatch(path.name):
                errors.append(
                    f"{rel(path)}: topic filename must match NN_topic_name.md"
                )


def resolve_local_target(source: Path, raw_target: str) -> tuple[Path, str] | None:
    if raw_target.startswith(("http://", "https://", "mailto:")):
        return None
    path_part, _, fragment = raw_target.partition("#")
    target = source if not path_part else (source.parent / unquote(path_part)).resolve()
    if target.is_dir():
        target = target / "README.md"
    return target, unquote(fragment).lower()


def check_links(files: list[Path], errors: list[str]) -> dict[Path, int]:
    incoming = {path.resolve(): 0 for path in files}
    slug_cache: dict[Path, set[str]] = {}

    for source in files:
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1).strip()
            resolved = resolve_local_target(source, raw_target)
            if resolved is None:
                continue
            target, fragment = resolved
            location = f"{rel(source)}:{line_number(text, match.start())}"

            if not target.exists():
                errors.append(f"{location}: missing local link target {raw_target!r}")
                continue

            if target.resolve() in incoming and target.resolve() != source.resolve():
                incoming[target.resolve()] += 1

            if fragment and target.suffix.lower() == ".md":
                slugs = slug_cache.setdefault(
                    target.resolve(), heading_slugs(target.read_text(encoding="utf-8"))
                )
                if fragment not in slugs:
                    errors.append(f"{location}: missing heading anchor {raw_target!r}")

    return incoming


def check_navigation(files: list[Path], incoming: dict[Path, int], errors: list[str]) -> None:
    index_dirs = [ROOT / "learning" / name for name in LEARNING_DIRS]
    index_dirs += [ROOT / "training", ROOT / "reference"]

    for directory in index_dirs:
        index = directory / "README.md"
        if not index.exists():
            errors.append(f"{rel(directory)}: missing README.md")
            continue
        linked = {
            target.partition("#")[0]
            for target in LINK_RE.findall(index.read_text(encoding="utf-8"))
            if not target.startswith(("http://", "https://", "mailto:", "#"))
        }
        expected = {path.name for path in directory.glob("*.md") if path.name != "README.md"}
        missing = sorted(expected - linked)
        if missing:
            errors.append(f"{rel(index)}: does not index {missing}")

    for path in files:
        if path == ROOT / "README.md":
            continue
        if incoming.get(path.resolve(), 0) == 0:
            errors.append(f"{rel(path)}: no incoming local Markdown link")


def check_sources(files: list[Path], errors: list[str]) -> None:
    registry_path = ROOT / "reference" / "official_sources.md"
    if not registry_path.is_file():
        return
    registry = registry_path.read_text(encoding="utf-8")
    registry_section = markdown_section(registry, "已登记来源")
    if registry_section is None:
        errors.append(f"{rel(registry_path)}: missing '已登记来源' section")
        registered: set[str] = set()
    else:
        registered_ids: list[str] = []
        registry_rows = markdown_table_rows(registry_section)
        if not registry_rows:
            errors.append(f"{rel(registry_path)}: source registry has no data rows")
        for cells in registry_rows:
            source_id = cells[0].strip("`") if cells else ""
            if not SOURCE_ID_RE.fullmatch(source_id):
                errors.append(
                    f"{rel(registry_path)}: invalid registered Source ID {source_id!r}"
                )
                continue
            registered_ids.append(source_id)
        duplicates = sorted(
            source_id
            for source_id, count in Counter(registered_ids).items()
            if count > 1
        )
        if duplicates:
            errors.append(f"{rel(registry_path)}: duplicate registered Source IDs: {duplicates}")
        registered = set(registered_ids)

    used: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in SOURCE_ID_TOKEN_RE.finditer(text):
            source_id = match.group(0)
            if not SOURCE_ID_RE.fullmatch(source_id):
                errors.append(
                    f"{rel(path)}:{line_number(text, match.start())}: "
                    f"invalid Source ID {source_id!r}"
                )
                continue
            used.add(source_id)
    missing = sorted(used - registered)
    if missing:
        errors.append(f"unregistered Source IDs: {missing}")


def check_audit_statuses(errors: list[str]) -> None:
    audit_path = ROOT / "reference" / "audit_matrix.md"
    if not audit_path.is_file():
        return
    audit = audit_path.read_text(encoding="utf-8")
    matrix_section = markdown_section(audit, "当前矩阵")
    if matrix_section is None:
        errors.append(f"{rel(audit_path)}: missing '当前矩阵' section")
        return

    rows = markdown_table_rows(matrix_section)
    if not rows:
        errors.append(f"{rel(audit_path)}: audit matrix has no data rows")
        return

    for number, cells in enumerate(rows, 1):
        if len(cells) != 6:
            errors.append(
                f"{rel(audit_path)}: matrix row {number} has {len(cells)} columns, expected 6"
            )
            continue
        status = cells[-1].split("；", 1)[0].strip()
        if status not in AUDIT_STATUSES:
            errors.append(
                f"{rel(audit_path)}: matrix row {number} uses unsupported audit status {status!r}"
            )


def check_layer_boundaries(files: list[Path], errors: list[str]) -> None:
    legacy_patterns = [
        (INTERNAL_FIELD_RE, "old numbered execution label"),
        (INTERNAL_FLOW_RE, "old single-letter execution chain"),
        (INTERNAL_LABEL_RE, "old single-letter field label"),
    ]
    for path in files:
        text = path.read_text(encoding="utf-8")
        for pattern, description in legacy_patterns:
            match = pattern.search(text)
            if match:
                errors.append(
                    f"{rel(path)}:{line_number(text, match.start())}: "
                    f"{description} {match.group(0)!r}"
                )

    canonical_markers = (
        "[基本信息]",
        "[市场与候选]",
        "[交易计划]",
        "[交易数学]",
        "[订单与成交",
        "[管理事件",
    )
    for path in (ROOT / "training").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        markers = [marker for marker in canonical_markers if marker in text]
        if len(markers) >= 2 or re.search(
            r"^#{1,6}\s+规范执行记录\s*$", text, re.MULTILINE
        ):
            errors.append(f"{rel(path)}: duplicates the canonical execution form")

    for path in files:
        text = path.read_text(encoding="utf-8")
        match = ATLAS_RE.search(text)
        if match:
            errors.append(
                f"{rel(path)}:{line_number(text, match.start())}: removed atlas reference {match.group(0)!r}"
            )


def main() -> int:
    errors: list[str] = []
    files = markdown_files()

    check_required_structure(errors)
    check_markdown_structure(files, errors)
    check_file_names(files, errors)
    incoming = check_links(files, errors)
    check_navigation(files, incoming, errors)
    check_sources(files, errors)
    check_audit_statuses(errors)
    check_layer_boundaries(files, errors)

    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Documentation checks passed: {len(files)} Markdown files validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
