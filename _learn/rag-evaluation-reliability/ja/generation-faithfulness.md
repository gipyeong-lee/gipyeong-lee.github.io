---
layout: learn-module
title: 根拠忠実度評価
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-ja
course_locale: ja
lang: ja
ref: learn:rag-evaluation-reliability:generation-faithfulness
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/generation-faithfulness/
- lang: en
  url: /learn/en/rag-evaluation-reliability/generation-faithfulness/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/generation-faithfulness/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/generation-faithfulness/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/generation-faithfulness/
module_id: m5
permalink: /learn/ja/rag-evaluation-reliability/generation-faithfulness/
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
id: m5
slug: generation-faithfulness
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- 根拠忠実度(Faithfulness)の概念を理解し、RAGシステムにおける重要性を把握する。
- Ragasフレームワークを活用し、生成された回答が検索されたコンテキスト(Context)に基づいているか定量的に評価する。
- 自動化された評価指標を活用して幻覚(Hallucination)リスクを分析する。
worked_examples:
- '例 1: コンテキスト「リンゴはビタミンCが豊富だ」と回答「リンゴはビタミンCが多く免疫力に良い」がある場合、「免疫力に良い」はコンテキストにない情報なので根拠忠実度スコアが低下する。'
- '例 2: コンテキスト「当社の創立日は 2020年 5月 1日である」と回答「当社は 2020年 5月に設立された」という情報は一致するため、高い根拠忠実度スコアを持つ。'
lab:
  title: Ragasを活用した生成回答の根拠忠実度測定
  steps:
  - 評価データセット(質問、検索されたコンテキスト、生成された回答)を準備する。
  - Ragasライブラリをインストールし、`Faithfulness`メトリックをインポートする。
  - 準備されたデータセットをRagasのデータ構造に変換する。
  - LLMベースの評価者を構成してデータセットの根拠忠実度スコアを算出する。
  - スコアが低い回答を標本抽出し、検索されたコンテキストとの差異を人間による検討で分析する。
  safety:
  - 非公開文書や個人情報が含まれたデータセットを外部LLM APIに伝送しない。
  - APIリクエスト数制限を確認し、キャッシュ(Cache)を使用してコストを制御する。
  - 人間による検討時、標本データのセキュリティを維持する。
  deliverables:
  - データセット全体の平均根拠忠実度スコアレポート
  - 低スコアを記録した回答の分析データセット
  - 自動評価結果と人間によるレビュー結果の比較分析
assignment:
  title: RAGパイプライン信頼性評価レポート
  deliverables:
  - 根拠忠実度評価を含むJupyter Notebook
  - エラー分類およびハルシネーション発生頻度分析レポート
  rubric:
  - 根拠忠実度メトリクスが正しく実装されているか？
  - 生成された回答のハルシネーション事例を正確に分類したか？
  - 自動評価結果と人間によるレビューの定性的一貫性が確保されているか？
quiz:
- question: RAGシステムにおける「根拠忠実度（Faithfulness）」とは何か？
  choices:
  - 検索されたコンテキストが質問と関連性が高い程度
  - 生成された回答が、検索されたコンテキストの情報に基づいている程度
  - LLMが事前学習済みの知識を多く活用している程度
  - ユーザーの質問に回答が正確に一致する程度
  answer_index: 1
  explanation: 根拠忠実度は、生成された回答が外部から検索されたコンテキストの事実に依存しているかを評価する指標です。
- question: Ragasフレームワークの特徴として正しいものは？
  choices:
  - 必ず人間による注釈（Ground Truth）がなければ評価できない。
  - 参照基盤のない（reference-free）評価方式をサポートする。
  - 検索効率のみを評価し、生成品質は評価しない。
  - LLMを評価者として活用せず、統計的な方式のみを使用する。
  answer_index: 1
  explanation: Ragasは参照基盤なしで評価可能なフレームワークを目指しており、LLMを評価者として積極的に活用します [S3, S4]。
completion_criteria:
- Ragasライブラリを使用して、生成された回答の根拠忠実度を定量的に測定できる。
- 評価結果から、ハルシネーションの発生タイプを少なくとも 3 種類以上分類できる。
- 自動化された評価パイプラインの結果と実際の回答の一貫性を検証できる。
source_ids:
- S3
- S4
---

## 根拠忠実度 (Faithfulness) 評価

RAG(Retrieval-Augmented Generation)システムの核心は、LLMが外部知識データベースから検索された情報を活用して回答を生成することである。根拠忠実度(Faithfulness)は、生成された回答が検索されたコンテキストに記述された情報のみを忠実に反映しているかを示す指標である [S3]。

### 1. なぜ根拠忠実度を評価するのか？
LLMは事前学習された知識に基づいて回答しようとする傾向があり、検索されたコンテキストと無関係な情報を生成したり、コンテキストを歪曲したりすることがある。これを「幻覚(Hallucination)」と呼び、根拠忠実度評価を通じてこれを定量的に測定できる [S4]。

### 2. 評価フレームワーク: Ragas
Ragasはユーザーによる注釈がない状況でも、参照なし(reference-free)で評価が可能なフレームワークを提案する [S3]。根拠忠実度評価過程は一般的に次の段階に従う:
- **回答から陳述の抽出**: 回答から検証可能な事実的陳述を分離する。
- **証拠の検索**: 各陳述が検索されたコンテキストのどの部分から導き出されたか確認する。
- **検証**: 抽出された陳述がコンテキスト情報と一致するか判断する。

RagasはLLMを評価者として使用し、この過程を自動化する [S4]。
