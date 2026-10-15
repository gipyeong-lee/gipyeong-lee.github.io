---
layout: learn-module
title: Performance Evaluation and Benchmarking
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-en
course_locale: en
lang: en
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
permalink: /learn/en/post-quantum-cryptography-migration-lab/performance-benchmarking/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e5164bbefc324eff94b7957c62695f66
translation_run_id: ed63e04456d444fdb25fb34dc6a5dbd0
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
- Understand the performance evaluation indicators (time, memory, throughput) for
  post-quantum cryptographic algorithms (ML-KEM).
- Analyze the impact of KEM operations on performance in the TLS 1.3 handshake process.
- Benchmark the performance of hybrid cryptographic modes utilizing the Liboqs and
  oqs-provider framework.
worked_examples:
- 'Example 1: Benchmarking a single KEM operation using Liboqs

  A method to measure the operation times of `keypair`, `encaps`, and `decaps` for
  `ML-KEM-768` using the Python `timeit` module and saving results to CSV.'
- 'Example 2: Measuring Hybrid TLS 1.3 handshake throughput

  An analysis procedure for calculating Handshakes Per Second (TPS) by measuring the
  total time taken for 100 connections using `s_client` and `s_server` in a local
  server/client environment with oqs-provider applied.'
lab:
  title: PQC Performance Benchmarking Lab
  steps:
  - Install liboqs and oqs-provider in an isolated development environment and verify
    environment settings.
  - Write a benchmarking Python script to measure the operation time of the ML-KEM
    algorithm.
  - Execute Wireshark to capture TLS handshake packets and analyze data size changes
    in hybrid mode.
  - Graph operation time and throughput indicators based on measured data.
  safety:
  - Experiments must be performed only within a local isolated environment, and certificates
    or keys from actual operational environments must never be used.
  - Monitor system resources as high CPU load may occur during the benchmarking process.
  - Be careful not to include actual secret values or key data in capture files.
  deliverables:
  - Operation performance measurement script (.py).
  - Measured result CSV data.
  - Performance comparison analysis report by algorithm (.md or .ipynb).
assignment:
  title: Performance Evaluation Report Based on Cryptographic Agility
  deliverables:
  - Analysis of algorithm selection reasons and security/performance trade-offs.
  - Data visualization materials for benchmarking.
  - Migration roadmap revision based on performance results.
  rubric:
  - Is benchmarking data measurable in a reproducible and independent environment?
  - Did you accurately analyze the technical causes of performance degradation (key
    size, operation complexity)?
  - Did you discuss the benefits and costs of hybrid mode in a balanced way?
quiz:
- question: Which factor related to PQC algorithms is most important for TLS 1.3 handshake
    performance?
  choices:
  - Block size of symmetric key encryption algorithm.
  - Operation time of KEM key generation and encapsulation.
  - Type of hash algorithm.
  - Type of server operating system.
  answer_index: 1
  explanation: TLS 1.3 handshake performance is largely dependent on the operation
    efficiency of the KEM algorithm [S2].
- question: Why is hybrid mode used during performance evaluation?
  choices:
  - Because it is always faster than traditional algorithms.
  - To maintain security while preparing for PQC's security threats.
  - To reduce network bandwidth.
  - To minimize computational resources.
  answer_index: 1
  explanation: Hybrid mode combines PQC's future security with traditional algorithms'
    verified security, enabling gradual migration.
completion_criteria:
- Secure benchmarking script execution and result data.
- Submission and passing of performance evaluation report.
- Completion of TLS hybrid mode performance analysis.
source_ids:
- S2
---

## Performance Evaluation and Benchmarking

Migration to Post-Quantum Cryptography (PQC) is not just about algorithm replacement, but a problem directly linked to the performance of existing network protocols (e.g., TLS 1.3). In particular, KEM (Key Encapsulation Mechanism) operations directly impact the handshake latency and server connection processing throughput (handshakes per second) [S2].

### Performance Indicators
1. **Computation Time:** CPU cycles or time (ms) spent on key generation (KeyGen), encapsulation (Encaps), and decapsulation (Decaps).
2. **Data Size:** Size of public keys and encapsulated text (ciphertext). This determines network bandwidth consumption and potential for fragmentation.
3. **Throughput:** Number of handshakes processable per second. Optimized implementations (e.g., utilizing AVX-512) increase polynomial multiplication and modular operation speed, greatly improving throughput [S2].

### Hybrid Mode
During migration, a hybrid approach using traditional algorithms (ECDH) together with PQC (ML-KEM) is recommended. This is to secure PQC's security benefits while preparing for PQC's potential vulnerabilities. Hybrid modes have increased computational complexity, so performance degradation must be closely evaluated [S2].
