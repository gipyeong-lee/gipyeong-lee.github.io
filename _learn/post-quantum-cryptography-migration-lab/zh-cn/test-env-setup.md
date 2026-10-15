---
layout: learn-module
title: 构建隔离实验环境
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:post-quantum-cryptography-migration-lab:test-env-setup
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/test-env-setup/
module_id: m4
permalink: /learn/zh-cn/post-quantum-cryptography-migration-lab/test-env-setup/
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
id: m4
slug: test-env-setup
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- 理解用于后量子密码 (PQC) 实验的隔离本地开发环境的构成原理，以及必要工具（liboqs, oqs-provider）的作用。
- 分析在 TLS 1.3 等协议中 KEM 性能对握手延迟的影响。
- 使用 Docker 容器设计并构建依赖项固定、可重现的实验环境。
worked_examples:
- 示例 1：利用 Dockerfile 构建基于 oqs-provider 的环境。说明通过明确各库版本来确保构建可重现性的方式。
- 示例 2：使用 OpenSSL CLI 进行混合 TLS 握手测试。说明使用 'openssl s_server' 和 's_client' 模拟连接支持 ML-KEM-768
  的混合 TLS 1.3 的方法。
lab:
  title: 构建隔离的 PQC 测试台 (Testbed)
  steps:
  - 准备实验用 Docker 容器镜像基础 (Ubuntu 22.04 LTS 及以上)。
  - 克隆 (clone) liboqs 及 oqs-provider 源代码，并检出特定提交哈希以固定版本。
  - 使用 CMake 编译 liboqs 时，设置优化等级（如 AVX2）并执行构建。
  - 配置 OpenSSL 3.x 环境并激活 oqs-provider。
  - 通过本地网络接口的固定回环连接，测量基础 TLS 1.3 握手性能指标。
  safety:
  - 实验环境必须仅在本地隔离的容器内执行。
  - 严禁将生产环境的证书、真实私钥及客户数据带入容器内。
  - 注意编译与执行过程中生成的测量值仅视为公开测试数据，与实际安全策略无关。
  - 在监控实际硬件或功率时，请遵守制造商明确规定的额定电流及电压范围。
  deliverables:
  - 固定依赖版本的 Dockerfile 及构建日志。
  - 终端截图，展示已成功从 OpenSSL 中调用 PQC 算法列表。
  - 已完成环境配置的隔离开发环境校验和 (SHA-256)。
assignment:
  title: PQC 测试台文档化与评估
  deliverables:
  - 所构建测试台的架构图及选定算法的版本说明书。
  - 测试环境中传统算法与混合 ML-KEM 算法的握手时间对比数据 CSV。
  - 用于维持隔离环境的安全策略报告。
  rubric:
  - 依赖项版本固定及构建可重现性 (30%)
  - 在隔离实验环境中进行混合 TLS 握手的成功率 (40%)
  - 算法配置与测量程序的清晰度及安全性合规 (30%)
quiz:
- question: oqs-provider 的主要作用是什么？
  choices:
  - 在硬件层面加速 PQC 算法。
  - 作为在 OpenSSL 3 中使后量子算法能够用于 TLS 协议等的连接接口。
  - 自动更新生产环境的安全证书。
  - 拦截量子计算机的攻击向量。
  answer_index: 1
  explanation: oqs-provider 利用 OpenSSL 的 Provider 架构将 PQC 算法集成到标准库中，从而使现有应用程序能够使用
    PQC 算法。
- question: 在隔离实验环境中必须进行版本固定 (Locking) 的原因是什么？
  choices:
  - 因为最新版本总是更快。
  - 为了保证可重现性，并减少研究人员之间因运行环境差异导致的测量误差。
  - 为了加强生产安全。
  - 为了缩短构建时间。
  answer_index: 1
  explanation: 版本固定确保了环境的可重现性，是保障测量数据完整性及研究客观性的必备条件。
completion_criteria:
- 成功构成基于 Docker 的隔离构建环境。
- 完成通过 oqs-provider 进行 ML-KEM 混合模式演示。
- 提交包含实验数据测量及安全策略的报告。
source_ids:
- S2
---

### 隔离 PQC 实验环境的必要性
为了保护现有公钥密码（RSA, ECDH 等）免受量子计算机威胁，NIST 标准化了如 ML-KEM（基于 Kyber）及 ML-DSA（基于 Dilithium）等后量子算法。要在本地环境评估这些算法的性能与安全性，具备“密码敏捷性 (Crypto-agility)”且可重现的环境至关重要 [S2]。

#### 1. 主要构成要素
*   **liboqs**: 以 C 语言实现 PQC 算法的库，为测试各种 KEM 及签名算法提供基础。
*   **oqs-provider**: 利用 OpenSSL 3 的 Provider 架构，将 PQC 算法集成至现有 TLS 基础设施的接口。
*   **混合模式 (Hybrid mode)**: 结合现有传统密码 (ECDH) 与 PQC 算法，作为一种转换期策略，即使在 PQC 库存在潜在缺陷时也能维持现有的安全水平 [S2]。

#### 2. 实验环境核心：隔离与可重现性
实验必须完全脱离生产环境。利用 Docker 等容器技术固定 (Locking) 依赖项版本，可以减少研究人员之间的执行结果差异，从而精确测量算法优化（如利用 AVX-512）的效果 [S2]。在进行握手性能评估时，应使用固定的硬件和隔离的网络，以最小化延迟的不确定性。
