# 趋势延续 Setup

> **状态：Learning / Non-normative**
>
> 用于概念学习；价格行为结论由本页、相关学习专题与来源共同支持。

## 它解决什么问题

趋势延续 setup 试图顺着当前控制方入场。典型场景是强趋势或有效通道中出现回调，反方尝试失败，原趋势恢复。

## 结构骨架

以多头为例，空头镜像：

```text
既有牛趋势 -> 回调但主要 higher low 未被破坏
           -> 空头缺乏跟进 / 二次下探失败
           -> H2、wedge pullback 或 double bottom bull flag 向上触发
           -> 原趋势恢复；按 scalp / swing 计划测试前方 magnet
```

结构需要同时包含：

- Always In 或其他控制证据仍偏向原趋势方。
- 回调深度、持续时间和重叠仍符合当前趋势/通道，而不是已经转成交易区间或反向突破。
- 回调位于可解释的位置，并保留到本次 scalp 或 swing 目标的现实空间。
- H2/L2、wedge pullback、double bottom bull flag 或 double top bear flag 只负责组织回调和触发，不单独证明趋势仍在。

趋势延续常用 stop entry，让价格先越过 prospective signal bar 并证明原趋势正在恢复。强趋势中的普通 signal bar 可能足够；宽通道或接近目标时，需要更好的位置、触发和目标空间。

## Premise 失效和止损

多头 premise 是“回调仍是牛趋势内的测试，原控制方会恢复”。若价格有效跌破定义该回调的低点或主要 higher low，并出现足以把市场改读为交易区间或反向运动的跟进，premise 失效；空头镜像。

H2/L2 的 swing 管理需要使用正确的 price-action stop，但所有旗形并不共用一个固定锚点。顺势 swing 的 stop 常参考最近 major higher low / lower high、完整回调极值，或其他足以说明趋势 premise 已失效的位置；具体选择取决于当前趋势和回调结构。

Signal-bar stop 只有在 signal bar 另一端同时就是合格的 price-action stop 时才足够。若合理 stop 更远，应缩小仓位或等待，不能为了缩短风险距离把 stop 放进正常回调。

Gap 被进入或回补本身只表示原趋势强度证据减弱。Premise 是否失效还要看更广的价格行为，例如旧区域是否被重新接受、所依赖的 swing 是否被破坏，以及反向运动是否获得跟进；不能把任意 gap 边界或 gap 中点机械当 stop。

## 价格行为预期

H2/L2 的典型逻辑是：反趋势方两次尝试失败后，原趋势恢复，运动通常较快。交易者经常 scalp 这类 setup；只有趋势仍强时，才 swing 部分或全部仓位。因此，“H2/L2 的目标”不是一个固定价位，而先取决于这笔交易到底是 continuation scalp 还是 trend swing。

不同 continuation 结构的直接价格预期也不同：

- H2/L2、double bottom/top flag 或 wedge pullback 的直接预期是原趋势恢复；具体 profit target 仍由 scalp/swing 选择和前方 magnets 决定，它们本身不保证 measured move。
- 强趋势第一次形成 moving-average gap bar 的深回调，典型预期是随后测试原趋势极值。因此在这个特定 setup 中，旧高/旧低有直接结构依据。
- 若当前 premise 实际是强 breakout 后的 pullback continuation，则按突破结构评估 measured move 或第二腿；普通趋势回调没有这一固定目标。

## Profit targets

1. 先决定是 scalp 还是 swing。Scalp 使用当前波动下足以覆盖成本、并与风险匹配的现实利润；Swing 则需要原趋势仍强，并通常寻找至少约两倍 initial risk 的潜在回报。
2. 沿交易方向标出常见 magnets：旧趋势极值、前高前低、趋势线/通道线、breakout point、均线和其他明显支撑阻力。目标要与本次 setup 和 scalp/swing 计划相符，不能自动使用最远 magnet。
3. 只有当前结构实际给出可复核的第一腿、旗形/区间高度、spike 高度或 micro measuring gap 时，才把 measured move 加入目标地图。
4. Gap 只有在它改变趋势强度、回测支撑阻力或前方路径时才相关；它不是 continuation target 的必填项。

前方 support/resistance 会影响继续持有到更远 target 的概率。不能忽略当前 continuation setup 实际准备采用的目标，只靠一个与结构无关的远端投射制造更好的 Trader's Equation。

## 常见失败

- 把 trading range 中的普通反弹当趋势恢复。
- 在宽通道边缘追随。
- 忽略合理止损太远。
- 把 scalp 入场改成 swing 管理。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-10-PATTERNS`、`SRC-GLOSSARY`、`SRC-TREND-CHANNELS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-RISK-113` 与 `SRC-POSITION-SIZE`。
