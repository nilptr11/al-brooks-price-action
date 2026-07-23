# 市场周期（Market Cycle）

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## 它解决什么问题

Market cycle 是读图的第一层。它决定顺势、回调、区间交易、突破、反转或等待中的哪一类行为更合理。

## 基础层级

先做两层判断：

1. 基础状态是 trend，还是 trading range？
2. 如果是 trend，当前主要是已形成方向控制的 breakout phase（spike），还是 channel？

这层判断可以展开成连续谱：`breakout phase / spike -> tight channel -> broad channel -> trading range`。越向右，回调、重叠和双边交易通常越多。这里的 breakout phase 是突破已获得足够接受并形成方向控制后的趋势阶段，不是价格刚越过重要价位的单个 breakout event / attempt；“获接受”是本仓库对中间状态的整理标签。具体结构线索和典型根数见[趋势和通道](01_trends_and_channels.md)，不同突破粒度和命名边界见[突破和突破模式](03_breakouts_and_breakout_mode.md#本仓库的分层口径)。

### 状态必须绑定周期和观察窗口

Market-cycle 标签不是脱离尺度的永久属性。同一段价格在较高周期可能是一根 breakout bar，在当前交易周期表现为 tight channel，在更低周期又能展开成 broad channel 和 trading range。因此每次判断至少要隐含或写明：

- 使用哪个时间周期；
- 判断覆盖哪一段可见价格；
- 哪一层是当前交易周期的主要状态，哪一层只是局部腿或外层背景。

不同周期的标签可以同时为真，不能用小周期的局部反向 trend 自动宣告大周期趋势结束，也不能用大周期方向否认交易周期已经进入双边状态。周期的具体分工见[周期与时段 Context](../02_context/02_time_and_timeframes.md)。

### 状态不清时的逐层 fallback

保守归类必须作用于当前未决的层级，不能把不同层的规则混用：

- 如果连 trend 还是 trading range 都分不清，先按 trading range 处理；混乱本身就是区间证据。
- 如果已经确认属于趋势类环境，只是分不清 breakout phase 还是 channel，先按 breakout phase 处理。
- 如果已经确认是 channel，只是分不清 tight 还是 broad，先按 tight channel 处理，避免过早采用逆势逻辑。
- 如果分不清 broad channel 还是 trading range，先按 trading range 处理。

这些是信息不足时的管理假设，不是对市场真实标签的永久宣判。新突破、follow-through、重叠和双边获利等证据出现后，必须重新分类。

## Reversal 与 Minor Reversal

Reversal 的广义含义是价格方向或行为向相反状态变化；它可以是 trend 转为 trading range、trading range 突破成 trend，或原趋势转为 opposite trend。可交易意义上的 reversal 必须绑定时间周期、观察窗口和被反转的原状态；一根影线或极小方向变化在最宽语义上也可叫 reversal，却不能因此直接升级为新的交易趋势。

Minor reversal 是当前周期中逆着既有趋势、但尚未建立相反趋势控制的反转尝试。第一次逆势反转通常先按 minor 处理，常见结果是原趋势中的 pullback / flag，或先进入 trading range；它不自动授权按 opposite trend 管理。该默认只说明状态先验，不能替代对反向突破与 follow-through 的观察。

[Major Trend Reversal](../05_setups/04_major_trend_reversal.md) 是一类要求旧趋势已出现有意义的结构破坏和旧极值测试、反方正尝试建立可持续 swing 的 Setup。早期候选可以在强反向 breakout 前承担较低概率风险；反向 breakout 与 follow-through 出现后，控制转移才得到更多确认。它不是“幅度较大的 minor reversal”，也不能仅凭形态名称确认。背景极强时状态可能很快切换，背景模糊时则可能经过较长 trading range 才清楚，因此 Core 不用固定棒数区分 minor 与 major。

## 跨层叠加信息

Breakout mode 说明任一方向的突破都可能获得跟进，是双向候选状态；过快过远的 climactic move 提示当前运动可能接近转换；回调加深、双边交易增加、趋势线突破或顺势突破缺乏跟进等 transition evidence 则记录状态可能正在变化。它们都可以叠加在当前基础状态或趋势阶段上，不应与 trend / trading range 当成互斥并列项。只有加入具体 Context 与入场依据后，breakout-mode 候选才形成 Setup。

课程会用 climactic move / climax bar 描述当下的加速与极端行为；官方 glossary 的 `climax` 词条则要求运动已经反向进入 trading range 或 opposite trend。两种用法不能互相覆盖，完整边界见[高潮和状态转换](04_climax_and_transition.md)。

这些都不是静态标签。形成方向控制的 breakout phase（spike）可以进入 tight channel，再扩展为 broad channel 或 trading range；trading range 边界可以出现 breakout event / attempt，失败后仍维持区间，获得接受并形成方向控制后才可能把基础状态更新为 trend。这是常见演化路径，不是必须依次走完的固定四步循环；市场可以跳过阶段、在局部与外层呈现不同阶段，也没有固定持续根数。

## 读循环的问题

每次读图先问：

- 基础状态首先是 trend，还是 trading range？
- 若是 trend，当前更像形成方向控制的 breakout phase（spike）、tight channel 还是 broad channel？
- 回调是否开始变深？
- 双边交易是否增加？
- 突破是否有跟进？
- 价格是否开始围绕公平区域来回测试？
- 是否只是出现 breakout mode、高潮式推进或 transition evidence，而基础状态尚未改变？
- 当前交易方式是否仍适合当前循环？

如果 market cycle 判断错，后面的形态通常都会被误读。

## 相关来源

- [`SRC-GLOSSARY`](../../reference/official_sources.md)、[`SRC-MANUAL`](../../reference/official_sources.md) 与 [`SRC-STRONG-LEGS-2016`](../../reference/official_sources.md)：Market Cycle、trend / trading range 与 breakout phase—channel 连续谱。
- `SRC-COURSE-01-36`：课程 12A–12C、13A、14C–14E、16A–18F、21A；状态层级、模糊时 fallback、周期绑定和 minor / major reversal。
- `SRC-COURSE-37-52`：课程 37A–37B、41B、43A–49E；多周期执行、breakout—channel—trading range 演化及局部/外层状态。
