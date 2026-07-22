# K 线类型

> **状态：Core / Definition**
>
> 本文界定核心概念；价格行为结论由本页、相关专题与来源共同支持。

## Trend Bar

单根 K 线处在 trend-bar 与 trading-range-bar 的连续谱上。实体相对较大、影线较小、收盘靠近方向端点时更像 trend bar；小实体与大影线更像 trading-range bar。边界不清时，以附近 K 线和市场 Context 判定，不能仅凭 open 与 close 不相等下定义。

需要表达“强趋势 K 线”时，再检查相对大小和收盘质量。强突破还需要后续跟进、少重叠，并且不能快速退回大实体。

单根趋势 K 线不等于趋势。趋势需要连续性和跟进。

## Signal Bar

对常见 stop-entry，触发入场的前一根是 signal bar，实际成交所在根是 entry bar；在 K 线收盘直接成交时，同一根可以同时承担 signal bar 与 entry bar。只有订单实际成交后，相应 K 线才取得这项角色；成交前可以称 prospective signal bar，但不能把候选触发误记成已有交易。

好的 prospective signal bar 通常方向清晰、收盘较强、反向影线较少，但必须服从 context。交易区间中部的漂亮 K 线仍可能没有优势。

## Entry Bar

Entry bar 是交易实际成交所在的 K 线。它的方向和收盘是信号是否得到初步跟进的第一道检验，但成交事实才是角色定义。

强 entry bar 通常朝交易方向收盘，并且没有立刻回到 signal bar 内部。弱 entry bar 常提示信号可能失败。

## Inside / Outside Bar

Inside bar 满足 high ≤ 前高且 low ≥ 前低，一端相等仍可成立。连续 inside bar 常进入 breakout mode；标准 ii / iii 使用完整高低范围，bodies-only ii 是较弱变体。

Outside bar 存在来源口径差异。官方 glossary 要求至少一端严格越过、另一端可相等或越过：`high > 前高且 low ≤ 前低`，或 `low < 前低且 high ≥ 前高`；课程 08B p450 则使用 `high ≥ 前高且 low ≤ 前低`。引用、标注或回测时必须注明采用哪一口径。无论采用哪套边界，它都可能代表强控制，也可能是双边混乱，收盘与后续比标签更重要。

## Tails 和 Doji

影线只是实体到本根极值之间的价格范围。长下影可累积为买压，长上影可累积为卖压，但是否是有意义的拒绝取决于位置和跟进。Doji 是相对周围实体很小或没有实体的 K 线。

这些 K 线只有在重要位置和后续跟进中才有交易意义。

## Reversal Bar / Two-Bar Reversal

`Reversal bar` 有两个来源层级：官方 glossary 的简化最低定义是与当前 trend / leg 相反的 trend bar；课程的操作性 buy / sell reversal bar 还容许反色实体，只要收盘位置满足相应方向的最低要求。经典牛反转常有下影和近高收，经典熊反转常有上影和近低收；先创新极值再收回只是常见增强项，不是统一必要条件。

Classic two-bar reversal 由相邻两根共同完成控制转移，第二根可以是 inside bar，不要求外包、等大或吞没第一根。课程同时使用更宽的功能性谱系：反转可以跨两根以上，multi-bar reversal 甚至不要求组成 K 线连续。记录时应区分 `classic two-bar reversal` 与 `course functional / multi-bar reversal`，不能用相邻两根的严格边界覆盖后者。

## Pullback / Pause Bar

牛向运动中的 bar pullback 要求本根 low 低于前 low；pause bar 则停止扩展趋势方向极值，通常 high 不高于前 high，强牛 K 后只高一跳的小 K 也可视为 pause。熊向运动镜像。Pause bar 属于 pullback 语言；它与 bar pullback 是两项不同几何测试，可能同时成立，并非互斥类别。

## 相关来源

相关来源见[正式来源台账](../../reference/official_sources.md)中的 `SRC-GLOSSARY`。
