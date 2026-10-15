---
layout: learn-module
title: OQSおよびoqs-provider統合
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-ja
course_locale: ja
lang: ja
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
permalink: /learn/ja/post-quantum-cryptography-migration-lab/liboqs-integration/
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
id: m5
slug: liboqs-integration
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- Open Quantum Safe(OQS)アーキテクチャとoqs-providerの役割を理解する。
- TLS 1.3 でPQ(Post-Quantum)アルゴリズムが統合される方式を把握する。
- ローカル環境でハイブリッド(Hybrid) TLSハンドシェイクを構成および検証する。
- KEM実装の最適化(AVX-512など)が実際のハンドシェイクパフォーマンスに与える影響を考察する。
worked_examples:
- '例 1: oqs-providerがOpenSSLにロードされているかを確認するには `openssl list -providers` コマンドを実行する。出力結果に
  ''oqs'' プロバイダーが含まれている必要がある。'
- '例 2: ハイブリッドハンドシェイク実行時、 `openssl s_client -groups kyber768_x25519...` のようにコマンド引数を通じて鍵交換グループを指定する。これは
  ML-KEM(Kyber)と古典的な Curve25519 を結合したハイブリッドグループである。'
lab:
  title: ローカル環境におけるハイブリッドTLSテスト
  steps:
  - 隔離されたDockerコンテナ内でliboqsおよびoqs-providerをビルドしインストールする。
  - OpenSSL設定ファイル(`openssl.cnf`)を修正し、oqsプロバイダーを有効化する。
  - 二つのターミナルを開き、一方は `openssl s_server` を、もう一方は `openssl s_client` をハイブリッドモードで実行する。
  - Wiresharkを使用して ClientHello パケットにおいて、共有鍵グループ(Key Share)がどのように送信されるかをキャプチャおよび分析する。
  - ハンドシェイク成功可否とセッション暗号化アルゴリズム情報を確認する。
  safety:
  - 実験は必ず隔離されたローカル仮想環境内でのみ実行すること。
  - 運用サービスに使用される証明書や鍵は決して使用しないこと。
  - Wiresharkキャプチャ時、実際のサービストラフィックが含まれないよう注意すること。
  deliverables:
  - oqs-provider有効化確認スクリーンショット
  - ハイブリッドハンドシェイクログファイル
  - Wiresharkキャプチャパケットの共有鍵グループ分析レポート
assignment:
  title: 暗号アジリティベースの移行分析レポート
  deliverables:
  - TLSハンドシェイクパフォーマンス測定結果データ(CSV)
  - ハイブリッドモード使用理由とパフォーマンス低下に関する分析エッセイ
  - 優先順位ベースの耐量子移行ロードマップ
  rubric:
  - OQSツールチェーンのビルドおよび実行の成功可否
  - パケット分析を通じてハイブリッドモードの動作を正確に説明しているか
  - パフォーマンス測定データが実験環境とバージョン情報を含み再現可能か
  - 暗号アジリティの概念に基づき移行ロードマップが論理的に作成されているか
quiz:
- question: oqs-providerがOpenSSLで担当する中核的な役割は何ですか？
  choices:
  - ネットワークパケットを暗号化するハードウェアアクセラレータ
  - OpenSSLがliboqsのPQCアルゴリズムを呼び出せるようにするレイヤー
  - インターネットで公開鍵証明書を発行するサービス
  - 量子コンピュータの攻撃を検知するIDSツール
  answer_index: 1
  explanation: oqs-providerはOpenSSLのプロバイダー構造を通じてliboqsのアルゴリズムをOpenSSLアプリケーションから直接使用できるように接続します。
- question: TLS 1.3 で「ハイブリッドモード」鍵交換を使用する主な理由は何ですか？
  choices:
  - パフォーマンスを 100 倍以上に高めるため
  - 単一アルゴリズムの実装エラーや将来的な脆弱性に備えてセキュリティを保証するため
  - すべての既存クライアントをサポートするため
  - 量子コンピュータを使用してハンドシェイクを行うため
  answer_index: 1
  explanation: ハイブリッドモードは古典的なアルゴリズムとPQCアルゴリズムを結合し、実装上の欠陥や未知の脆弱性に備える多層防御戦略です。
completion_criteria:
- oqs-providerベースのローカルテスト環境ビルド完了
- ハイブリッドTLSハンドシェイク成功およびパケットキャプチャ検証完了
- 実験結果と分析が含まれたレポート作成完了
- 耐量子移行ロードマップ策定完了
source_ids:
- S2
---

## OQSおよびoqs-provider統合理論

量子コンピュータの脅威から既存のデータ転送を保護するために、NIST標準に基づく耐量子アルゴリズム(PQC)をTLS 1.3 のような既存プロトコルに統合することが不可欠である。OQS(Open Quantum Safe)プロジェクトは、これらの統合を加速させる主要フレームワークを提供する [S2]。

### 1. liboqsとoqs-provider
- **liboqs**: PQCアルゴリズム(ML-KEM, ML-DSAなど)のC言語実装を含むコアライブラリである。多様なアルゴリズムに対して統一されたAPIを提供する。
- **oqs-provider**: OpenSSL 3 のプロバイダー構造を活用して、OpenSSLアプリケーション(例: `s_client`, `s_server`)がliboqsのPQCアルゴリズムをネイティブに使用できるよう支援する中間レイヤーである。これにより修正を加えることなく、既存のTLSツールでPQC機能をテストできる。

### 2. TLS 1.3 のPQ統合方式
TLS 1.3 ハンドシェイク過程において、PQC KEMは既存の鍵交換(例: ECDH)を代替または補完する。
- **PQ-onlyモード**: PQC KEMのみを使用して鍵を交換する。
- **ハイブリッド(Hybrid)モード**: 既存の古典アルゴリズム(ECDH)とPQCアルゴリズムを結合する。これは耐量子安全性を確保しつつ古典的なセキュリティ保証も維持するものであり、アルゴリズム実装エラーや将来的な脆弱性から保護するための戦略である。

### 3. パフォーマンスの考慮事項
PQC KEMは既存のアルゴリズムよりも鍵サイズや計算量が多くなる可能性があり、ハンドシェイクパフォーマンスに直接的な影響を与える [S2]。最新のハードウェア命令セット(AVX-512など)を使用して多項式乗算やモジュラ縮小などを最適化することで、ハンドシェイク速度を向上させることができる [S2]。
