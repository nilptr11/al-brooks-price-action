# 从 Setup 到交易计划

> **状态：Core / Definition**
>
> 本文是 Trade Plan 的权威定义页，负责一笔交易的组成部分及其一致性。

## Trade Plan 的定义

Trade Plan 是围绕一个 Setup 固化的完整交易方案。它把交易命题、实际承担的风险和成交后管理放在同一组假设中，使入场前的判断和事后复盘可以核对。

一份完整计划至少包含：

| 组成 | 必须回答的问题 |
| --- | --- |
| Premise | 当前 Setup 押注什么价格行为，哪些 Context 支持它？ |
| Entry | 哪个可观察条件触发订单，预计实际成交怎样处理？ |
| Invalidation | 哪些新价格事实说明原命题不再成立？ |
| Protective stop | 最远保护价在哪里，为什么该位置容许正常波动却限制错误判断？ |
| Profit target | 准备在哪个现实区域或价格兑现，依据是什么？ |
| Position size | 按 entry 到 protective stop 的真实风险，可以承担多少数量？ |
| Management | 按 scalp 还是 swing，怎样处理正常回调、部分退出、时间和新证据？ |
| Trader's Equation | 这组概率、risk、reward 与成本是否值得承担？ |

Invalidation 与 protective stop 相关但不等同：前者是原 premise 被新证据否定，后者是在无法或不应继续管理时限制损失的最远订单保护。交易者可以在 protective stop 触发前，基于可观察的 premise 变化退出。

## 一致性约束

- Entry、stop、target、概率和仓位必须来自同一版本，不能拼接不同方案中最有利的输入。
- Stop 改变会同时改变风险距离、仓位和 Trader's Equation；target 或管理改变也要重新检查整套数学。
- Profit target 使用实际准备交易的价格，不使用与当前 Setup 无关的远端投射来制造理想 reward/risk。
- Scalp 与 swing 对回调、持有时间和目标空间的容忍不同；入场后不能只因盈亏情绪随意切换。
- Catastrophe stop 可以作为后备保护，但不能替代 price-action stop、premise 判断和主动管理。

Protective stop 的订单用途见 [Stop Entry 和 Protective Stop](../03_order_flow/01_stop_entry_vs_protective_stop.md)，目标构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)，仓位数学见[概率、风险和回报](../00_method/01_probability_risk_reward.md)。

## 成交后的更新

计划不是静态剧本。成交后继续观察 entry bar、follow-through、关键位置是否守住、反方是否获得强突破，以及原目标是否仍现实。

[接受、失望与失败证据](../03_order_flow/00_acceptance_and_failure.md)区分正常波动、entry disappointment、premise 变化和 trade failure；[Scalp 与 Swing](01_scalp_vs_swing.md)界定持有方式，[加仓与减仓](02_scaling_in_out.md)界定数量变化。正常 pullback 不自动否定交易，强反向证据也不能因为没有逐字预写而被忽略。

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE`、`SRC-GOOD-TRADE-2017` 与 `SRC-HOLDING-WIDE-STOPS`。
