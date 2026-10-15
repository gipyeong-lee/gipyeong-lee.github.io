---
layout: learn-module
title: Quantum Threats and Lattice-based Cryptography
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-en
course_locale: en
lang: en
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
permalink: /learn/en/post-quantum-cryptography-migration-lab/quantum-threat-model/
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
id: m1
slug: quantum-threat-model
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- Understand the threat models quantum computers pose to modern cryptographic systems
  (RSA, ECC).
- Analyze the mathematical foundations and security proofs of Lattice-based Cryptography.
- Learn the design principles of NIST-recommended Post-Quantum Cryptographic standards
  (ML-KEM, ML-DSA).
- Describe the efficiency and security characteristics (worst-case hardness) of lattice-based
  algorithms.
worked_examples:
- 'Example 1: Analysis of the impact of quantum computers on RSA - RSA is based on
  the difficulty of factoring large integers. Shor''s algorithm reduces the complexity
  of factoring n-bit integers from exponential to polynomial time, decrypting ciphertext
  immediately.'
- 'Example 2: Understanding the Lattice-based Hard Problem (LWE) concept - Consider
  a system of linear equations A*s + e = t with a secret vector s and error e added.
  Lattice-based cryptography is based on the difficulty of the ''Learning With Errors''
  problem, which makes finding s from matrix A and result t difficult.'
lab:
  title: Setting up Basic Lattice Cryptography Environment and Visualization
  steps:
  - Create a Python 3 virtual environment in an isolated Linux/Docker environment.
  - Install and compile the liboqs library.
  - Write a script to collect key sizes and computation times according to parameter
    changes in the lattice-based LWE problem.
  - Run data analysis and visualization notebooks.
  safety:
  - All experiments must be performed within an isolated local virtual environment.
  - Strictly prohibited to use actual operational certificates, private keys, or customer
    data.
  - Do not treat research libraries as operational service security tools.
  deliverables:
  - Environment setup logs and compilation outputs.
  - Algorithm performance (key size, time) comparative analysis data.
  - Report on characteristics of lattice-based cryptography.
assignment:
  title: Writing a Quantum Threat Analysis Report
  deliverables:
  - Document summarizing quantum threat models and lattice-based cryptographic theory.
  - Comparison table of major PQC algorithms (ML-KEM, ML-DSA).
  rubric:
  - Accurately explains the principles of Shor's algorithm.
  - Logically describes the concept of worst-case hardness in lattice-based cryptography.
  - Describes the challenges faced by modern cryptography based on the provided sources
    [S3, S4].
quiz:
- question: What threat does Shor's algorithm pose to existing PKI?
  choices:
  - It decrypts all symmetric key encryption unconditionally.
  - It solves integer factorization and discrete logarithm problems in polynomial
    time.
  - It completely removes the collision resistance of hash functions.
  - It slows down the processing speed of quantum computers.
  answer_index: 1
  explanation: Shor's algorithm threatens existing public-key cryptosystems by solving
    integer factorization (basis of RSA) and discrete logarithm problems (basis of
    ECC) in polynomial time.
- question: Why is Lattice-based Cryptography promising?
  choices:
  - Because worst-case hardness can be converted to average-case hardness.
  - Because it is much faster than all symmetric key encryption.
  - Because it cannot be solved even by quantum computers.
  - Because it uses no computer memory at all.
  answer_index: 0
  explanation: Lattice-based cryptography has the mathematical strength of ensuring
    average-case security from worst-case hardness[S4].
completion_criteria:
- Complete theory learning and submit quantum threat report.
- Successfully execute basic algorithms using liboqs in the lab environment.
- Achieve a correct answer rate of 80% or higher for each quiz item.
source_ids:
- S3
- S4
---

## Quantum Threat Model
Modern public-key cryptography (PKI) primarily relies on the hardness of integer factorization (RSA) and discrete logarithm problems (ECC). Shor's algorithm can solve these problems in polynomial time using a quantum computer, which implies that it effectively nullifies all current standard PKI[S3].

## Lattice-based Cryptography
Lattice-based cryptography uses problems such as finding points in a lattice from basis vectors (e.g., SVP, LWE) in high-dimensional space as hard problems. It has been proven that these problems are hard even in the worst-case, and security is guaranteed in the average-case as well[S4].

## Post-Quantum Standards (ML-KEM/ML-DSA)
- **ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism):** A key encapsulation mechanism providing quantum resistance using lattice-based hard problems along with efficient implementation.
- **ML-DSA (Module-Lattice-based Digital Signature Algorithm):** A digital signature standard ensuring strong signature integrity using lattice-based mathematical structures.
Lattice-based systems are becoming the center of PQC migration, proving strong worst-case to average-case hardness and efficient performance in the current standardization process[S4].
