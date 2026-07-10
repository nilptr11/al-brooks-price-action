# Stop Entry 和 Protective Stop

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../README.md#权威层级)。

## 它解决什么问题

中文里很多地方都叫“止损单”，但 Brooks 语境中必须区分 stop entry 和 protective stop。混淆二者会误读 H1/H2/L1/L2、signal bar 和 trapped traders。

## Stop Entry

Stop entry 是用 stop order 触发入场。它表示交易者愿意在价格朝交易方向运动后入场，用较差价格换取方向确认。

典型表达：

- Buy stop：在 signal bar 高点上方一跳买入。
- Sell stop：在 signal bar 低点下方一跳卖出或做空。

Stop entry 常见于强趋势、强突破、小回调趋势和强 surprise 后。

Brooks 公开 manual 中也强调，stop order entry 通常更适合多数学习者，因为市场至少已经朝交易方向走了一跳。强突破中直接市价或收盘附近追随也可能顺势，但对初学者更难。

## Protective Stop

Protective stop 是入场后的保护性止损，用来把交易命题的无效点转换成有限损失的订单。无效点是市场事实，stop 是订单价格，两者不能混为一个词。

它可以位于：

- 回调低点或高点外。
- 突破失败位置外。
- 区间边界外。
- 反转结构被否定的位置外。

Protective stop 服务于无效点，不是入场触发。Signal bar 另一端只是常见候选；只有它同时界定命题失败时，才是合格的结构止损。

## Stop Order Market

Stop order market 指市场强到交易者愿意用较差价格换取确认。优势是先让市场证明方向，风险是入场价格差、止损距离可能变大。没有跟进时，追随者容易被困。

与之相对，在 trading range 顶底用 limit order fade 突破属于更高管理难度的交易。它不是错误，但通常需要多年经验、清晰最大风险和小目标管理。

## One Tick Above / Below

Brooks 常说 one tick above / below，重点不是具体 tick size，而是 signal bar 高低点附近可能集中入场单和保护性止损。价格越过这些点后，要观察是否有跟进。

## 执行边界

- 先找结构无效点，再决定 protective stop；不能从希望承受的点数反推一个虚假的结构。
- 合理止损过远时缩小仓位、等待或放弃，不能为了好看的 R 倍数把 stop 放进正常波动。
- 入场后不得把 stop 移出预设 outer boundary；新的有效结构只能用于向保护利润方向推进止损。

来源审计见 `reference/official_sources.md` 中的 `SRC-STOP-ORDERS`、`SRC-RISK-113`，以及 `reference/audit_matrix.md`。
