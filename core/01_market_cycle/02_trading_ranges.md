# 交易区间（Trading Ranges）

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## 定义

Trading range 是市场围绕公平价格上下测试的状态。多空双方都能赚钱，方向优势下降，区间中部通常缺少优势，边缘更容易形成交易结构。

交易区间不是简单震荡，也不是无条件均值回归。它是双方都能构造理由、但都无法持续控制的环境。

## 基本行为

交易区间中的基本思想是 buy low, sell high, scalp。顶部的强上涨可能诱多，底部的强下跌可能诱空。多数区间突破尝试会失败，但成功突破一旦出现，市场会寻找新的公平价格区。

交易区间经常看起来像马上要突破。强上涨腿可能只是测试上沿的 vacuum，强下跌腿也可能只是测试下沿的 vacuum。经验不足的交易者最容易在这些腿的末端追随。

## Tight Trading Range 和 Barbwire

紧密交易区间重叠多、空间小、方向不清。信号质量通常低，因为没有足够目标空间和跟进。

Barbwire 是三根以上大量重叠的 K 线组合，带显著影线且至少包含一根 doji。K 线本身可以相对较大；关键不是“全部小实体”，而是重叠、影线和双向冲突让 stop entry 很难获利。经验不足的交易者更适合等待市场脱离该区域。

## Broad Trading Range

宽交易区间有更大波动，边缘可能提供交易机会。重点是位置、失败、反向强度和目标空间。

中部交易通常没有优势，尤其应避免在区间中间三分之一追逐普通信号。如果必须堆很多理由证明中部交易成立，通常说明交易本身不够清晰。

边缘回归如何形成交易命题见[交易区间 Fade Setup](../05_setups/03_trading_range_fade.md)，限价单占优时的订单行为见 [Limit Order Market](../03_acceptance_and_order_logic/02_limit_order_market.md)。

## 区间突破

区间边界被越过时，先把它视为突破尝试。突破事件和质量由[突破和突破模式](03_breakouts_and_breakout_mode.md)定义，触发后的接受证据由[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)定义；本页只说明这些结果怎样改变原 trading-range 判断。成功突破不要求先回踩，没有回踩本身不构成失败。

如果突破后缺乏跟进并快速回到区间内，突破尝试可能形成 failed breakout，追随者也可能被困。若这一反向尝试又失败，则可能形成 failed failure，并引发更强运动。这里的 failure 描述价格运动，实际 trade failure 的结果边界见[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md#disappointmentpremise-变化和-trade-failure)。

成功突破怎样升级为交易命题见[突破延续 Setup](../05_setups/02_breakout_continuation.md)。

## 常见误读

- 把所有区间都当均值回归。
- 在区间中部追随普通信号。
- 看到强突破 K 线就认定趋势开始。
- 忘记成熟区间最终也会突破。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-TRADING-RANGES`、`SRC-10-PATTERNS`。
