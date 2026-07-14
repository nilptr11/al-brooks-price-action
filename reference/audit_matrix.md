# 主题与执行规则审计矩阵

> **状态：Evidence Audit / Non-normative**
>
> 本文件记录证据、性质和核对状态，不定义价格行为或交易动作。

本文件只在维护、来源核对或处理概念冲突时使用，不属于学习路径或训练任务。

## 状态定义

- **已核对**：核心结论已找到直接来源锚点，并检查了当前文档表达。
- **部分核对**：已有来源依据，但仍存在范围、版本或文字冲突。
- **待核对**：当前结论尚无足够来源锚点，不得写成稳定 Brooks 规则。
- **仓库操作规范**：只涉及配置、记录、平台订单、成交保护、成本或训练组织，不定义 setup、stop、target、概率或交易准入。
- **内部治理**：只涉及仓库结构、文档职责和维护边界。

## 当前矩阵

| 主题或规则 | 主要所有者 / 使用位置 | 派生或关联文档 | Source ID | 性质 | 状态与边界 |
| --- | --- | --- | --- | --- | --- |
| 文档结构、状态与依赖 | `DOCUMENTATION_GOVERNANCE.md` | 根 `README.md`、各目录 `README.md` | — | 内部治理 | 内部治理；仓库权威不能覆盖来源中的价格行为定义 |
| 批次配置、计划快照、订单状态、成交保护和事件日志 | `EXECUTION_MANUAL.md`“仓库订单与记录操作” | `EXECUTION_RECORD_TEMPLATE.md`、`training/` | — | 仓库操作规范 | 仓库操作规范；只保证记录可复核、订单状态清楚和持仓受到保护，不增加交易条件 |
| 账户、单笔、时段与相关敞口边界 | `EXECUTION_MANUAL.md`“使用边界” | `EXECUTION_RECORD_TEMPLATE.md` | — | 用户风险配置 + 仓库范围声明 | 仓库不提供具体数值；未设定用户风险边界时只用于学习、回放和模拟 |
| 价格行为交易主线 | `learning/00_method/00_al_brooks_thesis.md`；`learning/05_setups/00_what_is_a_setup.md`；`learning/06_trade_management/00_trade_plan.md` | `EXECUTION_MANUAL.md`、`LEARNING_PATH.md`、训练材料 | `SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE`、`SRC-10-PATTERNS`、`SRC-GOOD-TRADE-2017` | Brooks 方法汇总 | 已核对；market cycle、context、setup、stop、target、Trader's Equation 与 premise 管理在学习目录内构成闭环；执行手册只做融会贯通的派生汇总，不另建内部阶段码或固定五问规则 |
| Market cycle 与结构连续谱 | `reference/glossary.md`；`learning/01_market_cycle/` | `EXECUTION_MANUAL.md` | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STRONG-LEGS-2016` | 定义 + 视觉经验倾向 | 已核对；先分 trend / trading range，trend 再观察 breakout / channel；根数与回调深度是典型线索，不是机械阈值 |
| Context、buying/selling pressure、Always In 与位置 | `reference/glossary.md`；`learning/02_context/00_context_location_control.md` | 执行手册、训练 | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016` | Brooks 概念与普通读图语言 | 已核对；context 比孤立 candle pattern 重要，pressure 必须落回可观察价格行为；control/location 不作为独立交易系统 |
| Pattern、setup、signal bar 与 entry bar | `reference/glossary.md`；`learning/04_patterns/00_patterns_are_language.md`；`learning/05_setups/00_what_is_a_setup.md` | 执行手册 | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-SCALE-IN-TRENDS` | 最低定义 + 交易关系 | 已核对；setup 是带 context、可作为入场依据的 pattern；实际 entry 后最后一根才取得 signal-bar 角色；完整交易还需 stop、target 和管理，但这些不反向扩充 setup 定义 |
| Follow-through、disappointment、failure、success 与 trapped in a trade | `reference/glossary.md`；`learning/03_order_flow/00_acceptance_and_failure.md` | setup 与复盘文档 | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-GOOD-TRADE-2017` | 定义与结果边界 | 已核对；entry disappointment、premise 变化和 failure 是不同事情，不再使用仓库自造的 weak/tentative/confirmed 等级 |
| Breakout 最低事件、质量和 breakout mode | `reference/glossary.md`；`learning/01_market_cycle/03_breakouts_and_breakout_mode.md` | setup、opening 训练 | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STRONG-LEGS-2016`、`SRC-ABBREVIATIONS` | 定义 + 质量证据 | 已核对；最低越界事件与可交易 breakout pattern 分开，回踩不是成功突破的必要步骤，breakout mode 不预设方向 |
| Trading range、BLSHS、宽/紧区间 | `learning/01_market_cycle/02_trading_ranges.md`；`learning/05_setups/03_trading_range_fade.md` | 执行手册 | `SRC-MANUAL`、`SRC-TRADING-RANGES`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016` | 定义 + 管理原则 | 已核对；区间中部通常回避，宽区间可使用 stop 或 limit 方案，紧区间多数初学者等待；没有统一 midpoint target 或统一边界 stop |
| Trader's Equation 与 40–60 | `reference/glossary.md`；`learning/00_method/01_probability_risk_reward.md` | 执行手册、trade management | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-BREAKOUTS-2025` | 公式与经验倾向 | 已核对；核心比较概率×回报与失败概率×风险；40–60 与约 2R 是典型启发，不是固定胜率或机械 target；成本只在仓库记录中另算净结果 |
| Scalp、swing 与初学者学习顺序 | `reference/glossary.md`；`learning/06_trade_management/01_scalp_vs_swing.md`；执行手册“初学者学习范围” | 章节 README | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-RISK-113` | 定义 + 学习建议 | 已核对；stop-entry swing 是初学者基础，limit、close、scale-in、scalp 和 reversal 仍属于 Brooks 方法，不写成禁用交易 |
| Stop entry、protective stop 与 price-action stop | `learning/03_order_flow/01_stop_entry_vs_protective_stop.md`；`learning/06_trade_management/00_trade_plan.md` | 执行手册、记录模板 | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-TREND-CHANNELS`、`SRC-RISK-113`、`SRC-GOOD-TRADE-2017`、`SRC-PATTERNS-OPEN-2018` | 定义 + stop 管理 | 已核对；同图可能有 signal/pattern、swing 或 catastrophe stop；premise 改变可在最远 stop 前退出；平台触发价和预计 fill 只是仓库订单字段 |
| Position size、stop 距离与行为承受能力 | `learning/06_trade_management/03_risk_psychology.md`；执行手册 | 记录模板、复盘 | `SRC-POSITION-SIZE`、`SRC-RISK-113`、`SRC-SCALE-IN-TRENDS` | 仓位原则 | 已核对；price-action stop 越远，仓位应越小，并应小到能够客观管理；账户结果视图与日志频率属于仓库操作 |
| Support/resistance、profit target、measured move 与 magnet | `learning/02_context/01_support_resistance_targets.md`；各 setup 页 | 执行手册、trade plan | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-BREAKOUTS-2025`、`SRC-LIVE-TR-BO-2021` | 目标定义与 setup 依据 | 已核对；target 由 setup、scalp/swing、support/resistance 和 Trader's Equation 决定；measured move 是 magnet 而非保证；不再使用统一“第一现实目标/延伸目标”分类 |
| 成交后 premise、early exit、stop 调整与 scale-in | `learning/03_order_flow/00_acceptance_and_failure.md`；`learning/06_trade_management/00_trade_plan.md`；`learning/06_trade_management/02_scaling_in_out.md` | 执行手册、记录模板、训练复盘 | `SRC-GOOD-TRADE-2017`、`SRC-MAKE-MONEY-2016`、`SRC-HOLDING-WIDE-STOPS`、`SRC-SCALE-IN-TRENDS`、`SRC-POSITION-SIZE` | 交易管理 + 仓库记录 | 已核对；premise 失效应退出，wide stop 可作为 catastrophe stop；planned scale-in 必须按总风险设计；执行手册只汇总管理逻辑，事件保存方式才属于仓库操作 |
| Setup families 与各自 stop/target | `learning/05_setups/` | 执行手册“交易计划中的一致关系” | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-10-PATTERNS`、`SRC-TREND-CHANNELS`、`SRC-TRADING-RANGES`、`SRC-STRONG-LEGS-2016`、`SRC-BREAKOUTS-2025`、`SRC-MTR-2025` | 非穷尽的 setup 对照 | 已核对；趋势 flag、breakout、range trade、MTR 和 second entry 只是本章选取的主题，不构成仓库四分法或统一准入 |
| Major Trend Reversal | `reference/glossary.md`；`learning/05_setups/04_major_trend_reversal.md` | climax、setup、management | `SRC-GLOSSARY`、`SRC-MTR-2025`、`SRC-10-PATTERNS`、`SRC-PATTERNS-OPEN-2018` | 定义 + 经验概率倾向 | 已核对；完整结构含通道突破和旧极值测试；约 40%/60% 是典型交换；约 2R 是常见 swing 关系，不是 MTR 定义或仓库硬门槛 |
| Gap、Body Gap、measuring gap 与 exhaustion | `reference/glossary.md`；`learning/04_patterns/07_gaps.md` | context、setup、opening | `SRC-GLOSSARY`、`SRC-STRONG-LEGS-2016`、`SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` | 定义 + 案例 | 已核对；Body Gap 不要求参照 K 线相邻；gap 只在实际提供强度、support/resistance、接受/拒绝或量度信息时参与判断 |
| Wedge 与 Parabolic Wedge | `reference/glossary.md`；`learning/04_patterns/03_wedges.md` | MTR、climax | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-PATTERNS-OPEN-2018` | 最低结构 + 经验路径 | 已核对；parabolic wedge 是 tight channel 中至少三腿的 climactic wedge，不要求逐腿更陡；首次反向运动常仍只是 minor reversal |
| TBTL | `reference/glossary.md`；`learning/06_trade_management/01_scalp_vs_swing.md` | MTR、final flag | `SRC-ABBREVIATIONS`、`SRC-10-PATTERNS`、`SRC-MTR-2025` | 术语 + 经验预期 | 已核对；Ten Bars, Two Legs correction 是常见反转 swing 路径，不是固定价格 target 或所有 correction 的硬条件 |
| Inside/outside/reversal bar 与 OO | `reference/glossary.md`；`learning/04_patterns/01_bar_types.md`、`06_triangles_ii_ioi_oo.md` | — | `SRC-GLOSSARY` | 最低定义 | 已核对；outside bar 允许一侧相等、另一侧严格越界；reversal bar 的经典影线外观不是最低条件；OO 要求第二根更大 |
| H/L 计数、second entry 与 second signal | `reference/glossary.md`；`learning/04_patterns/02_h1_h2_l1_l2.md`、`learning/05_setups/05_second_entries_and_traps.md` | — | `SRC-GLOSSARY`、`SRC-10-PATTERNS` | 来源存在文字差异 | 部分核对；Brooks glossary 使用严格 `above` / `below`，形态文章使用 `at or above` / `at or below`；术语表和正文明确保留这一差异，不将相等高低点写成无争议规则 |
| Micro double top / bottom | `reference/glossary.md`；`learning/04_patterns/04_double_tops_bottoms.md` | — | `SRC-GLOSSARY` | 最低定义 | 已核对；micro double 既可承担 one-bar flag，也可在相反 flag 末端成为 reversal setup，不天然等于反转 |
| Triangle | `reference/glossary.md`；`learning/04_patterns/06_triangles_ii_ioi_oo.md` | — | `SRC-ABBREVIATIONS` | 最低结构 + 概率倾向 | 已核对；至少五次反转；约 50/50 方向和首破失败只属于 triangle 语境，不能外推到所有 breakout mode |
| Opening、day type、周期与时段 | `learning/02_context/02_time_and_timeframes.md`；`training/00_day_types.md`、`01_opening_range_and_opening_reversal.md` | 执行配置 | `SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` | 案例 + 需市场数据验证 | 部分核对；opening price action 有直接案例，跨市场 session 与 day-type 倾向仍需目标品种样本校准，不写成固定定律 |

## 已移除的内部交易标签

以下内容曾用于组织仓库，但没有直接 Brooks 定义，现已从学习与交易规则中移除：

- “趋势恢复 / 突破接受 / 回归公平 / 控制权反转”四分法。
- “第一现实目标 / 条件式延伸目标”统一 target 分类。
- `weak / tentative / confirmed failure` 三层结果等级和 `strict failure` 标签。
- `climactic behavior` 作为独立正式状态。
- 由固定五问、字段完整度或仓库分类产生的独立 setup 准入。

书面计划快照、配置版本、订单状态、保护覆盖、费用、日志和复盘输出仍保留，但只属于仓库操作规范。
