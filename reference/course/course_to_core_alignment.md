# 01–52 课程综合与 Core 对齐

> **状态：Course Synthesis / Core Alignment**
>
> 本文把 01–52 全部课程材料串成一套完整思想，并逐一对齐 `core/` 的 31 篇正文。它用于决定 Core 是否需要保留、补充、加限定或重写，本身不取代逐讲材料，也不直接规定交易动作。
>
> **实施状态：P0、P1、P2 调整及第二轮全课程精修已完成；现有七层结构保持不变。**

## 一、覆盖范围与使用方式

本次综合覆盖：

- 01–52 共 52 个课程主编号；
- 191 个实际分讲 Markdown；
- `core/` 七个专题目录下的 31 篇正文；
- 课程中的定义、镜像、状态转换、规则—案例、数学张力和管理边界。

逐讲证据仍以本目录的编号文件为准；跨讲重复见[重复矩阵](repetition_matrix.md)，数字和规则冲突见[边界与冲突](boundaries_and_conflicts.md)。本文只负责回答三个问题：

1. 每一章在完整课程中承担什么职责？
2. 这项思想应该进入 Core、Reference、Strategy 还是 Execution？
3. Core 当前是否已经完整表达，若没有，具体缺什么？

### 对齐状态

| 状态 | 含义 |
| --- | --- |
| 完整覆盖 | Core 已表达课程主旨和关键边界，不应为重复而重写 |
| 需要补边界 | 主旨存在，但缺少会改变理解、方向或风险的条件 |
| 需要补连接 | 各概念分别存在，但缺少跨页面的状态转换或管理关系 |
| Reference-only | 属于产品知识、统计争议、指标或因果叙事，不应成为 Core 定义 |
| Strategy / Execution | 属于具体入场版本、时间窗口、订单参数或安全流程，不应塞入 Core |
| 冲突待定 | 课程内部存在算术、数字或译文冲突，核清前不能写入权威定义 |

## 二、01–52 串联后的完整思想

课程的完整思想不是一组形态信号，而是一条持续更新的判断链：

```text
价格与成交形成可观察图表
    ↓
判断 Market Cycle：trend / trading range
    ↓
若为 trend，再判断 breakout phase / tight channel / broad channel
    ↓
结合 Context：位置、压力、Always In、支撑阻力、周期与剩余时间
    ↓
Pattern 只描述当前结构，不直接生成交易
    ↓
Setup 把状态、位置、触发和失效事实组合成一个交易命题
    ↓
Trader's Equation 检查同一方案的概率、风险、回报和成本
    ↓
Trade Plan 固定 entry、protective stop、target、仓位和管理方式
    ↓
成交后观察 acceptance、disappointment、failure 与 premise 变化
    ↓
继续持有、主动退出、分批处理或在新信号下重新入场
```

这条链有七个不能拆开的原则：

1. **状态优先于形态。** 同一个 H2、楔形、双底或强 K 线，在紧密趋势、宽通道和交易区间中的意义不同。
2. **位置与路径决定形态是否有价值。** 支撑阻力、旧高低点、突破点、测量目标、入场价和剩余时间会改变现实回报。
3. **概率只能属于定义清楚的事件。** 40%、60%、70%、75%、80%、90% 的分母、目标距离和观察时点不同，不能互相替换或相乘。
4. **确认与价格存在交换。** 早入获得较好价格和较近结构，但概率较低；等待突破与跟进提高确认，却常带来更远止损和更小剩余空间。
5. **管理必须继承原交易构造。** Scalp、swing、stop entry、limit entry、单次入场和分批建仓分别拥有不同的止损、目标和结果分布，不能成交后随意互换。
6. **前提必须随新证据更新。** 正常回调不自动否定 swing；强反向突破、持续跟进、交易区间化或 Always In 翻转则可能要求提前退出。退出后可以重新入场。
7. **风险控制独立于方向判断。** 小止损不等于好交易，宽止损不等于账户风险大；结构决定止损，仓位决定金额风险，计划内总敞口决定最坏损失。

## 三、01–52 每章职责与知识去向

| 课程 | 在完整体系中的职责 | 主要增量 | 仓库去向 |
| --- | --- | --- | --- |
| [01](01.md) | 建立术语和基础框架 | 把趋势、区间、K 线、scalp/swing 等词放进同一语言系统 | Core 方法主线与 Glossary |
| [02A–D](02A.md) | 解释图表、价格行为和市场反应 | 成交量、新闻、Pain Trade、Context、Momentum；重点是观察价格反应而非猜参与者 | Core 方法、Context、Acceptance；部分市场机制留 Reference |
| [03A–E](03A.md) | 补充外汇产品知识 | 报价、pip、点差、保证金、rollover、carry 和损益换算 | Reference-only；不进入通用价格行为 Core |
| [04](04.md) | 建立交易环境和周期分工 | 交易周期、大周期、均线及观察设置怎样服务 Context | Core 周期与时段 Context |
| [05](05.md) | 讨论程序化交易和市场操纵叙事 | 算法、高频和操纵观点不能替代可观察价格证据 | 方法边界；具体事实留 Reference |
| [06](06.md) | 描述成功交易所需行为 | 纪律、耐心、客观、风格适配和风险承受 | Core 风险心理；执行纪律 |
| [07A–B](07A.md) | 把学习起步连接到实际选择 | 市场和周期选择、选择性交易、情绪及客观执行 | Core 时间周期、风险心理；Execution |
| [08A–D](08A.md) | 建立 K 线与 signal 语言 | Trend/TR bar、反转、内外包、ii、signal bar 与 Context | Core Pattern、Bar Types、Setup 边界 |
| [09A–C](09A.md) | 定义回调和 H/L 计数 | H1/H2/L1/L2、bar counting、endless pullback、多周期计数 | Core H/L、趋势延续、二次入场 |
| [10A–B](10A.md) | 建立买卖压力语言 | 收盘、连续性、影线、广义 gap 和区间压力怎样显示控制变化 | Core Context、Acceptance、Gap |
| [11A–D](11A.md) | 系统定义 Gap 家族 | Opening、micro、MA gap bar、measuring/exhaustion gap 和目标 | Core Gaps、支撑阻力、趋势延续 |
| [12A–C](12A.md) | 建立 Market Cycle | 突破、通道、交易区间、转换，以及趋势/区间惯性 | Core Market Cycle |
| [13A–C](13A.md) | 连接 Always In、方程和管理 | 方向控制、概率—风险—回报、scalp/swing 选择 | Core Context、Trader's Equation、Scalp/Swing |
| [14A–E](14A.md) | 系统解释趋势和通道 | 趋势结构止损、急速—通道、紧密/宽幅、小回调趋势 | Core Trends and Channels |
| [15A–G](15A.md) | 系统解释突破与失败 | Breakout attempt、跟进、surprise、第二腿、第二腿陷阱、测量/衰竭 gap | Core Breakouts、Acceptance、Second Entries |
| [16A–F](16A.md) | 展开通道的构造和演化 | 动态重画、边界测试、70/30 经验、周期嵌套、通道向区间演化 | Core Trends/Channels、Transition、Context |
| [17A–B](17A.md) | 细化紧密通道和微型结构 | 微型通道、小回调趋势、首次反转危险和紧密区间 | Core Trends/Channels、Trading Ranges |
| [18A–F](18A.md) | 系统解释交易区间 | 区间连续谱、BLSHS、BOM、限价市场、真空、成功突破和第二腿陷阱 | Core Trading Ranges、LOM、Breakouts |
| [19A–E](19A.md) | 建立支撑阻力和磁点体系 | 市场状态改变水平作用；多周期磁点、整数位、入场价和 50% 回调 | Core Context、Support/Resistance/Targets |
| [20A–B](20A.md) | 定义测量移动 | Leg 1 = Leg 2、区间/突破高度、双向投射和目标选择 | Core Support/Resistance/Targets |
| [21A–D](21A.md) | 建立反转总框架 | 次要/主要反转、早入/确认、压力、TBTL 和反转交易方程 | Core MTR、Trader's Equation、Scalp/Swing |
| [22A–D](22A.md) | 完整展开 MTR | 趋势线破坏、旧极值测试、HL/LH、重新入场和失败后重置 | Core Major Trend Reversal、Acceptance |
| [23A–B](23A.md) | 定义 Final Flag | 候选与事后确认、趋势晚段、尺度、BOM 和低概率早入 | Core Final Flags、Climax |
| [24A–E](24A.md) | 系统解释 Wedge | 三推、坏楔形、抛物线楔形、75/25 先验和突破后更新 | Core Wedges、Climax、Breakouts |
| [25A–B](25A.md) | 解释广义双顶双底 | 双测试、旗形、颈线、支撑阻力复测和失败机制 | Core Double Tops/Bottoms、MTR |
| [26A–B](26A.md) | 定义三角形与扩张三角形 | 五腿成熟度、压缩/扩张、旗形与反转职责 | Core Triangles、Breakout Mode |
| [27A–B](27A.md) | 将头肩形还原为价格行为 | MTR 骨架、右肩、颈线失败及区间本质 | 不建独立 Core 形态；归 MTR、Double Tests、Trading Range |
| [28](28.md) | 将圆弧顶底还原为状态过程 | 圆弧常是交易区间或 endless pullback 的另一标签 | 不建独立 Core 形态；归 Trading Range、Pullback |
| [29A–E](29A.md) | 系统解释 Climax | 事后命名、V 形过渡、TBTL、连续高潮、真空、gap 和周期重置 | Core Climax/Transition、Gaps、Scalp/Swing |
| [30A–E](30A.md) | 深入 Trader's Equation | 微小优势、概率/RR 交换、40–60、等距目标和统计冲突 | Core Probability/Risk/Reward；冲突留 Reference |
| [31A–D](31A.md) | 明确 Scalp 与 Swing | 目标尺度、持有方式、成本、2R、强突破和计划一致性 | Core Scalp/Swing、Trade Plan |
| [32A–C](32A.md) | 系统解释订单 | Stop、limit、market、bracket/OCO、状态与订单选择 | Core Order Logic；平台安全进入 Execution |
| [33A–G](33A.md) | 系统解释 Stop | 保护止损、结构失效、追踪、宽/窄止损、保本和仓位反推 | Core Stop、Trade Plan、Risk |
| [34A–B](34A.md) | 区分初始与实际风险 | Initial risk、事后 Actual Risk、目标替代和样本统计问题 | Core 风险口径需补边界；统计冲突留 Reference |
| [35A–C](35A.md) | 展开分批建仓数学 | 加权均价、层数、间距、共同止损、最坏总风险和高胜率代价 | Core Scaling In/Out、Trade Plan |
| [36A–B](36A.md) | 解释成交后的计划更新 | 利润保护、目标变化、OPM 误区和默认管理 | Core Trade Plan、Acceptance |
| [37A–B](37A.md) | 将前 36 讲重新整合 | 状态—交易构造—双周期—40/60—默认目标 | Core 方法主线和全局交叉检查 |
| [38A–D](38A.md) | 顶部 MTR 完整案例 | 卖压、较低高点、确认、再次入场、止盈和止损 | Core MTR；具体计划进入 Strategy |
| [39A–D](39A.md) | 底部 MTR 镜像案例 | 买压、更高低点、概率交换、追踪止损和开盘案例 | Core MTR；具体计划进入 Strategy |
| [40A–E](40A.md) | 解释趋势末端追价和失望 | FOMO、Final Trend Bar、Give-up Bar、入场价测试、被套和风格切换 | Core Climax、Acceptance、Risk Psychology |
| [41A–D](41A.md) | 展开强突破和 Buy/Sell the Close | 收盘入场、swing stop、突破—通道、陷阱与趋势退出 | Core Breakout/Trend Setup；具体动作进入 Strategy |
| [42A–C](42A.md) | 重新整理高潮和失败反转 | minor/major climax、测量/衰竭 gap、微型通道和区间第二腿 | Core Climax、Gaps、Second-leg Trap |
| [43A–D](43A.md) | 紧密多头通道专题 | 首次反转、顺势买入、逆势分批困难、区间化 | Core Trends/Channels、Scaling；策略案例 |
| [44A–D](44A.md) | 紧密空头通道镜像 | 首次反转、顺势卖出、逆势分批困难、区间化 | Core Trends/Channels、Scaling；策略案例 |
| [45A–E](45A.md) | 宽幅多头通道专题 | 趋势/区间双重属性、周期嵌套、失败反转、50% 回调和买入区 | Core Trends/Channels、Context；策略案例 |
| [46A–E](46A.md) | 宽幅空头通道镜像 | 主要高点、局部反转、逆势管理、50% 回调和卖出区 | Core Trends/Channels、Context；策略案例 |
| [47A–D](47A.md) | 交易区间综合专题 | 困惑诊断、80% 规则、第二腿陷阱、限价交易、最终突破 | Core Trading Ranges、LOM、Second Entries |
| [48A–K](48A.md) | 日内时段和开收盘专题 | 开盘状态、前日/高周期背景、前 18 根、日中转换、尾盘时间风险和磁点 | Core Time/Session；具体窗口进入 Strategy/Execution |
| [49A–E](49A.md) | 用整日案例验证状态重判 | 开盘反转、急速—通道、区间反复、高潮、第二腿陷阱和尾盘转换 | 用于验证全部 Core；不新增独立定义 |
| [50A–E](50A.md) | 剥头皮专题 | 适用状态、交易者门槛、低周期陷阱、TICK 辅助和案例管理 | Core Scalp/Swing；TICK 留 Reference；具体计划进入 Strategy |
| [51A–D](51A.md) | 解释因错误造成的亏损 | 错误信念、坏交易、心理止损、低风险误区、正确 stop、分批风险和周期一致性 | Core Trade Plan、Risk Psychology、Stop、Scaling |
| [52A–B](52A.md) | 汇总防止大亏的管理规则 | 三层保护、趋势末端失望、前提改变、保本边界和 trapped traders | Core Acceptance、Trade Plan、Risk Psychology |

## 四、跨章节思想怎样落入七个 Core 专题

| Core 专题 | 课程连续链 | 应保留的统一思想 | 不能混入的内容 |
| --- | --- | --- | --- |
| `00_method` | 01–02 → 12–13 → 30 → 37 → 51–52 | 状态、背景、形态、Setup、方程、计划和更新是一条链 | 产品规格、固定胜率、Z-score 冲突 |
| `01_market_cycle` | 12 → 14–18 → 29 → 40–47 → 49 | Trend/TR 基础状态；breakout phase、tight/broad channel 连续谱；区间最终突破 | 把 breakout mode 当第三种基础状态；把 climax 当立即反转信号 |
| `02_context` | 02D、04、10、19–20 → 37 → 45–49 | 位置、压力、Always In、支阻、目标、周期和剩余时间共同改变交易方程 | 猜测真实订单身份；固定开盘/尾盘参数 |
| `03_acceptance_and_order_logic` | 08–10、15、18 → 32–33 → 40–42、47、52 | 触发后看跟进、收回、失望、失败；区分 stop entry/protective stop；识别二次尝试和陷阱 | 把第二次信号当独立优势；把限价入场当无限摊平 |
| `04_patterns` | 08–11 → 23–29 → 42 | 形态描述压力和结构，不脱离 Context；候选与事后结果分开 | 为头肩、圆弧等同义标签重复建立交易规则 |
| `05_setups` | 09、15、18、21–22 → 38–47 | 趋势延续、突破延续、区间 fade、MTR 是四种交易命题原型 | 具体价格、订单寿命、固定时间窗口和完整执行方案 |
| `06_trade_plan_and_management` | 30–36 → 50–52 | 同一版本的 entry/stop/target/size/management；scalp/swing；总风险；心理纪律 | 课程内部错误算术、业绩承诺和未经限制的加仓 |

## 五、Core 31 篇正文逐项对齐

### 00_method

| Core 页面 | 课程依据 | 当前覆盖 | 差异与建议 |
| --- | --- | --- | --- |
| `00_al_brooks_thesis.md` | 01–02、06–08、12–13、30、37、49、51–52 | **完整覆盖** | 已把状态、Context、Pattern、Setup、Trade Plan、方程和成交后更新连成一条链。只需链接本文，不应再塞入章节摘要。 |
| `01_probability_risk_reward.md` | 13A、21B、30A–E、31、34A–B、37B、39C、51A–C | **需要补边界** | 方程和 40–60 已正确；建议新增“初始风险、事后 Actual Risk、账户金额风险、个人风险”四分法，并明确 Actual Risk 不能用单笔赢家的事后浅回调证明事前正期望。不得引入 30C 的 Z-score 解释、p2362 的错误结论或 34B 的十亿交易者算例。 |

### 01_market_cycle

| Core 页面 | 课程依据 | 当前覆盖 | 差异与建议 |
| --- | --- | --- | --- |
| `00_market_cycle.md` | 12A–C、14、16–18、37、43–49 | **完整覆盖** | Trend/TR 两层基础状态与 breakout phase—channel 连续谱已清楚；breakout mode、climax 和 transition 也未被误列成并列基础状态。无需重写。 |
| `01_trends_and_channels.md` | 14A–E、16A–F、17A–B、43–46 | **完整覆盖** | Tight/broad channel、首次反转、70/75 概率分母、局部/外层周期和逆势获利难度均已覆盖。保持数字限定，不新增镜像重复。 |
| `02_trading_ranges.md` | 18A–F、28、37、42C、47A–D、49 | **需要补连接** | 普通区间、TTR、宽区间、80% 与 BOM 例外已完整。建议补一个短连接：区间内强第二腿可能是陷阱，只有真正脱离区间并获得接受才升级为趋势；链接 `03_second_entries_and_traps.md`。 |
| `03_breakouts_and_breakout_mode.md` | 15A–G、18B/F、20B、24E、29E、41–42、47 | **完整覆盖** | Breakout event、接受、breakout phase、BOM 和 second-leg 倾向已区分。可增加反向链接到“区间第二腿陷阱”，但不需要重写定义。 |
| `04_climax_and_transition.md` | 23、24D、29A–E、40A–E、42A–C、48J、49、52 | **需要补连接** | 进行时/事后 climax、TBTL 和首次反转边界已完整。建议补“Final Trend Bar/趋势末端失望”作为管理线索，并链接 Acceptance；不得把它升级成顶部/底部预测。 |

### 02_context

| Core 页面 | 课程依据 | 当前覆盖 | 差异与建议 |
| --- | --- | --- | --- |
| `00_context_location_control.md` | 02D、08D、10、13、19、37、40、43–49 | **完整覆盖** | Buying/selling pressure、Always In、位置和路径空间已完整；明确不猜订单身份。无需另建“压力”目录。 |
| `01_support_resistance_targets.md` | 11D、19A–E、20A–B、29、33F、34B、42、48 | **基本完整** | 建议检查是否明确区分“目标是 magnet”与“目标必到”，并补入 entry price/最高最低收盘作为失望交易者的潜在测试磁点；不采用 52B 的“1–3 或 20 根必测”数字。 |
| `02_time_and_timeframes.md` | 04、09C、12B、16C、19A/C、37A、45–46、48–49、51D、52A | **需要补边界** | 多周期分工和 session 已完整。建议明确：若依据交易周期入场，主要管理也应使用该周期；只有入场前定义的多周期方案才能用小周期触发或退出，不能因压力临时切周期。补充临近 session 结束时目标可达性下降，但保留市场/持仓计划条件。 |

### 03_acceptance_and_order_logic

| Core 页面 | 课程依据 | 当前覆盖 | 差异与建议 |
| --- | --- | --- | --- |
| `00_stop_entry_vs_protective_stop.md` | 08D–09、32A–C、33A–G、41B/D、51B–D、52A | **需要补风险边界** | 两类 stop 和多个结构候选已清楚。建议补“保护性 stop 应实际在场，不能只靠 mental stop”，同时明确 stop 不能保证成交价格，滑点/跳空属于执行风险。 |
| `01_acceptance_and_failure.md` | 10、15、18、19D、33D、36、40、42、52A–B | **需要补连接** | Acceptance、disappointment、premise change、trade failure 和 trapped traders 已完整。建议加入三层保护的概念连接：硬 stop、合理反向结构、无标准形态但连续强反向动量；并写明退出后可在原趋势恢复时重新入场。 |
| `02_limit_order_market.md` | 18D–E、32B–C、35、43C–47D、50E、52B | **完整覆盖** | 已限定区间/宽通道、成本、计划内分批和强突破失效。不要把限价成交或“差一 tick”写成保证。 |
| `03_second_entries_and_traps.md` | 09、15D、18B、21D、24、42C、47C、49C、51B | **完整覆盖** | 已明确第二信号继承上层命题，不能挽救坏 Context。建议只增加从 Trading Range 页面来的第二腿陷阱交叉链接。 |

### 04_patterns

| Core 页面 | 课程依据 | 当前覆盖 | 差异与建议 |
| --- | --- | --- | --- |
| `00_patterns_are_language.md` | 02D、08D、21–29、42 | **完整覆盖** | 已正确把 Pattern 与 Setup 分开。应补一句维护原则：头肩形、圆弧顶底等替代标签不因课程有专讲就自动建立独立 Pattern Definition。 |
| `01_bar_types.md` | 08A–D、10、40C、52 | **基本完整** | Trend/TR/reversal/signal/entry bar 边界已覆盖。Final Trend Bar 和 Give-up Bar 是趋势末端的情境角色，建议链接 Climax/Acceptance，不宜扩成新的最低 K 线类型。 |
| `02_h1_h2_l1_l2.md` | 09A–C、14、17、22、24、49B | **完整覆盖** | 几何计数、触发和 Context 边界已经清楚。无需加入固定胜率。 |
| `03_wedges.md` | 24A–E、27、29、42、49 | **完整覆盖** | 三推、抛物线楔形和多种职责已覆盖。维持“坏楔形/强趋势例外”，不把 75/25 写成任意 wedge 交易胜率。 |
| `04_double_tops_bottoms.md` | 09B、21D、22–25、27–28、38–39 | **完整覆盖** | 广义双测试、旗形和微型变体已覆盖。头肩/圆弧材料可通过本页与 MTR/TR 解释，无需新增目录。 |
| `05_final_flags.md` | 23A–B、29、40E、43C、48J | **完整覆盖** | 候选、可小至一根、事后确认和晚段语境已经清楚。无需把“final”变成实时确定标签。 |
| `06_triangles_ii_ioi_oo.md` | 08C、18B、26A–B、29E、47 | **完整覆盖** | Triangle 成熟度、压缩形态和统一观察流程已覆盖。保持 triangle 50/50 与普通 TR 80% 不互换。 |
| `07_gaps.md` | 10–11、15E、29A–C、34B、42A–B、48F | **完整覆盖** | Opening/body/micro/measuring/exhaustion 的候选—结果边界已覆盖。继续并列课程进行时用法与事后定义，不强行统一。 |

### 05_setups

| Core 页面 | 课程依据 | 当前覆盖 | 差异与建议 |
| --- | --- | --- | --- |
| `00_what_is_a_setup.md` | 08D、13、21、30、37、49 | **完整覆盖** | Setup 与 Pattern/Trade Plan 边界、仓库分类非穷尽性均已说明。无需修改。 |
| `01_trend_continuation.md` | 09、13–14、17、22C、31、41、43–46 | **完整覆盖** | H2/L2、wedge flag、double test、MA gap bar、premise 和目标差异均已覆盖。无需添加具体订单。 |
| `02_breakout_continuation.md` | 15、18、20、24E、29E、31D、41–42 | **完整覆盖** | 预判/确认版本、接受、第二腿和 measured move 条件完整。保持与 MTR 的双向链接。 |
| `03_trading_range_fade.md` | 15G、18、19、28、37、47、50E | **完整覆盖** | 成熟区间边缘、limit/stop 两类 entry、premise 失效和区间目标完整。第二腿陷阱由上游状态页定义即可。 |
| `04_major_trend_reversal.md` | 21–22、27、29、38–39、40E、42 | **完整覆盖** | 成熟趋势—结构破坏—旧极值测试—HL/LH—反方控制，以及 40/60 风险时点均完整。无需为头肩形单立 Setup。 |

### 06_trade_plan_and_management

| Core 页面 | 课程依据 | 当前覆盖 | 差异与建议 |
| --- | --- | --- | --- |
| `00_trade_plan.md` | 30–36、37、41、51–52 | **需要补连接** | Schema、一致性、active stop、catastrophe backup、动态 premise 已完整。建议把 52A 的三层退出保护映射为：在场硬 stop、预写结构失效、连续强反向动量；并明确“退出后再入”是新版本计划，不是撤销原退出。 |
| `01_scalp_vs_swing.md` | 13B–C、21D、31A–D、36、50A–E、51C–D | **完整覆盖** | 概率/RR、成本、TBTL 和管理不可混用均已清楚。可增加一句：极高胜率说法不是准入标准，也不能补偿无限大尾部损失。 |
| `02_scaling_in_out.md` | 30B、35A–C、36、43C–44C、45D–46D、47C、51D、52A–B | **需要补数学** | 原则正确，但建议加入最小计算框架：加权平均 entry、所有计划数量在共同 stop 下的总风险、交易成本，以及“止损距离倍增则每层仓位反向缩小”的关系。明确计划内加仓不提高市场客观方向概率，只可能改变整仓盈利/保本条件。 |
| `03_risk_psychology.md` | 06–07、30C、33、40A、50B、51A–D、52A–B | **需要补内容** | 仓位、FOMO、连续亏损和分析瘫痪已覆盖。建议增加：正常统计亏损与规则错误分开；错误时快速退出而不自我惩罚；“无关痛痒仓位”用于训练正确执行；希望和等待保本不能替代 premise；不采用遗传决定论和“所有导师无用”的绝对叙事。 |

## 六、完整课程中不应进入 Core 的内容

### 1. 产品和账户机制

03A–E 的外汇报价、pip、保证金、rollover、carry 和换算属于产品 Reference。它们会随产品、账户货币、经纪商和监管变化，不是通用价格行为定义。

### 2. 因果和参与者身份叙事

05 的算法/高频/操纵、29E 的期权对冲占比、34B 的机构算法止盈、51C 的遗传希望叙事，都只能作为可能解释或待核事实。Core 应只保留可观察的价格、跟进、回调、突破和失败。

### 3. 专用指标

50C 的 NYSE TICK 是辅助信息，不属于 Price Action 最低框架。若保留，应进入 Reference 或具体策略背景，并说明数据源、市场和阈值。

### 4. 固定执行参数

48–49 的开盘/尾盘案例可支持时段 Context，但固定分钟窗口、订单寿命、精确目标和记录字段属于 Strategy / Execution。Core 只定义“时段会改变波动、剩余时间和目标可达性”。

### 5. 课程内部冲突

以下内容在核清前只留在材料审计中：

- 30C 的 Z-score 公式与收益解释；
- p2362 的 80%/3R 结论；
- 34B 的十亿交易者连续 100 胜/负算例；
- 43C 的 60%/80%/90% 胜率冲突；
- 51B 无风险回报比的“60% 仍亏损”；
- 用单笔事后 Actual Risk 证明事前正期望。

## 七、Core 调整优先级

### P0：先处理会改变风险理解的内容（已完成）

1. `core/00_method/01_probability_risk_reward.md`
   - 增加 initial / actual / account / personal risk 的边界；
   - 明确 Actual Risk 是事后统计量，不能单笔倒推事前方程。
2. `core/03_acceptance_and_order_logic/00_stop_entry_vs_protective_stop.md`
   - 明确实际保护单与 mental stop 的区别；
   - 补充跳空、滑点和成交价不保证的边界，并链接 Execution。
3. `core/06_trade_plan_and_management/02_scaling_in_out.md`
   - 加入加权均价和完整 scale-in 计划的总风险计算；
   - 明确加仓改善整仓价格不等于提高市场方向概率。
4. `core/06_trade_plan_and_management/00_trade_plan.md`
   - 把三层保护与当前 schema 对齐；
   - 明确退出后的重新入场属于新计划版本。

### P1：补足状态转换和管理连接（已完成）

1. `core/01_market_cycle/02_trading_ranges.md`：加入区间第二腿陷阱与真正接受的分界。
2. `core/01_market_cycle/04_climax_and_transition.md`：加入 Final Trend Bar/失望管理链接。
3. `core/02_context/02_time_and_timeframes.md`：加入入场周期与管理周期一致性、尾盘剩余时间边界。
4. `core/03_acceptance_and_order_logic/01_acceptance_and_failure.md`：加入三层退出保护、强反向动量和退出后再入。
5. `core/06_trade_plan_and_management/03_risk_psychology.md`：补正常亏损/规则错误、客观仓位和等待保本的边界。

### P2：加强交叉链接，避免重复建定义（已完成）

1. `core/03_acceptance_and_order_logic/03_second_entries_and_traps.md` 与交易区间页互链第二腿陷阱。
2. `core/04_patterns/00_patterns_are_language.md` 说明头肩形、圆弧等替代标签不自动建立独立 Definition。
3. `core/04_patterns/01_bar_types.md` 将 Final Trend Bar / Give-up Bar 链接到高潮和接受页面。
4. `core/02_context/01_support_resistance_targets.md` 补 entry-price magnet，但不导入“1–3/20 根必测”的经验数字。

### P3：主体无需重写，第二轮只补边界或来源

- `core/01_market_cycle/00_market_cycle.md`
- `core/01_market_cycle/01_trends_and_channels.md`
- `core/01_market_cycle/03_breakouts_and_breakout_mode.md`
- `core/02_context/00_context_location_control.md`
- `core/03_acceptance_and_order_logic/02_limit_order_market.md`
- `core/04_patterns/02_h1_h2_l1_l2.md` 至 `07_gaps.md` 的主体定义
- `core/05_setups/` 全部五篇正文
- `core/06_trade_plan_and_management/01_scalp_vs_swing.md`

这些页面在第一轮已经表达课程主旨和关键限定，不需要为了“全量调整”而重写。第二轮逐讲复核后，只在其中少数页面补入此前压缩过度的必要边界（例如 market-cycle 的周期绑定、endless pullback、H/L 多周期计数、MTR 压力强度和 TBTL 最高相关周期），并为全部 Core 正文补齐课程讲次追溯；主体职责与目录结构均未改变。

## 八、建议实施顺序

```text
风险词义与数学
    ↓
Stop、Trade Plan 与 Scaling 总风险
    ↓
Acceptance、退出与重新入场
    ↓
Trading Range 第二腿陷阱与 Climax 末端失望
    ↓
Timeframe / Session 管理一致性
    ↓
Risk Psychology 行为边界
    ↓
Pattern 和 Target 的交叉链接
```

每次修改只处理一个权威页面；其他页面保留必要摘要并链接，不复制完整定义。完成一组后，应重新检查：

- 是否改变了原有 Definition 的职责；
- 是否把课程经验数字写成固定统计；
- 是否把 Reference-only 材料带入 Core；
- 是否让 Core 开始生成具体策略或执行参数；
- 是否与 Strategy、Execution 的现有权威位置重复。

## 九、完成审计

| 审计项 | 结果 |
| --- | ---: |
| 课程主编号 | 52 / 52 |
| 实际分讲材料 | 191 / 191 |
| Core 专题目录 | 7 / 7 |
| Core 正文 | 31 / 31 |
| 未分配课程主题 | 0；已分别归入 Core、Reference 或 Strategy/Execution |
| 建议修改范围 | P0 4 项、P1 5 项、P2 4 项均已实施；第二轮补充 6 个课程边界簇并完成 31 / 31 正文的课程讲次追溯 |
| 明确无需主体重写 | 17 篇以上；其余多数仅补边界或交叉链接 |

## 十、实施结果

第一轮按前述 P0–P2 顺序修改了 13 篇 Core 正文。第二轮重新沿 01–52 全课程逐项复核，在不改变七层结构和权威注册表的前提下，当前累计精修 28 篇 Core 正文及入口页：

- 风险与管理：风险四分法、Actual Risk 事后边界、实际 protective stop、滑点边界、scale-in 加权均价和总风险、三层退出保护；
- 状态与 Context：区间第二腿陷阱、Final Trend Bar 的事后角色、管理周期一致性和 session 结束时的时间风险；
- 接受与心理：失望—退出—重新入场链、正常统计亏损与规则错误、无关痛痒仓位、希望和保本边界；
- Pattern 与目标：替代形态不重复建 Definition、趋势末端 K 线角色、entry-price magnet 的非保证边界。
- 第二轮状态精修：明确每个 market-cycle 标签必须绑定周期与观察窗口，补充主要/局部趋势结构、趋势线与通道线动态重画、宽通道深回调，以及 endless pullback 从普通回调到平衡或反向趋势的升级条件；
- 第二轮形态与 Setup 精修：补充 H/L 计数的多周期差异和 MTR 反向压力“强度优先于机械根数”，但不新增形态或 Setup 家族；
- 第二轮管理精修：补充 scalp 的成本侵蚀、TBTL 的最高相关周期，以及盈利加仓与亏损加仓在证据和退出目的上的不同；
- 证据追溯：31 / 31 篇 Core 正文均明确链接 `SRC-COURSE-01-36` 或 `SRC-COURSE-37-52` 的对应讲次；课程综合文档从 Core 入口可达。

`core/05_setups/`、Market Cycle 主定义、通道主定义及主要 Pattern 定义经对齐后保持主体职责不变。课程中的产品知识、专用指标、参与者因果叙事和数学冲突仍留在 Reference，不进入 Core。

Core 已按 P0 → P2 补齐跨章节连接，继续维持“一条权威定义 + 必要摘要 + 交叉链接”的仓库结构。后续若继续调整，应来自新的来源核对或实际发现的职责冲突，而不是再次按课程顺序复制内容。
