---
layout: learn-module
title: Drafting a Migration Prioritization Report
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-en
course_locale: en
lang: en
ref: learn:post-quantum-cryptography-migration-lab:migration-roadmap
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/migration-roadmap/
module_id: m8
permalink: /learn/en/post-quantum-cryptography-migration-lab/migration-roadmap/
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
id: m8
slug: migration-roadmap
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m7
objectives:
- Understand risk and business impact analysis frameworks for Post-Quantum Cryptography
  (PQC) migration.
- Determine migration priorities based on cryptographic asset inventory data.
- Establish technical strategies to ensure Cryptographic Agility.
- Structure a final migration roadmap and validation report.
worked_examples:
- 'Example 1: Priority calculation based on data lifecycle - A personal information
  database preserved for 20 years is evaluated with a higher PQC migration priority
  than log data preserved for 5 years.'
- 'Example 2: Hybrid TLS configuration case - Analysis of a hybrid model designed
  to combine existing ECDH and ML-KEM, ensuring communication confidentiality even
  if only one of the two algorithms remains secure.'
lab:
  title: Migration Roadmap Simulation
  steps:
  - Load the inventory CSV data created in the previous module.
  - Write a Python script that calculates a [Risk * Criticality * Shelf Life] score
    for each asset.
  - Develop hybrid implementation plans for the top 3 priority assets.
  - Describe potential compatibility issues and countermeasures (Fall-back strategy)
    during migration.
  safety:
  - Perform all calculations and analysis only in an independent, isolated virtual
    environment.
  - Do not modify the actual cryptographic configuration of production servers.
  - Review analysis notebooks to ensure actual key material is not included.
  deliverables:
  - Prioritized inventory CSV analysis.
  - Technical decision-making table including migration plans.
assignment:
  title: PQC Migration Prioritization Report
  deliverables:
  - Cryptographic Agility Analysis Report (PDF)
  - Risk-based migration roadmap (including tables)
  rubric:
  - Reasonable prioritization logic based on data shelf life and exposure risk.
  - Consideration of cryptographic agility through the introduction of hybrid cryptographic
    schemes.
  - Step-by-step feasibility of the migration plan.
  - Consistency with experimental results and data inventory.
quiz:
- question: Which data characteristic should be most considered when determining cryptographic
    migration priority?
  choices:
  - Programming language in which the data is used.
  - Data Security Shelf Life.
  - Number of system developers.
  - Capacity of the latest data storage.
  answer_index: 1
  explanation: Quantum threats imply a risk that data may be decrypted in the future,
    so data that must remain confidential for a long time requires PQC migration first.
- question: What software design approach is recommended for Cryptographic Agility?
  choices:
  - Using hard-coded cryptographic algorithms.
  - Abstracting and separating encryption modules from business logic.
  - Closed structure using only a single algorithm.
  - Direct reference to operating system-level cryptographic libraries.
  answer_index: 1
  explanation: A structure that separates the cryptographic engine from logic to minimize
    code changes during algorithm replacement is key to ensuring cryptographic agility.
completion_criteria:
- Submission of an inventory analysis file with migration priorities specified.
- Preparation of a migration roadmap report incorporating cryptographic agility considerations.
- Completion of a reproduction package containing all lab code and measurements.
source_ids:
- S1
---

### Migration Prioritization Strategy

Migration to NIST post-quantum standards (ML-KEM, ML-DSA) begins with a system-wide assessment of cryptographic assets. Migration priority is determined not simply by the degree of algorithm obsolescence, but by data shelf life, cryptographic exposure risk, and the strategic importance of the system [S1].

#### 1. Assessment Criteria
To determine migration urgency, the following criteria are used:
- **Data Security Shelf Life:** Impact when encrypted data is decrypted by future quantum computers (e.g., data requiring confidentiality for 10 years or more).
- **System Agility:** Whether current cryptographic implementations are hard-coded or if algorithms can be replaced via configuration files.
- **Technical Debt:** Dependencies using the cryptographic module and maintainability.

#### 2. Ensuring Cryptographic Agility
The key to a migration roadmap is to minimize code changes during algorithm replacement. Using an abstraction layer to decouple business logic from the cryptographic engine, and employing a hybrid key exchange approach to ensure both the stability of existing algorithms and the quantum resistance of PQC, is the recommended strategy.
