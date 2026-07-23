# 加仓与减仓

> **状态：Core / Definition**
>
> 本文解释加减仓如何改变整笔交易的风险、回报和管理方式。

## Scaling In

Scaling in 是分批增加数量。它可能改善平均 entry，却同时改变总数量、stop 结果、成本和 profit target 的回报，因此不能只用“均价更好”判断交易是否改善。整个 scale-in 计划合在一起才是一份完整 Trader's Equation。

合理的 scale-in 从第一笔 entry 前就使用较小初始仓位、明确最外侧 stop，并计算所有计划数量的总风险。它可以在趋势 pullback、broad channel 或 trading range 中使用；若市场形成强反向 breakout、原 premise 改变，继续加仓就不再由原计划支持。

这种方法更常出现在有经验的交易者处理宽 trading range 或 limit-order environment 时。紧区间、区间中部和强趋势逆势场景通常更难，因为目标空间、突破风险或单边压力可能让平均价格的改善失去意义。

### 盈利加仓与亏损加仓不是同一件事

向盈利仓位加仓通常依赖新的顺势 breakout、follow-through 或回调恢复，意味着市场已提供更多方向证据；但新层仍会提高总数量和回撤暴露，每一次都必须作为新增风险重新计算。后续层可以按较短目标管理，早期层保留为 swing，也可以使用统一管理；选择必须事前写明。动量衰减、重叠增加或结构进入 trading range 时，应按计划把扩大后的仓位降回常态，不能让“已有浮盈”替代总风险控制。

向亏损仓位加仓主要改善整仓均价和保本/减亏退出条件，并不获得上述顺势确认。只有原 premise 仍有效、计划层尚未用完、新 entry 自己具有可观察依据且全部数量风险仍在上限内，才可以执行；价格越不利、反向证据越强时，应该退出而不是强制完成剩余层。多数交易者更适合等待原本准备加仓的位置作为第一次 entry，或在退出后等待新的反转再入场。

### 整仓均价与总风险

多次入场必须按一笔整仓计算。若第 `i` 次 entry price 为 `eᵢ`、数量为 `qᵢ`，总数量 `Q = Σqᵢ`，则忽略费用时：

```text
weighted average entry = Σ(qᵢ × eᵢ) / Q
```

若多单所有层共用 protective stop `s`，触及该 stop 的价格风险为：

```text
long gross stop risk = Σ[qᵢ × (eᵢ - s)]
```

空单使用镜像距离 `Σ[qᵢ × (s - eᵢ)]`。真实账户风险还要乘每点价值，并加入手续费、滑点以及无法按计划成交的异常余量。两次等量入场时，两个 entry 的中点才是忽略成本的整仓 breakeven；数量不等时必须使用加权均价，不能机械取中点。

所有计划层都应在第一笔 entry 前进入最坏总风险。若 stop 距离约为通常的两倍，而允许账户风险不变，全部计划数量原则上要约减半；若又分三层，风险预算还要在三层之间分配，而不是每层继续使用普通仓位。具体数量仍取决于各层 entry 到共同 stop 的不同距离。

Scale-in 可以改善整仓均价，并改变整仓达到 breakeven 或 profit target 的条件，但不会让市场朝原方向运动的客观概率凭空提高。概率是否改善只能由新的 Context、独立信号和完整策略样本判断；单纯增加 entry 次数只会增加敞口。

## Scaling Out

Scaling out 是分批减少数量。它会改变剩余仓位的风险、目标分布和结果路径，常见用途包括：

- 到达计划 target 后部分止盈。
- 强趋势中保留一部分仓位。
- 按预写管理分支，在信号实质弱化或新证据改变 premise 时降低风险。
- 目标附近减少暴露。

减仓不是为了逃避计划，也不是看到任意弱 K 线就临场修改；它必须来自预写管理分支，或足以实质改变 premise 的新证据，并按既定目标、风险收缩或异常处置降低风险。同质仓位按比例缩小只会同比降低回报和风险，不会改变每单位期望的正负；是否保留、减少或按原 scale-in 计划增加数量，仍由当前 price action、总风险和原 premise 决定。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-SCALE-IN-TRENDS`、`SRC-POSITION-SIZE`、`SRC-TRADING-RANGES`、`SRC-STOP-ORDERS`、`SRC-COURSE-01-36`（课程 30B、35A–36B）与 `SRC-COURSE-37-52`（课程 43C–47C、51D、52A–52B）。
