# Stop 入场与保护性 Stop（Stop Entry / Protective Stop）

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## 它解决什么问题

中文里很多地方都叫“止损单”，但 stop entry 和 protective stop 用途不同。混淆二者会误读 H1/H2/L1/L2、signal bar 和 trapped traders。

## Stop Entry

Stop entry 是用 stop order 触发入场。它表示交易者愿意在价格朝交易方向运动后入场，用较差价格换取方向确认。

典型表达：

- Buy stop：计划时放在 prospective signal bar 高点上方一跳。
- Sell stop：计划时放在 prospective signal bar 低点下方一跳。

Signal bar 与 entry bar 的角色及成立时点见 [K 线类型](../04_patterns/01_bar_types.md)。

Stop entry 常见于强趋势、强突破、小回调趋势和强 surprise 后。

Stop order entry 通常更适合多数经验较少的交易者，因为市场至少已经朝交易方向走了一跳。强突破中直接市价或收盘附近追随也可能顺势，但对经验较少的交易者更难。

## Protective Stop

Protective stop 是入场后的保护性止损。它应放在合理的 price-action 位置，使交易者在判断错误或无法继续管理时仍有有限风险；交易者也可以在 stop 触发前因 premise 改变而退出。

它可以位于：

- 回调低点或高点外。
- 突破失败位置外。
- 区间边界外。
- 反转结构被否定的位置外。

Protective stop 不是入场触发。Signal bar 另一端、完整 pullback 或 major swing 都可能是合理 stop，具体取决于 setup 和交易按 scalp 还是 swing 管理。

同一图表有时存在多个合理 protective stop：较近的 signal / pattern stop、完整 pullback / swing 外的 stop，或更宽的 catastrophe stop。它们对应不同风险距离、仓位和管理方式。

Price-action stop、经纪商触发价和预计成交价是不同层面：前者来自图表与管理，后两者用于真实订单和风险计算。滑点会改变实际 fill，但不会反向决定图上的合理 stop。

## Stop Order Market

Stop order market 指市场强到交易者愿意用较差价格换取确认。优势是先让市场证明方向，风险是入场价格差、止损距离可能变大。没有跟进时，追随者容易被困。

与之相对，在 trading range 顶底用 limit order fade 突破属于更高管理难度的交易。它不是错误，但通常需要多年经验、清晰最大风险和小目标管理。

## One Tick Above / Below

One tick above / below 的重点不是具体 tick size，而是 signal bar 高低点附近可能集中入场单和保护性止损。价格越过这些点后，要观察是否有跟进。

## 与其他核心主题的边界

本页只负责区分入场 stop 与保护性 stop。具体 setup 的 stop 依据见[Setup 是什么](../05_setups/00_what_is_a_setup.md)，target 依据见[Support、Resistance、Target 与 Measured Move](../02_context/01_support_resistance_targets.md)，成交后是否继续持有则见[接受、失望与失败证据](01_acceptance_and_failure.md)和[从 Setup 到交易计划](../06_trade_plan_and_management/00_trade_plan.md)。经纪商触发、实际成交与平台异常不会改变这些价格行为概念。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-STOP-ORDERS`、`SRC-RISK-113`、`SRC-BREAKOUTS-2025` 与 `SRC-GOOD-TRADE-2017`。
