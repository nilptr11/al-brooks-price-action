# 交易区间 Fade Setup

> **状态：Core / Application**
>
> 本文只说明成熟区间边缘回归原型的 premise、抽象进入类别、失效结构和特有风险；它不能直接生成订单计划。

## 交易命题

Trading range fade 押注市场仍在围绕公平区域双向交易，边缘突破没有获得接受，价格将恢复区间内轮动。

以区间底部做多为例，顶部做空镜像：

```text
成熟交易区间 -> 测试或短暂跌破下边缘
             -> 向下尝试缺乏跟进 / 重新进入旧区域
             -> 反向触发
             -> 回到区间内部价值区域
```

成立时需要同时确认：区间已经由多次双向测试和重叠建立；entry 位于边缘附近而非中部；突破方未获得接受；到区间内部现实目标仍有空间。Double bottom/top、wedge 或 failed breakout 只描述局部结构，不能替代这些条件。

## Entry 与 Stop 差异

- **确认型 stop entry**：等待突破尝试失败、价格重新进入区间并形成反向触发。Failed-breakout 完整极值只有在再次越过它足以证明突破方向重新获得接受时，才是 stop 锚点。
- **Limit probe / 预先设计的 scale-in**：用更好价格交换更少确认，通常必须容许更深 overshoot。它只说明本 Setup 的进入角色；层数、共同 stop 与全部计划数量的总风险统一由[加仓与减仓](../06_trade_plan_and_management/02_scaling_in_out.md)定义，并在第一笔 entry 前确定。

区间边界不是自动止损线。Reasonable stop 要容许正常边缘 overshoot，同时位于足以否定当前 fade premise 的结构外。更远 catastrophe stop 只能作为后备保护，不能替代对区间外 acceptance 的判断。

## Premise 失效

多头 premise 在价格离开下边缘后形成足够强的向下 breakout，或在突破后出现持续跟进，或再次跌破失败极值并在区间外获得接受时失效；空头镜像。单次轻微越界或只有普通强外观的一根 K 线通常不足以推翻成熟区间的 fade 先验，但异常强的反向 breakout 本身就可以要求先退出；follow-through 会进一步强化失效判断，不能把它误写成任何退出都必须等待的条件。

## 结果与目标差异

核心结果是 buy low, sell high, scalp：从区间边缘回到内部价值区域。Midpoint、均线、opening price、前 swing 和上/下半区都可能是现实目标，但没有一个适用于全部区间的固定价格；是否争取另一侧边缘取决于区间宽度、内部障碍和原管理方案。

区间另一侧发生成功突破后，原 fade premise 已结束；区间高度 measured move 属于新的 breakout 命题。通用目标构造见[支撑阻力与目标](../02_context/01_support_resistance_targets.md)。

## 主要误读

- 在仍未成熟的暂停区或区间中部做 fade。
- 看到强边缘腿就认定区间必然突破或必然反转。
- 把 limit entry 当成亏损后无上限摊平。
- 忽略合理 stop 可能远于视觉上的区间边缘。
- 紧区间没有扣除成本后的 scalp 空间，仍强行交易。

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-MANUAL`、`SRC-TRADING-RANGES`、`SRC-STOP-ORDERS`、`SRC-SCALE-IN-TRENDS`、`SRC-STRONG-LEGS-2016`、`SRC-GOOD-TRADE-2017`、`SRC-HOLDING-WIDE-STOPS`、`SRC-COURSE-01-36`（课程 15G、18A–18F、19A）与 `SRC-COURSE-37-52`（课程 47A–47D、50E）。
