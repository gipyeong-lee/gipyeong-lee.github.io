---
layout: learn-module
title: OQS 與 oqs-provider 整合
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:post-quantum-cryptography-migration-lab:liboqs-integration
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/liboqs-integration/
module_id: m5
permalink: /learn/zh-tw/post-quantum-cryptography-migration-lab/liboqs-integration/
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
id: m5
slug: liboqs-integration
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- 理解 Open Quantum Safe(OQS) 架構與 oqs-provider 的角色。
- 掌握 PQ (Post-Quantum) 演算法整合至 TLS 1.3 的方式。
- 在本地環境中建置並驗證混合 (Hybrid) TLS 交握。
- 探討 KEM 實作最佳化 (AVX-512 等) 對實際交握效能的影響。
worked_examples:
- 範例 1：若要確認 oqs-provider 是否已載入 OpenSSL，執行 `openssl list -providers` 指令。輸出結果應包含 'oqs'
  提供者。
- 範例 2：執行混合交握時，使用指令引數指定金鑰交換群組，如 `openssl s_client -groups kyber768_x25519...`。此為結合
  ML-KEM (Kyber) 與傳統 Curve25519 的混合群組。
lab:
  title: 本地環境中的混合 TLS 測試
  steps:
  - 在隔離的 Docker 容器內建置並安裝 liboqs 與 oqs-provider。
  - 修改 OpenSSL 設定檔 (`openssl.cnf`) 以啟用 oqs 提供者。
  - 開啟兩個終端機，一個執行 `openssl s_server`，另一個以混合模式執行 `openssl s_client`。
  - 使用 Wireshark 擷取並分析 ClientHello 封包內，共享金鑰群組 (Key Share) 的傳輸方式。
  - 確認交握成功與否及連線加密演算法資訊。
  safety:
  - 實驗務必僅在隔離的本地虛擬環境內進行。
  - 絕不使用營運服務中所使用的憑證或金鑰。
  - 使用 Wireshark 擷取時，請注意勿包含實際服務流量。
  deliverables:
  - oqs-provider 啟用確認截圖
  - 混合交握日誌檔案
  - Wireshark 擷取封包的共享金鑰群組分析報告
assignment:
  title: 基於密碼敏捷性的遷移分析報告
  deliverables:
  - TLS 交握效能測量結果資料 (CSV)
  - 針對使用混合模式原因與效能下降的分析論文
  - 基於優先級的後量子遷移路線圖
  rubric:
  - OQS 工具鏈建置與執行成功與否
  - 是否透過 TLS 封包分析準確說明混合模式動作
  - 效能測量資料是否包含實驗環境與版本資訊，且具備可重現性
  - 是否基於密碼敏捷性概念邏輯地撰寫遷移路線圖
quiz:
- question: oqs-provider 在 OpenSSL 中負責的核心角色是什麼？
  choices:
  - 加密網路封包的硬體加速器
  - 讓 OpenSSL 應用程式能呼叫 liboqs 的 PQC 演算法的層級
  - 在網際網路發行公開金鑰憑證的服務
  - 偵測量子電腦攻擊的 IDS 工具
  answer_index: 1
  explanation: oqs-provider 透過 OpenSSL 的提供者架構，連結 liboqs 的演算法，使其能直接用於 OpenSSL 應用程式中。
- question: 在 TLS 1.3 中使用『混合模式』金鑰交換的主要原因是什麼？
  choices:
  - 將效能提升 100 倍以上
  - 為了防備單一演算法實作錯誤或未來漏洞，確保安全性
  - 支援所有現有的用戶端
  - 使用量子電腦進行交握
  answer_index: 1
  explanation: 混合模式結合了傳統演算法與 PQC 演算法，是一種防範實作缺失或未知漏洞的縱深防禦策略。
completion_criteria:
- 完成基於 oqs-provider 的本地測試環境建置
- 完成混合 TLS 交握成功與封包擷取驗證
- 完成包含實驗結果與分析的報告撰寫
- 建立後量子遷移路線圖
source_ids:
- S2
---

## OQS 與 oqs-provider 整合理論

為了保護現有資料傳輸免受量子電腦威脅，必須將 NIST 標準基礎的後量子演算法 (PQC) 整合至 TLS 1.3 等現有協定中。OQS (Open Quantum Safe) 專案提供了加速此類整合的主要框架 [S2]。

### 1. liboqs 與 oqs-provider
- **liboqs**: 包含 PQC 演算法 (ML-KEM, ML-DSA 等) C 語言實作的核心函式庫。提供統一的演算法 API。
- **oqs-provider**: 利用 OpenSSL 3 的提供者架構，協助 OpenSSL 應用程式 (如 `s_client`, `s_server`) 原生使用 liboqs 的 PQC 演算法。這讓現有的 TLS 工具無需修改即可測試 PQC 功能。

### 2. TLS 1.3 的 PQ 整合方式
在 TLS 1.3 交握過程中，PQC KEM 取代或補充現有的金鑰交換 (如 ECDH)。
- **PQ-only 模式**: 僅使用 PQC KEM 進行金鑰交換。
- **混合 (Hybrid) 模式**: 結合現有的傳統演算法 (ECDH) 與 PQC 演算法。這是兼顧確保後量子安全性與維持傳統安全保障的策略，目的在於保護免受演算法實作錯誤或未來漏洞的影響。

### 3. 效能考量
PQC KEM 的金鑰大小或運算量可能大於現有演算法，因此對交握效能有直接影響 [S2]。利用最新硬體指令集 (AVX-512 等) 優化多項式乘法與模組化縮減，可提升交握速度 [S2]。
