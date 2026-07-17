# 学习主题与人工策略地图

> **定位：供学习者确认知识怎样进入人工决策，并供维护者检查策略覆盖**
>
> 学习主题不一定都应成为独立策略。只有能够独立说明适用环境、形成顺序、入场、撤单、保护止损、目标、管理和放弃条件的内容，才拥有策略页。

## 五种角色

| 角色 | 含义 |
| --- | --- |
| 市场背景 | 帮助选择策略家族，本身不直接触发交易 |
| 形态语言 | 描述结构、位置或顺序，必须依附上层交易理由 |
| 可执行策略 | 已有一页完整的人工计划 |
| 管理原则 | 影响数量、止损、目标和持仓处理，不独立决定方向 |
| 执行原则 | 处理订单、成交、保护和复盘，不选择市场机会 |

## 三层来源归属

| 层级 | 可以归到这一层的内容 | 不能据此宣称的内容 |
| --- | --- | --- |
| Brooks 明示 | [来源台账](official_sources.md)已核验的市场周期、形态定义、价格行为 premise、常见目标或管理原则 | 有 Brooks 概念锚点，不等于整张策略页及其参数都是 Brooks 原文规则 |
| 仓库推导 | 把多个 Brooks 概念组合成单一候选，划分策略页、选择目标锚点、规定策略之间的归类与切换 | 这是可审计的人工整理，不是新增的 Brooks 定义或通用概率结论 |
| 执行基线 | 固定根数与时间窗口、精确实体比例、唯一入场时点、撤单期限、单目标和订单状态处理 | 这些参数服务一致执行，不应外推为所有市场、周期和交易者的统一硬规则 |

同一页可以同时包含三层内容。审核时应分别标记“官方锚点”“仓库推导”和“执行基线”；只确认其中一层，不能替另外两层背书。

## Brooks 10 Best Patterns 覆盖

以下十项按来源台账中的 `SRC-10-PATTERNS` 对照；这里只说明概念在本仓库的去向，不把策略页的人工参数归回官方来源。

| Brooks pattern | 在本仓库的角色 | 覆盖方式 |
| --- | --- | --- |
| Major trend reversals | 可执行策略 | 同一 MTR 过程分为[旧极值测试失败后的第二次反向信号入场](../strategy/reversal/mtr_old_extreme_test_failure.md)与[强反向突破、跟进后的第一次回调信号入场](../strategy/reversal/mtr_confirmed_breakout_pullback.md)两个仓库执行版本 |
| Final flags | 形态语言与可执行策略 | [最终旗形突破失败后的反转](../strategy/reversal/final_flag_reversal.md) |
| Breakouts | 市场背景与可执行策略 | 强突破、跟进确认、第一次回测和 failed failure 四条[突破路径](../strategy/breakout/README.md) |
| High 2 / Low 2 | 形态语言与可执行策略 | [趋势中的第二次恢复入场](../strategy/trend/second_entry_continuation.md) |
| Wedges | 形态语言与可执行策略 | 趋势内使用[三推回调](../strategy/trend/wedge_pullback_continuation.md)，趋势末端使用[楔形逆向修正](../strategy/reversal/wedge_correction.md) |
| Channels | 市场背景 | 用于判断顺势、回调、宽通道转区间或反转环境；不凭“存在通道”独立入场 |
| Measured moves | 管理原则（目标概念） | 为突破或摆动提供目标候选；投射是 magnet，不保证到达，也不是独立 setup |
| Trading range reversals | 可执行策略 | 区间边缘确认、预设限价加仓与 failed breakout 三条[区间路径](../strategy/range/README.md) |
| Opening reversals | 可执行策略 | [前一交易日极值二次反转](../strategy/opening/opening_previous_extreme_reversal.md)；其他开盘机会仍须各自满足独立 premise |
| Magnets | 市场背景与管理原则（目标概念） | 支撑阻力、旧极值和 session open 可成为吸引位；仍需另一项 setup 触发，尾盘例见[开盘价回归](../strategy/opening/late_session_open_magnet.md) |

这张表只说明官方 pattern 在人工计划中的去向；“可执行”指已有仓库策略页，不表示该页的固定参数属于 Brooks 明示。

## 市场周期与 Setup 家族

| 学习主题 | 在人工体系中的角色 | 对应策略或处理方式 |
| --- | --- | --- |
| Market cycle | 市场背景 | 先用[如何选择策略](../strategy/how_to_choose.md)区分趋势或交易区间这一基础状态；若是趋势再区分突破或通道，并记录双向等待或反转过程 |
| Trend 与 channel | 市场背景 | 进入趋势延续、突破延续或趋势反转家族；趋势和通道本身不是入场信号 |
| Trading range | 市场背景 | 使用[成熟区间边缘确认后反转](../strategy/range/range_edge_confirmation.md)、[成熟区间边缘限价试仓与预设加仓](../strategy/range/range_edge_limit_scale_in.md)或[突破失败后回到区间](../strategy/range/failed_breakout_return.md) |
| Breakout 与接受 | 市场背景与可执行策略 | 使用[强突破收盘后立即跟随](../strategy/breakout/strong_breakout_close.md)、[突破后的跟进确认](../strategy/breakout/breakout_follow_through.md)、[突破后的第一次回测](../strategy/breakout/breakout_first_pullback.md)或[假突破失败后恢复原突破方向](../strategy/breakout/failed_failure_continuation.md) |
| Breakout mode | 市场背景 | 方向未定；目前只有[严格 ii 双向突破等待](../strategy/breakout_mode/ii_bidirectional_breakout.md)形成独立双向计划 |
| Climax 与 transition | 市场背景 | 先判断是普通修正、抛物线高潮修正，还是已经发展成主要趋势反转 |
| Major trend reversal | 可执行策略 | 两条路径都先要求通道或主要趋势线突破，以及旧趋势恢复测试旧极值的过程；旧极值实际测试失败并形成第二次反向信号时可用[测试失败信号版本](../strategy/reversal/mtr_old_extreme_test_failure.md)，其后再出现强反向突破、跟进和第一次回调时才进入[突破回调信号版本](../strategy/reversal/mtr_confirmed_breakout_pullback.md) |

## 趋势延续主题

| 学习主题 | 在人工体系中的角色 | 对应策略或处理方式 |
| --- | --- | --- |
| H1/L1 | 形态语言与可执行策略 | 强趋势第一次浅回调使用[强趋势中的第一次小回调](../strategy/trend/first_small_pullback.md) |
| H2/L2 与 second entry | 形态语言与可执行策略 | 趋势背景完整时使用[趋势中的第二次恢复入场](../strategy/trend/second_entry_continuation.md) |
| Wedge pullback | 形态语言与可执行策略 | 三推是逆趋势回调且上层趋势仍完整时，使用[趋势中的三推回调](../strategy/trend/wedge_pullback_continuation.md) |
| 第一次 moving-average gap bar | 形态语言与可执行策略 | 使用[第一次均线缺口回调](../strategy/trend/first_ma_gap_pullback.md) |
| 长期不触均线后的第一次测试 | 可执行策略 | 使用[长期远离均线后的第一次测试](../strategy/trend/first_ma_test_after_long_gap.md) |
| Second moving-average gap bar | 可执行策略 | 使用[第二次均线缺口回调](../strategy/trend/second_ma_gap_pullback.md)；不能只因数到第二次就入场 |

## 反转与末端结构

| 学习主题 | 在人工体系中的角色 | 对应策略或处理方式 |
| --- | --- | --- |
| 普通 wedge reversal | 形态语言与可执行策略 | 使用[普通楔形后的逆向修正](../strategy/reversal/wedge_correction.md)，先预期修正而不是自动预期新趋势 |
| Parabolic climax | 市场背景与可执行策略 | 使用[抛物线高潮后的逆向修正](../strategy/reversal/parabolic_climax_correction.md) |
| Final flag | 形态语言与可执行策略 | 延续突破先失败并反向触发时，使用[最终旗形突破失败后的反转](../strategy/reversal/final_flag_reversal.md) |
| Double top / double bottom | 形态语言 | 根据上层背景服务趋势延续、区间反转或主要趋势反转，不独立形成统一计划 |
| Failed second entry 与 trap | 形态语言 | 先确认原方向实际失败，再从当前价格重新归入区间、突破或反转策略；不机械反手 |

## 三角形、内包和扩张结构

| 学习主题 | 在人工体系中的角色 | 对应策略或处理方式 |
| --- | --- | --- |
| ii | 形态语言与可执行策略 | 只有严格嵌套的 ii 使用[双向突破等待](../strategy/breakout_mode/ii_bidirectional_breakout.md) |
| ioi、oo、普通 triangle | 形态语言 | 保持方向中立；真正突破后根据接受、跟进或回测进入突破策略 |
| Tight trading range | 市场背景 | 成本和双边失败风险通常使交易不值得；除非完全符合现有策略，否则等待 |
| Expanding triangle | 市场背景 | 它是波动扩大的区间，不是压缩；在外侧边缘使用区间策略，获得接受的突破使用突破策略 |

## Gap、开盘与时段

| 学习主题 | 在人工体系中的角色 | 对应策略或处理方式 |
| --- | --- | --- |
| Opening gap | 市场背景 | 判断新价格被接受还是拒绝，再选择开盘突破、开盘反转或继续观察 |
| Body gap、micro measuring gap | 形态语言 | 用于判断突破强度、支撑阻力和目标，不独立触发交易 |
| Measuring gap、exhaustion gap | 事后确认与市场背景 | 实时只能记录候选；不能用后验名称提前交易 |
| 开盘测试前一交易日极值 | 可执行策略 | 使用[开盘测试前一交易日极值后的二次反转](../strategy/opening/opening_previous_extreme_reversal.md) |
| Opening range breakout | 可执行策略 | 使用[开盘区间突破并获得接受](../strategy/opening/opening_range_breakout.md) |
| Trend from the open 的第一次回调 | 可执行策略 | 使用[开盘趋势中的第一次回调](../strategy/opening/opening_trend_first_pullback.md) |
| 尾盘与 session open magnet | 可执行策略 | 仍为区间且剩余时间足够时，使用[尾盘区间向开盘价回归](../strategy/opening/late_session_open_magnet.md) |
| 最终 day type | 事后结果 | 只能在执行结束后描述，不能参与当时入场判断 |

## 交易管理与执行

| 学习主题 | 在人工体系中的角色 | 对应策略或处理方式 |
| --- | --- | --- |
| Stop entry、结构止损与 catastrophe stop | 管理原则 | Stop entry 用于触发计划；structural / price-action stop 放在该页所依赖结构之外，成交表示这项结构 premise 已失效；catastrophe stop 只是更远的安全后盾，premise 可能先失效并要求提前退出，不能等同为实时失效边界 |
| Scalp 与 swing | 管理原则 | 在入场前决定，不能成交后因盈亏临时切换 |
| Scale in | 管理原则 | 只有区间限价策略明确采用预设加仓；其他策略不得临场加仓 |
| Scale out 与 runner | 管理原则 | 只有具体策略页明确写入时才使用；当前多数基线采用单一目标 |
| Premise weakening / failure | 管理原则 | 按策略页写明的价格事实处理；premise 可以在 catastrophe stop 触发前失效，主动退出时仍保留保护直到仓位归零；原计划失败后使用[重新判断流程](../strategy/switching_after_failure.md) |
| Trader's Equation、仓位和风险心理 | 管理原则 | 每次计划都要结合真实止损、目标、成本和个人风险边界 |
| 订单、部分成交、保护与异常 | 执行原则 | 统一使用[执行手册](../execution/execution_manual.md) |
| 历史回放、模拟与实盘 | 执行原则 | 三种环境使用相同策略条件，差异见[执行环境](../execution/execution_modes.md) |
| 观察、交易与复盘记录 | 执行原则 | 统一使用[执行与复盘记录](../execution/execution_and_review_record.md) |

## 覆盖判断

当前 learning 中所有主要主题都有明确角色：成为市场背景、形态语言、管理/执行原则，或进入一项完整人工策略。没有独立策略页不表示遗漏；它表示该主题本身不足以独立决定入场、止损、目标和管理。

以后新增 learning 主题时，必须先在本页说明它的角色。只有能够写出一页单一、完整、可执行计划时，才加入策略手册。
