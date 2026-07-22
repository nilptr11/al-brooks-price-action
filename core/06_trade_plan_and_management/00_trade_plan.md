# 从 Setup 到交易计划

> **状态：Core / Definition**
>
> 本文是 Trade Plan schema 的权威定义页，负责规定一笔交易实例必须包含的组成及其一致性；它本身不生成具体策略计划。

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
- 在承担风险前，stop、target 或管理的任何改变都表示计划版本已经改变，必须同时重算风险距离、仓位和 Trader's Equation。
- Profit target 使用实际准备交易的价格，不使用与当前 Setup 无关的远端投射来制造理想 reward/risk。
- 成交后不因行情结果扩大目标、重选 measured-move 端点或切换到更有利的计划版本；premise 变化导致的主动退出属于风险管理，不是修改原 target。
- Scalp 与 swing 对回调、持有时间和目标空间的容忍不同；入场后不能只因盈亏情绪随意切换。
- Catastrophe stop 可以作为后备保护，但不能替代 price-action stop、premise 判断和主动管理。

Protective stop 的订单用途见 [Stop Entry 和 Protective Stop](../03_acceptance_and_order_logic/00_stop_entry_vs_protective_stop.md)，目标构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)，仓位数学见[概率、风险和回报](../00_method/01_probability_risk_reward.md)。

## Stop 调整与保本

保本止损可以降低心理压力，但也可能让正常回调提前结束交易，因此不能仅因浮盈出现就机械移到 entry。

价格到达原计划允许减仓的 target、新 higher low / lower high 或其他 price-action 结构，可能支持向保护方向调整 stop。任何调整仍须服从原 Setup、当前 premise、剩余仓位和管理方式；Stop 放得过近，可能在正常回踩中提前结束本来合理的交易。

## 成交后的更新

计划不是静态剧本，因为 premise 会随新事实接受复核；计划也不是允许事后重写输入的草稿。成交后继续观察 entry bar、follow-through、关键位置是否守住、反方是否获得强突破，以及原目标是否仍现实。目标不再现实必须进入记录并按入场前选择的管理分支处理，但不会把更近或更远的价位追认为原 target。

[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)区分正常波动、entry disappointment、premise 变化和 trade failure；[Scalp 与 Swing](01_scalp_vs_swing.md)界定持有方式，[加仓与减仓](02_scaling_in_out.md)界定数量变化。正常 pullback 不自动否定交易；强反向证据必须记录并按已选管理分支解释，不能为迎合结果临场切换分支。

具体策略必须在入场前选择管理分支：要么写出可观察的 premise 变化及对应主动退出；要么明确采用只由结构保护止损和固定目标结束的审计基线，中途证据继续记录，但不临场新增视觉退出。后一种是 Strategy 对本 schema 的具体实例化，并不把所有交易定义成静态管理。无论选择哪一分支，订单回执不明、保护不足、连接异常等执行安全事实都由[执行手册](../../execution/execution_manual.md)处理，任何策略都不能用“固定管理”忽略真实仓位风险。

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE`、`SRC-GOOD-TRADE-2017` 与 `SRC-HOLDING-WIDE-STOPS`。
