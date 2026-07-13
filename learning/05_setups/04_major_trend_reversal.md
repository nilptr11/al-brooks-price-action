# Major Trend Reversal

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../../README.md#权威层级)。

## Al Brooks 语境中的定义

Major trend reversal 不是单根 K 线或单个外观，而是原趋势失去控制、反方尝试建立新方向的过程。官方术语表要求 setup 包含对原趋势通道/趋势线的突破，以及对旧趋势极值的测试。交易者是在新趋势明确前入场，因此早期概率通常不高。

官方公开材料里，早期 MTR 即使看起来很好，swing 概率通常约 40%。等待反向强突破后，示例中的 swing 概率可提高到约 60%，但代价是止损更远、剩余回报更小。这是 MTR 的典型概率交换，不是所有反转的固定胜率。

## 基本组件

常见组件包括：

- 成熟趋势。
- 反向运动明确突破原趋势通道或趋势线。
- 原趋势恢复并测试旧极值。
- 第二次回调或测试逐渐发展成反向趋势。
- 回探原极值失败或形成更低高点 / 更高低点。
- 双边交易增加。
- 反向运动有足够目标空间。

## 四类常见变体

Higher high MTR：牛趋势中突破前高后失败，形成更高高点反转。

Lower high MTR：牛趋势或上涨通道后，回探未能到达或突破前高，在较低高点形成卖压。

Lower low MTR：熊趋势中跌破前低后失败，形成更低低点反转。

Higher low MTR：熊趋势或下跌通道后，回探未能到达或跌破前低，在较高低点形成买压。

这些名称不重要，重要的是原趋势方是否失去控制，反方是否获得跟进。Climactic behavior、已经形成的 climax、wedge、final flag 或单根强反转 bar 都可以提供背景，但不能替代通道突破、旧极值测试和反向 signal 组成的过程。

## 交易管理

官方 2025 coaching 材料把成功反转描述为形成两腿并获得 swing profit，且常演变为较大 trading range，而不是立刻形成无回调的新趋势。TBTL 指 Ten Bars, Two Legs correction，是管理时间/腿数的经验语言，不是价格目标。

早期反转的 stop 常需要放在旧趋势极值测试或完整反转结构外。等待强反向 breakout 可以提高概率，但 entry 更差、stop 可能更远、剩余回报也更小；两条路线必须分别评估。

均线、前 swing 和区间中轴可以是部分兑现位置，但它们通常只代表回到公平区域。若交易命题是 major reversal，计划还要有可量化的反向 swing 空间，例如反向 Leg 1 = Leg 2、反转结构高度或其他有依据的 measured move。

看到第一根反向强 K 线就期待完整新趋势，是常见错误。

执行层可以区分“提前下注控制权转移”和“完整 MTR”两种版本，但这不等于把早期候选命名为官方完整 MTR。若目标只到均线、区间中轴或旧公平区域，应按 minor reversal 或回归公平区域理解，而不是反向 swing。

来源审计见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-MTR-2025`。
