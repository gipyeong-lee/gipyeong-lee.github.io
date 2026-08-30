---
layout: learn-module
title: 自動評価フレームワーク（Ragas）の適用
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-ja
course_locale: ja
lang: ja
ref: learn:rag-evaluation-reliability:automated-eval-framework
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/automated-eval-framework/
- lang: en
  url: /learn/en/rag-evaluation-reliability/automated-eval-framework/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/automated-eval-framework/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/automated-eval-framework/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/automated-eval-framework/
module_id: m7
permalink: /learn/ja/rag-evaluation-reliability/automated-eval-framework/
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
id: m7
slug: automated-eval-framework
phase_id: p2
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- RAGパイプラインの主要な評価次元（検索および生成品質）を理解する。
- Ragasフレームワークを使用して、参照なし（reference-free）でRAG性能を自動評価する方法を習得する。
- 定量的なメトリクスを通じてハルシネーション（hallucination）リスクを分析および緩和する。
worked_examples:
- 事例 1：Context Relevanceの計算。RagasはLLMを使用して、検索されたコンテキスト（Context）から質問に回答するために実際に必要な文章を抽出し、全体のコンテキストに対する必要な文章の割合を通じてスコアを計算します。
- 事例 2：Faithfulnessの評価。生成された回答の各主張が、検索されたコンテキストで支持されているかをLLMが判断します。支持されていない主張が多いほど、ハルシネーションスコアが高くなります。
lab:
  title: Ragasを活用したRAG性能定量評価実習
  steps:
  - 評価データセット（質問、検索されたコンテキスト、生成された回答）を準備します。
  - Python環境で `ragas` ライブラリをインストールします。
  - 評価データセットを `ragas` のDatasetオブジェクトに変換します。
  - Ragasの `evaluate` 関数を呼び出し、Context RelevanceやFaithfulnessなどのメトリクスを計算します。
  - 結果を可視化し、スコアが低いクエリを分析します。
  safety:
  - 評価に使用するドキュメントコーパスに個人情報や非公開データが含まれていないかを確認します。
  - APIの使用コストを防ぐために、テスト時にはローカルモデルやキャッシュを積極的に活用します。
  - 自動評価結果は信頼性の補助指標であり、実際のモデルの品質確定は、人間によるサンプルレビューと交差検証を並行して行います。
  deliverables:
  - メトリクススコアが含まれる評価結果のデータフレーム
  - 低スコアを受けたクエリタイプの分析ログ
assignment:
  title: RAGパイプライン性能比較レポート
  deliverables:
  - 検索設定（k値、埋め込みモデルなど）が異なる二つのRAGパイプラインのRagas評価結果
  - 二つの設定間の性能差分析報告書
  rubric:
  - Ragasメトリクス（Context Relevance, Faithfulnessなど）が正しく実装されているか？
  - 評価結果が定量的に比較され、論理的な解釈が含まれているか？
  - ハルシネーションタイプを少なくとも 3 件以上分類し、改善案を提示したか？
quiz:
- question: Ragasフレームワークの最大の利点は何ですか？
  choices:
  - 人間の正解データセットが必ず必要である
  - 参照なしで（reference-free）RAGパイプラインを評価できる
  - 検索段階のみを評価し、生成段階は評価しない
  - GPUが必ず 10 台以上必要である
  answer_index: 1
  explanation: Ragasは正解データセットなしでLLMを活用し、検索および生成品質を自動評価するフレームワークです [S3, S4]。
- question: Ragasで測定する「Faithfulness」メトリクスの定義は何ですか？
  choices:
  - 検索されたコンテキストが質問とどれだけ関連しているか
  - 質問がドキュメントコーパス内に存在するか
  - 生成された回答が検索されたコンテキストに基づいているか
  - 質問者がLLMの回答をどれだけ信頼しているか
  answer_index: 2
  explanation: Faithfulnessは、生成された回答が提供された検索コンテキストにどれだけ忠実に基づいているか（ハルシネーション防止）を測定する指標です
    [S4]。
completion_criteria:
- Ragasライブラリを使用して、少なくとも10件のクエリに対して4種類以上のメトリクスを計算することに成功していること
- 実習ノートブックがGitリポジトリに定期的にコミットされていること
- 性能比較レポート内に、少なくとも3件のエラー分類事例が含まれていること
source_ids:
- S3
- S4
---

## RAG評価の課題とRagas

RAGシステムは検索モジュールとLLMベースの生成モジュールで構成されます [S3, S4]。このような構造を評価することは困難な作業です。なぜなら、検索システムが関連性の高いコンテキスト（context）をどれだけうまく識別できているか、LLMが提供されたコンテキストをどれだけ忠実に（faithfully）活用できているか、そして回答の品質はどうか、これらすべてを考慮しなければならないからです [S4]。

従来の評価方法は、人間が直接正解（ground truth）を作成し比較する方式に依存していましたが、これはコストがかかり時間がかかるため、迅速な反復サイクルには不向きです [S3, S4]。

### Ragasフレームワーク
Ragas（Retrieval Augmented Generation Assessment）は、正解データセットがなくてもRAGパイプラインを評価できるフレームワークです [S3, S4]。Ragasは以下の重要な次元を自動評価します：

1. **検索品質（Retrieval Quality）：** 検索されたコンテキストが質問とどれだけ関連しているか（Context Relevance）、必要な情報をすべて含んでいるか（Context Recall）を測定します。
2. **生成品質（Generation Quality）：** 生成された回答が検索されたコンテキストに基づいているか（Faithfulness）、質問とどれだけ関連しているか（Answer Relevance）を測定します。

これらのメトリクスは、LLMを「評価者（judge）」として活用することで、参照なしでも評価を可能にし、RAG開発サイクルを短縮することに貢献します [S3, S4]。
