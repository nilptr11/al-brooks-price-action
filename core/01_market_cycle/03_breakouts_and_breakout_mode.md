# 突破和突破模式

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## Breakout Event / Attempt

Breakout event 的最低定义只是：当前 K 线高点或低点越过某个重要价位，例如前高低、某根 K 线极值、趋势线、通道线或交易区间边界。在新价格是否获得接受仍未知时，把这个事件视为 breakout attempt；它本身不说明基础状态已经从 trading range 变成 trend，也不等于趋势中的 breakout phase。

因此“发生突破事件”和“突破获得接受”必须分开。收盘在边界外、大趋势实体和后续跟进会逐步支持市场接受新价格；若随后出现回踩，守住突破点是额外证据。

## 本仓库的分层口径

“获接受的突破 / accepted breakout”是本仓库为了避免职责混写而使用的状态标签，不是 Brooks 官方 glossary 中一个统一、独立的词条。它把可观察过程分成三层：

1. `breakout event / attempt`：价格越过重要价位，结果尚未知。
2. `接受证据累积`：收盘在外、follow-through、旧区域未被快速重新接受，必要时再加突破测试守住。
3. `breakout phase / spike`：证据已足以形成持续方向控制，成为 trend 的阶段。

这套分层是仓库综合 glossary 的 breakout / follow-through 定义和课程逐 K 线判断后的组织方式。引用 Brooks 原话时仍使用具体原术语；“获接受”只表示证据状态，不给交易许可，也不要求先发生回踩。

最低 breakout event / attempt、接受证据，以及趋势中的 breakout phase（spike）是不同粒度：第一层只要求高低点越过重要价位；第二层要求新价格得到收盘、follow-through 或没有快速收回等证据支持；第三层要求这些证据进一步形成持续方向控制，因此属于 trend 的阶段。可交易 breakout pattern 更强调 trend bar、收盘越过 support/resistance、follow-through 和新价格是否被接受，但仍须结合 Context 才能形成 Setup。回踩守住可以加强判断，却不是 breakout event 发生或接受证据成立的必要步骤。

## 突破质量

突破获得接受的常见线索：

- 大趋势 K 线。
- 强收盘。
- 较少重叠。
- 较少反向影线。
- 后续跟进。
- 回踩守住突破点。
- 反方无法快速收回。

没有跟进的 breakout event 仍只是尝试。快速回到原区域时，追随突破者容易被困。即使局部突破已获得接受，也只有当方向控制足以改变主要运动时，才把它提升为 trend 中的 breakout phase（spike）。

Follow-through、旧区域重新接受和 trade failure 的结果边界见[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)；把突破组成具体交易命题见[突破延续 Setup](../05_setups/02_breakout_continuation.md)。

## Breakout Pullback 与 Breakout Test

Breakout pullback 是突破事件后的回调；breakout test 更具体地测试原边界、突破价或相关入场区域。测试可以很快发生，也可以延后许多根；它不是 breakout event 已发生或新价格已获得接受的必要条件。回调守住旧边界会增加接受证据。Failed breakout 则要求突破尝试缺乏接受并明确回到或重新接受旧区域；仅仅没有立即跟进，还不足以确认失败。

## Surprise 和 Inertia

强且获得接受的突破常构成 surprise，因此 surprise 与后续惯性可以加强突破质量判断；它们不是 breakout event 或 accepted breakout 的必要定义。Surprise、惯性以及“常再尝试第二腿但不保证直线运动”的通用边界，统一由[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md#follow-throughsurprise-和惯性)定义。

## Breakout Mode

突破模式是任一方向突破都可能获得跟进的双向候选状态。它是叠加在现有 market-cycle 判断上的跨层信息，不是与 trend / trading range 并列的第三种基础状态，也不是已经发生的 breakout event 或已经形成的 breakout phase。三角形、窄幅震荡、连续内包 K 线、ii、ioi、oo 和双向反转都可能构成；波动压缩很常见，但不是定义本身。

官方 glossary 直接把 breakout mode 称为一种 `setup`。本仓库的 [Setup](../05_setups/00_what_is_a_setup.md#setup-的定义) schema 还要求写明具体 Context、premise、触发、失效事实和直接预期，因此在仓库职责上先把 breakout mode 记为双向候选，再由具体策略实例化。这是同一个概念在 Brooks 宽泛 setup 用语与仓库严格 Setup 层之间的翻译，不是否定官方词条。

突破模式的重点不是预测方向，而是等待市场表态：

- 突破是否强？
- 是否有跟进？
- 是否回到压缩区？
- 首次突破是否失败？
- 失败后反向是否更强？

Breakout mode 只说明任一方向的突破都有获得跟进的可能，不保证首破获得接受，也不等同于普通窄幅外观。按仓库的严格层级，只有加入具体 Context、premise 与入场依据后，它才形成一项可审计 Setup。Triangle 的“方向约对半、首破也常失败”等数字只适用于相应语境，不能复制给所有 breakout-mode 候选。

## 常见误读

- 在突破模式中提前假设方向。
- 把首次 breakout event 当成必然会获得接受。
- 在没有目标空间时追随突破。
- 忽略突破失败后被困交易者的力量。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-ABBREVIATIONS`、`SRC-10-PATTERNS`、`SRC-OPENING-REVERSALS-2017`。
