---
layout: learn-module
title: 移行優先順位レポートの作成
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-ja
course_locale: ja
lang: ja
ref: learn:post-quantum-cryptography-migration-lab:migration-roadmap
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/migration-roadmap/
module_id: m8
permalink: /learn/ja/post-quantum-cryptography-migration-lab/migration-roadmap/
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
id: m8
slug: migration-roadmap
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m7
objectives:
- 耐量子計算機暗号（PQC）移行のためのリスクおよびビジネス影響分析フレームワークの理解
- 暗号資産インベントリデータに基づく移行優先順位の決定
- 暗号アジリティ（Cryptographic Agility）確保のための技術戦略の策定
- 最終移行ロードマップおよび検証レポートの構造化
worked_examples:
- 例 1：データライフサイクルに基づく優先順位算出 - 20年保存される個人情報データベースは、5年保存されるログデータよりもPQC移行の優先順位が高く評価される。
- 例 2：ハイブリッドTLS構成事例 - 既存のECDHとML-KEMを組み合わせ、両アルゴリズムのいずれか一方が安全であれば通信機密性が維持されるように設計するハイブリッドモデルの分析。
lab:
  title: 移行ロードマップシミュレーション
  steps:
  - 前のモジュールで作成したインベントリCSVデータを読み込みます。
  - 各資産に対して[リスク * 重要度 * 寿命]スコアを算出するPythonスクリプトを作成します。
  - 優先順位上位3個の資産に対するハイブリッド実装計画を立てます。
  - 移行時に発生し得る互換性の問題と対応策（フォールバック戦略）を記述します。
  safety:
  - すべての計算および分析は、独立した隔離仮想環境でのみ行います。
  - 運用サーバーの実際の暗号構成は変更しません。
  - 実際の鍵素材が含まれないよう、分析ノートブックを確認します。
  deliverables:
  - 優先順位付けされたインベントリCSV分析版
  - 移行計画を含む技術意思決定表
assignment:
  title: PQC移行優先順位レポート
  deliverables:
  - 暗号アジリティ分析レポート（PDF）
  - リスク等級に基づく移行ロードマップ（表を含む）
  rubric:
  - データ寿命および露出リスクに基づく妥当な優先順位論理
  - ハイブリッド暗号体系導入を通じた暗号アジリティの考慮
  - 移行計画の段階的な実行可能性
  - 実験結果およびデータインベントリとの整合性
quiz:
- question: 暗号移行の優先順位を決定する際、最も考慮すべきデータ特性は何ですか？
  choices:
  - データが使用されるプログラミング言語
  - データのセキュリティ必要寿命（Data Shelf Life）
  - システムの開発者数
  - 最新データストレージの容量
  answer_index: 1
  explanation: 量子脅威はデータが将来解読されるリスクを内包しているため、長期間機密が維持されるべきデータが最も優先的にPQC移行を必要とします。
- question: 暗号アジリティ（Cryptographic Agility）のために推奨されるソフトウェア設計方式は何ですか？
  choices:
  - ハードコーディングされた暗号アルゴリズムの使用
  - 暗号モジュールとビジネスロジックの抽象化分離
  - 単一アルゴリズムのみを使用するクローズド構造
  - OSレベルの暗号ライブラリの直接参照
  answer_index: 1
  explanation: 暗号エンジンとロジックを分離し、アルゴリズム交換時のコード変更を最小限に抑える構造が、暗号アジリティ確保の鍵です。
completion_criteria:
- 移行優先順位が明記されたインベントリ分析ファイルの提出
- 暗号アジリティの考慮事項が含まれた移行ロードマップレポートの作成
- すべての実習コードおよび測定値が含まれた再現パッケージの完了
source_ids:
- S1
---

### 移行優先順位戦略 (Migration Prioritization Strategy)

NIST耐量子標準（ML-KEM、ML-DSA）への移行は、システム全体の暗号資産評価から始まります。移行の優先順位は、単にアルゴリズムの老朽化度だけでなく、データの寿命（Data Shelf Life）、暗号露出のリスク、そしてシステムの戦略的重要度に応じて決定されます [S1]。

#### 1. 暗号資産評価基準 (Assessment Criteria)
移行の緊急度を判断するために、次の基準を活用します：
- **データセキュリティ寿命：** 暗号化されたデータが将来の量子コンピュータによって解読された場合に及ぼす影響（例：10年以上機密保持が必要なデータ）。
- **システムアジリティ：** 現在実装されている暗号がハードコーディングされているか、構成ファイル（Config）を通じてアルゴリズムの交換が可能か否か。
- **技術的負債：** 当該暗号モジュールを使用する依存関係（Dependency）およびメンテナンスの可否。

#### 2. 暗号アジリティの確保
移行ロードマップの鍵は、アルゴリズム交換時のコード変更を最小限に抑えることです。抽象化レイヤー（Abstraction Layer）を使用してビジネスロジックと暗号エンジンを分離し、ハイブリッド鍵交換方式を通じて既存アルゴリズムの安定性とPQCの量子耐性を同時に確保する戦略が推奨されます。
