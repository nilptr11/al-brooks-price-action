# 突破延续 Setup

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../README.md#权威层级)。

## 它解决什么问题

突破延续 setup 试图跟随市场离开旧价格区域。它下注的是新价格将被或已经被接受，而不是“高低点刚越界”这一事实本身。

## 判断重点

- 突破是否强。
- 是否有连续性和 follow-through。
- 回踩是否守住突破点。
- 突破收盘与旧边界之间的空间、body gap 或 micro gap 是否保留；它们是强度证据，不是必要条件。
- 反方是否无法快速收回。
- 目标空间是否足够补偿较差入场价格。

## 入场方式

需要区分两个版本：

- 预判版本：breakout mode 的初始 stop entry，或强 breakout bar 的 close entry。价格较早，但确认更少。
- 确认版本：follow-through、回踩守住、failed failure 后再次触发。概率可能更高，但入场更差、stop 更远或剩余目标更近。

强突破可能不给舒服回踩。等待回踩能改善 stop 结构，但也可能错过；两种版本必须分别评估 entry、stop、目标、概率和 Trader's Equation，不能把确认版本的概率套给早期价格。

## Stop 和目标

直接追随强 breakout 时，正确 stop 可能在完整 breakout leg 的另一端，而不只是最近一根 K 线外；确认入场则常使用回踩结构和突破失败边界。确认越多通常意味着 entry 更差、stop 可能更远、剩余 reward 更小，因此仓位必须随真实 stop 距离调整。

目标先列支撑阻力、旧极值和其他 magnet；若存在清晰测量结构，再计算区间/形态高度或 breakout height measured move。强且被接受的 breakout 可以把投射作为主要目标；若突破较弱或前方有明显阻力，更远投射只是延伸候选。实际获利价通常放在目标区域近侧，而不是要求市场先越过理想投射。

## 主要风险

突破交易通常概率较高，但风险回报可能较差。若突破没有跟进，追随者容易成为 trapped traders。

Gap 被进入或回补只说明突破强度证据减弱；如果突破回到旧区域并获得反向跟进，原突破延续命题才明确失效。Failed breakout 只生成新的回归或反转候选，仍需从当前价格重新评估背景、触发、止损、目标和 Trader's Equation；不能把原仓位机械反手。

来源审计见 `reference/official_sources.md` 中的 `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-BREAKOUTS-2025` 与 `SRC-LIVE-TR-BO-2021`。
