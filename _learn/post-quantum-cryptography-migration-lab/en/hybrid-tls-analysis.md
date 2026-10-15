---
layout: learn-module
title: Hybrid TLS Handshake Analysis
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-en
course_locale: en
lang: en
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
permalink: /learn/en/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
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
id: m7
slug: hybrid-tls-analysis
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m6
objectives:
- Explain the vulnerabilities of TLS 1.3 in a quantum threat environment.
- Understand the ML-KEM-based hybrid TLS handshake structure.
- Measure the performance of hybrid mode in a local OQS (Open Quantum Safe)-based
  environment.
- Analyze the handshake process where classical algorithms and PQ algorithms are combined
  through packet capture.
worked_examples:
- 'Example 1: Hybrid key exchange process - The client transmits the classical shared
  secret value and the PQC encapsulation result value to the server. After decapsulation,
  the server combines the two shared secrets in the KDF (Key Derivation Function)
  to generate a session key.'
- 'Example 2: Handshake latency analysis - Comparative analysis is performed on the
  phenomenon where network transmission time increases as key size increases when
  applying PQ algorithms. The difference in Handshakes per second before and after
  applying performance optimizations (e.g., using AVX-512) is quantified[S2].'
lab:
  title: OQS-based Hybrid TLS Handshake Reproduction Experiment
  steps:
  - Build an OpenSSL 3 build environment with integrated liboqs and oqs-provider within
    an isolated Docker environment.
  - Configure existing ECDH mode and ML-KEM-based hybrid mode (e.g., secp256r1_mlkem768).
  - Execute TLS 1.3 handshake between the two modes using a local loopback interface.
  - Capture key exchange data fields in ClientHello and ServerHello messages using
    Wireshark.
  - Measure the average time of 100 or more handshakes using an execution time measurement
    script and record the overhead of hybrid mode.
  safety:
  - This experiment is performed only on a local isolated loopback interface and generates
    no external network traffic.
  - Never use operational security assets such as actual certificates, private keys,
    or user data.
  - Note that learning-purpose OQS libraries are experimental tools and not to be
    used for actual operational security services.
  - Delete all generated temporary keys and local measurement data upon experiment
    conclusion.
  deliverables:
  - Configuration and execution log files.
  - Wireshark packet capture file (.pcapng) and key exchange field analysis notes.
  - Handshake performance comparison measurement CSV data.
assignment:
  title: TLS 1.3 Hybrid Migration Performance Analysis Report
  deliverables:
  - Handshake latency comparison analysis graph and data visualization.
  - Hybrid mode packet analysis and summary of key exchange algorithm characteristics.
  - Decision table for performance and security considerations expected when applied
    to operational environments.
  rubric:
  - Reproducibility of the experiment (whether environment setup and scripts are specified).
  - Accuracy of packet analysis (identification of key exchange fields).
  - Logical interpretation of performance measurement data.
  - Connectivity between theoretical security assumptions and experimental results.
quiz:
- question: What is the primary security advantage of a hybrid TLS handshake?
  choices:
  - Increases speed by drastically reducing handshake steps.
  - Maintains secrecy if at least one of either the classical algorithm or the PQC
    algorithm is secure.
  - Completely eliminates network transmission costs.
  - Reduces the complexity of certificate management.
  answer_index: 1
  explanation: Hybrid mode is a transitional strategy designed to maintain security
    if one of the two algorithms remains secure by combining the results of existing
    algorithms and PQC algorithms.
- question: What is the PQ algorithm element that has the greatest impact on TLS 1.3
    handshake performance?
  choices:
  - Consider only network latency.
  - Computational cost of KEM (Key Encapsulation Mechanism) key generation, encapsulation,
    and decapsulation operations.
  - Server disk I/O speed.
  - Client browser version.
  answer_index: 1
  explanation: The computational cost of KEM algorithms is directly linked to TLS
    1.3 handshake performance, and optimizing this is key to performance improvement
    [S2].
completion_criteria:
- Successful reproduction of liboqs-based hybrid TLS handshake in a local environment.
- Verification of hybrid key exchange messages through Wireshark analysis.
- Submission of a result analysis report based on performance measurement data.
- Confirmation of adherence to safety constraints (data isolation, no use of production
  keys).
source_ids:
- S2
---

### Hybrid TLS Handshake Theory

Current TLS 1.3 relies on classical public-key cryptography such as ECDH (Elliptic Curve Diffie-Hellman), which is exposed to attack threats upon the emergence of sufficiently powerful quantum computers[S2]. In response, active research is underway to integrate Post-Quantum Cryptography (PQC) such as the NIST standard ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism)[S2].

#### Security Assumptions of Hybrid Mode
Before full PQC migration, 'Hybrid mode' combining classical algorithms and PQ algorithms is used for operational stability. This method combines the shared secrets of the two algorithms and is designed to guarantee the secrecy of communications even if only one of the two algorithms remains secure.

#### Performance Considerations
TLS 1.3 handshake performance is directly dependent on the computational cost of KEM[S2]. In particular, operation efficiency in the Key Generation, Encapsulation, and Decapsulation stages determines total handshake speed. Recently, techniques to increase handshake performance by accelerating polynomial multiplication and modular reduction processes through instruction set optimizations like AVX-512 are being applied[S2].
