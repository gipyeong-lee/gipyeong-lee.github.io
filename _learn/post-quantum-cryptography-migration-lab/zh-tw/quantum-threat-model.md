---
layout: learn-module
title: 量子威脅與格點密碼學
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-tw
course_locale: zh-tw
lang: zh-tw
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
permalink: /learn/zh-tw/post-quantum-cryptography-migration-lab/quantum-threat-model/
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
id: m1
slug: quantum-threat-model
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- 理解量子電腦對現代密碼體系 (RSA, ECC) 造成的威脅模型。
- 分析格點密碼學 (Lattice-based Cryptography) 的數學基礎與安全性依據。
- 學習 NIST 建議的後量子密碼標準 (ML-KEM, ML-DSA) 的設計原理。
- 描述格點演算法的效率及安全特性 (worst-case hardness)。
worked_examples:
- 範例 1：量子電腦對 RSA 的影響分析 - RSA 基於大數質因數分解的難度。Shor 演算法將分解 n 位元整數的複雜度從指數時間縮短為多項式時間，從而立即破解加密訊息。
- 範例 2：格點基礎難題 (LWE) 概念理解 - 考慮一個加入秘密向量 s 與誤差 e 的線性方程式系統 A*s + e = t。格點密碼學基於「學習錯誤問題」(Learning
  With Errors) 的難度，即給定矩陣 A 與結果 t，難以找出 s。
lab:
  title: 格點密碼學基礎環境建置與視覺化
  steps:
  - 在隔離的 Linux/Docker 環境中建立 Python 3 虛擬環境
  - 安裝並編譯 liboqs 函式庫
  - 撰寫腳本，收集格點基礎 LWE 問題在參數變化下的金鑰大小與運算時間
  - 執行資料分析與視覺化筆記本
  safety:
  - 所有實驗均在隔離的本地虛擬環境內進行
  - 絕對禁止使用真實營運憑證、私鑰與客戶資料
  - 勿將研究用函式庫視為實際服務安全手段
  deliverables:
  - 環境設定日誌與編譯產出
  - 演算法效能 (金鑰大小、時間) 比較分析資料
  - 格點密碼學特性報告
assignment:
  title: 撰寫量子威脅分析報告
  deliverables:
  - 量子威脅模型與格點密碼學理論總結文件
  - 主要 PQC 演算法 (ML-KEM, ML-DSA) 比較表
  rubric:
  - 準確解釋 Shor 演算法的原理
  - 邏輯描述格點密碼學的最壞情況難題 (worst-case hardness) 概念
  - 基於提供的來源 [S3, S4] 描述現代密碼學面臨的挑戰
quiz:
- question: Shor 演算法 (Shor's algorithm) 對現有 PKI 造成的威脅是什麼？
  choices:
  - 無條件破解所有對稱金鑰加密。
  - 在多項式時間內解決質因數分解與離散對數問題。
  - 徹底消除雜湊函數的抗碰撞性。
  - 降低量子電腦的處理速度。
  answer_index: 1
  explanation: Shor 演算法透過在多項式時間內解決 RSA 基礎的質因數分解與 ECC 基礎的離散對數問題，從而威脅現有的公開金鑰密碼體系。
- question: 格點密碼學 (Lattice-based Cryptography) 為何具有前瞻性？
  choices:
  - 因為它能將最壞情況難題還原為平均情況難題。
  - 因為它比所有對稱金鑰加密快得多。
  - 因為量子電腦也絕對無法破解它。
  - 因為它完全不需要電腦記憶體。
  answer_index: 0
  explanation: 格點密碼學具有數學優勢，能從最壞情況難題 (worst-case hardness) 保證平均情況 (average-case) 的安全性
    [S4]。
completion_criteria:
- 完成理論學習並提交量子威脅報告
- 在實作環境中成功利用 liboqs 執行基礎演算法
- 測驗項目達到 80% 以上的正確率
source_ids:
- S3
- S4
---

## 量子威脅模型
現代公開金鑰密碼學 (PKI) 主要依賴於質因數分解 (RSA) 與離散對數問題 (ECC) 的困難難題。Shor 演算法 (Shor's algorithm) 能夠使用量子電腦在多項式時間內解決這些問題，這意味著它實際上破解了目前所有的標準 PKI [S3]。

## 格點密碼學 (Lattice-based Cryptography)
格點密碼學將高維空間中從格點 (Lattice) 的基底向量尋找特定點的問題 (例如 SVP, LWE) 作為難題。這些問題已被證明即使在最壞情況 (worst-case) 下也難以求解，且在平均情況 (average-case) 下亦能保證安全性 [S4]。

## 後量子標準 (ML-KEM/ML-DSA)
- **ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism):** 一種金鑰封裝機制，結合高效實現與格點基礎難題以提供量子抵抗力。
- **ML-DSA (Module-Lattice-based Digital Signature Algorithm):** 電子簽章標準，利用格點基礎數學結構以確保強大的簽章完整性。
格點系統在目前的標準化過程中，證明了其強大的 worst-case to average-case 還原性與高效性能，正成為 PQC 遷移的核心 [S4]。
