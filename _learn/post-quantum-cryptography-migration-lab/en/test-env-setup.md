---
layout: learn-module
title: Setting up Isolated Experimental Environments
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-en
course_locale: en
lang: en
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
permalink: /learn/en/post-quantum-cryptography-migration-lab/test-env-setup/
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
id: m4
slug: test-env-setup
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- Understand the configuration principles of isolated local development environments
  for Post-Quantum Cryptography (PQC) experiments and the roles of essential tools
  (liboqs, oqs-provider).
- Analyze the impact of KEM performance on handshake latency in protocols such as
  TLS 1.3.
- Design and build a reproducible experimental environment with fixed dependencies
  using Docker containers.
worked_examples:
- 'Example 1: Building an environment based on oqs-provider utilizing Dockerfile.
  Describes how to ensure build reproducibility by specifying versions for each library.'
- 'Example 2: Hybrid TLS handshake test using OpenSSL CLI. Describes how to simulate
  an ML-KEM-768-supported hybrid TLS 1.3 connection using ''openssl s_server'' and
  ''s_client''.'
lab:
  title: Building an Isolated PQC Testbed
  steps:
  - Prepare an experimental Docker container image base (Ubuntu 22.04 LTS or higher).
  - Clone liboqs and oqs-provider source code and check out specific commit hashes
    to lock versions.
  - Perform build by setting optimization levels (e.g., AVX2) when compiling liboqs
    using CMake.
  - Configure OpenSSL 3.x environment and activate oqs-provider.
  - Measure basic TLS 1.3 handshake performance standards through fixed loopback connections
    on local network interfaces.
  safety:
  - Experimental environments must be run only within isolated local containers.
  - Certificates, actual private keys, and customer data from operational environments
    must never be brought into containers.
  - Note that measurements generated during compilation and execution are considered
    public test data and are irrelevant to actual security policies.
  - When monitoring actual hardware or power, comply with the rated current and voltage
    ranges specified by the manufacturer.
  deliverables:
  - Dockerfile with locked dependency versions and build logs.
  - Terminal capture showing successful loading of the PQC algorithm list in OpenSSL.
  - Checksum (SHA-256) of the isolated development environment with completed configuration.
assignment:
  title: PQC Testbed Documentation and Evaluation
  deliverables:
  - Configuration diagram of the built testbed and specification of selected algorithm
    versions.
  - CSV of handshake time comparison data between classical algorithms and hybrid
    ML-KEM algorithms in the testbed environment.
  - Security policy report for maintaining isolated environments.
  rubric:
  - Possibility of locking dependency versions and reproducing builds (30%).
  - Success of hybrid TLS handshake in an isolated experimental environment (40%).
  - Clarity of algorithm configuration and measurement procedures and security compliance
    (30%).
quiz:
- question: What is the primary role of oqs-provider?
  choices:
  - Accelerates PQC algorithms at the hardware level.
  - Acts as an interface that allows Post-Quantum algorithms to be used in TLS protocols,
    etc., in OpenSSL 3.
  - Automatically renews security certificates in operational environments.
  - Blocks quantum computer attack vectors.
  answer_index: 1
  explanation: oqs-provider uses the OpenSSL provider architecture to integrate PQC
    algorithms into standard libraries, allowing existing applications to use PQC
    algorithms.
- question: Why should versions be locked in an isolated experimental environment?
  choices:
  - Because the latest version is always faster.
  - To ensure reproducibility and reduce measurement errors due to differences in
    execution environments between researchers.
  - To strengthen operational security.
  - To shorten build times.
  answer_index: 1
  explanation: Version locking is essential to ensure that the same environment can
    be reproduced, securing the integrity of performance measurement values and the
    objectivity of research.
completion_criteria:
- Successful configuration of a Docker-based isolated build environment.
- Demonstration of ML-KEM hybrid mode through oqs-provider.
- Submission of a report including experimental data measurement and security policies.
source_ids:
- S2
---

### Need for Isolated PQC Experimental Environments
To protect existing public-key cryptography (RSA, ECDH, etc.) from quantum computer threats, NIST has standardized post-quantum algorithms such as ML-KEM (based on Kyber) and ML-DSA (based on Dilithium). To evaluate the performance and security of these algorithms in a local environment, a reproducible environment with **Crypto-agility** is essential [S2].

#### 1. Key Components
*   **liboqs**: A C-language implementation of PQC algorithms, providing a foundation to test various KEM and signature algorithms.
*   **oqs-provider**: An interface that uses the OpenSSL 3 provider architecture to allow integrating PQC algorithms into existing TLS infrastructure.
*   **Hybrid Mode**: A transitional strategy that combines existing classical cryptography (ECDH) with PQC algorithms to maintain existing security levels despite potential vulnerabilities in PQC libraries [S2].

#### 2. The Core of Experimental Environments: Isolation and Reproducibility
Experiments must be completely separated from operational environments. By locking dependency versions using container technologies like Docker, one can reduce differences in execution results between researchers and accurately measure the effects of algorithm optimization (e.g., utilizing AVX-512) [S2]. When evaluating handshake performance, one should use fixed hardware and an isolated network to minimize latency uncertainty.
