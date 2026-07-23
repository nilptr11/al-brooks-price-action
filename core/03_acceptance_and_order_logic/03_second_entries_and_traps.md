# 二次入场和陷阱

> **状态：Core / Definition**
>
> 本文界定触发顺序和失败机制；Second entry 与 trap 都不是独立 Setup 家族。

## Second Signal 与 Second Entry

课程实务会把“等待第二次入场”宽泛用于第二次可交易机会；官方 glossary 则严格区分 second signal 与 second entry。为同时保留两种用法，本仓库记录三个不同事实：

1. **Second signal**：同一交易逻辑第二次形成 signal / 候选触发，结果是否越过触发价仍可未知。
2. **Second-entry opportunity / chart entry bar**：第一次 entry opportunity 已在价格上触发并形成 chart entry bar，随后数根内同一逻辑再次触发并形成第二根 chart entry bar。Chart entry bar 由既定触发条件第一次被越过或满足定义，不要求观察者下单或亲自参与第一次交易。
3. **Second actual fill / actual fill bar**：同一执行账户确实获得第二次成交，并记录真实成交所在的 actual fill bar；这是订单与持仓事实，不能从图形名称推定。

引用课程案例时可以保留其较宽的 `second entry` 原词，但仓库分析必须补充当时实际指 second signal、第二次触发机会，还是账户第二次成交。因而图上“数到二”仍不必然代表严格 glossary second entry：

- 第一次 signal 若从未触发，后来形成的是第二个 signal / 第二次机会，不是严格的第二根 chart entry bar。
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

Second signal、second-entry opportunity、second actual fill 和 trap 本身都不规定 protective stop、profit target 或管理方式：

- 趋势延续中的 H2/L2 继承趋势恢复的 premise 与目标逻辑。
- 区间边缘的 second signal 继承 range-fade 的失效边界和区间内目标。
- 强 breakout 后的第二次触发继承新价格接受与第二腿预期。
- 仍在交易区间内的强第一腿或第二腿不能借用已获接受 breakout 的延续概率；若边界没有被真正突破并守住，它可能只是[区间第二腿陷阱](../01_market_cycle/02_trading_ranges.md#强区间腿与第二腿陷阱)。
- MTR 的第二次测试继承旧趋势失去控制的反向 swing 命题。
- Failed H2/L2 的反向交易必须重新归类，原交易者的 stop 不能自动成为新交易的 stop。

完整交易仍由 [Trade Plan](../06_trade_plan_and_management/00_trade_plan.md) 检查，不能从“二次”这个计数直接推导 reward/risk。

## 读图检查

- 第一次 signal 是否触发并形成 chart entry bar，账户是否真的成交并形成 actual fill bar？
- 第一次只是弱跟进、正常回撤，还是原 premise 已失效？
- 第二次出现的是 signal、价格触发机会，还是账户实际成交；它是否仍属于同一逻辑？
- 哪些可观察价格和退出边界支持 trapped-trader 推断？
- 这个顺序服务于哪一个上层 Setup？

## 相关来源

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-MANUAL`、`SRC-10-PATTERNS`、`SRC-TREND-CHANNELS`、`SRC-TRADING-RANGES`、`SRC-STRONG-LEGS-2016`、`SRC-MTR-2025`、`SRC-PATTERNS-OPEN-2018`、`SRC-COURSE-01-36`（课程 08D–09C、15C–15D、18B、21D、24A–24E）与 `SRC-COURSE-37-52`（课程 42C、47C、49C、50D–51D）。
