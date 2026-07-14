# 从 Setup 到交易计划

> **状态：Learning / Non-normative**
>
> 本文解释一笔交易如何把 setup、stop、target、position size 和 management 连在一起，并完成学习体系中的交易闭环。

## Setup 仍不是完整交易

Setup 提供 context 与入场依据，但交易者还需要选择合理 entry、protective stop、profit target、仓位和管理方式，才能判断 Trader's Equation。

一份计划至少回答：

- 当前是什么市场状态和位置？
- 当前 setup 的 premise 和典型价格行为结果是什么？
- 什么具体行为构成 entry？
- 合理的 price-action stop 在哪里，哪些新证据会让交易者提前退出？
- Protective stop 和仓位如何限制风险？
- 这类 setup 的 profit target 是什么？
- 正常回调、目标、反向强突破和时间退出分别如何管理？

## Stop、target 与管理必须属于同一笔交易

同一图表可能容许 signal-bar stop、完整 pullback stop 或更宽的 price-action stop。它们改变 stop 距离、仓位、概率、target 和管理方式，因此不能把不同方案中最有利的输入拼在一起。Setup-specific stop 与 target 见[什么是 Setup](../05_setups/00_what_is_a_setup.md)和[支撑阻力与目标](../02_context/01_support_resistance_targets.md)。

## 目标、仓位与数学必须一致

Trader's Equation 使用这类 setup 实际准备采用的 profit target，不是形态名称自动生成的愿望。目标可能是 scalp、旧极值、区间内部位置、measured move、反向 swing 或 runner；常见构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)。

仓位把价格风险转换成账户结果。Entry、stop、target、数量和概率必须描述同一笔交易；改动任一项，都要重新检查 Trader's Equation。费用和滑点在订单记录中另行计算。

## 管理是对命题的持续复核

成交后需要区分原 premise 仍成立的正常波动、计划中已经考虑的目标或时间事件，以及使 premise 失效的新证据。计划要在入场前说明这些行为将怎样影响管理，复盘则检查当时判断是否有可观察证据。

Scalp 与 swing 对正常回调、目标距离和持有时间的预期不同，概念差异见[Scalp 与 Swing](01_scalp_vs_swing.md)。成交后继续观察 entry 与 follow-through、关键位置是否守住、反方是否形成强 breakout 或持续跟进，以及原目标是否仍现实；[接受、失望与失败证据](../03_order_flow/00_acceptance_and_failure.md)说明这些结果边界，[加仓与减仓](02_scaling_in_out.md)说明数量和 stop 调整如何改变原交易数学。

正常 pullback 或单根令人失望的 entry bar 不自动使交易失败。只要新的 price action 仍符合原 setup 的典型路径和风险假设，就按预定 scalp 或 swing 方案管理；强反向行为、持续反向 follow-through、关键结构失守，或其他足以否定原 premise 的证据出现时，可以在最远 protective stop 触发前退出。最远 stop 可以是 catastrophe protection，但不能代替持续读取 price action。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE`、`SRC-GOOD-TRADE-2017` 与 `SRC-HOLDING-WIDE-STOPS`。
