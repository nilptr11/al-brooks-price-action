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

本仓库分析时先使用二结果近似；这是为了检查同一方案是否自洽的整理方法，不是 Brooks glossary 中的独立术语。只有部分止盈、scratch 或提前退出明显改变结果时，才需要拆分更多互斥结果；没有可靠样本时，不构造看似精确的完整概率树。

## 40–60 思维

多数普通交易没有压倒性胜率。不确定时常按约 40–60% 思考：约 40% 的较低概率一侧通常需要更大的潜在回报，swing 常以约 2R 作对照；较高概率可以接受较小 reward/risk。

这不是固定胜率或机械目标，而是在提醒交易者：

- 高概率通常要用更差 entry、更远 stop 或更小相对回报交换。
- 低概率只有在潜在回报足够大时才可能合理。
- 预判型和确认型入场是两个不同方程，不能沿用同一概率。
- 附近支撑阻力会压缩现实回报，远端幻想目标不能修复数学。

在“盈利时得到 `2R`、失败时损失 `1R`”的二结果且暂不计成本模型中，正期望要求 `2p - (1-p) > 0`，即成功概率 `p > 1/3`；佣金、滑点与提前退出会提高实际门槛。因此，课程多处把约 `2R` 作为低概率 swing 的实用基线，不等于任何 `2R` 目标都“总是”具有正 Trader's Equation。

## 概率措辞边界

Brooks glossary 和课程把 `likely / probably` 约定为至少约 `60%` 的判断。这个数字是 Brooks 教学语言的内部阈值，不是普通英语的普遍定义，也不是经过校准的统计模型；价格行为概率仍是近似估计，`60%+` 更不表示结果确定。

Glossary 中的 `risky` 指 Trader's Equation 不清楚、仅勉强有利，或成功概率在 `50%` 以下。本仓库在解释风险来源时再把它拆成成功概率较低、合理 stop 较远、现实 reward 不足、成本过高或这些因素的组合；这是一种诊断展开，不能脱离同一 entry、stop、target 和管理方案，也不能覆盖 Brooks 的最低词条。

## 风险优先

入场前先决定合理的 price-action stop。好的 stop 不是越小越好，而是能让正常价格波动有空间，并与 setup、target 和概率形成合理整体。

合理结构 stop 太远时，应缩小仓位、等待更好价格或放弃。Stop 不能只为了得到更漂亮的 reward/risk 而放进正常波动；成交后则继续根据 premise 和新的 price action 管理，而不是依赖希望。

Trader's Equation 中的 risk 来自 entry 到合理 protective stop 的距离；账户结果还会受到仓位、实际成交、滑点和成本影响。Stop 越远，仓位通常越小。这些账户与成交因素需要另行计入真实结果，但不改变 price-action stop 的依据。

### 四种不能混用的风险

课程在不同章节使用 risk 时，至少涉及四个层面：

| 风险 | 含义 | 能否在入场前确定 |
| --- | --- | --- |
| Initial / price risk | 计划 entry 到合理 active protective stop 的结构距离 | 可以，是事前计划输入 |
| Actual Risk / MAE | 交易结束后回看，价格实际走过的最大不利距离 | 不可以，是事后样本结果 |
| Account risk | 风险距离乘仓位，再计合约价值、成本、滑点和全部计划加仓 | 可以估算，但实际成交可能扩大它 |
| Personal risk | 因希望、恐惧、仓位过大、心理止损或破坏规则产生的额外损失 | 只能通过计划、仓位和纪律限制 |

Trader's Equation 必须使用承担风险前可定义的结果分布。不能因为某笔赢家事后只有很小的 Actual Risk，就把这段浅回调当成该交易事前唯一可能的亏损，再用它证明原 entry 天然具有很高 reward/risk。Actual Risk 更适合在完整连续样本中作为 MAE 统计，用来研究是否存在更合理的 stop 或管理方案；它不能替代 original protective stop、失败结果和尾部风险。

账户风险与 price risk 也不是同一概念。合理结构 stop 较远时，可以通过缩小仓位保持账户风险很小；任意缩短结构 stop 反而可能让正常波动频繁结束交易。行为层面的 Personal risk 见[风险与心理纪律](../06_trade_plan_and_management/03_risk_psychology.md)，完整 scale-in 总风险见[加仓与减仓](../06_trade_plan_and_management/02_scaling_in_out.md)。

## 与 target 和管理的关系

Trader's Equation 使用这类 setup 实际准备交易的 profit target。Measured move 只有在参照结构和投射起点清晰时才使用；support/resistance、scalp/swing 选择、部分止盈和 runner 都会改变 reward 与到达概率。

Trader's Equation 主要用于是否承担新风险。成交后不必为每根 K 线制造伪精确概率，但必须继续判断原 premise 是否仍成立；正常回调可以持有，强反向证据或 premise 失效则应按当前事实管理风险。

相关来源见 [`reference/official_sources.md`](../../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-STOP-ORDERS`、`SRC-POSITION-SIZE`、`SRC-BREAKOUTS-2025`、`SRC-COURSE-01-36`（课程 13A、21B、30A–31D、34A–34B）与 `SRC-COURSE-37-52`（课程 37B、39C、51A–51D）。
