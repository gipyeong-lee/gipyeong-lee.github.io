---
layout: learn-module
title: Hybrid TLSハンドシェイク分析
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-ja
course_locale: ja
lang: ja
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
permalink: /learn/ja/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
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
id: m7
slug: hybrid-tls-analysis
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m6
objectives:
- 量子脅威環境下におけるTLS 1.3 の脆弱性を説明する。
- ML-KEMベースのハイブリッド(Hybrid) TLSハンドシェイク構造を理解する。
- OQS(Open Quantum Safe)ベースのローカル環境にてハイブリッドモードパフォーマンスを測定する。
- パケットキャプチャを通じて、既存アルゴリズムとPQアルゴリズムが結合されたハンドシェイクプロセスを分析する。
worked_examples:
- '例 1: ハイブリッド鍵交換プロセス - クライアントは古典的共有秘密値とPQCカプセル化結果値をサーバーに送信します。サーバーは逆カプセル化の後、二つの共有秘密をKDF(Key
  Derivation Function)に結合してセッションキーを生成します。'
- '例 2: ハンドシェイク遅延分析 - PQアルゴリズム適用時、追加的な鍵サイズ(Key Size)が増加するに従い、ネットワーク転送時間が増える現象を比較分析します。パフォーマンス最適化(例:
  AVX-512 使用)適用前後でのハンドシェイク当たりの処理量(Handshakes per second)の差を数値化します [S2]。'
lab:
  title: OQSベースのハイブリッドTLSハンドシェイク再現実験
  steps:
  - 隔離されたDocker環境にてliboqsおよびoqs-providerが統合されたOpenSSL 3 ビルド環境を構築する。
  - '既存ECDHモードとML-KEMベースのハイブリッドモード(例: secp256r1_mlkem768)を設定する。'
  - ローカルループバック(Loopback)インターフェースを使用して、両モード間でTLS 1.3 ハンドシェイクを実行する。
  - Wiresharkを使用して ClientHello および ServerHello メッセージ内の鍵交換データフィールドをパケットキャプチャする。
  - 実行時間測定スクリプトを使用して 100 回以上のハンドシェイク平均時間を測定し、ハイブリッドモードのオーバーヘッドを記録する。
  safety:
  - 本実験はローカル環境の隔離されたループバックインターフェースでのみ実行し、外部ネットワークトラフィックを生成しないこと。
  - 実際の証明書、秘密鍵、ユーザーデータなどの運用セキュリティ資産を絶対に使用しないこと。
  - 学習用OQSライブラリは実験的なツールであるため、実際の運用セキュリティサービスには使用しないこと。
  - 実験終了時、生成されたすべての臨時鍵とローカル測定データを削除すること。
  deliverables:
  - 設定および実行ログファイル
  - Wiresharkパケットキャプチャファイル(.pcapng)および鍵交換フィールド分析ノート
  - ハンドシェイクパフォーマンス比較測定CSVデータ
assignment:
  title: TLS 1.3 ハイブリッド移行パフォーマンス分析レポート
  deliverables:
  - ハンドシェイク遅延時間比較分析グラフおよびデータ視覚化
  - ハイブリッドモードパケット分析および鍵交換アルゴリズム特徴のまとめ
  - 運用環境適用時に予想されるパフォーマンスおよびセキュリティ考慮事項の意思決定表
  rubric:
  - 実験の再現可能性(環境設定およびスクリプト明示の有無)
  - パケット分析の正確性(鍵交換フィールドの識別)
  - パフォーマンス測定データの論理的解釈
  - 理論的なセキュリティ仮定と実験結果の関連性
quiz:
- question: ハイブリッドTLSハンドシェイクの主なセキュリティ上の利点は何ですか？
  choices:
  - ハンドシェイクステップを劇的に減らして速度を高める。
  - 古典的アルゴリズムとPQCアルゴリズムのいずれか一方が安全であれば秘密性を維持する。
  - ネットワーク転送コストを完全に排除する。
  - 証明書管理の複雑度を下げる。
  answer_index: 1
  explanation: ハイブリッドモードは既存のアルゴリズムとPQCアルゴリズムの結果を結合し、両アルゴリズムのいずれか一方が安全であればセキュリティが維持されるように設計された移行期の戦略です。
- question: TLS 1.3 ハンドシェイクパフォーマンスに最も大きな影響を与えるPQアルゴリズム要素は何ですか？
  choices:
  - ネットワークレイテンシのみを考慮する。
  - KEM（鍵カプセル化メカニズム）の鍵生成、カプセル化、逆カプセル化の計算コスト
  - サーバーのディスクI/O速度
  - クライアントのブラウザバージョン
  answer_index: 1
  explanation: KEMアルゴリズムの計算コストは、TLS 1.3 ハンドシェイクのパフォーマンスに直結するため、これを最適化することが性能改善の鍵となります[S2]。
completion_criteria:
- ローカル環境でのliboqsベースのハイブリッドTLSハンドシェイクの再現成功
- Wireshark分析を通じたハイブリッド鍵交換メッセージの確認
- 性能測定データに基づく結果分析レポートの提出
- 安全上の制約事項（データ分離、運用鍵の不使用）の遵守確認
source_ids:
- S2
---

### ハイブリッドTLSハンドシェイク理論

現行のTLS 1.3 はECDH(Elliptic Curve Diffie-Hellman)のような古典的な公開鍵暗号に依存しており、これは十分な性能の量子コンピュータが登場した場合、攻撃の脅威にさらされる [S2]。これへの対応として、NIST標準であるML-KEM(Module-Lattice-Based Key-Encapsulation Mechanism)のような耐量子暗号(PQC)を統合する研究が活発である [S2]。

#### ハイブリッドモードのセキュリティ仮定
完全なPQC移行前に運用安定性を確保するため、古典的アルゴリズムとPQアルゴリズムを結合した「ハイブリッド(Hybrid)モード」を使用する。この方式は、両アルゴリズムの共有秘密(Shared Secret)を結合し、両アルゴリズムのいずれか一方が安全であれば通信の秘密性を保証するように設計されている。

#### パフォーマンスの考慮事項
TLS 1.3 ハンドシェイクパフォーマンスはKEMの計算コストに直接的に依存する [S2]。特に鍵生成(Key Generation)、カプセル化(Encapsulation)、逆カプセル化(Decapsulation)段階における演算効率が、ハンドシェイク全体の速度を決定する。近年ではAVX-512のような命令セット最適化を通じて、多項式乗算およびモジュラ縮小プロセスを加速し、ハンドシェイクパフォーマンスを高める手法が適用されている [S2]。
