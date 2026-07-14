# 接受、失望与失败证据

> **状态：Learning / Non-normative**
>
> 本文用可观察的价格行为理解触发后的结果，不要求猜测真实订单簿或参与者身份。

## 触发之后看什么

价格越过关键位置时，可能同时遇到 stop entry、protective stop、limit order 和获利了结。我们无法知道每笔订单来自谁，真正可观察的是市场是否接受新的方向：

- Entry bar 是否有力度。
- 后续是否出现 follow-through。
- 回调是否浅，突破点或关键区域是否守住。
- 反方是否快速收回关键位置。
- 原方向恢复，还是失败后形成反向运动。

触发本身不等于成功，单根强 K 线也不等于持续趋势。

## Follow-through、surprise 和惯性

Follow-through 的最低含义是初始运动之后，后续一根或多根 K 线继续延伸该运动。强收盘、浅回调和反方失败可以作为更广的 acceptance evidence，但不改变这个最低定义。

Surprise 是明显超出交易者预期的强行为。强 surprise 常使错过者追随、站错者退出，因此市场往往还会尝试形成第二腿；这只是概率倾向，不表示价格必须直线延伸。

没有 follow-through 会削弱突破或 setup，但不能仅凭下一根普通回调就宣告失败。

## Disappointment、premise 变化和 failure

这里的 protective stop 是保护实际持仓的退出 stop，scalper's profit 是典型 scalp 目标；它们只界定结果，不提供新的 entry 依据。若两类 stop 仍易混淆，按需查 [Stop Entry 和 Protective Stop](01_stop_entry_vs_protective_stop.md)。

需要区分三种不同事情：

- **Entry disappointment**：entry 弱、价格暂时没有离开入场区，结果尚未确定。它可能只是正常 pullback。
- **Premise 不再成立**：新的 price action 已经让交易者认为原计划错误，可以在最远 protective stop 触发前退出。
- **Failure**：实际 entry 后，原目标或至少 scalper's profit 尚未实现，protective stop 却先到达。

Entry disappointment 和 premise 变化描述不同阶段的价格行为，两者都不自动等于 failure。正常 swing pullback 不能仅因令人失望就归为 failed entry；在 protective stop 前提前退出时，分别记录当时 premise 判断和实际价格结果。

## Trapped traders

只有当一方已经实际入场、没有先获得原目标或至少 scalper's profit、仍处于开放亏损，并在反向运动中很可能被迫退出时，才有足够证据把他们称为当前 trapped traders。若反向运动已经迫使他们退出，可以描述为“曾被困并退出”，但不再属于当前 `trapped in a trade` 状态。他们的退出可能增强反向订单压力，但这个叙述仍必须由价格、stop/entry 区域、实际失败和目标空间支持。

判断时问：

- 是否有足够交易者可能已经被触发入场？
- 原目标或至少 scalper's profit 是否尚未先实现？
- 已入场一方是否处于开放亏损？
- 反向运动是否已威胁或触及可见失效边界？
- 是否出现足以迫使退出、或已经造成实际退出的强度？
- 反向运动前方是否有现实空间？

## Failed failure

失败也可能失败。例如突破后快速收回，但随后原突破方向再次触发并获得强跟进。此时第一次失败转成 breakout pullback，逆向交易者反而可能被困。

Failed failure 往往比第一次尝试更可靠，但名称本身仍不能替代 context、follow-through 和目标空间。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016` 与 `SRC-GOOD-TRADE-2017`。
