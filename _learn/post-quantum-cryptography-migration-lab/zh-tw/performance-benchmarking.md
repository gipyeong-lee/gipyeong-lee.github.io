---
layout: learn-module
title: 效能評估與標竿測試
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:post-quantum-cryptography-migration-lab:performance-benchmarking
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/performance-benchmarking/
module_id: m6
permalink: /learn/zh-tw/post-quantum-cryptography-migration-lab/performance-benchmarking/
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
id: m6
slug: performance-benchmarking
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m5
objectives:
- 理解後量子密碼演算法 (ML-KEM) 的效能評估指標 (時間、記憶體、處理量)。
- 分析 KEM 運算在 TLS 1.3 交握過程中對效能的影響。
- 利用 Liboqs 與 oqs-provider 框架標竿測試混合密碼模式的效能。
worked_examples:
- '範例 1：利用 Liboqs 進行單一 KEM 運算標竿測試

  透過 Python 腳本，利用 `timeit` 模組測量 `ML-KEM-768` 的 `keypair`、`encaps`、`decaps` 運作時間並儲存為
  CSV 的方法。'
- '範例 2：混合 TLS 1.3 交握處理量測量

  在已套用 oqs-provider 的本地伺服器/用戶端環境中，使用 `s_client` 與 `s_server` 測量 100 次連線所需的總時間，以分析出計算每秒交握數
  (TPS) 的程序。'
lab:
  title: PQC 效能標竿測試實作
  steps:
  - 在隔離的開發環境內安裝 liboqs 與 oqs-provider 並確認環境設定。
  - 撰寫標竿測試用 Python 腳本，測量 ML-KEM 演算法的運算時間。
  - 執行 Wireshark 擷取 TLS 交握封包，分析混合模式下的資料大小變化。
  - 基於測量資料，將運算時間與處理量指標繪製成圖表。
  safety:
  - 實驗僅在本地隔離環境內執行，絕對不使用實際營運環境的憑證或金鑰。
  - 由於標竿測試過程中可能產生高 CPU 負載，請監控系統資源。
  - 注意避免將實際秘密值或金鑰資料包含在擷取檔案中。
  deliverables:
  - 運算效能測量腳本 (.py)
  - 測量結果 CSV 資料
  - 各演算法效能比較分析報告 (.md 或 .ipynb)
assignment:
  title: 基於密碼敏捷性的效能評估報告
  deliverables:
  - 演算法選擇原因與安全/效能權衡分析
  - 標竿測試資料視覺化素材
  - 基於效能結果的遷移路線圖修正案
  rubric:
  - 標竿測試資料是否在可重現且獨立的環境中測量？
  - 是否準確分析效能下降的技術原因 (金鑰大小、運算複雜度)？
  - 是否平衡討論了混合模式的優點與成本？
quiz:
- question: TLS 1.3 交握效能中，最關鍵的 PQC 演算法相關要素是什麼？
  choices:
  - 對稱金鑰加密演算法的區塊大小
  - KEM 的金鑰產生與封裝運算時間
  - 雜湊演算法的種類
  - 伺服器的作業系統種類
  answer_index: 1
  explanation: TLS 1.3 交握效能極大程度地取決於 KEM 演算法的運算效率 [S2]。
- question: 效能評估時使用混合模式的主要原因？
  choices:
  - 因為它總比傳統演算法快
  - 為了防備 PQC 的安全威脅同時維持安全性
  - 為了縮減網路頻寬
  - 為了最小化運算資源
  answer_index: 1
  explanation: 混合模式結合了 PQC 的未來安全性與傳統演算法經過驗證的安全性，實現逐步遷移。
completion_criteria:
- 完成標竿測試腳本執行與結果資料確保
- 提交效能評估報告並通過
- 完成 TLS 混合模式效能分析
source_ids:
- S2
---

## 效能評估與標竿測試

遷移至後量子密碼 (PQC) 不僅僅是更換演算法，更是與現有網路協定 (如 TLS 1.3) 的效能直接相關的問題。特別是 KEM (Key Encapsulation Mechanism) 運算會直接影響交握的延遲 (latency) 與伺服器每秒連線處理量 (handshakes per second) [S2]。

### 效能指標
1. **運算時間 (Computation Time):** 金鑰產生 (KeyGen)、封裝 (Encaps)、解封 (Decaps) 各自消耗的 CPU 週期或時間 (ms)。
2. **資料大小:** 公開金鑰與封裝後文字 (ciphertext) 的大小。這決定了網路頻寬消耗與發生分段的可能性。
3. **處理量 (Throughput):** 每秒可處理的交握次數。優化實作 (例如利用 AVX-512) 可提升多項式乘法與模組化運算速度，大幅改善處理量 [S2]。

### 混合模式
轉型期建議採取同時使用傳統演算法 (ECDH) 與 PQC (ML-KEM) 的混合方法。這是為了在防範 PQC 潛在漏洞的同時，獲取 PQC 的安全優勢。由於混合模式運算複雜度增加，必須嚴密評估效能下降情況 [S2]。
