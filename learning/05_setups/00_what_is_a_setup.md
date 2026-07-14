# 什么是 Setup

> **状态：Learning / Non-normative**
>
> 用于概念学习；价格行为结论由本页、相关学习专题与来源共同支持。

## Setup 的定义

Setup 的最低定义是：由 context 和一根或多根 K 线构成、可作为放置入场单依据的 pattern。订单实际成交后，setup 的最后一根才成为 signal bar；成交所在 K 线是 entry bar。

因此，setup 比孤立形态多了 context 和入场依据，但它本身不等于完整交易。一个 wedge、H2 或 double bottom 可以只是 pattern；当交易者把它放回 context，并据此准备入场单时，才形成 setup。

## 从 Setup 到交易

Setup 提供 context 和入场依据，但交易者还需要决定：

- Market cycle。
- Context 和 location。
- 方向理由。
- 触发点。
- 合理的 protective stop。
- 与该 setup 对应的 profit target。
- 管理方式。
- Trader's Equation。

这些决定共同形成交易计划；其中的概率、风险和回报再由 Trader's Equation 检查是否匹配。它们不是 setup 定义的一部分，但如果风险、目标或管理方式仍不清楚，交易仍没有被完整描述。

## 本章统一结构

后续页面都说明同样几项关系，避免只给形态名称或方向判断：

```text
背景与位置 -> setup 结构 -> entry
           -> reasonable protective stop -> setup 对应 target -> management
```

- **Setup 结构**回答价格必须形成什么关系；例如趋势中的回调未破坏主要 swing、区间边缘的突破失败，或 MTR 的通道突破与旧极值测试。
- **入场触发**回答订单依据是什么；它不能代替完整结构。
- **Protective stop**使用这类 setup 的合理 price-action stop。Signal bar、pullback、major swing、breakout leg 或 range 结构都可能提供 stop，具体取决于交易按 scalp 还是 swing 管理。
- **Profit target**来自 setup 的典型价格行为结果、support/resistance、magnets 和 Trader's Equation，不存在适用于所有 setup 的“第一”或“延伸”层级。

## 目标如何确定

Pattern 名称本身不会生成固定目标。同一个 H2、wedge 或 breakout 会因为 market cycle、位置、强度和交易者选择 scalp 还是 swing 而使用不同目标。目标判断要依次回答：

1. **这个 setup 正在押注什么价格结果**：趋势旗形押注原趋势恢复；强 breakout 常押注继续形成 measured move 或至少第二腿；交易区间 fade 押注区间内轮动；MTR 押注形成反向 swing。
2. **这种 setup 通常有什么幅度或路径预期**：例如 moving-average gap bar 后常测试旧趋势极值，强 breakout 后至少第二腿，MTR 常以 TBTL 和 swing profit 为一般目标。时间/腿数预期不等于价格目标。
3. **前方有哪些 targets 和 magnets**：前高前低、区间边缘、趋势线与通道线、均线、breakout point、opening price、measured-move projection，以及真正相关的 gap 边界都可能成为支撑阻力或兑现位置。
4. **这笔交易按 scalp 还是 swing 管理**：区间和部分 H2/L2 常被 scalp；趋势足够强时可 swing。Swing 通常要求潜在 reward 至少约为 initial risk 的两倍；高概率强 breakout 可以接受较小 reward/risk，但必须使用同一份 entry、stop 和目标重新计算 Trader's Equation。

目标依据不限于某一种工具。Gap 只在它实际改变强度、接受/拒绝、支撑阻力或路径时使用；measured move 只在参照结构和投射起点清楚时使用。与当前 setup 无关的依据不必加入计划。

本章选取趋势 flag、breakout、trading-range fade、MTR 和 second entry 等常见主题作对照，不把它们宣称为穷尽所有 setup 的固定分类。常见目标构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)，完整计划与成交后管理见[从 Setup 到交易计划](../06_trade_management/00_trade_plan.md)。

## Setup、Pattern 和 Trade Plan

Pattern 描述市场行为，例如 H2、wedge、double top。Setup 是带 context、可作为放置入场单依据的 pattern。Trade plan 再把失效、protective stop、仓位、目标、管理和 Trader's Equation 固化下来。

同一个 pattern 可以支持不同 setup，也可以完全没有交易价值；同一个 setup 也可能因为合理 stop 太远、现实 target 太近或成本影响而得不到正的 Trader's Equation。

## 同一笔交易中需要保持一致的关系

看到可能交易点时，需要把以下关系放在同一个方案中理解：

- 当前 market cycle、context 和位置怎样支持这个 setup。
- 哪些可观察价格行为构成 setup 和具体入场条件。
- 这类 setup 的合理 protective stop 在哪里，哪些回调仍属正常测试。
- Profit target 是 scalp、旧极值、区间内部位置、measured move 还是反向 swing，以及依据是什么。
- 触发后哪些新证据继续支持原 premise，哪些证据使它失效。
- 概率、风险、回报、成本和仓位是否来自同一方案，并满足 Trader's Equation。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-RISK-113`、`SRC-BREAKOUTS-2025` 与 `SRC-MTR-2025`。
