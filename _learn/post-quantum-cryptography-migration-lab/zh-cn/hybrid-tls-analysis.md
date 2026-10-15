---
layout: learn-module
title: 混合 TLS 握手分析
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:post-quantum-cryptography-migration-lab:hybrid-tls-analysis
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
module_id: m7
permalink: /learn/zh-cn/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
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
id: m7
slug: hybrid-tls-analysis
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m6
objectives:
- 说明量子威胁环境下 TLS 1.3 的脆弱性。
- 理解基于 ML-KEM 的混合 (Hybrid) TLS 握手结构。
- 在基于 OQS (Open Quantum Safe) 的本地环境中测量混合模式性能。
- 通过数据包捕获分析传统算法与 PQ 算法相结合的握手过程。
worked_examples:
- 示例 1：混合密钥交换过程 - 客户端将传统共享秘密值和 PQC 封装结果发送给服务器。服务器反封装后，结合两者的共享秘密并使用 KDF (Key Derivation
  Function) 合并，生成会话密钥。
- 示例 2：握手延迟分析 - 比较分析随着 PQ 算法应用导致额外的密钥大小 (Key Size) 增加从而延长网络传输时间的过程。量化性能优化 (如使用 AVX-512)
  应用前后的每秒握手次数 (Handshakes per second) 差异 [S2]。
lab:
  title: 基于 OQS 的混合 TLS 握手重现实验
  steps:
  - 在隔离的 Docker 环境中构建集成 liboqs 及 oqs-provider 的 OpenSSL 3 构建环境。
  - 配置现有 ECDH 模式与基于 ML-KEM 的混合模式 (如 secp256r1_mlkem768)。
  - 使用本地回环 (Loopback) 接口执行两种模式间的 TLS 1.3 握手。
  - 使用 Wireshark 捕获 ClientHello 及 ServerHello 消息中密钥交换数据字段的数据包。
  - 使用执行时间测量脚本测量 100 次以上的平均握手时间，并记录混合模式的开销。
  safety:
  - 本实验仅在本地环境的隔离回环接口上执行，不产生外部网络流量。
  - 绝对不得使用生产环境的证书、个人密钥等操作安全资产。
  - 学习用的 OQS 库属于实验性工具，不得用于实际生产安全服务。
  - 实验结束时删除所有生成的临时密钥及本地测量数据。
  deliverables:
  - 配置及执行日志文件
  - Wireshark 数据包捕获文件 (.pcapng) 及密钥交换字段分析笔记
  - 握手性能对比测量 CSV 数据
assignment:
  title: TLS 1.3 混合转换性能分析报告
  deliverables:
  - 握手延迟对比分析图表及数据可视化
  - 混合模式数据包分析与密钥交换算法特性总结
  - 生产环境应用时预期的性能及安全考虑事项决策表
  rubric:
  - 实验的可重现性（环境配置及脚本明确与否）
  - 数据包分析的准确性（密钥交换字段识别）
  - 性能测量数据的逻辑性诠释
  - 理论安全假设与实验结果的联系
quiz:
- question: 混合 TLS 握手的主要安全优势是什么？
  choices:
  - 通过显著减少握手步骤提高速度。
  - 确保传统算法和 PQC 算法中只要有一种安全，就能维持机密性。
  - 完全消除网络传输成本。
  - 降低证书管理的复杂度。
  answer_index: 1
  explanation: 混合模式结合了传统算法与 PQC 算法的结果，设计为即使其中一种算法失效也能保持机密性，这是一种转换期策略。
- question: 对 TLS 1.3 握手性能影响最大的 PQ 算法要素是什么？
  choices:
  - 仅考虑网络延迟。
  - KEM（密钥封装机制）的密钥生成、封装及解封装运算成本
  - 服务器的磁盘 I/O 速度
  - 客户端的浏览器版本
  answer_index: 1
  explanation: KEM 算法的计算成本直接关系到 TLS 1.3 握手性能，优化该指标是提升性能的核心 [S2]。
completion_criteria:
- 在本地环境中成功复现基于 liboqs 的混合 TLS 握手
- 通过 Wireshark 分析确认混合密钥交换消息
- 提交基于性能测量数据的分析报告
- 确认遵守安全约束（数据隔离、不使用生产密钥）
source_ids:
- S2
---

### 混合 TLS 握手理论

现行 TLS 1.3 依赖于传统公钥密码（如椭圆曲线 Diffie-Hellman，ECDH），在性能足以破解密码的量子计算机出现时，将暴露于攻击风险中 [S2]。为此，将 NIST 标准的 ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism) 等后量子密码 (PQC) 进行集成成为研究热点 [S2]。

#### 混合模式的安全假设
在完全转向 PQC 之前，为保证操作稳定性，使用结合了传统算法与 PQ 算法的“混合 (Hybrid) 模式”。此方式通过结合两种算法的共享秘密值 (Shared Secret)，确保即使两种算法中仅有一种安全，也能保证通信机密性。

#### 性能考虑因素
TLS 1.3 的握手性能直接依赖于 KEM 的计算成本 [S2]。特别是密钥生成 (Key Generation)、封装 (Encapsulation) 及反封装 (Decapsulation) 阶段的运算效率决定了整体握手速度。最近，通过 AVX-512 等指令集优化多项式乘法和模运算，加速了提升握手性能的手段已被应用 [S2]。
