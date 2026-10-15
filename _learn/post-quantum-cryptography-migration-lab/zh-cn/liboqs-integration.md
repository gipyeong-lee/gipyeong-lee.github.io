---
layout: learn-module
title: OQS 与 oqs-provider 集成
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:post-quantum-cryptography-migration-lab:liboqs-integration
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/liboqs-integration/
module_id: m5
permalink: /learn/zh-cn/post-quantum-cryptography-migration-lab/liboqs-integration/
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
id: m5
slug: liboqs-integration
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- 理解 Open Quantum Safe (OQS) 架构与 oqs-provider 的作用。
- 掌握 PQ (Post-Quantum) 算法在 TLS 1.3 中的集成方式。
- 在本地环境中构建并验证混合 (Hybrid) TLS 握手。
- 思考 KEM 实现优化（如 AVX-512）对实际握手性能的影响。
worked_examples:
- 示例 1：要验证 oqs-provider 是否已加载到 OpenSSL 中，执行 `openssl list -providers` 命令。输出结果应包含 'oqs'
  提供程序。
- 示例 2：执行混合握手时，通过命令行参数指定密钥交换组，如 `openssl s_client -groups kyber768_x25519...`。这是 ML-KEM
  (Kyber) 与传统 Curve25519 相结合的混合组。
lab:
  title: 本地环境下的混合 TLS 测试
  steps:
  - 在隔离的 Docker 容器中构建并安装 liboqs 和 oqs-provider。
  - 修改 OpenSSL 配置文件 (`openssl.cnf`) 以激活 oqs 提供程序。
  - 打开两个终端，分别以混合模式运行 `openssl s_server` 和 `openssl s_client`。
  - 使用 Wireshark 捕获并分析 ClientHello 和 ServerHello 数据包中共享密钥组 (Key Share) 的传输情况。
  - 验证握手是否成功，并查看会话加密算法信息。
  safety:
  - 实验务必仅在隔离的本地虚拟环境内执行。
  - 绝不使用生产服务中使用的证书或密钥。
  - Wireshark 捕获时请确保不包含真实服务流量。
  deliverables:
  - oqs-provider 激活确认截图
  - 混合握手日志文件
  - Wireshark 捕获数据包的共享密钥组分析报告
assignment:
  title: 基于密码敏捷性的转换分析报告
  deliverables:
  - TLS 握手性能测量结果数据 (CSV)
  - 混合模式使用理由与性能损耗分析小论文
  - 基于优先级的后量子转换路线图
  rubric:
  - OQS 工具链构建及执行成功与否
  - 通过 TLS 数据包分析，是否准确说明了混合模式的操作
  - 性能测量数据是否包含实验环境及版本信息且可重现
  - 是否基于密码敏捷性概念逻辑地编写了转换路线图
quiz:
- question: oqs-provider 在 OpenSSL 中的核心作用是什么？
  choices:
  - 加密网络数据包的硬件加速器
  - 允许 OpenSSL 调用 liboqs PQC 算法的接口层
  - 在互联网上发布公钥证书的服务
  - 检测量子计算机攻击的 IDS 工具
  answer_index: 1
  explanation: oqs-provider 通过 OpenSSL 的 Provider 架构，将 liboqs 的算法连接至 OpenSSL 应用程序，使其能直接使用。
- question: 在 TLS 1.3 中使用“混合模式”密钥交换的主要原因是什么？
  choices:
  - 为了将性能提高 100 倍以上
  - 为了在单一算法实现出错或未来出现漏洞时确保安全性
  - 为了支持所有现有客户端
  - 为了使用量子计算机进行握手
  answer_index: 1
  explanation: 混合模式结合了传统算法与 PQC 算法，是一种多层防御策略，旨在防范实现缺陷或未知的漏洞。
completion_criteria:
- 基于 oqs-provider 的本地测试环境构建完成
- 混合 TLS 握手成功并通过数据包捕获验证
- 完成包含实验结果与分析的报告编写
- 制定完成的后量子转换路线图
source_ids:
- S2
---

## OQS 与 oqs-provider 集成理论

为了保护现有的数据传输免受量子计算机威胁，将 NIST 标准的后量子算法 (PQC) 集成至现有协议（如 TLS 1.3）中至关重要。OQS (Open Quantum Safe) 项目为加速这一集成提供了关键框架 [S2]。

### 1. liboqs 与 oqs-provider
- **liboqs**: 包含 PQC 算法 (ML-KEM, ML-DSA 等) 的 C 语言实现的核心库，为各种算法提供统一 API。
- **oqs-provider**: 利用 OpenSSL 3 的 Provider 架构，帮助 OpenSSL 应用程序 (如 `s_client`, `s_server`) 原生使用 liboqs 的 PQC 算法的中间层。通过此方式，无需修改代码即可在现有 TLS 工具中测试 PQC 功能。

### 2. TLS 1.3 的 PQ 集成方式
在 TLS 1.3 握手过程中，PQC KEM 替换或补充了现有的密钥交换 (如 ECDH)。
- **PQ-only 模式**: 仅使用 PQC KEM 进行密钥交换。
- **混合 (Hybrid) 模式**: 结合现有的传统算法 (ECDH) 与 PQC 算法。此策略旨在确保后量子安全性同时保持传统安全保障，从而应对算法实现错误或未来的漏洞 [S2]。

### 3. 性能考虑因素
PQC KEM 的密钥大小或计算量通常大于传统算法，因此会对握手性能产生直接影响 [S2]。利用最新的硬件指令集 (如 AVX-512) 优化多项式乘法及模运算，可以提升握手速度 [S2]。
