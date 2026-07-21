# 趋势延续 Setup

> **状态：Core / Application**
>
> 本文只说明趋势延续区别于其他 Setup 的 premise、结构和结果预期。

## 交易命题

趋势延续 Setup 押注当前控制方仍然有效：回调属于原 trend 或 channel 内的测试，反方未能建立持续控制，原方向将恢复。

以多头为例，空头镜像：

```text
既有牛趋势 -> 回调未破坏主要 higher low
           -> 空头缺乏跟进或二次下探失败
           -> 顺势触发
           -> 测试旧极值或继续原趋势
```

成立时需要同时看到：

- Always In 或其他累积压力仍支持原趋势方。
- 回调深度、持续时间和重叠仍符合当前 trend / channel，而不是已转成交易区间或反向突破。
- 位置保留到现实 magnet 的空间。
- H2/L2、wedge pullback 或 double bottom/top flag 只组织回调和触发，不单独证明趋势仍在。

趋势延续常使用 stop entry 越过 prospective signal bar。H1/H2/L1/L2 的计数见[形态页](../04_patterns/02_h1_h2_l1_l2.md)，second entry 的实际触发边界见[接受与订单逻辑专题](../03_acceptance_and_order_logic/03_second_entries_and_traps.md)。

## Premise 失效与 Stop 差异

多头 premise 在定义回调的低点或主要 higher low 被有效跌破、反向运动获得足以改变 market-cycle 判断的跟进时失效；空头镜像。

Swing stop 常以最近 major higher low / lower high、完整回调极值或其他能否定趋势 premise 的结构为锚点。候选 K 线另一端的 stop 只有在该位置同时就是完整 premise 的失效边界时才足够。合理 stop 更远时，应调整仓位或放弃，不能把 stop 塞进正常回调。

## Moving-Average Gap Bar

Moving-average gap bar 的最低几何定义见 [Gaps](../04_patterns/07_gaps.md)。它在趋势延续中常有两类特定语境：

- 强趋势首次深回调穿过均线后，若整根 K 线来到均线反侧，市场通常仍会测试原趋势极值。牛趋势中该 K 线最高价低于当根均线值；熊趋势镜像。
- 连续约 20 根或更多 K 线未触及均线后，首次触及均线常成为测试原趋势极值的背景。根数是典型线索，不是硬阈值。

第一次朝均线的反转若未能触及均线、价格又远离，下一次朝均线的反转可称 second moving-average gap bar setup。它仍需趋势强度、具体触发和可承担的 stop 支持，不是机械均线挂单规则。

## 结果与目标差异

H2/L2、wedge flag 和 double bottom/top flag 的直接预期只是原趋势恢复。它们可能按 scalp 管理；趋势仍强且空间足够时才支持 swing。Moving-average gap bar 的上述特定语境则直接支持“测试旧趋势极值”的预期。

Measured move 只有在当前走势另有清楚的 breakout leg、旗形高度、Leg 1 = Leg 2 或 micro measuring gap 时才加入；普通趋势回调不会因“continuation”名称自动获得量度目标。目标区域的通用构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)。

## 主要误读

- 把 trading range 中的普通反弹当成趋势恢复。
- 在宽通道边缘或重要目标前追随。
- 只看 H2/L2 计数，忽略原控制是否仍在。
- 为了缩短风险使用无法容纳正常回调的 stop。
- 把 scalp premise 临场改成远端 trend swing。

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-10-PATTERNS`、`SRC-GLOSSARY`、`SRC-TREND-CHANNELS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-RISK-113` 与 `SRC-POSITION-SIZE`。
