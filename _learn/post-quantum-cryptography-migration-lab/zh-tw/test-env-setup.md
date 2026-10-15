---
layout: learn-module
title: 建立隔離的實驗環境
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:post-quantum-cryptography-migration-lab:test-env-setup
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/test-env-setup/
module_id: m4
permalink: /learn/zh-tw/post-quantum-cryptography-migration-lab/test-env-setup/
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
id: m4
slug: test-env-setup
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- 理解用於後量子密碼 (PQC) 實驗的隔離式本地開發環境的結構原理及其必要工具 (liboqs, oqs-provider) 的角色。
- 分析 KEM 效能在 TLS 1.3 等協定中對交握 (Handshake) 延遲的影響。
- 利用 Docker 容器設計並建立具備固定依賴、可重現的實驗環境。
worked_examples:
- 範例 1：利用 Dockerfile 建立基於 oqs-provider 的環境。說明如何藉由註明各函式庫版本以確保建置可重現性。
- 範例 2：利用 OpenSSL CLI 測試混合 TLS 交握。使用 'openssl s_server' 與 's_client' 模擬 ML-KEM-768
  支援的混合 TLS 1.3 連線的方法。
lab:
  title: 建置隔離的 PQC 測試平台
  steps:
  - 準備實驗用 Docker 容器映像檔基礎 (Ubuntu 22.04 LTS 以上)。
  - 複製 (clone) liboqs 與 oqs-provider 原始程式碼，並簽出特定的 commit hash 以固定版本。
  - 使用 CMake 編譯 liboqs 時，設定最佳化層級 (例如 AVX2) 並執行建置。
  - 設定 OpenSSL 3.x 環境並啟用 oqs-provider。
  - 透過本地網路介面固定回送 (Loopback) 連線，測量基礎 TLS 1.3 交握效能指標。
  safety:
  - 實驗用環境必須僅在本地隔離的容器內執行。
  - 絕不將營運環境的憑證、真實私鑰、客戶資料帶入容器。
  - 請注意，編譯與執行過程中產生的測量值僅視為公開測試資料，與實際安全政策無關。
  - 若監控實際硬體或電力消耗，請遵守製造商指定的額定電流與電壓範圍。
  deliverables:
  - 具備固定依賴版本的 Dockerfile 與建置日誌。
  - 顯示已成功從 OpenSSL 載入 PQC 演算法清單的終端機截圖。
  - 環境設定完成的隔離開發環境檢查碼 (SHA-256)。
assignment:
  title: PQC 測試平台文件化與評估
  deliverables:
  - 所建置測試平台的架構圖與所選演算法版本規格說明書。
  - 在測試平台環境中，傳統演算法與混合 ML-KEM 演算法的交握時間比較資料 CSV。
  - 維持隔離環境的安全政策報告。
  rubric:
  - 依賴版本固定及建置可重現性 (30%)
  - 在隔離實驗環境下的混合 TLS 交握成功與否 (40%)
  - 演算法構成與測量程序的明確性與安全遵循 (30%)
quiz:
- question: oqs-provider 的主要角色是什麼？
  choices:
  - 在硬體層級加速 PQC 演算法。
  - 作為介面，讓 OpenSSL 3 能將後量子演算法用於 TLS 協定等。
  - 自動更新營運環境的安全憑證。
  - 阻斷量子電腦的攻擊向量。
  answer_index: 1
  explanation: oqs-provider 使用 OpenSSL 提供者架構將 PQC 演算法整合至標準函式庫中，並使現有應用程式能使用 PQC 演算法。
- question: 為何在隔離實驗環境中必須固定 (Locking) 版本？
  choices:
  - 因為最新版本總是更快。
  - 為了確保可重現性，並減少因研究者間執行環境差異導致的測量誤差。
  - 為了強化營運安全性。
  - 為了縮短建置時間。
  answer_index: 1
  explanation: 版本固定對於確保相同環境的可重現性、獲取效能測量值的完整性與研究的客觀性至關重要。
completion_criteria:
- 成功構成基於 Docker 的隔離建置環境。
- 透過 oqs-provider 完成 ML-KEM 混合模式演示。
- 提交包含實驗資料測量與安全政策的報告。
source_ids:
- S2
---

### 隔離 PQC 實驗環境的必要性
為了保護現有公開金鑰密碼 (RSA, ECDH 等) 免受量子電腦威脅，NIST 標準化了 ML-KEM (基於 Kyber) 與 ML-DSA (基於 Dilithium) 等後量子演算法。若要在本地環境評估這些演算法的效能與安全性，具備 **密碼敏捷性 (Crypto-agility)** 且可重現的環境是不可或缺的 [S2]。

#### 1. 主要構成要素
*   **liboqs**: 以 C 語言實作 PQC 演算法的函式庫，提供了可測試多種 KEM 與簽章演算法的基礎。
*   **oqs-provider**: 使用 OpenSSL 3 的提供者架構，將 PQC 演算法整合至現有 TLS 基礎設施的介面。
*   **混合模式 (Hybrid mode)**: 結合現有傳統密碼 (ECDH) 與 PQC 演算法，作為即使 PQC 函式庫存在潛在弱點也能維持現有安全水準的轉型策略 [S2]。

#### 2. 實驗環境的核心：隔離與可重現性
實驗必須與營運環境徹底分離。使用 Docker 等容器技術將依賴版本固定 (Locking)，可減少研究者間執行結果的差異，並能準確測量演算法最佳化 (例如利用 AVX-512) 的效果 [S2]。在評估交握效能時，應使用固定硬體與隔離網路，以將延遲時間的不確定性降至最低。
