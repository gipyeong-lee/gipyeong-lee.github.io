---
layout: learn-module
title: 密码资产识别与管理
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:post-quantum-cryptography-migration-lab:crypto-inventory
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/crypto-inventory/
module_id: m3
permalink: /learn/zh-cn/post-quantum-cryptography-migration-lab/crypto-inventory/
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
id: m3
slug: crypto-inventory
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- 解释密码资产识别 (Cryptographic Inventory) 的概念与必要性。
- 学习系统分类组织内加密算法、库及使用处的方法。
- 掌握为密码敏捷性 (Crypto-agility) 进行元数据管理的要素。
- 评估已识别密码资产的风险等级，以确定后量子转换优先级。
worked_examples:
- 系统扫描结果示例：识别到“正在使用 TLS 1.2 (ECDHE-RSA-AES128-GCM-SHA256)”。在此情况下，意识到 RSA 和 ECDHE 暴露于量子威胁，并对
  ML-KEM/ML-DSA 转换对象进行分类。
- 密码敏捷性自检表：若“算法是否被硬编码？”回答为“是”，则提升风险分数。若“是否可以通过配置文件选择密码算法？”回答为“否”，则提升转换难度。
lab:
  title: 密码资产识别与风险评估实操
  steps:
  - 对示例项目的源代码进行 'AES', 'RSA', 'ECC' 关键词搜索，寻找使用点。
  - 将已识别的密码实现（包括库）记录至 '密码资产清单 CSV'。
  - 根据 '安全寿命', '量子威胁等级', '数据重要性' 为每项资产核算风险分数。
  - 基于算出的分数对转换优先级 (P0~P3) 进行分类。
  safety:
  - 不得扫描正在运行的生产系统中的私钥或实际服务证书。
  - 测试仅使用隔离于虚拟环境内的虚拟证书（测试用）。
  - 分析结果（CSV, 文档）中不得包含实际秘密值或加密密钥值。
  deliverables:
  - 密码资产清单 CSV 文件（包括算法、使用处、库、库版本）
  - 基于优先级的密码资产风险评估报告 (Markdown)
assignment:
  title: 密码敏捷性分析与转换路线图制定
  deliverables:
  - 密码资产清单 CSV
  - 定义了转换优先级的决策表
  - 后量子转换路线图
  rubric:
  - 是否全面识别了密码资产？
  - 风险评估标准是否客观合理？
  - 转换路线图是否遵循了后量子技术转换的逻辑顺序？
  - 是否包含了改进密码敏捷性的具体技术建议？
quiz:
- question: 密码资产识别 (Cryptographic Inventory) 的主要目的是什么？
  choices:
  - 为了优化所有加密库的性能
  - 为了把握组织内的密码依赖性，准备 PQC 转换
  - 为了删除所有加密算法
  - 为了强制仅使用非对称密码
  answer_index: 1
  explanation: 密码资产识别旨在系统地管理需要转换的加密算法位置和依赖关系，从而有效地执行 PQC 转换。
- question: 下列关于密码敏捷性 (Crypto-agility) 的定义，哪项最为贴切？
  choices:
  - 为了更强大的加密而更换硬件的过程
  - 自动化更新加密库的功能
  - 在最小化代码变更的前提下，需要时能迅速更换密码算法的灵活性
  - 极其频繁地更换加密密钥
  answer_index: 2
  explanation: 密码敏捷性是指在算法更换时最小化代码变更负担，以适应不断变化的安全环境的能力。
completion_criteria:
- 提交密码资产清单 CSV 并完成风险评估
- 编写各密码资产转换难度及风险优先级说明报告
- 퀴즈 项目正确率达到 100%
source_ids:
- S1
---

## 密码资产识别 (Cryptographic Inventory)

密码资产识别是指将组织内使用的所有加密算法、协议、库以及应用这些加密技术的系统和数据进行系统化列表的过程。这是准备向后量子密码 (PQC) 转换的第一步，核心在于明确所保护密码算法的依赖关系 [S1]。

### 1. 主要管理对象
- **算法与协议**: TLS, SSH, 代码签名, 数据加密 (AES, RSA, ECC 等)。
- **基础设施**: 证书颁发机构 (CA), 密钥管理系统 (KMS), HSM, 云密钥存储。
- **软件**: 加密库版本 (OpenSSL, BoringSSL 等) 及静态/动态链接情况。

### 2. 密码敏捷性 (Crypto-agility)
密码敏捷性是指在最小化代码变更的前提下，能够迅速更换加密算法的能力。为实现此点，系统不应硬编码特定算法，而应具备通过配置文件选择算法的抽象层。

### 3. 风险评估标准
- **数据生命周期**: 加密数据在未来是否需要保持机密？（例如：现在窃取并在未来可能被解密的数据）
- **转换难度**: 是否需要更换硬件，还是仅需软件更新即可？
- **法规与合规**: 是否与 NIST PQC 标准的应用时机对齐。
