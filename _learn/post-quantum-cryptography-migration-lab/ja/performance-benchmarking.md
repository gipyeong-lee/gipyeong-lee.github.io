---
layout: learn-module
title: パフォーマンス評価およびベンチマーク
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-ja
course_locale: ja
lang: ja
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
permalink: /learn/ja/post-quantum-cryptography-migration-lab/performance-benchmarking/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e5164bbefc324eff94b7957c62695f66
translation_run_id: 180bcdae1f304308ae765fa770418d34
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
- 耐量子暗号アルゴリズム(ML-KEM)のパフォーマンス評価指標(時間、メモリ、処理能力)を理解する。
- TLS 1.3 ハンドシェイク過程においてKEM演算がパフォーマンスに与える影響を分析する。
- Liboqsおよびoqs-providerフレームワークを活用してハイブリッド暗号モードのパフォーマンスをベンチマークする。
worked_examples:
- '例 1: Liboqsを使用した単一KEM演算ベンチマーク

  Pythonスクリプトを通じて `ML-KEM-768` の `keypair`, `encaps`, `decaps` 動作時間を `timeit` モジュールで測定し、結果をCSVとして保存する方法である。'
- '例 2: ハイブリッドTLS 1.3 ハンドシェイク処理能力測定

  oqs-providerが適用されたローカルサーバー/クライアント環境にて `s_client` と `s_server` を使用し、100回接続時に要する合計時間を測定して秒間ハンドシェイク数(TPS)を算出する分析手順である。'
lab:
  title: PQCパフォーマンスベンチマーク実習
  steps:
  - 隔離された開発環境にてliboqsおよびoqs-providerをインストールし、環境設定を確認する。
  - ベンチマーク用Pythonスクリプトを作成し、ML-KEMアルゴリズムの演算時間を測定する。
  - Wiresharkを実行してTLSハンドシェイクパケットをキャプチャし、ハイブリッドモード時のデータサイズ変化を分析する。
  - 測定されたデータに基づき、演算時間および処理能力指標をグラフ化する。
  safety:
  - 実験はローカル隔離環境内でのみ実行し、実際の運用環境の証明書や鍵を絶対に使用しないこと。
  - ベンチマーク過程で高いCPU負荷が発生する可能性があるため、システムリソースをモニタリングすること。
  - 実際の秘密値や鍵データをキャプチャファイルに含めないよう注意すること。
  deliverables:
  - 演算パフォーマンス測定スクリプト(.py)
  - 測定結果CSVデータ
  - アルゴリズム別パフォーマンス比較分析レポート(.mdまたは.ipynb)
assignment:
  title: 暗号アジリティベースのパフォーマンス評価レポート
  deliverables:
  - アルゴリズム選択理由およびセキュリティ/パフォーマンスのトレードオフ分析
  - ベンチマークデータ視覚化資料
  - パフォーマンス結果に基づいた移行ロードマップ修正案
  rubric:
  - ベンチマークデータが再現可能であり、独立した環境で測定されているか？
  - パフォーマンス低下の技術的原因(鍵サイズ、演算複雑度)を正確に分析しているか？
  - ハイブリッドモードの利点とコストをバランスよく議論しているか？
quiz:
- question: TLS 1.3 ハンドシェイクパフォーマンスにおいて最も重要なPQCアルゴリズム関連要素は？
  choices:
  - 対称鍵暗号アルゴリズムのブロックサイズ
  - KEMの鍵生成およびカプセル化演算時間
  - ハッシュアルゴリズムの種類
  - サーバーのオペレーティングシステムの種類
  answer_index: 1
  explanation: TLS 1.3 ハンドシェイクパフォーマンスは、KEMアルゴリズムの演算効率に大きく左右されます [S2]。
- question: パフォーマンス評価時にハイブリッドモードを使用する主な理由は？
  choices:
  - 伝統的なアルゴリズムよりも常に高速であるため
  - PQCのセキュリティ脅威に備えつつセキュリティ性を維持するため
  - ネットワーク帯域幅を減らすため
  - 演算リソースを最小化するため
  answer_index: 1
  explanation: ハイブリッドモードはPQCの未来のセキュリティ性と、伝統的アルゴリズムの検証済みのセキュリティ性を結合し、段階的な移行を可能にします。
completion_criteria:
- ベンチマークスクリプトの実行および結果データ確保完了
- パフォーマンス評価レポート提出および通過
- TLSハイブリッドモードパフォーマンス分析完了
source_ids:
- S2
---

## パフォーマンス評価およびベンチマーク

耐量子暗号(PQC)への移行は、単にアルゴリズムを交換するだけでなく、既存のネットワークプロトコル(例: TLS 1.3)のパフォーマンスに直結する問題である。特にKEM(Key Encapsulation Mechanism)演算は、ハンドシェイクの遅延時間(latency)とサーバーの秒間接続処理数(handshakes per second)に直接的な影響を与える [S2]。

### パフォーマンス指標
1. **演算時間(Computation Time):** 鍵生成(KeyGen)、カプセル化(Encaps)、逆カプセル化(Decaps)のそれぞれに要するCPUサイクルまたは時間(ms)。
2. **データサイズ:** 公開鍵およびカプセル化されたテキスト(ciphertext)のサイズ。これはネットワーク帯域幅消費と断片化発生の可能性を決定する。
3. **スループット(Throughput):** 秒間処理可能なハンドシェイク数。最適化された実装(例: AVX-512 活用)はポリノミアル乗算およびモジュラ演算速度を高め、処理能力を大幅に改善できる [S2]。

### ハイブリッドモード
移行期には従来のアルゴリズム(ECDH)とPQC(ML-KEM)を併用するハイブリッドアプローチが推奨される。これはPQCの潜在的な脆弱性に備えつつ、PQCのセキュリティ利点を確保するためである。ハイブリッドモードは演算複雑度が増加するため、パフォーマンス低下を綿密に評価しなければならない [S2]。
