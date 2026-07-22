# Al Brooks 价格行为核心术语

> **状态：Reference / Non-normative**
>
> 本表是从 [`core/README.md` 的 Definition 权威注册表](../core/README.md#definition-权威注册表)派生的复核速查，不直接形成交易计划。每个条目只保留权威页中的必要摘要；权威归属以注册表和条目所链接的 Core Definition 为准，若本表与 Core Definition 冲突，以后者为准。

本表不另立定义，也不能作为核心框架的缩略替代品。完整理解必须覆盖[核心框架的全部组成及其关系](../core/README.md#整体理解要求)；完整人工策略见[策略手册](../strategy/README.md)，订单、记录与复盘见[执行与复盘](../execution/README.md)。

## 判断与交易数学

### Context

派生自：[Core Definition：Context](../core/02_context/00_context_location_control.md#它解决什么问题)。

左侧价格行为、买卖压力、支撑阻力和市场状态对当前 setup 的支持或反对。Context 比孤立的 K 线或形态名称更重要。

### Market Cycle

派生自：[Core Definition：Market Cycle](../core/01_market_cycle/00_market_cycle.md#基础层级)。

基础状态先分 trend 与 trading range；trend 再观察当前主要是已形成方向控制的 breakout phase（spike）还是 channel，实务上可看成 `breakout phase / spike -> tight channel -> broad channel -> trading range` 的连续谱。Breakout mode、climactic move 与 transition evidence 是可叠加的跨层信息，不与两种基础状态并列。

### Pattern / Setup

派生自：[Core Definition：Pattern](../core/04_patterns/00_patterns_are_language.md#pattern-的定义)与 [Core Definition：Setup](../core/05_setups/00_what_is_a_setup.md#setup-的定义)。

Pattern 是对可观察价格行为及其几何或顺序关系的命名。Setup 则把具体 Context、交易 premise、支持证据、方向、可观察触发、失效事实和直接期待的价格运动组合起来；它仍不是完整 Trade Plan。

### Trader's Equation / 40–60 Thinking

派生自：[Core Definition：Trader's Equation](../core/00_method/01_probability_risk_reward.md#traders-equation)与 [40–60 思维](../core/00_method/01_probability_risk_reward.md#40–60-思维)。

Trader's Equation 比较成功概率与回报、失败概率与风险，判断交易是否具有正的数学期望；佣金和滑点另行影响净结果。多数普通交易没有压倒性胜率，应同时考虑两个方向，并用风险回报补偿不确定性。

### Likely / Probably / Risky

派生自：[Core Definition：概率措辞边界](../core/00_method/01_probability_risk_reward.md#概率措辞边界)。

Brooks glossary 和课程把 `likely / probably` 约定为至少约 60%，但这只是其教学语言阈值，不是普通英语定义或已校准模型，也不表示确定。Glossary 的 `risky` 指 Trader's Equation 不清楚、勉强有利，或概率不高于约 50%；仓库诊断时再检查具体是概率、合理 stop、现实 reward 还是成本造成。实际判断必须回到同一组 entry、protective stop、target 和管理。

### Success / Failure

派生自：[Core Definition：Trade Failure](../core/03_acceptance_and_order_logic/01_acceptance_and_failure.md#disappointmentpremise-变化和-trade-failure)。

Success 按当前计划的目标是否先于 protective stop 到达复核；先获得 scalper's profit 或方向短暂走对，不自动等于完整目标成功。Trade failure 要求实际 entry 后，原目标或至少 scalper's profit 尚未实现而 protective stop 先到；弱 entry bar、短暂失望或 premise 提前变化不是同一结果。

## 市场状态、位置与路径

以下条目只用于回查市场状态、位置与路径用语；完整关系仍须阅读 [`core/01_market_cycle/`](../core/01_market_cycle/README.md) 和 [`core/02_context/`](../core/02_context/README.md)。

### Breakout

派生自：[Core Definition：Breakout Event / Attempt](../core/01_market_cycle/03_breakouts_and_breakout_mode.md#breakout-event--attempt)。

Breakout event 是当前 K 线高点或低点越过重要旧价位；接受证据未知时先视为 breakout attempt。强收盘、follow-through 和没有快速收回支持新价格逐步获得接受；这些证据进一步形成持续方向控制后，才可称为 trend 中的 breakout phase（spike）。“获接受的突破”是本仓库对证据状态的整理标签，不是官方 glossary 的独立词条。

### Breakout Pullback / Breakout Test

派生自：[Core Definition：Breakout Pullback / Breakout Test](../core/01_market_cycle/03_breakouts_and_breakout_mode.md#breakout-pullback-与-breakout-test)。

Breakout pullback 是突破后的回调；breakout test 更具体地测试原入场价或旧边界附近。测试可能很快发生，也可能延后很多根，不是突破获得接受的必要步骤。

### Breakout Mode

派生自：[Core Definition：Breakout Mode](../core/01_market_cycle/03_breakouts_and_breakout_mode.md#breakout-mode)。

任一方向突破都应有获得 follow-through 的可能，不预设方向，也不保证第一次突破获得接受。官方 glossary 称它为一种 setup；仓库的严格 Setup schema 还要求具体 Context、premise、触发和失效，因此先把它作为可叠加的双向候选状态。它不是与 trend / trading range 并列的第三种基础状态，也不是已经发生的 breakout event 或 breakout phase。

### Tight Channel / Broad Channel

派生自：[Core Definition：Trend / Channel](../core/01_market_cycle/01_trends_and_channels.md#定义)。

Tight channel 推进稳定、回调浅、重叠少，反向交易通常风险较高。Broad channel 方向优势较弱、回调更深、重叠更多，行为逐渐接近倾斜 trading range。

### Tight Trading Range / Broad Trading Range

派生自：[Core Definition：Tight Trading Range](../core/01_market_cycle/02_trading_ranges.md#tight-trading-range-和-barbwire)与 [Broad Trading Range](../core/01_market_cycle/02_trading_ranges.md#broad-trading-range)。

Tight trading range 重叠多、空间小、方向不清，多数经验不足的交易者更适合等待突破。Broad trading range 空间较大，边缘可能有机会，中部通常没有优势。

### Climax

派生自：[Core Definition：Climax / Transition](../core/01_market_cycle/04_climax_and_transition.md#两种并存的用法)。

课程可把当下加速、大实体 breakout bar 或极端微型通道称为 climactic move / climax bar；这描述行为，不保证反转。官方 glossary 的严格 `climax` 词条则要求运动走得过快过远，并且市场已经反向进入 trading range 或相反 trend。本仓库分别写作“高潮式推进/候选”和“已确认的反转或耗竭高潮”，避免把进行时行为直接当成逆势许可。

### Pullback / Leg / Swing

派生自：[Core Definition：Pullback / Leg](../core/01_market_cycle/01_trends_and_channels.md#pullback-与-leg)与 [Core Definition：Swing](../core/06_trade_plan_and_management/01_scalp_vs_swing.md#swing)。

Pullback 是原运动中的暂时暂停或反向运动，尚未否定其恢复预期；leg 是较大结构中的一段方向运动，可以属于趋势、通道、交易区间或修正过程。Swing 寻求比 scalp 更大的价格运动，并愿意承受符合 premise 的正常 pullback。

### Always In

派生自：[Core Definition：Always In](../core/02_context/00_context_location_control.md#always-in-是强控制判断)。

在当前时点，若必须持仓，交易者更可能选择的方向。它是控制方向摘要，不替代位置、目标或 Trader's Equation。

### Buying Pressure / Selling Pressure

派生自：[Core Definition：Context / Control](../core/02_context/00_context_location_control.md#控制权)。

连续强 K 线、收盘、失败、回调和跟进形成的累积买卖证据；不是对真实订单簿身份或单笔成交动机的断言。

### Support / Resistance / Magnet

派生自：[Core Definition：Support / Resistance](../core/02_context/01_support_resistance_targets.md#它解决什么问题)与 [Magnet](../core/02_context/01_support_resistance_targets.md#磁吸目标)。

Support 在当前价格下方，是下跌可能停顿或反转的候选区域；resistance 在当前价格上方，是上涨可能停顿或反转的候选区域。同一价格区被穿越后可以交换角色，它们不是保证反转的精确线。Magnet 是可能吸引价格测试的目标区域；吸引不保证到达。

### Measured Move

派生自：[Core Definition：Measured Move](../core/02_context/01_support_resistance_targets.md#量度目标)。

依据已经形成的结构估算下一段可能测试的区域，例如 Leg 1 = Leg 2 或区间高度投射；它是 target / magnet 候选，不是价格承诺。

## 订单、触发与结果

订单用途与结果证据见 [`core/03_acceptance_and_order_logic/`](../core/03_acceptance_and_order_logic/README.md)。

### Stop Entry / Protective Stop

派生自：[Core Definition：Stop Entry](../core/03_acceptance_and_order_logic/00_stop_entry_vs_protective_stop.md#stop-entry)与 [Protective Stop](../core/03_acceptance_and_order_logic/00_stop_entry_vs_protective_stop.md#protective-stop)。

Stop entry 在价格向交易方向越过触发价后入场；buy stop 在当前价上方触发买入，sell stop 在当前价下方触发卖出；protective stop 则用于退出并保护持仓。二者用途不同，实际成交都可能因跳空或滑点偏离触发价。一份计划还须区分当前实际在场的 active protective stop 与另行预算的 catastrophe backup，不能用同一名称指两个价位。

### Limit Entry / Limit Order Market

派生自：[Core Definition：Limit Order Market](../core/03_acceptance_and_order_logic/02_limit_order_market.md#定义)。

Limit entry 只允许在指定价格或更好价格成交，常用于区间或弱通道；更好价格不代表更高胜率，也不保证成交。Limit Order Market 指双边交易者常能通过逆向 limit entry 获利的环境。

### Invalidation

派生自：[Core Definition：Trade Plan](../core/06_trade_plan_and_management/00_trade_plan.md#trade-plan-的定义)。

可观察的价格事实，说明原交易 premise 不再成立；它不等于任意固定金额止损，也不要求等待最远 protective stop 成交。

### Entry Trigger

派生自：[Core Definition：Setup](../core/05_setups/00_what_is_a_setup.md#setup-的定义)。

使计划入场条件成立的具体价格事件；触发不等于经纪商已接受订单，也不等于已经成交。

### Signal Bar / Entry Bar

派生自：[Core Definition：Signal Bar](../core/04_patterns/01_bar_types.md#signal-bar)与 [Entry Bar](../core/04_patterns/01_bar_types.md#entry-bar)。

对常见 stop-entry，signal bar 是实际 entry bar 前、用于放置入场单的最后一根；在 K 线收盘直接成交时，同一根可以同时是 signal bar 和 entry bar。没有真实入场时，更准确地称为 prospective signal bar（候选信号 K 线）；entry bar 是订单实际成交所在的 K 线。

### Fade / Countertrend

派生自：[Core Definition：Fade / Countertrend](../core/03_acceptance_and_order_logic/02_limit_order_market.md#fade-与-countertrend)与 [Core Definition：Always In](../core/02_context/00_context_location_control.md#always-in-是强控制判断)。

Fade 押注当前方向尝试不会获接受，常见于区间边缘的逆向 limit-order 行为；countertrend 则明确逆当前 Always In 方向。两者可以重叠，但方向不清的 trading range fade 不必属于 countertrend。

### Follow-through

派生自：[Core Definition：Follow-through](../core/03_acceptance_and_order_logic/01_acceptance_and_failure.md#follow-throughsurprise-和惯性)。

初始运动之后，后续一根或多根 K 线继续延伸该运动。强收盘、浅回调和反方失败属于更广的 acceptance evidence，不能替代是否出现后续延伸这一检查。

### Surprise / Entry Disappointment

派生自：[Core Definition：Surprise](../core/03_acceptance_and_order_logic/01_acceptance_and_failure.md#follow-throughsurprise-和惯性)与 [Entry Disappointment](../core/03_acceptance_and_order_logic/01_acceptance_and_failure.md#disappointmentpremise-变化和-trade-failure)。

Surprise 是明显超出交易者预期的强行为，常增加第二腿可能性，但不保证直线延伸。Entry disappointment 只表示入场表现偏弱或暂未离开入场区，不能单独确认 trade failure。

### Failed Entry

派生自：[Core Definition：Trade Failure](../core/03_acceptance_and_order_logic/01_acceptance_and_failure.md#disappointmentpremise-变化和-trade-failure)。

已经实际触发并成交的 setup 最终成为 failure。没有成交的潜在 setup、普通 pullback 或弱 entry bar 不能单独称为 failed entry。

### Failed Breakout / Failed Failure

派生自：[Core Definition：Breakout Acceptance](../core/01_market_cycle/03_breakouts_and_breakout_mode.md#突破质量)与 [Core Definition：Failed Failure](../core/03_acceptance_and_order_logic/01_acceptance_and_failure.md#failed-failure运动尝试)。

Failed breakout 是 breakout attempt 缺乏接受并明确回到原区域；failed failure 则是这次失败运动随后也失败，价格恢复原突破方向。两者描述价格运动，不自动等于某笔实际交易已触及 protective stop。

### Trapped Traders

派生自：[Core Definition：Trapped Traders](../core/03_acceptance_and_order_logic/01_acceptance_and_failure.md#trapped-traders)。

已经实际入场、尚未获得原目标或至少 scalper's profit、当前处于开放亏损，并很可能被迫退出的一方。已经退出者可记录为“曾被困并被迫退出”，不再属于当前 `trapped in a trade` 状态。

## K 线与计数边界

这里只保留容易发生误读的几何和计数摘要；识别和用法见 [`core/04_patterns/`](../core/04_patterns/README.md)。

### Inside Bar / Outside Bar

派生自：[Core Definition：Inside / Outside Bar](../core/04_patterns/01_bar_types.md#inside--outside-bar)。

Inside bar 的高点不高于前高且低点不低于前低。Outside bar 有来源口径差异：glossary 要求至少一端严格越过、另一端相等或越过；课程 08B p450 则允许两端都只相等，即 `high ≥ 前高且 low ≤ 前低`。机械标注时必须注明采用哪套边界。

### Reversal Bar

派生自：[Core Definition：Reversal Bar](../core/04_patterns/01_bar_types.md#reversal-bar--two-bar-reversal)。

Glossary 的简化最低定义是与当前 trend 或 leg 方向相反的 trend bar；课程的操作性 buy / sell reversal bar 还容许反色实体，只要收盘位置满足相应方向要求。反向测试影线和靠近新方向极值的收盘是常见加强项；外观良好仍不表示 Context 支持反转。

### ii / ioi / oo

派生自：[Core Definition：ii](../core/04_patterns/06_triangles_ii_ioi_oo.md#ii--iii)、[ioi](../core/04_patterns/06_triangles_ii_ioi_oo.md#ioi)与 [oo](../core/04_patterns/06_triangles_ii_ioi_oo.md#oo)。

ii 是连续两根 inside bar；ioi 是 inside–outside–inside；oo 是 outside bar 后紧接一根更大的 outside bar。它们常处于 breakout mode，不能只凭形态名预设方向；但压缩并不消除 Context，强趋势或尚未成熟的紧结构仍可保留方向偏置。成熟 triangle 的近 50/50 先验不能外推给所有 ii、ioi 或 oo。

### H1 / H2 / L1 / L2

派生自：[Core Definition：H1 / H2 / L1 / L2](../core/04_patterns/02_h1_h2_l1_l2.md#定义)。

H1/H2 对回调中的第一次/第二次向上触发尝试计数；L1/L2 对第一次/第二次向下触发尝试计数。Brooks glossary 使用严格 `above` / `below`，而 *10 Best Price Action Trading Patterns* 的图例写作 `at or above` / `at or below`；公开材料对相等高低点的边界并不完全一致，不能让这一差异取代 context 和触发质量。

### Second Signal / Second Entry

派生自：[Core Definition：Second Signal / Second Entry](../core/03_acceptance_and_order_logic/03_second_entries_and_traps.md#second-signal-与-second-entry)。

Second signal 是同一交易逻辑第二次形成候选触发；second entry 则要求第一次 entry 已经发生，随后仍基于同一逻辑第二次实际形成 entry bar。

## 形态名称复核

本节只保留名称容易诱发错误推论时所需的摘要；完整结构、识别线索和交易含义由 [`core/04_patterns/`](../core/04_patterns/README.md) 与 [`core/05_setups/`](../core/05_setups/README.md) 解释。

### Micro Double Top / Bottom

派生自：[Core Definition：Micro Double Top / Bottom](../core/04_patterns/04_double_tops_bottoms.md#micro-double-top--bottom)。

发生在相邻或近邻 K 线中的极小双顶底。它既可能是趋势中的 one-bar flag，也可能在反向 flag 末端成为 reversal setup，不天然等于反转。

### Wedge / Parabolic Wedge

派生自：[Core Definition：Wedge](../core/04_patterns/03_wedges.md#定义)与 [Parabolic Wedge](../core/04_patterns/03_wedges.md#parabolic-wedge-怎么读)。

Wedge 通常表示三次推动或三次尝试，在不同 Context 中可以是顺势回调、反转尝试或没有优势的普通结构。Parabolic wedge 是 tight channel 中至少三腿或三次 surge 构成的 climactic wedge；它不要求每一腿更陡，也不自动导出反转、两腿修正或 MTR。

### Final Flag

派生自：[Core Definition：Final Flag](../core/04_patterns/05_final_flags.md#定义)。

任何趋势腿——包括交易区间内的小趋势腿——都可能被某个 flag 终结，且 flag 可小至一根。实时只能标记为 candidate final flag；趋势晚段、magnet、高潮和双边交易增加只会提高嫌疑。只有后续结果显示该 flag 终结了原趋势腿，才支持 confirmed final-flag interpretation。

### Triangle

派生自：[Core Definition：Triangle](../core/04_patterns/06_triangles_ii_ioi_oo.md#triangle)。

至少五次反转的 trading range，可由“两次 higher low 加一次 lower high”或镜像结构形成，并处于 breakout mode。约 50/50 的突破方向和首次突破失败倾向只属于 triangle 语境，不能外推到所有 breakout mode。

### Major Trend Reversal / MTR

派生自：[Core Application：Major Trend Reversal](../core/05_setups/04_major_trend_reversal.md#交易命题)与 [Core Definition：Setup](../core/05_setups/00_what_is_a_setup.md#setup-的定义)。

MTR 在核心框架中是反转 Setup 原型，不是单根 K 线或孤立 Pattern 的同义词。把它作为候选 Setup 时，仍须说明具体 Context、premise、支持证据、反向触发、失效事实和直接期待的价格运动。

### Gap / Body Gap

派生自：[Core Definition：Gap](../core/04_patterns/07_gaps.md#gap-的最低含义)与 [Body Gap](../core/04_patterns/07_gaps.md#术语边界)。

Gap 是明确的两个支撑阻力对象之间缺少充分双边交易的价格空间，不限于隔夜跳空或严格无重叠。Body gap 更具体地表示两个参照 K 线的实体不重叠，影线可以重叠。

### Measuring Gap / Exhaustion Gap

派生自：[Core Definition：Measuring Gap / Exhaustion Gap](../core/04_patterns/07_gaps.md#术语边界)。

Measuring gap 最终支持 measured move。Exhaustion gap 存在来源口径差异：glossary 要求成熟趋势末端至少出现小反转；课程案例也容许只停止顺势压力并转横盘、gap 仍开放的末端结果。两种名称都取决于后续结果，实时只能标 candidate / potential，并注明采用的来源口径。

## 管理边界

管理选择见 [`core/06_trade_plan_and_management/`](../core/06_trade_plan_and_management/README.md)。

### Scalp / Swing

派生自：[Core Definition：Scalp](../core/06_trade_plan_and_management/01_scalp_vs_swing.md#scalp)与 [Swing](../core/06_trade_plan_and_management/01_scalp_vs_swing.md#swing)。

Scalp 以较小目标快速兑现；目标小于风险时，需要多数交易者难以维持的高胜率。Swing 寻求较大运动，并愿意承受部分正常 pullback；二者必须与 stop、target 和 Trader's Equation 保持一致。

### TBTL

派生自：[Core Definition：TBTL](../core/06_trade_plan_and_management/01_scalp_vs_swing.md#tbtl-是时间与腿数预期)。

Ten Bars, Two Legs correction。它是反转 swing 的常见时间与路径预期，不是所有 correction 的硬性完成条件，也不是价格目标。

## 常用缩写

| 缩写 | 含义 |
| --- | --- |
| `AIL` / `AIS` | Always In Long / Short |
| `BO` / `BOM` / `BP` / `BT` | Breakout / Breakout Mode / Breakout Pullback / Breakout Test |
| `FBO` / `FF` / `FT` | Failed Breakout / Final Flag / Follow-through |
| `H1` / `H2` / `L1` / `L2` | High / Low counting |
| `LOM` | Limit Order Market |
| `MDB` / `MDT` / `MTR` | Micro Double Bottom / Top / Major Trend Reversal |
| `TE` / `TBTL` / `TTR` | Trader's Equation / Ten Bars, Two Legs / Tight Trading Range |
