# Brooks Price Action 核心框架

> **状态：Core / Index**
>
> 本页说明核心概念之间的关系和各专题的职责，不提供机械交易规则。

## 定位

本目录提炼 Al Brooks Price Action 的核心理念：市场如何在 trend 与 trading range 之间转换、trend 如何以形成方向控制的 breakout phase / spike 或 channel 发展，以及交易者如何结合 context、接受与订单逻辑和交易数学构造并持续复核一笔交易。

它不是可以选择性抽取几个专题的形态百科或策略清单。首次学习必须按目录和文件编号完成全部内容；交叉链接只帮助复核依赖关系，不能代替被链接专题的完整阅读。七个目录共同构成同一套判断体系，不能用其中一个专题、一个 README 或一组常用形态代替对整体框架的理解。

Core 与 01–52 官方课程的逐章、逐页职责对照见[课程综合与 Core 对齐](../reference/course/course_to_core_alignment.md)。该文档用于追溯课程证据和发现遗漏，不构成另一套核心框架，也不能代替本目录正文。

## 核心关系

```text
Market Cycle
    ↓
Context、Location 与 Control
    ↓
Pattern 描述价格行为
    ↓
Setup 把 context 与入场依据组合起来
    ↓
Trade Plan 固化 premise、entry、stop、target、仓位与 management

Acceptance / Failure 用于持续复核结果
Trader's Equation 约束所有承担新风险的决定
```

Pattern 不是自动信号，Setup 不是完整交易，Trade Plan 也不是入场后不再更新的剧本。三者的职责边界分别由对应权威页面定义。

## 完整必读顺序

首次学习只有以下一条完整顺序。进入每个目录时先读该目录的 `README.md`，再按编号读完该目录的全部正文；以下 31 个正文文件全部必读，没有“主线页”与“选读页”之分：

1. [方法论](00_method/README.md)
   1. [方法与读图主线](00_method/00_al_brooks_thesis.md)
   2. [概率、风险和回报](00_method/01_probability_risk_reward.md)
2. [市场周期](01_market_cycle/README.md)
   1. [市场周期的基础层级](01_market_cycle/00_market_cycle.md)
   2. [趋势和通道](01_market_cycle/01_trends_and_channels.md)
   3. [交易区间](01_market_cycle/02_trading_ranges.md)
   4. [突破和突破模式](01_market_cycle/03_breakouts_and_breakout_mode.md)
   5. [高潮和状态转换](01_market_cycle/04_climax_and_transition.md)
3. [Context](02_context/README.md)
   1. [背景、位置和控制权](02_context/00_context_location_control.md)
   2. [支撑阻力与目标](02_context/01_support_resistance_targets.md)
   3. [周期与时段 Context](02_context/02_time_and_timeframes.md)
4. [接受、失败与订单逻辑](03_acceptance_and_order_logic/README.md)
   1. [Stop 入场与保护性 Stop](03_acceptance_and_order_logic/00_stop_entry_vs_protective_stop.md)
   2. [接受、失望与失败证据](03_acceptance_and_order_logic/01_acceptance_and_failure.md)
   3. [限价单市场](03_acceptance_and_order_logic/02_limit_order_market.md)
   4. [二次入场和陷阱](03_acceptance_and_order_logic/03_second_entries_and_traps.md)
5. [形态语言](04_patterns/README.md)
   1. [形态只是语言](04_patterns/00_patterns_are_language.md)
   2. [K 线类型](04_patterns/01_bar_types.md)
   3. [H1、H2、L1、L2](04_patterns/02_h1_h2_l1_l2.md)
   4. [楔形](04_patterns/03_wedges.md)
   5. [双顶、双底和旗形变体](04_patterns/04_double_tops_bottoms.md)
   6. [最终旗形](04_patterns/05_final_flags.md)
   7. [Triangles、ii、ioi 和 oo](04_patterns/06_triangles_ii_ioi_oo.md)
   8. [缺口](04_patterns/07_gaps.md)
6. [交易命题](05_setups/README.md)
   1. [什么是 Setup](05_setups/00_what_is_a_setup.md)
   2. [趋势延续 Setup](05_setups/01_trend_continuation.md)
   3. [突破延续 Setup](05_setups/02_breakout_continuation.md)
   4. [交易区间 Fade Setup](05_setups/03_trading_range_fade.md)
   5. [主要趋势反转](05_setups/04_major_trend_reversal.md)
7. [交易计划与管理](06_trade_plan_and_management/README.md)
   1. [从 Setup 到交易计划](06_trade_plan_and_management/00_trade_plan.md)
   2. [Scalp 与 Swing](06_trade_plan_and_management/01_scalp_vs_swing.md)
   3. [加仓与减仓](06_trade_plan_and_management/02_scaling_in_out.md)
   4. [风险与心理纪律](06_trade_plan_and_management/03_risk_psychology.md)

部分概念会在后续目录获得更完整的语言，例如前文使用的 signal bar、follow-through 或 Pattern。首次学习仍按上列顺序继续读完；完成全部内容后，再沿交叉链接复核概念关系，不通过跳页把循环依赖改成选择性阅读。

## Definition 权威注册表

本表覆盖每一个标记为 `Core / Definition` 的正文文件。一个最低定义只能归属其中一页；其他页面可以保留必要摘要和本地应用，但必须链接到这里登记的权威页。

| 权威主题 | 权威页面 | 该页负责什么 |
| --- | --- | --- |
| Brooks 方法主线 | [方法与读图主线](00_method/00_al_brooks_thesis.md) | 连接市场状态、背景、交易机会和交易数学 |
| Trader's Equation / Probability Language | [概率、风险和回报](00_method/01_probability_risk_reward.md) | 定义概率、风险、回报属于同一交易方案及 likely / risky 等措辞边界 |
| Market Cycle | [市场周期](01_market_cycle/00_market_cycle.md) | 定义 trend / trading range 基础状态与 breakout phase / channel 层级；接受状态是仓库整理口径 |
| Trend / Channel / Pullback / Leg | [趋势和通道](01_market_cycle/01_trends_and_channels.md) | 定义趋势、通道、回调、腿和连续谱线索 |
| Trading Range | [交易区间](01_market_cycle/02_trading_ranges.md) | 定义交易区间、紧区间、宽区间和双边行为 |
| Breakout Event / Test / Mode | [突破和突破模式](01_market_cycle/03_breakouts_and_breakout_mode.md) | 定义越界事件、接受/失败、回测和双向候选状态 |
| Climax / Transition | [高潮和状态转换](01_market_cycle/04_climax_and_transition.md) | 区分高潮式推进、事后确认的 climax 和状态转换线索 |
| Context | [背景、位置与控制](02_context/00_context_location_control.md) | 定义 location、control、Always In 和路径空间 |
| Support / Resistance / Target | [支撑阻力与目标](02_context/01_support_resistance_targets.md) | 定义区域、magnets、路径障碍和 measured move |
| Timeframe / Session / Opening | [周期与时段 Context](02_context/02_time_and_timeframes.md) | 定义周期分工、实时 session state 与开盘概念 |
| Stop Entry / Protective Stop | [两类 Stop](03_acceptance_and_order_logic/00_stop_entry_vs_protective_stop.md) | 定义入场触发与持仓保护的不同用途 |
| Acceptance / Failure | [接受、失望与失败证据](03_acceptance_and_order_logic/01_acceptance_and_failure.md) | 区分跟进、失望、premise 变化、trade failure 和 trapped traders |
| Limit Entry / LOM / Fade / Countertrend | [限价单市场](03_acceptance_and_order_logic/02_limit_order_market.md) | 定义限价成交边界、逆向限价行为环境及 fade / countertrend 区别 |
| Second Signal / Second Entry / Trap | [二次入场和陷阱](03_acceptance_and_order_logic/03_second_entries_and_traps.md) | 区分候选触发顺序、实际入场顺序和失败压力 |
| Pattern | [形态只是语言](04_patterns/00_patterns_are_language.md) | 定义形态语言及其与 Setup 的边界 |
| Bar Types / Bar Roles | [K 线类型](04_patterns/01_bar_types.md) | 定义 K 线几何、signal bar、entry bar 及其成立时点 |
| H1 / H2 / L1 / L2 | [H1、H2、L1、L2](04_patterns/02_h1_h2_l1_l2.md) | 定义回调中的触发尝试计数 |
| Wedge / Parabolic Wedge | [楔形](04_patterns/03_wedges.md) | 定义三推结构及其顺势、逆势和高潮语境 |
| Double Top / Double Bottom | [双顶、双底和旗形变体](04_patterns/04_double_tops_bottoms.md) | 定义双测试、旗形和微型变体 |
| Final Flag | [最终旗形](04_patterns/05_final_flags.md) | 定义任意趋势腿中的候选 flag、可小至一根，以及事后确认边界 |
| Triangle / ii / ioi / oo | [Triangles、ii、ioi 和 oo](04_patterns/06_triangles_ii_ioi_oo.md) | 定义三角形与压缩、扩张的 K 线结构 |
| Gap Family | [缺口](04_patterns/07_gaps.md) | 定义 opening、body、micro measuring、measuring 和 exhaustion gap |
| Setup | [什么是 Setup](05_setups/00_what_is_a_setup.md) | 定义带 context 的 premise、触发、失效和分类边界 |
| Trade Plan | [从 Setup 到交易计划](06_trade_plan_and_management/00_trade_plan.md) | 定义一笔完整交易必须保持一致的组成部分 |
| Scalp / Swing / TBTL | [Scalp 与 Swing](06_trade_plan_and_management/01_scalp_vs_swing.md) | 定义管理方式和时间/腿数预期 |
| Scaling In / Scaling Out | [加仓与减仓](06_trade_plan_and_management/02_scaling_in_out.md) | 定义数量变化怎样改变整笔交易的总风险和管理 |

`Core / Application` 页面不进入本注册表，因为它们只能应用上述定义，不能建立新的最低边界。若 Application 页面需要定义新术语，必须先调整其状态与权威归属。

## 状态标签

- **Index**：只负责入口、阅读路径和职责导航，不另立概念定义。
- **Definition**：某个概念的最低边界或权威定义；同一概念只能有一个完整定义位置。
- **Application**：把已有定义用于特定语境，可以说明本地影响，但必须链接权威页，不能重定义最低边界。

## 目录职责

| 目录 | 职责 | 不负责 |
| --- | --- | --- |
| [`00_method/`](00_method/README.md) | Brooks 方法主线与 Trader's Equation | 罗列具体形态或策略 |
| [`01_market_cycle/`](01_market_cycle/README.md) | 市场基础状态及其转换 | 把市场状态直接变成入场许可 |
| [`02_context/`](02_context/README.md) | 位置、控制权、支撑阻力、目标空间、周期与时段 | 定义订单触发和成交结果 |
| [`03_acceptance_and_order_logic/`](03_acceptance_and_order_logic/README.md) | Stop/limit order 用途、触发顺序、接受、失败与 trapped traders | 猜测真实订单簿身份或生成独立 Setup 家族 |
| [`04_patterns/`](04_patterns/README.md) | Brooks 形态与 K 线语言的最低边界 | 脱离 context 给出交易结论 |
| [`05_setups/`](05_setups/README.md) | 比较不可直接执行的 Setup 原型、抽象触发类别、特有失效边界和结果预期 | 给出仓库策略的具体订单、价格、根数窗口或完整管理 |
| [`06_trade_plan_and_management/`](06_trade_plan_and_management/README.md) | 定义 Trade Plan schema、通用管理原则、数量风险和行为纪律 | 实例化某项策略，或重新定义上游形态和市场状态 |

## 整体理解要求

七个目录是同一条决策链的不同职责，不是可以互相替代的独立模块。完整理解必须覆盖方法论、Market Cycle、Context、接受与订单逻辑、Pattern、Setup 和交易计划与管理，并能够说明它们怎样共同约束一笔交易。

本页的权威注册表和目录职责只用于确定概念由谁定义，不能据此删减理解范围。[核心术语表](../reference/glossary.md)只是从 Definition 页面派生的复核摘要，不能建立另一套最低边界，也不能代替核心框架及其概念关系。

## 与策略和执行的边界

本目录解释“市场行为怎样关联”，并定义 Setup 原型与 Trade Plan schema；这些页面都不能直接生成仓库订单。将原型实例化为带具体形成顺序、订单、价格、窗口和管理的计划，进入[策略手册](../strategy/README.md)；处理真实订单、成交安全和复盘记录，进入[执行手册](../execution/README.md)。

## 维护原则

- 一个概念只在一处给出完整定义；其他页面保留必要结论和本地应用，并链接权威页面。
- Core 文件只使用 Index、Definition 和 Application 三类状态标签，标签含义以本页为准。
- Pattern 页面描述语言，Setup 页面描述交易命题，Trade Plan 页面描述完整交易，三者不互相代写。
- 实时可观察事实与事后结果名称分开；例如 breakout attempt、candidate measuring gap 和已确认 trade failure 不能混用。
- 概率、根数、腿数和倍数都写明适用语境，不把典型经验改写成跨市场硬规则。
- 课程内容进入 Core 前先通过[课程综合与 Core 对齐](../reference/course/course_to_core_alignment.md)确定权威落点；同一思想只补到负责其最低边界的页面，不按课程讲次重复铺陈。
