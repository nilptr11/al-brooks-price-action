# Brooks 价格行为文档

本仓库用于学习 Brooks 价格行为、练习交易计划并核对官方来源。它不是自动信号系统、回测报告，也不提供特定市场的交易建议。

## 快速入口

| 当前任务 | 从哪里开始 | 负责什么 |
| --- | --- | --- |
| 第一次接触或系统学习 | [`LEARNING_PATH.md`](LEARNING_PATH.md) | 最小核心学习路径与按需专题 |
| 设计交易或管理持仓 | [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) | 唯一规范执行文本；高级订单细节在同文件附录 |
| 做逐根回放或场景练习 | [`training/README.md`](training/README.md) | 训练闭环与场景入口 |
| 复盘已完成、未成交或放弃的计划 | [`training/03_review_checklist.md`](training/03_review_checklist.md) | 九个核心问题与复盘输出 |
| 查 Brooks 术语 | [`reference/glossary.md`](reference/glossary.md) | 快速定义，不许可交易动作 |
| 核对结论与官方依据 | [`reference/audit_matrix.md`](reference/audit_matrix.md) | 结论性质、来源和审计状态 |
| 了解术语、来源和审计的分工 | [`reference/README.md`](reference/README.md) | 参考层导航与权威边界 |
| 维护文档 | [`DOCUMENTATION_GOVERNANCE.md`](DOCUMENTATION_GOVERNANCE.md) | 目录、权威、来源和变更规则 |

学习材料回答“如何理解”；执行手册回答“这份计划是否完整、成交后如何控制风险”；训练材料负责把理解变成可复核记录。

## 项目结构

```text
README.md                       任务分流
LEARNING_PATH.md                最小学习路径与按需专题
EXECUTION_MANUAL.md             核心执行流程 + 高级执行附录
DOCUMENTATION_GOVERNANCE.md     文档维护规则
learning/                       概念正文与可选形态参考
training/                       场景、逐根观察和复盘
reference/                      术语、官方来源和审计矩阵
scripts/check_docs.py           文档一致性检查
```

## 三条使用路径

- **系统学习**：先完成 [`LEARNING_PATH.md`](LEARNING_PATH.md) 的七份核心材料，再进入训练；形态库和高级主题按遇到的问题查阅。
- **计划与执行**：按 [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) 的自然语言五问建立一份计划；只有出现复杂订单、部分成交或预设加仓时才进入高级附录。
- **训练与复盘**：从 [`training/README.md`](training/README.md) 选一段走势，记录当时事实、判断变化和待验证信息，最后只修正一个主要问题。

核心流程只有一条：

```text
市场与位置 -> 一个交易想法 -> setup、失效与 stop
-> 现实目标、数学与仓位 -> 订单和真实成交
-> 随新价格信息管理 premise -> 复盘
```

## 权威层级

| 层级 | 入口 | 职责 | 是否规范执行 |
| --- | --- | --- | --- |
| 执行 | [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) | 入场、失效、stop、目标、仓位、Trader's Equation、订单和管理 | 是，唯一执行权威 |
| 学习 | [`learning/`](learning/00_method/README.md) | Brooks 概念、推导和常见边界 | 否 |
| 训练 | [`training/`](training/README.md) | 场景、逐根观察和复盘 | 否 |
| 查阅 | [`reference/glossary.md`](reference/glossary.md) | Brooks 术语快速解释 | 否 |
| 来源 | [`reference/official_sources.md`](reference/official_sources.md) | 官方来源 ID、URL 和原文锚点 | 否，只负责证据定位 |
| 审计 | [`reference/audit_matrix.md`](reference/audit_matrix.md) | 结论性质、覆盖文件和核对状态 | 否，负责证明和校准 |

执行手册含有仓库内部的保守政策，不等于 Brooks 官方原文。官方资料负责证明和校准理念；冲突时按[文档治理规范](DOCUMENTATION_GOVERNANCE.md)定位真正所有者并修正。

## 范围

- 仓库不替用户设定具体账户、单笔或时段风险数值；真实交易前必须另行确定这些上位边界，未设定时只能用于模拟和复盘。
- 不把任何形态写成脱离 context、location、follow-through 和 Trader's Equation 的自动信号。
- 官方内容只保存精炼转述、URL、页码或 slide 锚点和必要短引文，不复制受版权保护的大段原文。
