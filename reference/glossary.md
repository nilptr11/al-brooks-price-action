# Al Brooks 价格行为核心术语

> **状态：Reference / Non-normative**
>
> 本表只统一跨章节反复使用、混淆后会改变判断的术语边界，不直接形成交易计划。完整人工策略见[策略手册](../strategy/README.md)，订单、记录与复盘见[执行与复盘](../execution/README.md)，来源与覆盖关系见[参考资料](README.md)。

使用时直接搜索英文词。只需确认最低定义时查本表；需要识别线索、例图、stop、target 或管理方式时，按[学习路径](../learning/README.md#按需专题)进入对应专题。未收录的普通词和专题词在首次出现处或专题正文解释，本表不扩写成第二本教材。

## 判断与交易数学

### Context

左侧价格行为、买卖压力、支撑阻力和市场状态对当前 setup 的支持或反对。Context 比孤立的 K 线或形态名称更重要。

### Market Cycle

先分 trend 与 trading range；trend 再观察 breakout 或 channel。实务上可看成 breakout、tight channel、broad channel、trading range 的连续谱。

### Pattern / Setup

Pattern 是 H2、wedge、double bottom 等市场行为语言。Setup 是带 context、可作为放置入场单依据的 pattern；它仍不等于包含 entry、stop、target、仓位和管理的完整交易计划。

### Trader's Equation / 40–60 Thinking

Trader's Equation 比较成功概率与回报、失败概率与风险，判断交易是否具有正的数学期望；佣金和滑点另行影响净结果。多数普通交易没有压倒性胜率，应同时考虑两个方向，并用风险回报补偿不确定性。

### Likely / Probably / Risky

Likely 或 probably 表示可能性明显偏向一侧，通常约为 60% 或更高，不是确定发生。Risky 表示 Trader's Equation 不清楚或仅勉强有利，也可表示成功概率不高于约 50%；不等同于“波动很大”。

### Success / Failure

Success 是预定目标先于 protective stop 到达；先获得 scalper's profit 或方向短暂走对，不自动等于完整目标成功。Failure 是原目标或至少 scalper's profit 尚未先实现，protective stop 却先到；弱 entry bar、短暂失望或 premise 提前变化不能单独改写这一结果边界。

## 市场状态、位置与路径

完整识别方法见 [`learning/01_market_cycle/`](../learning/01_market_cycle/README.md) 和 [`learning/02_context/`](../learning/02_context/README.md)。

### Breakout

当前 K 线高点或低点越过重要旧价位。强收盘和 follow-through 决定质量，但不属于突破已经发生的最低条件。

### Breakout Pullback / Breakout Test

Breakout pullback 是突破后的回调；breakout test 更具体地测试原入场价或旧边界附近。测试可能很快发生，也可能延后很多根，不是成功突破的必要步骤。

### Breakout Mode

任一方向突破都应有获得 follow-through 的可能，不预设方向，也不保证第一次突破成功或失败。

### Tight Channel / Broad Channel

Tight channel 推进稳定、回调浅、重叠少，反向交易通常风险较高。Broad channel 方向优势较弱、回调更深、重叠更多，行为逐渐接近倾斜 trading range。

### Tight Trading Range / Broad Trading Range

Tight trading range 重叠多、空间小、方向不清，多数学习者更适合等待突破。Broad trading range 空间较大，边缘可能有机会，中部通常没有优势。

### Climax

一段运动走得过快过远，并且市场已经反向进入 trading range 或相反 trend。反转出现前只能描述为高潮式推进或 possible climax，不能只因价格“太高、太低、太快”就确认 climax。

### Pullback / Leg / Swing

Pullback 是原运动中的暂时暂停或反向运动，尚未否定其恢复预期。Leg 是较大结构中的一段小趋势；swing 是比 scalp 更大的价格运动，交易者通常愿意穿越部分 pullback 以寻求更远目标。

### Always In

从某个较早时点起，若必须持仓，交易者更可能选择的方向。它是控制方向摘要，不替代位置、目标或 Trader's Equation。

### Buying Pressure / Selling Pressure

连续强 K 线、收盘、失败、回调和跟进形成的累积买卖证据；不是对真实订单簿身份或单笔成交动机的断言。

### Support / Resistance / Magnet

Support 和 resistance 是市场可能出现买入或卖出反应的区域，不是保证反转的精确线。Magnet 是可能吸引价格测试的区域；吸引不保证到达。

### Measured Move

依据前一段运动或形态高度投射的目标候选，例如 Leg 1 = Leg 2 或区间高度；它是 magnet，不是价格承诺。

## 订单、触发与结果

订单用途与结果证据见 [`learning/03_order_flow/`](../learning/03_order_flow/README.md)。

### Stop Entry / Protective Stop

Stop entry 在价格向交易方向越过触发价后入场；buy stop 在当前价上方触发买入，sell stop 在当前价下方触发卖出。Protective stop 用于退出并保护持仓。二者用途不同，实际成交都可能因跳空或滑点偏离触发价。

### Limit Entry / Limit Order Market

Limit entry 在指定价格或更好价格成交，常用于区间或弱通道中的高级交易；更好价格不代表更高胜率。Limit Order Market 指双边交易者常能通过逆向 limit entry 获利的环境。

### Invalidation

可观察的价格事实，说明原交易 premise 不再成立；它不等于任意固定金额止损，也不要求等待最远 protective stop 成交。

### Entry Trigger

使计划入场条件成立的具体价格事件；触发不等于经纪商已接受订单，也不等于已经成交。

### Signal Bar / Entry Bar

Signal bar 是实际 entry bar 前、用于放置入场单的最后一根 K 线；没有真实入场时，更准确地称为潜在 signal bar。Entry bar 是订单实际成交所在的 K 线。

### Fade / Countertrend

Fade 是逆当前 trend 交易，例如卖出预期会失败的 bull breakout。Countertrend 是逆当前 Always In 方向的交易或 setup。两者高度重叠，但 trading range 边缘的 failed-breakout fade 在方向不清时不一定属于 countertrend。

### Follow-through

初始运动之后，后续一根或多根 K 线继续延伸该运动。强收盘、浅回调和反方失败可以加强接受或延续判断，但不都是 follow-through 的最低定义。

### Surprise / Disappointment Bar

Surprise 是明显超出交易者预期的强行为，常增加第二腿可能性，但不保证直线延伸。Disappointment Bar 的窄义是 Buy The Close bull trend 中的 bear bar，或 Sell The Close bear trend 中的 bull bar；日常所说的 entry disappointment 只是行为弱于预期，单独不足以确认 failure。

### Failed Entry

已经实际触发并成交的 setup 最终成为 failure。没有成交的潜在 setup、普通 pullback 或弱 entry bar 不能单独称为 failed entry。

### Failed Breakout / Failed Failure

Failed breakout 是价格突破旧区域后缺乏接受，并明确回到原区域。Failed failure 是原突破先失败，随后该失败又失败，价格恢复原突破方向；结构上可能转成 breakout pullback 或 second signal。

### Trapped Traders

已经实际入场、尚未获得原目标或至少 scalper's profit、当前处于开放亏损，并很可能被迫退出的一方。已经退出者可记录为“曾被困并被迫退出”，不再属于当前 `trapped in a trade` 状态。

## K 线与计数边界

这里只保留容易发生定义误读的边界；识别和用法见 [`learning/04_patterns/`](../learning/04_patterns/README.md)。

### Inside Bar / Outside Bar

Inside bar 的高点不高于前高且低点不低于前低。Outside bar 至少一端严格越过、另一端相等或越过前一根：`high > 前高且 low ≤ 前低`，或 `low < 前低且 high ≥ 前高`。

### Reversal Bar

与当前 trend 或 leg 方向相反的 trend bar。经典外观常带反向测试形成的影线，并收在新方向极值附近，但这些不是最低定义；外观良好也不等于 context 支持反转。

### ii / ioi / oo

ii 是连续两根 inside bar；ioi 是 inside–outside–inside；oo 是 outside bar 后紧接一根更大的 outside bar。它们常处于 breakout mode，不能预设方向。

### H1 / H2 / L1 / L2

H1/H2 对回调中的第一次/第二次向上触发尝试计数；L1/L2 对第一次/第二次向下触发尝试计数。Brooks glossary 使用严格 `above` / `below`，而 *10 Best Price Action Trading Patterns* 的图例写作 `at or above` / `at or below`；公开材料对相等高低点的边界并不完全一致，不能让这一差异取代 context 和触发质量。

### Second Entry / Second Signal

Second entry 要求第一次尝试已形成实际 entry bar；若第一次只出现潜在信号而没有成交，下一次通常只是 second signal。

## 形态最低边界

本节只保留名称容易诱发错误推论的形态；完整结构、识别线索和交易含义由 [`learning/04_patterns/`](../learning/04_patterns/README.md) 与 [`learning/05_setups/`](../learning/05_setups/README.md) 解释。

### Micro Double Top / Bottom

只隔一两根 K 线的极小双顶底。它既可能是趋势中的 one-bar flag，也可能在反向 flag 末端成为 reversal setup，不天然等于反转。

### Wedge / Parabolic Wedge

Wedge 通常由三次推动构成，第三次推动后交易者寻找至少两腿修正。Parabolic wedge 是 tight channel 中至少三腿或三次 surge 构成的 climactic wedge；不要求每一腿更陡，也不自动意味着 major reversal。

### Final Flag

成熟趋势末端的小整理；只有随后突破失败并形成反向证据，才支持“最终”解释。

### Triangle

至少五次反转的 trading range，可由“两次 higher low 加一次 lower high”或镜像结构形成，并处于 breakout mode。约 50/50 的突破方向和首次突破失败倾向只属于 triangle 语境，不能外推到所有 breakout mode。

### Major Trend Reversal / MTR

完整结构通常包含趋势、通道或趋势线突破、对旧趋势极值的测试，以及反向 signal；早期外观不等于已经完成反转。

### Gap / Body Gap

Gap 是两个价格对象之间没有重叠的空间。Body gap 是两个参照 K 线的实体不重叠，影线可以重叠；参照对象可以相隔数根，不要求相邻。

### Measuring Gap / Exhaustion Gap

Measuring gap 最终支持 measured move；exhaustion gap 位于成熟趋势末端并已出现至少小反转。名称取决于后续结果，不能只凭 gap 外观预判。

## 管理边界

管理选择见 [`learning/06_trade_management/`](../learning/06_trade_management/README.md)。

### Scalp / Swing

Scalp 以较小目标快速兑现；目标小于风险时，需要多数交易者难以维持的高胜率。Swing 寻求较大运动，并愿意承受部分正常 pullback；二者必须与 stop、target 和 Trader's Equation 保持一致。

### TBTL

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
