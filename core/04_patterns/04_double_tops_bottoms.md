# 双顶、双底和旗形变体

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## Double Top / Double Bottom

双顶和双底表示市场第二次测试某个区域。第二次测试失败时，说明突破或延续遇到阻力。

两个测试本身就构成形态；跌破中间 swing low 或突破中间 swing high 是后续确认，不是“双顶/双底成立”的必要定义。两个高低点只需位于近似价格区域，不要求完全相等。

它们的含义取决于上下文：

- 区间顶部的双顶可能支持卖出。
- 区间底部的双底可能支持买入。
- 熊趋势中的双顶可能是 double top bear flag。
- 牛趋势中的双底可能是 double bottom bull flag。

## Neckline、确认与结果分支

双顶的 neckline（颈线）是两次顶部之间的 swing low；双底的 neckline 是两次底部之间的 swing high。双顶下破 neckline 或双底上破 neckline，会破坏旧趋势所需的高低点序列，因此确认的是一次反转尝试：旧趋势可能结束，但后续仍可能只是 trading range，不能把一次越界直接写成相反趋势已经确认。

形态高度可以从近似顶/底区域到 neckline 估算，再从有效突破处向突破方向投射 measured move。它只是候选目标；neckline 和投射起点可能不止一个，实际目标选择、剩余空间与管理统一回到[支撑阻力与目标](../02_context/01_support_resistance_targets.md#量度目标)。

若已经确认的双顶下破后来失败，价格重新上穿 neckline 并恢复上涨，可以提出相反方向的向上量度假设；已确认双底上破后的向下失败分支完全镜像。必须保留“先突破、再失败、重新接受”的事件顺序，不能仅凭价格当前位于 neckline 哪一侧追认失败。突破质量见[突破和突破模式](../01_market_cycle/03_breakouts_and_breakout_mode.md)，重新进入、接受和失败证据见[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)。

## Double Top / Bottom Flag

Double top bear flag 与 double bottom bull flag 是同一延续逻辑的双向镜像：

| 当前控制 | Pullback 测试 | 失败事实 | 延续证据 |
| --- | --- | --- | --- |
| 熊趋势仍偏空 | 反弹两次测试近似高位 | 第二次测试不能改变空头控制 | 空头恢复并获得跟进 |
| 牛趋势仍偏多 | 回调两次测试近似低位 | 第二次下探没有破坏多头结构 | 多头恢复并获得跟进 |

前者称 double top bear flag，后者称 double bottom bull flag。表格保留完整多空镜像，但不重复两套同构判断清单；实际 target space、stop 和管理由 Setup 与 Trade Plan 决定。

## Micro Double Top / Bottom

微型双顶或双底发生在相邻或近邻 K 线中，常作为 signal bar 附近的辅助证据，也可能承担延续功能：

- Micro double bottom 在 bear spike 中可以是一根 one-bar bear flag；出现在 bull flag 末端时，也可以成为向上的 reversal setup。
- Micro double top 在 bull spike 中可以是一根 one-bar bull flag；出现在 bear flag 末端时，也可以成为向下的 reversal setup。

因此微型双测试不天然等于反转；名称、当前趋势和它所在的 pullback 语境必须一起读取。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-COURSE-01-36`（课程 09B、21D、22A–22D、25A，以及 25B p2103–2115 的 neckline、量度与失败链；27A–27B）与 `SRC-COURSE-37-52`（课程 38A–39D）。
