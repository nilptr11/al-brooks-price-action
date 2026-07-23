# 交易区间（Trading Ranges）

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## 定义

Trading range 是市场围绕公平价格上下测试的状态。多空双方都能赚钱，方向优势下降，区间中部通常缺少优势，边缘更容易形成交易结构。

交易区间不是简单震荡，也不是无条件均值回归。它是双方都能构造理由、但都无法持续控制的环境。

## 基本行为

交易区间中的基本思想是 buy low, sell high, scalp。顶部的强上涨可能诱多，底部的强下跌可能诱空。课程对普通 trading range 给出的经验先验是：约 `80%` 的单次 breakout attempts 会失败；突破获得接受并形成方向控制后，基础状态才可能更新为 trend，市场会寻找新的公平价格区。

这里的分母是“区间内的一次突破尝试”，不是“区间最终是否突破”。只有当区间已经发展到前序趋势影响明显衰减、市场趋于中性，或多空 swing setup 并存而进入 breakout mode 时，课程才把两个突破方向简化为接近 `50/50` 的候选先验。它不是所有 trading range 的固有属性：短区间仍可能受前序趋势影响，当前位置、既有突破尝试和更高周期背景也会改变方向偏置。`50/50` 只描述方向不确定，不能证明任一侧的具体 entry、stop 和 target 都具有相同期望。

成熟区间最终会突破，但这一事实不给出可交易时点。普通区间中约 `80%` 的单次尝试失败，也不能直接套到已经进入 breakout mode 的决断阶段；两个比例的事件和观察窗口不同。

交易区间经常看起来像马上要突破。强上涨腿可能只是测试上沿的 vacuum，强下跌腿也可能只是测试下沿的 vacuum。经验不足的交易者最容易在这些腿的末端追随。

### 强区间腿与第二腿陷阱

区间内部的强腿常让交易者预期还会有第二腿，但“第一腿很强”不等于市场已经接受区间外的新价格。若运动仍未清楚突破区间、区间内已经完成一段或两段同向运动，或边缘突破缺少 follow-through，所谓第二腿可能只是测试边界的最后一段，并形成追随者陷阱。

这不表示看到第二腿就应机械反向。关键仍是区分：价格是否真正离开区间并在外部获得接受，还是只在公平区域内完成另一段双向轮动。第二信号、第二入场和 trap 的次序边界见[二次入场和陷阱](../03_acceptance_and_order_logic/03_second_entries_and_traps.md)。

## Tight Trading Range 和 Barbwire

紧密交易区间重叠多、空间小、方向不清。信号质量通常低，因为没有足够目标空间和跟进。

Barbwire 是三根以上大量重叠的 K 线组合，带显著影线且至少包含一根 doji。K 线本身可以相对较大；关键不是“全部小实体”，而是重叠、影线和双向冲突让 stop entry 很难获利。经验不足的交易者更适合等待市场脱离该区域。

## Broad Trading Range

宽交易区间有更大波动，边缘可能提供交易机会。重点是位置、失败、反向强度和目标空间。

中部交易通常没有优势，尤其应避免在区间中间三分之一追逐普通信号。如果必须堆很多理由证明中部交易成立，通常说明交易本身不够清晰。

边缘回归如何形成交易命题见[交易区间 Fade Setup](../05_setups/03_trading_range_fade.md)，限价单占优时的订单行为见 [Limit Order Market](../03_acceptance_and_order_logic/02_limit_order_market.md)。

## 区间突破

区间边界被越过时，先把它视为突破尝试。突破事件和质量由[突破和突破模式](03_breakouts_and_breakout_mode.md)定义，触发后的接受证据由[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)定义；本页只说明这些结果怎样改变原 trading-range 判断。突破获得接受不要求先回踩，没有回踩本身不构成失败。

如果突破后缺乏跟进并快速回到区间内，突破尝试可能形成 failed breakout，追随者也可能被困。若这一反向尝试又失败，则可能形成 failed failure，并引发更强运动。这里的 failure 描述价格运动，实际 trade failure 的结果边界见[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md#disappointmentpremise-变化和-trade-failure)。

获接受的突破怎样升级为趋势阶段见[突破和突破模式](03_breakouts_and_breakout_mode.md)，怎样组成交易命题见[突破延续 Setup](../05_setups/02_breakout_continuation.md)。

## 常见误读

- 把所有区间都当均值回归。
- 在区间中部追随普通信号。
- 看到单根强突破 K 线就认定基础状态已经转为 trend。
- 忘记成熟区间最终也会突破。

- [`SRC-GLOSSARY`](../../reference/official_sources.md)、[`SRC-TRADING-RANGES`](../../reference/official_sources.md) 与 [`SRC-10-PATTERNS`](../../reference/official_sources.md)：trading range、TTR、区间位置与突破边界。
- `SRC-COURSE-01-36`：课程 12B–12C、13A、17A–17B、18A–18F、19A、28；趋势影响衰减、普通区间/BOM、BLSHS、TTR、vacuum 和 endless pullback。
- `SRC-COURSE-37-52`：课程 37A–37B、39C、42C、47A–47D、49A–49E；BOM 的方向先验、第二腿陷阱、限价单环境和成功突破后的逻辑切换。
