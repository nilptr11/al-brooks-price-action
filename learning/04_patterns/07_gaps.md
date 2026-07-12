# Gaps

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../../README.md#权威层级)。

## Gap 是什么

Al Brooks 对 gap 的使用比传统“隔夜跳空”更广：任何两个支撑阻力对象之间的空间都可能被称为 gap，对象可以是 K 线的高低开收、旧 swing、突破点、均线或趋势线。Gap 的核心含义是某段价格没有形成充分的双边交易，因此它可能提供强度、接受/拒绝、支撑阻力和目标线索。

分析任何 gap 时先回答：

1. 比较的是哪两个对象，边界价格是什么？
2. 它发生在什么周期和 market cycle 位置？
3. 当前是保持、被测试、部分进入还是已经失去作用？
4. 后续是同方向跟进，还是回到旧区域并出现反向跟进？

Gap 是 context，不是独立入场信号。只有位置、触发、止损、目标和交易数学共同合格时，才可能形成交易。

## 实时事实与事后名称

| 名称 | 当时能否确认 | 最低边界 |
| --- | --- | --- |
| Opening gap | 能 | 当日第一根开盘越过昨日最后一根 K 线或整个昨日范围的高/低。 |
| Gap reversal | 能确认几何事件 | 当前 K 线向 gap 方向越过前一根 K 线至少一跳；不表示价格已到达 gap 边界、gap 已回补或反向已被接受。 |
| Body gap | 能 | 回测时影线可以重叠，但两个参照 K 线的实体仍不重叠。 |
| Micro measuring gap | 能 | 强趋势 K 线前后两根 K 线的完整范围不重叠。 |
| Moving-average gap bar | 能 | 整根 K 线没有触及均线。 |
| Measuring gap | Breakout 形成时只能记候选 | 只有该 breakout 最终带来 measured move 后才确认。 |
| Exhaustion gap | 大 K 线形成时只能记 potential | 趋势后期异常大的顺势 K 线或连续 K 线之后，已经出现获利了结和至少小反转时才确认。 |

这种区分很重要：同一个开放空间在趋势早期可能是 strength，在成熟趋势末端可能只是 potential exhaustion；后续行为出现前不能用结果名称替代当时判断。

## Opening Gap 与 Gap Reversal

Opening gap 只说明市场在开盘时重新定价，不决定当天方向。Gap down 后可以继续形成熊趋势，也可以因强买压发展成 bull trend from the open；gap up 同样可能延续、横盘或反转。

接受新价格的常见证据：

- 开盘方向获得连续趋势 K 线和 follow-through。
- 回踩无法进入旧价格区域。
- Gap 边界或昨日高低点转为有效支撑阻力。
- 反方信号反复失败。

拒绝新价格的常见证据：

- 价格进入 gap 并回到旧区域。
- 开盘方向缺乏跟进。
- 出现反向强 K 线、二次信号或 failed breakout。
- 回到旧区域后得到反向 follow-through。

官方 gap reversal 的最低定义是当前 K 线向 gap 方向越过前一根 K 线至少一跳；例如 gap up 后第二根跌破第一根低点一跳。它是拒绝路径的早期事件，不保证价格已经触及真正的 gap 区域，更不是交易许可；开盘案例中更可靠的反转通常还要结合昨日高低点、二次信号、signal bar 和后续跟进。

## 突破形成的空间、Body Gap 和 Micro Measuring Gap

Breakout 收盘越过旧高低点或其他重要边界时，突破更强；收盘与旧边界之间的空间经常成为 measuring-gap 候选，并可在回测时承担支撑阻力作用。

Body gap 常在突破后的回测中出现：影线已经重叠，但实体仍不重叠。官方 glossary 用突破后约 5—10 根的回调举例，这只是典型案例，不是形成 body gap 的固定时间阈值。Body gap 比完整价格 gap 弱，但仍是接受和强度证据。

Micro measuring gap 比较强趋势 K 线前后两根 K 线的完整范围。牛例中，后一根低点不低于前一根高点；熊例镜像，两条边界的中点是官方给出的量度参考。它经常支持至少第二腿或 measured move，但不提供确定概率，也不免除对路径障碍和剩余时间的检查。

这些 gap 后续被进入或回补，只表示原强度证据削弱。没有回到旧区域和反向跟进时，不能仅凭“gap 消失”宣布趋势反转。

## Moving-Average Gap Bar

Moving-average gap bar 是整根 K 线不触及均线。官方 glossary 特别关注两种语境：

- 强趋势首次深回调形成均线缺口 K 线后，市场通常还会测试原趋势极值。
- 连续约 20 根或更多 K 线未触及均线后，首次触及均线常形成测试原趋势极值的 setup。

出现第一次 moving-average gap bar 后，如果随后朝均线的反转未能触及均线、价格又继续远离均线，那么下一次再次朝均线的反转称 second moving-average gap bar setup。

这些都是趋势背景和 setup 线索，不是机械在均线挂单的理由；仍要检查趋势是否强、当前触发是否成立，以及正确 stop 是否可承受。

## Measuring Gap 与 Exhaustion Gap

Measuring gap 的官方最低定义是最终带来 measured move 的 breakout。多数目标首先按突破前交易区间或形态高度投射；在特定图表中，也可以把 gap 的中点或靠近运动起点的一侧边缘当作量度参考。实时只能记录“候选 measuring gap”，并持续检查 gap 是否开放、突破是否被接受以及目标前是否存在更近障碍。

Exhaustion gap 出现在趋势后期：异常大的顺势 K 线或连续 K 线之后，获利了结增加并已经出现至少小反转。它不要求快速或完整回补，但仅凭“大 K 线”“图表右侧”或 gap 开始被测试，仍不能提前逆势。多数高潮先转成交易区间；主要反转还需要结构破坏、旧极值测试失败和反向持续压力。

## 在市场判断中的作用

- **强度**：保留的 breakout、body 或 micro gap 表示重叠少，一方控制更强。
- **接受/拒绝**：Gap 边界守住支持新价格被接受；回旧区域并获得反向跟进支持拒绝。
- **市场周期**：早期 gap 常支持 breakout 或 tight channel；成熟趋势末端的大 gap 需要同时观察 climactic behavior。
- **支撑阻力**：Gap 边界、突破点和旧价格区域可能成为回测位置或 trapped traders 的退出位置。
- **目标**：Gap 可以构成回补目标、路径障碍或 measured-move 参考，但不能保证到达。
- **止损**：Gap 边界只有在越过它确实否定交易想法时才是合理锚点，不能机械使用 gap 中点。

## 常见误读

- 把所有 gap 都当作传统 opening gap。
- 看到 gap up 就只做多，gap down 就只做空。
- 把 gap reversal 当成完整反转或直接入场信号。
- 把官方 body-gap 案例中的 5—10 根当成硬阈值。
- 事前把任意开放 gap 命名为 measuring gap。
- 仅凭趋势末端大 K 线提前宣布 exhaustion gap 并逆势。
- 看到 gap 被填就宣布反转，忽略旧区域是否被重新接受和反向 follow-through。

来源审计见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-STRONG-LEGS-2016`、`SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018`、`SRC-LIVE-TR-BO-2021`，以及 [`reference/audit_matrix.md`](../../reference/audit_matrix.md)。
