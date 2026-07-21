# 缺口（Gaps）

> **状态：Core / Definition**
>
> 本文只界定 gap 词汇和实时命名边界；具体 Context、Setup、target 与 management 回到各自专题。

## Gap 的最低含义

Brooks 语境中的 gap 不只指隔夜跳空。任何两个支撑阻力对象之间缺少充分双边交易的价格空间，都可能称为 gap；分析时必须先写清比较对象和两个边界。

Gap 本身不是方向判断或入场许可。它只有在实际改变强度、接受/拒绝、支撑阻力、路径障碍或目标时才需要进入判断。

## 术语边界

| 名称 | 最低边界 | 成立时点 |
| --- | --- | --- |
| Opening gap | 当日第一根开盘越过昨日最后一根 K 线或整个昨日范围的高/低 | 开盘即可确认几何事实 |
| Gap reversal | 当前 K 线向 gap 方向越过前一根 K 线至少一跳 | 只能确认初始反向事件，不表示 gap 已回补或反向已被接受 |
| Body gap | 回测时影线可以重叠，但两个参照 K 线的实体仍不重叠 | 实体关系出现时可确认 |
| Micro measuring gap | 强趋势 K 线前后两根 K 线的完整范围不重叠 | 完整范围关系出现时可确认 |
| Moving-average gap bar | 整根 K 线没有触及均线 | 当根完成时可确认 |
| Measuring gap | 最终带来 measured move 的 breakout | 实时只能称 candidate measuring gap，达到结果后才能确认 |
| Exhaustion gap | 趋势后期异常顺势运动后，已经出现获利了结和至少小反转 | 大 K 线出现时只能称 potential exhaustion |

同一个开放空间在趋势建立阶段可能支持 strength，在成熟趋势末端可能只是 potential exhaustion。结果出现前，不能用事后名称替代当时可观察事实。

## 怎样使用这些词

- Opening gap 的 session context 和方向边界见[周期与时段 Context](../02_context/02_time_and_timeframes.md)。
- Breakout、body gap 和 micro measuring gap 对强度与接受的作用，回到[突破和突破模式](../01_market_cycle/03_breakouts_and_breakout_mode.md)及[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)。
- Moving-average gap bar 作为趋势延续线索时，回到[趋势延续 Setup](../05_setups/01_trend_continuation.md#moving-average-gap-bar)。
- Gap 边界作为 magnet、路径障碍或 measured-move 参照时，回到[支撑阻力与目标](../02_context/01_support_resistance_targets.md)。
- Exhaustion 只有放回趋势成熟度和状态转换中才有意义，见[高潮与状态转换](../01_market_cycle/04_climax_and_transition.md)。

Gap 被进入或回补只说明原证据发生变化。没有旧区域重新获得接受和反向 follow-through，不能仅凭“gap 消失”宣布趋势反转；也不能因“gap 迟早回补”把它机械设成 target。

## 常见误读

- 把所有 gap 都当作 opening gap。
- 看到 gap up 只做多，gap down 只做空。
- 把 gap reversal 当成完整反转或直接入场信号。
- 事前把任意开放 gap 命名为 measuring gap。
- 仅凭趋势末端大 K 线提前宣布 exhaustion gap。
- 把 gap 边界或中点机械设为 stop 或 target。

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-STRONG-LEGS-2016`、`SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` 与 `SRC-LIVE-TR-BO-2021`。
