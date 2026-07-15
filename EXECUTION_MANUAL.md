# Al Brooks 价格行为交易与执行手册

> **状态：Normative**
>
> 本文件前半部从完整的[学习体系](LEARNING_PATH.md)提炼并融会贯通本仓库实际使用的 Al Brooks 交易原则，后半部规定仓库的订单与记录操作。价格行为定义以已核对来源、[核心术语表](reference/glossary.md)和对应学习专题为准；`Normative` 只表示使用本仓库执行与记录流程时必须遵守后半部的操作边界，不表示仓库可以另造 setup、stop 或 target 规则。

## 1. 使用边界

Al Brooks 的交易主线是：先判断 market cycle 和 context，再寻找有意义的 setup；根据 price action 决定 entry、protective stop 和 profit target，用 Trader's Equation 判断交易是否合理，并在成交后继续根据新的 price action 管理原 premise。

本手册不把这条主线重新编号成一套新方法，也不限定只有某几类 setup 才能交易。趋势 flag、breakout、breakout pullback、trading-range trade、failed breakout、MTR、final flag 和其他 Brooks setup，都必须使用各自的结构、stop 和目标逻辑。

仓库只额外规定以下操作事项：

- 用统一版式保存当时的交易计划、订单和成交事实。
- 区分模拟与真实订单，区分触发条件、平台订单、成交和真实持仓。
- 真实或模拟持仓都必须有明确的 protective-stop 保护；真实订单还要核对经纪商状态。
- 保存原始判断，不用后续结果覆盖当时记录。
- 记录费用、滑点、部分成交和订单异常，使复盘能够还原实际风险。

这些是记录与订单安全约定，不是 Al Brooks 价格行为术语，也不决定某个 setup 的市场含义。

仓库不替用户设定账户、单笔、时段或相关敞口的具体数值。使用真实资金前必须自行确定这些边界；没有风险边界时，本仓库只能用于学习、回放和模拟。

## 2. 价格行为交易主线

### Market cycle 与 context

先判断市场更接近 trend 还是 trading range。Trend 再观察当前是 breakout、tight channel 还是 broad channel。这个连续谱决定交易者更适合顺势、等待回调、在区间边缘交易，还是等待更清楚的价格行为。

Context 包括左侧价格行为、买卖压力、支撑阻力、旧高低点、趋势成熟度和当前所在位置。K 线形态只有放回 context 后才可能成为 setup；漂亮 signal bar 不能覆盖不利位置或已经耗尽的目标空间。

### Setup、entry 与反方理由

Setup 是带 context、可作为放置入场单依据的 pattern。下单前需要知道：交易者准备按什么价格行为入场、反方向为什么仍可能合理，以及哪种后续行为会削弱或否定当前 premise。

入场逻辑与平台订单类型必须分开。例如，在 signal bar 高点上方一个 tick 买入描述的是 buy stop-entry 逻辑；平台可能使用 stop-market 或 stop-limit。Stop entry 用于进入交易，protective stop 用于退出已成交持仓，两者不能都简写成“stop order”。

如果无法把 context、entry、stop、target 和 Trader's Equation 组织成一笔合理交易，就没有必要仅因出现某个 pattern 而下单。

### Protective stop 与 position size

Protective stop 应放在价格行为表明交易 premise 已错、或交易者不再愿意承担该结构风险的位置。Signal-bar stop、swing stop、完整 breakout stop 或更宽的 price-action stop 都可能合理；选择取决于具体 setup 和管理方式。

同一图表可能存在多个合理 stop。较宽 stop 要用较小仓位，不能把窄 stop 的仓位与宽 stop 的存活空间拼成一笔交易。仓位由 stop 距离和交易者能够客观管理的规模决定，而不是由信心决定。

宽 stop 有时只是 catastrophe stop。若新的 price action 已经使 premise 不再成立，应按当前判断退出，而不是只因最远 stop 尚未触发而继续依赖希望。

### Profit target 与 Trader's Equation

Profit target 来自具体 setup、scalp 或 swing 的管理选择，以及图上的 support/resistance 和 magnets。常见依据包括前高前低、区间内部或边缘、均线、趋势线和通道线、breakout point、opening price、Leg 1 = Leg 2、区间或形态高度，以及结构清楚的 measuring gap。

不同 setup 的预期不同：H2/L2 常按 scalp 管理，趋势仍强时可 swing；moving-average gap bar 可能测试旧趋势极值；强 breakout 常使用 measured move 或至少第二腿；trading range 以 buy low, sell high, scalp 为主；成功 MTR 寻找反向两腿和 swing profit。路径预期不自动等于固定价格目标。

目标是区域而不是保证。前方 support/resistance 会影响更远目标的到达概率，但不要求交易者在每个较近价位退出。多目标、scaling out 或 runner 是否合适，取决于当前结构和原管理计划。

Trader's Equation 把成功概率、潜在回报和风险放在同一问题中。多数不确定场景的方向概率接近 40–60%；swing 通常寻找至少约两倍风险的潜在回报，高概率强 breakout 可以接受较小 reward/risk，但会付出较差 entry、较宽 stop 或较少剩余空间。

### 成交后的 premise 管理

入场前要知道交易按 scalp 还是 swing 管理、stop 在哪里、目标是什么。成交后继续读取 price action：只要市场行为仍符合 premise，就按相应 scalp 或 swing 方式管理；当强反向行为、持续反向 follow-through 或其他证据使 premise 不再成立时，及时退出并重新评估。

交易者可以在 target 或 stop 触发前退出，也可以在新 swing 形成后向保护方向调整 stop。Scale-in 也可以是合理管理，但必须从一开始就按较小初始仓位、最外侧 stop 和全部数量的总风险设计，不能把情绪性加仓当作价格行为依据。

新的反向机会应按新的 context、entry、stop、target 和 Trader's Equation 评估，不能仅因原交易亏损就机械反手。

## 3. 初学者学习范围

初学者通常应以 stop entry 和 swing trading 为基础，因为 stop entry 至少要求价格先向交易方向运动，swing 的较大目标也比小目标 scalp 更容易形成可行的 Trader's Equation。

学习阶段宜：

- 主要练习清楚 context 中的合理 stop-entry setup。
- 使用正确的 price-action stop，并按 stop 距离缩小仓位。
- 优先理解 swing、40–60 概率与约 2R 回报之间的交换。
- 使用小到能够客观管理的仓位。
- 避免在 trading range 中部追逐普通信号；tight trading range 中通常等待突破。

Limit entry、close entry、scale-in、scalp 和早期 reversal 都属于 Brooks 方法的一部分，并非无效或禁止。它们需要更强的读图与管理能力，因此可以在掌握基础 stop-entry swing 后再系统练习。

## 4. 入场后观察什么

触发之后重点观察：

- Entry bar 是否有力度，后续是否有 follow-through。
- 突破点、signal bar 或关键 support/resistance 是否守住。
- 回调是否符合当前 trend、channel 或 trading range。
- 反方是否快速收回关键位置并获得连续性。
- 原 setup 的 scalp 或 swing 目标是否仍现实。

弱 entry 或短暂失望会降低信心，但不自动等于 failure。Failure、failed breakout 和 trapped traders 有各自定义；不能只凭一根反向 K 线编造被困者故事。

## 5. Stop、目标和风险计算

Price-action 判断与订单计算要分别写清：

- 哪个价格行为或结构使 premise 不再成立。
- 采用哪一个合理 protective stop，以及对应触发价。
- 预计实际成交与滑点后，账户会承担多少风险。
- 当前 setup 使用什么 profit target，依据是什么。
- 这笔交易按 scalp、swing、scale-out 还是 runner 管理。

Measured move 只有在测量对象和投射起点清楚时才是合格目标候选。Gap 只有在它实际构成支撑阻力、接受/拒绝证据或量度参照时才参与计划。

最简 Trader's Equation 可以写成：

```text
成功概率 × 潜在回报 > 失败概率 × 风险
```

佣金、滑点和资金费不属于价格行为定义，但会影响真实净结果，因此在仓库记录中单独计算。所有输入必须描述同一笔交易；如果 entry、stop、target 或管理方式改变，就要重新评估相应的概率、风险和回报。

没有可靠统计时，不写伪精确概率。不能用理想成交、完美临场退出或与当前 setup 无关的远端投射制造看似有利的数学。

## 6. 交易计划中的一致关系

一笔交易计划需要让以下关系彼此一致：

- 当前 market cycle、context 和位置。
- Setup、entry，以及反方向仍可能合理的原因。
- 合理 protective stop 与匹配该 stop 距离的仓位。
- 这类 setup 的 profit target，以及 scalp 或 swing 管理方式。
- Trader's Equation，以及成交后继续支持或否定 premise 的价格行为。

这些关系来自前文所述的价格行为交易主线，不是另一套 setup 分类或编号。具体 setup 的 structure、stop 和 target 见 [`learning/05_setups/`](learning/05_setups/README.md)。

## 7. 仓库订单与记录操作

本节是仓库自定的操作规范。它只保证记录可复核、订单状态清楚和持仓受到保护，不增加价格行为准入条件。

### 批次配置与计划快照

开始连续回放、模拟或实盘前，记录执行来源、交易所与数据源、品种、时区与时段、决策周期、tick、费用、滑点处理和用户风险边界。环境发生实质变化时建立新配置。

准备提交订单时，用[执行记录模板](EXECUTION_RECORD_TEMPLATE.md)保存当时的 context、setup、entry、stop、target、Trader's Equation、仓位和管理方式。后续信息以事件追加，不覆盖原计划；这项冻结只服务于复盘，不禁止交易者根据新 price action 管理持仓。

### 订单、成交与保护

必须区分：

| 状态 | 含义 |
| --- | --- |
| 计划完成 | 已记录交易计划，尚未向平台提交 |
| 活动订单 | 平台或经纪商已接受，仍有未成交数量 |
| 部分成交 | 已成交数量构成持仓，余量仍是活动订单 |
| 全部成交 | 计划数量已成交，没有活动入场余量 |
| 撤销、到期或拒绝 | 对应订单不再活动；此前成交形成的持仓不因此消失 |

只有成交确认才改变持仓数量。任何入场成交后，立即核对实际数量，并确认全部持仓已由 protective stop 覆盖；真实交易还必须确认经纪商已经接受 stop。Stop 被拒绝、意外撤销、数量不足且无法立即恢复时，退出未受保护的持仓。

退出决定不等于已经退出。退出订单成交前，仍按实际持仓维持保护。

### 管理事件

订单状态、成交、持仓数量、active stop、目标订单、premise 判断或实际动作发生变化时，在同一记录中追加事件。逐根观察保留在训练时间线中，不复制成第二份订单日志。

只有持仓数量或 active stop 变化时，才追加两项账户视图：若当前 stop 成交的保守账户结果，以及按当时市价计算的潜在浮盈回吐。它们只用于记录风险，不自动触发减仓或推进 stop。

### 预设 scale-in 与多目标

使用 scale-in 时，记录每层计划价格、数量、共同或分别使用的 stop，以及全部层的最坏总结果。计划可以根据新 price action 取消尚未成交的层级；已经成交的数量仍按真实持仓处理。

使用多个目标时，每个活动退出订单都要有明确数量，避免重复计算同一仓位。Runner 可以使用 price-action trailing 而不设置固定最终限价单；记录中仍应说明它依据什么结构继续持有或退出。

### 部分成交与异常

部分成交后，已成交数量立即成为持仓并获得完整保护；未成交余单继续按活动订单管理。若 setup、允许价格或总风险改变，可以撤销余单，但不能把已成交持仓当成未成交。

若成交越过计划允许价格、数量错误或风险超出用户边界：

1. 取消所有尚未成交的新增风险订单。
2. 确认真实持仓已有 protective stop。
3. 用真实 fill 和数量重新计算风险。
4. 当前交易不再合理或超出风险边界时，减仓或退出。
5. 在复盘中记录执行异常，不用最终盈亏证明异常成交合理。

复杂订单日志至少保存时间、用途、状态、计划数量、活动数量、本次与累计成交、成交价、费用、实际持仓、active stop 和当前风险。

## 8. 复盘入口

复盘应分开评价：当时的 market reading 与交易计划是否合理，订单和管理是否按当时计划及后续 price action 执行，以及后来市场实际如何发展。盈利不能证明错误计划合理，亏损也不能单独证明合理 setup 错误。

训练与复盘见 [`training/README.md`](training/README.md)，空白记录见 [`EXECUTION_RECORD_TEMPLATE.md`](EXECUTION_RECORD_TEMPLATE.md)，跨章节核心术语边界见 [`reference/glossary.md`](reference/glossary.md)。来源身份与核对状态从 [`reference/README.md`](reference/README.md) 进入。
