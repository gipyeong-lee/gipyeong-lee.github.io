---
layout: learn-module
title: Understanding ML-KEM and ML-DSA Standards
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-en
course_locale: en
lang: en
ref: learn:post-quantum-cryptography-migration-lab:nist-pq-standards
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/nist-pq-standards/
module_id: m2
permalink: /learn/en/post-quantum-cryptography-migration-lab/nist-pq-standards/
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
id: m2
slug: nist-pq-standards
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- Explain the mathematical foundations and security proofs of Lattice-based cryptography.
- Understand the operational principles of the NIST standard ML-KEM (Key Encapsulation
  Mechanism).
- Identify the structural characteristics of the NIST standard ML-DSA (Digital Signature
  Algorithm).
- Analyze why lattice cryptography holds practical advantages over other cryptographic
  methods (code-based, hash-based).
worked_examples:
- 'Example 1: Comparison of security strength of lattice-based KEM. ML-KEM-512, 768,
  and 1024 correspond to NIST security strength levels 1, 3, and 5, respectively.
  These target security levels similar to classical AES-128, 192, and 256.'
- 'Example 2: Applying the Module Lattice concept. Operations are made efficient using
  vectors and matrices to optimize performance while maintaining security strength
  compared to general lattices.'
lab:
  title: Basic Experiments with ML-KEM and ML-DSA Algorithms
  steps:
  - Install liboqs and set environment variables.
  - Execute the process of generating ML-KEM key pairs and encapsulation using sample
    Python code.
  - Execute a script to sign and verify messages using ML-DSA.
  - Measure and record the time taken for each operation.
  safety:
  - Do not access system certificates or actual key files outside the experimental
    virtual environment.
  - Use the liboqs library only for research and test purposes and do not mistake
    it for an operational environment security solution.
  - All experimental data is kept in the local virtual environment and not transmitted
    to external networks.
  deliverables:
  - CSV file containing operation time measurement data.
  - Capture of algorithm implementation execution results.
  - Summary log of the lab process.
assignment:
  title: Post-Quantum Cryptography Standard Analysis Report
  deliverables:
  - Summary table of algorithmic features of ML-KEM and ML-DSA.
  - Analysis of performance constraints (key size, etc.) to consider during actual
    migration to lattice-based systems.
  - Description of limitations of tests using research libraries.
  rubric:
  - Did you accurately describe the mathematical basis of the standard algorithm?
  - Did you analyze the advantages and limitations of lattice-based systems?
  - Does it show a correct understanding of security threat models?
quiz:
- question: Which of the following is the primary reason why lattice-based systems
    are driving practical standardization?
  choices:
  - Because they have the shortest security history.
  - Because they allow for reduction from worst-case to average-case and allow efficient
    implementation.
  - Because they can be easily solved by quantum algorithms.
  - Because they maximize security using only code-based cryptography.
  answer_index: 1
  explanation: Lattice-based systems are at the center of NIST standardization due
    to strong mathematical reduction grounds and potential for efficient implementation
    [S4].
- question: What type of mathematical problem is ML-KEM based on?
  choices:
  - Integer factorization problem.
  - Elliptic curve discrete logarithm problem.
  - Module Learning With Errors (MLWE) problem.
  - Hash collision problem.
  answer_index: 2
  explanation: ML-KEM bases its security on the Module Lattice-based Learning With
    Errors (MLWE) problem.
completion_criteria:
- Pass all theory verification quizzes with correct answers.
- Submit a report including experimental processes and measurement data.
- Submit a checklist confirming adherence to lab safety guidelines and that tests
  were performed in an isolated environment.
source_ids:
- S4
---

## Understanding ML-KEM and ML-DSA Standards

### 1. The Rise of Lattice-based Cryptography
Lattice-based systems are currently driving practical standardization. This is because there exist strong mathematical reductions from worst-case to average-case, and efficient implementation is possible [S4]. On the other hand, code-based or hash-based methods serve as conservative anchors, requiring a longer security history or minimal assumptions [S4].

### 2. ML-KEM (Module-Lattice Key Encapsulation Mechanism)
ML-KEM is based on the algorithm previously known as Kyber. It is based on the Module Learning With Errors (MLWE) problem and follows this flow:
- **KeyGen:** Generate public and secret keys within a module lattice.
- **Encapsulation:** Generate a shared secret and encapsulated key (Ciphertext) using the public key.
- **Decapsulation:** Recover the original shared secret from the encapsulated key using the secret key.

### 3. ML-DSA (Module-Lattice Digital Signature Algorithm)
ML-DSA is based on Dilithium and uses the 'Fiat-Shamir with Aborts' technique. It provides forgery resistance through the hardness of lattice problems and is a practical standard that balances signature size and public key size.

### 4. Security Assumptions
The security of lattice-based systems is closely related to the Shortest Vector Problem (SVP). Unlike Shor's algorithm, which efficiently breaks RSA or ECC, lattice problems are assumed not to be solvable in polynomial time even by quantum algorithms.
