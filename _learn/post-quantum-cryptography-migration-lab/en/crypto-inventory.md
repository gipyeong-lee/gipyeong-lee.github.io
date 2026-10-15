---
layout: learn-module
title: Cryptographic Asset Identification and Management
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-en
course_locale: en
lang: en
ref: learn:post-quantum-cryptography-migration-lab:crypto-inventory
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/crypto-inventory/
module_id: m3
permalink: /learn/en/post-quantum-cryptography-migration-lab/crypto-inventory/
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
id: m3
slug: crypto-inventory
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- Explain the concept and necessity of Cryptographic Inventory.
- Learn how to systematically classify encryption algorithms, libraries, and usage
  in an organization.
- Identify metadata management elements for Crypto-agility.
- Evaluate the risk of identified cryptographic assets to determine Post-Quantum migration
  priorities.
worked_examples:
- 'System scan result example: Identifying an asset as ''Using TLS 1.2(ECDHE-RSA-AES128-GCM-SHA256)''.
  In this case, recognize that RSA and ECDHE are exposed to quantum threats and categorize
  targets for ML-KEM/ML-DSA migration.'
- 'Crypto-agility self-checklist: If ''Is the algorithm hard-coded?'' is ''Yes'',
  increase risk score. If ''Is it possible to select cryptographic algorithms via
  configuration files?'' is ''No'', increase migration difficulty.'
lab:
  title: Cryptographic Asset Identification and Risk Assessment Lab
  steps:
  - Search source code of sample projects for keywords 'AES', 'RSA', 'ECC' to find
    where they are used.
  - Record identified cryptographic implementations (including libraries) in 'Cryptographic
    Asset Inventory CSV'.
  - Calculate risk scores for each asset based on 'security lifespan', 'quantum threat
    level', and 'data importance'.
  - Classify migration priorities (P0~P3) based on the calculated scores.
  safety:
  - Do not scan private keys or actual service certificates of systems currently in
    operation.
  - Use only dummy certificates (for testing) isolated within the virtual environment
    for testing.
  - Do not include actual secret values or encryption key values in the analysis results
    (CSV, documents).
  deliverables:
  - Cryptographic Asset Inventory CSV file (including algorithm, usage, library, library
    version).
  - Priority-based cryptographic asset risk assessment report (Markdown).
assignment:
  title: Cryptographic Agility Analysis and Migration Roadmap Establishment
  deliverables:
  - Cryptographic Asset Inventory CSV.
  - Decision table with migration priorities defined.
  - Post-Quantum Migration Roadmap.
  rubric:
  - Were cryptographic assets comprehensively identified?
  - Are risk assessment criteria objective and valid?
  - Does the migration roadmap follow the logical order of Post-Quantum technology
    migration?
  - Are specific technical suggestions included for improving cryptographic agility?
quiz:
- question: What is the primary purpose of Cryptographic Inventory?
  choices:
  - To optimize the performance of all encryption libraries.
  - To understand cryptographic dependencies within an organization to prepare for
    PQC migration.
  - To delete all encryption algorithms.
  - To force the use of asymmetric encryption only.
  answer_index: 1
  explanation: Cryptographic Inventory aims to efficiently perform PQC migration by
    systematically managing the locations and dependencies of encryption algorithms
    that need to be migrated.
- question: Which of the following is the most appropriate definition of Crypto-agility?
  choices:
  - The process of replacing hardware for stronger encryption.
  - The function that automates encryption library updates.
  - Flexibility to minimize code changes and quickly replace encryption algorithms
    when necessary.
  - Changing encryption keys very frequently.
  answer_index: 2
  explanation: Crypto-agility refers to the ability to adapt to changing security
    environments by minimizing the burden of code changes when replacing algorithms.
completion_criteria:
- Submit Cryptographic Asset Identification Inventory CSV and complete risk assessment.
- Author a report stating the migration difficulty and risk priority of each cryptographic
  asset.
- Achieve 100% correct answers in the quiz.
source_ids:
- S1
---

## Cryptographic Inventory

Cryptographic asset identification is the process of systematically listing all cryptographic algorithms, protocols, libraries, and the systems and data they are applied to within an organization. This is the first step in preparing for the migration to Post-Quantum Cryptography (PQC), and identifying dependencies on the cryptographic algorithms being protected is key [S1].

### 1. Key Management Targets
- **Algorithms and Protocols**: TLS, SSH, code signing, data encryption (AES, RSA, ECC, etc.), etc.
- **Infrastructure**: Certificate Authorities (CA), Key Management Systems (KMS), HSM, cloud key storage.
- **Software**: Encryption library versions (OpenSSL, BoringSSL, etc.) and static/dynamic linkage status.

### 2. Crypto-agility
Crypto-agility refers to the ability to quickly replace encryption algorithms while minimizing code changes. For this, systems should not be hard-coded to specific algorithms but should have an abstraction layer that allows selecting algorithms through configuration files.

### 3. Risk Assessment Criteria
- **Data Lifecycle**: Does the encrypted data need to remain secret in the future? (e.g., data at risk of being stolen now and decrypted in the future)
- **Migration Difficulty**: Is hardware replacement needed, or is software update sufficient?
- **Regulation and Compliance**: Alignment with NIST PQC standard application timelines.
