# 交易区间 Fade Setup

> **状态：Learning / Non-normative**
>
> 用于概念学习；价格行为结论由本页、相关学习专题与来源共同支持。

## 它解决什么问题

Trading range fade 试图在区间边缘反向入场。它依赖市场仍在围绕公平价格交易，而不是已经接受突破。

## 结构骨架

以区间底部做多为例，顶部做空镜像：

```text
成熟交易区间 -> 测试或短暂跌破下边缘
             -> 向下突破缺乏跟进 / 价格重新进入区间
             -> double bottom、wedge 或 failed-breakout signal 向上触发
             -> 恢复区间内轮动；下半区多头通常在上半区兑现
```

结构必须同时回答：

- 区间是否已经通过多次双向测试和重叠得到确认，而不是一个仍在形成的短暂停顿。
- Entry 是否确实位于边缘或边缘外，而不是中部。
- 突破方是否缺乏跟进，价格是否重新进入旧区域，反向是否出现可交易触发。
- 到区间内部支撑阻力、上半区或其他计划目标是否仍有足够现实空间。

## 常见形态语言

- Failed breakout。
- Double top / double bottom。
- Wedge at edge。
- Signal failure。
- Trapped breakout traders。

这些都不是独立信号，必须放回 trading range 的位置和双边行为中理解。

## Premise 失效和止损

多头 premise 是“向下测试没有被接受，价格仍将在旧区间内围绕公平价值交易”。若价格离开下边缘后出现强突破和持续跟进，或重新跌破 failed-breakout 极值并在区间外被接受，fade premise 失效；空头镜像。

宽区间交易需要使用 reasonable stop；limit entry 的 stop 有时必须很远，区间边界或 failed-breakout 极值都不是统一默认 stop。不同入场方案可以使用不同的 price-action stop：

- Failed breakout 后的 stop entry，可以把 failed-breakout 完整极值作为候选锚点，但只有越过它足以说明突破方向重新被接受时才成立。
- 边缘内侧的确认入场，可以评估反向结构 swing 外的较近 stop；它与边缘外的完整结构 stop 是两个不同概率和仓位方案。
- Limit probe 或事前设计的 scale-in 可能需要允许更深的边缘外测试，因此所选 structural / price-action stop 更宽、仓位更小；这一 stop 和全部计划数量的总风险应在第一笔 entry 前一起评估。

区间边界本身不是自动止损线。对本页所选的 structural / price-action stop，锚点应位于足以否定当前 fade 结构的位置外，并给正常的边缘 overshoot 留出空间。Stop 较宽不自动表示它是 catastrophe stop；两者按用途区分，而不是按距离命名。

交易者也可以另设更远的 catastrophe stop，作为无法继续管理、连接中断或其他意外情况下的后备保护。它不等于本页的结构失效线，也不能替代持续判断 premise。强突破与持续跟进、区间外重新获得接受，或其他足以否定原 fade premise 的价格事实已经出现时，应在 catastrophe stop 触发前退出；不能因为后备保护仍很远而继续依赖希望。

## 价格行为预期

Trading range 的核心逻辑是 buy low, sell high, scalp。多头可在区间下半部建立仓位，并在上半部获利；空头镜像。这不等于每笔 fade 都必须持有到另一侧边缘，也不把 midpoint 规定为统一目标。

宽区间存在多种合理兑现方式：在合格 minimum scalp 之上，可按约 1–2 倍当前实际风险兑现；若区间持续形成大幅双向 swing，也可以让部分仓位争取更远区域。目标随 entry、scale-in、stop 和区间宽度变化，不存在一个脱离方案的固定点数。

## Profit targets

1. 先按 scalp 设计。区间底部多单沿途检查前 swing、均线、开盘价、区间中部和其他内部阻力；选择能够形成合格 Trader's Equation 的现实兑现位置。顶部空单镜像。
2. 区间中部可以是近端支撑阻力或保守兑现区域，但不是所有 fade 的统一目标。若 entry 位于下半区且区间足够宽，多头可计划在上半区获利；空头镜像。
3. 若计划保留仓位争取另一侧边缘，必须把区间内部障碍和相应到达概率纳入原 Trader's Equation。突破另一侧后的区间高度 measured move 属于新的 breakout premise，需要重新评估。
4. Gap、opening price、均线或 measured move 只有在当前区间内实际形成支撑阻力、路径障碍或风险边界时才相关。

区间 fade 的合理 stop 有时比看上去宽得多，因此不能只用边缘到中轴/上半部的图上距离判断交易“完美”。若扣除成本后没有合格 scalp 空间，正确动作仍是等待。

成熟宽区间边缘可以有小仓 limit probe，也可以等待 failed breakout 后的 stop entry；两种入场的确认程度、价格、止损和概率不同，必须分别评估 Trader's Equation。区间中部回避，紧区间若扣除成本后没有足够 scalp 空间，多数交易者应等待。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-MANUAL`、`SRC-TRADING-RANGES`、`SRC-STOP-ORDERS`、`SRC-SCALE-IN-TRENDS`、`SRC-STRONG-LEGS-2016`、`SRC-GOOD-TRADE-2017` 与 `SRC-HOLDING-WIDE-STOPS`。
