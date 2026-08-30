---
layout: learn-module
title: RAGアーキテクチャの理解
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-ja
course_locale: ja
lang: ja
ref: learn:rag-evaluation-reliability:intro-rag-architecture
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/intro-rag-architecture/
- lang: en
  url: /learn/en/rag-evaluation-reliability/intro-rag-architecture/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/intro-rag-architecture/
module_id: m1
permalink: /learn/ja/rag-evaluation-reliability/intro-rag-architecture/
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
id: m1
slug: intro-rag-architecture
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- RAG (Retrieval-Augmented Generation) アーキテクチャの主要構成要素を理解する。
- 大規模言語モデル (LLM) が持つ知識の限界と、検索ベースの拡張の必要性を把握する。
- 検索-生成パイプラインの構造的な流れを説明できるようにする。
worked_examples:
- '事例 1: 従来のLLM方式 - 「今日のニュースを教えて」と質問した場合、学習データ以降の出来事を認識できず、誤った情報を生成するリスクがある。'
- '事例 2: RAG方式 - 「今日のニュースを教えて」と質問した際、1) 外部検索エンジンやリアルタイムニュースAPIを通じて検索器 (Retriever)
  が関連記事を収集し、2) これを文脈 (context) として含めてLLMに渡すことで、正確な最新情報の回答を生成。'
lab:
  title: RAGアーキテクチャのフロー可視化および分析
  steps:
  - Jupyter Notebookを開き、RAG基本パイプラインの3段階（入力、検索、生成）の構造を模式化する。
  - オープンライセンスのドキュメントコーパスから5個の短いテキストを抽出し、データセットのサンプルを作成する。
  - 単純なキーワードマッチングを行う検索器 (Retriever) 関数を作成し、質問に適したドキュメントを返すよう実装する。
  - 検索されたドキュメントをプロンプトテンプレートに注入する拡張段階をコードで作成する。
  safety:
  - 実際の個人情報や機密ドキュメントを、絶対にコーパスデータとして使用しないこと。
  - API使用時は呼び出し回数の制限 (Rate Limit) を確認し、テストコードにシード (seed) 値を設定して再現性を確保すること。
  deliverables:
  - RAGアーキテクチャのダイアグラム (Notebookセル内に含めること)
  - 単純なキーワードベースの検索器の実装コード
  - ドキュメント注入型プロンプトの生成結果
assignment:
  title: RAGベースの情報検索パイプライン分析レポート
  deliverables:
  - 実装したRAGパイプラインの動作原理を説明するNotebook
  - 検索器がドキュメントの関連性を判断する際に発生しうる潜在的な失敗事例3件の記述
  rubric:
  - RAGの3段階（検索、拡張、生成）が正確に区別されて説明されているか？
  - 検索段階において、無関係なドキュメントが検索される可能性に対する分析が妥当か？
  - 非公開データのセキュリティ指針を遵守して実装したか？
quiz:
- question: RAGがLLMの学習方式と比較して持つ主な利点は何ですか？
  choices:
  - LLMのパラメータサイズを削減できる。
  - モデルの知識を最新の状態に維持し、根拠を提示できる。
  - モデルの学習速度を加速させる。
  - すべての質問に対して100%事実である回答を生成する。
  answer_index: 1
  explanation: RAGは外部ドキュメントを参照するため最新情報を反映でき、生成された回答の根拠をドキュメントから見つけられるため、信頼性が高いです。
- question: 検索器 (Retriever) の役割として正しいものは何ですか？
  choices:
  - 回答を生成する役割を担う。
  - 学習データを再学習させる役割を担う。
  - 質問に関連する外部ドキュメントの断片を検索する。
  - ユーザーインターフェースを管理する。
  answer_index: 2
  explanation: 検索器は、ユーザーの質問と意味的に類似していたり関連性が高いドキュメントを、外部データソースから見つけ出す役割を担います。
completion_criteria:
- RAGアーキテクチャの構成要素を説明できる。
- 実習したRAGパイプラインのコードが正常に動作し、関連ドキュメントの検索および拡張を確認できる。
- RAGパイプラインの限界点と改善方向を分析レポートに記述する。
source_ids:
- S1
- S2
---

## RAG (Retrieval-Augmented Generation) アーキテクチャの概要

最新の自然言語処理 (NLP) およびディープラーニングモデルは、膨大なテキストデータを学習して優れた性能を発揮しますが、モデルの学習時点に含まれていない最新情報や、特定のドメインの非公開データに対しては、ハルシネーション（幻覚）を引き起こしたり、情報を知らないといった限界があります [S1]。

### 検索を通じたLLMの限界克服
RAGは、モデルがすべての知識をパラメータ内部に記憶させるのではなく、質問に関連する外部の信頼できるドキュメントを「適切な時点 (just-in-time)」で検索し、生成段階の入力として提供する方式です [S2]。

### 主要構成要素
1. **検索器 (Retriever)**: ユーザーのクエリ (query) を受け取り、ベクトルデータベースなどで関連性の高いドキュメントの断片 (chunk) を特定します。
2. **拡張 (Augmentation)**: 検索されたドキュメントと元の質問を組み合わせて、LLMに渡すプロンプトを構成します。
3. **生成器 (Generator)**: 拡張された情報を基に、事実に基づいた回答を生成します。

このような構造は、モデルの知識を最新の状態に維持し、生成された回答の根拠を追跡可能にすることで、信頼性を確保するのに寄与します。
