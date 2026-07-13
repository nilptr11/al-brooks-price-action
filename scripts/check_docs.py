#!/usr/bin/env python3
"""Run the few durable checks needed by this Markdown repository."""

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
SOURCE_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_])SRC-[A-Za-z0-9_-]+")

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


def relative(path: Path) -> str:
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
        suffix = counts[base]
        counts[base] += 1
        slugs.add(base if suffix == 0 else f"{base}-{suffix}")
    return slugs


def markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def check_required_paths(errors: list[str]) -> None:
    for item in REQUIRED_PATHS:
        if not (ROOT / item).is_file():
            errors.append(f"missing core document: {item}")


def check_h1(files: list[Path], errors: list[str]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        h1_count = sum(len(match.group(1)) == 1 for match in HEADING_RE.finditer(text))
        if h1_count != 1:
            errors.append(f"{relative(path)}: expected exactly one H1, found {h1_count}")


def local_target(source: Path, raw: str) -> tuple[Path, str] | None:
    raw = raw.strip().strip("<>")
    if raw.startswith(("http://", "https://", "mailto:")):
        return None
    path_part, _, fragment = raw.partition("#")
    target = source if not path_part else (source.parent / unquote(path_part)).resolve()
    if target.is_dir():
        target = target / "README.md"
    return target, unquote(fragment).lower()


def check_links(files: list[Path], errors: list[str]) -> None:
    slug_cache: dict[Path, set[str]] = {}
    for source in files:
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip()
            resolved = local_target(source, raw)
            if resolved is None:
                continue
            target, fragment = resolved
            location = f"{relative(source)}:{line_number(text, match.start())}"
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{location}: local link escapes repository {raw!r}")
                continue
            if not target.exists():
                errors.append(f"{location}: missing local link target {raw!r}")
                continue
            if fragment and target.suffix.lower() == ".md":
                slugs = slug_cache.setdefault(
                    target, heading_slugs(target.read_text(encoding="utf-8"))
                )
                if fragment not in slugs:
                    errors.append(f"{location}: missing heading anchor {raw!r}")


def registered_source_ids(registry: str, errors: list[str]) -> set[str]:
    match = re.search(
        r"^## 已登记来源\s*$([\s\S]*?)(?=^##\s|\Z)", registry, re.MULTILINE
    )
    if not match:
        errors.append("reference/official_sources.md: missing '已登记来源' section")
        return set()
    ids = re.findall(r"^\|\s*`(SRC-[^`]+)`\s*\|", match.group(1), re.MULTILINE)
    invalid = sorted({source_id for source_id in ids if not SOURCE_ID_RE.fullmatch(source_id)})
    if invalid:
        errors.append(f"reference/official_sources.md: invalid Source IDs: {invalid}")
    duplicates = sorted(source_id for source_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append(f"reference/official_sources.md: duplicate Source IDs: {duplicates}")
    return {source_id for source_id in ids if SOURCE_ID_RE.fullmatch(source_id)}


def check_source_ids(files: list[Path], errors: list[str]) -> None:
    registry_path = ROOT / "reference/official_sources.md"
    if not registry_path.is_file():
        return
    registered = registered_source_ids(registry_path.read_text(encoding="utf-8"), errors)
    used: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in SOURCE_TOKEN_RE.finditer(text):
            source_id = match.group(0)
            if not SOURCE_ID_RE.fullmatch(source_id):
                errors.append(
                    f"{relative(path)}:{line_number(text, match.start())}: "
                    f"invalid Source ID {source_id!r}"
                )
            else:
                used.add(source_id)
    missing = sorted(used - registered)
    if missing:
        errors.append(f"unregistered Source IDs: {missing}")
    registry = registry_path.read_text(encoding="utf-8")
    anchor_match = re.search(
        r"^## 来源锚点定位\s*$([\s\S]*?)(?=^##\s|\Z)", registry, re.MULTILINE
    )
    if not anchor_match:
        errors.append("reference/official_sources.md: missing '来源锚点定位' section")
        return
    anchored = set(
        re.findall(r"^\|\s*`(SRC-[^`]+)`\s*\|", anchor_match.group(1), re.MULTILINE)
    )
    missing_anchors = sorted(registered - anchored)
    if missing_anchors:
        errors.append(f"Source IDs without registry anchors: {missing_anchors}")


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    check_required_paths(errors)
    check_h1(files, errors)
    check_links(files, errors)
    check_source_ids(files, errors)

    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Documentation checks passed: {len(files)} Markdown files validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
