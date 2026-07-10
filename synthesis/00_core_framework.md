# 核心压缩框架

> **状态：Research / Non-normative**
>
> 本文只做学习概念压缩，不定义执行状态；完整 M/K/C/T/D/Q/P/E/A、订单边界和管理配置以当前[执行手册](../README.md#权威层级)为准。

## 总结结论

Brooks 文档里大量概念可以压缩成一条主链条：

```text
Market Cycle
-> Control / Always In
-> Location / Target
-> Trigger / Order Flow
-> Initial Contract: Invalidation / Stop Anchor-Trigger-Fill / Size / Target Zone-Exit Price / Management
-> Entry Trader's Equation
-> 允许下单 / 已挂单 / 部分或全部成交
-> Follow-through or Failure / Trapped Traders
-> Live State / Hold Trader's Equation
-> Hold / Reduce / Exit / New Candidate
```

这条链条比单独记形态更重要。形态名称只是在描述市场行为，真正决定是否交易的是这条链条是否完整。

Follow-through、failure 和 trapped traders 是市场结果，不依赖观察者是否成交；零成交时它们更新候选或已挂订单，已有仓位时才进入持仓数学和动作选择。

这条链条不是一次性的线性流程，而是逐根 K 线更新的循环。每根 K 线都会增强、削弱或改变原判断。

多周期和时段不是额外指标，而是 context / location 的组成部分。大周期影响背景、目标和关键位置；时段影响流动性、跟进质量和目标是否可达。

## 每一层回答的问题

| 层级 | 核心问题 | 常见误读 |
| --- | --- | --- |
| Market Cycle | 当前首先是 trend 还是 trading range；若是 trend，更像 breakout、tight channel 还是 broad channel？是否叠加 breakout mode 或 climactic behavior？ | 把 channel 当成 trend 之外的并列市场，或先看 signal bar 再倒推环境。 |
| Control / Always In | 哪一边暂时控制市场？优势是否明显？ | 把单根强 K 线当成控制权，或用控制权替代风险回报。 |
| Location / Target | 价格在什么位置，哪些关键结构证据会改变判断，目标空间是否足够？ | 在区间中部追普通信号，把支撑阻力当精确价格线，或为每种可见现象建立强制分析层。 |
| Trigger / Order Flow | 触发点在哪里？谁会入场、退出或止损？ | 只看形态名字，不看订单触发。 |
| Initial Trade Design | 权限、无效点、stop 的结构锚点/触发价/预计成交价、仓位、路径障碍、目标区/保守退出价、初始管理和提前退出是否完整？ | 把 entry 当成完整交易，混用不同 stop 方案，或在没有清晰测量结构时用远端投射跳过近端障碍。 |
| Entry Trader's Equation | 当前整套 entry、stop、目标、管理和成本是否值得承担新风险？ | 用脱离当前价格的胜率或远端目标修复交易。 |
| Order / Fill Boundary | 订单只是允许下单、已经挂出，还是部分/全部实际成交？ | 把通过审查、活动挂单或计划退出数量误记成实际库存。 |
| Follow-through or Failure | 触发后市场是否接受这个方向？ | 突破后没有跟进仍坚持原判断。 |
| Trapped Traders | 如果失败，哪一边会被迫退出？ | 把所有失败都当成反向交易，不看反向强度和目标空间。 |
| Live State / Hold Math | 相对现在退出，active stop、剩余目标、剩余时间和增量持有成本是否仍支持持有？ | 用原 entry、已实现盈亏或沉没成本替当前持仓辩护，或临场拉远目标、补 runner、升级管理尺度来修复 Q_hold。 |
| Action / Management | 当前实际数量应不变、减后仍非零，还是降为零；退出订单是否已经真实成交？ | 把推进止损误记成减仓，把 TBTL 当成独立类别，或把旧仓位直接改名过户。 |

## 最小读图模板

每次复盘或实时读图，只保留这些问题：

1. 当前 market cycle 是什么？
2. 多空谁有控制权？
3. 价格是否在有意义的位置；是否存在会实质改变判断的关键证据，例如相关 gap 或大周期结构？
4. 当前触发会让谁入场或退出？
5. 权限、无效点、stop 锚点/触发价/预计成交价、仓位、目标区/保守退出价、管理和提前退出是否完整？
6. 入场概率、损失、回报和成本是否合算？
7. 订单是允许下单、已挂单、部分/全部成交还是已经终止；实际成交数量是多少？
8. 触发后有没有跟进；如果失败，谁会被困？
9. 从当前价格继续持有是否合算；实际数量应该不变、减后仍非零、降为零，还是在归零后生成新候选？

## 学习含义

学习重点不是扩大术语量，而是减少判断步骤里的模糊地带。

如果一个形态无法放进这条链条，它通常只是描述。Brooks setup 的最低定义是带 context、可作为入场单依据的 pattern；如果它在这条链条上缺了止损、目标或管理，它仍不是本仓库可批准的交易计划。

特别要避免把压缩框架重新变成机械信号。Brooks 文档中的概率语言通常是条件性的：强趋势、强突破或失败信号都只是在特定 context、location、follow-through 和 Trader's Equation 下才有交易意义。
