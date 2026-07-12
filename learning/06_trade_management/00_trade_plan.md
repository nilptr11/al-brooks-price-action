# 从 Setup 到交易计划

> **状态：Learning / Non-normative**
>
> 本文解释完整交易想法的组成，不定义订单动作；实际执行只见当前[执行手册](../../EXECUTION_MANUAL.md)。

## Setup 仍不是完整交易

Setup 提供 context 与入场依据，但交易还必须把 entry、premise 失效、protective stop、目标、仓位和管理放进同一个方案。缺少其中任何关键部分，都只能等待或继续设计。

一份计划至少回答：

- 当前是什么市场状态和位置？
- 正在验证哪一种交易想法？
- 什么具体行为构成 entry？
- 什么事实说明 premise 已错？
- Protective stop 和仓位如何限制最坏结果？
- 第一现实目标是否足以补偿风险？
- 正常回调、目标、反向强突破和时间退出分别如何管理？

## 从失效事实到 protective stop

需要分开四层：

1. **Premise 失效事实**：交易想法不再成立的市场行为。
2. **结构锚点**：代表该事实或灾难边界的 signal bar、pullback、swing、突破腿或区间边缘。
3. **Stop 触发价**：实际经纪商 protective-stop 订单价格。
4. **保守 stop fill**：计入滑点后用于计算仓位和最坏结果的价格。

Signal-bar stop、完整结构 stop 和 wide structural stop 可以都合理，但它们是不同交易方案。每个方案都要重新评估 entry、仓位、目标空间和概率，不能拿窄 stop 的仓位配宽 stop 的存活率。

合理 stop 太远时，缩小仓位、等待或放弃；不得为了得到漂亮 R 倍数把 stop 塞进正常波动，也不得成交后向风险方向移动。

## 第一现实目标

目标不是愿望，而是 Trader's Equation 的输入。先沿交易方向列出最近的重要支撑阻力和路径障碍，再决定第一笔真实退出会发生在哪里。

Measured move、另一侧区间边缘或 runner 都可能是更远候选，但不能静默越过近端障碍来修复数学。Measured move 的常见构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)；它不是每笔计划的必填项，也不保证到达。

## 仓位与真实风险

仓位应服从合理 stop 距离和用户预设的损失边界。计算使用保守 entry、保守 stop fill、真实数量以及尚未嵌入价格的成本。

成交后必须用真实 fill、真实数量和 active stop 检查风险。市场出现更远结构不构成放宽 stop 的许可；若 premise 已失效，应退出并为下一笔机会重新建立计划。

## 成交后的管理

计划用于防止临场扩大风险，不用于拒绝新信息：

- 原 premise 仍成立、只是正常 pullback 或短暂 disappointment：按原 scalp/swing 方式管理。
- 目标、trailing 或时间条件成立：按计划处理对应数量。
- 强反向突破、持续反向跟进或其他事实使 premise 不再成立：及时退出，不因该情形没有逐字预写而继续依赖希望。

可以提前写常见条件以降低情绪干扰，但不允许放宽 stop、拉远目标、临时加仓或把失败交易改名成另一种交易。

来源和审计状态见 [`reference/official_sources.md`](../../reference/official_sources.md) 与 [`reference/audit_matrix.md`](../../reference/audit_matrix.md)。
