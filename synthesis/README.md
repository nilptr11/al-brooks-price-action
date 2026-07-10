# 分析与归并工作区

本目录保存概念压缩、重复概念归并和当前执行流程映射。这里的内容是研究与学习材料，不是执行规则，也不拥有术语定义权。

## 权威边界

- 实际执行以当前[执行手册](../README.md#权威层级)为准。
- 术语快速解释见 `reference/glossary.md`。
- 官方来源和审计状态见 `reference/official_sources.md` 与 `reference/audit_matrix.md`。
- 本目录中的结论若被采纳为执行规则，必须显式提升到执行手册并完成来源/政策标记。

## 当前文件

1. `00_core_framework.md`：把 Brooks 阅读压缩成一条学习主链条。
2. `01_repeated_concepts_map.md`：整理看似重复、实则处于不同层级的概念。

复盘训练清单已迁至 `07_scenarios/05_review_checklist.md`，避免在研究目录保留第二套执行问题。

## 使用原则

- 可以记录尚未收敛的分析，但要明确它不是执行权威。
- 可以引用当前执行流程的内部编号，但只能作为派生映射；执行流程重构时，本目录按实际依赖同步更新。
- 不用形态名称替代 context、触发、无效点、目标和交易数学。
- 发现与官方资料或执行手册冲突时，在 `reference/audit_matrix.md` 登记，再决定修改哪一层。
- 不在本目录重新复制完整的 stop、target、Trader's Equation 或 setup 定义。
