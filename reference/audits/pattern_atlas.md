# 88 图形的官方来源与几何审计

> **状态：Evidence Audit / Non-normative**

本文件记录根目录 `al-brooks-pattern-atlas.html` 的来源层级、定义边界和绘图验收规则。它不定义交易动作；执行以当前[执行手册](../../README.md#权威层级)为准。统一来源编号见 `reference/official_sources.md`。

## 来源层级

1. `SRC-GLOSSARY`：[Brooks Trading Course Glossary](https://www.brookstradingcourse.com/price-action-trading-terms-glossary/)——术语最低定义和 K 线关系的首要依据。
2. `SRC-10-PATTERNS`：[10 Best Price Action Trading Patterns](https://www.brookstradingcourse.com/price-action/10-best-price-action-trading-patterns/)——H1/H2、旗形、楔形、MTR 等面向交易者的概述；与 glossary 出现宽松措辞差异时，在图中保留 stop-entry 的严格触发语义。
3. `SRC-STRONG-LEGS-2016`：[Distinguishing Strong Legs: Trading Ranges vs Trends](https://www.brookstradingcourse.com/wp-content/uploads/2016/05/Al-Brooks-Webinar-Distinguishing-Strong-Legs-TR-vs-Trends-May-3-2016.pdf)——强趋势、紧通道、宽通道和交易区间的视觉差异。
4. `SRC-MTR-2025`：[Major Trend Reversals coaching session](https://www.brookstradingcourse.com/wp-content/uploads/2025/08/250830-Coaching-Session-3-MTRs.pdf)——MTR 的成熟趋势、趋势线破坏、旧极值测试和反向跟进。
5. `SRC-OPENING-REVERSALS-2017` 与 `SRC-PATTERNS-OPEN-2018`：[Opening Reversals](https://www.brookstradingcourse.com/wp-content/uploads/2017/10/171017-Futures.io-Presentation-Opening-Reversals-Al-Brooks.pdf)、[Patterns on the Open](https://www.brookstradingcourse.com/wp-content/uploads/2018/10/181030-futuresio-Patterns-on-the-Open-Al-Brooks.pdf)——opening reversal、trend from the open 和开盘后形态。
6. `SRC-ENCYCLOPEDIA-SAMPLER` 和 `SRC-ASK-AL` 用于补充语境，不覆盖 glossary 的最低定义。

## 审计原则

- 先验证 OHLC 几何，再验证看起来是否像；标记必须落在真实 high / low 上。
- 定义、质量和确认分开。例：越过重要价位已经是 breakout；近极值收盘和 follow-through 决定它是否强、是否成功。
- “常见外观”不是必要条件。楔形不必完美收敛，two-bar reversal 的第二根不必吞没第一根，牛旗也不必浅。
- 镜像形态必须保持同一逻辑，而不是只把颜色反转。
- 相似卡片要用可比较的尺度表达本质差异；尤其 tight channel 与 broad channel、trend from open 与普通 trend day。

## 逐组覆盖矩阵

| 编号 | Atlas ID | 官方定义锚点 | 图形验收重点 | 状态 |
| --- | --- | --- | --- | --- |
| 1–4 | `trend-bar`, `doji`, `shaved-bar`, `tail` | Glossary: Trend Bar, Doji, Shaved Body, Tail | 普通趋势 K 与强趋势 K 分层；doji 按相对实体；shaved 只表示一端/两端无影线；tail 是实体至极值的范围 | 已校准 |
| 5–6 | `reversal-bar`, `two-bar-reversal` | Glossary: Reversal Bar, Two-Bar Reversal | 反转 K 是原运动反方向趋势 K，旧极值测试只是加强项；第二根允许 inside，不强制 engulf | 已校准 |
| 7–8 | `inside-bar`, `outside-bar` | Glossary: Inside Bar, Outside Bar | inside 使用 `H≤前H且L≥前L`；outside 至少一侧严格越过，另一侧可相等 | 已校准 |
| 9–13 | `pullback-pause-bar`, `ii-iii`, `ioi`, `oo`, `signal-entry-bar` | Glossary: Pullback Bar, Pause Bar, ii, ioi, oo, Signal/Entry Bar | pause 与 bar pullback 使用不同几何测试但允许重叠；iii 画满母 K + 三根 inside；Signal/Entry 按实际成交后的订单角色标记 | 已校准 |
| 14–15 | `bull-trend`, `bear-trend` | Glossary: Bull/Bear Trend；Strong Legs PDF | 相对大的顺势实体、近极值收盘、浅且明显更弱的反向 K；多空严格镜像 | 已校准 |
| 16–17 | `tight-channel`, `broad-channel` | Glossary: Tight/Broad Channel；Strong Legs PDF | 紧通道窄、1–3 根浅回调、逆势弱；宽通道是倾斜区间，3–10 根深回调、双向强腿和更多重叠 | 已校准 |
| 18–21 | `spike`, `spike-channel`, `small-pullback-trend`, `micro-channel` | Glossary 对应条目 | spike 用连续大趋势 K；channel 阶段斜率和实体下降；小回调趋势回调浅；micro-channel 图采用“牛向每根低点不低于前低”的严格无回调子型，不冒充全部定义 | 已校准 |
| 22–26 | `stairs`, `shrinking-stairs`, `leg-two-legs`, `climax`, `overshoot` | Glossary 对应条目 | 新极值间距、两腿停顿、加速与通道线越界必须由实际摆动表达；`climax` 图必须在过快过远后显示已反向 / 区间化，单独 overshoot 仍只是线索 | 已校准 |
| 27–30 | `trading-range`, `tight-trading-range`, `barbwire`, `broad-trading-range` | Glossary: Trading Range, TTR, Barbwire | Barbwire 至少 3 根高度重叠、显著影线、至少 1 doji，K 线可较大；宽区间必须有可交易摆动空间 | 已校准 |
| 31–33 | `triangle`, `expanding-triangle`, `breakout-mode` | Glossary 对应条目 | 收敛/扩张用真实摆动极值；BOM 是双向概率状态，不限于压缩 | 已校准 |
| 34–38 | `breakout`, `failed-breakout`, `failed-failure`, `breakout-pullback`, `breakout-test` | Glossary: Breakout, Breakout Test；Stop Orders manual | 越界与成功分开；failed failure 在恢复触发处标记；BT 测试原 stop-entry / breakeven 价，可早可晚 | 已校准 |
| 39–41 | `ledge`, `measured-move`, `vacuum-test` | Glossary 对应条目 | 牛 ledge 相同低点、熊 ledge 相同高点；量度投射长度相等；vacuum 到达目标后才判断接受/拒绝 | 已校准 |
| 42–43 | `bull-flag`, `bear-flag` | Glossary 与 10 Best Patterns | 旗形可一根也可很深，核心是 Always In 背景和随后顺势恢复 | 已校准 |
| 44–49 | `h1`, `h2`, `l1`, `l2`, `h2-bull-flag`, `l2-bear-flag` | Glossary；10 Best Patterns；Stop Orders manual | H/L 候选按本根极值严格越过前根极值绘制，相等不计数；候选、second signal 和实际 second entry 分开；H2/L2 可像微双底/顶但不是必要外观 | 已校准 |
| 50–52 | `double-bottom-bull-flag`, `double-top-bear-flag`, `wedge-flag` | Glossary 与 10 Best Patterns | 延续背景优先；wedge flag 的三次推动清楚，不强制收敛或逐推衰减 | 已校准 |
| 53–58 | `double-top`, `double-bottom`, `micro-double-top`, `micro-double-bottom`, `double-top-pullback`, `double-bottom-pullback` | Glossary 对应条目 | 两次真实 swing test 定义形态，neckline 只确认；micro double 可延续也可反转；所有标签锚定真实极值 | 已校准 |
| 59–63 | `wedge`, `wedge-reversal`, `parabolic-wedge`, `micro-wedge`, `nested-wedge` | Glossary；10 Best Patterns | 三推标记落在真实 swing；不强制几何收敛；反转图必须显示反向触发/跟进；nested 同时呈现大、小三推 | 已校准 |
| 64–66 | `final-flag`, `head-shoulders-top`, `head-shoulders-bottom` | Glossary 对应条目 | Final flag 需趋势后期、目标/磁吸和失败的最后突破；H&S 多数仅带来 minor reversal，颈线跟进决定升级 | 已校准 |
| 67–70 | `hh-mtr`, `lh-mtr`, `ll-mtr`, `hl-mtr` | MTR coaching PDF；Ask Al MTR | 成熟趋势 → 两点定义的主要趋势线 → 实际破线 → 旧极值 HH/LH/LL/HL 测试 → 反向跟进 | 已校准 |
| 71 | `minor-reversal` | Glossary: Minor Reversal, TBTL | 只画小回调/区间化，不把两根 K 线标作 TBTL | 已校准 |
| 72–73 | `gap-up`, `gap-down` | Glossary: Gap Up/Down | 由开盘价越过前一范围定义，不要求整根 K 与前一根完全分离 | 已校准 |
| 74–75 | `body-gap`, `micro-gap` | Glossary: Body Gap, Micro Measuring Gap | Body Gap 比较突破 K 与约 5–10 根后的测试 K，影线可重叠而实体不重叠；微量度缺口比较强趋势 K 前后两根完整范围 | 已校准 |
| 76–78 | `breakout-gap`, `measuring-gap`, `exhaustion-gap` | Glossary 对应条目 | 突破缺口区域持续开放；量度缺口投射等长运动；衰竭缺口需显示趋势后期异常运动后已出现至少小反转，快速回补只是一种示例而非定义 | 已校准 |
| 79–80 | `failed-gap`, `ma-gap-bar` | Glossary 对应条目 | failed gap 回到旧区域并反向；MA gap bar 的整根高低区间与 EMA 不相交 | 已校准 |
| 81–83 | `opening-range`, `opening-range-breakout`, `opening-reversal` | Opening Reversals / Patterns on the Open PDFs | OR 只框早期实际范围；ORB 从真实框顶/底派生边界；opening reversal 同时显示支撑/阻力/磁吸目标 | 已校准 |
| 84–88 | `trend-from-open`, `trend-day`, `trading-range-day`, `reversal-day`, `breakout-day` | Patterns on the Open PDF；Glossary day/open terms | TFO 早段无 bar pullback 且起始极值保持；普通趋势日允许受控回调；区间日用多 K 线双向腿；反转日不强制完整回测；breakout-day 明确为实用结构标签 | 已校准 |

## 防回归几何检查

- `tightChannelBars` 的反向段必须明显短于顺势段；`broadChannelBars` 至少包含数段 3 根以上的深回调，且两者使用可比纵轴。
- `reversalBar` 的反转 K 可以不越过旧极值；`twoBar` 第二根必须保留 inside 示例。
- `inside` 至少保留一侧相等示例；`outside` 至少保留一侧相等、另一侧严格突破示例。
- `ii` 必须包含母 K、i、ii、iii 和随后突破，不能只显示两根 inside。
- Double Top/Bottom、Wedge、MTR 的数字/字母标记必须来自真实 high / low，而不是 close。
- 四种 MTR 都要显示趋势线被价格实际穿越，以及之后对旧极值区域的 HH/LH/LL/HL 测试。
- Body Gap 必须允许影线重叠而实体不重叠；Micro Measuring Gap 必须让强趋势 K 前后两根范围不重叠。
- Measuring Gap 的前后投射必须等长；当前 Exhaustion Gap 图若画出回补，高亮区域在本例回补 K 处结束，但不得把快速回补当成术语必要条件。
- Trend From Open 的顺势序列不得出现 bar pullback；Trend Day 至少有一次真实、受控的 bar pullback；Trading Range Day 至少有多根组成的上、下腿。
- 页面固定渲染 88 张卡；筛选、搜索和展开详情在桌面与手机宽度都必须可操作，控制台不得出现 error 或 warning。
