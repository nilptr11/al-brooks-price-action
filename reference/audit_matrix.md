# 主题与执行规则审计矩阵

> **状态：Evidence Audit / Non-normative**
>
> 本文件记录证据、性质和审计状态，不替代当前[执行手册](../EXECUTION_MANUAL.md)的执行文本。

本文件仅在维护、来源核对或处理概念冲突时使用，不属于学习路径或训练任务。

## 状态定义

- **已核对**：核心结论已找到直接官方锚点，并检查了当前文档表达。
- **部分核对**：已有官方依据，但仍有未核对的细节、范围或冲突。
- **待核对**：当前主要来自内部文档或经验归并，尚无足够官方锚点。
- **内部执行政策**：仓库为保证一致执行而制定，不宣称是 Al Brooks 官方规则。
- **内部治理**：仓库结构、文档职责或维护边界，不属于 Al Brooks 结论或交易动作。

## 当前矩阵

| 主题或规则 | 执行手册位置 | 派生/关联文档 | Source ID | 性质 | 状态与下一步 |
| --- | --- | --- | --- | --- | --- |
| 文档权威与学习优先结构 | “使用边界”、README“权威层级” | `DOCUMENTATION_GOVERNANCE.md`、`LEARNING_PATH.md`、各目录 `README.md` | — | 内部治理 | 内部治理；学习、执行、训练、查阅、来源和审计已有唯一所有者，形态库与高级执行均不属于默认学习主线 |
| 自然语言核心流程与高级附录边界 | “核心五问”、“高级执行附录” | `training/README.md`、`training/02_bar_by_bar_templates.md`、`training/03_review_checklist.md` | — | 内部执行政策 | 内部执行政策；核心只保留市场与位置、交易想法、入场与失效、数学与仓位、成交后管理；复杂订单仅在实际相关时进入同文件附录 |
| 账户、单笔与时段风险范围 | “使用边界”、“一份核心交易计划” | `README.md` | — | 范围声明 | 内部治理；仓库不提供具体风险数值，但真实交易前必须另行设定账户、单笔、时段和相关敞口边界；未设定时只用于模拟与复盘 |
| Market cycle 与结构连续谱 | “市场状态与四种交易想法” | `learning/01_market_cycle/` | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STRONG-LEGS-2016` | 官方概念 | 已核对；先分 trend / trading range，trend 再分 breakout / channel；breakout、tight channel、broad channel、trading range 构成连续谱 |
| Context、位置、控制权与 Always In | “核心五问”、“市场状态与四种交易想法” | `learning/02_context/00_context_location_control.md` | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016` | 官方概念 + 学习归并 | 已核对；context 重于单根 pattern，控制方向来自累积买卖压力和失败行为；Always In 不替代位置、目标或 Trader's Equation |
| Pattern、setup、signal bar 与 entry bar | “Setup、入场和可观察证据” | `learning/04_patterns/00_patterns_are_language.md`、`learning/05_setups/00_what_is_a_setup.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS` | 官方最低定义 + 教学边界 | 已核对；setup 由 context 和入场依据组成，实际 fill 后最后一根才取得 signal-bar 角色；pattern 不自动许可交易 |
| Follow-through、失望、failure 与 trapped traders | “Setup、入场和可观察证据”、“成交后的管理” | `learning/03_order_flow/00_acceptance_and_failure.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-GOOD-TRADE-2017` | 官方结果边界 + 描述性教学语言 | 已核对；弱跟进不等于 confirmed failure 或已被困；confirmed failure 要求原目标或至少 scalper's profit 未先实现而 protective stop 先触发；trapped trader 还要求已经入场、处于开放亏损，并很可能被迫或已经实际退出。premise 失效后的提前亏损退出另记为内部操作性结果，不冒充 glossary 的严格 failure 名称 |
| Breakout 最低定义、接受与 breakout mode | “市场状态与四种交易想法” | `learning/01_market_cycle/02_trading_ranges.md`、`learning/01_market_cycle/03_breakouts_and_breakout_mode.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STRONG-LEGS-2016`、`SRC-ABBREVIATIONS` | 官方概念 | 已核对；越过重要旧价位是最低事件，强收盘和 follow-through 增加接受证据；若发生回踩，守住是额外证据而非必要步骤；breakout mode 不预设方向 |
| Trading range、BLSHS 与紧区间回避 | “学习者默认范围”、“四种交易想法” | `learning/01_market_cycle/02_trading_ranges.md`、`learning/05_setups/03_trading_range_fade.md` | `SRC-TRADING-RANGES`、`SRC-STOP-ORDERS` | 官方原则 + 保守范围 | 已核对；区间中部回避，宽区间边缘可出现 stop 或高级 limit 方案，紧区间多数学习者等待 |
| Trader's Equation 与 40–60 思维 | “Trader's Equation” | `learning/00_method/01_probability_risk_reward.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-STOP-ORDERS`、`SRC-BREAKOUTS-2025` | 官方原则 + 保守执行估算 | 已核对；概率、entry、stop、target 和管理必须属于同一方案；不确定时以约 40–50% 和至少约两倍风险回报作启发，不写伪精确概率树 |
| Scalp、swing 与学习者默认范围 | “学习者默认范围” | `learning/06_trade_management/01_scalp_vs_swing.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-RISK-113` | 官方原则 + 学习范围 | 已核对；多数学习者优先小仓位、stop entry 与 swing；小目标若小于风险需要多数人难以达到的高胜率 |
| Entry、premise 失效与 protective stop | “Protective stop、目标和仓位” | `learning/03_order_flow/01_stop_entry_vs_protective_stop.md`、`learning/06_trade_management/00_trade_plan.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-RISK-113`、`SRC-GOOD-TRADE-2017` | 官方依据 + 执行政策 | 已核对；失效事实、结构锚点、经纪商 trigger 和保守 stop fill 分开；同图多个合理 stop 必须作为不同方案，成交后不得向风险方向放宽 |
| Position size 与最坏计划结果 | “Protective stop、目标和仓位”、“高级执行附录” | `learning/06_trade_management/02_scaling_in_out.md`、`learning/06_trade_management/03_risk_psychology.md` | `SRC-POSITION-SIZE`、`SRC-RISK-113`、`SRC-TRADING-RANGES`、`SRC-BREAKOUTS-2025` | 官方原则 + 内部核算 | 已核对；仓位服从合理 stop 距离和行为承受上限；部分成交或预设加仓时使用真实 fill、真实数量和全部活动风险检查最坏结果 |
| Target、support/resistance 与 measured move | “Protective stop、目标和仓位” | `learning/02_context/01_support_resistance_targets.md`、`learning/06_trade_management/00_trade_plan.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-LIVE-TR-BO-2021` | 官方依据 + 保守执行政策 | 已核对；先处理最近现实障碍与目标，measured move 只是有依据时的目标候选；多目标必须绑定数量，不用远端投射修复近端空间不足 |
| 成交后管理与 premise 更新 | “成交后的管理” | `learning/06_trade_management/00_trade_plan.md`、`training/03_review_checklist.md` | `SRC-GOOD-TRADE-2017`、`SRC-LIVE-TR-BO-2021`、`SRC-MAKE-MONEY-2016` | 官方管理依据 + 内部风险边界 | 已核对；正常回调不因焦虑提前退出，强反向突破、持续反向跟进或 premise 失效时及时降险；新信息可降低风险，但不得放宽 stop、拉远目标或临时加仓 |
| 四种交易想法 | “市场状态与四种交易想法” | `learning/05_setups/01_trend_continuation.md`、`02_breakout_continuation.md`、`03_trading_range_fade.md`、`04_major_trend_reversal.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-TRADING-RANGES`、`SRC-MTR-2025` | 官方 setup 家族 + 内部归并 | 内部执行政策；趋势恢复、突破接受、回归公平区域和控制权反转只分类一次，用于组织不同 premise、失效和第一目标，不宣称为 Al Brooks 官方四分法 |
| Major Trend Reversal | “四种交易想法” | `learning/05_setups/04_major_trend_reversal.md` | `SRC-GLOSSARY`、`SRC-MTR-2025`、`SRC-10-PATTERNS` | 官方 MTR | 已核对；完整结构包含通道突破和旧趋势极值测试；早期与强反向 breakout 确认版本存在约 40%/60% 的典型概率—风险—回报交换 |
| Gap 的可选作用 | “市场状态与四种交易想法” | `learning/02_context/00_context_location_control.md`、`learning/04_patterns/07_gaps.md`、`training/01_opening_range_and_opening_reversal.md` | `SRC-GLOSSARY`、`SRC-STRONG-LEGS-2016`、`SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` | 官方定义/案例 + 可选路由 | 已核对；gap 只有实质改变位置、接受/拒绝、障碍或目标时才记录；开放或回补不能单独许可 entry、hold 或 exit |
| TBTL | “高级执行附录” | `learning/06_trade_management/01_scalp_vs_swing.md` | `SRC-ABBREVIATIONS`、`SRC-10-PATTERNS`、`SRC-MTR-2025` | 官方术语 + 保守解释 | 已核对；Ten Bars, Two Legs correction 是反转 swing 的常见经验预期，不是所有 correction 的硬性完成条件或价格目标 |
| Micro double、OO 与其他高风险 glossary 条目 | 术语边界，非执行许可 | `reference/glossary.md`、`learning/04_patterns/04_double_tops_bottoms.md`、`learning/04_patterns/06_triangles_ii_ioi_oo.md`、`learning/05_setups/05_second_entries_and_traps.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS` | 官方最低定义 | 已核对；micro double bottom/top 的趋势语境、outside-outside 的连续更大 outside bar、second entry/signal 与 H/L 严格计数均已直接核对 |
| Opening、day type、周期与时段 | 核心流程的 context 输入 | `learning/02_context/02_time_and_timeframes.md`、`training/00_day_types.md`、`training/01_opening_range_and_opening_reversal.md` | `SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` | 官方案例 + 经验归并 | 部分核对；开盘相关路径已有官方案例，跨市场时段倾向仍需用目标品种样本校准，不写成固定定律 |
