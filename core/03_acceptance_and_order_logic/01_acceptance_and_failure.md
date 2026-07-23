# 接受、失望与失败证据

> **状态：Core / Definition**
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

## Disappointment、premise 变化和 Trade Failure

这里的 protective stop 是保护实际持仓的退出 stop，scalper's profit 是典型 scalp 目标；它们只界定结果，不提供新的 entry 依据。本节必须结合 [Stop Entry 和 Protective Stop](00_stop_entry_vs_protective_stop.md) 的完整定义理解，不能混用两类 stop。

为防止中文“失败”把不同对象混在一起，本仓库单独使用 **trade failure** 表示实际交易的结果；这是术语分工，不是另造一条 Brooks 交易规则。`failed breakout`、`failed H2` 或“旧极值测试失败”描述的是某次价格运动未达到预期，不自动表示某位交易者已经触及 protective stop。使用 failure 时应写清失败的对象。

实际交易还要区分三种不同事情：

- **Entry disappointment**：entry 弱、价格暂时没有离开入场区，结果尚未确定。它可能只是正常 pullback。
- **Premise 不再成立**：新的 price action 已经让交易者认为原计划错误，可以在最远 protective stop 触发前退出。
- **Trade failure**：实际 entry 后，原目标或至少 scalper's profit 尚未实现，protective stop 却先到达。

在同一份二结果计划的事后核对中，**success** 表示原计划目标先于 protective stop 到达；方向短暂走对或只先获得一个并非原目标的 scalper's profit，不自动等于完整目标成功。计划本来包含部分退出、scratch 或主动退出时，应按 Trade Plan 预先写出的互斥结果分别记录，不能事后硬改成二结果。

Entry disappointment 和 premise 变化描述不同阶段的价格行为，两者都不自动等于 trade failure。正常 swing pullback 不能仅因令人失望就归为 failed entry；`failed entry` 至少要求实际 entry 已经发生，没有成交的候选只能记录为未触发、过期、拒绝或失效。在 protective stop 前提前退出时，分别记录当时 premise 判断和实际价格结果。

### 从失望到退出，以及退出后的重新入场

管理不能只在“继续持有”和“等待最远 stop”之间二选一。实际持仓还应使用[Trade Plan 的三层退出保护](../06_trade_plan_and_management/00_trade_plan.md#三层退出保护)：在场 protective stop 负责最后保护；合理反向结构可以证明 premise 已失效；没有漂亮形态时，连续强反向动量也可能已经足以要求退出。普通小反向 K 线仍可能只是正常 pullback，必须按原 Context、管理周期和失效条件判断。

提前退出只表示当前计划不再值得承担风险，不表示原方向永远错误。若反向尝试随后失败、原方向重新获得接受，可以根据新的 trigger 建立新 Trade Plan；原 entry、概率、stop 和目标不能自动复用。

## Trapped traders

课程至少使用两种方向不同的 `trapped` 语言，必须分开：

- **Trapped in a trade**：一方已经实际入场、没有先获得原目标或至少 scalper's profit、仍处于开放亏损，并在反向运动中很可能被迫亏损退出。若反向运动已经迫使他们退出，可以描述为“曾被困并退出”，但不再属于当前开放的 `trapped in a trade` 状态。
- **Trapped out of a trade**：一方因为等待更好价格、止损距离不舒服、过早退出或其他原因没有建立或没有保留原本想要的仓位，随后行情沿该方向快速发展，使其被挡在交易之外。这里没有开放亏损仓位；潜在压力来自追价、回调重新入场或放弃参与，而不是亏损持仓的 protective stop。

`Trapped out` 也不等于“曾 trapped in 后已经止损退出”。前者描述错过或过早离开机会，后者描述一笔实际持仓的历史结果。两种 trapped 叙述都只是订单行为解释模型，必须由价格、可见 entry / stop 区域、follow-through 和目标空间支持，不能声称已经观察到所有参与者的真实仓位。

### Pain Trade

Pain Trade 是一种行为与价格路径模型：当许多交易者已经押注某一方向或等待市场按常见预期行动，行情却沿低预期方向持续扩展时，`trapped in` 一方的退出和 `trapped out` 一方的追入可能共同增加运动压力。这里描述的是从可见价格行为推断的潜在响应，而不是已经看见真实订单、持仓或参与者身份。

Pain Trade 不是新的 Setup，也不是独立的 failure state。实际判断仍回到本页的接受 / 失败框架：是否出现有效突破、follow-through、关键位置守住或快速收回，以及前方是否仍有现实空间。

判断时问：

- 当前讨论的是 `trapped in`、`trapped out`，还是曾被困后已经退出？
- 若为 `trapped in`：是否有足够交易者可能已经入场，且未先获得原目标或 scalper's profit、当前仍处于开放亏损？
- 若为 `trapped out`：哪些可见价格行为支持他们曾等待更好价格、过早退出或未能保留仓位？
- 后续运动是否强到足以迫使亏损退出、追价或重新入场？
- 反向运动前方是否有现实空间？

## Failed Failure（运动尝试）

失败的价格运动也可能失败。例如突破后快速收回，但随后原突破方向再次触发并获得强跟进。此时第一次 failed breakout 转成 breakout pullback，逆向交易者反而可能被困。这里描述两次运动尝试的结果，不表示同一笔交易连续两次触及 protective stop。

Failed failure 往往比第一次尝试更可靠，但名称本身仍不能替代 context、follow-through 和目标空间。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-GOOD-TRADE-2017`、`SRC-COURSE-01-36`（课程 02C、08C–10B、15A–15G、18A–20A、30A–30E、33D、36A–36B）与 `SRC-COURSE-37-52`（课程 40A–42C、49C–51D、52A–52B）。
