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

| 主题或规则 | 主要所有者 / 规范执行位置 | 派生/关联文档 | Source ID | 性质 | 状态与下一步 |
| --- | --- | --- | --- | --- | --- |
| 文档权威与学习优先结构 | 结构：`DOCUMENTATION_GOVERNANCE.md`；全局顺序：`LEARNING_PATH.md` | 根 `README.md`、各目录 `README.md` | — | 内部治理 | 内部治理；学习、执行、训练、查阅、来源和审计已有分离所有者，形态库与高级执行均不属于默认学习主线 |
| 自然语言核心流程、连续训练与高级附录边界 | `EXECUTION_MANUAL.md`“一条执行流程”、“核心五问”、“高级执行附录” | `EXECUTION_RECORD_TEMPLATE.md`、`training/README.md`、`training/02_bar_by_bar_templates.md`、`training/03_review_checklist.md` | — | 内部执行政策 | 内部执行政策；执行顺序、记录契约与动作只由手册规定，派生模板只承载批次配置和单笔记录版式，训练层只组织连续回放、观察和复盘，复杂订单仅在实际相关时进入同一权威文件的附录 |
| 账户、单笔与时段风险范围 | `EXECUTION_MANUAL.md`“使用边界”、“一条执行流程” | `EXECUTION_RECORD_TEMPLATE.md`、`README.md`、`LEARNING_PATH.md` | — | 范围声明 | 内部治理；未另行设定上位风险边界时只用于模拟与复盘，核心学习不构成实盘许可 |
| Market cycle 与结构连续谱 | 术语：`reference/glossary.md`；教学：`learning/01_market_cycle/00_market_cycle.md`；执行：手册“市场状态” | `learning/01_market_cycle/` | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STRONG-LEGS-2016` | 官方概念 + 官方视觉经验倾向 | 已核对；先分 trend / trading range，trend 再分 breakout / channel；连续谱的根数与回调深度是官方识别线索，不是机械阈值或目标市场统计 |
| Context、买卖压力、位置、控制权与 Always In | 术语：`reference/glossary.md`；教学：`learning/02_context/00_context_location_control.md`；执行：手册“核心五问” | `learning/02_context/` | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016` | 官方概念 + 本仓库教学归并 | 已核对；pressure 是累积价格证据，control / location 是教学组织词，Always In 不替代目标或 Trader's Equation |
| Pattern、setup、signal bar 与 entry bar | 术语：`reference/glossary.md`；教学：`learning/05_setups/00_what_is_a_setup.md`；执行：手册“Setup、入场和可观察证据” | `learning/04_patterns/00_patterns_are_language.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS` | 官方最低定义 + 本仓库准入边界 | 已核对；实际 fill 后最后一根才取得 signal-bar 角色，pattern 和官方 setup 都不自动完成本仓库交易计划 |
| Follow-through、failure、success 与 trapped in a trade | 术语：`reference/glossary.md`；教学：`learning/03_order_flow/00_acceptance_and_failure.md`；执行：手册“Setup、入场和可观察证据” | `training/03_review_checklist.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-GOOD-TRADE-2017` | 官方结果边界 + 本仓库描述性教学标签 | 已核对；weak / tentative / confirmed 是教学层级；strict failure、success 与当前 trapped 状态已按官方边界区分，premise 提前失效退出不另造官方结果名 |
| Breakout 最低定义、接受与 breakout mode | 术语：`reference/glossary.md`；教学：`learning/01_market_cycle/03_breakouts_and_breakout_mode.md`；执行：手册“市场状态” | `learning/01_market_cycle/02_trading_ranges.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STRONG-LEGS-2016`、`SRC-ABBREVIATIONS` | 官方最低事件 + 质量证据 | 已核对；最低越界事件与可交易 breakout pattern 的强收盘/跟进粒度分开，回踩不是必要步骤，breakout mode 不预设方向 |
| Trading range、BLSHS 与紧区间回避 | 教学：`learning/01_market_cycle/02_trading_ranges.md`；执行：手册“学习者默认范围”、“四种交易想法” | `learning/05_setups/03_trading_range_fade.md` | `SRC-TRADING-RANGES`、`SRC-STOP-ORDERS` | 官方原则 + 保守学习范围 | 已核对；区间中部回避，宽区间边缘可有 stop 或高级 limit 方案，紧区间多数学习者等待 |
| Trader's Equation 与 40–60 启发 | 术语：`reference/glossary.md`；教学：`learning/00_method/01_probability_risk_reward.md`；执行：手册“Trader's Equation” | `learning/06_trade_management/01_scalp_vs_swing.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-STOP-ORDERS`、`SRC-BREAKOUTS-2025` | 官方公式/经验启发 + 本仓库成本扩展 | 已核对；官方最低式与约 40–50% / 2R 启发已核对，单列成本 `C`、同方案约束和避免伪精确属于明确标注的保守执行扩展 |
| Scalp、swing 与学习者默认范围 | 术语：`reference/glossary.md`；教学：`learning/06_trade_management/01_scalp_vs_swing.md`；执行：手册“学习者默认范围” | `learning/06_trade_management/README.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-RISK-113` | 官方定义/经验倾向 + 保守学习范围 | 已核对；小目标常需多数人难以维持的高胜率，多数学习者优先小仓、stop entry 与 swing |
| Entry、订单类型、premise 失效与 protective stop | 执行：`EXECUTION_MANUAL.md`“一条执行流程”、“Setup、入场和可观察证据”、“Protective stop、目标和仓位”；教学：`learning/03_order_flow/01_stop_entry_vs_protective_stop.md` | `EXECUTION_RECORD_TEMPLATE.md`、`learning/06_trade_management/00_trade_plan.md`、`training/03_review_checklist.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-RISK-113`、`SRC-GOOD-TRADE-2017` | 官方 stop 依据 + 本仓库执行拆分 | 内部执行政策；stop-entry 逻辑与平台 stop-market / stop-limit 类型、protective stop 分列，合理 price-action stop、多个可行 stop 与远 stop 配小仓的官方底座已核对；四层 stop 拆分及不得放宽属于仓库政策 |
| Position size、计划损失与持仓回吐记录 | 执行：`EXECUTION_MANUAL.md`“Protective stop、目标和仓位” | `training/03_review_checklist.md`、`learning/06_trade_management/02_scaling_in_out.md`、`03_risk_psychology.md` | `SRC-POSITION-SIZE`、`SRC-RISK-113`、`SRC-TRADING-RANGES`、`SRC-BREAKOUTS-2025` | 官方仓位原则 + 内部风险核算 | 内部执行政策；仓位服从 stop 距离和行为承受能力、持仓后关注当前价到 stop 距离的官方原则已核对；仅在实际数量或 active stop 变化时，把 stop 若成交的账户结果与该事件时未实现利润回吐分列追加，不另设自动减仓或推进 stop 阈值 |
| Target、support/resistance 与 measured move | 教学：`learning/02_context/01_support_resistance_targets.md`；执行：手册“Protective stop、目标和仓位” | `learning/06_trade_management/00_trade_plan.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-LIVE-TR-BO-2021` | 官方目标依据 + 保守执行政策 | 内部执行政策；measured move 的官方构造与 magnet 边界已核对，第一现实目标、多目标绑定数量和不以远端投射修复近端空间属于仓库政策 |
| 成交后管理与 premise 更新 | `EXECUTION_MANUAL.md`“成交后的管理” | `learning/06_trade_management/00_trade_plan.md`、`training/03_review_checklist.md` | `SRC-GOOD-TRADE-2017`、`SRC-LIVE-TR-BO-2021`、`SRC-MAKE-MONEY-2016` | 官方管理依据 + 内部风险边界 | 内部执行政策；反向信号/突破可提前退出的官方依据已核对，不放宽 stop、不拉远目标、不临时加仓及事件记录是内部规范 |
| 四种交易想法 | `EXECUTION_MANUAL.md`“市场状态与四种交易想法” | `learning/05_setups/01_trend_continuation.md`、`02_breakout_continuation.md`、`03_trading_range_fade.md`、`04_major_trend_reversal.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-TRADING-RANGES`、`SRC-MTR-2025` | 官方 setup 家族 + 本仓库组织归并 | 内部执行政策；四分法只组织 premise、失效和第一目标，不宣称为 Al Brooks 官方分类 |
| Major Trend Reversal | 术语：`reference/glossary.md`；教学：`learning/05_setups/04_major_trend_reversal.md`；执行：手册“四种交易想法” | `learning/01_market_cycle/04_climax_and_transition.md` | `SRC-GLOSSARY`、`SRC-MTR-2025`、`SRC-10-PATTERNS` | 官方定义 + 官方经验性概率倾向 | 已核对；完整结构含通道突破和旧极值测试；约 40%/60% 是官方典型交换，不是跨市场固定胜率 |
| Gap、Body Gap 与重新定价 | 教学：`learning/04_patterns/07_gaps.md`；术语：`reference/glossary.md`；执行：手册“市场状态” | `learning/02_context/00_context_location_control.md`、`training/01_opening_range_and_opening_reversal.md` | `SRC-GLOSSARY`、`SRC-STRONG-LEGS-2016`、`SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` | 官方定义/案例 + 可选路由 | 已核对；Body Gap 不要求参照 K 线相邻；本仓库只在 gap 改变位置、接受/拒绝、障碍或目标时把它纳入核心判断 |
| Wedge 与 Parabolic Wedge | 教学：`learning/04_patterns/03_wedges.md`；术语：`reference/glossary.md` | `learning/05_setups/04_major_trend_reversal.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-PATTERNS-OPEN-2018` | 官方最低结构 + 官方经验性结果倾向 | 已核对；parabolic wedge 是 tight channel 中至少三腿的 climactic wedge，不要求逐腿更陡；首次反转常只按 minor reversal / trading range 路径观察，不自动升级 MTR |
| TBTL | 术语：`reference/glossary.md`；教学：`learning/06_trade_management/01_scalp_vs_swing.md`；执行：手册“高级执行附录” | `learning/05_setups/04_major_trend_reversal.md` | `SRC-ABBREVIATIONS`、`SRC-10-PATTERNS`、`SRC-MTR-2025` | 官方术语 + 官方经验预期 + 保守解释 | 已核对；Ten Bars, Two Legs correction 是反转 swing 的常见预期，不是所有 correction 的硬条件或价格目标 |
| Inside / outside / reversal bar 与 OO | 术语：`reference/glossary.md`；教学：`learning/04_patterns/01_bar_types.md`、`06_triangles_ii_ioi_oo.md` | — | `SRC-GLOSSARY` | 官方最低定义 | 已核对；outside bar 允许一侧相等、另一侧严格越界，reversal bar 的经典外观不是最低条件，OO 要求第二根是更大的 outside bar |
| H/L 计数、second entry 与 second signal | 术语：`reference/glossary.md`；教学：`learning/04_patterns/02_h1_h2_l1_l2.md`、`learning/05_setups/05_second_entries_and_traps.md` | — | `SRC-GLOSSARY`、`SRC-10-PATTERNS` | 官方最低定义 + 仓库一致计数约定 | 部分核对；仓库按当前 glossary 的严格 `above` / `below` 计数，但 2020 官方形态文章存在 `at or above` / `at or below` 的较松文字，保留差异而不机械统一 |
| Micro double top / bottom | 术语：`reference/glossary.md`；教学：`learning/04_patterns/04_double_tops_bottoms.md` | — | `SRC-GLOSSARY` | 官方最低定义 | 已核对；micro double 在 spike 中可承担 one-bar flag，在相反 flag 末端也可成为 reversal setup，不天然等于反转 |
| Triangle | 术语：`reference/glossary.md`；教学：`learning/04_patterns/06_triangles_ii_ioi_oo.md` | — | `SRC-ABBREVIATIONS` | 官方最低定义 + 官方经验性概率倾向 | 已核对；TRI 至少五次反转，约 50/50 方向和首破失败只属于 triangle 语境；expanding triangle 作为相邻变体分开说明 |
| Opening、day type、周期与时段 | 教学：`learning/02_context/02_time_and_timeframes.md`；训练：`training/00_day_types.md`、`01_opening_range_and_opening_reversal.md` | 手册“核心五问”的 context 输入 | `SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` | 官方案例 + 本仓库训练归并 + 需市场数据验证 | 部分核对；开盘路径已有官方案例，跨市场时段与日型倾向仍需目标品种样本校准，不写成固定定律 |
