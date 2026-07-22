# 什么是 Setup

> **状态：Core / Definition**
>
> 本文是 Setup 的权威定义页，只界定交易命题及其与 Pattern、Trade Plan 的边界。

本目录中的 Setup 家族页是不可直接执行的原型。它们说明某类价格行为为何可能成为入场依据；只有[策略手册](../../strategy/README.md)把原型实例化为完整形成顺序、订单、具体价格、有效窗口和管理后，才形成仓库可执行计划。

## Setup 的定义

Setup 是处在具体 Context 中、可以作为放置入场单依据的一组价格行为。它至少包含：

- 当前 market cycle、location 与控制权背景。
- 准备交易的价格行为命题，即 premise。
- 支持该命题的一根或多根 K 线或 pattern。
- 明确方向和可观察的入场触发条件。
- 哪些可观察事实会使 premise 失效，以及该命题直接期待哪类价格运动。

一项实际 Setup 必须有明确触发；本目录的家族原型只规定应回答的触发类别和结构关系，不替具体机会填写 K 线顺序、订单价格或有效期。

一个 wedge、H2 或 double bottom 可以只是 Pattern；只有当交易者说明为什么在当前背景下交易它、准备怎样触发时，它才形成 Setup。涉及的 K 线角色以 [K 线类型](../04_patterns/01_bar_types.md)为准。

## Setup 不等于完整交易

Setup 回答“在什么背景下，准备交易什么价格行为、怎样触发，以及什么事实会使命题失效”。Setup 家族可以说明 stop 需要锚定哪类结构和直接期待哪类结果，但不独自固定最终 protective-stop 价格、实际退出价格、position size、scalp/swing 方案或成交后管理。

这些决定可能反过来淘汰一个 Setup：如果合理 stop 太远、现实 target 太近，或概率不足以补偿风险，那么候选仍然存在，但不应形成实际交易。完整闭环由 [Trade Plan](../06_trade_plan_and_management/00_trade_plan.md) 定义，数学约束由 [Trader's Equation](../00_method/01_probability_risk_reward.md) 定义。

## 三层边界

下面的 `Pattern → Setup → Trade Plan` 是仓库为消除职责重叠建立的组织模型，不是 Brooks 官方给出的固定三层分类。各层中的价格行为关系由来源支持；层名之间的权限边界属于仓库综合。

| 层次 | 回答的问题 | 不负责 |
| --- | --- | --- |
| Pattern | 看到了什么价格行为？ | 给出交易许可 |
| Setup | 为什么在这里交易、怎样触发、什么使 premise 失效？ | 固化最终订单价格、仓位与完整管理 |
| Trade Plan | 用哪套 entry、stop、target、仓位和 management 执行？ | 重新定义 Pattern 或 Context |

## Setup 家族不是穷尽分类

本目录用趋势延续、突破延续、交易区间 fade 和 MTR 比较不同交易命题。这些是组织核心差异的示例家族，不是所有 Setup 的固定清单。

Second entry 和 trap 描述触发顺序与失败机制，必须服务于某个上层交易命题，因此归入[接受与订单逻辑专题](../03_acceptance_and_order_logic/03_second_entries_and_traps.md)，不与四类 Setup 并列。

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS` 与 `SRC-RISK-113`。
