# 接受、失败与订单逻辑

> **状态：Core / Index**
>
> 本页说明订单用途、触发顺序和结果证据的职责及文件入口，不读取或猜测真实订单簿身份。

## 职责

本目录界定 stop entry、protective stop 和 limit-order behavior，判断一次尝试是否获得接受，并区分 second entry、trap、entry disappointment、premise 变化和 trade failure。

Second entry 描述触发顺序，trap 描述失败后的持仓压力；两者都不生成独立的 stop、target 或 Setup 家族。

## 文件

1. [`00_stop_entry_vs_protective_stop.md`](00_stop_entry_vs_protective_stop.md)：入场 stop 与保护性 stop 的不同用途。
2. [`01_acceptance_and_failure.md`](01_acceptance_and_failure.md)：follow-through、失望、失败和 trapped traders。
3. [`02_limit_order_market.md`](02_limit_order_market.md)：双边限价交易占优时的行为和风险边界。
4. [`03_second_entries_and_traps.md`](03_second_entries_and_traps.md)：second signal、second entry、失败尝试与 trap。

首次阅读先完成第 1 页，再读第 2 页；第 3、4 页在这两个边界上补充特定订单环境和触发顺序。编号同时表示稳定排列和这里的最低前置依赖。

K 线角色的最低定义见 [K 线类型](../04_patterns/01_bar_types.md)，概念总图见[核心框架](../README.md)。
