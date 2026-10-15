---
layout: learn-module
title: 编写转换优先级报告
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:post-quantum-cryptography-migration-lab:migration-roadmap
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/migration-roadmap/
module_id: m8
permalink: /learn/zh-cn/post-quantum-cryptography-migration-lab/migration-roadmap/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e5164bbefc324eff94b7957c62695f66
translation_run_id: 5e5e07b174e14daeb3ffc1651fe9dcbe
primary_category: ai-software
topics:
- post-quantum-cryptography
- cryptographic-inventory
- ml-kem
- ml-dsa
- crypto-agility
course_type: academic
published_at: '2026-10-16T00:55:40.127560+09:00'
id: m8
slug: migration-roadmap
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m7
objectives:
- 理解用于后量子密码 (PQC) 转换的风险与业务影响分析框架
- 基于加密资产清单数据确定转换优先级
- 为确保密码敏捷性 (Cryptographic Agility) 制定技术策略
- 构建最终转换路线图及验证报告
worked_examples:
- 示例 1：基于数据生命周期的优先级估算 - 需保存 20 年的人事信息数据库比仅需保存 5 年的日志数据在 PQC 转换中具有更高的优先级。
- 示例 2：混合 TLS 配置案例 - 分析将现有的 ECDH 与 ML-KEM 相结合，从而设计出只要两种算法中有一种是安全的，就能维持通信保密性的混合模型。
lab:
  title: 转换路线图模拟
  steps:
  - 加载上一模块中编写的清单 CSV 数据。
  - 编写一个 Python 脚本，为每项资产计算 [风险 * 重要性 * 生命周期] 分数。
  - 为优先级最高的 3 个资产制定混合实现计划。
  - 描述转换过程中可能出现的兼容性问题及其应对措施（回退策略）。
  safety:
  - 所有计算和分析仅在独立的隔离虚拟环境中进行。
  - 不得更改生产服务器的实际加密配置。
  - 审查分析笔记，确保其中不包含实际的密钥材料。
  deliverables:
  - 已排列优先级的清单 CSV 分析文档
  - 包含转换计划的技术决策表
assignment:
  title: PQC 转换优先级报告
  deliverables:
  - 密码敏捷性分析报告 (PDF)
  - 基于风险等级的转换路线图（含表格）
  rubric:
  - 基于数据生命周期和暴露风险的合理优先级逻辑
  - 通过引入混合加密体系考虑密码敏捷性
  - 转换计划的分阶段可行性
  - 实验结果与数据清单的一致性
quiz:
- question: 在确定密码转换优先级时，最需要考虑的数据特性是什么？
  choices:
  - 数据所使用的编程语言
  - 数据的安全必要生命周期 (Data Shelf Life)
  - 系统的开发者人数
  - 最新数据存储库的容量
  answer_index: 1
  explanation: 由于量子威胁包含了数据在未来被破解的风险，因此需要长期保密的数据最优先需要进行 PQC 转换。
- question: 为了实现密码敏捷性 (Cryptographic Agility)，推荐采用哪种软件设计方式？
  choices:
  - 使用硬编码的加密算法
  - 将加密模块与业务逻辑进行抽象分离
  - 仅使用单一算法的封闭结构
  - 直接引用操作系统级别的加密库
  answer_index: 1
  explanation: 将加密引擎与逻辑分离，在更换算法时最大限度减少代码变更的结构，是确保密码敏捷性的核心。
completion_criteria:
- 提交明确标注转换优先级的清单分析文件
- 编写包含密码敏捷性考量的转换路线图报告
- 完成包含所有实验代码和测量值的复现包
source_ids:
- S1
---

### 转换优先级策略 (Migration Prioritization Strategy)

向 NIST 后量子标准 (ML-KEM, ML-DSA) 的转换始于对整个系统的加密资产评估。转换优先级不仅取决于算法的老化程度，还取决于数据的生命周期 (Data Shelf Life)、加密暴露风险以及系统的战略重要性 [S1]。

#### 1. 加密资产评估标准 (Assessment Criteria)
使用以下标准来判断转换的紧迫性：
- **数据安全生命周期：** 加密数据在未来被量子计算机破解时产生的影响（例如：需要保密 10 年以上的数据）。
- **系统敏捷性：** 当前实现的密码是硬编码的，还是可以通过配置文件 (Config) 替换算法。
- **技术债务：** 使用该加密模块的依赖项 (Dependency) 以及是否可维护。

#### 2. 确保密码敏捷性
转换路线图的核心是在替换算法时最大限度地减少代码更改。建议采用抽象层 (Abstraction Layer) 将业务逻辑与加密引擎分离，并通过混合密钥交换方式确保既有算法的稳定性和 PQC 的抗量子性。
