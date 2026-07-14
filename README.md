# Al Brooks 价格行为文档

本仓库用于学习 Al Brooks 价格行为、练习交易计划并核对来源。它不是自动信号系统、回测报告，也不提供特定市场的交易建议。

## 快速入口

| 当前任务 | 从哪里开始 | 负责什么 |
| --- | --- | --- |
| 第一次接触或系统学习 | [`LEARNING_PATH.md`](LEARNING_PATH.md) | 最小核心学习路径与按需专题 |
| 融会贯通地组织交易或管理持仓 | [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) | 学习体系的交易主线汇总，以及仓库的订单与记录操作 |
| 填写批次配置或单笔交易记录 | [`EXECUTION_RECORD_TEMPLATE.md`](EXECUTION_RECORD_TEMPLATE.md) | 执行手册的唯一派生记录版式 |
| 做连续逐根回放或模拟训练 | [`training/README.md`](training/README.md) | 连续训练闭环与按需观察提示 |
| 复盘已完成、未成交或放弃的计划 | [`training/03_review_checklist.md`](training/03_review_checklist.md) | 九个核心问题与复盘输出 |
| 查 Al Brooks 术语 | [`reference/glossary.md`](reference/glossary.md) | 快速定义，不许可交易动作 |
| 维护文档 | [`DOCUMENTATION_GOVERNANCE.md`](DOCUMENTATION_GOVERNANCE.md) | 目录、权威、来源和变更规则 |

学习材料回答“如何理解”；执行手册汇总 Brooks 的交易主线，并单独规定仓库如何记录订单、成交和保护；执行记录模板负责承载配置、计划和事件；训练材料负责把这些内容组成连续练习与复盘。

## 项目结构

```text
README.md                       任务分流
LEARNING_PATH.md                最小学习路径与按需专题
EXECUTION_MANUAL.md             Brooks 交易主线 + 仓库订单与记录操作
EXECUTION_RECORD_TEMPLATE.md    批次配置 + 单笔交易记录版式
DOCUMENTATION_GOVERNANCE.md     文档维护规则
learning/                       概念正文与可选形态参考
training/                       连续回放、逐根观察和复盘
reference/                      核心术语与维护证据
scripts/check_docs.py           入口、链接、锚点与来源引用检查
```

## 三条使用路径

- **系统学习**：先完成 [`LEARNING_PATH.md`](LEARNING_PATH.md) 的七份核心材料，再进入训练；形态库和高级主题按遇到的问题查阅。
- **计划与执行**：按 [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) 组织 context、setup、entry、stop、target、Trader's Equation 与 management，并用 [`EXECUTION_RECORD_TEMPLATE.md`](EXECUTION_RECORD_TEMPLATE.md) 保存订单和事件。
- **训练与复盘**：按 [`training/README.md`](training/README.md) 从保存的历史位置连续推进，记录当时事实、判断变化和自然出现的交易计划，最后只修正一个主要流程问题。

核心流程只有一条：

```text
market cycle 与 context -> setup、entry 与 protective stop
-> profit target、Trader's Equation 与仓位 -> 订单和成交
-> 随新价格信息管理 premise -> 复盘
```

## 权威层级

| 层级 | 入口 | 职责 | 是否规范执行 |
| --- | --- | --- | --- |
| 交易汇总与仓库操作 | [`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) | 从学习体系提炼交易主线；规定仓库订单、成交保护和记录操作 | 仅仓库操作部分具有规范性 |
| 记录工具 | [`EXECUTION_RECORD_TEMPLATE.md`](EXECUTION_RECORD_TEMPLATE.md) | 批次配置与单笔交易的可填写版式 | 否，从执行手册派生 |
| 学习 | [`learning/`](learning/00_method/README.md) | Al Brooks 概念、推导和常见边界 | 否 |
| 训练 | [`training/`](training/README.md) | 连续回放、逐根观察和复盘 | 否 |
| 查阅 | [`reference/glossary.md`](reference/glossary.md) | Al Brooks 术语快速解释 | 否 |
| 证据维护 | [`reference/`](reference/README.md) | Al Brooks 来源、结论性质和审计状态 | 否，只负责证明和校准 |

价格行为定义和交易原则必须能够回到 Al Brooks 来源。仓库只对文档维护、订单安全和记录完整性作操作约定；这些约定不能增加 setup 分类、stop 逻辑、target 公式或交易准入门槛。冲突时按[文档治理规范](DOCUMENTATION_GOVERNANCE.md)定位真正所有者并修正。

## 范围

- 仓库不替用户设定具体账户、单笔或时段风险数值；真实交易前必须另行确定这些上位边界，未设定时只能用于模拟和复盘。
- 不把任何形态写成脱离 context、location、follow-through 和 Trader's Equation 的自动信号。
- 来源内容只保存精炼转述、URL、页码或 slide 锚点和必要短引文，不复制受版权保护的大段原文。
