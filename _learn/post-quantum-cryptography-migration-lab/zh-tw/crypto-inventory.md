---
layout: learn-module
title: 密碼資產識別與管理
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-tw
course_locale: zh-tw
lang: zh-tw
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
permalink: /learn/zh-tw/post-quantum-cryptography-migration-lab/crypto-inventory/
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
id: m3
slug: crypto-inventory
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- 說明密碼資產識別 (Cryptographic Inventory) 的概念與必要性。
- 學習有系統地分類組織內密碼加密演算法、函式庫與使用場所的方法。
- 掌握為了密碼敏捷性 (Crypto-agility) 的後設資料管理要素。
- 評估已識別密碼資產的風險，決定後量子遷移優先級。
worked_examples:
- 系統掃描結果範例：識別出資產 '使用 TLS 1.2 (ECDHE-RSA-AES128-GCM-SHA256)'。在此情況下，須認知到 RSA 與 ECDHE
  面臨量子威脅，並將 ML-KEM/ML-DSA 列為遷移對象。
- 密碼敏捷性自我檢查表：若問『演算法是否硬編碼？』回答『是』，則提高風險分數。若問『是否能透過設定檔選擇密碼演算法？』回答『否』，則提高遷移困難度。
lab:
  title: 密碼資產識別與風險評估實作
  steps:
  - 針對樣本專案的原始程式碼，執行『AES』、『RSA』、『ECC』關鍵字搜尋以尋找使用場所。
  - 將識別出的密碼實作 (包含函式庫) 記錄於『密碼資產 Inventory CSV』。
  - 針對各項資產，根據『安全壽命』、『量子威脅水準』、『資料重要性』計算風險分數。
  - 根據計算分數將遷移優先級 (P0~P3) 進行分類。
  safety:
  - 不掃描實際營運中的系統私鑰或實際服務憑證。
  - 為進行測試，僅使用虛擬環境內隔離的 dummy 憑證 (測試用)。
  - 分析產出物 (CSV, 文件) 中不包含實際秘密值或加密金鑰值。
  deliverables:
  - 密碼資產 Inventory CSV 檔案 (包含演算法、使用場所、函式庫、函式庫版本)
  - 基於優先級的密碼資產風險評估報告 (Markdown)
assignment:
  title: 密碼敏捷性分析與遷移路線圖規劃
  deliverables:
  - 密碼資產 Inventory CSV
  - 定義遷移優先級的決策表
  - 後量子遷移路線圖
  rubric:
  - 密碼資產識別是否全面？
  - 風險評估標準是否客觀且妥當？
  - 遷移路線圖是否遵循後量子技術轉換的邏輯順序？
  - 是否包含改善密碼敏捷性的具體技術建議？
quiz:
- question: 密碼資產識別 (Cryptographic Inventory) 的主要目的是什麼？
  choices:
  - 為了優化所有加密函式庫的效能
  - 為了掌握組織內密碼依賴性，以準備 PQC 遷移
  - 為了刪除所有加密演算法
  - 為了強制僅使用非對稱密碼學
  answer_index: 1
  explanation: 密碼資產識別旨在有系統地管理應遷移加密演算法的位置與依賴性，以高效執行 PQC 遷移。
- question: 下列關於密碼敏捷性 (Crypto-agility) 的定義何者最恰當？
  choices:
  - 為了更強的加密而更換硬體的過程
  - 自動化加密函式庫更新的功能
  - 將程式碼變更最小化，並在必要時能快速更換加密演算法的靈活性
  - 非常頻繁地更換加密金鑰
  answer_index: 2
  explanation: 密碼敏捷性意指將更換演算法時的程式碼變更負擔最小化，以適應不斷變化的安全環境的能力。
completion_criteria:
- 提交密碼資產識別 Inventory CSV 並完成風險評估
- 撰寫明列各密碼資產遷移困難度及風險優先級的報告
- 測驗項目達到 100% 正確率
source_ids:
- S1
---

## 密碼資產識別 (Cryptographic Inventory)

密碼資產識別是指將組織內使用的所有加密演算法、協定、函式庫，以及這些演算法所應用的系統與資料進行有系統清單化的過程。這是準備遷移至後量子密碼 (PQC) 的第一步，關鍵在於明確掌握受保護的加密演算法依賴性 [S1]。

### 1. 主要管理對象
- **演算法與協定**: TLS, SSH, 程式碼簽章, 資料加密 (AES, RSA, ECC 等) 等。
- **基礎設施**: 憑證授權單位 (CA), 金鑰管理系統 (KMS), HSM, 雲端金鑰儲存庫。
- **軟體**: 加密函式庫版本 (OpenSSL, BoringSSL 等) 以及靜態/動態連結狀態。

### 2. 密碼敏捷性 (Crypto-agility)
密碼敏捷性意指在將程式碼變更最小化的同時，能夠快速更換加密演算法的能力。為此，系統不應將特定演算法硬編碼，而應擁有能透過設定檔選擇演算法的抽象層。

### 3. 風險評估標準
- **資料生命週期**: 加密後的資料在未來是否仍需維持隱密？ (例如：現在被竊取並在未來被解密的風險資料)
- **遷移困難度**: 是否需要更換硬體，還是僅需軟體更新即可？
- **法規與遵循**: 是否與 NIST PQC 標準應用時間點對齊。
