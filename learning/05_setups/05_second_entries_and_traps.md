# 二次入场和陷阱

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../../README.md#权威层级)。

## Brooks 语境中的定义

官方 glossary 的最低定义是：第一次 entry 后的数根内，市场基于同一逻辑第二次形成 entry bar。若第二次只形成 setup、订单尚未成交，则更准确地说是 second signal。

Second entry 不表示“第二次一定成功”。它是订单事件；反方再次失败、被困和控制权变化是它可能产生交易意义的原因，不是定义本身。

## First Entry

第一次入场是市场在回调或反转后第一次尝试恢复某个方向。强趋势中第一次入场可能足够；在通道、交易区间或反转环境中，第一次入场经常失败。

第一次多头入场通常通过 buy stop 触发。第一次空头入场通常通过 sell stop 触发。

## Second Entry

第二次入场发生在第一次 entry 后不久，市场再次以同一逻辑实际触发入场。H2 和 L2 是典型 second-entry 语言。

第一次通常缺乏跟进、回撤或失败，才会产生第二次机会；但不要求第一次先触发 protective stop。真正的 second entry 必须有第二次实际 entry bar，不能只凭外观数到“二”。

## Failed Second Entry

失败的二次入场可能很重要，但“立刻令人失望”不等于已经 confirmed failure 或已经被困。先按[接受、失望与失败证据](../03_order_flow/00_acceptance_and_failure.md)区分 weak follow-through、tentative failure 和实际失败结果。

- Confirmed failed H2 可能成为空头机会。
- Confirmed failed L2 可能成为多头机会。

它们常出现在 trading range、趋势后期或反转过程中。

## 读图问题

判断二次入场时要问：

- 第一次 entry 是否实际发生，触发点是什么？
- 第一次只是弱跟进，还是已经形成可确认的失败结果？
- 第二次触发是否更强？
- 哪些可观察价格和退出边界支持 trapped-trader 推断？
- 当前 market cycle 是否支持这个方向？
