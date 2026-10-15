---
layout: learn-module
title: 量子威胁与格密码
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:post-quantum-cryptography-migration-lab:quantum-threat-model
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/quantum-threat-model/
module_id: m1
permalink: /learn/zh-cn/post-quantum-cryptography-migration-lab/quantum-threat-model/
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
id: m1
slug: quantum-threat-model
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- 理解量子计算机对现代密码体系（RSA, ECC）构成的威胁模型。
- 分析格密码（Lattice-based Cryptography）的数学基础及安全性依据。
- 学习 NIST 推荐的后量子密码标准（ML-KEM, ML-DSA）的设计原理。
- 描述格密码算法的效率及安全性特性（最坏情况难度，worst-case hardness）。
worked_examples:
- 示例 1：量子计算机对 RSA 的影响分析 - RSA 基于大数分解难度。Shor 算法将 n 位整数分解的复杂度从指数时间降至多项式时间，从而即时破解加密文。
- 示例 2：格密码难题 (LWE) 概念理解 - 考虑添加了秘密向量 s 和误差 e 的线性方程组系统 A*s + e = t。格密码基于“学习误差问题 (Learning
  With Errors)”，即从矩阵 A 和结果 t 中寻找 s 的难度。
lab:
  title: 格密码基础环境构建与可视化
  steps:
  - 在隔离的 Linux/Docker 环境中创建 Python 3 虚拟环境
  - 安装并编译 liboqs 库
  - 编写脚本，收集格密码 LWE 问题随参数变化导致的密钥大小及运算时间数据
  - 运行数据分析与可视化笔记本
  safety:
  - 所有实验均在隔离的本地虚拟环境内执行
  - 严禁使用真实生产证书、私钥及客户数据
  - 不得将研究用库视为实际服务的安全手段
  deliverables:
  - 环境配置日志及编译结果
  - 算法性能（密钥大小、时间）对比分析数据
  - 格密码特性报告
assignment:
  title: 撰写量子威胁分析报告
  deliverables:
  - 量子威胁模型及格密码理论总结文档
  - 主要 PQC 算法（ML-KEM, ML-DSA）对比表
  rubric:
  - 准确解释了 Shor 算法原理
  - 逻辑描述了格密码的最坏情况难度 (worst-case hardness) 概念
  - 基于所给来源 [S3, S4] 描述了现代密码学面临的挑战
quiz:
- question: Shor 算法对现有 PKI 构成的威胁是什么？
  choices:
  - 无条件破解所有对称密码。
  - 在多项式时间内解决大整数分解及离散对数问题。
  - 彻底消除哈希函数的抗碰撞性。
  - 降低量子计算机的处理速度。
  answer_index: 1
  explanation: Shor 算法通过在多项式时间内解决 RSA 基础的大整数分解问题和 ECC 基础的离散对数问题，威胁了现有的公钥密码体系。
- question: 格密码为何具有前景？
  choices:
  - 因为可以将最坏情况难题转化为平均情况难题。
  - 因为它比所有对称密码快得多。
  - 因为在量子计算机上也必然无法求解。
  - 因为它完全不占用计算机内存。
  answer_index: 0
  explanation: 格密码具有从最坏情况难度 (worst-case hardness) 保证平均情况 (average-case) 安全性的数学优势 [S4]。
completion_criteria:
- 完成理论学习并提交量子威胁报告
- 在实验环境中成功使用 liboqs 运行基础算法
- 퀴즈 题目正确率达到 80% 以上
source_ids:
- S3
- S4
---

## 量子威胁模型
现代公钥密码 (PKI) 主要依赖于大整数分解 (RSA) 和离散对数问题 (ECC) 的数学难题。Shor 算法能够利用量子计算机在多项式时间内解决这些问题，这意味着它实际上将导致目前所有标准 PKI 失效 [S3]。

## 格密码 (Lattice-based Cryptography)
格密码利用高维空间中从格 (Lattice) 的基向量中寻找特定点的难题（如 SVP, LWE）作为安全基础。这些问题已被证明在最坏情况 (worst-case) 下亦难以求解，且在平均情况 (average-case) 下亦能保障安全性 [S4]。

## 后量子标准 (ML-KEM/ML-DSA)
- **ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism):** 一种密钥封装机制，在提供高效实现的同时，利用格密码难题提供量子抗性。
- **ML-DSA (Module-Lattice-based Digital Signature Algorithm):** 数字签名标准，利用格密码数学结构保证强大的签名完整性。
格密码系统因其在当前标准化过程中展现出的强大“最坏情况到平均情况”归约性及高效性能，正成为 PQC 转换的核心 [S4]。
