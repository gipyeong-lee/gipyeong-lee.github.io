---
layout: learn-module
title: 引用の正確性および出典追跡
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-ja
course_locale: ja
lang: ja
ref: learn:rag-evaluation-reliability:citation-accuracy
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/citation-accuracy/
- lang: en
  url: /learn/en/rag-evaluation-reliability/citation-accuracy/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/citation-accuracy/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/citation-accuracy/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/citation-accuracy/
module_id: m6
permalink: /learn/ja/rag-evaluation-reliability/citation-accuracy/
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
id: m6
slug: citation-accuracy
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m5
objectives:
- RAGシステムにおいて、回答が検索されたドキュメントの内容をどれだけ忠実に反映しているかを理解する。
- 引用（Citation）の正確性の定義と測定方法を学習する。
- Ragasフレームワークを活用し、回答の根拠忠実度（Faithfulness）と回答関連性（Answer Relevance）を定量評価する。
- モデルの回答における出典追跡可能性を検証するプロセスを設計する。
worked_examples:
- 例 1：根拠忠実度スコアの計算。質問「A社の 2025 年の売上は？」に対して回答「A社の 2025 年の売上は 100 億です。」が生成され、コンテキストドキュメントに「A社は
  2025 年に 100 億の売上を記録した。」が含まれている場合、回答のすべての情報がコンテキスト内に存在するため、根拠忠実度スコアは 1.0 （最大値）と評価されます。
- 例 2：引用正確性のエラー識別。質問「A社の創立年は？」に対して回答「A社は 1990 年に創立されました（参照：ドキュメント 1）。」が生成されたが、ドキュメント
  1 に「A社は 1995 年創立」と明示されている場合、これは「事実歪曲」の失敗タイプに分類され、引用正確性が低いと判断します。
lab:
  title: Ragasを活用した回答の根拠忠実度自動評価実習
  steps:
  - 評価するRAGシステムの検索結果（Context）と生成された回答（Answer）のデータセットを準備します。
  - Ragasフレームワークをインストールし、回答データセットを読み込みます。
  - Ragasの `Faithfulness` 指標を使用して、データセットの各質問と回答のペアに対してスコアを計算します。
  - 根拠忠実度が 0.7 未満の回答 30 件を別途抽出します。
  - 抽出されたサンプルを人間が直接確認し、「引用漏れ」、「虚偽引用」、「事実歪曲」のいずれかの失敗タイプをタグ付けします。
  safety:
  - 評価プロセスで使用されるドキュメントコーパスに個人情報や企業機密が含まれないよう、事前に非識別化処理を完了してください。
  - 外部API呼び出し時にはコスト上限を設定し、再現性のためにシード（Seed）値を固定することで、繰り返しのAPIコスト発生を防止してください。
  deliverables:
  - 評価結果が含まれるJupyter Notebookファイル（.ipynb）
  - 根拠忠実度スコア分布の可視化チャート
  - 人間によるレビュー記録を含む失敗タイプ分類テーブル
assignment:
  title: RAGシステム信頼性回帰評価レポートの作成
  deliverables:
  - 二つ以上のRAG設定（例：検索Top-k値の変更）に基づく根拠忠実度の統計比較結果
  - サンプル 30 件に対する人間によるレビュー対照表
  - システムの引用正確性向上のための改善提案書
  rubric:
  - 評価指標の定量的算出方式が正確に明示されているか？
  - 検索ドキュメントと生成された回答間の引用関係が論理的に追跡可能か？
  - 失敗タイプの分類が人間によるレビューデータと一致し、妥当な根拠が提示されているか？
quiz:
- question: Ragasフレームワークの「根拠忠実度（Faithfulness）」指標に関する説明として正しいものは？
  choices:
  - 回答が質問と関連性があるかを評価する。
  - 回答のすべての情報が提供されたコンテキストドキュメント内に存在するかを測定する。
  - 回答が文法的にどれだけ正確かを評価する。
  - 回答が外部知識ベースのすべての情報を含んでいるかを測定する。
  answer_index: 1
  explanation: 根拠忠実度は、生成された回答の主張が検索されたコンテキストに基づいているかを測定する指標です。
- question: 引用正確性の評価時、「事実歪曲」の失敗タイプに該当するのは？
  choices:
  - 検索ドキュメントにない内容を回答に含めた場合
  - 引用表示を漏らした場合
  - 引用は正しく表示されているが、原文の事実関係を誤解釈して記述した場合
  - 回答が質問の意図と完全に異なる場合
  answer_index: 2
  explanation: 事実歪曲は、ソースドキュメントを引用したにもかかわらず、原文の情報を間違った方法で要約または変形して生成してしまった場合を指します。
completion_criteria:
- Jupyter Notebookを通じた自動化された評価指標の算出完了
- 少なくとも 30 件の回答サンプルに対する人間によるレビューおよび失敗タイプ分類記録の提出
- 評価結果と改善策が含まれる最終レポートの作成
source_ids:
- S4
---

## RAGシステムの引用および根拠忠実度評価

RAG（Retrieval Augmented Generation）システムは外部知識ベースを活用してLLMのハルシネーション（Hallucination）リスクを低減させますが、生成された回答が検索されたドキュメントを正確に引用しているかを検証するプロセスが必須です [S4]。

### 1. 主要評価指標
* **根拠忠実度（Faithfulness）：** 生成された回答が提供された検索コンテキスト（Context）から導出されているかを測定します。回答のすべての主張が検索されたドキュメントに基づいていなければならず、外部知識やモデルの事前学習知識のみで回答する場合はスコアが低くなります [S4]。
* **回答関連性（Answer Relevance）：** 回答が与えられた質問とどれだけ直接的に関連しているかを評価します。これは、検索された情報が十分であっても、回答が質問の意図から逸脱している場合を特定するために使用されます。

### 2. 引用正確性検証プロセス
引用正確性は、回答の特定の文章が検索されたコンテキストのどこを引用したかを識別し、その原文の事実と一致しているかを確認するプロセスです。自動評価フレームワークであるRagasは、このプロセスを実行するために、参照データ（Ground Truth）がなくても根拠忠実度を評価できる指標を提供します [S4]。

### 3. 失敗タイプ分類
- **引用漏れ：** 回答の事実関係が検索ドキュメントに存在するにもかかわらず、引用を表示していない。
- **虚偽引用：** 検索ドキュメントにない内容を引用したかのように表示。
- **事実歪曲：** 引用は正しく表示されているが、原文の意味を誤解釈して生成した。
