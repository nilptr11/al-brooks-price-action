# 从 Setup 到交易计划

> **状态：Core / Definition**
>
> 本文是 Trade Plan schema 的权威定义页，负责规定一笔交易实例必须包含的组成及其一致性；它本身不生成具体策略计划。

本页的固定字段、版本记录和管理分支是仓库为一致执行与复盘建立的综合 schema / 执行基线，不是 Brooks 官方给出的固定八字段表。字段中的价格行为、风险与管理关系仍分别由相关来源支持。

## Trade Plan 的定义

Trade Plan 是围绕一个 Setup 固化的完整交易方案。它把交易命题、实际承担的风险和成交后管理放在同一组假设中，使入场前的判断和事后复盘可以核对。

一份完整计划至少包含：

| 组成 | 必须回答的问题 |
| --- | --- |
| Premise | 当前 Setup 押注什么价格行为，哪些 Context 支持它？ |
| Entry | 哪个可观察条件触发订单，预计实际成交怎样处理？ |
| Invalidation | 哪些新价格事实说明原命题不再成立？ |
| Active protective stop | 当前实际保护单在哪里，为什么该位置容许正常波动却限制错误判断？ |
| Profit target | 准备在哪个现实区域或价格兑现，依据是什么？ |
| Position size | 按 entry 到 protective stop 的真实风险，可以承担多少数量？ |
| Management | 按 scalp 还是 swing，怎样处理正常回调、部分退出、时间和新证据？ |
| Trader's Equation | 这组概率、risk、reward 与成本是否值得承担？ |

Invalidation 与 active protective stop 相关但不等同：前者是原 premise 被新证据否定，后者是当前真实在场、用于限制这份计划风险的保护订单。交易者可以在该 stop 触发前，基于可观察的 premise 变化主动退出。

若交易架构还使用更远的 `catastrophe backup`，必须把它作为独立可选字段记录，并明确极端情况下从 entry 到该订单的最大损失、相应仓位上限以及何时撤换。它不等于 active protective stop，也不能被用来缩小计划表中的真实最坏风险。所谓 price-action stop 必须落到前述某个明确订单或主动退出规则，不能同时指代两个不同价位。

## 一致性约束

- Entry、active protective stop、target、概率和仓位必须来自同一版本，不能拼接不同方案中最有利的输入；若另有 catastrophe backup，也必须计入最坏损失与仓位约束。
- 在承担风险前，stop、target 或管理的任何改变都表示计划版本已经改变，必须同时重算风险距离、仓位和 Trader's Equation。
- Profit target 使用实际准备交易的价格，不使用与当前 Setup 无关的远端投射来制造理想 reward/risk。
- `original_target` 是入场时的审计原值，成交后不得因结果而回填、重选 measured-move 端点或伪装成另一版本。新证据可以使目标不再现实，也可以支持按预写分支调整管理；此时另记 `current_management_target` 与 `actual_exit`、时间和证据，不覆盖原值，并重新检查剩余仓位的 Trader's Equation。
- Scalp 与 swing 对回调、持有时间和目标空间的容忍不同；入场后不能只因盈亏情绪随意切换。
- Catastrophe backup 只能作为另行预算的灾难性后备，不能替代 active protective stop、premise 判断和主动管理。

Protective stop 的订单用途见 [Stop Entry 和 Protective Stop](../03_acceptance_and_order_logic/00_stop_entry_vs_protective_stop.md)，目标构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)，仓位数学见[概率、风险和回报](../00_method/01_probability_risk_reward.md)。

## Stop 调整与保本

保本止损可以降低心理压力，但也可能让正常回调提前结束交易，因此不能仅因浮盈出现就机械移到 entry。

价格到达原计划允许减仓的 target、新 higher low / lower high 或其他 price-action 结构，可能支持向保护方向调整 stop。任何调整仍须服从原 Setup、当前 premise、剩余仓位和管理方式；Stop 放得过近，可能在正常回踩中提前结束本来合理的交易。

## 三层退出保护

每笔实际持仓至少要能区分三种保护，它们不是三个互相替代的 stop price：

1. **Active protective stop**：实际在场的最后保护，用于在主动判断、连接或执行失败时限制最坏风险。
2. **Premise invalidation / 合理反向结构**：新的价格事实已经使原交易命题不再成立，可以在最远 stop 触发前主动退出；它必须由计划中可观察的条件定义，不能只写“感觉不对”。
3. **强反向动量**：即使还没有漂亮的反转形态，一根异常强反向趋势 K 线、数根连续无重叠的反向 K 线或 Always In 明确翻转，也可能已经足以否定原 premise；具体强度仍由 Context 和原管理周期判断。

这三层共同防止正常亏损变成大额亏损：硬 stop 防止失控，结构失效允许更早承认错误，强反向动量避免为了等待完美信号而忽视市场已经改变。普通小反向 K 线和正常 swing pullback 不自动触发第二或第三层。

主动退出后，若反转失败、原方向重新获得接受，交易者可以重新入场；这必须建立新的 observable trigger、stop、target、仓位和 Trader's Equation，并记录为新的计划版本。重新入场的可能性不能反向证明先前退出错误，也不能成为取消当前保护的理由。

## 成交后的更新

计划不是静态剧本，因为 premise 会随新事实接受复核；计划也不是允许事后重写输入的草稿。成交后继续观察 entry bar、follow-through、关键位置是否守住、反方是否获得强突破，以及原目标是否仍现实。目标不再现实必须进入记录并按入场前选择的管理分支处理，但不会把更近或更远的价位追认为原 target。

[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)区分正常波动、entry disappointment、premise 变化和 trade failure；[Scalp 与 Swing](01_scalp_vs_swing.md)界定持有方式，[加仓与减仓](02_scaling_in_out.md)界定数量变化。正常 pullback 不自动否定交易；强反向证据必须记录并按已选管理分支解释，不能为迎合结果临场切换分支。

标准策略计划必须在入场前写出可观察的 premise 变化及对应主动退出；结构保护止损和固定目标是订单基线，不表示可以忽略这些变化。若维护者只想隔离 stop / target 的机械结果，必须另立预先声明的 `mechanical_only` 独立研究变体：中途证据仍继续记录，但不临场新增视觉退出；它不属于三种标准执行环境的同口径结果，也不得与标准回放、模拟或实盘直接比较。无论采用哪种研究或执行口径，订单回执不明、保护不足、连接异常等安全事实都由[执行手册](../../execution/execution_manual.md)处理，任何计划都不能用“固定管理”忽略真实仓位风险。

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE`、`SRC-GOOD-TRADE-2017`、`SRC-HOLDING-WIDE-STOPS`、`SRC-COURSE-01-36`（课程 30A–36B）与 `SRC-COURSE-37-52`（课程 37A–37B、41A–41D、51A–52B）。
