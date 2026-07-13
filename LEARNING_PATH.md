# 学习路径

> **状态：Navigation / Non-normative**
>
> 本文只规定学习顺序，不定义交易动作。实际执行以 [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) 为准。

## 核心路径

先完成下面七份材料。它们回答 Al Brooks 方法最重要的问题，不要求先背完整形态库：

1. [`learning/00_method/00_al_brooks_thesis.md`](learning/00_method/00_al_brooks_thesis.md)：用五个问题建立完整读图主线。
2. [`learning/01_market_cycle/00_market_cycle.md`](learning/01_market_cycle/00_market_cycle.md)：先分 trend / trading range，再识别 breakout / channel。
3. [`learning/02_context/00_context_location_control.md`](learning/02_context/00_context_location_control.md)：判断控制方向、位置和第一目标空间。
4. [`learning/05_setups/00_what_is_a_setup.md`](learning/05_setups/00_what_is_a_setup.md)：分清 pattern、setup 和完整交易计划。
5. [`learning/03_order_flow/00_acceptance_and_failure.md`](learning/03_order_flow/00_acceptance_and_failure.md)：用跟进、失望和失败判断市场是否接受一次尝试。
6. [`learning/00_method/01_probability_risk_reward.md`](learning/00_method/01_probability_risk_reward.md)：把概率、风险、回报和成本放进同一问题。
7. [`learning/06_trade_management/00_trade_plan.md`](learning/06_trade_management/00_trade_plan.md)：把 setup 补成包含失效、stop、目标、仓位和管理的计划。

核心路径结束时，应能不用内部代码回答：

- 当前是趋势还是交易区间，价格位于哪里？
- 正在验证什么交易想法，什么证据支持或否定它？
- Entry、失效、protective stop 和第一现实目标是什么？
- 概率、风险、回报和仓位是否匹配？
- 成交后的新信息是正常波动，还是 premise 已经失效？

## 立即开始基础训练

完成核心路径后即可进入 [`training/README.md`](training/README.md)，不需要先读完所有专题：

1. 先练市场状态、位置和一个交易想法。
2. 再补 entry、失效、stop、第一目标和简单 Trader's Equation。
3. 最后先在回放或模拟环境练订单状态、成交保护和持仓管理；若使用真实资金，必须先满足执行手册规定的账户、单笔、时段和相关敞口边界。

每轮只训练一个问题。遇到不认识的形态或管理概念，再返回下面的按需专题。

## 按需专题

| 遇到的问题 | 查阅入口 | 定位 |
| --- | --- | --- |
| 趋势、通道、区间、突破或高潮分不清 | [`learning/01_market_cycle/`](learning/01_market_cycle/README.md) | 核心概念扩展 |
| 支撑阻力、目标、周期或时段影响不清 | [`learning/02_context/`](learning/02_context/README.md) | Context 扩展 |
| Stop entry、protective stop 或 limit-order market 混淆 | [`learning/03_order_flow/`](learning/03_order_flow/README.md) | 订单方式与结果证据 |
| H1/H2、wedge、double top、triangle、gap 等名称不熟 | [`learning/04_patterns/`](learning/04_patterns/README.md) | 可选形态参考库，不是必读主线 |
| 想比较四类常见 setup | [`learning/05_setups/`](learning/05_setups/README.md) | 趋势恢复、突破、区间回归和 MTR |
| Scalp/swing、TBTL、加减仓或心理纪律 | [`learning/06_trade_management/`](learning/06_trade_management/README.md) | 管理专题；复杂行为后学 |

遇到陌生术语时查 [`reference/glossary.md`](reference/glossary.md)，不要为了背术语中断训练。形态库解释名称，不能覆盖 context、stop、目标或 Trader's Equation。
