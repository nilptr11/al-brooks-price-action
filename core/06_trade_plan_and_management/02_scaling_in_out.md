# 加仓与减仓

> **状态：Core / Definition**
>
> 本文解释加减仓如何改变整笔交易的风险、回报和管理方式。

## Scaling In

Scaling in 是分批增加数量。它可能改善平均 entry，却同时改变总数量、stop 结果、成本和 profit target 的回报，因此不能只用“均价更好”判断交易是否改善。整个 scale-in 计划合在一起才是一份完整 Trader's Equation。

合理的 scale-in 从第一笔 entry 前就使用较小初始仓位、明确最外侧 stop，并计算所有计划数量的总风险。它可以在趋势 pullback、broad channel 或 trading range 中使用；若市场形成强反向 breakout、原 premise 改变，继续加仓就不再由原计划支持。

这种方法更常出现在有经验的交易者处理宽 trading range 或 limit-order environment 时。紧区间、区间中部和强趋势逆势场景通常更难，因为目标空间、突破风险或单边压力可能让平均价格的改善失去意义。

## Scaling Out

Scaling out 是分批减少数量。它会改变剩余仓位的风险、目标分布和结果路径，常见用途包括：

- 到达计划 target 后部分止盈。
- 强趋势中保留一部分仓位。
- 信号弱化时降低风险。
- 目标附近减少暴露。

减仓不是为了逃避计划，而是按既定目标、风险收缩、异常处置，或新出现的 premise 失效证据降低风险。同质仓位按比例缩小只会同比降低回报和风险，不会改变每单位期望的正负；是否保留、减少或按原 scale-in 计划增加数量，仍由当前 price action、总风险和原 premise 决定。

## Breakeven Stop

保本止损可以降低心理压力，但也可能让正常回调提前结束交易。

不应机械保本。价格到达计划 target 可以减仓；新 higher low / lower high 或其他 price-action 结构也可能支持向保护方向调整 stop。Stop 放得过近，可能在正常回踩中提前结束本来合理的交易。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-SCALE-IN-TRENDS`、`SRC-POSITION-SIZE`、`SRC-TRADING-RANGES` 与 `SRC-STOP-ORDERS`。
