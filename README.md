# Brooks 价格行为文档

本仓库整理 Brooks 价格行为的执行规则、术语参考、学习材料、训练场景和研究审计。它不是自动信号系统、回测报告或对特定市场的交易建议。

## 权威层级

| 层级 | 文件或目录 | 职责 | 是否规范执行 |
| --- | --- | --- | --- |
| 执行 | [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) | 入场、无效点、止损、目标、仓位、Trader's Equation、管理和退出 | 是，仓库内唯一执行权威 |
| 来源 | [`reference/official_sources.md`](reference/official_sources.md) | 官方来源 ID、URL 和原文锚点登记 | 否，只负责证据定位 |
| 审计 | [`reference/audit_matrix.md`](reference/audit_matrix.md) | 结论性质、覆盖文件、核对状态和下一步 | 否，负责证明和校准 |
| 查阅 | [`reference/glossary.md`](reference/glossary.md) | 术语快速解释 | 否 |
| 学习 | `00_method/` 至 `06_trade_management/` | 概念、背景、推导和常见误读 | 否 |
| 训练 | [`07_scenarios/`](07_scenarios/README.md) | 场景、逐根模板、管理示例和复盘清单 | 否 |
| 图谱 | `al-brooks-pattern-atlas.html`、[`reference/audits/pattern_atlas.md`](reference/audits/pattern_atlas.md) | 视觉索引及其来源、几何审计 | 否 |
| 研究 | `synthesis/` | 概念归并和未定结论 | 否 |

“执行权威”不等于“Brooks 官方原文”。执行手册包含仓库自己的 M/K/C/T/D/Q/P 路由、人的订单/成交边界、管理合同和保守执行政策；G1–G3 是 D 内的管理配置，不是独立状态层。官方资料是证据权威，用来审计和修正这些政策。若学习文档与执行手册冲突，执行时以执行手册为准，同时在审计矩阵中记录并校准差异。

## 快速入口

- 实盘前或复盘一笔交易：先看 [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md)。
- 查术语：看 [`reference/glossary.md`](reference/glossary.md)。
- 判断某条结论是否核对过官方资料：看 [`reference/audit_matrix.md`](reference/audit_matrix.md)。
- 系统学习：按 `00_method/` 至 `06_trade_management/` 的编号顺序阅读。
- 做场景训练：使用 `07_scenarios/`，逐笔复盘从 [`07_scenarios/05_review_checklist.md`](07_scenarios/05_review_checklist.md) 开始。
- 查看 88 图形：打开 `al-brooks-pattern-atlas.html`；来源与几何审计见 [`reference/audits/pattern_atlas.md`](reference/audits/pattern_atlas.md)。

## 学习路线

1. `00_method/`：Brooks 方法、阅读顺序、概率和风险回报。
2. `01_market_cycle/`：先分 trend / trading range，再学习 breakout / tight channel / broad channel 连续谱，以及 breakout mode、climactic behavior 等阶段信息。
3. `02_context/`：Always In、控制权、位置、目标、多周期和时段。
4. `03_order_flow/`：订单触发、跟进、失败和被困交易者。
5. `04_setups/`：趋势延续、突破、区间回归和 Major Trend Reversal。
6. `05_patterns/`：把 H/L、楔形、双顶底、最终旗形、三角形和缺口当成语言。
7. `06_trade_management/`：入场、止损、目标、scalp/swing、TBTL、加减仓和心理纪律。
8. `07_scenarios/`：开盘、缺口、交易日类型和逐根训练。

## 官方资料校准流程

```text
登记官方来源
-> 为待核结论建立来源锚点
-> 区分官方结论 / 我们的推导 / 内部执行政策
-> 官方概念或解释变化：
   更新 glossary、受影响的学习文档或图谱；
   只有执行输入或政策确实改变时才更新执行手册
-> 内部执行流程或政策变化：
   先更新执行手册；
   只同步直接依赖该字段、状态或规则的训练、审计和必要研究文档
-> 更新审计状态与日期
```

官方内容只保存精炼转述、URL、页码或 slide 锚点和必要的短引文；不在仓库复制受版权保护的课程、书籍或大段原文。

## 文档边界

- 不把任何形态写成脱离 context、location、follow-through 和 Trader's Equation 的自动信号。
- 学习文档可以保留解释和例子，但不得另立执行规则，也不得使用执行手册的内部流程编号和字段。
- `M/K/C/T/D/Q/P`、`G1–G3`、`PT1/PT2`、`MaxLoss`、`PlannedLoss` 等内部简称只属于执行手册；训练、审计和研究文档可以明确地作为当前流程派生物引用。成交后使用自然语言记录实际触发的管理事件，不另设持仓状态编号。
- 学习文档统一通过本 README 的权威层级进入执行层，不直接绑定执行手册文件名。
- 未核对来源的内容必须在审计矩阵中标为“待核对”或“内部执行政策”，不得笼统声称来自官方。

这样控制变更传播：

- 仅重命名执行编号、字段或重排执行手册章节：修改执行手册、直接引用该记法的 `07_scenarios/`、对应审计行，以及确实复述该流程的 `synthesis/`；不改 `00_method/`–`06_trade_management/`、glossary、来源台账或图谱。
- Brooks 概念或官方解释变化：修改 glossary 和实际受影响的学习文档、图谱或来源审计；只有它改变执行输入或内部政策时才修改执行手册。
- 仅增补来源 URL、页码或 slide 锚点：修改来源台账及相关审计行，不向正文传播。
