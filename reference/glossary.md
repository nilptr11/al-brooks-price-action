# Brooks 价格行为核心术语

> **状态：Reference / Non-normative**
>
> 本表只帮助快速读懂正文，不定义交易动作。执行规则以当前[执行手册](../EXECUTION_MANUAL.md)为准；来源与审计入口见[参考与来源](README.md)。

只收录三类词：核心流程反复使用的词、容易混淆且会改变判断的词，以及官方最低定义与本仓库执行边界不同的词。形态细节由 [`learning/04_patterns/`](../learning/04_patterns/README.md) 解释，低频词直接在首次出现处说明。

## 方法与交易数学

### Price Action

价格行为。通过 K 线、结构、位置、目标、失败和跟进理解市场，而不是把指标或形态名称当成自动信号。

### Bar-by-bar Reading

逐根阅读。只使用当时已经出现的 K 线更新判断，不用后续结果改写过去。

### Context

上下文。左侧价格行为、买卖压力、支撑阻力和市场状态对当前 setup 的支持或反对。

### Market Cycle

市场循环。先分 trend 与 trading range；trend 再观察 breakout 或 channel。实务上可看成 breakout、tight channel、broad channel、trading range 的连续谱。

### Pattern

形态语言，例如 H2、wedge、double bottom。它描述市场行为，不自动许可交易。

### Setup

带 context、可作为放置入场单依据的 pattern。实际成交后，setup 的最后一根才取得 signal bar 角色；setup 仍不等于完整交易计划。

### Trader's Equation

交易数学。把成功概率、保守回报、保守亏损和成本放进同一方案，判断风险是否值得承担。

### Probability

某个目标先于相反结果发生的可能性。概率不能脱离 entry、stop、target 和管理单独判断。

### Likely / Probably

可能性明显偏向一侧，Brooks 语境中通常约为 60% 或更高；不是确定发生。

### 40–60 Thinking

多数普通交易没有压倒性胜率，应同时考虑两个方向，并用风险回报补偿不确定性。

### Risk / Reward

从计划 entry 到合理 protective stop 的风险，与到现实 target 的潜在回报之间的关系。

### Risky

Trader's Equation 不清楚或仅勉强有利，也可表示成功概率不高于约 50%；不等同于“波动很大”。

### Success

预定目标或至少 scalper's profit 先于 protective stop 到达。方向短暂走对不等于成功。

### No-trade

市场、位置、空间、触发或数学不清楚时选择等待；它是有效结果，不是遗漏交易。

## 市场状态与运动

### Trend

价格持续寻找更高或更低区域，一方控制明显，反方尝试经常失败。

### Breakout

当前 K 线高点或低点越过重要旧价位。强收盘和 follow-through 决定质量，但不属于突破发生的最低条件。

### Breakout Pullback / Breakout Test

Breakout pullback 是突破后的回调；breakout test 更具体地测试原入场价或旧边界附近。测试可能很快发生，也可能延后很多根，不是成功突破的必要步骤。

### Channel

Breakout 后动能较低但仍有方向的 trend，双边交易和 pullback 比 breakout 阶段更多。

### Tight Channel

推进稳定、回调浅、重叠少的通道；反向交易通常风险较高。

### Broad Channel

方向优势较弱、回调更深、重叠更多的通道，行为逐渐接近倾斜 trading range。

### Spike and Channel

趋势先以强 spike 开始，随后进入较弱但仍有方向的 channel。

### Small Pullback Trend

强趋势中的回调很浅，等待深回调的交易者经常被迫追随。

### Micro Channel

紧通道的极端形式，可以没有回调，也可以有一两次小回调；高低点严格单调只是其中一种子型。

### Trading Range

双方都未持续控制、价格围绕公平区域双向交易的结构。最低术语定义不等于已经具备可交易空间。

### Tight Trading Range / TTR

重叠多、空间小、方向不清的区间，多数学习者更适合等待突破。

### Broad Trading Range

空间较大的交易区间；边缘可能有机会，中部通常没有优势。

### Breakout Mode

任一方向突破都应有获得 follow-through 的可能，不预设方向，也不保证第一次突破成功或失败。

### Climax / Climactic Behavior

Climactic behavior 指运动看起来过快过远；只有已经转入 trading range 或反向 trend，才符合官方 climax 的严格结果定义。

### Pullback

Trend、swing 或 leg 中的暂时暂停或反向运动，尚未否定原运动恢复的预期。

### Leg

较大结构中的一段小趋势，可以是顺势推进、回调或区间内 swing。

### Swing

比 scalp 更大的价格运动；交易者通常愿意穿越部分 pullback 以寻求更远目标。

### Two Legs

两次可区分的推动，中间至少有一次暂停或反向尝试；不要求两腿完全对称。

## Context、位置与目标

### Always In

从某个较早时点起，若必须持仓，交易者更可能选择的方向。它是控制方向摘要，不替代位置、目标或 Trader's Equation。

### Buying Pressure / Selling Pressure

来自连续强 K 线、收盘、失败、回调和跟进的累积买卖证据；不是对真实订单簿身份的断言。

### Control

当前哪一方更能推动价格并让对方尝试失败。控制可以逐步改变，不需要等待单一反转形态。

### Location

价格相对于支撑阻力、区间边缘、旧极值和目标的位置。

### Support / Resistance

市场可能出现买入或卖出反应的价格区域。它们是区域和概率，不是保证反转的精确线。

### Magnet

可能吸引价格测试的区域，例如旧高低点、均线、开盘价或 measured move；吸引不保证到达。

### Target

计划兑现利润或检验交易想法的现实价格区域，必须考虑路径上的近端障碍。

### Measured Move

依据前一段运动或形态高度投射的目标候选，例如 Leg 1 = Leg 2 或区间高度；它不是价格承诺。

### Moving Average / EMA

近期价格的平滑参考，可成为动态支撑阻力或公平区域；不能单独许可交易。

### Multi-timeframe / HTF / LTF

高周期提供更大位置和障碍，低周期提供更细触发。不同周期的信息必须说明如何影响当前计划。

### Time of Day / Session

当前时段的流动性、剩余时间和常见参与结构。时段倾向需要按具体市场验证，不能写成跨市场定律。

## 订单、触发与结果

### Stop Entry

价格向交易方向越过触发价后入场，常用于要求市场先证明方向的 setup。

### Buy Stop / Sell Stop

Buy stop 在当前价上方触发买入；sell stop 在当前价下方触发卖出。它们既可用于入场，也可用于退出，必须结合用途理解。

### Protective Stop

保护持仓的退出订单。它与 stop entry 用途不同，实际成交可能因跳空或滑点偏离触发价。

### Invalidation

可观察的价格事实，说明原交易 premise 不再成立。它不等于任意固定金额止损。

### Limit Entry

在指定价格或更好价格成交的入场方式，常用于区间或弱通道中的高级交易；更好价格不代表更高胜率。

### Limit Order Market / LOM

双边交易者常能通过逆向 limit entry 获利的环境，通常见于 trading range 或弱 channel。

### Entry Trigger

使计划入场条件成立的具体价格事件；触发不等于经纪商已接受，也不等于已经成交。

### Signal Bar

实际 entry bar 前、用于放置入场单的最后一根 K 线。没有真实入场时，更准确地称为潜在 signal bar。

### Entry Bar

订单实际成交所在的 K 线。

### Fade / Countertrend

Fade 是交易一次尝试会失败并回到旧区域；countertrend 是逆当前趋势方向交易。两者可能重叠，但不是同义词。

### Follow-through

初始运动之后，后续 K 线继续支持同一方向。强收盘、连续延伸、浅回调和反方失败都可以构成证据。

### Surprise

明显超出交易者预期的强行为，常使站错者退出、错过者追随，因此增加第二腿可能性，但不保证直线延伸。

### Disappointment

触发后的力度或跟进弱于预期。它削弱 setup，但单独不足以确认 failure。

### Failure

实际 entry 后，原目标或至少 scalper's profit 尚未先实现，protective stop 却先到。

### Failed Entry

已经实际触发并成交的 setup 最终成为 failure。普通 pullback 或弱 entry bar 不能单独确认。

### Failed Breakout

价格突破旧区域后缺乏接受，并明确回到原区域。

### Failed Failure

原突破先失败，随后该失败又失败，价格恢复原突破方向；结构上可能转成 breakout pullback 或 second signal。

### Trapped Traders

已经实际入场、尚未获得目标或至少 scalper's profit、处于开放亏损，并很可能被迫或已经实际退出的一方。

## K 线与计数

### Trend Bar

有实体的 K 线；强 trend bar 通常实体较大、收盘靠近趋势方向极值、反向影线较短。

### Doji

开收盘接近、实体很小的 K 线，表示该根内部双边交易较多；意义取决于 context。

### Inside Bar

高点不高于前高且低点不低于前低的 K 线，表示短期波动收缩。

### Outside Bar

高点高于前高且低点低于前低的 K 线，表示当根双向扩张。

### ii / ioi / oo

ii 是连续两根 inside bar；ioi 是 inside–outside–inside；oo 是 outside bar 后紧接一根更大的 outside bar。它们常处于 breakout mode，不能预设方向。

### Pause Bar / Pullback Bar

Pause bar 暂停当前推进；pullback bar 向原运动反方向延伸。几何上可能重叠，作用由 context 决定。

### Reversal Bar

先向一侧测试、后向另一侧收盘的 K 线。外观良好不等于 context 支持反转。

### H1 / H2 / L1 / L2

H1/H2 是回调中第一次/第二次严格越过前高的买入触发；L1/L2 是第一次/第二次严格跌破前低的卖出触发。

### Second Entry / Second Signal

Second entry 要求第一次尝试已形成实际 entry bar；若第一次只出现潜在信号而没有成交，下一次通常只是 second signal。

## 常见形态

### Double Top / Double Bottom

两次测试相近高点或低点后未能继续。相近是结构区域，不要求价格完全相等。

### Micro Double Top / Bottom

只隔一两根 K 线的极小双顶底。它既可能是趋势中的 one-bar flag，也可能在反向 flag 末端成为 reversal setup。

### Wedge

通常由三次推动构成，第三次推动后交易者寻找至少两腿修正；三次推动不必完全对称。

### Parabolic Wedge

三次或更多推动逐渐加速、通道越来越陡的 wedge，常带 climactic behavior。

### Final Flag

成熟趋势末端的小整理；只有随后突破失败并形成反向证据，才支持“最终”解释。

### Triangle

至少三次交替推动、方向逐渐收敛的 trading range，通常处于 breakout mode。

### Major Trend Reversal / MTR

完整结构通常包含趋势、通道或趋势线突破、对旧趋势极值的测试，以及反向 signal；早期外观不等于已经完成反转。

## Gap 与重新定价

### Gap

两个价格对象之间没有重叠的空间，可以发生在相邻 K 线、实体、均线或其他支撑阻力对象之间。

### Gap Up / Gap Down

开盘高于或低于前一时段参考范围。Gap 方向本身不决定当日趋势方向。

### Gap Reversal

价格先朝 gap 方向尝试，随后出现反向触发；最低几何定义不要求已经触及真正 gap 边界。

### Body Gap

相邻 K 线实体不重叠形成的空间，影线可以重叠。

### Micro Measuring Gap

强 trend bar 前后完整区间不重叠形成的小 gap，可作为趋势强度和 measured move 线索。

### Breakout / Measuring / Exhaustion Gap

Breakout gap 强调离开旧区域；measuring gap 最终支持 measured move；exhaustion gap 位于成熟趋势末端并已出现至少小反转。名称取决于后续结果，不能只凭 gap 外观预判。

## 管理、风险与时段

### Scalp

以较小目标快速兑现的交易。目标小于风险时，需要多数交易者难以维持的高胜率。

### Swing Trade

寻求较大运动、愿意承受部分正常 pullback 的交易，通常需要更大目标空间。

### TBTL

Ten Bars, Two Legs correction。它是反转 swing 的常见经验预期，不是所有修正的硬性完成条件，也不是价格目标。

### Scaling In / Scaling Out

Scaling in 是分批增加仓位；scaling out 是分批退出。两者都必须事前绑定数量、价格和完整风险。

### Breakeven Stop / Scratch

Breakeven stop 把保护价移到接近实际成本；scratch 是接近零盈亏退出。二者不应被当成没有承担风险。

### Initial Risk

按计划 entry 到合理 protective stop 的初始风险距离；实际成交、滑点和成本可能使账户结果不同。

### Position Size

持仓数量。它服从合理 stop 距离、账户风险边界和行为承受能力，而不是服从信心。

### Opening Range / OR

开盘后形成的初始交易范围；具体持续时间取决于市场和训练定义。

### Opening Range Breakout / ORB

价格离开 opening range 的尝试；仍需检查位置、强度、follow-through 和失败路径。

### Opening Reversal

开盘初始方向失败后形成的反向运动，不能只凭 opening gap 或第一根反向 K 线确认。

### Trend From The Open

市场从开盘附近开始保持明显单向控制，回调通常较小。

### Trend / Trading Range / Reversal Day

对日内主要结构的事后或动态描述。日型会随新信息改变，不应在开盘时被当成固定标签。

## 常用缩写

| 缩写 | 含义 |
| --- | --- |
| `AIL` / `AIS` | Always In Long / Short |
| `BO` / `BOM` / `BP` / `BT` | Breakout / Breakout Mode / Breakout Pullback / Breakout Test |
| `EMA` | Exponential Moving Average |
| `FBO` / `FF` / `FT` | Failed Breakout / Final Flag / Follow-through |
| `H1` / `H2` / `L1` / `L2` | High / Low counting |
| `HTF` / `LTF` | Higher / Lower Time Frame |
| `LOM` | Limit Order Market |
| `MDB` / `MDT` / `MTR` | Micro Double Bottom / Top / Major Trend Reversal |
| `OR` / `ORB` | Opening Range / Opening Range Breakout |
| `TE` / `TBTL` / `TTR` | Trader's Equation / Ten Bars, Two Legs / Tight Trading Range |
