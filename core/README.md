# Brooks Price Action 核心框架

> **状态：Core / Knowledge Map**
>
> 本页说明核心概念之间的关系和各专题的职责，不提供机械交易规则。

## 定位

本目录提炼 Al Brooks Price Action 的核心理念：市场如何在 trend、trading range、breakout 和 channel 之间转换，交易者如何结合 context、order flow 和交易数学构造并持续复核一笔交易。

它不是按章节推进的入门课程，也不是形态百科或策略清单。目录编号只用于稳定排列和主题分组，不代表严格阅读顺序；七个目录共同构成同一套判断体系，不能用其中一个专题代替对整体框架的理解。

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

## 权威定义归属

| 概念 | 权威页面 | 该页负责什么 |
| --- | --- | --- |
| Brooks 方法主线 | [方法与读图主线](00_method/00_al_brooks_thesis.md) | 连接市场状态、背景、交易机会和交易数学 |
| Trader's Equation | [概率、风险和回报](00_method/01_probability_risk_reward.md) | 定义概率、风险、回报属于同一交易方案 |
| Market Cycle | [Market Cycle](01_market_cycle/00_market_cycle.md) | 定义 trend / trading range 与 breakout / channel 层级 |
| Breakout / Breakout Mode | [突破和突破模式](01_market_cycle/03_breakouts_and_breakout_mode.md) | 定义越界事件、突破质量和双向候选状态 |
| Context | [背景、位置与控制](02_context/00_context_location_control.md) | 定义 location、control、Always In 和路径空间 |
| Support / Resistance / Target | [支撑阻力与目标](02_context/01_support_resistance_targets.md) | 定义目标区域、实际退出价格和 measured move |
| Acceptance / Failure | [接受、失望与失败证据](03_order_flow/00_acceptance_and_failure.md) | 区分跟进、失望、premise 变化和 trade failure |
| Stop Entry / Protective Stop | [两类 Stop](03_order_flow/01_stop_entry_vs_protective_stop.md) | 定义入场触发与持仓保护的不同用途 |
| Signal Bar / Entry Bar | [K 线类型](04_patterns/01_bar_types.md) | 定义 K 线角色及其成立时点 |
| Pattern | [形态只是语言](04_patterns/00_patterns_are_language.md) | 定义形态语言及其与 Setup 的边界 |
| Setup | [什么是 Setup](05_setups/00_what_is_a_setup.md) | 定义带 context 的入场依据及其分类边界 |
| Trade Plan | [从 Setup 到交易计划](06_trade_management/00_trade_plan.md) | 定义一笔完整交易必须保持一致的组成部分 |
| Scalp / Swing / TBTL | [Scalp 与 Swing](06_trade_management/01_scalp_vs_swing.md) | 定义管理方式和时间/腿数预期 |

其他页面可以概括这些结论并说明本页应用，但不重新给出另一套最低定义。

## 目录职责

| 目录 | 职责 | 不负责 |
| --- | --- | --- |
| [`00_method/`](00_method/README.md) | Brooks 方法主线与 Trader's Equation | 罗列具体形态或策略 |
| [`01_market_cycle/`](01_market_cycle/README.md) | 市场基础状态及其转换 | 把市场状态直接变成入场许可 |
| [`02_context/`](02_context/README.md) | 位置、控制权、支撑阻力、目标空间、周期与时段 | 定义订单触发和成交结果 |
| [`03_order_flow/`](03_order_flow/README.md) | 接受、失败、订单用途、二次触发与 trapped traders | 生成独立的 Setup 家族 |
| [`04_patterns/`](04_patterns/README.md) | Brooks 形态与 K 线语言的最低边界 | 脱离 context 给出交易结论 |
| [`05_setups/`](05_setups/README.md) | 比较延续、突破、区间和 MTR 等交易命题 | 重复完整交易计划和通用目标理论 |
| [`06_trade_management/`](06_trade_management/README.md) | 把 Setup、风险、目标、仓位和管理组成同一方案 | 重新定义上游形态或市场状态 |

## 整体理解要求

七个目录是同一条决策链的不同职责，不是可以互相替代的独立模块。完整理解必须覆盖方法论、Market Cycle、Context、Order Flow、Pattern、Setup 和 Trade Management，并能够说明它们怎样共同约束一笔交易。

本页的权威定义归属和目录职责只用于确定概念由谁定义，不能据此删减理解范围。跨专题术语的最低边界见[核心术语表](../reference/glossary.md)；术语表只能用于复核，不能代替核心框架及其概念关系。

## 与策略和执行的边界

本目录解释“市场行为怎样关联”。将这些概念落成可选择的交易条件，进入[策略手册](../strategy/README.md)；处理真实订单、成交安全和复盘记录，进入[执行手册](../execution/README.md)。

## 维护原则

- 一个概念只在一处给出完整定义；其他页面保留必要结论和本地应用，并链接权威页面。
- Pattern 页面描述语言，Setup 页面描述交易命题，Trade Plan 页面描述完整交易，三者不互相代写。
- 实时可观察事实与事后结果名称分开；例如 breakout attempt、candidate measuring gap 和已确认 trade failure 不能混用。
- 概率、根数、腿数和倍数都写明适用语境，不把典型经验改写成跨市场硬规则。
