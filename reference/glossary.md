# Brooks 价格行为术语表

> **状态：Reference / Non-normative**
>
> 本术语表只做快速解释，不定义交易动作。执行规则以当前[执行手册](../README.md#权威层级)为准；官方来源和核对状态见 `reference/official_sources.md` 与 `reference/audit_matrix.md`。

本术语表按学习流程分类，而不是按字母排序。定义尽量保持简短；复杂边界应放入学习文档或审计记录，不在这里形成第二套执行规则。若官方最低定义与本仓库的执行准入不同，本表先写官方定义，再明确标出更严格的内部边界；不能用内部政策改写官方术语。

收录标准：

- 正文已经出现，或复盘问题中反复需要的 Brooks 术语。
- 直接影响主链条：market cycle、context、location、trigger、follow-through、failure、trapped traders、Trader's Equation 和 management。
- 容易混淆且会影响阅读流程的概念。
- 官方公开 glossary / abbreviations 中的术语，只有进入主链条或正文时才放进主表；否则放到“扩展术语”。

## 方法、阅读和交易数学

这些词描述 Brooks 阅读框架和交易数学，不对应单一形态。

### Price Action

价格行为。通过 K 线、结构、位置、目标、失败和跟进来阅读市场，而不是依赖指标信号。

### Bar-by-bar Reading

逐根 K 线阅读。每根 K 线都会增加、削弱或改变原判断。

### Context

上下文。左侧所有 K 线、买卖压力、支撑阻力和当前环境对 setup 的支持或反对。

### Market Cycle

市场循环。官方公开 manual 先判断市场处于 trend 还是 trading range；若是 trend，再判断它主要表现为 breakout 还是 channel。官方 webinar 将实务结构放在 breakout、tight channel、broad channel、trading range 的连续谱上。Breakout mode 与 climactic behavior 是 setup / 阶段信息，不是这一基础层级中的并列第五、六种市场。

### Setup

交易设置。官方 glossary 的最低定义是：由 context 和一根或多根 K 线构成、可作为放置入场单依据的 pattern；订单实际成交后，setup 的最后一根才成为 signal bar。本仓库的执行准入更严格：一个 Brooks setup 仍只是候选，只有完成失效点、protective stop、仓位、目标、管理和 Trader's Equation 后，才是可执行交易计划。

### Pattern

形态语言。用来描述市场行为，例如 H2、wedge、triangle；它不是自动交易信号。

### Trader's Equation

交易数学。概率、风险、回报、成本和管理能力共同决定一笔交易是否值得做。

### 40-60 Thinking

40-60 思维。多数普通交易没有压倒性胜率，交易者必须同时看概率和风险回报。

### Directional Probability

方向概率。价格先朝某方向走到目标，而不是先朝反方向走到同等距离的概率。

### Probability

概率。某一方向或某个目标先发生的可能性；不能脱离风险和回报单独判断。

### Likely / Probably

可能性较高。Brooks 语境中通常表示至少约 60% 的把握，不代表确定。

### High Probability / HP

高概率。概率相对明显偏向一边，但通常要用更差风险回报支付。

### Low Probability / LP

低概率。通常需要更大目标或 swing 空间补偿，或者直接等待。

### Risk / Reward

风险回报。合理交易必须有清楚的亏损边界和目标空间；swing 通常需要足够大的潜在回报。

### Risky

风险偏高。官方 glossary 指 Trader's Equation 不清楚或仅勉强有利，也可以指成功概率不高于约 50%，即使表面风险回报尚可。

### Success

成功。交易者的预定利润目标先于 protective stop 到达；不是单纯方向判断正确。

### No-trade

不交易环境。方向、位置、目标或管理不清楚时，等待本身是有效选择。

## 市场循环和结构

这些词用于判断市场当前处于什么结构，以及应该优先寻找哪类交易。

### Trend

趋势。市场持续寻找更高或更低价格，一方控制明显，反方尝试经常失败。

### Bull Trend / Bear Trend

牛趋势 / 熊趋势。牛趋势持续向上寻找价格，熊趋势持续向下寻找价格。

### Bull Flag / Bear Flag

牛旗 / 熊旗。趋势中的小反向运动或横向整理，交易者期待原趋势恢复。

### Bull Reversal / Bear Reversal

牛反转 / 熊反转。市场从下跌行为转向上涨，或从上涨行为转向下跌。

### Channel

通道。Trend 的一种形态：价格仍有方向，但相较 breakout 出现更多 pullback 和双边交易。Spike and channel 中，breakout 的 follow-through 以动能较低的 channel 延续；channel 越宽，越接近倾斜的 trading range。

### Tight Channel

紧通道。趋势线与通道线靠近；价格沿一个方向稳定推进，典型回调浅且仅持续 1—3 根，重叠少，常见缺口、微缺口或近似缺口。反方 K 线少而弱，逆势交易风险高。强度来自持续控制，不要求每根 K 线都有巨大实体。

### Broad Channel

宽通道。有轻微方向优势，但更接近倾斜 trading range。典型回调持续 3—10 根、回撤深、重叠多，顺逆两方都能走出可交易的腿。

### Spike and Channel

急冲通道。趋势先以强 spike 开始，随后进入较弱但仍有方向的 channel。

### Small Pullback Trend

小回调趋势。强趋势中的回调很浅，通常仅 1—3 根；即使出现小实体、影线、反向实体或重叠，只要回撤保持浅，等待深回调的交易者仍常被迫追随。

### Micro Channel

微型通道。紧通道的极端形式，多数 K 线高低点贴近 trend line，并常同时贴近 trend channel line；可以完全没有回调，也可以有一两次小回调。“牛向每根低点不低于前低 / 熊向每根高点不高于前高”只是严格的无 bar-pullback 子型，不是所有 micro channel 的必要定义。

### Trading Range

交易区间。官方 glossary 的最低结构甚至可以从一根范围被前一根大幅重叠的 K 线开始，表示短期横向、双方都未控制；发展后的 trading range 会反复双向尝试并围绕公平区域交易。本仓库的 M3 执行状态要求已经有足够双边行为和可识别边缘，不把每次单根重叠都直接升级为可交易区间。

### Tight Trading Range / TTR

紧密交易区间。K 线重叠多、空间小、方向不清，通常更适合等待突破。

### Broad Trading Range

宽交易区间。波动较大，边缘更可能提供交易机会，中部通常没有优势。

### Barbwire

铁丝网。至少 3 根 K 线高度重叠、影线明显，且至少有 1 根 doji；K 线本身可以相对较大。它是很难交易的 tight trading range，多数学习者更适合等待突破。

### Breakout

突破。当前 K 线的高点或低点越过重要价格，即已构成 breakout；这只是最低限度的结构定义。强度、收盘、跟进和市场是否接受新价格，决定突破能否成功，不能反过来写进“突破”的定义。

### Breakout Bar

突破 K 线。形成突破的 K 线，通常是强趋势 K 线。

### Breakout Pullback / BP

突破后回调。突破后数根 K 线内的小回调，若交易者认为突破会延续，它就是突破延续 setup。

### Breakout Test / BT

突破测试。Breakout pullback 回到原始入场价附近，测试突破交易者的 breakeven stop；可以略微越过或差几跳不到。它可能在入场后一两根内出现，也可能在较长运动、甚至 20 根以上之后出现；官方定义没有“通常为 5—10 根”的要求。若原入场价靠近旧边界，它也可能同时检验该区域是否转为支撑或阻力。

### Breakout Mode

突破模式。官方最低定义是：任一方向的突破都应有获得 follow-through 的可能。它常见于区间、三角形、ii/iii、ioi 等结构，但不要求价格一定先“压缩”；“方向接近中性”或“首次突破常失败”只属于 triangle、opening 等具体语境，不能作为所有 breakout mode 的定义。

### Climax

高潮。官方 glossary 的最低定义是运动过快过远后已经反向进入 trading range 或反向 trend；多数 climax 最终只形成 trading range，而不是相反趋势。反转尚未出现前，更准确的说法是 climactic behavior 或疑似高潮，不能把“看起来过度”直接当成已确认反转。

### Pullback

回调。趋势、swing 或 leg 中的暂时暂停或反向运动，尚未回撤超过该运动的起点，交易者仍预期原运动恢复并至少测试前极值。它可以小到一跳或一根 inside / pause bar；若持续扩展，则可能演变成 trading range 或反转。

### Leg

一腿运动。较大结构中的一段小趋势，会突破某一级别的 trend line；通常只有图上至少能区分两腿时才使用这个词。它可以是趋势中的顺势段、回调，也可以是 trading range 中的一段 swing。

### Swing

波段。会突破某一级别 trend line 的较小趋势，通常只有图上至少能看见两个 swing 时才这样命名；它既可出现在更大趋势内，也可出现在横向市场中。它是价格结构，不等同于下面的 swing trade 管理方式。

### Two Legs

两腿。Brooks 常用的修正或目标语言，表示市场以两段运动完成测试或调整。

### Trendline Break

趋势线突破。原趋势结构被破坏的线索，但不等于反转已经成立。

### Major Trend Line

主要趋势线。包含图表上大部分价格行为的趋势线，通常比小型微趋势线更有背景意义。

### Overshoot

超越。价格超过重要 swing point、趋势线或通道线；可能是加速，也可能是衰竭。

## 上下文、位置和目标

这些词用于判断某个信号是否发生在有意义的位置。

### Always In

市场强到如果交易者被迫在 long 和 short 中选一边，会对某一边有足够信心。

### Always In Long / AIL

始终偏多。一方强到交易者若必须持仓，更倾向持有多头。

### Always In Short / AIS

始终偏空。一方强到交易者若必须持仓，更倾向持有空头。

### Control

控制权。当前多空谁更主动，优势是否足够明显。

### Buying Pressure / Selling Pressure

买压 / 卖压。强多头或强空头通过趋势 K 线、影线拒绝和两根 K 线反转等行为累积影响市场。

### Strong Bulls / Strong Bears

强多头 / 强空头。机构级交易者的累积买入或卖出压力，决定市场主要方向。

### Location

位置。价格相对支撑阻力、区间边缘、目标、突破点和大周期结构的位置。

### Support / Resistance

支撑 / 阻力。交易者会改变行为的区域，不是精确价格线。

### Magnet

磁吸目标。价格容易被吸向的明显目标，例如前高、前低、区间边缘或整数位。

### Target

目标。交易者预期价格可能测试的位置，必须和止损、概率、管理一起评估。

### Measured Move

量度目标。当前同向腿预计走出与更早同向腿近似的距离，或突破后走出与此前交易区间/形态高度近似的距离；官方材料也列出基于日内 gap 与 breakout height 的变体。它是可计算的目标区域和 magnet，不是保证，也不能在没有明确参照结构与投射起点时随意“量一段”。

### Vacuum Test

吸向目标的测试。价格快速接近明显目标，可能是订单集中造成，不一定代表趋势质量高。

### 50% Pullback

50% 回调。前一段运动大约一半的位置，用于观察回调深度和控制权变化。

### Prior High / Prior Low

前高 / 前低。常见目标、止盈区、突破点或失败突破位置。

### Swing High / Swing Low

波段高点 / 波段低点。短期结构转折位置，可用于判断趋势、目标和止损。

### High of Day / Low of Day

当日高点 / 当日低点。日内交易者常关注的目标和失败突破位置；24/7 市场要先定义 session。

### Big Round Number

大整数位。心理和视觉价格区域，可能成为目标、止盈区或支撑阻力。

### Moving Average / EMA

均线 / 指数均线。可作背景参考，但不作为机械信号。

### Moving Average Gap Bar

均线缺口 K 线。在强趋势中，一根回调 K 线的高低区间与均线完全不相交，二者之间仍有空隙；随后恢复趋势时常提示趋势仍强，但不是机械入场信号。

### Multi-timeframe / HTF / LTF

多周期 / 大周期 / 小周期。大周期提供背景和目标，小周期提供触发和管理细节。

### Time of Day / Session

时段 / 交易时段。开盘、中段、收盘和低流动性阶段会改变同一形态的意义。

## 订单、触发和失败

这些词用于把价格越过关键点后的行为翻译成交易者入场、退出和被困。

### Order Flow

订单流模型。用价格行为推断哪一边正在入场、退出、止损或被困。

### Stop Entry

用 stop order 触发入场。它不同于 protective stop。

### Buy Stop

价格向上触发后的买入 stop entry，常见于 signal bar 高点上方一跳。

### Sell Stop

价格向下触发后的卖出或做空 stop entry，常见于 signal bar 低点下方一跳。

### Protective Stop

保护性止损。把交易命题的无效点转换成有限损失的订单价格；它不同于 stop entry，也不必机械等于 signal bar 另一端。

### Invalidation

无效点。否定当前交易命题的可观察市场事实或结构；它是 protective stop 的依据，但不是订单本身。

### Stop Order Market / Stop Entry Market

止损单入场者主导的环境。交易者愿意用较差价格换取方向确认，常见于强趋势和强突破。

### Limit Entry

限价入场。价格朝不利方向移动时入场，期待回到公平价格或区间内部。

### Buy Below

在当前价格下方用限价思维买入，常见于 trading range 或弱通道。

### Sell Above

在当前价格上方用限价思维卖出，常见于 trading range 或弱通道。

### Limit Order Market / LOM

限价单交易者主导的环境，常见行为是买低、卖高、scalp。交易者更愿意用好价格换取较少确认，常见于 trading range。

### Market Order

市价单。立即成交的入场方式；在强动量中可能顺势，但风险回报要重新评估。

### Close Entry

收盘附近入场。Buy The Close / Sell The Close 属于强趋势中的特殊 close entry 语言。

### Buy The Close / Sell The Close

强趋势中在趋势 K 线收盘附近追随；只适合强趋势语境。

### One Tick Above / Below

高点上方或低点下方一跳。强调 signal bar 高低点附近可能集中触发单和止损单。

### Signal Bar High / Low

信号 K 线高点 / 低点。常作为 buy stop 或 sell stop 的触发位置。

### Entry Trigger

入场触发点。交易者愿意被触发进场的位置。

### Early Longs / Early Shorts

提前多头 / 提前空头。在 signal bar 还没收盘时提前入场，而不是等收盘后用 stop entry 触发。

### Fade

反向交易。对某个突破或趋势方向做反向交易，通常基于该方向会失败的判断。

### Countertrend

逆势交易。与当前 always-in 方向相反的交易；多数交易者很难长期做好。

### Countertrend Scalp

逆势 scalp。认为原趋势仍会继续，但短期小回调即将出现，试图逆势抓小利润。官方 glossary 明确警告这通常是错误、应避免；本仓库也不因目标小就放宽 Trader's Equation 或权限要求。

### Follow-through

跟进。信号、突破或反转尝试后，后续 K 线继续支持该方向。

### Follow-through Bar

跟进 K 线。entry bar 之后继续支持交易方向的 K 线，通常越早越有意义。

### Surprise Bar

意外 K 线。明显超出预期的强 K 线，常迫使错过者追随、站错者退出。

### Inertia

惯性。强 breakout 或 surprise 后，市场常再次测试该方向，即使中间先回调。

### Disappointment Bar

失望 K 线。官方 glossary 的窄义是 Buy The Close 牛趋势中的熊 K 线，或 Sell The Close 熊趋势中的牛 K 线，趋势方常在其外侧止盈。一般性的“跟进偏弱”可以描述为 disappointment，但不必把每根弱 K 线都命名为 Disappointment Bar。

### Failure

失败。市场未达到交易者目标或先触发 protective stop，常导致反向运动。

### Failed Entry

失败入场。信号触发后没有跟进，随后反向，使刚入场的一方被困。

### Failed Breakout

失败突破。价格突破旧区域后缺乏跟进，并回到原区域。

### Failed Second Entry

失败二次入场。看似合理的 H2 / L2 或 second entry 触发后立刻失败。

### Failed Failure

失败的失败。原突破先失败，随后这个失败又失败，价格恢复原突破方向；因此它在结构上转成 breakout pullback / second signal。两批交易者可能连续被困，但仍需由恢复触发和后续跟进确认。

### Trapped Traders

被困交易者。入场后没有得到预期跟进，被迫在反向运动中退出的一方。

### Stop Run

快速触发一批 stop entry 或 protective stop 的运动；重点是触发后是否有跟进。

## K 线、计数和小结构

这些词用于描述单根 K 线、K 线组合和 Brooks 的 bar counting 语言。

### Trend Bar

趋势 K 线。技术上指开盘与收盘不同、具有实体的 K 线；实体不必很大。强趋势 K 线才强调相对大实体、收盘接近趋势方向极值和较短的反向影线。

### Candle

蜡烛图 K 线。实体表示开收盘之间的区域，影线表示高低点测试。

### Signal Bar

信号 K 线。官方严格定义是实际 entry bar 的前一根，也是 setup 的最后一根；只有入场单实际成交后，它才取得 signal bar 角色。成交前可称 prospective signal bar，但不能把候选触发误记成已有交易。

### Entry Bar

入场 K 线。交易实际成交所在的 K 线。它的方向和收盘可检验初步质量，但“实际发生入场”才是角色定义。

### Doji

十字或相对其整根范围而言实体很小的 K 线。通常表示犹豫、双边交易或暂时平衡；不能只用固定像素或固定点数判断。

### Shaved Body

光头 / 光脚实体。实体的一端或两端没有影线；它本身是中性的外形术语。只有趋势方向一端被削平，例如牛 K 线收在最高点或熊 K 线收在最低点时，才额外体现较强收盘。

### Tail

影线。实体边缘到该 K 线极值之间的价格范围。长影线有时表示测试和拒绝，但这不是定义，也不能脱离位置与后续 K 线自动解释为反转。

### Inside Bar

内包 K 线。其高点不高于前一根高点、低点不低于前一根低点（`high <= prior high` 且 `low >= prior low`）；一侧或两侧相等仍可算 inside bar。

### Outside Bar

外包 K 线。其范围包住前一根，并至少严格突破一侧：`high > prior high` 且 `low <= prior low`，或 `low < prior low` 且 `high >= prior high`。一侧相等仍可算 outside bar；它既可能显示强控制，也可能只是双边混乱。

### Outside Up Bar / Outside Down Bar

向上 / 向下外包 K 线。外包 K 线收在开盘上方或下方，收盘方向帮助判断哪一边更强。

### Pullback Bar / Bar Pullback

回调 K 线。在上涨中低点低于前一根，或在下跌中高点高于前一根，表示短期反向测试。

### Pause Bar

暂停 K 线。没有延续趋势方向极值的 K 线；牛向运动中通常本根高点不高于前高，强牛 K 后只高一跳的小 K 也可视为 pause，熊向镜像。官方 glossary 把它视为一种 pullback；它与 bar pullback 是两项不同几何测试，可能同时成立，并非互斥类别。

### Reversal Bar

反转 K 线。朝原运动反方向的趋势 K 线；单根反转 K 线通常不足以证明大反转。

### ii / iii

母 K 线之后连续两根 / 三根 inside bar；这些 inside bar 通常仍在母 K 线的完整范围内。它常进入 breakout mode，不预测突破方向。

### ioi

Inside-outside-inside。波动收缩、扩大、再收缩的三 K 线结构，常是 breakout mode。

### oo

连续两根 outside bar；表示波动扩大和双边冲突，收盘与随后跟进比名称本身更重要。

### Bar Counting

K 线计数。用 H1/H2/L1/L2 等语言描述回调中的恢复尝试，不是机械数数。

### H1 / H2 / H3 / H4

High 1/2/3/4。牛旗或交易区间下部中，第 1、2、3、4 次本根高点严格高于前高的恢复尝试；相等不计数。High 2 要先出现一个或数个 lower high，再由下一根严格上破前高形成候选；是否实际入场仍取决于 stop order 是否成交。

### L1 / L2 / L3 / L4

Low 1/2/3/4。熊旗或交易区间上部中，第 1、2、3、4 次本根低点严格低于前低的恢复尝试；相等不计数。Low 2 要先出现一个或数个 higher low，再由下一根严格下破前低形成候选；是否实际入场仍取决于 stop order 是否成交。

### High 2 Bull Flag

High 2 牛旗。牛趋势或牛腿回调中的第二次上破尝试，常与小双底相关。

### Low 2 Bear Flag

Low 2 熊旗。熊趋势或熊腿回调中的第二次下破尝试，常与小双顶相关。

### Second Entry

二次入场。在第一次入场后的数根内，市场基于同一逻辑第二次形成实际 entry bar。第一次常缺乏跟进或失败，但“必须先触发 protective stop”不是定义要求；若第二次只形成 setup 而尚未成交，更准确地说是 second signal。

## 形态语言

这些词用于命名市场行为，但都必须回到 context、location 和 management。

### Double Top / Double Bottom

双顶 / 双底。市场第二次测试前一波段高点或低点所在区域；两个测试本身定义形态。突破两次测试之间的 swing point（常称 neckline）是后续确认，不是形态成立的必要定义。

### Double Top Bear Flag

双顶熊旗。熊趋势中的反弹两次测试高位后失败，是趋势延续语境下的双顶。

### Double Bottom Bull Flag

双底牛旗。牛趋势中的回调两次测试低位后失败，是趋势延续语境下的双底。

### Micro Double Top / Bottom

微型双顶 / 双底。通常只跨少数 K 线的二次测试；它既可以是反转信号，也可以在趋势回调中充当延续结构，必须由背景和跟进决定。

### Micro Wedge / MW

微型楔形。仅由数根 K 线形成的三推结构。

### Nested Wedge / NW

嵌套楔形。大三推结构中的某一推内部又形成小楔形。

### Wedge

楔形。通常是三次推动或三次尝试；可作回调、反转尝试或趋势暂停。

### Wedge Flag

楔形旗形。趋势中的三推回调，可能成为顺势恢复背景。

### Wedge Reversal

楔形反转。趋势或通道后期三次推动后反方尝试反转，需要跟进确认。

### Parabolic Wedge

抛物线式楔形。趋势加速后的三次推动，常提示 climactic behavior 或趋势后期；尚未反向时不能据此宣告 confirmed climax。

### Final Flag

最终旗形。趋势后期最后一次顺势整理，突破后若缺乏跟进，可能引发反向运动。

### Triangle

三角形。多次反转形成的 trading range / breakout mode；方向接近中性，首次突破常失败。

### Expanding Triangle

扩大型三角形。高点更高、低点更低，波动扩大但方向不稳定。

### Major Trend Reversal / MTR

主要趋势反转。成熟趋势先突破主要趋势线或通道结构，随后回测原趋势极值，并在更高高点、较低高点、更低低点或较高低点处失败，再由反向信号和跟进确认。只出现一根大反向 K 线、只破趋势线或只测旧极值，都不够构成完整 MTR。

### Higher High MTR

更高高点主要趋势反转。牛趋势中突破前高后失败，形成更高高点反转。

### Lower High MTR

较低高点主要趋势反转。牛趋势后回探未能到达或突破前高，在较低高点转弱。

### Lower Low MTR

更低低点主要趋势反转。熊趋势中跌破前低后失败，形成更低低点反转。

### Higher Low MTR

较高低点主要趋势反转。熊趋势后回探未能到达或跌破前低，在较高低点转强。

### Minor Reversal

小反转。通常只是趋势中的回调或 trading range 化，不一定改变 market cycle。

### Head and Shoulders

头肩。Brooks 语境中不是魔法形态，而是趋势转弱、回探失败和双边交易增加的表现。

## 缺口和重新定价

这些词用于描述市场跳过某些价格、接受或拒绝新价格区域。

### Gap

缺口。两个价格区域之间出现空间，可能是开盘缺口，也可能是日内结构性缺口。

### Gap Up / Gap Down

向上 / 向下缺口。本根 K 线或本交易日的开盘价高于前一根 / 前一日高点，或低于前一根 / 前一日低点。缺口成立不要求新 K 线的整段范围都与前一根分离。

### Gap Close

缺口回补。价格回到缺口前区域，说明市场可能拒绝新价格。

### Gap Reversal

缺口反转。价格在缺口方向尝试后反向进入缺口区域。

### Body Gap

实体缺口。强突破后约 5—10 根出现回调时，回调 K 线的实体仍未与突破前 K 线的实体重叠，即使两者影线已经重叠也仍保留 body gap；它不是泛指任意相邻两根实体之间的小空隙。

### Micro Measuring Gap

微型量度缺口。一根强趋势 K 线前后的 K 线完整区间彼此不重叠，例如强牛 K 线后一根的低点不低于其前一根的高点；这是强度线索，且常引出 measured move，但本身不保证目标到达。

### Breakout Gap

突破缺口。强突破后，旧区间边界与随后价格之间形成持续未回补的区域；它强调市场接受新区间，是否保留仍由回调和跟进验证。

### Measuring Gap

量度缺口。官方 glossary 的最低定义是“最终带来 measured move 的 breakout”：缺口位于 breakout bar 收盘与突破点之间，后续目标通常按突破前交易区间或形态高度投射。它带有事后分类性质；把任意未回补缺口直接称为运动中点，或在结果出现前断定它必然是 measuring gap，都超出了最低定义。

### Exhaustion Gap

衰竭缺口。官方 glossary 指趋势后期出现异常大的顺势 K 线或连续 K 线，随后获利了结增加并形成至少小反转；缺口参考区位于末端 K 线收盘与 breakout point 之间，也可扩展到 climax bars 的另一端。它带有后续确认，但不要求快速或完整回补；仅凭“大”或“发生在图表右侧”仍不能提前逆势。

### Failed Gap

失败缺口。市场开在新区域后无法继续，并回到原区域，使追随缺口方向的交易者被困。

## 交易管理和风险

这些词用于处理入场后的目标、退出、仓位和心理风险。

### Scalp

以小利润快速退出、通常不准备穿越正常 pullback 的交易，常见于 trading range 或双边市场。官方 glossary 警告：若潜在回报小于风险，需要多数交易者难以达到的极高胜率；除非极有经验，潜在回报至少应不低于风险。本仓库直接把小于 1R 的 scalp 设为不批准。

### Swing Trade

持有时间长于 scalp、愿意穿越一个或多个 pullback 以捕捉较大运动的交易。官方典型基线是约 40—50% 概率时寻求至少约 2 倍风险的潜在回报；强 breakout 的概率可更高，交易者也可能在约 1 倍风险处兑现。它是管理方式，不等同于上文的 swing 价格结构。

### TBTL

Ten Bars, Two Legs。大约十根 K 线并形成两腿运动的时间—结构经验法则，常用于管理 swing 或判断回调是否充分；它绝不是任意两根反向 K 线。

### Scaling In

加仓。必须预先设计最大风险；不是临场摊平亏损。

### Scaling Out

减仓。通过部分退出降低管理压力或锁定部分利润。

### Breakeven Stop

保本止损。把止损移到入场价附近，可降低风险，也可能让正常回调提前结束交易。

### Scratch

接近保本退出。可能是小赚、小亏或基本持平。

### Initial / Theoretical Risk

初始 / 理论风险。入场前从预计 entry 到初始 protective stop 的每单位价格距离；官方 glossary 的 `risk` 以此为基础，并提醒滑点等因素可能让最终成交损失更大。

### Actual Risk

歧义术语，不作为本仓库执行变量。Brooks 的公开 Ask Al / webinar 管理语境会把 `Actual Risk` 与 `Initial Risk` 对照，前者可能在入场后小于后者；官方 web glossary 又在 `risk` 条目中用小写 `actual risk` 指滑点导致的更大实际损失。两者不能混成“交易结束后的真实盈亏”。在公开来源未给出统一计算定义前，执行手册只使用明确的 `PlannedLoss`、`OpenRisk` 和已实现盈亏，不用 `Actual Risk` 参与下单或仓位公式。

### Position Size

仓位大小。由 protective stop 距离、计划风险预算和心理承受能力共同限制，而不是服务于信心。

### Risk of Ruin

破产风险。连续亏损、重仓或未受控风险扩大导致无法继续执行计划的风险。

### Day Trade

日内交易。计划在入场当天退出的交易。

### Long / Short

多头 / 空头。Long 是买入或持有多头；short 是卖空或持有空头。

## 时段和交易日

这些词用于把 market cycle 放到一个交易时段内部观察。

### Opening Range

开盘区间。开盘后早期形成的高低范围，后续常成为支撑阻力。

### Opening Range Breakout / ORB

开盘区间突破。突破开盘区间后若有跟进，可能开启 trend day 或 breakout day。

### Opening Reversal

开盘反转。开盘早期价格测试明确的支撑、阻力或磁吸目标，并以另一种形态（如双顶、楔形、失败突破）反转；仅仅先涨后跌或先跌后涨，不足以表达 Brooks 的 opening reversal setup。

### Opening Swing

开盘后一两个小时内形成的主要运动，可能发展成 trend day，也可能只是区间日一腿。

### Trend From The Open

开盘即趋势。开盘后很快形成方向，开盘附近的起始极值保持不被突破，并在早段连续推进、没有 bar pullback；它比普通 trend day 更严格。

### Trend Day

趋势日。一方在当天大部分时间控制市场，虽可出现清楚但受控的回调，仍不断恢复原方向，收盘常接近当天极端位置；它不要求像 trend from the open 那样早段完全没有 bar pullback。

### Trading Range Day

交易区间日。当天由多根 K 线组成的上行腿和下行腿反复测试公平区域，多空双方都能获利，边缘比中部重要；它不等同于一小团 barbwire。

### Reversal Day

反转日。先形成一段明显运动，随后原方向失败并转向另一方向，最终由反方控制；完整回到开盘价或精确重测起点是常见结果，但不是定义要求。

### Early Range Breakout Trend Day

早盘区间突破趋势日。开盘后先形成区间，随后强势突破并获得持续跟进，发展成 trend day。“Breakout Day”是实用分类标签，不是官方 glossary 中独立且严格定义的基础术语。

### Low Liquidity

低流动性。假突破、快速刺穿和缺乏跟进更常见，小样本形态可信度下降。

## 扩展术语

这些词可辅助阅读，但不是主链条节点。只有正文复盘需要时才展开。

### Perfect Trade

完美交易。高概率且回报远大于风险的理论状态。

### Ledge

平台。数根 K 线形成很窄的交易区间；牛 ledge 以多个完全相同的低点为核心，熊 ledge 以多个完全相同的高点为核心，不能只画成普通近似横盘。

### Stair / Shrinking Stairs

台阶 / 收缩台阶。趋势中连续推进到新极端；推进幅度变小可能提示动能减弱。

### Melt-up / Meltdown

过度上涨 / 过度下跌。强 spike 或 tight channel 中价格持续远离公平区域。

### Institution

机构。足以影响市场的大交易者或机构群体。

### HFT / Program Trading

高频交易 / 程序交易。基于统计或程序的大量交易行为。

### Smart Traders

聪明交易者。持续盈利、通常交易较大规模的交易者。

### Five-tick Failure / Tick Trap

差一跳失败。价格几乎到达 scalp 目标但差一点失败。

### Second Signal

二次信号。与第一次信号逻辑相同、相隔数根 K 线后再次出现的 setup。

### Double Top Pullback

双顶回调。双顶后出现较深回调并形成较低高点的空头 setup。

### Double Bottom Pullback

双底回调。双底后出现较深回调并形成较高低点的多头 setup。

### Neckline

颈线。连接头肩、双顶双底等结构中关键 swing point 的参考线。

### Scalper

主要做 scalp 的交易者。

### Scalper's Profit

Scalper 的典型目标利润。具体点数随市场和波动变化。

## 缩写速查

这些是正文中常见的 Brooks 缩写和英文简称。

### AIL / AIS (abbr)

Always In Long / Always In Short。

### BO / BOM / BP / BT (abbr)

Breakout / Breakout Mode / Breakout Pullback / Breakout Test。

### BLSHS (abbr)

Buy Low, Sell High, Scalp。交易区间中的基本管理语言。

### BRN (abbr)

Big Round Number，大整数位。

### BSB / SSB (abbr)

Buy Signal Bar / Sell Signal Bar。

### BTC / STC (abbr)

Buy The Close / Sell The Close。

### DBBF / DTBF (abbr)

Double Bottom Bull Flag / Double Top Bear Flag。

### EMA (abbr)

Exponential Moving Average，指数均线。

### FBO / FF / FT (abbr)

Failed Breakout / Final Flag / Follow Through。

### GD / GU (abbr)

Gap Down / Gap Up。

### HOD / LOD (abbr)

High of Day / Low of Day。

### HTF / LTF (abbr)

Higher Time Frame / Lower Time Frame。

### LOM (abbr)

Limit Order Market。

### MDB / MDT / MW (abbr)

Micro Double Bottom / Micro Double Top / Micro Wedge。

### MTR (abbr)

Major Trend Reversal。

### MRV (abbr)

Minor Trend Reversal。

### OR / ORB (abbr)

Opening Range / Opening Range Breakout。

### TBTL (abbr)

Ten Bars, Two Legs。

### TTR (abbr)

Tight Trading Range。
