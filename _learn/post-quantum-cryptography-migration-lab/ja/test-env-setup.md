---
layout: learn-module
title: 隔離された実験環境の構築
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-ja
course_locale: ja
lang: ja
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
permalink: /learn/ja/post-quantum-cryptography-migration-lab/test-env-setup/
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
id: m4
slug: test-env-setup
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- 耐量子暗号(PQC)実験のための隔離されたローカル開発環境の構成原理と必須ツール(liboqs, oqs-provider)の役割を理解する。
- TLS 1.3 などのプロトコルにおいて、KEMパフォーマンスがハンドシェイク遅延時間に与える影響を分析する。
- Dockerコンテナを使用して、依存関係が固定された再現可能な実験環境を設計し構築する。
worked_examples:
- '例 1: Dockerfileを活用したoqs-providerベースの環境構築。各ライブラリのバージョンを明示してビルド再現性を確保する方式の説明。'
- '例 2: OpenSSL CLIを利用したハイブリッドTLSハンドシェイクテスト。''openssl s_server'' と ''s_client'' を使用して
  ML-KEM-768 をサポートするハイブリッドTLS 1.3 接続シミュレーションの方法。'
lab:
  title: 隔離されたPQCテストベッドの構築
  steps:
  - 実験用Dockerコンテナイメージベース(Ubuntu 22.04 LTS以上)を準備。
  - liboqsおよびoqs-providerのソースコードを複製(clone)し、特定のコミットハッシュをチェックアウトしてバージョンを固定。
  - 'CMakeを使用してliboqsコンパイル時、最適化レベル(例: AVX2)を設定しビルドを実行。'
  - OpenSSL 3.x 環境設定およびoqs-providerの有効化。
  - ローカルネットワークインターフェースに固定されたループバック接続を通じて、基本TLS 1.3 ハンドシェイクパフォーマンス基準を測定。
  safety:
  - 実験用環境は必ずローカル隔離されたコンテナ内でのみ実行すること。
  - 運用環境の証明書、実際の秘密鍵、顧客データは決してコンテナ内に持ち込まないこと。
  - コンパイルおよび実行過程で生成された測定値は公開テストデータと見なし、実際のセキュリティポリシーとは無関係であることに留意すること。
  - 実際のハードウェアや電力モニタリング時、製造元が明示した定格電流および電圧範囲を遵守すること。
  deliverables:
  - 依存関係バージョンが固定されたDockerfileおよびビルドログ。
  - OpenSSLでPQCアルゴリズムリストを正常に読み込めたことを示すターミナルキャプチャ。
  - 環境設定が完了した隔離された開発環境のチェックサム(SHA-256)。
assignment:
  title: PQCテストベッドの文書化および評価
  deliverables:
  - 構築したテストベッドの構成図および選択したアルゴリズムバージョン明細書。
  - テストベッド環境での古典アルゴリズムとハイブリッドML-KEMアルゴリズムのハンドシェイク時間比較データCSV。
  - 隔離された環境維持のためのセキュリティポリシーレポート。
  rubric:
  - 依存関係バージョンの固定およびビルド再現の可能性 (30%)
  - 隔離された実験環境でのハイブリッドTLSハンドシェイク成功可否 (40%)
  - アルゴリズム構成および測定手順の明確さとセキュリティ遵守 (30%)
quiz:
- question: oqs-providerの主な役割は何ですか？
  choices:
  - PQCアルゴリズムをハードウェアレベルで加速する。
  - OpenSSL 3 で耐量子アルゴリズムをTLSプロトコルなどに使用できるように接続するインターフェースの役割を果たす。
  - 運用環境のセキュリティ証明書を自動的に更新する。
  - 量子コンピュータの攻撃ベクトルを遮断する。
  answer_index: 1
  explanation: oqs-providerはOpenSSLのプロバイダーアーキテクチャを使用してPQCアルゴリズムを標準ライブラリに統合し、それによって既存のアプリケーションがPQCアルゴリズムを使用できるようにします。
- question: 隔離された実験環境でバージョンを固定(Locking)すべき理由は何ですか？
  choices:
  - 最新バージョンが常に高速であるためである。
  - 再現性を保証し、研究者間での実行環境の差異による測定誤差を減らすためである。
  - 運用セキュリティを強化するためである。
  - ビルド時間を短縮するためである。
  answer_index: 1
  explanation: バージョン固定は同一環境を再現可能にし、パフォーマンス測定値の整合性と研究の客観性を確保するために不可欠です。
completion_criteria:
- Dockerベースの隔離されたビルド環境構成に成功。
- oqs-providerを通じたML-KEMハイブリッドモードのデモンストレーション完了。
- 実験データ測定およびセキュリティポリシーが含まれたレポート提出。
source_ids:
- S2
---

### 隔離されたPQC実験環境の必要性
量子コンピュータの脅威から既存の公開鍵暗号(RSA, ECDHなど)を保護するために、NISTはML-KEM(Kyberベース)およびML-DSA(Dilithiumベース)のような耐量子アルゴリズムを標準化した。これらのアルゴリズムのパフォーマンスとセキュリティをローカル環境で評価するには、**暗号アジリティ(Crypto-agility)**を備えた再現可能な環境が不可欠である [S2]。

#### 1. 主要構成要素
*   **liboqs**: PQCアルゴリズムをC言語で実装したライブラリであり、様々なKEMおよび署名アルゴリズムをテストできる基盤を提供する。
*   **oqs-provider**: OpenSSL 3 のプロバイダーアーキテクチャを使用して、PQCアルゴリズムを既存のTLSインフラに統合可能にするインターフェースである。
*   **ハイブリッドモード**: 既存の古典暗号(ECDH)とPQCアルゴリズムを結合し、PQCライブラリの潜在的な脆弱性にもかかわらず既存のセキュリティレベルを維持する移行期の戦略である [S2]。

#### 2. 実験環境の鍵: 隔離および再現性
実験は運用環境と完全に分離されるべきである。Dockerなどのコンテナ技術を使用して依存関係バージョンを固定(Locking)すれば、研究者間での実行結果の差異を減らし、アルゴリズム最適化(例: AVX-512 活用)の効果を正確に測定できる [S2]。ハンドシェイクパフォーマンス評価時には、固定されたハードウェアと隔離されたネットワークを使用して、遅延時間の不確実性を最小限に抑える必要がある。
