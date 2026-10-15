---
layout: learn-module
title: 理解 ML-KEM 與 ML-DSA 標準
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-tw
course_locale: zh-tw
lang: zh-tw
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
permalink: /learn/zh-tw/post-quantum-cryptography-migration-lab/nist-pq-standards/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e5164bbefc324eff94b7957c62695f66
translation_run_id: 00e08f372b7e4cc3a87aa790941d7690
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
- 說明格點基礎密碼體系 (Lattice-based cryptography) 的數學基礎與安全性依據。
- 理解 NIST 標準 ML-KEM (金鑰封裝機制) 的運作原理。
- 掌握 NIST 標準 ML-DSA (數位簽章演算法) 的結構特性。
- 分析格點密碼學相較於其他密碼方式 (基於代碼、基於雜湊) 具有實務優勢的原因。
worked_examples:
- 範例 1：格點基礎 KEM 安全強度比較。ML-KEM-512, 768, 1024 分別對應 NIST 安全強度 1, 3, 5 等級。這目標是達到與傳統密碼
  AES-128, 192, 256 相似的安全水平。
- 範例 2：模組格點 (Module Lattice) 概念應用。使用向量與矩陣使運算效率化，藉此優化效能但維持安全性。
lab:
  title: ML-KEM 與 ML-DSA 演算法基礎實驗
  steps:
  - 安裝 liboqs 並設定環境變數。
  - 使用範例 Python 程式碼執行 ML-KEM 金鑰對產生與封裝過程。
  - 執行使用 ML-DSA 對訊息進行簽章與驗證的腳本。
  - 測量並記錄各運算所需的時間。
  safety:
  - 不存取實驗用虛擬環境以外的系統憑證或真實金鑰檔案。
  - liboqs 函式庫僅供研究與測試用途，勿誤認為營運環境安全解決方案。
  - 所有實驗資料均保留在本地虛擬環境中，不傳送至外部網路。
  deliverables:
  - 包含運算時間測量資料的 CSV 檔案
  - 演算法實作執行結果擷圖
  - 實習過程摘要日誌
assignment:
  title: 後量子密碼標準分析報告
  deliverables:
  - ML-KEM 與 ML-DSA 演算法特徵摘要表
  - 格點基礎系統在實際遷移時應考慮的效能限制 (金鑰大小等) 分析
  - 利用研究用函式庫進行測試的限制點說明
  rubric:
  - 是否準確技術描述了標準演算法的數學基礎？
  - 是否分析了格點基礎系統的優點與限制？
  - 是否顯示了對安全威脅模型的正確理解？
quiz:
- question: 下列哪項是格點基礎系統主導實務標準化的主要原因？
  choices:
  - 因為它擁有最短的安全歷史
  - 因為它能從最壞情況還原為平均情況，且具備高效實作可能性
  - 因為它很容易被量子演算法破解
  - 因為它僅使用基於代碼的密碼學來最大化安全性
  answer_index: 1
  explanation: 格點基礎系統憑藉強大的數學還原依據與高效實作可行性，成為 NIST 標準化的核心 [S4]。
- question: ML-KEM 基礎的數學問題類型是什麼？
  choices:
  - 質因數分解問題
  - 橢圓曲線離散對數問題
  - 模組學習錯誤問題 (MLWE)
  - 雜湊碰撞問題
  answer_index: 2
  explanation: ML-KEM 以模組格點基礎的學習錯誤 (MLWE) 問題作為安全依據。
completion_criteria:
- 理論學習確認測驗全數正確通過
- 提交包含實驗過程與測量資料的報告
- 提交確認遵守實習安全指南並於隔離環境進行測試的檢查清單
source_ids:
- S4
---

## 理解 ML-KEM 與 ML-DSA 標準

### 1. 格點密碼學的興起
目前主導實務標準化的是格點基礎 (Lattice-based) 系統。這是因為從最壞情況 (worst-case) 到平均情況 (average-case) 存在強大的數學還原 (reductions)，且能進行高效實作 [S4]。另一方面，基於代碼 (Code-based) 或基於雜湊 (Hash-based) 的方式扮演著保守錨點 (conservative anchors) 的角色，具有更長的安全歷史或僅需最小化假設的特性 [S4]。

### 2. ML-KEM (Module-Lattice Key Encapsulation Mechanism)
ML-KEM 基於先前稱為 Kyber 的演算法。基於模組格點問題 (Module Learning With Errors, MLWE)，運作流程如下：
- **KeyGen:** 在模組格點內產生公開金鑰與私密金鑰。
- **Encapsulation:** 使用公開金鑰產生共享秘密值 (Shared Secret) 與封裝後的金鑰 (Ciphertext)。
- **Decapsulation:** 使用私密金鑰從封裝後的金鑰還原原始共享秘密值。

### 3. ML-DSA (Module-Lattice Digital Signature Algorithm)
ML-DSA 基於 Dilithium，使用「Fiat-Shamir with Aborts」技術。透過格點問題的困難度提供抗偽造性，是在簽章大小與公開金鑰大小之間取得平衡的實務標準。

### 4. 安全假設
格點基礎系統的安全性與尋找最短向量問題 (Shortest Vector Problem, SVP) 密切相關。與量子電腦的「Shor 演算法」能有效破解現有的 RSA 或 ECC 不同，格點問題被假設即使使用量子演算法也無法在多項式時間內求解。
