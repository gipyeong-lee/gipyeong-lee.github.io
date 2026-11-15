---
layout: post
title: "AIが複雑な決定を一度に下す？Perplexity「Decider v1.3」の秘密"
description: "Perplexityが公開したオープンウェイト・マルチモーダル決定モデル「Decider v1.3」の性能、分類・抽出能力、そしてビジネスでの活用方法を分かりやすく解説します。"
summary: "Perplexityが分類、ルーティング、スコアリング、情報抽出を一度に行うオープンウェイト・マルチモーダル決定モデル「Decider v1.3」および「Decider Flash v1.3」を公開しました。"
tags: [Perplexity, Decider, AI Models, Multimodal, Open-weight]
image: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases.jpg
image_alt: "多様なデータや文書を一目で分析・分類するAI決定モデルの概念図を表現したイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Decider v1.3は、AIが単なる対話相手の枠を超え、企業の複雑な意思決定やデータ分類業務を直接実行する強力な実務パートナーへと進化していることを示しています。"
quiz:
  - question: "Perplexityが今回公開した決定モデルv1.3シリーズの特徴として正しいものはどれか？"
    choices: ["テキストのみ処理できる", "分類、スコアリング、情報抽出を一度に行う", "入力データを途中で必ず切り捨てる（Truncation）"]
    answer: 1
    explanation: "Decider v1.3は、テキスト、構造化JSON、画像を基に、分類、ルーティング、スコアリング、情報抽出をわずか1回のパスで処理できるマルチモーダル決定モデルです。"
  - question: "Decider v1.3が63個のクエリ分類タスクで記録した平均精度はどれか？"
    choices: ["81.2%", "91.6%", "99.4%"]
    answer: 1
    explanation: "より大規模なモデル基準で63個のクエリ分類タスクにおいて91.6%の平均精度を記録し、自社の本番用分類器を超える優れたパフォーマンスを証明しました。"
  - question: "新しく追加されたDecider v1.3の核心機能の一つで、テキストの中から特定の情報を直接ピンポイントで抽出する能力は何と呼ばれるか？"
    choices: ["ロケート（Locate）", "トランスレート（Translate）", "コンパイル（Compile）"]
    answer: 0
    explanation: "Decider v1.3は、新たに導入された「ロケート（Locate）」機能を通じて、テキストの中から特定の情報を直接抽出する能力を備えています。"
lang: ja
ref: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases
---

想像してみてください。数千件の顧客からの問い合わせや書類、画像が殺到する大規模なカスタマーセンターで、担当スタッフが毎回これが払い戻しリクエストなのか、単なる問い合わせなのか、緊急の苦情なのかを分類して採点し、疲弊しきっています。しかし、この複雑で退屈な判断作業をわずか数秒で、人間よりも正確にこなしてしまうAIが登場しました。[Perplexity（AIベースの検索および対話型プラットフォーム）](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)が公開したオープンウェイト（Open-weight、誰もが内部構造を確認して活用できる公開ウェイトモデル）マルチモーダル（Multimodal、テキストだけでなく画像や音声など多様な形態のデータを同時に理解する技術）決定モデル**「Decider v1.3」**と**「Decider Flash v1.3」**の話です [Source 2, Source 7]。

本記事では、Perplexityが発表したこの新しい意思決定AIがなぜ注目を集めているのか、私たちの日常やビジネスにどのような変化をもたらすのかを順を追って見ていきます。

---

## なぜこれが重要なのか？

企業がAIをビジネスに導入する際、最も頭を悩ませるポイントは「判断と決定」です。例えるなら、巨大な工場で数多くの部品の不良の有無を一つひとつ手作業で検品するために立ち止まっているようなものです。「このメールはスパムですか？」「この顧客が提出した書類は規定を満たしていますか？」「この商品のレビューはポジティブですか、ネガティブですか？」といった質問に答えるため、従来はそれぞれ異なるプログラムを複雑に組み合わせる必要がありました。

しかし、[PerplexityのDecider v1.3](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)は、63個のクエリ分類（Query-classification、ユーザーの質問やリクエストの意図をタイプ別に分ける作業）タスクにおいて**平均精度91.6%**を記録し、自社の従来の本番用分類器よりも6.54パーセントポイント高いパフォーマンスを証明しました [Source 2]。 

単に文章を読んで答えるだけでなく、**分類（Classification）、スコアリング（Scoring、採点）、情報抽出（Extraction）**をわずか1回のパスで処理できるため [Source 4, Source 6]、企業ははるかに低コストで迅速かつ正確な自動化システムを構築できるようになります。

---

## 分かりやすく解説：Decider v1.3はどのように働くのか？

簡単に言うと、Decider v1.3はまるで**「超高速の裁判官」**あるいは**「大型図書館の天才司書」**に例えられます。 

このモデルは、テキスト、構造化JSON（データを保存・交換するための軽量なテキストフォーマット）、さらには画像まで、多様な形式のデータを一度に受け入れます [Source 6]。そして、Yes/Noの質問、ユーザーが事前に設定したカスタム選択肢、順序のあるルーブリック（Rubric、評価基準表）に基づいて徹底的に審査した後、確率値とともにタイピングされた正解を出力します [Source 6]。

### 比喩で見る核心機能
- **X線セキュリティ検査場**：空港の検査場が荷物をスキャンするように、Decider v1.3は膨大なデータの中から規約違反や特定の項目を誤差なく選び出します。
- **新しい「ロケート（Locate）」機能**：テキストの中から特定の情報を直接ピンポイントで抽出する能力が追加されました [Source 1, Source 7]。まるで巨大な百科事典から特定の単語が書かれたページを正確にナイフで切り出すかのように探し出す技術です。

このすべてのプロセスが1つのモデル内で有機的に行われるという点が、従来のAIとの最大の違いです [Source 4, Source 6]。

---

## 現在の状況：どこまで進んでいるのか？

[Perplexity Decider v1.3](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)は、前バージョンのv1、v1.1、v1.2、そしてFlash v1.2の優れた系譜を受け継いで誕生した最新モデルです [Source 2]。現在判明している技術的特徴とスペックは以下の通りです。

1. **強力なマルチモーダル処理**：テキストだけでなく、画像や構造化データまで同時に評価できます [Source 6]。
2. **膨大なコンテキストウィンドウ**：**256K（約25万6千個）**という圧倒的なコンテキストウィンドウ（Context window、AIが一度に記憶して処理できる情報の量）を提供し、本1冊分のデータを丸ごと読み込ませて分析することができます [Source 6]。
3. **入力データのロスレス保存**：学習プロセスにおいて最大**30,720トークン（Token、AIが文章を読み込んで処理する基本単位）**長のシーケンスを使用し、入力データを途中で決して切り捨てない（Truncation）原則を堅持しています [Source 9]。
4. **柔軟な質問制限**：質問の数に固定された制限がなく、許可された長さの制限内で一度に大量の質問を投げかけることができます [Source 9]。

開発者や企業は、OpenRouterやVercel AI Gatewayなどを通じてこのモデルを簡単にテストし、API形式で利用することができます [Source 6, Source 8]。

---

## 今後どうなるのか？

[Perplexity](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)がオープンウェイトモデルとして[Decider v1.3およびDecider Flash v1.3](https://lapaasvoice.com/perplexity-open-sources-decider-v1.3-and-decider-flash-v1-3-with-new-locate-feature/)を全面開放したことに伴い [Source 2, Source 7]、今後は多数の企業や開発者がそれぞれのサービスにこの「インテリジェント判断エンジン」を移植していくものと見られます。

カスタマーセンターの自動分類システム、大規模な契約書や法律文書のレビュー、リアルタイムのコンテンツモデレーションなど、「正確な判断」がビジネスの勝敗を分ける領域において、Decider v1.3は中核的なインフラとして定着する見通しです。AIが単に上手に話す域を超え、真の「優秀な参謀」へと生まれ変わる時計の針が急速に動き始めています。

---

## AIの視点

MindTickleBytesのAI記者による視点：AIの発展は単に文章を上手に書くことの枠を超え、「正しい判断を下す」という精密さへと進化しています。Decider v1.3は、AIが単なるお喋りではなく、ビジネスの最も厳しい意思決定者の傍らで働く信頼できる参謀になり得ることを証明しています。

---

## 参考資料

1. [Perplexity Decider v1.3: Training, eval, and use cases](https://www.perplexity.ai/hub/blog/perplexity-decider)
2. [Perplexity Ships Decider v1.3 Classifier, 91.6% on 63 Tasks](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)
3. [Perplexity's Decider v1.3 lets one model · 21 HN comments | Zeli](https://zeli.app/story/50488464)
4. [Decider v1.3: Release, Decision Index Score, Performance ...](https://artificialanalysis.ai/decision-models/pplx-decider-v1-3)
5. [Decider V1.3 API, Pricing & Playground | Vercel AI Gateway](https://vercel.com/ai-gateway/models/pplx-decider-v1.3)
6. [Perplexity Open-Sources Decider v1.3 and Decider Flash v1.3 ...](https://lapaasvoice.com/perplexity-open-sources-decider-v1.3-and-decider-flash-v1-3-with-new-locate-feature/)
7. [DeciderV1.3(free) - API Pricing & Providers | OpenRouter](https://openrouter.ai/perplexity/pplx-decider-v1.3:free)
8. [perplexity-ai/pplx-decider-v1.3 · Hugging Face](https://huggingface.co/perplexity-ai/pplx-decider-v1.3)
9. [Perplexity Decider v1.2 27B Benchmarks & Pricing | BenchLM.ai](https://benchlm.ai/models/pplx-decider-v1.2)
10. [How To Use Decision Models for Evals – Hamel’s Blog](https://hamel.dev/blog/posts/decision-model-evals/)
11. [Perplexity Decider V1.2 API Pricing & Benchmarks | LMSpeed](https://lmspeed.net/model/pplx-decider-v1.2)