---
layout: learn-module
title: 質問-正解評価セットの構築
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-ja
course_locale: ja
lang: ja
ref: learn:rag-evaluation-reliability:eval-set-generation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/eval-set-generation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/eval-set-generation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/eval-set-generation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/eval-set-generation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/eval-set-generation/
module_id: m3
permalink: /learn/ja/rag-evaluation-reliability/eval-set-generation/
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
id: m3
slug: eval-set-generation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- RAGシステム評価のための高品質な質問-正解 (QA) 評価セットの必要性を理解する。
- 合成データ生成手法 (Synthetic Data Generation) を活用して評価セットを構築する原理を把握する。
- TrueTeacherのような手法を通じ、モデルが生成した回答の事実的一貫性を評価する論理を習得する。
- 評価セットの品質を維持しながら、ドメインの変化に堅牢なデータセットを生成するプロセスを設計する。
worked_examples:
- '例 1: 文書コーパスから核心的な節を抽出する。与えられた文書からLLMを使用して文脈上重要な事実文を抽出し、これに基づいて「回答可能な質問」と「誤った質問(Negative
  Sample)」を生成するパイプラインを構成する。'
- '例 2: 事実性検証プロンプトの設計。生成された質問と検索された文書をもとに、LLMに対して「検索された文書に基づいて質問に回答し、回答が事実的に一貫しているかTrue/Falseで判断せよ」と指示し、評価用正解地(Ground
  Truth)を精緻化する過程。'
lab:
  title: 合成評価セット生成実習
  steps:
  - 準備されたオープンライセンス文書コーパスをロードし、テキストチャンク単位に分割する。
  - LLM APIを使用して、各チャンクから抽出可能な固有の質問-回答ペアを 100件以上生成する。
  - 生成された質問に対して検索システムをシミュレーションし、上位k個の文書を検索する。
  - 検索された文書と生成された回答間の事実的一貫性を判断する評価パイプラインを構築する。
  - 結果データをJSONL形式で保存し、サンプル 30件を手動で検討してデータ品質を記録する。
  safety:
  - 評価セット構築過程で外部APIを使用する場合、コスト上限(API Key Limit)を必ず設定する。
  - 生成されたデータセット内に原本文書の機密情報や個人情報が含まれていないか、正規表現でフィルタリングする。
  - モデル評価結果のみを盲信せず、標本に対する手動照合を必ず併行する。
  deliverables:
  - 構築された 100問以上の質問-回答評価セット(JSONLファイル)
  - データセット生成および検証コードが含まれたJupyter Notebook
  - 人間による検討記録が含まれた品質分析レポート
assignment:
  title: RAG信頼性評価セット回帰レポート
  deliverables:
  - 生成された評価セットの統計的分布(質問長、回答長、文書参照頻度など)を分析したダッシュボード
  - 二つ以上のRAG設定（例：検索アルゴリズムの変更、モデルの変更）を同一の評価セットで比較した成果物
  - エラー分類表(Hallucination、Contextual Irrelevanceなど)の作成および事例分析
  rubric:
  - 評価セットが文書コーパス全体のの内容を均等に反映しているか？
  - 合成データ生成パイプラインが再現可能な形式で作成されているか？
  - エラータイプの分類が具体的で定量的な根拠を備えているか？
  - 人間による検討を通じて、自動評価指標の妥当性を立証したか？
quiz:
- question: TrueTeacher方法論が従来の合成データ生成方式と差別化される点は何ですか？
  choices:
  - 人間が作成した要約に全面的に依存する。
  - モデルが生成した多様な要約を注釈処理して合成データを生成する。
  - 小型モデルのみを学習用の教師として使用する。
  - データセットを手動でのみ作成して精度を高める。
  answer_index: 1
  explanation: TrueTeacherは人間が作成した要約に依存せず、LLMを使用してモデルが生成した多様な要約を注釈処理することで合成データを生成します
    [S5]。
- question: RAG評価セット構築時、モデルの自動評価のみで事実性を確定しない理由は何ですか？
  choices:
  - モデル自動評価が人間より非常に遅いためです。
  - モデル自動評価が完璧ではなく、幻覚(Hallucination)を完全に排除できないためです。
  - 人間評価にはコストがかからないためです。
  - 事実性評価にはモデルが不要であるためです。
  answer_index: 1
  explanation: 自動化された評価ツールは効率的ですが完璧ではないため、事実性検証のために必ず標本の手動検討と出典照合を併行する必要があります。
completion_criteria:
- 100問以上の質問-回答評価セットデータセット構築完了
- データセット品質分析および人間による検討記録の提出
- RAGパイプラインの性能評価のためのノートブック実装および結果レポート作成
- CI/CD環境で再実行可能な形式の評価パッケージ構成
source_ids:
- S5
---

## RAG評価のための質問-回答(QA)評価セットの構築

RAG(Retrieval-Augmented Generation)システムの性能を信頼性を持って測定するためには、精巧に設計された評価セットが不可欠です。単純に人間が作成した質問と回答にのみ依存する方式は、大規模評価を行う際にコストと拡張性の面で限界があります。

### 合成データ生成の重要性
最新の研究であるTrueTeacher方法論によると、LLMを活用してモデルが生成した多様な回答を注釈処理することで、合成訓練データを生成できます [S5]。この方式には以下のような利点があります:
1. **コスト効率**: 人間が直接作成した要約や回答に依存しないため、大規模データセット(例: 1.4M例)の生成が可能です [S5]。
2. **多言語および拡張性**: 特定の言語に限定されず、ドメイン転換(Domain-shift)に対しても頑健性を示します [S5]。
3. **事実的一貫性評価**: 合成データを通じて学習された小型モデルは、大型LLM教師モデルの知識を成功裏に蒸留(Distillation)し、効率的な事実性評価ツールとして活用できます [S5]。

### データセット構成戦略
評価セットを構築する際は、単に質問-回答のペアを作ることを超えて、「検索結果が回答を導き出すために必要な根拠を含んでいるか？」と「モデルが該当する根拠を歪曲なく参照しているか？」を測定できるように構成しなければなりません。このために、データセット生成時に質問の複雑度、検索結果との関連性、回答の事実的一貫性を体系的にラベリング、または検証する必要があります。
