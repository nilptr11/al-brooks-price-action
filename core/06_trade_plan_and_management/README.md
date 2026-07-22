# 交易计划与管理

> **状态：Core / Index**
>
> 本页说明 Trade Plan schema、通用管理、数量风险和行为纪律的职责及文件入口，不实例化策略，也不重新定义上游市场状态、形态或 Setup。

首次学习时，进入本目录前应已按编号完整读完 `core/00_method` 至 `core/05_setups`；进入后按 `00`–`03` 顺序读完本目录全部正文。管理主题彼此依赖，不是按交易风格选择的菜单。

## 职责

本目录定义怎样把 premise、entry、protective stop、profit target、position size 和 management 固化成同一笔交易的通用 schema，并说明成交后怎样按新价格事实更新判断、怎样控制数量风险与行为偏差。

Setup 原型定义“准备交易哪类价格行为”；Trade Plan schema 定义“一份实例必须用哪套一致的风险与管理字段表达”；[策略手册](../../strategy/README.md)才提供具体实例。

## 文件

1. [`00_trade_plan.md`](00_trade_plan.md)：完整交易计划及其一致性约束。
2. [`01_scalp_vs_swing.md`](01_scalp_vs_swing.md)：scalp、swing 与 TBTL 的边界。
3. [`02_scaling_in_out.md`](02_scaling_in_out.md)：加减仓及其总风险。
4. [`03_risk_psychology.md`](03_risk_psychology.md)：仓位、连续亏损和行为纪律。

Trader's Equation 的定义见[概率、风险和回报](../00_method/01_probability_risk_reward.md)，概念总图见[核心框架](../README.md)。
