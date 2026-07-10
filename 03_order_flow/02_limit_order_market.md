# Limit Order Market

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../README.md#权威层级)。

## Brooks 语境中的定义

Limit order market 是限价单交易者主导的环境。交易者愿意在价格朝不利方向移动时入场，期待价格回到公平价格或区间内部。

它常见于 trading range、宽通道和弱趋势。

## 常见语言

- Buy below：在当前价格下方买入。
- Sell above：在当前价格上方卖出。
- Buy low, sell high, scalp。
- 在区间边缘 fade 突破。

限价入场能获得更好价格，但确认更少，管理要求更高。

## 交易含义

Limit order market 中，强 K 线突破不一定代表趋势开始。很多突破只是区间腿的末端，随后缺乏跟进并回到区间内。

交易者必须提前知道：

- 共同 outer stop 和计划最大账户损失。
- 是否允许分批入场。
- 如果继续不利运动，哪里证明想法错了。
- 第一目标是否足够近且现实。

成熟宽区间的清晰边缘可以支持小仓 limit probe；区间中部应回避。紧区间若高度不足以支持扣除成本后的 scalp，多数交易者应等待 breakout，而不是用加仓制造空间。

## 常见误读

- 把限价入场当成摊平亏损。
- 在趋势环境里逆势 buy below 或 sell above。
- 只因价格“便宜”或“贵”就入场。
- 忽略成功突破会让区间 fade 失效。

来源审计见 `reference/official_sources.md` 中的 `SRC-TRADING-RANGES`、`SRC-STOP-ORDERS`，以及 `reference/audit_matrix.md`。
