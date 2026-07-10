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

| 主题或规则 | 执行手册位置 | 学习/研究文档 | Source ID | 性质 | 状态与下一步 |
| --- | --- | --- | --- | --- | --- |
| 文档权威层级 | 文件顶部、README | `synthesis/README.md` | — | 内部治理 | 内部执行政策；已建立 |
| 学习/执行依赖边界 | README“文档边界”、执行手册“内部记法的作用域” | `00_method/`–`07_scenarios/` | — | 内部治理 | 00–06 只使用稳定概念和 README 入口；07、审计与研究可作为当前执行模型派生层 |
| M/K/C/T/D/Q/P/E/A 路由，D_init/D_live 与 Q_entry/Q_hold 边界 | 层级、两张流程图 | `synthesis/00_core_framework.md`、`synthesis/01_repeated_concepts_map.md` | — | 内部归并 | 内部执行政策；已完成第二轮逻辑审查并同步派生研究文档；G 已降为 D_init 内配置 |
| 订单批准、待成交、部分成交与实际成交 | Q“订单批准、撤销与成交”、两张流程图 | `synthesis/00_core_framework.md`、`07_scenarios/03_bar_by_bar_templates.md` | `SRC-STOP-ORDERS` | 官方订单机制 + 内部状态边界 | 已区分 Q_entry 通过与 P 激活；已成交部分使用 Q_hold，未成交余单继续使用 Q_entry |
| 基础/高级执行权限 | D“执行权限”、P1–P4 计划卡 | `07_scenarios/05_review_checklist.md` | — | 内部风险政策 | 待用交易记录校准；权限必须在时段前逐项设定，未宣称为 Brooks 官方分类 |
| Market cycle 与 M1–M6 复盘记法 | M | `01_market_cycle/` | `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-STRONG-LEGS-2016`、`SRC-MTR-2025` | 官方概念 + 内部路由 | 已核对公开层级：trend / trading range 为第一分叉，trend 再分 breakout / channel；breakout–tight channel–broad channel–trading range 是连续谱。M1–M3 base 与 M4–M6 overlay 是内部压缩，M6 可提前记录 climactic behavior，不等同于官方事后定义的 confirmed climax |
| Breakout 最低定义与接受/失败 | M4、P2、E2/E3 | `01_market_cycle/03_breakouts_and_breakout_mode.md`、`03_order_flow/03_follow_through_surprise_inertia.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STRONG-LEGS-2016` | 官方派生 | 已核对；已记录 glossary 最低事件定义与专题文章可交易形态粒度的差异，M4 不再把质量证据写成最低定义 |
| Breakout mode 与首次突破 | M5、P2/P3 | `01_market_cycle/03_breakouts_and_breakout_mode.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-OPENING-REVERSALS-2017` | 官方派生 + 执行政策 | 已核对；预判/确认路线分别进入 D_init/Q_entry，triangle/open 的概率数字不得外推到所有 M5 |
| Trader's Equation | D_init、Q_entry、Q_hold | `00_method/02_probability_risk_reward.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-STOP-ORDERS` | 官方派生 + 保守执行政策 | 已核对官方基础并同步学习文档；entry/hold 拆分、多结果、部分止盈及“同质减仓不改变每单位期望”属于内部保守化 |
| Entry / invalidation / protective stop | D_init、P1–P4 计划卡 | `03_order_flow/01_stop_entry_vs_protective_stop.md`、`06_trade_management/01_entries_stops_targets.md` | `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-RISK-113` | 官方依据 + 执行政策 | 已核对并同步学习文档；D_init 必填字段和禁止未预设放宽明确标为内部执行政策 |
| Target / measured move / partial exit | D_init、D_live、P1–P4 计划卡 | `02_context/02_support_resistance_targets.md`、`06_trade_management/01_entries_stops_targets.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-MTR-2025` | 官方依据 + 执行政策 | 已核对 PT1、支撑阻力处兑现、部分止盈与 swing 回报基线；measured move 已收敛为 Leg 1 = Leg 2、区间/形态高度、日内 gap 和 breakout height 等官方族，要求写明结构与投射锚点属于内部执行政策 |
| Position size / planned loss / scaling | D_init、D_live、P3、A | `06_trade_management/04_scaling_in_out.md`、`06_trade_management/05_risk_psychology.md` | `SRC-POSITION-SIZE`、`SRC-RISK-113`、`SRC-TRADING-RANGES` | 官方依据 + 执行政策 | 已核对并同步学习文档；仓位随止损距离调整、行为承受上限和区间 scale-in 有官方锚点，数量相关成本、`MaxLoss` 汇总、`OpenRisk` 与 `Cost_hold_delta` 公式明确为内部政策 |
| P1 趋势延续 | P1 | `04_setups/01_trend_continuation.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-MANUAL` | 官方派生 + 内部归并 | 已核对核心 setup 与 stop/target 基线；具体形态变体持续审计 |
| P2 突破跟随 | P2 | `04_setups/02_breakout_continuation.md` | `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STRONG-LEGS-2016`、`SRC-STOP-ORDERS` | 官方派生 + 内部归并 | 已核对预判/确认入场、接受/失败、D_init 基线，以及区间/形态高度、gap、breakout height 的 measured-move 目标族 |
| P3 边缘失败 / 回归 | P3 | `04_setups/03_trading_range_fade.md`、`03_order_flow/02_limit_order_market.md` | `SRC-GLOSSARY`、`SRC-TRADING-RANGES`、`SRC-STOP-ORDERS` | 官方派生 + 内部归并 | 已核对宽区间边缘、中部回避、limit/stop 路线和预设 scale-in 边界 |
| P4 控制权反转 / MTR | P4 | `04_setups/04_major_trend_reversal.md` | `SRC-GLOSSARY`、`SRC-MTR-2025`、`SRC-10-PATTERNS` | 官方 MTR + 内部 P4 边界 | 已核对完整 MTR 结构、约 40%/60% 典型概率交换和 swing 目标；早期 K4 明确标为内部候选而非官方完整 MTR |
| TBTL | P4、D_init management | `06_trade_management/03_tbtl.md` | `SRC-ABBREVIATIONS`、`SRC-MTR-2025`、`SRC-10-PATTERNS` | 官方术语 + 执行解释 | 已核对；明确是 Ten Bars, Two Legs correction / swing 预期，不是精确价格目标或 Q_entry 替代品 |
| Opening / day type | 场景叠加 | `07_scenarios/00_day_types.md`、`07_scenarios/01_opening_range_and_opening_reversal.md` | `SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` | 官方派生 + 实用分类 | 部分核对 |
| Gap 分类 | 场景叠加 | `05_patterns/06_gaps.md`、`07_scenarios/02_gap_scenarios.md` | `SRC-GLOSSARY` | 官方派生 | 部分核对；measuring / micro measuring / body / exhaustion 的高风险定义已校准，其他低影响 gap 变体继续按使用频率核对 |
| 88 pattern atlas | 非执行 | `reference/audits/pattern_atlas.md` | 多个已登记来源 | 来源/几何审计 | 已核对；持续做防回归检查 |
| Glossary 高风险执行相关条目 | 术语边界，非执行许可 | `reference/glossary.md`、`04_setups/00_what_is_a_setup.md`、`04_setups/05_second_entries_and_traps.md`、`05_patterns/07_bar_types.md` | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-MAKE-MONEY-2016`、`SRC-MISTAKES-2016` | 官方最低定义 + 明示的内部边界 | 已核对 market cycle、setup / signal / entry 时序、H/L 严格计数、second entry/signal、micro channel、pause/pullback、breakout test/mode、scalp/swing 与风险歧义；内部执行准入不再覆盖官方术语 |
| Glossary 扩展与低影响条目 | 非执行 | `reference/glossary.md`“扩展术语”与缩写区 | `SRC-GLOSSARY`、`SRC-ABBREVIATIONS` | 快速参考 | 待按正文使用频率逐步核对；不得覆盖执行手册，也不阻塞当前执行文档 |

## 审计顺序

1. ~~Entry、protective stop、planned loss、position size。~~ 已完成本轮审计。
2. ~~第一目标、部分止盈、measured move、时间约束。~~ 已完成本轮审计；具体图形的投射起止点继续在专题图形审计中校准。
3. ~~Trader's Equation 和管理尺度。~~ 已完成本轮审计。
4. ~~Breakout / breakout mode 的预判与确认路线。~~ 已完成本轮审计。
5. ~~MTR、早期反转和 TBTL。~~ 已完成本轮审计。
6. ~~Market cycle 与 glossary 高风险定义。~~ 已完成本轮审计；glossary 扩展与低影响条目按正文使用频率继续核对。
