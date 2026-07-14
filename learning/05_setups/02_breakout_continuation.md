# 突破延续 Setup

> **状态：Learning / Non-normative**
>
> 用于概念学习；价格行为结论由本页、相关学习专题与来源共同支持。

## 它解决什么问题

突破延续 setup 试图跟随市场离开旧价格区域。它下注的是新价格将被或已经被接受，而不是“高低点刚越界”这一事实本身。

## 结构骨架

以向上突破为例，向下镜像：

```text
清楚的旧边界 / 交易区间 -> 强牛突破收在边界外
                         -> follow-through 或回踩守住突破点
                         -> 旧区域未被重新接受
                         -> 向新价格区域的第一障碍或量度目标推进
```

单次越界只形成 breakout attempt。延续结构还要检查：

- 突破 K 线的实体、收盘位置和连续性是否足以说明一方控制。
- Follow-through 是否延伸突破，或者回踩是否守住突破点并形成新的 higher low / lower high。
- 价格是否保留在旧边界外；反方能否快速收回并在旧区域内获得跟进。
- 新区域内的目标空间是否足以补偿较差 entry 和真实 structure stop。

## 入场方式

需要区分两个版本：

- 预判版本：breakout mode 的初始 stop entry，或强 breakout bar 的 close entry。价格较早，但确认更少。
- 确认版本：follow-through、回踩守住、failed failure 后再次触发。概率可能更高，但入场更差、stop 更远或剩余目标更近。

强突破可能不给舒服回踩。等待回踩能改善 stop 结构，但也可能错过；两种版本必须分别评估 entry、stop、目标、概率和 Trader's Equation，不能把确认版本的概率套给早期价格。

## Premise 失效和止损

多头 premise 是“市场已经或正在接受旧边界上方的新价格”。价格只回测突破点并不构成失败；若它明确回到旧区域，并以反向跟进显示旧区域重新被接受，延续 premise 才失效。空头镜像。

直接追随强 breakout 时，顺势初始 stop 可以放在完整 breakout leg 外；后续新强突破形成 major higher low / lower high 后，再按新结构推进保护。Breakout pullback 和 failed failure 没有跨图表统一的 stop 位置，仍要使用能够否定当前接受结构的 price-action stop：

- **直接追随强突破**：完整 breakout leg 的另一端可以作为初始 price-action stop；不能自动缩到最近一根 K 线外。
- **Breakout pullback**：回踩 swing 极值或突破失败边界可以提供 price-action stop，前提是越过该点确实意味着旧区域重新被接受。
- **Failed failure 后再次触发**：反方收回尝试的完整极值可以提供 stop，仍须结合当前 breakout 结构判断。

确认越多通常意味着 entry 更差、stop 可能更远、剩余 reward 更小，因此各版本必须使用自己的 entry、stop、概率和仓位。

## 价格行为预期

Breakout 的最低预期只是继续一点；强 breakout 才经常支持更大的目标。强突破通常同时意味着较高的成功概率、较宽的正确 stop，以及形成 measured move 的可能。强 breakout 后，至少形成第二腿是常见的 minimum goal。

Measured move 的测量方法由被突破的结构和后续腿决定：

- 交易区间、三角形、旗形或其他边界清楚的 pattern，可以从 breakout point 投射其高度。
- 连续强 breakout bars 形成清楚的 breakout leg 时，可以复制该 breakout 的大小。
- 第一腿完成并回调后，可用 Leg 1 = Leg 2 估计第二腿。
- Gap 或 micro measuring gap 只有在特定图上确实提供运动中点或量度参照时才参与；多数 breakout measured move 并不需要 gap。

## Profit targets

1. 先写清“突破了什么”，再选择与该结构匹配的投射；没有清楚测量对象时，只保留“继续一点”的最低预期和前方 support/resistance。
2. 标出 measured move 之前的旧高低点、更大周期支撑阻力、整数位、趋势/通道线等 magnets。强 breakout 可以计划穿越较小障碍，但必须把它们对到达概率的影响算进 Trader's Equation。
3. 当 breakout 足够强、投射清楚且前方没有更重要障碍时，measured move 可以成为 profit target。若更近的支撑阻力显著降低到达概率，可以在那里兑现，或在原计划已包含分批管理时只让部分仓位继续尝试投射目标。
4. 实际获利价通常放在目标区域近侧。高概率突破有时只需较小 reward/risk 仍可合算，但必须使用真实宽 stop 和较差 entry 计算，不能只看目标距离。

Breakout gap、body gap 和 micro gap 主要帮助判断突破是否被接受、回踩是否守住以及趋势强度；只有它们同时构成明确支撑阻力或量度参照时，才直接进入 target 计算。

## 主要风险

突破交易通常概率较高，但风险回报可能较差。若突破没有跟进，追随者容易成为 trapped traders。

Gap 被进入或回补只说明突破强度证据减弱；如果突破回到旧区域并获得反向跟进，原突破延续命题才明确失效。Failed breakout 只生成新的回归或反转候选，仍需从当前价格重新评估背景、触发、止损、目标和 Trader's Equation；不能把原仓位机械反手。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-BREAKOUTS-2025` 与 `SRC-LIVE-TR-BO-2021`。
