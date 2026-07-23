# 接受、失败与订单逻辑

> **状态：Core / Index**
>
> 本页说明订单用途、触发顺序和结果证据的职责及文件入口，不读取或猜测真实订单簿身份。

## 职责

本目录界定 stop entry、protective stop 和 limit-order behavior，判断一次尝试是否获得接受，并区分 second signal / second entry、trapped in / trapped out、entry disappointment、premise 变化和 trade failure。

Second entry 描述信号或触发顺序，trap 描述持仓内被迫退出或被挡在交易外的压力；两者都不生成独立的 stop、target 或 Setup 家族。

## 文件

1. [`00_stop_entry_vs_protective_stop.md`](00_stop_entry_vs_protective_stop.md)：入场 stop 与保护性 stop 的不同用途。
2. [`01_acceptance_and_failure.md`](01_acceptance_and_failure.md)：follow-through、失望、失败、trapped in / trapped out，以及 Pain Trade 行为路径模型。
3. [`02_limit_order_market.md`](02_limit_order_market.md)：双边限价交易占优时的行为和风险边界。
4. [`03_second_entries_and_traps.md`](03_second_entries_and_traps.md)：second signal、chart entry bar、账户 actual fill、失败尝试与 trap。

四页全部必读，并严格按上述编号阅读：第 1 页先区分入场与保护订单，第 2 页建立接受/失败边界，第 3、4 页再分别加入限价行为环境和触发顺序。编号表示完整阅读顺序及概念前置关系，不表示后两页可以省略。

K 线角色的最低定义见 [K 线类型](../04_patterns/01_bar_types.md)，概念总图见[核心框架](../README.md)。
