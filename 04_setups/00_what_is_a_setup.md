# 什么是 Setup

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../README.md#权威层级)。

## Brooks 语境中的定义

官方 glossary 对 setup 的最低定义是：由 context 和一根或多根 K 线构成、可作为放置入场单依据的 pattern。订单实际成交后，setup 的最后一根才成为 signal bar；成交所在 K 线是 entry bar。

因此，setup 比孤立形态多了 context 和入场依据，但它本身不等于已经获得执行许可。一个 wedge、H2 或 double bottom 可以只是 pattern；当交易者把它放回 context，并据此准备入场单时，才形成 Brooks 意义上的 setup。

## 从 Setup 到可执行计划

本仓库使用更严格的内部准入，但不把它冒充成官方定义。实际交易前还必须补齐：

- Market cycle。
- Context 和 location。
- 方向理由。
- 触发点。
- 失效点。
- 目标。
- 管理方式。
- Trader's Equation。

这些要素完成后，setup 才成为可执行交易计划；缺失任何关键项时，正确状态是候选或等待，而不是下单。

## Setup、Pattern 和 Trade Plan

Pattern 描述市场行为，例如 H2、wedge、double top。Setup 是带 context、可作为放置入场单依据的 pattern。Trade plan 再把失效、protective stop、仓位、目标、管理和 Trader's Equation 固化下来。

同一个 pattern 可以支持不同 setup，也可以完全没有交易价值；同一个 setup 也可能因为止损、目标或成本不合格而不能执行。

## Setup 检查表

看到可能交易点时，按顺序问：

1. 当前环境支持 stop entry、limit entry，还是等待？
2. 价格是否在好位置？
3. 触发点在哪里？
4. 触发后谁会被困？
5. 合理止损在哪里？
6. 第一目标在哪里？
7. 这笔交易是 scalp 还是 swing？
8. 概率、风险、回报和成本是否合算？

如果答案需要大量解释，通常说明 setup 不够清晰。
