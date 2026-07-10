# 主题与执行规则审计矩阵

> **状态：Evidence Audit / Non-normative**
>
> 本文件记录证据、性质和审计状态，不替代当前[执行手册](../README.md#权威层级)的执行文本。

本矩阵连接执行手册、学习文档和官方来源，用于证明每项规则的来源与审计状态。

## 状态定义

- **已核对**：核心结论已找到直接官方锚点，并检查了当前文档表达。
- **部分核对**：已有官方依据，但仍有未核对的执行细节、范围或冲突。
- **待核对**：当前主要来自内部文档或经验归并，尚无足够官方锚点。
- **内部执行政策**：仓库为保证一致执行而制定，不宣称是 Brooks 官方术语或规则。

## 当前矩阵

| 主题或规则 | 执行手册位置 | 派生/关联文档 | Source ID | 性质 | 状态与下一步 |
| --- | --- | --- | --- | --- | --- |
| 文档权威层级 | 文件顶部、README | `synthesis/README.md` | — | 内部治理 | 内部执行政策；已建立 |
| 学习/执行依赖边界 | README“文档边界”、执行手册“使用方式” | `00_method/`–`07_scenarios/` | — | 内部治理 | 00–06 只使用稳定概念和 README 入口；07、审计与研究可作为当前执行流程派生层 |
| 人的执行记录与同次数据约束 | “一页执行记录”、D、Q、管理事件 | `07_scenarios/03_bar_by_bar_templates.md`、`07_scenarios/05_review_checklist.md` | — | 内部治理与风控 | 不使用版本或 revision 字段；入场前只保留一份当前计划，确认旧订单无活动数量后再重写；成交后保留原始计划，只追加真实 fill 与实际触发的管理事件，无事件不重复记录；追加不授权拉远目标、补 runner/TBTL、升级 G、未预设加仓或改写命题 |
| M/K/C/T/D/Q/P 路由与管理合同边界 | 使用方式、执行层级、成交后的管理合同 | `synthesis/00_core_framework.md`、`synthesis/01_repeated_concepts_map.md` | — | 内部归并 | 内部执行政策；P1–P4 只在实际 fill 后激活，P0 是未激活交易的终端结果；G 是 D 内配置；成交后不再建立 E/A 状态或逐根 hold 方程，而是无事件持有、事件触发动作 |
| 允许下单、已挂单、部分成交与实际成交 | “订单与实际成交”、“成交后的管理合同” | `synthesis/00_core_framework.md`、`07_scenarios/03_bar_by_bar_templates.md`、`07_scenarios/05_review_checklist.md` | `SRC-STOP-ORDERS` | 官方订单机制 + 内部流程边界 | 已区分人的批准、经纪商活动订单和真实 fill；部分成交后，实际库存立即确认 protective stop 并进入原管理合同，活动余量继续检查 Q；计划改变时先确认旧订单无活动数量再重写；越过最差可接受成交价的 fill 取消余单、恢复保护，并按真实最差总结果强制减仓或退出 |
| 管理合同、部分退出与退出成交边界 | 成交后的管理合同、事件驱动检查 | `07_scenarios/04_management_examples.md`、`07_scenarios/05_review_checklist.md` | `SRC-STOP-ORDERS` | 官方管理依据 + 内部流程边界 | 无管理事件时持有；目标、失效/stop、trailing、时间或异常事件成立时执行预写动作；推进 stop 不等于减仓，退出单实际 fill 前仍按真实库存维持 protective stop |
| 基础/高级执行权限 | D“执行权限”、P1–P4 计划卡 | `07_scenarios/05_review_checklist.md` | — | 内部风险政策 | 待用交易记录校准；权限必须在时段前逐项设定，未宣称为 Brooks 官方分类 |
| Market cycle 与 M1–M6 复盘记法 | M | `01_market_cycle/` | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STRONG-LEGS-2016`、`SRC-MTR-2025` | 官方概念 + 内部路由 | 已核对公开层级：trend / trading range 为第一分叉，trend 再分 breakout / channel；breakout–tight channel–broad channel–trading range 是连续谱。M1–M3 base 与 M4–M6 overlay 是内部压缩，M6 可提前记录 climactic behavior，不等同于官方事后定义的 confirmed climax |
| 对手方、订单压力与被困交易者 | C、T | `03_order_flow/00_order_flow_model.md`、`03_order_flow/04_failed_entries_and_trapped_traders.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016` | 官方概念 + 内部执行提示 | C 要求陈述对手方最合理的 context/location/target 理由及其是否已被削弱；T 要求说明谁会入场、退出或止损及主要订单压力，不新增独立层级，也不允许无法从价格行为验证的参与者叙事 |
| Breakout 最低定义与接受/失败 | M4、P2、管理合同中的接受/失败事件 | `01_market_cycle/03_breakouts_and_breakout_mode.md`、`03_order_flow/03_follow_through_surprise_inertia.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STRONG-LEGS-2016` | 官方派生 | 已核对；glossary 给出最低事件定义，专题文章描述可交易形态粒度；M4 的质量证据不属于最低定义 |
| Breakout mode 与首次突破 | M5、P2/P3 | `01_market_cycle/03_breakouts_and_breakout_mode.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-OPENING-REVERSALS-2017` | 官方派生 + 执行政策 | 已核对；预判/确认路线分别进入 D/Q，triangle/open 的概率数字不得外推到所有 M5 |
| Trader's Equation | D、Q、新增风险 | `00_method/02_probability_risk_reward.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-STOP-ORDERS`、`SRC-BREAKOUTS-2025` | 官方派生 + 保守执行政策 | 已核对官方基础；Q 用于决定是否承担新风险，多结果和部分止盈按实际入场计划计算；毛盈利使用保守退出价、毛亏损使用最差预计止损成交价，未嵌入成本只扣一次；成交后不逐根建立 hold 方程，只有预写 scale-in 或异常成交改变风险时重新检查 |
| Entry / invalidation / protective stop | D、P1–P4 计划卡 | `03_order_flow/01_stop_entry_vs_protective_stop.md`、`06_trade_management/01_entries_stops_targets.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-RISK-113`、`SRC-BREAKOUTS-2025`、`SRC-GOOD-TRADE-2017` | 官方依据 + 执行政策 | 官方材料支持 price-action stop、同图多个合理 stop、宽 stop 配小仓位及提前退出；仓库将 invalidation、结构锚点、订单触发价和最差预计成交价分开，并要求每个 stop 方案独立完成 size、target、概率和 Q |
| Target / measured move / partial exit | D、管理合同、P1–P4 计划卡 | `02_context/02_support_resistance_targets.md`、`06_trade_management/01_entries_stops_targets.md`、`07_scenarios/04_management_examples.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-BREAKOUTS-2025`、`SRC-LIVE-TR-BO-2021`、`SRC-MTR-2025` | 官方依据 + 执行政策 | 官方材料支持在支撑阻力附近兑现、使用多种 measured move 形成目标候选，并按突破强度与路径阻力选择较近或较远目标；仓库将其落实为必填的路径障碍、结构目标区、保守退出价和绑定数量，measured move 仅在实际被选作目标依据时调用并冻结端点 |
| Position size / planned loss / scaling | D、P3、管理事件 | `06_trade_management/04_scaling_in_out.md`、`06_trade_management/05_risk_psychology.md`、`07_scenarios/05_review_checklist.md` | `SRC-POSITION-SIZE`、`SRC-RISK-113`、`SRC-TRADING-RANGES`、`SRC-BREAKOUTS-2025`、`SRC-GOOD-TRADE-2017` | 官方依据 + 执行政策 | 官方原则是仓位服从正确 stop 距离；仓库以最差 entry 到最差预计 stop fill 计量，部分成交采用真实 fill + 活动余量最差价格的混合 PlannedLoss；每次入场/加仓 fill 后确认 protective stop 与最差总结果，每次 scale-in 同时通过预写触发、该层 Q 和汇总风险 |
| P1 趋势延续 | P1 | `04_setups/01_trend_continuation.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-MANUAL`、`SRC-STRONG-LEGS-2016`、`SRC-RISK-113`、`SRC-POSITION-SIZE` | 官方派生 + 内部归并 | 已核对回调/flag 结构 stop、signal stop 的适用边界、仓位随 stop 调整，以及前极值、Leg 1 = Leg 2 和条件式延伸目标的层级；gap 只在相关时作为控制证据 |
| P2 突破跟随 | P2 | `04_setups/02_breakout_continuation.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STRONG-LEGS-2016`、`SRC-STOP-ORDERS`、`SRC-BREAKOUTS-2025`、`SRC-LIVE-TR-BO-2021` | 官方派生 + 内部归并 | 已核对直接突破与回踩确认的 stop 差异、完整 breakout-leg 风险、近端阻力、现实兑现价及条件式区间/形态/breakout-height 投射；gap 保留或回补只在相关时作为接受/失败证据 |
| P3 边缘失败 / 回归 | P3 | `04_setups/03_trading_range_fade.md`、`03_order_flow/02_limit_order_market.md` | `SRC-GLOSSARY`、`SRC-TRADING-RANGES`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016` | 官方派生 + 内部归并 | 已核对宽区间边缘、中部回避、limit/stop 路线、wide structural stop、多个合理兑现位和预设 scale-in 边界 |
| P4 控制权反转 / MTR | P4 | `04_setups/04_major_trend_reversal.md` | `SRC-GLOSSARY`、`SRC-MTR-2025`、`SRC-10-PATTERNS` | 官方 MTR + 内部 P4 边界 | 已核对完整 MTR 结构、旧极值测试外的 stop、约 40%/60% 概率—风险—回报交换和反向 swing / measured-move 目标；早期 K4 明确标为内部候选而非官方完整 MTR |
| TBTL | P4、D management | `06_trade_management/03_tbtl.md` | `SRC-ABBREVIATIONS`、`SRC-MTR-2025`、`SRC-10-PATTERNS` | 官方术语 + 执行解释 | 已核对；明确是 Ten Bars, Two Legs correction / swing 预期，不是精确价格目标或 Q 替代品 |
| Opening / day type | 场景叠加 | `07_scenarios/00_day_types.md`、`07_scenarios/01_opening_range_and_opening_reversal.md` | `SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` | 官方派生 + 实用分类 | 部分核对 |
| Gap 定义与条件式执行作用 | M、C、D、管理合同、目标（如相关） | `02_context/00_context_location_control.md`、`04_setups/02_breakout_continuation.md`、`05_patterns/06_gaps.md`、`07_scenarios/01_opening_range_and_opening_reversal.md`、`07_scenarios/02_gap_scenarios.md` | `SRC-GLOSSARY`、`SRC-STRONG-LEGS-2016`、`SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018`、`SRC-LIVE-TR-BO-2021` | 官方定义/案例 + 内部执行路由 | 已核对 opening、gap reversal、body、micro measuring、moving-average、measuring 和 exhaustion 的实时/事后边界；gap 不是主链节点或每笔必填项，只有会实质改变判断时才记录比较对象、状态和接受/拒绝证据，并并入既有候选、结构 stop、路径障碍、目标或预写管理事件；回补或开放状态不能单独触发动作 |
| 88 pattern atlas | 非执行 | `reference/audits/pattern_atlas.md` | 多个已登记来源 | 来源/几何审计 | 已核对；持续做防回归检查 |
| Glossary 高风险执行相关条目 | 术语边界，非执行许可 | `reference/glossary.md`、`04_setups/00_what_is_a_setup.md`、`04_setups/05_second_entries_and_traps.md`、`05_patterns/07_bar_types.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-MAKE-MONEY-2016`、`SRC-MISTAKES-2016` | 官方最低定义 + 指向执行层的边界 | 已核对 market cycle、setup / signal / entry 时序、H/L 严格计数、second entry/signal、micro channel、pause/pullback、breakout test/mode、scalp/swing 与风险歧义；glossary 不复制内部流程字段、M3 编号或小于 1R 的内部批准政策 |
| Glossary 扩展与低影响条目 | 非执行 | `reference/glossary.md`“扩展术语”与缩写区 | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS` | 快速参考 | 待按正文使用频率逐步核对；不得覆盖执行手册，也不阻塞当前执行文档 |
