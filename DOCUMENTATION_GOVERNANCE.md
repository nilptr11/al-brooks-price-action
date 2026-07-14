# 文档治理规范

> **状态：Governance / Normative**
>
> 本文件只规范仓库结构、文档职责和维护流程，不定义价格行为。Al Brooks 概念与交易原则必须由来源、术语表和学习正文支持；[`EXECUTION_MANUAL.md`](EXECUTION_MANUAL.md) 只汇总这些原则并规范仓库的订单与记录操作。

## 1. 治理目标

本仓库以学习路径为主干，按“学习、执行、训练、查阅”分工，并在根目录保留导航、执行和治理入口。每项稳定结论只能有一个主要所有者，其他文档通过链接、转述或派生使用，不建立第二个维护点。

目标骨架如下：

```text
README.md
LEARNING_PATH.md
EXECUTION_MANUAL.md
EXECUTION_RECORD_TEMPLATE.md
DOCUMENTATION_GOVERNANCE.md

learning/
  00_method/
  01_market_cycle/
  02_context/
  03_order_flow/
  04_patterns/
  05_setups/
  06_trade_management/

training/
reference/
  README.md
  glossary.md
  official_sources.md
  audit_matrix.md

scripts/
  check_docs.py
```

目录职责：

- `learning/` 解释稳定概念、判断依据、概念之间的关系和常见误读，并在目录内部完成从 market reading 到 trade management 的知识闭环。
- `EXECUTION_MANUAL.md` 从学习体系和来源中提炼一份融会贯通的交易主线，并在独立章节规定仓库的订单、成交保护和记录操作；仓库操作具有规范性，价格行为内容不能由该文件自行发明。
- `EXECUTION_RECORD_TEMPLATE.md` 只把交易计划和仓库操作需要的信息排成可复制的批次配置与单笔记录，不定义 setup、stop、target、概率或例外。
- `training/` 保存连续回放流程、按需观察提示、逐根观察和复盘材料；它只派生使用学习与执行内容。
- `reference/` 保存稳定术语、Al Brooks 来源登记和审计状态。
- 根目录文件负责全仓入口、交易与操作汇总、唯一派生记录版式和文档治理，不在根目录堆放专题正文。

## 2. 状态类型

除根导航页外，每份 Markdown 正文都应在一级标题后声明状态。状态必须使用下表中的完整写法，不自行创造近义标签。

| 状态 | 适用范围 | 含义 |
| --- | --- | --- |
| `Governance / Normative` | `DOCUMENTATION_GOVERNANCE.md` | 规范文档结构与维护；不具有交易执行权威。 |
| `Normative` | `EXECUTION_MANUAL.md` | 汇总有来源支持的交易原则，并规范仓库订单、成交保护和记录操作；规范性不扩展到自创价格行为规则。 |
| `Execution / Derived` | `EXECUTION_RECORD_TEMPLATE.md` | 从执行手册派生的可填写记录版式；不增加规则或改变字段含义。 |
| `Navigation / Non-normative` | `LEARNING_PATH.md` 等跨目录导航 | 只负责入口、顺序和映射。 |
| `Learning / Navigation` | `learning/*/README.md` | 只负责单章范围、前置条件和章节索引。 |
| `Learning / Non-normative` | `learning/**/*.md` 专题正文 | 解释概念，不许可交易动作。 |
| `Training / Derived` | `training/**/*.md` | 从执行与学习层派生的训练材料。 |
| `Reference / Non-normative` | `reference/README.md`、`reference/glossary.md` | 快速查阅与稳定术语定义。 |
| `Evidence Registry / Non-normative` | `reference/official_sources.md` | 登记来源身份、访问范围和原文锚点。 |
| `Evidence Audit / Non-normative` | `reference/audit_matrix.md` | 登记结论性质、覆盖范围和核对状态。 |

`Normative` 表示仓库操作必须遵守；它不能覆盖已核对的 Al Brooks 定义和交易原则。`Governance / Normative` 只表示维护规则必须遵守。`Execution / Derived`、`Training / Derived`、`Non-normative` 和 `Navigation` 文档即使包含空白字段、示例、摘要或引用，也不能覆盖其上游所有者。

## 3. 文档所有权与权威层级

| 内容 | 唯一所有者 | 其他文档如何使用 |
| --- | --- | --- |
| 仓库入口和任务分流 | `README.md` | 链接到负责该任务的文档，不复制正文。 |
| 学习顺序与课程映射 | `LEARNING_PATH.md` | 章节 README 可声明局部前置条件，但不另建全局学习路线。 |
| 文档结构、状态和维护规则 | `DOCUMENTATION_GOVERNANCE.md` | 所有文档遵守；目录 README 可做简短提示并回链。 |
| 价格行为概念与交易主线 | 对应的 `learning/` 专题文件；稳定术语由 `reference/glossary.md` 所有 | 执行手册可以融会贯通并做必要摘要，但不能成为学习正文成立所需的上游，也不能创造新的交易规则。 |
| 仓库订单、成交保护和记录操作 | `EXECUTION_MANUAL.md`“仓库订单与记录操作” | 执行记录模板和训练材料可以引用；不得把操作字段写成价格行为定义。 |
| 执行记录的可填写版式 | `EXECUTION_RECORD_TEMPLATE.md` | 只排列执行手册要求的信息；字段含义、必需条件和动作仍回到执行手册。不得维护第二份模拟或实盘模板。 |
| 稳定 Al Brooks 术语 | `reference/glossary.md` | 正文按需要解释语境并回链，不维护第二份词典。 |
| 来源 ID 与原文锚点 | `reference/official_sources.md` | 通过 Source ID 引用，不复制来源登记。 |
| 结论性质与核对状态 | `reference/audit_matrix.md` | 各正文不自行建立平行审计表。 |
| 学习概念正文 | 对应的 `learning/` 专题文件 | 其他章节链接或做必要短摘要，避免跨章重复解释。 |
| 训练材料 | 对应的 `training/` 文件 | 只记录练习或示例，不反向定义价格行为或仓库订单/记录操作。 |

权威冲突按以下顺序处理：

1. Al Brooks 定义或交易原则冲突时，先查来源台账与审计矩阵，并在术语表或对应学习正文修正；执行手册必须随之同步。
2. 文档职责、路径或维护方式冲突，以本文件为准。
3. 仓库订单、成交保护、记录字段或操作顺序冲突时，以 `EXECUTION_MANUAL.md` 的“仓库订单与记录操作”为准；派生模板必须随之修正。
4. Al Brooks 术语的稳定写法，以 `reference/glossary.md` 为准。
5. 来源身份和锚点，以 `reference/official_sources.md` 为准；结论是否已核对，以 `reference/audit_matrix.md` 为准。
6. 学习或训练内容出现冲突时，先定位真正所有者并在那里修正，再传播到派生文档。

来源材料负责证明和校准价格行为内容。执行手册可以汇总这些内容，但不能用仓库权威覆盖来源；它只对订单安全和记录操作拥有内部规范性。

## 4. 依赖方向

“依赖”指一份文档需要另一份文档的定义、字段或结论才能成立；普通导航链接不算依赖。允许方向如下：

```text
reference/official_sources.md
  -> reference/glossary.md
  -> learning/
  -> EXECUTION_MANUAL.md

EXECUTION_MANUAL.md
  -> EXECUTION_RECORD_TEMPLATE.md

learning/ + EXECUTION_MANUAL.md + EXECUTION_RECORD_TEMPLATE.md
  -> training/

上述各层
  -> reference/audit_matrix.md
```

同时遵守以下边界：

- `learning/` 可以依赖已登记来源和稳定术语，并通过学习目录内的专题链接完成价格行为知识闭环；不得引用训练材料、执行手册或记录模板来补全概念、交易计划或管理逻辑。
- 若执行手册的汇总暴露出学习层缺少必要概念，先补全对应学习专题，再同步执行手册；不能让学习正文反向依赖这份派生汇总。
- `EXECUTION_MANUAL.md` 可以汇总已审计的概念与证据，但不得创造 setup 分类、stop 依据、target 公式或概率阈值；仓库订单操作也不能反向改变价格行为定义。
- `EXECUTION_RECORD_TEMPLATE.md` 只能依赖当前执行手册，把交易与操作信息排成空白版式；不能定义 setup、stop、target、概率阈值或管理例外。
- `training/` 可以引用学习内容、当前执行手册和记录模板，但不得建立新的规范字段、执行分支、记录版式或规则版本。
- `reference/audit_matrix.md` 观察和审计各层，不因记录某项内容而成为该内容的所有者。
- 同层专题尽量只依赖更基础的专题；若出现双向依赖，应提取共同定义到明确所有者或改成单向链接。

## 5. 命名与编号

- 文件和目录名使用小写英文 `snake_case`；根目录约定文件保留现有大写名称，包括唯一派生执行版式 `EXECUTION_RECORD_TEMPLATE.md`。
- `learning/` 一级章节使用两位数字前缀，顺序固定为 `00_method`、`01_market_cycle`、`02_context`、`03_order_flow`、`04_patterns`、`05_setups`、`06_trade_management`。
- 每个学习章节必须有 `README.md`，负责章节目标、前置条件、完成标准和本章索引。
- 学习专题使用 `NN_topic_name.md`。编号表达章节内的稳定展示顺序，不等同于交易优先级，也不应用于暗示概率或质量等级。
- `training/` 专题统一使用 `NN_topic_name.md`；编号只表达训练材料的稳定展示顺序。
- `reference/` 使用职责型稳定名称，不增加数字前缀。
- `reference/` 当前只包含入口、术语表、来源台账和审计矩阵；若要增加第五类文档，必须先在状态表和所有权表中明确其职责。
- `reference/glossary.md` 只保留核心流程反复使用、容易混淆或来源中的最低定义会影响判断的术语；低频专题词在首次出现处解释，不把术语表扩写成第二本教材。
- `reference/audit_matrix.md` 是维护证据，不进入学习路线或训练流程；学习者无需逐行阅读。
- 交易原则和仓库操作都使用可直接朗读的自然语言标题与问题；可复制的空白版式只在 `EXECUTION_RECORD_TEMPLATE.md` 排版。不得使用单字母代码建立隐藏流程。
- 重命名或移动文件时必须在同一变更中更新全部本地链接；不要为了保留旧路径而留下内容重复的副本。
- 标题应表达概念或任务，不把状态、来源 ID 或内部版本号塞入标题。

## 6. 来源登记与审计

来源登记和结论审计是两件事，分别由两个文件维护：

1. 在 `reference/official_sources.md` 中分配唯一 Source ID，格式为 `SRC-大写短名`，并登记来源身份、URL、访问范围、核验日期以及实际使用的章节、页码或 slide 锚点。
2. 在正文中只引用已登记的 Source ID；必要时补充精确锚点，不复制来源台账的完整记录。
3. 在 `reference/audit_matrix.md` 中为受来源影响的主题登记：真正所有者、关联或派生文档、Source ID、结论性质、当前审计状态和下一步。
4. 审计状态只使用 `已核对`、`部分核对`、`待核对`、`仓库操作规范` 或 `内部治理`。`仓库操作规范` 只用于订单安全、记录和训练组织，不得包含自创 setup、stop、target、概率或交易准入规则；内部治理只用于仓库结构和维护边界。
5. “来源已登记”只证明来源可定位；“已核对”才表示核心结论已与锚点及当前表达比对。两者不得互相代替。
6. 发现来源冲突时保留各自语境，在审计矩阵记录差异；不能只按发布日期覆盖旧资料。
7. 仓库只保留精炼转述、定位信息和必要短引文，不复制受版权保护的课程、书籍或大段原文。

## 7. 变更传播

任何变更都先修改拥有该内容的文档，再检查直接依赖者。常见传播范围如下：

| 变更起点 | 必查下游 |
| --- | --- |
| `DOCUMENTATION_GOVERNANCE.md` 的结构或状态约定 | 根导航、目录 README 和路径引用；只有核心入口、链接、锚点或 Source ID 规则变化时才同步审查 `scripts/check_docs.py` |
| `LEARNING_PATH.md` 的学习顺序 | 相关 `learning/*/README.md` 和根导航 |
| `EXECUTION_MANUAL.md` 的交易汇总或仓库操作 | `EXECUTION_RECORD_TEMPLATE.md`、`training/`、`reference/audit_matrix.md`；若价格行为内容改变，必须先修改来源所有者和对应 `learning/` 正文 |
| `EXECUTION_RECORD_TEMPLATE.md` 的记录版式 | 根导航和引用该版式的 `training/`；若字段要求变化，必须先修改执行手册 |
| `reference/glossary.md` 的术语定义 | 使用该术语的 `learning/`、执行手册、训练和审计条目 |
| `reference/official_sources.md` 的来源或锚点 | `reference/audit_matrix.md` 及引用该 Source ID 的正文 |
| `learning/` 的稳定概念 | 相关章节索引、训练材料和审计；若执行输入受影响，再审查执行手册 |
| `training/` 的示例或模板 | 同目录索引；若暴露上游缺口，应另行修改真正所有者，不能在训练层就地补规则 |

变更完成后应搜索旧术语、旧路径、旧字段名和重复段落。只修正一个链接不算完成路径迁移；只更新派生示例不算完成规则变更。

## 8. 添加文档的步骤

1. 先确认现有文件不能容纳该内容，并写清这份新文档唯一负责的问题。
2. 根据职责选择 `learning/`、`training/`、`reference/` 或根目录约定文件；不要先写内容再决定归属。
3. 确认唯一所有者和允许的依赖方向，避免复制执行手册、术语表、来源台账或其他专题正文。
4. 按本规范选择文件名、编号和状态行；学习文档同时确认章节内位置与前置条件。
5. 在最近一级 `README.md` 增加入口。只有新增跨目录任务入口时才修改根 `README.md`；只有学习顺序变化时才修改 `LEARNING_PATH.md`。
6. 若包含可验证的 Al Brooks 结论，先登记 Source ID，再补充或更新审计矩阵；若只是订单、记录或训练组织方式，标记为仓库操作规范，不得扩展成交易规则。
7. 检查所有相对链接、标题锚点、状态、来源 ID、反向依赖和重复维护点。
8. 在仓库根目录运行：

   ```bash
   python3 scripts/check_docs.py
   ```

   脚本只检查必需入口、单一 H1、本地链接与锚点，以及 Source ID 的登记和来源锚点。状态、目录职责、外链是否仍可访问、结论是否忠于来源、所有权、依赖和内容边界仍需人工复核。

9. 校验失败时修复缺失入口、链接、锚点或 Source ID；状态、目录索引、职责、依赖和内容边界按本规范人工复核。

## 9. 最低完成标准

一项文档变更只有同时满足以下条件才算完成：

- 内容位于正确层级，并有唯一所有者。
- 状态、命名、编号和依赖方向符合本规范。
- 所有受影响的导航、来源登记、审计条目和直接派生文档已同步。
- 没有新增第二套执行流程、平行记录模板、规范字段集、术语表、来源台账或内部编码路由。
- `python3 scripts/check_docs.py` 通过，并已人工复核本规范中不适合程序化的职责与内容边界。
