---
layout: learn-module
title: Integration of OQS and oqs-provider
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-en
course_locale: en
lang: en
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
permalink: /learn/en/post-quantum-cryptography-migration-lab/liboqs-integration/
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
id: m5
slug: liboqs-integration
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- Understand the Open Quantum Safe (OQS) architecture and the role of oqs-provider.
- Understand how PQ (Post-Quantum) algorithms are integrated into TLS 1.3.
- Configure and verify a hybrid TLS handshake in a local environment.
- Consider the impact of KEM implementation optimization (e.g., AVX-512) on actual
  handshake performance.
worked_examples:
- 'Example 1: To verify that oqs-provider is loaded in OpenSSL, run the `openssl list
  -providers` command. The output must include the ''oqs'' provider.'
- 'Example 2: When performing a hybrid handshake, specify the key exchange group via
  command arguments, e.g., `openssl s_client -groups kyber768_x25519...`. This is
  a hybrid group that combines ML-KEM (Kyber) and classical Curve25519.'
lab:
  title: Hybrid TLS Testing in Local Environment
  steps:
  - Build and install liboqs and oqs-provider within an isolated Docker container.
  - Modify the OpenSSL configuration file (`openssl.cnf`) to activate the oqs provider.
  - Open two terminals and run `openssl s_server` in one and `openssl s_client` in
    the other in hybrid mode.
  - Use Wireshark to capture and analyze how the shared key group (Key Share) is transmitted
    in the ClientHello packet.
  - Check handshake success and session encryption algorithm information.
  safety:
  - Experiments must be performed only within an isolated local virtual environment.
  - Never use certificates or keys used for operational services.
  - Be careful not to include actual service traffic when capturing with Wireshark.
  deliverables:
  - Screenshot confirming activation of oqs-provider.
  - Hybrid handshake log file.
  - Analysis report of shared key group in Wireshark captured packets.
assignment:
  title: Migration Analysis Report Based on Cryptographic Agility
  deliverables:
  - TLS handshake performance measurement result data (CSV).
  - Analysis essay on the reasons for using hybrid mode and performance degradation.
  - Priority-based Post-Quantum Migration Roadmap.
  rubric:
  - Success of OQS toolchain build and execution.
  - Did you accurately describe hybrid mode operation through TLS packet analysis?
  - Is performance measurement data inclusive of experimental environment and version
    information and reproducible?
  - Is the migration roadmap logically authored based on the concept of cryptographic
    agility?
quiz:
- question: What is the core role of oqs-provider in OpenSSL?
  choices:
  - Hardware accelerator for encrypting network packets.
  - A layer that allows OpenSSL to call PQC algorithms of liboqs.
  - A service that issues public key certificates on the internet.
  - IDS tool for detecting attacks by quantum computers.
  answer_index: 1
  explanation: oqs-provider utilizes OpenSSL's provider structure to connect liboqs'
    algorithms so they can be directly used in OpenSSL applications.
- question: What is the primary reason for using 'hybrid mode' key exchange in TLS
    1.3?
  choices:
  - To increase performance by more than 100 times.
  - To ensure security against single algorithm implementation errors or future vulnerabilities.
  - To support all legacy clients.
  - To handshake using quantum computers.
  answer_index: 1
  explanation: Hybrid mode combines classical algorithms and PQC algorithms, serving
    as a multi-layered defense strategy to prepare for implementation defects or unknown
    vulnerabilities.
completion_criteria:
- Completion of building a local test environment based on oqs-provider.
- Completion of hybrid TLS handshake and packet capture verification.
- Completion of report including experimental results and analysis.
- Completion of Post-Quantum Migration Roadmap.
source_ids:
- S2
---

## Theory of OQS and oqs-provider Integration

To protect existing data transmissions from the threat of quantum computers, it is essential to integrate NIST-standard-based post-quantum algorithms (PQC) into existing protocols like TLS 1.3. The OQS (Open Quantum Safe) project provides major frameworks to accelerate this integration [S2].

### 1. liboqs and oqs-provider
- **liboqs**: The core library containing C-language implementations of PQC algorithms (ML-KEM, ML-DSA, etc.). It provides a unified API for various algorithms.
- **oqs-provider**: An intermediate layer that utilizes the OpenSSL 3 provider structure to help OpenSSL applications (e.g., `s_client`, `s_server`) natively use PQC algorithms in liboqs. This allows testing PQC features in existing TLS tools without modification.

### 2. PQ Integration Method for TLS 1.3
During the TLS 1.3 handshake process, PQC KEM replaces or supplements existing key exchanges (e.g., ECDH).
- **PQ-only mode**: Exchanges keys using only PQC KEM.
- **Hybrid mode**: Combines existing classical algorithms (ECDH) with PQC algorithms. This is a transitional strategy that secures post-quantum safety while maintaining classical security guarantees, protecting against potential PQC library implementation errors or future vulnerabilities.

### 3. Performance Considerations
PQC KEM can have larger key sizes or higher computational loads than existing algorithms, directly impacting handshake performance [S2]. Utilizing latest hardware instruction sets (e.g., AVX-512) to optimize polynomial multiplication and modular reduction can increase handshake speeds [S2].
