# 周期与时段 Context

> **状态：Core / Definition**
>
> 本文是周期分工、实时 session state、最终日型与开盘概念的权威定义页，并说明它们怎样进入 Context。具体时段倾向会因市场而异；没有当前品种样本支持时，不把经验倾向写成固定规则。

## 多周期如何分工

大周期主要帮助识别 market cycle、重要支撑阻力、大型区间和潜在目标；交易周期负责当前 setup、entry、stop 和管理。大周期不是用来否决所有小周期机会，小周期也不能因出现漂亮信号而忽略大周期关键位置。

周期冲突时，降低确定性并问：

- 哪个周期决定主要位置和目标？
- 当前 entry 与 protective stop 来自哪个周期的结构？
- 小周期运动是否真的足以改变大周期判断？
- 承受大周期波动的仓位是否足够小？

入场、stop 和目标周期应协调。用小周期 entry 追求大周期目标，就必须容许相应的正常波动；用大周期背景做短线 scalp，也不能自动获得大趋势目标。

## 时段如何影响 context

时段主要改变流动性、波动、剩余时间和目标可达性。开盘常有快速定价和突破尝试；完成大运动后的中段更可能双边交易；临近时段结束时，剩余时间可能不足以支持新 swing。

这些是观察方向，不是跨市场定律。每个市场都应先定义自己的 session，并用历史样本确认哪些时段差异具有稳定意义。执行时只保留会实质改变当前位置、目标空间或订单质量的时段信息。

## 实时 Session State 与最终日型

日内结构仍使用同一套 market-cycle 语言，只是观察窗口被预先定义为一个 session。盘中只能描述**截至当时**的状态；最终 day type 是时段结束后的结果标签，不能反向参与候选、入场或管理判断。

最低区分如下：

- **Trend session / trend day**：一方在 session 的主要部分保持控制，真实但受控的回调不自动否定趋势。
- **Trading-range session / range day**：价格在 session 内围绕公平区域反复双向测试；单条腿可以很强，不能因此提前把全天改写成趋势日。
- **Reversal session / reversal day**：session 先向一个方向推进，随后原方向失去接受，控制和持续路径转向另一侧。
- **Early-range breakout trend session**：session 开始后先形成区间，再由获得接受的突破发展成趋势；它是事件顺序描述，不是独立于 market cycle 的第四种基础状态。

这些标签会随新价格信息变化。盘中记录“当前更像什么，以及哪条新证据会改变判断”，不要为得到某种 day type 主动选择历史片段。对于 24 小时市场，session 及交易日边界必须在观察前固定。

## 开盘最低概念

- **Opening range**：预先定义的开盘窗口内形成的高低范围；窗口与边界必须使用当时数据，不能在收盘后按最好看的范围重画。
- **Opening-range breakout**：价格离开 opening range，首先只构成 breakout event / attempt；是否获得接受仍看收盘、跟进、回踩和旧区域是否被重新接受，单次刺穿不够。
- **Trend from the open**：开盘后很快形成方向，初始极值在随后许多根中保持，且没有真正 pullback；它比普通 trend day 更强调趋势从 session 开始阶段形成。
- **Opening reversal**：开盘后的初始方向在已知支撑、阻力或旧价格区域附近失去接受，随后形成反向路径。它可能与 double top/bottom、wedge 或 failed breakout 重叠，但名称本身不构成交易许可。

Opening gap 只说明开盘重新定价，不预设当天方向；opening gap 与 gap reversal 的最低定义见[缺口专题](../04_patterns/07_gaps.md)，新价格是否获得接受见[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)。开盘仍先判断基础状态是 trend 还是 trading range；若为 trend，再判断当前主要是获接受的 breakout phase（spike）还是 channel，同时另外记录 breakout mode、climactic move 和 transition evidence，并结合 session open、前一时段高低点、较大周期位置和 follow-through 更新判断。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-OPENING-REVERSALS-2017` 与 `SRC-PATTERNS-OPEN-2018`。
