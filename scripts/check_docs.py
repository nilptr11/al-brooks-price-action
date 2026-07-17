#!/usr/bin/env python3
"""Validate the human-readable Brooks PA knowledge and execution handbook."""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
VISIBLE_LINK_RE = re.compile(r"(!?\[[^\]]*\])\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
SOURCE_ID_RE = re.compile(r"SRC-[A-Z0-9]+(?:-[A-Z0-9]+)*")
SOURCE_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_])SRC-[A-Za-z0-9_-]+")
FENCED_CODE_RE = re.compile(r"^\s*(?:```|~~~)", re.MULTILINE)
SNAKE_CASE_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:[a-z][a-z0-9]*_)+[a-z0-9]+(?:\[\])?(?![A-Za-z0-9])"
)
FIELD_ASSIGNMENT_RE = re.compile(
    r"(?<![A-Za-z0-9_-])[a-z][a-z0-9_]*(?:\[\])?\s*=\s*(?!=)"
)

# These identifiers belonged to the removed machine-oriented strategy model.  They
# are deliberately not aliases for the new natural-language pages.
OLD_STRATEGY_ID_RE = re.compile(
    r"(?<![A-Z0-9-])(?:"
    r"BO-0[1-4]|TC-0[1-4]|TR-0[1-3]|BM-01|RV-0[1-4]|"
    r"OPEN-0[12]|TIME-01|FAIL-01"
    r")(?![A-Z0-9-])",
    re.IGNORECASE,
)
OLD_STRATEGY_FILENAME_RE = re.compile(
    r"^(?:bo|tc|tr|bm|rv|open|time|fail)_\d{2}(?:_|\.md)", re.IGNORECASE
)

FIXED_REQUIRED_PATHS = {
    "README.md",
    "learning/README.md",
    "strategy/README.md",
    "strategy/how_to_choose.md",
    "strategy/switching_after_failure.md",
    "execution/README.md",
    "execution/execution_manual.md",
    "execution/execution_modes.md",
    "execution/execution_and_review_record.md",
    "reference/README.md",
    "reference/glossary.md",
    "reference/official_sources.md",
    "reference/strategy_map.md",
}

FORBIDDEN_PATHS = {
    "quant",
    "training",
    "governance",
    "strategy/playbooks",
    "strategy/00_decision_lifecycle.md",
    "strategy/01_strategy_specification.md",
    "strategy/02_strategy_registry.md",
    "execution/00_execution_manual.md",
    "execution/01_record_schema.md",
    "execution/02_human_record_template.md",
    "reference/audit_matrix.md",
    "LEARNING_PATH.md",
    "DOCUMENTATION_GOVERNANCE.md",
    "EXECUTION_MANUAL.md",
    "EXECUTION_RECORD_TEMPLATE.md",
}

FORBIDDEN_REFERENCE_TOKENS = {
    "quant/",
    "training/",
    "governance/",
    "strategy/playbooks/",
    "strategy/00_decision_lifecycle.md",
    "strategy/01_strategy_specification.md",
    "strategy/02_strategy_registry.md",
    "execution/00_execution_manual.md",
    "execution/01_record_schema.md",
    "execution/02_human_record_template.md",
    "reference/audit_matrix.md",
}

COMPATIBILITY_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:deprecated|legacy|alias|compat(?:ibility)?)(?![A-Za-z0-9])"
    r"|兼容|旧路径|重定向|别名",
    re.IGNORECASE,
)

# Ban only implementation vocabulary from the retired in-repository machine
# model.  Brooks terms such as H2, MTR and OCO, real broker order numbers, and
# natural words such as “状态” or “事件” remain valid.
MACHINE_TERM_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\bartifact(?:s)?\b", re.IGNORECASE), "Artifact"),
    (re.compile(r"\badapter(?:s)?\b", re.IGNORECASE), "Adapter"),
    (re.compile(r"\breducer(?:s)?\b", re.IGNORECASE), "Reducer"),
    (re.compile(r"\bschema\b", re.IGNORECASE), "Schema"),
    (re.compile(r"\bpayload\b", re.IGNORECASE), "Payload"),
    (re.compile(r"\bfsm\b", re.IGNORECASE), "FSM"),
    (re.compile(r"\borchestration\b", re.IGNORECASE), "Orchestration"),
    (re.compile(r"\bdeployment\b", re.IGNORECASE), "Deployment"),
    (re.compile(r"\bbacktest(?:ing)?\b", re.IGNORECASE), "Backtest"),
    (re.compile(r"\bwalk[- ]forward\b", re.IGNORECASE), "Walk-forward"),
    (re.compile(r"\bout[- ]of[- ]sample\b|\bOOS\b", re.IGNORECASE), "OOS"),
    (re.compile(r"\bquant(?:itative)?\b|量化", re.IGNORECASE), "Quant"),
    (re.compile(r"\b(?:thesis|host|recipe|profile|instance|claim|stage|gate)\b", re.IGNORECASE), "old strategy model"),
    (re.compile(r"\bsetup_stage\b", re.IGNORECASE), "setup_stage"),
    (re.compile(r"\bcomposite_recipe\b", re.IGNORECASE), "composite_recipe"),
    (re.compile(r"\bactive_tradeable\b", re.IGNORECASE), "active_tradeable"),
    (re.compile(r"\bartifact_[a-z0-9_]+\b", re.IGNORECASE), "artifact_*"),
    (re.compile(r"\bhost_artifact[a-z0-9_]*\b", re.IGNORECASE), "host_artifact"),
    (re.compile(r"\bopportunity_claim[a-z0-9_]*\b", re.IGNORECASE), "opportunity_claim"),
    (re.compile(r"\bstrategy_version[a-z0-9_]*\b", re.IGNORECASE), "strategy_version"),
    (re.compile(r"\b(?:thesis|stage|recipe|parity|evidence)_id\b", re.IGNORECASE), "machine ID"),
    (re.compile(r"\brecord_schema[a-z0-9_]*\b", re.IGNORECASE), "record_schema"),
    (re.compile(r"\bevent_type\b", re.IGNORECASE), "event_type"),
    (re.compile(r"\binstance_relation[a-z0-9_]*\b", re.IGNORECASE), "instance_relation"),
    (re.compile(r"\bHuman Profile\b|\bQuant Profile\b", re.IGNORECASE), "machine Profile"),
    (re.compile(r"\bCandidate\b|\bQualification\b|\bFreeze(?: gate)?\b", re.IGNORECASE), "machine lifecycle"),
    (re.compile(r"\bobject_type\b|\bdirection_policy\b|\bexclusive_group[a-z0-9_]*\b", re.IGNORECASE), "machine strategy field"),
    (re.compile(r"\bavailable_at\b|\breason_codes?\b|\bQ[123]\b", re.IGNORECASE), "machine research field"),
    (re.compile(r"程序字段|机器字段|字段契约|事件载荷|状态机|唯一键|派生视图|因果时钟"), "machine contract language"),
    (re.compile(r"样本外|部署|检测器|适配器|归约器"), "machine research language"),
)

STRATEGY_FAMILY_COUNTS = {
    "trend": 6,
    "breakout": 4,
    "range": 3,
    "breakout_mode": 1,
    "reversal": 5,
    "opening": 4,
}

STRATEGY_REQUIRED_SEMANTICS: dict[str, tuple[str, ...]] = {
    "交易的市场行为": ("市场行为", "交易逻辑", "交易命题"),
    "适用环境": ("适用环境", "适合什么", "适合的市场"),
    "不适用环境": ("不适用", "不适合", "不要交易"),
    "事先准备": ("事先", "开始观察前", "开始前写清", "预先画", "预先写"),
    "机会形成": ("机会怎样", "机会形成", "开始关注", "形成过程"),
    "条件完整": ("条件成立", "条件完整", "确认条件", "准备交易"),
    "入场": ("入场",),
    "未成交撤单": ("撤单", "未成交"),
    "保护止损": ("保护止损",),
    "目标": ("目标",),
    "仓位": ("仓位", "数量", "风险"),
    "管理": ("管理",),
    "成交后的正常与失效判断": ("## 成交后的判断",),
    "平台或订单风险": ("平台", "订单风险", "执行风险"),
    "结束后重新判断": (
        "## 原计划结束后",
        "重新判断",
        "重新评估",
        "结束旧计划",
        "重新按",
        "另按",
    ),
    "多空镜像": ("镜像", "做多和做空", "多头和空头"),
    "常见误读": ("常见误读", "常见误判", "常见错误"),
    "正例": ("正例",),
    "反例": ("反例",),
    "边界案例": ("边界案例", "临界案例"),
    "复盘": ("复盘",),
    "学习来源": ("对应学习", "相关学习", "learning/"),
}

EXECUTION_REQUIRED_SEMANTICS: dict[str, dict[str, tuple[str, ...]]] = {
    "execution/README.md": {
        "执行手册入口": ("execution_manual.md", "执行手册"),
        "执行环境入口": ("execution_modes.md", "执行环境"),
        "执行记录入口": ("execution_and_review_record.md", "执行与复盘记录"),
    },
    "execution/execution_modes.md": {
        "历史回放": ("历史回放", "回放"),
        "模拟": ("模拟",),
        "实盘": ("实盘",),
        "隐藏未来": ("隐藏未来", "未知未来", "尚未发生"),
        "连续推进": ("连续", "继续位置", "接着上次"),
        "禁止挑图": (
            "不主动寻找",
            "不挑选",
            "不得挑选",
            "不选择漂亮",
            "跳到特定片段",
            "挑选对自己最有利",
        ),
    },
    "execution/execution_and_review_record.md": {
        "执行环境": ("执行环境", "执行方式"),
        "只追加": ("只追加", "按时间追加", "不得改写"),
        "事实与判断分开": ("事实", "判断"),
        "零候选记录": ("没有候选", "无候选", "零候选"),
        "拒绝过期未成交": ("拒绝", "放弃"),
        "过期": ("过期",),
        "未成交": ("未成交",),
        "策略复盘": ("策略", "复盘"),
        "计划复盘": ("计划",),
        "订单与执行安全": ("订单", "执行安全"),
        "保护": ("保护",),
        "市场结果": ("市场结果", "市场后来"),
        "下一次唯一重点": ("下一次", "一个流程问题", "唯一重点"),
    },
    "execution/execution_manual.md": {
        "开始前检查": ("开始前",),
        "价格触发不等于成交": ("价格触发", "触发条件"),
        "订单请求": ("发出订单", "提交订单"),
        "平台收到": ("平台收到", "平台已经收到"),
        "订单生效": ("订单生效", "可以成交"),
        "实际成交": ("实际成交", "真实成交"),
        "回执不明不得重试": ("无法确认", "不得重复", "停止重复"),
        "撤单仍可能成交": ("撤单", "仍可能成交"),
        "改单风险": ("改单",),
        "部分成交": ("部分成交",),
        "真实仓位": ("真实仓位",),
        "保护持仓": ("保护止损", "保护真实持仓"),
        "双向联动风险": ("二选一", "联动单", "OCO"),
        "平台核对": ("平台核对", "核对平台", "核对账户", "重新对账"),
        "异常处理": ("异常",),
        "关闭条件": ("仓位为零", "仓位归零"),
    },
}

# These phrases preserve decisions whose absence previously made two careful
# human traders take different actions from the same page.  They are intentionally
# narrow: the checker protects the resolved boundary, not the prose around it.
CRITICAL_HUMAN_EXECUTION_TEXT: dict[str, tuple[str, ...]] = {
    "execution/execution_manual.md": (
        "本轮所见页面证据",
        "原轮次记录和原机会页",
        "不得为同一风险建立新轮次",
    ),
    "execution/execution_and_review_record.md": (
        "本轮所见策略页面证据",
        "阶段性截点后的恢复核对",
        "不新建另一轮或复制机会页",
    ),
    "strategy/breakout_mode/ii_bidirectional_breakout.md": (
        "原子二选一组合",
        "单一组合确认",
        "不能用两张独立订单拼成双向计划",
        "过期计数只能从单一组合有效确认开始",
    ),
    "strategy/opening/README.md": (
        "严格早于",
        "订单到截止时点才确认有效，都已经太晚",
    ),
    "strategy/opening/opening_previous_extreme_reversal.md": (
        "首次测试参照 K 线",
        "订单到六十分钟截止时点仍未确认有效",
    ),
    "strategy/opening/opening_trend_first_pullback.md": (
        "顺势信号与入场单有效确认",
        "订单到六十分钟截止时点仍未确认有效",
    ),
    "strategy/opening/opening_range_breakout.md": (
        "跟进 K 线的收盘时间严格早于",
        "订单到九十分钟截止时点仍未确认有效",
    ),
    "strategy/opening/late_session_open_magnet.md": (
        "强制退出缓冲时点",
        "正常收盘前一个完整观察周期",
        "只减仓或平仓",
        "竞态成交",
        "正常收盘时仓位仍未确认归零，属于执行异常",
    ),
}

CRITICAL_FORBIDDEN_TEXT: dict[str, tuple[str, ...]] = {
    "execution/execution_manual.md": ("修订日期",),
    "execution/execution_modes.md": ("策略修订日期",),
    "execution/execution_and_review_record.md": ("策略页面修订日期",),
    "strategy/breakout_mode/ii_bidirectional_breakout.md": ("较晚的有效确认时间",),
    "strategy/opening/opening_previous_extreme_reversal.md": (
        "以首次越界 K 线为参照",
    ),
    "strategy/opening/late_session_open_magnet.md": (
        "最后一根完整决策 K 线收盘时",
    ),
}


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
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        parts = path.relative_to(ROOT).parts
        if ".git" in parts:
            continue
        item = path.relative_to(ROOT).as_posix()
        if any(item == old or item.startswith(f"{old}/") for old in FORBIDDEN_PATHS):
            continue
        files.append(path)
    return sorted(files)


def visible_human_text(text: str) -> str:
    """Keep link labels while hiding path/URL implementation details."""

    def hide_target(match: re.Match[str]) -> str:
        label = match.group(1)
        return label + " " * (len(match.group(0)) - len(label))

    return VISIBLE_LINK_RE.sub(hide_target, text)


def local_target(source: Path, raw: str) -> tuple[Path, str] | None:
    raw = raw.strip().strip("<>")
    if raw.startswith(("http://", "https://", "mailto:")):
        return None
    path_part, _, fragment = raw.partition("#")
    target = source if not path_part else (source.parent / unquote(path_part)).resolve()
    if target.is_dir():
        target = target / "README.md"
    return target, unquote(fragment).lower()


def discover_strategy_pages(errors: list[str]) -> dict[str, list[Path]]:
    strategy_root = ROOT / "strategy"
    discovered: dict[str, list[Path]] = {}
    for family, expected_count in STRATEGY_FAMILY_COUNTS.items():
        family_root = strategy_root / family
        if not family_root.is_dir():
            errors.append(f"missing strategy family directory: strategy/{family}")
            discovered[family] = []
            continue
        nested = sorted(path for path in family_root.iterdir() if path.is_dir())
        if nested:
            errors.append(
                f"strategy/{family}: nested directories are not allowed: "
                f"{[path.name for path in nested]}"
            )
        pages = sorted(
            path
            for path in family_root.glob("*.md")
            if path.name != "README.md"
        )
        discovered[family] = pages
        if len(pages) != expected_count:
            errors.append(
                f"strategy/{family}: expected {expected_count} strategy pages "
                f"excluding README.md, found {len(pages)}"
            )
    total = sum(len(pages) for pages in discovered.values())
    if total != 23:
        errors.append(f"strategy: expected 23 natural-language strategy pages, found {total}")
    return discovered


def check_structure(errors: list[str]) -> dict[str, list[Path]]:
    for item in sorted(FIXED_REQUIRED_PATHS):
        if not (ROOT / item).is_file():
            errors.append(f"missing core document: {item}")

    for item in sorted(FORBIDDEN_PATHS):
        if (ROOT / item).exists():
            errors.append(f"retired path must be deleted with no compatibility copy: {item}")

    root_markdown = sorted(path.name for path in ROOT.glob("*.md"))
    if root_markdown != ["README.md"]:
        errors.append(
            "repository root must contain only README.md as Markdown; "
            f"found={root_markdown}"
        )

    strategy_root = ROOT / "strategy"
    expected_strategy_root_files = {
        "README.md",
        "how_to_choose.md",
        "switching_after_failure.md",
    }
    if strategy_root.is_dir():
        actual = {path.name for path in strategy_root.glob("*.md")}
        if actual != expected_strategy_root_files:
            errors.append(
                "strategy root Markdown files must be exactly "
                f"{sorted(expected_strategy_root_files)}; found={sorted(actual)}"
            )
        actual_families = {path.name for path in strategy_root.iterdir() if path.is_dir()}
        expected_families = set(STRATEGY_FAMILY_COUNTS)
        if actual_families != expected_families:
            errors.append(
                "strategy family directories must be exactly "
                f"{sorted(expected_families)}; found={sorted(actual_families)}"
            )

    exact_directory_files = {
        "execution": {
            "README.md",
            "execution_manual.md",
            "execution_modes.md",
            "execution_and_review_record.md",
        },
        "reference": {
            "README.md",
            "glossary.md",
            "official_sources.md",
            "strategy_map.md",
        },
    }
    for directory, expected in exact_directory_files.items():
        root = ROOT / directory
        if not root.is_dir():
            continue
        actual = {path.name for path in root.glob("*.md")}
        if actual != expected:
            errors.append(
                f"{directory} Markdown files must be exactly {sorted(expected)}; "
                f"found={sorted(actual)}"
            )

    return discover_strategy_pages(errors)


def check_h1(files: list[Path], errors: list[str]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        h1_count = sum(len(match.group(1)) == 1 for match in HEADING_RE.finditer(text))
        if h1_count != 1:
            errors.append(f"{relative(path)}: expected exactly one H1, found {h1_count}")


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


def check_no_retired_language(files: list[Path], errors: list[str]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        item = relative(path)

        if OLD_STRATEGY_FILENAME_RE.match(path.name):
            errors.append(
                f"{item}: retired ID-based strategy filename is forbidden; "
                "use a natural-language descriptive filename"
            )

        old_id = OLD_STRATEGY_ID_RE.search(text)
        if old_id:
            errors.append(
                f"{item}:{line_number(text, old_id.start())}: retired strategy ID "
                f"{old_id.group(0)!r} is forbidden; use the natural-language name"
            )

        for token in sorted(FORBIDDEN_REFERENCE_TOKENS):
            offset = text.find(token)
            if offset >= 0:
                errors.append(
                    f"{item}:{line_number(text, offset)}: reference to retired path "
                    f"{token!r} is forbidden"
                )

        compatibility = COMPATIBILITY_RE.search(text)
        if compatibility:
            errors.append(
                f"{item}:{line_number(text, compatibility.start())}: compatibility "
                f"language {compatibility.group(0)!r} is forbidden"
            )

        for pattern, label in MACHINE_TERM_PATTERNS:
            match = pattern.search(text)
            if match:
                errors.append(
                    f"{item}:{line_number(text, match.start())}: retired machine term "
                    f"{match.group(0)!r} ({label}) is forbidden"
                )


def check_human_language(path: Path, errors: list[str]) -> None:
    raw_text = path.read_text(encoding="utf-8")
    text = visible_human_text(raw_text)
    item = relative(path)
    fenced = FENCED_CODE_RE.search(text)
    if fenced:
        errors.append(
            f"{item}:{line_number(text, fenced.start())}: human-facing documents "
            "must not use fenced code blocks"
        )
    snake = SNAKE_CASE_RE.search(text)
    if snake:
        errors.append(
            f"{item}:{line_number(text, snake.start())}: human-facing text must not "
            f"expose snake_case field {snake.group(0)!r}"
        )
    assignment = FIELD_ASSIGNMENT_RE.search(text)
    if assignment:
        errors.append(
            f"{item}:{line_number(text, assignment.start())}: human-facing text must "
            "not use machine field=value notation"
        )


def check_strategy_pages(
    families: dict[str, list[Path]], errors: list[str]
) -> set[Path]:
    pages = {path.resolve() for family in families.values() for path in family}
    learning_root = (ROOT / "learning").resolve()
    strategy_root = ROOT / "strategy"
    if strategy_root.is_dir():
        for document in sorted(strategy_root.rglob("*.md")):
            item = relative(document)
            if any(
                item == old or item.startswith(f"{old}/")
                for old in FORBIDDEN_PATHS
            ):
                continue
            check_human_language(document, errors)
    for page in sorted(pages):
        text = page.read_text(encoding="utf-8")
        item = relative(page)
        for label, alternatives in STRATEGY_REQUIRED_SEMANTICS.items():
            if not any(term in text for term in alternatives):
                errors.append(
                    f"{item}: strategy page lacks natural-language semantic "
                    f"{label!r}; expected one of {alternatives}"
                )

        learning_links = 0
        for raw in LINK_RE.findall(text):
            resolved = local_target(page, raw)
            if resolved is None:
                continue
            target, _ = resolved
            try:
                target.resolve().relative_to(learning_root)
                learning_links += 1
            except ValueError:
                pass
        if learning_links == 0:
            errors.append(f"{item}: strategy page must link to at least one learning topic")
    return pages


def direct_page_link_counts(index: Path, pages: set[Path]) -> Counter[Path]:
    counts: Counter[Path] = Counter()
    if not index.is_file():
        return counts
    text = index.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        resolved = local_target(index, raw)
        if resolved is None:
            continue
        target, _ = resolved
        target = target.resolve()
        if target in pages:
            counts[target] += 1
    return counts


def check_strategy_index_coverage(pages: set[Path], errors: list[str]) -> None:
    for item in ("strategy/README.md", "reference/strategy_map.md"):
        index = ROOT / item
        counts = direct_page_link_counts(index, pages)
        missing = sorted(relative(path) for path in pages if counts[path] == 0)
        if missing:
            errors.append(f"{item}: must directly link all 23 strategy pages; missing={missing}")


def check_execution_docs(errors: list[str]) -> None:
    execution_root = ROOT / "execution"
    for path in sorted(execution_root.glob("*.md")) if execution_root.is_dir() else []:
        check_human_language(path, errors)

    for item, required in EXECUTION_REQUIRED_SEMANTICS.items():
        path = ROOT / item
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for label, alternatives in required.items():
            if not any(term in text for term in alternatives):
                errors.append(
                    f"{item}: execution document lacks semantic {label!r}; "
                    f"expected one of {alternatives}"
                )


def check_critical_human_execution_text(errors: list[str]) -> None:
    for item, required_phrases in CRITICAL_HUMAN_EXECUTION_TEXT.items():
        path = ROOT / item
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(
                    f"{item}: resolved human-execution boundary is missing "
                    f"required wording {phrase!r}"
                )

    for item, forbidden_phrases in CRITICAL_FORBIDDEN_TEXT.items():
        path = ROOT / item
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in forbidden_phrases:
            if phrase in text:
                errors.append(
                    f"{item}: obsolete ambiguous wording {phrase!r} must not return"
                )


def check_learning_dependencies(files: list[Path], errors: list[str]) -> None:
    learning_root = (ROOT / "learning").resolve()
    learning_navigation = (ROOT / "learning/README.md").resolve()
    forbidden_roots = ((ROOT / "strategy").resolve(), (ROOT / "execution").resolve())
    for source in files:
        try:
            source.resolve().relative_to(learning_root)
        except ValueError:
            continue
        if source.resolve() == learning_navigation:
            continue
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            resolved = local_target(source, match.group(1))
            if resolved is None:
                continue
            target, _ = resolved
            target = target.resolve()
            if any(root == target or root in target.parents for root in forbidden_roots):
                try:
                    target_label = relative(target)
                except ValueError:
                    target_label = str(target)
                errors.append(
                    f"{relative(source)}:{line_number(text, match.start())}: learning "
                    "topics must explain the concept without depending on strategy or "
                    f"execution documents ({target_label})"
                )


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
    registry = registry_path.read_text(encoding="utf-8")
    registered = registered_source_ids(registry, errors)
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
    families = check_structure(errors)
    files = markdown_files()
    check_h1(files, errors)
    check_links(files, errors)
    check_no_retired_language(files, errors)
    pages = check_strategy_pages(families, errors)
    check_strategy_index_coverage(pages, errors)
    check_execution_docs(errors)
    check_critical_human_execution_text(errors)
    check_learning_dependencies(files, errors)
    check_source_ids(files, errors)

    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Documentation checks passed: "
        f"{len(files)} Markdown files and {len(pages)} strategy pages validated."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
