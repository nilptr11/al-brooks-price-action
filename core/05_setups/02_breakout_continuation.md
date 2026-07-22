# 突破延续 Setup

> **状态：Core / Application**
>
> 本文只说明怎样把 breakout event 与 acceptance evidence 组成不可直接执行的延续交易原型；具体进入时点和订单规则由策略页实例化。

## 交易命题

突破延续 Setup 押注市场正在或已经接受旧边界外的新价格，而不是交易“高低点刚刚越界”这一事实。

Breakout 的最低定义和强度线索见[突破和突破模式](../01_market_cycle/03_breakouts_and_breakout_mode.md)，follow-through 与 acceptance 的定义见[接受、失望与失败证据](../03_acceptance_and_order_logic/01_acceptance_and_failure.md)。本页只负责把这些事实组成交易：

```text
清楚旧边界 -> 强突破收在边界外
           -> follow-through 或回踩守住
           -> 旧区域未被重新接受
           -> 向新区域继续、形成第二腿或测试结构目标
```

还要确认新区域保留足够目标空间，能够补偿较差 entry 和真实 structure stop。

## 两种风险承担时点

- **预判版本**：在 breakout mode 初始 stop entry，或在强 breakout bar 收盘附近进入。确认较少，不能借用后续 acceptance evidence 的概率。
- **确认版本**：等待 follow-through、回踩守住或 failed failure 后再次触发。确认增加，但 entry 更差、stop 可能更远、剩余目标更近。

两种版本是两份不同 Trade Plan，必须分别使用自己的 entry、stop、概率和 target。

## Premise 失效与 Stop 差异

多头 premise 是旧边界上方的新价格获得接受。单纯回测突破点不构成失败；价格明确回到旧区域并在其中获得反向跟进时，延续 premise 才失效。空头镜像。

- 直接追随强 breakout 时，完整 breakout leg 外可以提供初始 price-action stop。
- Breakout pullback 可用回踩 swing 或足以证明旧区域重新接受的边界作为 stop 锚点。
- Failed failure 再次触发时，反方收回尝试的完整极值只有在能否定当前接受结构时才构成 stop。

最近一根 K 线外、gap 中点或 breakout point 本身都不是跨图表固定 stop。

## 结果与目标差异

Breakout 的最低预期只是继续一点；强 breakout 才常支持至少第二腿或 measured move。量度对象必须在当时可见并固定，例如被突破区间/形态的高度、清楚 breakout leg 的大小，或回调后的 Leg 1 = Leg 2。

Gap、body gap 和 micro measuring gap 主要提供强度与接受证据，只有同时构成清楚支撑阻力或量度参照时才进入目标计算。通用投射方法和目标区域边界见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)。

## 主要误读

- 把单次越界当成新价格已被接受。
- 把确认版本的概率套给预判版本的 entry。
- 忽略完整 breakout leg 所要求的真实 stop 距离。
- 为凑 reward/risk 跳过前方强障碍。
- Breakout 失败后机械反手，而不建立新的反向 Setup。

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-10-PATTERNS`、`SRC-STOP-ORDERS`、`SRC-STRONG-LEGS-2016`、`SRC-BREAKOUTS-2025` 与 `SRC-LIVE-TR-BO-2021`。
