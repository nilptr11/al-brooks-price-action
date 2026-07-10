# 缺口场景

> **状态：Training / Derived**
>
> 本文从当前[执行手册](../README.md#权威层级)派生，用于训练相关 gap 会实质改变判断时，如何把它并入市场读取、候选、目标和管理；不新增交易计划、通用必经步骤或执行规则。

## 核心边界

Gap 是条件式横切证据，不是 P5，也不是每笔交易都要建立的独立分析层。只有它会实质改变判断时才进入现有流程：

```text
读取 M -> 记录相关 gap 的边界、状态与作用 -> 路由 K -> 检查 C -> 等 T
-> 写 D / Q -> 实际成交并确认 protective stop
-> 只有匹配预写管理事件时才执行动作
```

Opening、body、micro measuring 和 moving-average gap 可以作为实时事实记录；`measuring gap` 只能先写候选，`exhaustion gap` 只能先写 potential，直到各自的后续结果已经出现。

## 相关 Gap 记录模板

```text
类型 / 周期：
两个边界或比较对象：
当前状态（保持、被测试、部分进入、关闭或不再相关）：
在 market cycle 中的位置（早期、延续、中后段、成熟末端）：
接受证据：
拒绝证据：
当前作用（强度、支撑阻力、路径障碍、回补目标、量度参考）：
仍未决的问题：
```

比较对象必须与类型匹配：body gap 看实体，micro measuring gap 看完整范围，moving-average gap 看整根 K 线与均线。不能只写“有 gap”，也不能在事后更换边界。

## 执行路由

| 当前 gap 状态 | M / K 路由 | C 与 T | D / 成交后边界 |
| --- | --- | --- | --- |
| Opening gap 获得同方向跟进、回踩守住旧边界 | M4，并观察新趋势结构；离开旧区域下注 K2，既有趋势恢复下注 K1。 | 检查下一现实阻力、gap 边界和旧区域；等待 T2 follow-through、回踩守住或 T1 恢复。 | Invalidation 是新区间不再被接受；stop 使用完整突破/回踩结构。Gap 保留只加强接受证据，不能单独触发管理动作。 |
| Opening gap 或突破形成的 gap 被进入，价格回旧区域并有反向跟进 | M4 失败并回到原基础状态或 M3；只回公平区域观察 K3。 | Gap reversal 只是早期事件；等待收回旧区域后的 failed entry、二次信号等 T3。 | Stop 在失败测试结构外；PT1 是旧公平区域中的第一现实目标。回补本身不足以确认失败或触发退出。 |
| 趋势中保留 body/micro gap，或 moving-average gap 后恢复 | 原方向控制增强，通常观察 K1；若正在离开重要旧区域才观察 K2。 | 先检查是否已追到差位置及目标空间；等待 T1，而不是因 gap 名称直接追价。 | 正确 stop 仍在 pullback/flag/swing 外；gap 消失只削弱证据，不自动使命题失效。 |
| 候选 measuring gap 仍开放且延续获得跟进 | 保持原 K1/K2，不生成新计划。 | 把 gap 投射与其他支撑阻力一起排序；它可以是 PT1、PT2 或仅为路径参考。 | D 冻结端点；只有最终形成 measured move 后才在复盘中确认名称。 |
| 成熟趋势末端出现异常大 gap / climax bars | 添加 M6，但不自动 K4。 | 先观察获利了结、小反转、结构破坏和旧极值测试；未出现前不逆势。 | 若只预期回到公平区域是 K3；只有控制权转移和反向 swing 空间成立才是 K4。 |
| Gap 状态未决、双方都无跟进 | 保留当前 M，并按无跟进 / 混乱处理。 | 不用“迟早回补”或“必然延续”选择方向；等待新信息。 | 空仓继续等待；持仓没有预写管理事件时继续执行原合同。 |

## 场景一：Opening Gap 被接受

以 gap up 为例：开盘后连续牛 K 线、收盘靠近高点，回踩无法进入旧区域，昨日高点或 gap 边界转为支撑。

执行顺序：

1. 标出 opening gap 的两个参照边界、昨日高点和下一阻力。
2. 记录 M4；若核心命题是市场接受新区间，观察 K2。
3. 不因 gap 标签在开盘价本身机械追入；按权限等待 T2 follow-through、回踩守住或 failed failure。
4. Stop anchor 使用完整突破腿或回踩失败结构；gap 中点不是默认 stop。
5. PT1 先使用下一现实阻力；只有强度和路径支持时，才使用区间高度或候选 measuring-gap 投射。
6. 成交后，gap 继续开放只是支持证据；如果动能下降但仍守住旧区域，可能转为 M2/M3，而不是立即反转。

Gap down 的熊向版本镜像；但若开盘后反而出现连续强牛 K 线，必须按实际买压重建候选，不能坚持 gap 方向。

## 场景二：Opening Gap 被拒绝

以 gap up 为例：市场进入 gap，回到昨日高点以下，原方向缺乏跟进，并形成反向 K 线或二次失败。

执行顺序：

1. `Gap reversal` 只记为当前 K 线向 gap 方向越过前一根至少一跳，甚至可能尚未到达真正的 gap 边界；此时仍可等待。
2. 回到旧区域并有反向跟进后，M4 失败；若只预期回归公平区域，观察 K3。
3. 基础权限等待 T3：收回旧区域后的 failed entry、二次信号或清晰反向 stop entry。
4. Stop anchor 放在失败 gap 的测试极值或完整失败结构外。
5. PT1 使用旧区域内第一个现实公平目标；不能默认整个 opening gap、昨日区间或远端目标必然被完全穿越。
6. 若要归 K4，必须另有趋势结构破坏、原方向测试失败和反向 swing 空间；gap fill 本身不够。

## 场景三：趋势中的 Gap

强趋势中出现 body gap、micro measuring gap，或首次深回调形成 moving-average gap bar，通常说明原方向仍有控制并可能再次测试趋势极值。

执行顺序：

1. 先确认当前仍是趋势，而不是成熟宽通道或交易区间中的第二腿末端。
2. Gap 只加强 K1 背景；仍需 H1/H2、L1/L2、旗形恢复或反方 failed entry 等 T1。
3. 价格已经远离正确 stop、第一目标空间不足时，不因 gap 强度追价。
4. Body/micro gap 后来被进入或回补时，重新评估控制权；没有反向跟进时可能只是正常 pullback。

## 场景四：Potential Exhaustion

成熟趋势末端出现异常大的顺势 K 线或连续高潮 K 线，并留下明显空间时，只先记录 M6 和 potential exhaustion。

之后分三条路：

- 原方向继续获得跟进：仍是延续，不能逆势。
- 获利了结后进入交易区间：可以观察 K3 回归，但目标仍以公平区域为界。
- 出现结构破坏、旧极值测试失败和反向持续压力：才观察 K4，并重新设计反向 swing 计划。

快速回补可以加强衰竭解释，但不是 exhaustion gap 的必要条件；一根反向 K 线也不等于 major reversal。

## D 与 Q 检查

每笔使用 gap 证据的计划都要回答：

1. Gap 改变的是概率、位置、stop anchor、路径障碍还是目标？
2. Invalidation 是什么可观察事实，而不是“gap 被碰到”这类模糊描述？
3. Gap 边界是否真的代表命题失效；若不是，正确结构 stop 在哪里？
4. PT1 前是否还有昨日高低点、均线、旧区间或其他明显障碍？
5. 若使用 gap measured move，端点是否在入场前冻结，退出价是否放在目标区近侧？
6. 使用保守 entry、stop fill 和退出价后，Q 是否仍合格？

## 成交后的更新

对使用了 gap 证据的计划，只有 gap 状态变化匹配预写的目标、失效、trailing 或条件式 runner 规则时才触发管理事件。Gap 仍开放、被进入或关闭本身都不要求动作；真正影响动作的是原管理合同中的可观察条件是否成立。

相关官方锚点见 [`reference/official_sources.md`](../reference/official_sources.md) 中的 `SRC-GLOSSARY`、`SRC-STRONG-LEGS-2016`、`SRC-OPENING-REVERSALS-2017`、`SRC-PATTERNS-OPEN-2018` 与 `SRC-LIVE-TR-BO-2021`。
