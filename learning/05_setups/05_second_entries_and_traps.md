# 二次入场和陷阱

> **状态：Learning / Non-normative**
>
> 用于概念学习；价格行为结论由本页、相关学习专题与来源共同支持。

## 定义

Second entry 的最低定义是：第一次 entry 后的数根内，市场基于同一逻辑第二次形成 entry bar。若第二次只形成 setup、订单尚未成交，则更准确地说是 second signal。

Second entry 不表示“第二次一定成功”。它是订单事件；反方再次失败、被困和控制权变化是它可能产生交易意义的原因，不是定义本身。

因此，second entry / trap 不是与趋势延续、区间 fade、突破延续或 MTR 并列的独立交易命题。它主要描述**触发顺序和失败机制**；stop 与目标必须继承它所服务的上层 setup。

## First Entry

第一次入场是市场在回调或反转后第一次尝试恢复某个方向。强趋势中第一次入场可能足够；在通道、交易区间或反转环境中，第一次入场经常失败。

第一次多头入场通常通过 buy stop 触发。第一次空头入场通常通过 sell stop 触发。

## Second Entry

第二次入场发生在第一次 entry 后不久，市场再次以同一逻辑实际触发入场。H2 和 L2 是典型 second-entry 语言。

第一次通常缺乏跟进、回撤或失败，才会产生第二次机会；但不要求第一次先触发 protective stop。真正的 second entry 必须有第二次实际 entry bar，不能只凭外观数到“二”。

## Failed Second Entry

失败的二次入场可能很重要，但“立刻令人失望”不等于已经形成 failure 或已经被困。先按[接受、失望与失败证据](../03_order_flow/00_acceptance_and_failure.md)区分 entry disappointment、premise 变化和实际 failure。

- 实际失败的 H2 可能成为空头机会。
- 实际失败的 L2 可能成为多头机会。

它们常出现在 trading range、趋势后期或反转过程中。

## 结构骨架

顺原方向的 second entry：

```text
上层 context 支持某方向 -> 第一次 entry 实际触发但缺乏延伸
                       -> 正常回撤，原 premise 尚未失效
                       -> 同一逻辑形成第二次 signal 并实际触发
```

交易反方失败的 trap：

```text
反方第一次 / 第二次 entry 触发 -> 未先获得原目标或 scalper's profit
                              -> 价格到达其 protective stop，确认 failure
                              -> 当前 context 支持的反方向另行形成 setup 和触发
```

“第二次”只描述 entry 次序。“陷阱”还要求有可观察的开放亏损和退出压力；即使确认反方 failure，也仍要重新检查当前 market cycle、位置和反方向目标，不能机械反手。

## Premise 失效和止损

Second entry / trap 本身不规定 protective stop。先选定它所服务的上层 premise，再按该价格结构确定锚点：

- 趋势延续中的 H2/L2 需要使用 correct swing stop；最近 major swing 或完整回调极值可以是 price-action 锚点，但不是所有 H2/L2 的固定 stop。
- 区间边缘的 second signal 仍使用 reasonable stop，且有时必须较远；failed-breakout 完整极值只有在足以代表 fade premise 失效时才是合格锚点。
- MTR 中的第二次测试，stop 通常在旧趋势极值测试或完整反转结构外。
- Failed H2/L2 的反向交易需要另建反向 premise；原入场者的 stop 位置不能自动充当新交易的 protective stop。

Signal-bar stop 只有在其另一端同时就是完整上层 premise 的失效点时才够用。第一次 entry 尚未触发 protective stop，并不妨碍出现 second entry；但若上层 premise 已经失效，就不能继续把下一次触发数成同一 setup。

## 价格行为预期与 Profit targets

Second entry 只定义同一逻辑的第二次实际触发，trap 只描述失败与持仓压力；两者都没有独立的 profit-target 公式。目标必须回到它们所处的 setup 和 market cycle：

| 上层语境 | 常见价格行为预期 | 常见 profit targets |
| --- | --- | --- |
| 趋势延续 H2/L2 | 反趋势方第二次尝试失败后，原趋势通常较快恢复 | 经常按 scalp 管理；趋势仍强时才 swing，并使用旧极值、前高低和其他 magnets |
| 强 breakout 后二次腿 | 强 breakout 后至少第二腿是 minimum goal | 使用第一腿/第二腿、breakout 大小、区间/形态高度和前方支撑阻力 |
| 区间边缘 second signal | Failed breakout 后恢复区间内轮动 | Buy low, sell high, scalp；在区间内部的合理利润位置或上/下半区兑现 |
| MTR 第二次测试 | 第二次反转尝试发展为反向两腿和 swing profit | TBTL 是路径预期；价格目标需提供约 2R 空间并落在真实 magnets 上 |
| Failed H2/L2 的反向交易 | 原方向失败只生成新的反向候选 | 先重新归类为区间 fade、MTR、突破或趋势恢复，再使用该 setup 的目标逻辑 |

Gap、measured move、旧极值、均线、区间边界或 actual-risk scalp 都可能在某个具体版本中相关；它们来自上层 context，不来自“第二次”这个计数本身。

## 读图问题

判断二次入场时要问：

- 第一次 entry 是否实际发生，触发点是什么？
- 第一次只是弱跟进，还是已经形成可确认的失败结果？
- 第二次触发是否更强？
- 哪些可观察价格和退出边界支持 trapped-trader 推断？
- 当前 market cycle 是否支持这个方向？
- 这个 second entry 属于什么 context，其 reasonable stop 和 profit target 分别是什么？

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-10-PATTERNS`、`SRC-TREND-CHANNELS`、`SRC-TRADING-RANGES`、`SRC-STRONG-LEGS-2016`、`SRC-BREAKOUTS-2025`、`SRC-MTR-2025` 与 `SRC-PATTERNS-OPEN-2018`。
