---
layout: learn-module
title: 暗号資産の特定および管理
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-ja
course_locale: ja
lang: ja
ref: learn:post-quantum-cryptography-migration-lab:crypto-inventory
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/crypto-inventory/
module_id: m3
permalink: /learn/ja/post-quantum-cryptography-migration-lab/crypto-inventory/
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
id: m3
slug: crypto-inventory
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- 暗号資産の特定(Cryptographic Inventory)の概念と必要性を説明する。
- 組織内の暗号化アルゴリズム、ライブラリ、使用箇所を体系的に分類する方法を習得する。
- 暗号アジリティ(Crypto-agility)のためのメタデータ管理要素を把握する。
- 特定された暗号資産のリスクを評価して、耐量子移行の優先順位を決定する。
worked_examples:
- 'システムスキャン結果の例: 「TLS 1.2(ECDHE-RSA-AES128-GCM-SHA256) を使用中」という資産特定。この場合、RSAとECDHEが量子脅威に露出していることを認識し、ML-KEM/ML-DSA移行対象として分類する。'
- '暗号アジリティ自己診断表: 「アルゴリズムがハードコーディングされているか？」という問いに「はい」であればリスクスコアを上げる。「設定ファイルを介した暗号アルゴリズムの選択が可能か？」という問いに「いいえ」であれば移行難易度を上げる。'
lab:
  title: 暗号資産の特定およびリスク評価実習
  steps:
  - サンプルプロジェクトのソースコードを対象に、「AES」、「RSA」、「ECC」のキーワード検索を実行して使用箇所を特定する。
  - 特定された暗号実装体(ライブラリを含む)を「暗号資産Inventory CSV」に記録する。
  - 各資産について「セキュリティ寿命」、「量子脅威レベル」、「データの重要度」を基準としてリスクスコアを算定する。
  - 算定されたスコアに基づき、移行優先順位(P0~P3)を分類する。
  safety:
  - 実際に運用中のシステムの秘密鍵や実際のサービス証明書をスキャンしないこと。
  - テストのために仮想環境内に隔離されたダミー証明書(テスト用)のみを使用すること。
  - 分析結果物(CSV, 文書)に実際の秘密値や暗号鍵値を含めないこと。
  deliverables:
  - 暗号資産Inventory CSVファイル (アルゴリズム, 使用箇所, ライブラリ, ライブラリバージョンを含む)
  - 優先順位ベースの暗号資産リスク評価レポート (Markdown)
assignment:
  title: 暗号アジリティ分析および移行ロードマップの策定
  deliverables:
  - 暗号資産Inventory CSV
  - 移行優先順位が定義された意思決定表
  - 耐量子移行ロードマップ
  rubric:
  - 暗号資産が包括的に特定されているか？
  - リスク評価基準が客観的かつ妥当か？
  - 移行ロードマップが耐量子技術移行の論理的順序に従っているか？
  - 暗号アジリティ改善のための具体的な技術提案が含まれているか？
quiz:
- question: 暗号資産の特定(Cryptographic Inventory)の主な目的は何か？
  choices:
  - すべての暗号化ライブラリのパフォーマンスを最適化するため
  - PQC移行を準備するため、組織内の暗号依存関係を把握するため
  - 暗号化アルゴリズムをすべて削除するため
  - 非対称暗号のみを使用するように強制するため
  answer_index: 1
  explanation: 暗号資産の特定は、移行すべき暗号化アルゴリズムの位置と依存関係を体系的に管理し、PQC移行を効率的に遂行することを目的とします。
- question: 次の中で暗号アジリティ(Crypto-agility)の定義として最も適切なものはどれか？
  choices:
  - より強力な暗号化のためにハードウェアを交換するプロセス
  - 暗号化ライブラリのアップデートを自動化する機能
  - コード変更を最小限に抑え、必要に応じて迅速に暗号アルゴリズムを交換できる柔軟性
  - 暗号化鍵を非常に頻繁に変更すること
  answer_index: 2
  explanation: 暗号アジリティとは、アルゴリズム交換時のコード変更負担を最小化し、変化するセキュリティ環境に適応する能力を意味します。
completion_criteria:
- 暗号資産特定Inventory CSVを提出し、リスク評価が完了していること
- 各暗号資産の移行難易度およびリスク優先順位が明記されたレポートを作成すること
- クイズ項目で 100% の正解率に到達
source_ids:
- S1
---

## 暗号資産の特定 (Cryptographic Inventory)

暗号資産の特定とは、組織内で使用されているすべての暗号化アルゴリズム、プロトコル、ライブラリ、およびそれらが適用されているシステムやデータを体系的にリスト化するプロセスである。これは耐量子暗号(PQC)への移行を準備する第一段階であり、保護対象となる暗号アルゴリズムの依存関係を明確に把握することが重要である [S1]。

### 1. 主要管理対象
- **アルゴリズムおよびプロトコル**: TLS, SSH, コード署名, データ暗号化(AES, RSA, ECCなど)など。
- **インフラ**: 認証局(CA), 鍵管理システム(KMS), HSM, クラウド鍵ストレージ。
- **ソフトウェア**: 暗号化ライブラリのバージョン(OpenSSL, BoringSSLなど)および静的/動的リンクの有無。

### 2. 暗号アジリティ(Crypto-agility)
暗号アジリティとは、コード変更を最小限に抑えながら暗号化アルゴリズムを迅速に交換できる能力を意味する。これを実現するため、システムは特定のアルゴリズムにハードコーディングされず、設定ファイルを介してアルゴリズムを選択できる抽象化レイヤーを持つべきである。

### 3. リスク評価基準
- **データライフサイクル**: 暗号化されたデータは未来においても秘密を維持しなければならないか？ (例: 今盗取されて未来に解読されるリスクがあるデータ)
- **移行難易度**: ハードウェアの交換が必要か、それともソフトウェアのアップデートだけで十分か？
- **規制およびコンプライアンス**: NIST PQC標準の適用時期との整合性。
