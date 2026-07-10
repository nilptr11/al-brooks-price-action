# 入场、止损和目标

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../README.md#权威层级)。

## 入场

入场方式应匹配市场环境：

- 强趋势和强突破更适合 stop entry。
- 交易区间边缘和弱通道更可能适合 limit entry。
- 强趋势中的特殊情境可能出现 Buy The Close / Sell The Close。

入场不是交易的核心，完整交易想法才是核心。

## Protective Stop

Protective stop 把交易命题的 invalidation 转换成有限损失的订单。它不同于 stop entry；invalidation 是可观察的市场事实，protective stop 是结构外的订单价格。

止损太近可能被正常波动扫出，止损太远可能让风险回报失衡。好的止损是结构、目标和概率共同作用的结果。

常见止损管理要分清：

- Signal-bar stop：放在 signal bar 外侧，常见于 stop entry 或反转触发，风险清楚但可能太近。
- Structure stop：放在回调、失败突破、回踩或反转结构外侧，更直接对应交易想法的失效点。
- Wide stop / scaling-in：用更远止损和加仓换取更高存活率，必须降低仓位并预先限定最大风险。

止损不能为了凑出好看的 R 倍数而放在正常波动范围内。如果合理结构止损太远，通常说明入场位置不好或这笔交易不该做。

入场前必须锁定最外侧止损。入场后不得为了挽救交易而继续放宽；向盈利方向 trailing 需要新的有效 higher low / lower high 等结构，breakeven 不是机械动作。

## Targets

目标应在入场前就有依据。常见目标包括：

- 前高和前低。
- 区间中轴或另一侧边缘。
- 突破点回探。
- 量度目标。
- 大周期支撑阻力。
- 强趋势中的跟踪目标。

目标不是保证，而是评估风险回报的基础。

目标也有优先级。先看最近、明显、现实的近端目标，再评估 measured move 或更远 swing 目标。若近端目标已经压缩空间，不能用远端目标强行证明交易值得做。

Measured move 可以来自 Leg 1 = Leg 2、交易区间/形态高度、日内 gap 或 breakout height。每次使用都必须能说清参照结构和投射起点；它如果确实是从当前 entry 出发遇到的第一现实目标，可以直接进入初始 Trader's Equation，不应因名称被机械降为远端目标。

第一现实目标必须进入初始 Trader's Equation。更远的 measured move、延伸目标或 runner 只有在趋势、突破接受或反向 swing 证据支持时才启用；部分退出按仓位比例计算。TBTL 不是价格目标。

## 风险与仓位

官方 glossary 用 entry 到 protective stop 的距离描述 risk，并提醒滑点等会让实际成交损失偏离理论值。完整计划还应把价格风险乘以仓位，并计入预估手续费和滑点，得到计划最大账户损失。

市场在入场后出现一个更远的结构，不构成放宽 stop 的许可。若原 stop 不再合理，应按原计划退出并重新建立候选；若当前价到 active stop 的开放风险/利润回吐扩大，则按预案减仓或在新结构允许时推进 stop。

来源审计见 `reference/official_sources.md` 中的 `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE`、`SRC-RISK-113`。
