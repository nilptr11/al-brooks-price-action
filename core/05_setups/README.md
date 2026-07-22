# 交易命题（Setups）

> **状态：Core / Index**
>
> 本页说明不可直接执行的 Setup 原型及其文件入口，不把示例家族宣称为穷尽分类。

首次学习时，进入本目录前应已按编号完整读完 `core/00_method` 至 `core/04_patterns`；进入后按 `00`–`04` 顺序读完本目录全部正文。下列家族用于比较不同命题，不是选读菜单。

## 职责

本目录负责说明 Pattern 何时在具体 Context 中成为可被策略实例化的抽象交易命题，并比较几类常见价格行为预期。

Setup 原型负责 premise、抽象触发类别、特有失效边界、stop 所需否定的结构和直接结果预期。它不提供可直接下单的完整条件，也不确定最终订单价格、根数窗口、仓位或成交后管理；这些实例化规则属于[策略手册](../../strategy/README.md)。通用目标理论属于 [Context](../02_context/01_support_resistance_targets.md)，概率约束属于 [Trader's Equation](../00_method/01_probability_risk_reward.md)，计划 schema 属于 [Trade Plan](../06_trade_plan_and_management/00_trade_plan.md)。

Second entry 和 trap 是触发顺序与失败机制，不是第五个 Setup 家族；其定义见[二次入场和陷阱](../03_acceptance_and_order_logic/03_second_entries_and_traps.md)。

## Setup 家族

| 家族 | 核心命题 | 典型结果 |
| --- | --- | --- |
| 趋势延续 | 回调没有破坏原控制，趋势方恢复 | 测试旧极值或继续原趋势 |
| 突破延续 | 市场接受旧边界外的新价格 | 突破继续、第二腿或清楚结构的 measured move |
| 交易区间 fade | 边缘突破未被接受，价格恢复区间内轮动 | 回到区间内部价值区域 |
| MTR | 原趋势失去控制，旧极值测试失败，反方建立 swing | 反向两腿或较大 trading range |

表中结果只说明各命题的差异，不替代现实 target、reasonable stop 或 Trader's Equation。

## 文件

1. [`00_what_is_a_setup.md`](00_what_is_a_setup.md)：Setup 的最低定义，以及 Pattern 与 Trade Plan 的边界。
2. [`01_trend_continuation.md`](01_trend_continuation.md)：趋势恢复。
3. [`02_breakout_continuation.md`](02_breakout_continuation.md)：新价格获得接受后的延续。
4. [`03_trading_range_fade.md`](03_trading_range_fade.md)：区间边缘失败后的回归。
5. [`04_major_trend_reversal.md`](04_major_trend_reversal.md)：完整 MTR 过程。

形态术语见[形态语言](../04_patterns/README.md)，概念总图见[核心框架](../README.md)。
