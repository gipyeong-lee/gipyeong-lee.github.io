---
layout: learn-module
title: 編寫轉換優先順序報告
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-tw
course_locale: zh-tw
lang: zh-tw
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
permalink: /learn/zh-tw/post-quantum-cryptography-migration-lab/migration-roadmap/
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
id: m8
slug: migration-roadmap
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m7
objectives:
- 理解用於後量子密碼 (PQC) 轉換的風險及業務影響分析架構
- 基於密碼資產清單數據決定轉換優先順序
- 建立確保密碼敏捷性 (Cryptographic Agility) 的技術策略
- 規劃最終轉換路線圖及結構化驗證報告
worked_examples:
- 範例 1：基於資料生命週期的優先順序計算 - 需保存 20 年的人事資料庫，其 PQC 轉換優先順序評估高於保存 5 年的日誌資料。
- 範例 2：混合式 TLS 設定案例 - 結合既有的 ECDH 與 ML-KEM，設計為即便其中一種演算法失效，仍能維持通訊機密性的混合式模型分析。
lab:
  title: 轉換路線圖模擬
  steps:
  - 載入前一模組中編寫的清單 CSV 數據。
  - 編寫 Python 指令碼，計算各資產的 [風險 * 重要性 * 壽命] 分數。
  - 針對優先順序前 3 項的資產建立混合式實現計畫。
  - 技術性描述轉換時可能發生的相容性問題及其對應策略 (Fall-back 策略)。
  safety:
  - 所有計算及分析僅在獨立隔離的虛擬環境中執行。
  - 不更動營運伺服器的實際密碼設定。
  - 審查分析用 Notebook，確保不包含實際金鑰資料。
  deliverables:
  - 已排序的清單 CSV 分析本
  - 包含轉換計畫的技術決策表
assignment:
  title: PQC 轉換優先順序報告
  deliverables:
  - 密碼敏捷性分析報告 (PDF)
  - 基於風險等級的轉換路線圖（含表格）
  rubric:
  - 基於資料壽命及暴露風險的合理優先順序邏輯
  - 透過引入混合式密碼體系考慮密碼敏捷性
  - 轉換計畫的階段性執行可行性
  - 實驗結果與資料清單的一致性
quiz:
- question: 決定密碼轉換優先順序時，最需要考慮的資料特性是什麼？
  choices:
  - 資料所使用的程式語言
  - 資料的安全需求壽命 (Data Shelf Life)
  - 系統的開發人員數量
  - 最新資料儲存空間的容量
  answer_index: 1
  explanation: 量子威脅隱含著資料未來可能被破解的風險，因此需要長時間維持機密性的資料，應最優先進行 PQC 轉換。
- question: 為了確保密碼敏捷性 (Cryptographic Agility)，建議採用哪種軟體設計方式？
  choices:
  - 使用硬編碼的密碼演算法
  - 分離密碼加密模組與業務邏輯的抽象化
  - 僅使用單一演算法的封閉式結構
  - 直接參考作業系統層級的密碼函式庫
  answer_index: 1
  explanation: 分離密碼引擎與邏輯，使演算法更換時的程式碼變更降至最低的結構，是確保密碼敏捷性的關鍵。
completion_criteria:
- 提交標明轉換優先順序的清單分析檔案
- 編寫包含密碼敏捷性考量的轉換路線圖報告
- 完成包含所有實作程式碼及測量值的重現包
source_ids:
- S1
---

### 轉換優先順序策略 (Migration Prioritization Strategy)

向 NIST 後量子標準 (ML-KEM, ML-DSA) 的轉換始於系統整體的密碼資產評估。轉換優先順序不僅取決於演算法的老舊程度，還取決於資料的壽命 (Data Shelf Life)、密碼暴露風險以及系統的戰略重要性 [S1]。

#### 1. 密碼資產評估標準 (Assessment Criteria)
為判斷轉換急迫性，請利用以下標準：
- **資料安全壽命：** 加密資料若在未來被量子電腦破解時所造成的影響（例如：10 年以上需維持機密性的資料）。
- **系統敏捷性：** 目前實現的密碼是否為硬編碼，或是能否透過設定檔 (Config) 進行演算法更換。
- **技術債：** 使用該密碼模組的依賴項 (Dependency) 及維護可能性。

#### 2. 確保密碼敏捷性
轉換路線圖的核心是在更換演算法時將程式碼變更最小化。建議使用抽象層 (Abstraction Layer) 分離業務邏輯與密碼引擎，並透過混合式金鑰交換方式，確保既有演算法的穩定性與 PQC 的量子抵抗性。
