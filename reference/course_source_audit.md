# Al Brooks 课程来源与仓库结构审计

> **状态：Evidence Audit / Non-normative**
>
> **审计日期：2026-07-22**
>
> 本报告说明来源覆盖、结构职责、重复治理和冲突处理，不直接许可交易。逐页版权正文、截图和抽取索引不进入仓库。

## 结论

仓库没有建立“最短主线”或选择性首读。`core/` 的七个目录和 31 篇正文共同组成完整理解范围；目录 README、术语表和策略关联只用于导航与复核，不能替代正文。

结构上的主要问题不是目录名普遍错配，而是少数页面把仓库分类写得像 Brooks 固定分类，或让入口摘要与正文职责发生漂移。内容上的主要问题来自四类：同一经验百分比丢失分母、glossary 与课程口径被压成唯一口径、课程翻译/算术/方向错误被误当规则，以及仓库精确执行参数未就近标明属于执行基线。本轮已优先修正会改变方向、风险或定义状态的项目。

## 审计范围与可复核性

### 课程来源

| Source ID | 物理页 | 独立命题 | 覆盖状态 |
| --- | ---: | ---: | --- |
| `SRC-COURSE-01-36` | 2,819 | 1,846 | 2,819/2,819 顺序阅读完成 |
| `SRC-COURSE-37-52` | 1,397 | 860 | 1,397/1,397 顺序阅读完成 |
| **合计** | **4,216** | **2,706** | **20 个连续分块，缺页 0、重复命题 ID 0** |

两份文件的 SHA-256、课程范围和稳定页码口径见[正式来源台账](official_sources.md#本地课程审计口径)。两页译者前言已阅读，但不归因于 Brooks。英文画面是主证据，中文翻译只作辅助；凡涉及 K 线相对位置、箭头、订单线、目标或逐帧变化，必须回看原 PDF 画面，不能只依赖文字抽取。

课程命题的稳定定位采用 `Source ID + 课程号 + 物理 PDF 页码 + 原始 bookmark`。单页、连续页段和非连续页组都进入索引；例如 p984、986 不会被错误扩成包含 p985 的连续范围。

### 仓库范围

初始全仓种子覆盖 81 个 Markdown 文件、3,475 个候选节点，其中 3,389 个需要职责或来源复核：

| 范围 | 文件 | 初始候选节点 | 需要复核 |
| --- | ---: | ---: | ---: |
| `core/` | 39 | 841 | 784 |
| `strategy/` | 33 | 1,836 | 1,815 |
| `execution/` | 4 | 510 | 506 |
| `reference/` | 4 | 261 | 257 |
| 根入口 | 1 | 27 | 27 |

候选节点只是防漏清单，不等于每一行都是 Brooks 主张。执行安全、目录导航、策略互斥、固定窗口和记录字段主要属于仓库综合或执行基线，不应强行要求课程逐句背书。

`strategy/` 的 33 个文件也已全部进入人工逐项复核：trend / breakout / breakout-mode 14/14 文件、655/655 个非导航主张；range / session 9/9 文件、448 个非导航主张归并为 105 个同证据组；reversal 6/6 文件、343/343 个非导航候选；4 个共同编排页另行核对职责、互斥和执行语义。这里的归并只减少统计重复，不删除镜像、状态转换、正反例或复盘问题。

### 证据状态

| 状态 | 含义 |
| --- | --- |
| Direct support | 来源明确给出同一最低定义、条件、事件或概率交换 |
| Context support | 来源支持组成机制，但仓库做了条件化、跨页组合或更窄应用 |
| Repository synthesis | 仓库为消歧、分层、分类或职责分配作的整理 |
| Execution baseline | 为一致执行、风险安全和复盘选择的精确参数或流程 |
| Source conflict | 官方公开来源、课程画面、课程文字或翻译之间存在口径冲突 |
| Unresolved / unsupported | 证据不足以定案，或找不到支持；不能用相似文本自动补证 |

Repository synthesis 和 execution baseline 可以合理，但必须与 Brooks 明示内容分开。来源冲突必须并列保存，不能静默选择一份覆盖另一份。

## 结构审计

| 范围 | 结构结果 | 发现与处理 |
| --- | --- | --- |
| 根目录 | `core / strategy / execution / reference` 四个入口与实际职责匹配 | 根 README 只保留全仓导航，不建立第五套定义 |
| `core/` | 7 个连续编号目录、31 篇正文；完整阅读注册表无缺失或重复 | `00_method` 至 `06_trade_plan_and_management` 的顺序与概念依赖一致；所有正文必读 |
| `core/04_patterns` | 实际为 9 个 Markdown：1 个 README + 8 篇正文 | README 的 `00`–`07` 清单与文件完全匹配；“9 篇正文”会把 README 误算为正文 |
| `core/05_setups` | README + 5 篇正文，职责与编号匹配 | 局部 README 已补“先完成 00–04，再完整读 00–04 五篇”，防止家族表被当选单 |
| `core/06_trade_plan_and_management` | README + 4 篇正文，职责与编号匹配 | 局部 README 已补“先完成 00–05，再完整读 00–03 四篇” |
| Pattern / Setup / Trade Plan | 三层职责清楚，但不是 Brooks 官方固定 taxonomy | 已在 Setup 定义页明确标为 repository synthesis |
| `strategy/` | 23 张正式策略 + 6 个家族 README + 4 个共同编排页，共 33 文件 | 具体形成窗口、单一目标和固定管理属于仓库执行基线；使用前仍须完整理解全部 Core |
| `strategy/reversal` | 实际包含三类逆向修正和同一 MTR 的两个风险时点 | 入口由“趋势反转”改为“逆向修正与主要趋势反转”，不再把普通 correction 误称为原趋势已失控 |
| `strategy/session` | 1 个时段 README + 3 张开盘策略 + 1 张尾盘策略 | 原 `strategy/opening` 与尾盘内容不匹配，已改为 `session`；完整保留四张策略，不建立选读路线 |
| `execution/` | 4 个文件分别负责入口、执行事实链、环境差异和只追加记录 | 安全不变量的重复是有意设计，不归因于 Brooks |
| `reference/` | 入口、派生 glossary、来源 registry、strategy map 与本审计报告五职分离 | Glossary 服从 Core Definition；registry 只保存证据；map 只保存概念去向；审计报告不许可交易 |

编号显示采用“列表序号 1…N + 文件前缀 00…N−1”的常见偏移，但物理顺序完全一致，不构成漏项。为了完整理解，不把这些清单改成推荐、可选或最短路线。

## 具体重复位置与处理判断

| 位置 | 重复思想 | 判断 | 处理 |
| --- | --- | --- | --- |
| `README.md`“四个目录各自负责什么” ↔ 各目录 README | 顶层职责 | 合理的全局导航 → 局部入口 | 根页保留一句摘要，细节归目录 README |
| `core/README.md`“核心关系/Definition 注册表” ↔ 各 Definition 页 | 概念关系与权威归属 | 合理的注册表 → 完整定义 | 注册表不复制条件与例外 |
| `core/01_market_cycle/00_market_cycle.md`“基础层级” ↔ “读循环的问题” | trend/TR 与 breakout/channel | 合理的定义 → 检查表 | 保留；两处功能不同 |
| `core/02_context/00_context_location_control.md` ↔ `core/03_acceptance_and_order_logic/01_acceptance_and_failure.md` | follow-through、快速收回、反方失败 | 合理职责交叉 | 前者记录背景累积，后者定义触发后证据，互链但不合并 |
| `core/04_patterns/03_wedges.md`“三种常见含义” ↔ “Parabolic Wedge 怎么读” | 紧通道、三 surge、高潮 | 原文重复 | 已把最低定义保留一次，后段只留整体紧迫性与控制限定 |
| `core/04_patterns/04_double_tops_bottoms.md` 原 Double Top Bear Flag ↔ Double Bottom Bull Flag | 同一延续逻辑的多空镜像 | 含义必须双向保留，文字可参数化 | 已合并为双向表，完整保留两方向 |
| `core/04_patterns/05_final_flags.md`“定义” ↔ “交易含义” | candidate、失败证据、事后确认 | 原文重复且状态容易漂移 | 已建立三状态表，应用段只引用状态 |
| `core/04_patterns/06_triangles_ii_ioi_oo.md` Triangle/ii/误读段 | 不预猜方向、看突破与跟进、首次突破可失败 | 多次近义重复 | 已集中为 `状态 → 突破 → follow-through → 回踩/重入` 流程 |
| `core/04_patterns/07_gaps.md`术语表 ↔ 实时命名规则 ↔ 常见误读 | measuring/exhaustion 不能事前确认 | 部分合理，误读段过度复述 | 术语表保留结果边界，误读合并为一条候选/结果规则 |
| `core/05_setups` 四个应用页的 Premise/Stop/结果/误读 | 同一页面模板 | 合理设计 | 保留完整模板、阶段和镜像，便于逐字段比较 |
| `core/05_setups/02_breakout_continuation.md` ↔ `04_major_trend_reversal.md` | 强反向 breakout + FT 后同一交易可有两个标签 | 非互斥职责，不是应删重复 | MTR 解释旧趋势失控；breakout continuation 解释新方向接受，已双向链接 |
| `core/05_setups/01_trend_continuation.md` MAG 段 ↔ MTR | 均线测试先延续旧趋势、后可能成为 MTR 背景 | 时间顺序互补 | 保留两阶段，不把首次测试提前称完整 MTR |
| 四个 Setup stop 段 ↔ `core/06_trade_plan_and_management/00_trade_plan.md` | 结构 stop、远则缩仓、目标与方程同版本 | 通用规则重复过多 | Trade Plan 单源定义；Setup 只保留自己的 premise 失效结构 |
| `strategy/reversal` 五页的严格 second signal、两根订单寿命、固定管理 | 同一仓库算法近乎逐字重复 | 参数锚点各异，通用理由应单源 | Common rules 拥有计数/固定管理语义；各页保留特有 entry、stop、target、镜像和边界例 |
| `strategy/trend` 六张策略的“只等止损或目标” | 单目标、全量退出和不主动 trailing 大量重复 | 可重复显示参数，但绝对语气会掩盖 Brooks 的动态 premise 管理 | 家族 README 与 common rules 单源说明两层管理；详情页保留特有 stop/target，并就近链接 premise-change 分支 |
| `strategy/README.md`、`strategy/session/README.md` 覆盖摘要 ↔ `strategy/how_to_choose.md`“时段策略怎样覆盖普通策略” | 候选起点、同底层机会、过期、重启和不可复用旧信号 | 权威算法应单源维护；入口仍须保留防止绕过时段限制的安全摘要 | `how_to_choose.md` 是完整权威定义；两个入口只保留摘要与链接，若有差异以权威页为准 |
| `strategy/range` 三页的中点公式 | 同一算术、取整和冻结规则 | 目标价格必须在各计划可见，概念理由不应维护三份 | 家族 README 单源定义并注明仓库基线；详情页只实例化本方向价格 |
| `strategy/range` 三页的主动退出阈值 | 一根外收盘、连续两根更外、强外收盘加跟进 | 看似矛盾，实际来自三种不同 entry premise | 已在家族 README 增加对照矩阵，保留三套阈值而不强行统一 |
| 时段页反复出现 30/60/90 分钟、根数和订单寿命 | 同一参数在适用、形成、放弃、例子和复盘中重现 | 状态边界必须完整可见，来源理由只应说明一次 | 家族与详情页就近标为仓库执行基线；后续宜由结构化字段生成，保留边界例 |
| `execution/` 多次“请求不等于成交” | 提交、撤单、改单、退出时都重申 | 安全关键不变量，合理重复 | 保留在每个会产生局部误读的阶段 |
| Core Definition ↔ `reference/glossary.md` | 同一术语 | 合理权威定义 → 派生速查 | Glossary 必须短、链接并在 Core 改动时同步差分 |

重复治理原则是“一条 canonical rule + 完整条件、状态转换、镜像、例子和交叉链接”。多空镜像、确认前后、逐帧概率更新和不同风险承担时点不因文字相似而删除。

## 仓库中发现的矛盾或归因风险

| 位置 | 原问题 | 来源判定 | 处理 |
| --- | --- | --- | --- |
| `core/00_method/01_probability_risk_reward.md` | 容易把课程“2R 总为正”照抄成数学结论 | 二结果且不计成本时仍须 `p > 1/3` | 明确公式条件，课程绝对句只登记为 source conflict |
| `core/01_market_cycle` 多页 | 75%、80%、70%、50/50 容易合并为同一概率 | 分别属于通道演化、普通区间单次突破、紧通道首次反转和 BOM | 所有数字补状态、事件和分母，不相互外推 |
| `core/01_market_cycle/03_breakouts_and_breakout_mode.md` | “获接受的突破”外观像官方固定词条 | 是仓库综合 breakout + FT + 持续方向控制的状态标签 | 明确 repository synthesis；官方引用仍用原词 |
| `core/01_market_cycle/04_climax_and_transition.md` | glossary 事后定义与课程进行时用法被当成二选一 | 两套用法并存 | 区分 climactic behavior / candidate 与 hindsight result |
| `core/04_patterns/01_bar_types.md` Trend Bar | 原文把任何 `open != close` 都定义为 trend bar | 课程使用相对实体、影线、收盘与 Context 的连续谱 | 已重写 |
| 同页 Signal/Entry Bar | 原文绝对限定为前一根/后一根 | Close entry 时同一根可兼任 | 已补例外 |
| 同页 Outside/Reversal Bar | 只采用 glossary 简化口径 | 课程 outside 使用双端 `at or`；操作性 reversal bar 可有反色实体 | 并列登记 source disagreement |
| `core/04_patterns/03_wedges.md` | “少数第五推”无已核稳定锚点 | 课程明确支持三推和偶见第四推 | 删除第五推规则，保留待来源化边界 |
| `core/04_patterns/05_final_flags.md` | 候选被限于成熟趋势晚段 | 课程说明任意趋势腿、包括区间内小腿，flag 可小至一根 | 已重写最低边界；晚段只作增强语境 |
| `core/04_patterns/07_gaps.md` | Opening 和 exhaustion 各被压成单一口径 | 课程使用多组 session 边界；课程 exhaustion 可只停止压力并横盘 | 明列参照边界与来源差异 |
| `core/05_setups/03_trading_range_fade.md` | “单根强 K 线不够”写成绝对句 | 足够强的反向 breakout 本身可要求退出，FT 再强化 | 改为区分轻微越界、普通外观和异常强突破 |
| `core/06_trade_plan_and_management/00_trade_plan.md` | protective stop、price-action stop、catastrophe stop 角色混用 | 来源允许多个合理 stop，但实际计划必须知道哪张订单在场 | 拆为 active protective stop 与独立 catastrophe backup |
| 同页 target | 原值冻结被误读为禁止动态管理 | 课程允许随 premise 更新目标与退出 | 拆为不可回填的 `original_target` 与留痕的 current target / actual exit |
| `core/06_trade_plan_and_management/03_risk_psychology.md` | 五项心理清单、追错比较和固定解法外观像 Brooks 原表 | 只有仓位/FOMO机制有直接或语境支持 | 明确为 repository psychology synthesis / execution baseline |
| `strategy/reversal/final_flag_reversal.md` | 入场前把 failed breakout + 反向信号称为 confirmed final flag | 这只形成 result evidence；final 身份只能事后确认 | 入口、正文、镜像、正例和复盘已同步修正 |
| `strategy/reversal/parabolic_climax_correction.md` | 把 micro trendline break 写成确认 climax 的必要条件 | 它只是一张策略的激活条件 | 改为“本策略尚未激活”，保留 climax 双口径 |
| 两张 MTR 策略 | 课程 40/60、FT、MM 容易被误当精确策略绩效和公式 | 课程支持风险时点；next-bar FT、two-bar MM 与固定管理是仓库基线 | 就近标明 course context，不声称策略回测胜率 |
| `strategy/trend/first_small_pullback.md` | 原误读段把第 4 根排除出 small pullback 概念 | 课程 14E 明确可为 1–4 根；本页只交易 1–3 根 | 改为“第 4 根只是本策略过期，不否定概念” |
| `core/04_patterns/06_triangles_ii_ioi_oo.md`、`strategy/breakout_mode` | 严格 ii 被写成无条件方向中立，甚至排除更高周期偏置 | 成熟 triangle 可近 50/50；未成熟 ii / 紧压缩仍可保留趋势先验 | Core、glossary 与策略页均补 Context / 成熟度门，任一侧 TE 不利则整组放弃 |
| `strategy/breakout/breakout_follow_through.md` | 紧接一根、更外收盘和自身半区容易被当成通用 FT 定义 | 通用 follow-through 可由一根或多根构成，不统一要求该比较 | 标题与开头明确为“紧接一根”的仓库严格子型 |
| `strategy/breakout/failed_failure_continuation.md` | “三根内收回”被写得像已确认 glossary failure | Glossary failure 取决于 stop 与 scalp / 原目标的结果顺序 | 改名为收盘突破被拒绝后再次接受；收回只作拒绝代理，与 failed-failure 机制关联但不重定义 failure |
| `strategy/session/opening_range_breakout.md` | Opening range 被直接等同于固定前三十分钟 | 课程区分 opening swing、opening range、BOM 与 first-18-bar breakout | 标题和定位改为“固定前三十分钟范围”；30/90 分钟均标仓库时钟基线 |
| 三张 session 页的“无视觉提前退出” | 机械 stop/target 被写成 Brooks 完整管理 | 课程明确 premise / Always In 改变时可在结构止损前退出 | 标准策略保留 premise-change；只隔离 stop / target 的回放另建 `mechanical_only` 独立研究变体，不与标准结果比较 |
| `strategy/session/late_session_open_magnet.md` | 把 reduce-only / close-only 竞态安全写成跨平台保证 | 取决于 broker、adapter、订单类型、部分成交和重试语义 | 改为 capability contract + 竞态测试的启用门；未验证时 fail closed |

## 课程源文件自身的错误与冲突实例

这些问题记录在来源层，不直接改写用户持有的 PDF，也不把错误页当作独立佐证。仓库规则优先依据英文画面、图中关系、相邻页、Trader's Equation 和公开官方来源交叉判断。

| Source / 位置 | 问题 | 审计处理 |
| --- | --- | --- |
| `SRC-COURSE-01-36` p692、p1462、p1492 | 中文把买卖或 HL 方向写反 | 以英文与图形为主，登记翻译错误 |
| 同源 p1549、p1552–1553 | 标题 `LCM`，目录与正文实际是 LOM | 仓库只保留 Limit Order Market，不建立 LCM 概念 |
| 同源 p1580、p1583 | Measured Move 被译成“均值” | 隔离 MM 与 mean reversion |
| 同源 p1685、p1690、p1695–1696、p1715 | 平仓/开空、limit/stop 订单角色错译 | 强制记录 open/close + long/short + order type |
| 同源 p2003、p2026、p2088、p2167 | undershoot、HL/LH、cover short 等方向错误 | 以相邻英文页和图形校正语义，不把错句提升为规则 |
| 同源 p2090 | 标题写 micro 2–4 bars，正文写 2–5 | 保留 source conflict，不静默选一边 |
| 同源 p2346–2351、p2362、p2396–2397 | runs/Z-score 与 Trader's Equation 算术或阈值错误 | 与交易数学隔离，禁止进入仓位或概率规则 |
| 同源 p2470、p2473 | 标题称 60% 胜率后亏损，正文给定算术却分别为 +$10、+$40 | 不能用标题覆盖算术；只保留“优势很薄、对成本敏感” |
| 同源 p2514–2521、p2516 | Bracket 被系统译成“一篮子订单”；多单英文把先成交写成 sell | Bracket/OCO 统一词典；p2516 以图和订单逻辑判为 buy |
| 同源 p2568、p2625、p2636 | TR、LH、buy 分别被译成趋势区域、HH、做空 | 方向级错误，禁止进入规则或题库 |
| 同源 p2780–2781 | 卖出例的英文复制残留写成 buy | 以整页卖出结构和数字为主，登记源文错误 |
| `SRC-COURSE-37-52` p261、p414 | 目标/买方方向被中文写反 | 以英文和图形为主 |
| 同源 p725、p727 | LH 被译为 HH | 修正结构层级，不让趋势失效点反向 |
| 同源 p838–839 | TTR 被译为“真实交易区间” | 统一为 tight trading range，避免外推到全部区间 |

此外，课程中的产品点数、tick/pip、HFT 成本、经纪商故障频率、历史事件和无样本百分比具有市场、年代或事实核验要求。它们可以作为当时教学例，不自动进入跨市场规范。

## 可执行优先级

### P0：阻断会改变方向、数学或风险角色的污染

1. 修正仓库中的方向级定义、final-flag 状态、单根强突破退出和 stop 角色混用。
2. 隔离课程的算术错误、buy/sell、HL/LH、MM/mean、LOM/LCM、Bracket 与 stop/limit 误译。
3. 所有经验百分比必须同时保存状态、事件、分母、观察时点、时间窗、市场/周期和成功定义。

本轮上述仓库 P0 已完成；源文件本身不改动，冲突保留在证据层。

### P1：把来源层级放到规则附近

1. **已完成**：对 Pattern–Setup–Trade Plan、六个策略家族、固定窗口、唯一目标、订单寿命和固定管理就近标明 `repository synthesis / execution baseline`。
2. **已完成**：对 glossary 与课程的 outside bar、reversal bar、climax、opening gap、exhaustion gap，以及 strict H/L 计数分歧并列登记。
3. **已完成**：small pullback、ii / triangle、opening / late-session、MTR 40/60、2R 等高风险数字均补稳定课程 locator；课程时点概率不再冒充仓库精确策略的回测胜率。
4. **已完成**：固定订单基线与 Brooks premise-change 标准管理分层；`mechanical_only` 已隔离为不可与标准环境比较的独立研究变体，记录模板增加管理口径；依赖 reduce-only / close-only 的尾盘策略增加 broker / adapter capability contract，未验证时 fail closed。

### P2：单源维护通用规则，不删完整思想链

1. **已完成**：Trade Plan 单源维护 active stop、catastrophe backup、仓位后果与 target 审计字段。
2. **已完成**：Strategy common rules 单源维护计数、订单寿命、固定管理理由和 premise-change；各页只实例化特有 entry、stop、target、阶段、镜像和边界例。
3. **已完成**：时段覆盖状态机的权威完整定义集中于 `how_to_choose.md`，根入口与 session 入口只保留安全摘要和链接；range README 集中中点与三种主动失效阈值；派生 glossary 与 strategy map 已随 Core Definition 做差分同步。
4. **后续维护**：重复参数可继续迁移到结构化字段或模板生成，但不能以删除镜像、状态转换、正反例和复盘问题换取表面精简。

### P3：把审计变成持续验证

1. 在保有本地审计环境的维护工作中，验证 Core 7 目录、31 正文与完整阅读注册表一一对应。
2. 在同一审计环境验证全部本地 Markdown 文件链接、章节锚点和 Source ID 均存在。
3. 重建课程 claim index 时检查 20 个分块、命题 ID、页码范围和非连续页组，保持缺失 0、重复 0；逐页版权索引与当前校验脚本未提交，普通 clone 不能仅凭仓库复现这一步。
4. 策略关键字段逐步增加 `source_claims / evidence_class / repo_baseline / overrides_common_rule`，用于防止来源与人工参数再次混写。

## 当前验证结果

- Core：7 个目录、31 篇正文；阅读注册缺失 0、重复 0。
- 课程：20 个连续分块、4,216 页、2,706 条命题；命题缺失 0、重复 0。
- Source ID：已使用的 21 个 ID 全部在来源台账注册。
- 最终仓库索引：82 个 Markdown、3,671 个候选节点，其中 3,583 个进入来源或职责复核队列；策略 33/33 文件均在索引内。
- 本地链接：82 个 Markdown、625 个本地文件/章节链接；缺失文件 0、缺失锚点 0。
- Markdown diff：无尾随空格或空白错误。

这些数字是本地审计环境在本次修改上的快照，不表示普通 clone 自带完整复现工具。后续新增正文或链接时，应在保有课程索引与校验脚本的审计环境重跑，不能把它们当永久常量。
