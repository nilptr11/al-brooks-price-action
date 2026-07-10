# 逐根 K 线阅读模板

> **状态：Training / Derived**
>
> 本模板从当前[执行手册](../README.md#权威层级)派生，不替代其 D_init/D_live 和 Q_entry/Q_hold 边界。

## 训练目标

逐根训练的目标不是预测每根 K 线，而是在信息不完整时保持结构化判断，并在每根 K 线后更新观点。

## 记录模板

```text
M_base + overlay：
K 候选 / 方向：
C 控制权、位置和 PT1 空间：
本根 K 线新增信息：
多头理由：
空头理由：
T 当前触发：
D_init Permission / Entry / 最不利可接受成交边界：
D_init Invalidation / Protective stop：
D_init MaxLoss / OpenRisk limit / size / costs：
D_init PT1 / PT2 / G / TBTL：
D_init Early exit / time：
Q_entry：
订单状态（未提交 / 待成交 / 撤销 / 部分成交 / 全部成交）：
D_live 实际均价 / 剩余数量 / active stop / 剩余目标 / OpenRisk / Cost_hold_delta：
持仓后的 E / Q_hold / A：
```

## 趋势日模板

开盘后出现强趋势 K 线并有跟进时，初步判断可能形成趋势日。若随后回调浅、反方 K 线弱、顺势再次触发，则趋势日判断增强。

如果突破后没有跟进、回调变深并进入重叠，应降低趋势日判断。

## 交易区间模板

开盘上下波动、K 线重叠、收盘位置混杂时，先按方向不清处理。突破早期高低点后若缺乏跟进并回到区间内，追随者可能被困。

中部不追随普通信号，等待边缘、失败或清晰突破。

## 反转尝试模板

趋势成熟后，不因 climactic behavior 直接逆势。先等趋势线突破、反向强度、回探原极值失败，再评估反转 setup。

反转后若没有跟进，先按 trading range 处理，而不是坚持大反转。
