---
layout: learn-module
title: 検索品質指標（Recall @k, MRR, nDCG）
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-ja
course_locale: ja
lang: ja
ref: learn:rag-evaluation-reliability:retrieval-metrics
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/retrieval-metrics/
- lang: en
  url: /learn/en/rag-evaluation-reliability/retrieval-metrics/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/retrieval-metrics/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/retrieval-metrics/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/retrieval-metrics/
module_id: m4
permalink: /learn/ja/rag-evaluation-reliability/retrieval-metrics/
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
id: m4
slug: retrieval-metrics
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- 検索拡張生成(RAG)パイプラインにおいて検索段階の重要性を理解する。
- Recall @k, MRR, nDCG指標の概念と、RAGシステム評価における意味を学習する。
- 検索されたコンテキストの関連性が、その後の回答生成品質に与える影響を分析する。
worked_examples:
- '質問に対してシステムが[DocB, DocA, DocC]の順で返却し、正解関連文書がDocAである場合？ MRR計算: DocAは 2番目なのでReciprocal
  Rankは 1/2 = 0.5である。'
- k=3のとき、上位 3個の検索結果に正解文書が含まれていればRecall @3 = 1、含まれていなければRecall @3 = 0である。
lab:
  title: 検索品質指標の定量測定実習
  steps:
  - 評価セット(質問、正解文書)を使用して 50個のサンプルデータを用意する。
  - 検索モジュールを実行して、各質問に対する上位k(k=3, 5, 10)個の文書を返却してもらう。
  - Recall @k, MRR, nDCG関数をPythonで直接実装するか、ライブラリを使用して計算する。
  - 質問別指標結果をデータフレームに整理して可視化する。
  safety:
  - 個人情報や非公開文書が含まれたデータセットを外部APIに伝送しない。
  - 実験時にAPIコスト制限を設定し、キャッシュを活用してリクエスト数を最適化する。
  deliverables:
  - 各質問別のRecall @k, MRR, nDCG値が含まれた結果データフレームのCSV
  - 指標分布を示すヒストグラムおよびボックスプロット画像
assignment:
  title: 検索機(Retriever)性能比較レポート
  deliverables:
  - 二つの検索設定（例：Sparse vs Dense Retrieval）を適用した評価結果レポート
  - 性能が低い上位 5個の質問に対する原因分析(誤検索タイプ分類)
  rubric:
  - Recall @k, MRR, nDCG指標を正確に計算したか？
  - 検索性能差を統計的に有意に解釈したか？
  - 失敗タイプを体系的に分類したか？
quiz:
- question: RAGシステムにおいて検索段階の品質が生成段階に与える影響は何ですか？
  choices:
  - 検索品質は生成品質と無関係である。
  - 関連性の低いコンテキストはLLMの幻覚を誘発するリスクを高める。
  - 検索段階はLLMの推論能力のみを評価する。
  - 検索結果が多いほど常に生成品質が良くなる。
  answer_index: 1
  explanation: 検索段階で関連性のない情報が伝達されると、LLMはこれに基づいて誤った回答を生成したり、幻覚を起こしたりすることがあります [S3]。
- question: MRR指標が最も高いときはいつですか？
  choices:
  - 関連文書が常に最後に出るとき
  - 関連文書が常に最も上端(1位)に位置するとき
  - 検索結果が全くないとき
  - 関連文書が常に中間に出るとき
  answer_index: 1
  explanation: MRRは正解文書の順位逆数の平均なので、1位に位置するとき値が最大(1)になります。
completion_criteria:
- Recall @k, MRR, nDCG計算コードを完成させ、サンプルデータに適用した。
- 二つの検索戦略を比較し、定量的な分析結果を導き出した。
- 検索失敗タイプを少なくとも 3種類以上分類してレポートに記載した。
source_ids:
- S3
- S4
---

### RAG検索品質評価の重要性

RAGシステムは、外部データベースから関連情報を検索し、それをLLMに伝えて回答を生成する [S3]。そのため、検索段階で関連性が高く集中したコンテキストを特定できなければ、いかに強力なLLMであっても正確な回答を生成することは困難である [S3]。検索品質を評価することは、RAGアーキテクチャの全体的な性能を改善するための第一歩である。

### 主要検索評価指標

1. **Recall @k（再現率）**: 検索された上位k個の結果に、実際の正解が含まれているかを測定する。つまり、必要な情報が検索システムによって捕捉されたかを確認する指標である。
2. **MRR（平均逆順位）**: ユーザーの質問に対する正解（関連文書）が、検索結果リストの何番目に位置しているかを測定する。最も最初の位置に関連文書が登場するほどMRR値は1に近づき、高いスコアとなる。
3. **nDCG（正規化割引累積利得）**: 検索結果の順序を考慮する指標であり、関連性の高い文書が上部に位置するほど高いスコアを付与する。単純な包含有無（Recall）よりも、検索結果の「順位精度」をより精密に評価する。

これらの指標は、参照データ（Ground Truth）がある場合、システム改善のために必須であり、Ragasのようなフレームワークは、これらの側面を定量的に分析できるツールを提供する [S3, S4]。
