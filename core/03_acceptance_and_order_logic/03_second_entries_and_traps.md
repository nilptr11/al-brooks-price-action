# 二次入场和陷阱

> **状态：Core / Definition**
>
> 本文界定触发顺序和失败机制；Second entry 与 trap 都不是独立 Setup 家族。

## Second Signal 与 Second Entry

Second signal 是同一交易逻辑第二次形成候选触发，但订单尚未成交。Second entry 则要求第一次 entry 已经发生，并在随后数根内基于同一逻辑第二次实际形成 entry bar。

因此，图上“数到二”不必然是 second entry：

- 第一次若从未实际触发，后来出现的是第二个 signal，不是第二次 entry。
- 第一次触发后可以只是缺乏跟进或正常回撤，不要求先触及 protective stop。
- 若原 premise 已经失效，后来的触发属于新的 Setup，不能继续沿用原计数。

H2/L2 是常见的 second-entry 语言，但 H1/H2/L1/L2 的几何计数由[对应形态页](../04_patterns/02_h1_h2_l1_l2.md)定义。

## 它为什么可能有意义

第一次尝试缺乏延伸后，反方仍未建立控制；同一方向再次触发，可能表明第一次回撤只是测试。另一种情况是反方尝试实际失败，其退出压力支持当前 Context 中的相反方向。

“第二次”只描述 entry 次序，不保证第二次成功。它的交易意义仍来自上层命题，例如趋势恢复、区间边缘回归、突破后的第二腿或 MTR 的旧极值测试。

## Trap 的边界

Trap 不能只凭走势看起来不利就事后命名。实际触发、目标结果、开放亏损和退出压力的最低判定统一见[接受、失望与失败证据](01_acceptance_and_failure.md)；本页不重复建立第二套清单。

满足 trapped-trader 边界也只说明反向压力可能增加，并生成新的候选；反向交易仍需自己的 Context、Setup 和 entry。

## 继承上层交易命题

Second entry / trap 本身不规定 protective stop、profit target 或管理方式：

- 趋势延续中的 H2/L2 继承趋势恢复的 premise 与目标逻辑。
- 区间边缘的 second signal 继承 range-fade 的失效边界和区间内目标。
- 强 breakout 后的第二次触发继承新价格接受与第二腿预期。
- MTR 的第二次测试继承旧趋势失去控制的反向 swing 命题。
- Failed H2/L2 的反向交易必须重新归类，原交易者的 stop 不能自动成为新交易的 stop。

完整交易仍由 [Trade Plan](../06_trade_plan_and_management/00_trade_plan.md) 检查，不能从“二次”这个计数直接推导 reward/risk。

## 读图检查

- 第一次 entry 是否实际发生？
- 第一次只是弱跟进、正常回撤，还是原 premise 已失效？
- 第二次触发是否仍属于同一逻辑？
- 哪些可观察价格和退出边界支持 trapped-trader 推断？
- 这个顺序服务于哪一个上层 Setup？

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-10-PATTERNS`、`SRC-TREND-CHANNELS`、`SRC-TRADING-RANGES`、`SRC-STRONG-LEGS-2016`、`SRC-MTR-2025` 与 `SRC-PATTERNS-OPEN-2018`。
