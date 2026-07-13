# 从 Setup 到交易计划

> **状态：Learning / Non-normative**
>
> 本文解释完整交易想法的组成，不定义订单动作；实际执行只见当前[执行手册](../../EXECUTION_MANUAL.md)。

## Setup 仍不是完整交易

Setup 提供 context 与入场依据，但交易还必须把 entry、premise 失效、protective stop、目标、仓位和管理放进同一个方案。缺少其中任何关键部分，都只能等待或继续设计。

一份计划至少回答：

- 当前是什么市场状态和位置？
- 正在验证哪一种交易想法？
- 什么具体行为构成 entry？
- 什么事实说明 premise 已错？
- Protective stop 和仓位如何限制最坏结果？
- 第一现实目标是否足以补偿风险？
- 正常回调、目标、反向强突破和时间退出分别如何管理？

## 把同一命题连成闭环

需要分开四层：

同一图表可能容许 signal-bar stop、完整结构 stop 或更宽的 price-action stop。它们改变 stop 距离、仓位、概率和目标空间，因此是不同候选方案，不能把其中最有利的输入拼在一起。字段含义和动作边界只见[执行手册的 stop、目标和仓位章节](../../EXECUTION_MANUAL.md#7-protective-stop目标和仓位)，可填写版式见[执行记录模板](../../EXECUTION_RECORD_TEMPLATE.md)。

## 目标、仓位与数学必须一致

第一现实目标是 Trader's Equation 的输入，不是形态名称自动给出的愿望。学习时先标出路径上的近端支撑阻力和现实退出位置，再判断更远的 measured move、区间另一侧或 runner 是否属于同一方案；常见构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)。

仓位把价格风险转换成账户结果。Entry、stop、第一目标、数量、成本和概率必须来自同一候选方案；改动任一项，都要重新检查整个 Trader's Equation。学习页只解释这项一致性，损失边界、订单保护和实际管理仍由执行手册规定。

## 管理是对命题的持续复核

成交后的新信息通常落入三类：原 premise 仍成立的正常波动、计划中已经考虑的目标或时间事件、使 premise 失效的新证据。计划要在入场前说明如何区分这些类别，复盘则检查当时判断是否有可观察证据。

Scalp 与 swing 对正常回调、目标距离和持有时间的预期不同，概念差异见[Scalp 与 Swing](01_scalp_vs_swing.md)。具体退出、stop 移动、减仓和异常处置不在本文重复，统一回到[执行手册的成交后管理](../../EXECUTION_MANUAL.md#10-成交后的管理)。

来源和审计状态见 [`reference/official_sources.md`](../../reference/official_sources.md) 与 [`reference/audit_matrix.md`](../../reference/audit_matrix.md)。
