---
layout: learn-module
title: Hybrid TLS 交握分析
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:post-quantum-cryptography-migration-lab:hybrid-tls-analysis
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
module_id: m7
permalink: /learn/zh-tw/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
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
id: m7
slug: hybrid-tls-analysis
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m6
objectives:
- 說明量子威脅環境下 TLS 1.3 的脆弱性。
- 理解基於 ML-KEM 的混合 (Hybrid) TLS 交握結構。
- 在基於 OQS (Open Quantum Safe) 的本地環境中測量混合模式效能。
- 透過封包擷取分析傳統演算法與 PQ 演算法結合的交握過程。
worked_examples:
- 範例 1：混合金鑰交換過程 - 用戶端將傳統共享秘密值與 PQC 封裝結果傳送給伺服器。伺服器在解封後，將兩組共享秘密結合至 KDF (Key Derivation
  Function) 以產生階段金鑰。
- 範例 2：交握延遲分析 - 比較 PQ 演算法應用時，因金鑰大小 (Key Size) 增加導致網路傳輸時間延長的現象。數值化性能最佳化 (例如 AVX-512
  使用) 應用前後，每秒交握數 (Handshakes per second) 的差異 [S2]。
lab:
  title: 基於 OQS 的混合 TLS 交握重現實驗
  steps:
  - 在隔離的 Docker 環境中建置整合 liboqs 與 oqs-provider 的 OpenSSL 3 建置環境。
  - 設定既有的 ECDH 模式與 ML-KEM 基礎的混合模式 (如 secp256r1_mlkem768)。
  - 利用本地回送 (Loopback) 介面執行兩模式間的 TLS 1.3 交握。
  - 使用 Wireshark 擷取 ClientHello 與 ServerHello 訊息內部的金鑰交換資料欄位並進行分析。
  - 利用執行時間測量腳本測量 100 次以上的交握平均時間，記錄混合模式的額外開銷 (Overhead)。
  safety:
  - 本實驗僅在本地環境的隔離回送介面執行，不產生對外網路流量。
  - 絕不使用憑證、私鑰、使用者資料等營運安全資產。
  - 學習用 OQS 函式庫為實驗工具，勿用於實際營運安全服務。
  - 實驗結束時刪除所有產出的暫存金鑰與本地測量資料。
  deliverables:
  - 設定與執行日誌檔案
  - Wireshark 封包擷取檔案 (.pcapng) 與金鑰交換欄位分析筆記
  - 交握效能比較測量 CSV 資料
assignment:
  title: TLS 1.3 混合遷移效能分析報告
  deliverables:
  - 交握延遲時間比較分析圖表與資料視覺化
  - 混合模式封包分析與金鑰交換演算法特徵摘要
  - 應用於營運環境時預期的效能與安全考量決策表
  rubric:
  - 實驗的可重現性 (環境設定與腳本明示與否)
  - 封包分析的準確性 (金鑰交換欄位識別)
  - 效能測量資料的邏輯解讀
  - 理論安全假設與實驗結果的連結性
quiz:
- question: 混合 TLS 交握的主要安全優勢是什麼？
  choices:
  - 大幅減少交握階段以提升速度。
  - 確保只要傳統演算法與 PQC 演算法中任一者安全，即可維持機密性。
  - 完全消除網路傳輸成本。
  - 降低憑證管理的複雜度。
  answer_index: 1
  explanation: 混合模式結合傳統演算法與 PQC 演算法的結果，是一種在兩演算法中任一者安全即可確保安全的轉型期策略。
- question: 對 TLS 1.3 交握效能影響最大的 PQ 演算法要素是什麼？
  choices:
  - 僅考慮網路延遲。
  - KEM（金鑰封裝機制）的金鑰生成、封裝與解封運算成本
  - 伺服器的磁碟 I/O 速度
  - 用戶端的瀏覽器版本
  answer_index: 1
  explanation: KEM 演算法的計算成本與 TLS 1.3 握手效能直接相關，優化此成本是提升效能的關鍵[S2]。
completion_criteria:
- 成功在本地環境中重現基於 liboqs 的混合式 TLS 握手
- 透過 Wireshark 分析確認混合式金鑰交換訊息
- 提交基於效能測量數據的結果分析報告
- 確認遵守安全約束事項（資料隔離、不使用營運金鑰）
source_ids:
- S2
---

### 混合 TLS 交握理論

現行的 TLS 1.3 依賴 ECDH (Elliptic Curve Diffie-Hellman) 等傳統公開金鑰密碼學，若足夠強大的量子電腦問世，此類加密將面臨被破解的風險 [S2]。作為應對，將 ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism) 等 NIST 標準後量子密碼 (PQC) 整合的研究正蓬勃發展 [S2]。

#### 混合模式的安全假設
在完全遷移至 PQC 之前，為確保營運穩定性，使用結合傳統演算法與 PQ 演算法的『混合 (Hybrid) 模式』。此方法結合兩演算法的共享秘密 (Shared Secret)，設計上確保只要兩演算法中任一者安全，即可維持通訊機密性。

#### 效能考量
TLS 1.3 交握效能直接依賴於 KEM 的計算成本 [S2]。特別是金鑰產生 (Key Generation)、封裝 (Encapsulation)、解封 (Decapsulation) 階段的運算效率決定了整體交握速度。近期已透過 AVX-512 等指令集最佳化，加速多項式乘法與模組化縮減，以提升交握效能的技術正被應用中 [S2]。
