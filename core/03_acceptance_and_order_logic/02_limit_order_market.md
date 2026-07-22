# 限价单市场（Limit Order Market）

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## 定义

Limit order market 是一种可观察的价格行为环境：双边交易者经常能够在价格朝暂时不利方向移动时使用逆向 limit entry，并从价格回到公平区域或区间内部的运动中获利。这个名称是行为模型，不表示我们知道真实订单簿中哪类订单或哪一类参与者正在“主导”。

Limit entry 只允许在指定价格或对交易者更有利的价格成交；它换取的是价格改善，不自动提高成功概率，也不保证能够成交。

它常见于 trading range、宽通道和弱趋势。

## 常见语言

- Buy below：在当前价格下方买入。
- Sell above：在当前价格上方卖出。
- Buy low, sell high, scalp。
- 在区间边缘 fade 突破。

## Fade 与 Countertrend

Fade 押注当前方向的尝试不会获得接受，常在区间边缘使用逆向 limit-order 行为；countertrend 则明确逆当前 Always In 方向。两者可以重叠，但方向不清的 trading range fade 不必属于 countertrend，逆强趋势交易也不能只因称为 fade 就降低风险。

限价入场能获得更好价格，但确认更少，管理要求更高。

## 交易含义

Limit order market 中，强 K 线突破不一定代表趋势开始。很多突破只是区间腿的末端，随后缺乏跟进并回到区间内。

使用 limit entry 时需要知道：

- 首个成交起就能保护持仓的 price-action stop 安排，以及计划最大账户损失。
- 初始计划是否包含分批入场，以及所有计划数量的总风险。
- 如果继续不利运动，哪里证明想法错了。
- Scalp 或 swing target 是否符合当前 range / channel 结构。

成熟宽区间的清晰边缘可以支持小仓 limit probe；区间中部应回避。紧区间若高度不足以支持扣除成本后的 scalp，多数交易者应等待 breakout，而不是用加仓制造空间。

## 常见误读

- 把限价入场当成摊平亏损。
- 在趋势环境里逆势 buy below 或 sell above。
- 只因价格“便宜”或“贵”就入场。
- 忽略成功突破会让区间 fade 失效。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-TRADING-RANGES`、`SRC-STOP-ORDERS` 与 `SRC-SCALE-IN-TRENDS`。
