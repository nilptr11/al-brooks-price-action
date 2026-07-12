# 交易区间 Fade Setup

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../../README.md#权威层级)。

## 它解决什么问题

Trading range fade 试图在区间边缘反向入场。它依赖市场仍在围绕公平价格交易，而不是已经接受突破。

## 判断重点

- 区间是否真实存在。
- 价格是否接近边缘，而非中部。
- 突破或边缘测试是否缺乏跟进。
- 是否出现反向强度。
- 目标到中轴或另一侧边缘是否足够。

## 常见形态语言

- Failed breakout。
- Double top / double bottom。
- Wedge at edge。
- Signal failure。
- Trapped breakout traders。

这些都不是独立信号，必须服务于区间 fade 的完整交易想法。

## 管理

区间 fade 更偏 scalp 或小 swing。第一目标常是区间中轴。只有反向强度足够、目标空间足够时，才考虑区间另一侧。

止损通常在 failed breakout 极值、区间边缘或能证明突破已被接受的结构外。较近的确认型 stop 与更宽的 limit / scale-in stop 是不同方案；后者必须用更小仓位承受完整测试，不能成交后才放宽。

中轴、开盘价、均线和前 swing 都可能代表公平区域。它们是比“区间另一侧”更早出现的现实兑现候选；measured move 可以提供汇合或说明突破方目标，但不能把回归公平区域的交易自动改写成反向趋势。

如果突破强且有跟进，fade 想法失效。

成熟宽区间边缘可以有小仓 limit probe，也可以等待 failed breakout 后的 stop entry；两种入场的确认程度、价格、止损和概率不同，必须分别评估 Trader's Equation。区间中部回避，紧区间若扣除成本后没有足够 scalp 空间，多数交易者应等待。

来源审计见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-TRADING-RANGES`、`SRC-STOP-ORDERS` 与 `SRC-STRONG-LEGS-2016`。
