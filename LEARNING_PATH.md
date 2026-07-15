# 学习路径

> **状态：Navigation / Non-normative**
>
> 本文只规定学习顺序，不定义交易动作。核心路径在 `learning/` 内完成从读图到交易管理的知识闭环；来源仅用于证据校准。

## 核心路径

先完成下面七份材料。它们回答 Al Brooks 方法最重要的问题，不要求先背完整形态库：

1. [`learning/00_method/00_al_brooks_thesis.md`](learning/00_method/00_al_brooks_thesis.md)：建立 market cycle、context、setup 和 Trader's Equation 的读图主线。
2. [`learning/01_market_cycle/00_market_cycle.md`](learning/01_market_cycle/00_market_cycle.md)：先分 trend / trading range，再识别 breakout / channel。
3. [`learning/02_context/00_context_location_control.md`](learning/02_context/00_context_location_control.md)：判断控制方向、位置和现实目标空间。
4. [`learning/05_setups/00_what_is_a_setup.md`](learning/05_setups/00_what_is_a_setup.md)：分清 pattern、setup 和完整交易计划。
5. [`learning/03_order_flow/00_acceptance_and_failure.md`](learning/03_order_flow/00_acceptance_and_failure.md)：用跟进、失望、premise 变化和 failure 理解一次尝试的结果。
6. [`learning/00_method/01_probability_risk_reward.md`](learning/00_method/01_probability_risk_reward.md)：把概率、风险、回报和成本放进同一问题。
7. [`learning/06_trade_management/00_trade_plan.md`](learning/06_trade_management/00_trade_plan.md)：把 setup 补成包含失效、stop、目标、仓位和管理的计划。

核心路径结束时，应能用自然语言回答：

- 当前是趋势还是交易区间，价格位于哪里？
- 当前 setup 与 entry 依据是什么，反方向为什么仍可能合理？
- Price-action stop 在哪里，这类 setup 的 profit target 是什么？
- 概率、风险、回报、管理方式和仓位是否匹配？
- 成交后的新信息是正常波动，还是 premise 已经失效？

## 立即开始基础训练

完成核心路径后即可进入 [`training/README.md`](training/README.md)，不需要先读完所有专题：

1. 固定数据源、品种和一个决策周期，从保存的历史位置连续逐根推进，不主动寻找指定形态。
2. 一边记录市场状态、位置和判断变化，一边在自然出现值得交易的 setup 时用[执行记录模板](EXECUTION_RECORD_TEMPLATE.md)记录 entry、price-action stop、setup 对应的 target、仓位、管理方式和 Trader's Equation，再进行回放或模拟成交。
3. 在同一记录中练订单状态、成交保护和持仓管理，结束后只复盘一个主要流程问题；若使用真实资金，必须先在批次配置中确定用户自己的账户、单笔、时段和相关敞口边界。

每轮只选择一个流程复盘重点，不要求市场出现对应形态或问题。遇到不认识的形态或管理概念，再返回下面的按需专题。

## 按需专题

| 遇到的问题 | 查阅入口 | 定位 |
| --- | --- | --- |
| 趋势、通道、区间、突破或高潮分不清 | [`learning/01_market_cycle/`](learning/01_market_cycle/README.md) | 核心概念扩展 |
| 支撑阻力、目标、周期或时段影响不清 | [`learning/02_context/`](learning/02_context/README.md) | Context 扩展 |
| Stop entry、protective stop 或 limit-order market 混淆 | [`learning/03_order_flow/`](learning/03_order_flow/README.md) | 订单方式与结果证据 |
| H1/H2、wedge、double top、triangle、gap 等名称不熟 | [`learning/04_patterns/`](learning/04_patterns/README.md) | 可选形态参考库，不是必读主线 |
| 想比较常见 setup 的 stop 与 target | [`learning/05_setups/`](learning/05_setups/README.md) | 趋势 flag、突破、区间交易、MTR 与二次入场 |
| Scalp/swing、TBTL、加减仓或心理纪律 | [`learning/06_trade_management/`](learning/06_trade_management/README.md) | 管理专题；复杂行为后学 |

需要确认跨章节核心术语的最低边界时查 [`reference/glossary.md`](reference/glossary.md)；形态、订单和管理词进入上表对应专题，不要为了背术语中断训练。形态库解释名称，不能覆盖 context、stop、目标或 Trader's Equation。
