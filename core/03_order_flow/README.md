# 接受、失败与订单流

> **状态：Core / Index**
>
> 本页说明订单流专题的职责和文件入口；这里的“订单流”只使用图表上可观察的价格行为，不猜测真实订单簿身份。

## 职责

本目录负责判断一次尝试是否获得接受，区分 entry disappointment、premise 变化和 trade failure，并界定 stop entry、protective stop、limit-order behavior、second entry 与 trap。

Second entry 描述触发顺序，trap 描述失败后的持仓压力；两者都不生成独立的 stop、target 或 Setup 家族。

## 文件

1. [`00_acceptance_and_failure.md`](00_acceptance_and_failure.md)：follow-through、失望、失败和 trapped traders。
2. [`01_stop_entry_vs_protective_stop.md`](01_stop_entry_vs_protective_stop.md)：入场 stop 与保护性 stop 的不同用途。
3. [`02_limit_order_market.md`](02_limit_order_market.md)：双边限价交易占优时的行为和风险边界。
4. [`03_second_entries_and_traps.md`](03_second_entries_and_traps.md)：second signal、second entry、失败尝试与 trap。

K 线角色的最低定义见 [K 线类型](../04_patterns/01_bar_types.md)，概念总图见[核心框架](../README.md)。
