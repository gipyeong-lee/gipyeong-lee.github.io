---
layout: learn-module
title: 性能评估与基准测试
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:post-quantum-cryptography-migration-lab:performance-benchmarking
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/performance-benchmarking/
module_id: m6
permalink: /learn/zh-cn/post-quantum-cryptography-migration-lab/performance-benchmarking/
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
id: m6
slug: performance-benchmarking
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m5
objectives:
- 理解后量子密码算法 (ML-KEM) 的性能评估指标（时间、内存、处理量）。
- 分析在 TLS 1.3 握手过程中 KEM 运算对性能的影响。
- 利用 Liboqs 及 oqs-provider 框架对混合密码模式进行基准测试。
worked_examples:
- '示例 1：使用 Liboqs 进行单 KEM 运算基准测试

  通过 Python 脚本，使用 `timeit` 模块测量 `ML-KEM-768` 的 `keypair`, `encaps`, `decaps` 动作时间，并将结果保存为
  CSV 的方法。'
- '示例 2：混合 TLS 1.3 握手处理量测量

  在应用 oqs-provider 的本地服务器/客户端环境中，使用 `s_client` 和 `s_server` 测量 100 次连接所耗费的总时间，从而计算每秒握手次数
  (TPS) 的分析流程。'
lab:
  title: PQC 性能基准测试实操
  steps:
  - 在隔离开发环境中安装 liboqs 和 oqs-provider 并确认环境配置。
  - 编写基准测试用 Python 脚本，测量 ML-KEM 算法的运算时间。
  - 执行 Wireshark 捕获 TLS 握手数据包，分析混合模式下的数据大小变化。
  - 基于测量数据，将运算时间与处理量指标进行图表化。
  safety:
  - 实验仅在本地隔离环境内进行，绝对不得使用生产环境的证书或密钥。
  - 由于基准测试过程可能产生高 CPU 负载，请监控系统资源。
  - 注意确保捕获文件中不包含真实秘密值或密钥数据。
  deliverables:
  - 运算性能测量脚本 (.py)
  - 测量结果 CSV 数据
  - 各算法性能对比分析报告 (.md 或 .ipynb)
assignment:
  title: 基于密码敏捷性的性能评估报告
  deliverables:
  - 算法选择理由及安全/性能折衷分析
  - 基准测试数据可视化资料
  - 基于性能结果的转换路线图修正案
  rubric:
  - 基准测试数据是否在可重现且独立的环境中测量？
  - 是否准确分析了性能损耗的技术原因（密钥大小、运算复杂度）？
  - 是否平衡讨论了混合模式的优势与成本？
quiz:
- question: 在 TLS 1.3 握手性能中，最重要的 PQC 算法相关要素是？
  choices:
  - 对称密码算法的块大小
  - KEM 的密钥生成及封装运算时间
  - 哈希算法种类
  - 服务器的操作系统类型
  answer_index: 1
  explanation: TLS 1.3 握手性能在很大程度上取决于 KEM 算法的运算效率 [S2]。
- question: 进行性能评估时使用混合模式的主要原因是？
  choices:
  - 因为它比传统算法总是更快
  - 为了在防范 PQC 安全威胁的同时维持安全性
  - 为了减少网络带宽
  - 为了最小化运算资源
  answer_index: 1
  explanation: 混合模式结合了 PQC 的未来安全性和传统算法的经受验证的安全性，从而实现渐进式转换。
completion_criteria:
- 基准测试脚本运行及结果数据获取完毕
- 性能评估报告提交并审核通过
- 完成 TLS 混合模式性能分析
source_ids:
- S2
---

## 性能评估与基准测试

向后量子密码 (PQC) 的转换不仅是算法替换问题，更是直接关乎现有网络协议（如 TLS 1.3）性能的问题。特别是 KEM (Key Encapsulation Mechanism) 运算直接影响握手延迟 (latency) 以及服务器每秒处理连接数 (handshakes per second) [S2]。

### 性能指标
1. **运算时间 (Computation Time):** 密钥生成 (KeyGen)、封装 (Encaps)、反封装 (Decaps) 各自消耗的 CPU 周期或时间 (ms)。
2. **数据大小:** 公钥及封装后的密钥 (ciphertext) 大小。这决定了网络带宽消耗及产生碎片化的可能性。
3. **处理量 (Throughput):** 每秒可处理的握手次数。优化的实现（如利用 AVX-512）可以通过提升多项式乘法及模运算速度显著改善处理量 [S2]。

### 混合模式
转换期推荐采用传统算法 (ECDH) 与 PQC (ML-KEM) 并存的混合方法。此举旨在防范 PQC 可能存在的脆弱性，同时获取 PQC 的安全优势。由于混合模式增加了运算复杂度，必须缜密评估其性能损耗 [S2]。
