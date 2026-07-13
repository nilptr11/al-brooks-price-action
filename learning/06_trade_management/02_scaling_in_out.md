# 加仓与减仓

> **状态：Learning / Non-normative**
>
> 本文只解释加减仓如何改变交易数学；是否允许以及所需字段，以[执行手册的主动高级行为](../../EXECUTION_MANUAL.md#主动高级行为)为唯一权威。

## Scaling In

Scaling in 是分批增加数量。它可能改善平均 entry，却同时改变总数量、stop 结果、成本和第一目标的回报，因此不能只用“均价更好”判断交易是否改善。每个层级合在一起才是一份完整 Trader's Equation；临场增加数量则构成一份新的风险问题。

这种方法更常出现在有经验的交易者处理宽 trading range 或 limit-order environment 时。紧区间、区间中部和强趋势逆势场景通常更难，因为目标空间、突破风险或单边压力可能让平均价格的改善失去意义。

## Scaling Out

Scaling out 是分批减少数量。它会改变剩余仓位的风险、目标分布和结果路径，常见用途包括：

- 到达第一目标部分止盈。
- 强趋势中保留一部分仓位。
- 信号弱化时降低风险。
- 目标附近减少暴露。

减仓不是为了逃避计划，而是按既定目标、风险收缩、异常处置，或新出现的 premise 失效证据降低风险。同质仓位按比例缩小只会同比降低回报和风险，不会改变每单位期望的正负；新信息可以要求降险，不能用来扩大原交易。

## Breakeven Stop

保本止损可以降低心理压力，但也可能让正常回调提前结束交易。

不应机械保本。价格到达第一目标可以按计划减仓，stop 只有在有效新结构形成时才向保护方向推进；否则维持原 stop，或在命题失效时退出，不能把 stop 放到正常回踩路径上。

来源审计见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-POSITION-SIZE`、`SRC-TRADING-RANGES`、`SRC-STOP-ORDERS`。
