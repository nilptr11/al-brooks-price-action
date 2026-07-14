# Major Trend Reversal

> **状态：Learning / Non-normative**
>
> 用于概念学习；价格行为结论由本页、相关学习专题与来源共同支持。

## 定义

Major trend reversal 不是单根 K 线或单个外观，而是原趋势失去控制、反方尝试建立新方向的过程。完整 setup 包含对原趋势通道/趋势线的突破，以及对旧趋势极值的测试。交易者是在新趋势明确前入场，因此早期概率通常不高。

早期 MTR 即使看起来很好，swing 概率通常也只有约 40%。等待反向强突破后，典型 swing 概率可提高到约 60%，但代价是止损更远、剩余回报更小。这是 MTR 的典型概率交换，不是所有反转的固定胜率。

## 结构骨架

以牛转熊为例，熊转牛镜像：

```text
成熟牛趋势 -> 反向突破牛通道 / 趋势线
           -> 多头回探旧高或形成更低高点
           -> 测试失败并出现空头触发
           -> 反向两腿或更大的交易区间
```

常见组件包括：

- 成熟趋势。
- 反向运动明确突破原趋势通道或趋势线。
- 原趋势恢复并测试旧极值。
- 第二次回调或测试逐渐发展成反向趋势。
- 回探原极值失败或形成更低高点 / 更高低点。
- 双边交易增加。
- 反向运动有足够目标空间。

通道突破、旧极值测试和反向 signal 是完整过程中的核心关系。若只有 climax、wedge、final flag 或一根强反转 bar，仍只是提前控制权转移候选；若只有通道突破而没有测试，也还不是完整 MTR。

## 四类常见变体

Higher high MTR：牛趋势中突破前高后失败，形成更高高点反转。

Lower high MTR：牛趋势或上涨通道后，回探未能到达或突破前高，在较低高点形成卖压。

Lower low MTR：熊趋势中跌破前低后失败，形成更低低点反转。

Higher low MTR：熊趋势或下跌通道后，回探未能到达或跌破前低，在较高低点形成买压。

这些名称不重要，重要的是原趋势方是否失去控制，反方是否获得跟进。高潮式推进、已经形成的 climax、wedge、final flag 或单根强反转 bar 都可以提供背景，但不能替代通道突破、旧极值测试和反向 signal 组成的过程。

## Premise 失效和止损

牛转熊 premise 是“原牛趋势已经失去控制，旧高测试失败，空头将建立至少一个可持续 swing”。若价格越过并重新接受旧趋势极值，否定该次测试失败，或原趋势以强突破和 follow-through 重新建立控制，premise 失效；熊转牛镜像。

Protective-stop 锚点取决于入场时点：

- **早期反转**：stop 通常在旧趋势极值测试或完整反转结构外。若价格仍可能正常再次测试旧极值，不能把 stop 只放在一根小 signal bar 外。
- **强反向 breakout 后确认入场**：stop 可以在反向趋势形成的 major higher low / lower high、回踩结构或完整反向 breakout 起点外；必须以所依赖的新结构为锚点。

等待确认可能提高概率，但 entry 更差、stop 可能更远、剩余回报更小。早期和确认路线必须分别评估，不能使用早期 entry、确认后的概率和较窄 signal-bar stop 拼成一份计划。

## 价格行为预期

成功 MTR 应形成两腿并获得 swing profit，而且通常先演变为较大的 trading range，而不是立即变成无回调新趋势。TBTL 是反转 swing 的 general goal；swing 的潜在 reward 通常至少约为 risk 的两倍。

这两项必须分开：

- **TBTL** 是对持有时间和价格路径的经验预期，提醒交易者不要在第一小腿过早退出；它不是一个价格坐标，也不表示必须机械等待十根。
- **Swing profit / 约 2R** 是 Trader's Equation 需要的回报条件。价格目标仍要落在图上的实际支撑阻力或其他 magnet，不能只写“等两腿”。

等待反向强 breakout 后入场时，典型概率可从约 40% 提高到约 60%，但 stop 更远、剩余 reward 更小。若反向 breakout 或后续两腿形成清楚的量度结构，可以加入相应 measured move；MTR 本身没有固定的量度公式。

## Profit targets

1. 早期 MTR 通常是约 40% 概率的 swing，因此需要足够大的潜在 reward。约 2R 是常见的 swing 目标关系，但具体价格仍应落在均线、前 swing、区间边界、measured move 或更大周期 support/resistance 等真实 magnets 上。
2. 均线、前 swing 或旧公平区域可以是部分兑现位置；若全部目标只到这些区域，计划验证的是 minor reversal profit，而不是两腿和 swing profit。
3. 确认版本按更差 entry、较远 stop 和新的反向结构重新计算；若反向 breakout 清楚，才加入 breakout-size、Leg 1 = Leg 2 或其他 measured move。
4. 趋势末端 gap、exhaustion、wedge 或 final flag 主要提供 context 和可能的反转位置。除非它们在当前图上形成可计算的 magnet，否则不直接决定 MTR profit target。

看到第一根反向强 K 线就期待完整新趋势，是常见错误。

“提前下注控制权转移”和完整 MTR 是不同计划版本；早期候选不能直接视为完整 MTR。若目标只到均线、区间中轴或旧公平区域，应按 minor reversal 或回归公平区域理解，而不是反向 swing。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-MTR-2025` 与 `SRC-PATTERNS-OPEN-2018`。
