# 周期与时段 Context

> **状态：Core / Definition**
>
> 本文是周期分工、实时 session state、最终日型与开盘概念的权威定义页，并说明它们怎样进入 Context。具体时段倾向会因市场而异；没有当前品种样本支持时，不把经验倾向写成固定规则。

## 多周期如何分工

大周期主要帮助识别 market cycle、重要支撑阻力、大型区间和潜在目标；交易周期负责当前 setup、entry、stop 和管理。大周期不是用来否决所有小周期机会，小周期也不能因出现漂亮信号而忽略大周期关键位置。

周期冲突时，降低确定性并问：

- 哪个周期决定主要位置和目标？
- 当前 entry 与 protective stop 来自哪个周期的结构？
- 小周期运动是否真的足以改变大周期判断？
- 承受大周期波动的仓位是否足够小？

入场、stop 和目标周期应协调。用小周期 entry 追求大周期目标，就必须容许相应的正常波动；用大周期背景做短线 scalp，也不能自动获得大趋势目标。

### 入场周期与管理周期一致

较小周期可以用于提前触发或精细化 entry，但这种多周期分工必须在承担风险前定义。若交易依据五分钟结构、stop 和目标建立，成交后不能只因害怕回吐就临时切到一分钟图，从普通小级别反转中寻找退出理由；这会替换原计划的噪声尺度、持有时间和 Trader's Equation。

反过来，小周期 entry 若计划持有大周期 swing，也必须使用能容纳大周期正常波动的 stop 和足够小仓位。新的小周期价格只有在计划预先允许，或其累积强度已经足以改变交易周期的 premise 时，才应改变管理。

## 时段如何影响 context

时段主要改变流动性、波动、剩余时间和目标可达性。开盘常有快速定价和突破尝试；完成大运动后的中段更可能双边交易；临近时段结束时，剩余时间可能不足以支持新 swing。

这些是观察方向，不是跨市场定律。每个市场都应先定义自己的 session，并用历史样本确认哪些时段差异具有稳定意义。执行时只保留会实质改变当前位置、目标空间或订单质量的时段信息。

接近 session 结束时，剩余时间可能不足以让反转重新测试 entry 或让新 swing 到达远端目标；同一反向证据因此可能要求更快降低日内风险。这只适用于不准备跨 session 持有的计划。允许隔夜、全天候交易或使用不同结算边界的方案，必须按自己的持仓期限重新定义时间风险。

对必须在本 session 内结束的计划，早段可行的宽 protective stop、逆向 limit entry 或 scale-in，可能依赖价格有足够时间回到成本区；进入尾段后，这个前提可能已经消失。不能只因价格 stop 尚未触发就忽略收盘前被迫退出的路径风险，也不能继续加仓等待已经缺少实现时间的均值回归。尾段才由反转形成的弱 channel 也更可能只是 trading range 的一条腿；除非随后出现清楚突破、跟进和足够目标空间，否则不能直接借用较早形成趋势通道的延续假设。

## 实时 Session State 与最终日型

日内结构仍使用同一套 market-cycle 语言，只是观察窗口被预先定义为一个 session。盘中只能描述**截至当时**的状态；最终 day type 是时段结束后的结果标签，不能反向参与候选、入场或管理判断。

为避免盘中用最终 day type 回填，本仓库采用以下实时状态与结果标签分工。课程和 glossary 支持各标签及其行为，但这四项是仓库整理的检查框架，不宣称是 Brooks 给出的固定、互斥且穷尽的 day-type 清单：

- **Trend session / trend day**：一方在 session 的主要部分保持控制，真实但受控的回调不自动否定趋势。
- **Trading-range session / range day**：价格在 session 内围绕公平区域反复双向测试；单条腿可以很强，不能因此提前把全天改写成趋势日。
- **Reversal session / reversal day**：session 先向一个方向推进，随后原方向失去接受，控制和持续路径转向另一侧。
- **Early-range breakout trend session**：session 开始后先形成区间，再由获得接受的突破发展成趋势；它是事件顺序描述，不是独立于 market cycle 的第四种基础状态。

这些标签会随新价格信息变化。盘中记录“当前更像什么，以及哪条新证据会改变判断”，不要为得到某种 day type 主动选择历史片段。对于 24 小时市场，session 及交易日边界必须在观察前固定。

## 开盘概念的分层

课程使用的开盘对象并不都指同一个固定窗口。记录时至少区分：

- **Opening / first swing**：从 session 开始到当天第一段向上或向下 swing 结束的描述性阶段。它的终点常要在走出若干后续价格后才清楚，因此不能在实时中假装存在一个可精确预知的结束 K 线，也不等于下面的内部固定窗口。
- **Opening Breakout Mode（Opening BOM）**：课程对这个名称也有较宽泛的用法，包括开盘强突破后很快形成早期区间、等待下一次方向选择的情形。为保持可执行和可审计，本仓库把“首根 K 线之后，价格对首根两侧先后进行测试和反转”定义为较成熟的 Opening BOM 子型：它形成早期双向候选区间，边界随早期新高、新低和失败尝试更新，不由固定根数单独定义；尚未突破时采用 trading-range / breakout-mode 逻辑，只有强突破和跟进才切换为顺势。这是仓库的操作性收窄，不是把课程的宽泛用法改写为唯一官方定义。
- **First-18-bar heuristic**：课程另外观察前 18 根 K 线的高低范围以及其后附近的突破或反转。`18` 是课程针对相应日内图表的近似成熟度提示，不是神奇阈值，也不与 Opening BOM 同义；它只能作为 Reference / Strategy 中经品种和周期验证后的启发式，不能成为本页的通用定义或自动入场条件。
- **Session opening window（仓库内部口径）**：若研究、回测或策略需要一个固定 opening range，必须在观察前明确根数或时间窗口，并只用当时可见数据计算高低点。它是内部可复现 schema，不宣称等同于 Brooks 的 first swing、Opening BOM 或 first-18 heuristic。
- **Opening-range breakout**：价格离开当前计划明确声明的 opening-range 边界，首先只构成 breakout event / attempt；必须同时注明边界来源，例如 Opening BOM 的动态边界、first-18-bar range、内部预设窗口，或另一项在观察前显式声明的来源。是否获得接受仍看收盘、跟进、回踩和旧区域是否被重新接受，单次刺穿不够。
- **Trend from the open**：开盘后很快形成方向，初始极值在随后许多根中保持，且没有真正 pullback；它比普通 trend day 更强调趋势从 session 开始阶段形成。
- **Opening Reversal**：session 早段的初始方向在已知支撑、阻力或旧价格区域附近失去接受，随后形成反向路径。它可能与 double top/bottom、wedge 或 failed breakout 重叠，但名称本身不构成交易许可；相同结构若到较晚阶段才出现，只称普通 reversal 或 MTR，不能继续借用 Opening Reversal 的早段语境。具体“多早”必须随品种、session 和 bar interval 校准，本页不设硬分钟数。

Opening gap 只说明开盘重新定价，不预设当天方向；opening gap 与 gap reversal 的最低定义见[缺口专题](../04_patterns/07_gaps.md)，新价格是否获得接受见[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)。开盘仍先判断基础状态是 trend 还是 trading range；若为 trend，再判断当前主要是已形成方向控制的 breakout phase（spike）还是 channel，同时另外记录 breakout mode、climactic move 和 transition evidence，并结合 session open、前一时段高低点、较大周期位置和 follow-through 更新判断。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018`、`SRC-COURSE-01-36`（课程 04 p271–276、09C、12B、16C、19A、19C）与 `SRC-COURSE-37-52`（课程 37A、40A–41D、45A–46E、48A–49E、51D、52A；其中 48D 说明 Opening BOM 的宽泛用法并区分其成熟子型与 first-18 heuristic，48E 保留 Opening Reversal 的早段边界，48I–48K 支持尾盘时间风险和高周期磁点限制）。
