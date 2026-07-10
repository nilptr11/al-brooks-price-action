# 入场、止损和目标

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../README.md#权威层级)。

## 入场

入场方式应匹配市场环境：

- 强趋势和强突破更适合 stop entry。
- 交易区间边缘和弱通道更可能适合 limit entry。
- 强趋势中的特殊情境可能出现 Buy The Close / Sell The Close。

入场不是交易的核心，完整交易想法才是核心。

## Protective Stop

Protective stop 把交易命题的 invalidation 转换成有限损失的订单。它不同于 stop entry；invalidation 是可观察的市场事实，protective stop 是结构外的订单价格。

从图表到真实风险至少有四层：命题失效事实、结构锚点、经纪商 stop 触发价，以及计入预计滑点后的保守成交价。滑点影响风险估计，不负责决定结构锚点。

止损太近可能被正常波动扫出，止损太远可能让风险回报失衡。好的止损是结构、目标和概率共同作用的结果。

常见止损管理要分清：

- Signal-bar stop：放在 signal bar 外侧，常见于 stop entry 或反转触发，风险清楚但可能太近。
- Structure stop：放在回调、失败突破、回踩或反转结构外侧，更直接对应交易想法的失效点。
- Wide stop / scaling-in：用更远止损和加仓换取更高存活率，必须降低仓位并预先限定最大风险。

同一图表可能同时存在两三个合理 stop。例如趋势回调可以使用 signal-bar stop，也可以使用完整 pullback / swing stop。它们不是可以自由拼接的“备用价格”：每个 stop 都会改变风险距离、仓位、目标空间、概率和管理方式，必须作为不同交易方案分别评估。

止损不能为了凑出好看的 R 倍数而放在正常波动范围内。如果合理结构止损太远，通常说明入场位置不好或这笔交易不该做。

每个交易方案在入场前都必须选定一个初始 protective stop，并让它从首个成交起生效。成交后不得为了挽救交易而放宽；向保护方向 trailing 需要新的有效 higher low / lower high 等结构，breakeven 不是机械动作。

Protective stop 只是最终保护。若出现足以否定原命题的反向信号、强反向 breakout 或其他预写退出条件，可以在 stop 触发前退出；这不等于可以只使用 mental stop。

## Targets

目标应在入场前就有依据。常见目标包括：

- 前高和前低。
- 区间中轴或另一侧边缘。
- 突破点回探。
- 量度目标。
- 大周期支撑阻力。
- 强趋势中的跟踪目标。

目标不是保证，而是评估风险回报的基础。

目标分析要区分三件事：路径上的支撑阻力、市场结构形成的目标区域，以及实际挂单和 Trader's Equation 使用的保守退出价。明显障碍会降低到达更远目标的概率，但并不自动要求全部退出；若计划要穿越它，必须有足够的趋势或突破证据。

目标也有优先级。先看最近、明显、现实的近端目标，再评估 measured move 或更远 swing 目标。若近端目标已经压缩空间，不能用远端目标强行证明交易值得做。

Measured move 不是每笔计划的必需项目。存在清晰测量结构时，它可以来自 Leg 1 = Leg 2、交易区间/形态高度或 breakout height；特定结构也可使用日内 gap 作为运动中间参照。每次使用都必须能说清参照结构和投射起点；它如果确实是从当前 entry 出发遇到的第一现实目标，可以直接进入初始 Trader's Equation，不应因名称被机械降为远端目标。

最常见的构造是：第一腿 `A -> B`、第二腿从 `C` 开始，则目标为 `C + (B - A)`；区间高度为 `H` 时，向上突破投射到上边界加 `H`，向下突破投射到下边界减 `H`。Breakout height 和 gap 投射也必须先固定可见端点，不能在事后从 close、high/low 或不同 K 线中挑最符合结果的一组。

Measuring gap 只有事后才能确认。实时只能把仍开放、且得到 follow-through 支持的 gap 当作候选延续证据；若更像趋势末端 exhaustion，就不能把同一 gap 当成保证到达的目标。

第一现实目标必须进入初始 Trader's Equation。更远的 measured move、延伸目标或 runner 只有在趋势、突破接受或反向 swing 证据支持时才启用；部分退出按仓位比例计算。TBTL 不是价格目标。

## 风险与仓位

官方 glossary 用 entry 到 protective stop 的距离描述 risk，并提醒滑点等会让实际成交损失偏离理论值。完整计划应使用保守 entry 与 stop 成交价计算价格风险，再乘以仓位，并只加入尚未嵌入这些价格的手续费、点差和滑点。

市场在入场后出现一个更远的结构，不构成放宽 stop 的许可。若原交易命题失效，应按原计划退出并重新建立候选；若预写的目标、提前退出或结构 trailing 条件成立，则按管理合同减仓、退出或推进 stop。没有事件时维持原计划，不逐根重新计算。

来源审计见 `reference/official_sources.md` 中的 `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE`、`SRC-RISK-113`、`SRC-BREAKOUTS-2025`、`SRC-LIVE-TR-BO-2021`、`SRC-GOOD-TRADE-2017`。
