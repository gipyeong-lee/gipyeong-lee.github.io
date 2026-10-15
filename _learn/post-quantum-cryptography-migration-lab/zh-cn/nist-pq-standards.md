---
layout: learn-module
title: ML-KEM 与 ML-DSA 标准理解
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:post-quantum-cryptography-migration-lab:nist-pq-standards
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/nist-pq-standards/
module_id: m2
permalink: /learn/zh-cn/post-quantum-cryptography-migration-lab/nist-pq-standards/
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
id: m2
slug: nist-pq-standards
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- 解释格密码体系的数学基础与安全性依据。
- 理解 NIST 标准 ML-KEM（密钥封装机制）的运行原理。
- 掌握 NIST 标准 ML-DSA（数字签名算法）的结构特性。
- 分析格密码相比其他密码方式（代码基、哈希基）具有实务优势的原因。
worked_examples:
- 示例 1：格基 KEM 的安全强度对比。ML-KEM-512, 768, 1024 分别对应 NIST 安全强度 1, 3, 5 级别。其目标是达到类似于传统密码
  AES-128, 192, 256 的安全水平。
- 示例 2：应用模格 (Module Lattice) 概念。通过使用向量和矩阵优化运算，从而在保持安全强度的情况下优化性能，优于普通格结构。
lab:
  title: ML-KEM 与 ML-DSA 算法基础实验
  steps:
  - 安装 liboqs 并设置环境变量。
  - 使用 Python 示例代码执行 ML-KEM 密钥对生成及封装过程。
  - 执行使用 ML-DSA 对消息进行签名与验证的脚本。
  - 测量并记录每项运算所需的时间。
  safety:
  - 不得访问实验用虚拟环境以外的系统证书或真实密钥文件。
  - liboqs 库仅供研究与测试使用，不得将其误认为是运行环境的安全解决方案。
  - 所有实验数据保留在本地虚拟环境中，不得传输至外部网络。
  deliverables:
  - 包含运算时间测量数据的 CSV 文件
  - 算法实现执行结果截图
  - 实操过程总结日志
assignment:
  title: 后量子密码标准分析报告
  deliverables:
  - ML-KEM 与 ML-DSA 算法特征总结表
  - 格密码系统在实际转换时需考虑的性能约束（如密钥大小）分析
  - 利用研究用库进行测试的局限性描述
  rubric:
  - 是否准确描述了标准算法的数学依据？
  - 是否分析了格密码系统的优势与局限？
  - 是否展示了对安全威胁模型的正确理解？
quiz:
- question: 下列哪项是格密码系统主导实务标准化的主要原因？
  choices:
  - 因为它拥有最短的安全历史
  - 因为它能够实现最坏情况到平均情况的归约，且具备高效实现可能
  - 因为它可以轻易被量子算法破解
  - 因为它仅使用基于代码的密码来最大化安全性
  answer_index: 1
  explanation: 格密码系统凭借其强大的数学归约依据及高效的实现可行性，处于 NIST 标准化的中心 [S4]。
- question: ML-KEM 基于哪种数学问题类型？
  choices:
  - 大整数分解问题
  - 椭圆曲线离散对数问题
  - 模学习误差问题 (MLWE)
  - 哈希冲突问题
  answer_index: 2
  explanation: ML-KEM 以模格基础的学习误差 (MLWE) 问题作为安全性依据。
completion_criteria:
- 理论学习评估测验全部答对
- 提交包含实验过程及测量数据的报告
- 提交确认已遵守实验安全指南并在隔离环境中进行测试的检查清单
source_ids:
- S4
---

## 理解 ML-KEM 与 ML-DSA 标准

### 1. 格密码的兴起
目前主导实务标准化的系统是基于格 (Lattice-based) 的系统。这是因为它们在最坏情况 (worst-case) 到平均情况 (average-case) 之间存在强大的数学归约 (reductions)，且能够高效实现 [S4]。另一方面，基于代码 (Code-based) 或基于哈希 (Hash-based) 的方式起着保守锚点 (conservative anchors) 的作用，具备更长的安全历史或仅需最低限度假设的特性 [S4]。

### 2. ML-KEM (Module-Lattice Key Encapsulation Mechanism)
ML-KEM 基于以前称为 Kyber 的算法。它基于模格难题 (Module Learning With Errors, MLWE)，流程如下：
- **KeyGen:** 在模格中生成公钥和私钥。
- **Encapsulation:** 使用公钥生成共享秘密值 (Shared Secret) 和封装后的密钥 (Ciphertext)。
- **Decapsulation:** 使用私钥从封装后的密钥中恢复出原始共享秘密值。

### 3. ML-DSA (Module-Lattice Digital Signature Algorithm)
ML-DSA 基于 Dilithium，使用了“带中止的 Fiat-Shamir (Fiat-Shamir with Aborts)”技术。它通过格难题的难度提供防伪能力，是兼顾签名大小与公钥大小的实用标准。

### 4. 安全假设
格密码系统的安全性与寻找最短向量问题 (Shortest Vector Problem, SVP) 密切相关。与量子计算机的 Shor 算法能高效破解传统 RSA 或 ECC 不同，格难题被认为即使使用量子算法也无法在多项式时间内求解。
