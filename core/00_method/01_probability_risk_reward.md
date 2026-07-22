# 概率、风险和回报

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## Trader's Equation

看对方向不等于能赚钱。每笔交易至少要回答：错了会亏多少、对了能赚多少、概率是否足以补偿风险，以及成本和实际执行后是否仍值得。

Trader's Equation 的核心关系是：

```text
成功概率 × reward > 失败概率 × risk
```

概率、reward 和 risk 必须描述同一笔 entry、protective stop、profit target 和管理方式。佣金、滑点等成本不属于价格行为公式，但会影响真实净结果，执行记录需要另行计算。

分析时先使用二结果近似。只有部分止盈、scratch 或提前退出明显改变结果时，才需要拆分更多互斥结果；没有可靠样本时，不构造看似精确的完整概率树。

## 40–60 思维

多数普通交易没有压倒性胜率。不确定时常按约 40–60% 思考：约 40% 的较低概率一侧通常需要更大的潜在回报，swing 常以约 2R 作对照；较高概率可以接受较小 reward/risk。

这不是固定胜率或机械目标，而是在提醒交易者：

- 高概率通常要用更差 entry、更远 stop 或更小相对回报交换。
- 低概率只有在潜在回报足够大时才可能合理。
- 预判型和确认型入场是两个不同方程，不能沿用同一概率。
- 附近支撑阻力会压缩现实回报，远端幻想目标不能修复数学。

## 概率措辞边界

Likely 或 probably 只表示现有证据使概率向一侧倾斜，不表示结果确定。Risky 必须说明风险来自哪里：成功概率较低、合理 stop 较远、现实 reward 不足、成本过高，或这些因素的组合；它不能作为脱离同一 entry、stop、target 和管理方案的笼统结论。

## 风险优先

入场前先决定合理的 price-action stop。好的 stop 不是越小越好，而是能让正常价格波动有空间，并与 setup、target 和概率形成合理整体。

合理结构 stop 太远时，应缩小仓位、等待更好价格或放弃。Stop 不能只为了得到更漂亮的 reward/risk 而放进正常波动；成交后则继续根据 premise 和新的 price action 管理，而不是依赖希望。

Trader's Equation 中的 risk 来自 entry 到合理 protective stop 的距离；账户结果还会受到仓位、实际成交、滑点和成本影响。Stop 越远，仓位通常越小。这些账户与成交因素需要另行计入真实结果，但不改变 price-action stop 的依据。

## 与 target 和管理的关系

Trader's Equation 使用这类 setup 实际准备交易的 profit target。Measured move 只有在参照结构和投射起点清晰时才使用；support/resistance、scalp/swing 选择、部分止盈和 runner 都会改变 reward 与到达概率。

Trader's Equation 主要用于是否承担新风险。成交后不必为每根 K 线制造伪精确概率，但必须继续判断原 premise 是否仍成立；正常回调可以持有，强反向证据或 premise 失效则应按当前事实管理风险。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE` 与 `SRC-BREAKOUTS-2025`。
