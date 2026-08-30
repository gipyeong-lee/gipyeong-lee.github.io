---
layout: learn-module
title: 評価用ドキュメントコーパスのキュレーション
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-ja
course_locale: ja
lang: ja
ref: learn:rag-evaluation-reliability:corpus-curation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/corpus-curation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/corpus-curation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/corpus-curation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/corpus-curation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/corpus-curation/
module_id: m2
permalink: /learn/ja/rag-evaluation-reliability/corpus-curation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: f439c689d3754cecbf386ffcc0c2bd7c
translation_run_id: 90eea7090f164c87b308c88bd9c36c4a
primary_category: ai-software
topics:
- retrieval-augmented-generation
- rag-evaluation
- information-retrieval
- llm-reliability
course_type: academic
published_at: '2026-08-30T15:42:37.390479+09:00'
id: m2
slug: corpus-curation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- RAG評価のための固定ドキュメントコーパスの重要性を理解する。
- 評価用ドキュメントデータの品質決定要素（正確性、多様性、重複排除）を学習する。
- 定量的な評価のためのドキュメント-質問-正解ペア (QA Pair) データセット構築戦略を習得する。
- データ漏洩 (Data Leakage) を防止するための学習/評価データの分割方法を習得する。
worked_examples:
- '例 1: ドキュメントチャンキング (Chunking) 戦略。テキストを固定サイズに分割する際、文脈が切れないように段落単位や意味単位で分けるPythonスクリプトの作成方法。'
- '例 2: 質問-回答データの構成。{ ''question'': ''...'', ''ground_truth'': ''...'', ''context_chunk_id'':
  ''...'' } 形式のJSONオブジェクト生成例。'
lab:
  title: 評価用コーパス構築の実習
  steps:
  - 評価対象ドメインのオープンライセンステキストファイル (.txt) を確保する。
  - Pythonを使用してテキストファイルを読み込み、チャンク単位に分けるスクリプトを作成する。
  - 各チャンクに一意の識別子 (ID) を付与し、メタデータ（タイトル、ソース）を記録する。
  - 作成したチャンクの中から質問を生成し、回答の根拠となるチャンクIDを記録して50個のQAペアを構成する。
  - 全コーパスを8:2の比率で開発セットとテストセットに分割して保存する。
  safety:
  - 個人情報が含まれるドキュメントは、評価コーパスに含めないこと。
  - 外部API使用時はリクエスト回数の上限を設定して費用を制御すること。
  - 作業時に生成されたデータはGitを通じてバージョン管理を行い、再現性を確保すること。
  deliverables:
  - 構築されたドキュメントコーパスファイル (JSONL形式)
  - 質問と正解が含まれたQAデータセット (JSON形式)
  - コーパス分割記録が収められたJupyter Notebookファイル
assignment:
  title: ドメインベースのRAGデータセット完成
  deliverables:
  - 少なくとも100問のQAデータセットファイル
  - データセット統計分析レポート（質問の長さ、チャンクの長さなど）
  - データ分割過程が含まれたPythonコード
  rubric:
  - コーパス内の重複チャンク除去の完了状況
  - テストセットと開発セットのデータ漏洩の有無確認
  - 回答の根拠となるドキュメント区間 (Chunk ID) の正確なマッピング状況
quiz:
- question: RAGシステムにおいて「データ漏洩 (Data Leakage)」を防止する最善の方法は何ですか？
  choices:
  - すべてのドキュメントに対して同一の質問を生成する。
  - 開発セットと最終評価用テストセットを分離して管理する。
  - 学習データに検索対象ドキュメント全体を含める。
  - 評価セットを毎回新しく生成して管理する。
  answer_index: 1
  explanation: 評価セットが学習（または開発）過程で検索対象ドキュメントに露出すると公平な評価が不可能なため、評価用テストセットを厳格に分離しなければなりません。
- question: コーパスキュレーション過程において「重複排除」が重要な理由は何ですか？
  choices:
  - LLMの生成速度を速めるため
  - ディスクの保存容量を節約するため
  - 検索結果の多様性を確保し、統計的な偏りを防止するため
  - ドキュメントの意味論的類似度を下げるため
  answer_index: 2
  explanation: 重複した情報は、検索エンジンが特定情報に偏って検索結果を返すように仕向け、定量的な評価指標を歪曲させる恐れがあります。
completion_criteria:
- 評価用ドキュメントコーパス（最低100個のチャンク以上）構築完了
- 検証可能なQAデータセット（最低100問）作成完了
- データセット分割ポリシー遵守の確認
- 成果物に対するピアレビューまたは自己評価チェックリストの作成完了
source_ids:
- S2
---

## RAG評価のためのコーパスキュレーション

大規模言語モデル (LLM) は学習されたパラメータ内の知識に依存する場合、ハルシネーション（幻覚）のリスクが存在します。検索拡張生成 (RAG) は、モデルがリアルタイムで外部知識にアクセスできるようにすることで、このような限界を克服します [S2]。効果的なRAGシステムの信頼性を定量的に評価するためには、**固定され、制御可能な評価用ドキュメントコーパス (Fixed Evaluation Corpus)** が不可欠です。

### 1. コーパス品質の決定要素
- **正確性 (Factuality):** ドキュメント内の情報は最新かつ事実である必要があります。誤った情報が含まれたコーパスは、誤った回答を生成させます。
- **ドメイン適合性:** 評価しようとする実際のサービス環境と類似したトピックや語彙を含んでいる必要があります。
- **重複排除 (De-duplication):** 同一情報が複数のドキュメントに重複していると、検索結果の多様性が損なわれ、評価統計に偏りを与える可能性があります。

### 2. QA評価データセットの構築
ドキュメントコーパスだけでは評価は不可能です。「ドキュメント-質問-正解」ペアを構築し、検索器が関連ドキュメントを正しく持ってくるか、生成器がこれを基に正確な回答をするかを測定しなければなりません。
- **質問生成:** LLMを使用してドキュメントから自動的に質問を生成するか、ドメイン専門家が直接作成します。
- **正解の定義:** 回答の根拠となるドキュメント区間 (Chunk) を明確に明示しなければなりません。

### 3. データの分割と整合性
評価セットの信頼性のため、**開発用 (Development Set)** と **最終評価用 (Hold-out Test Set)** を厳格に分割しなければなりません。評価セットに含まれる質問が、検索対象ドキュメントに直接含まれて露出してしまう「データ漏洩」現象を防止しなければなりません。
