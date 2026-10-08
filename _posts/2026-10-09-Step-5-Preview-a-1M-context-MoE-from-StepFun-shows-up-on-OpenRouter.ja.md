---
layout: post
title: "AIが数千冊の本を一度に読む？100万トークンの壁を突破した「Step5Preview」登場"
description: "記憶力の限界を突破した新しいAIモデル「Step5Preview」の特徴と、100万トークンのコンテキストウィンドウが持つ意味を分かりやすく解説します。"
summary: "StepFunが公開した6,000億パラメータ規模のMoEモデル「Step5Preview」は、100万トークンの膨大なコンテキストを処理し、エージェントタスクに特化した能力を発揮します。"
tags: [AI, StepFun, Step5Preview, 大規模言語モデル, 技術トレンド]
image: 2026-10-09-Step-5-Preview-a-1M-context-MoE-from-StepFun-shows-up-on-OpenRouter.jpg
image_alt: "膨大なデータの海を処理するAIの姿を可視化したグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "膨大なデータを一度に記憶する能力は、AIが単なるチャットボットを超え、実質的な業務アシスタントへと進化するための鍵となるでしょう。"
quiz:
  - question: "Step5Previewが持つ最大の特徴の一つは何ですか？"
    choices: ["100万トークンのコンテキストウィンドウ", "テキストのみ処理可能", "無料で公開されたモデル"]
    answer: 0
    explanation: "Step5Previewは、100万トークンに達する膨大な情報を一度に入力して処理できるモデルです。"
  - question: "MoE（Mixture-of-Experts）アーキテクチャとは何ですか？"
    choices: ["すべてのパラメータを常に使用する構造", "必要な専門家パラメータのみを活性化する構造", "人間の脳構造とは全く関係のない技術"]
    answer: 1
    explanation: "MoEは、全パラメータのうち特定の状況で必要な専門家パラメータのみを選択的に使用することで効率を高める技術です。"
  - question: "Step5Previewのオープンウェイト（Open Weights）公開予定日はいつですか？"
    choices: ["すでに公開済み", "2026年10月15日", "2026年12月31日"]
    answer: 1
    explanation: "StepFunは、該当モデルの重みを2026年10月15日に公開する予定です。"
lang: ja
ref: 2026-10-09-Step-5-Preview-a-1M-context-MoE-from-StepFun-shows-up-on-OpenRouter
---

想像してみてください。あなたの机の上に1,000ページを超える厚い会計報告書が50冊積み上がっています。あなたがAIアシスタントに「過去5年間の我が社の財務の流れから、異常の兆候をすべて見つけて要約して」と尋ねたらどうなるでしょうか？以前のAIであれば、これらの文書を一つ一つ分割して入力しなければならず、その過程で記憶を失ってしまうことも日常茶飯事でした。しかし、最近OpenRouterに登場した「Step5Preview」は、こうした不可能を打ち破る新たな挑戦者です。

### なぜこの技術が重要なのか？

日常的にAIを使っていると、もどかしい瞬間にしばしば遭遇します。たった今言ったことをすぐに忘れてしまったり、長い文書を渡しても正確に分析できなかったりするケースです。専門家はこれをAIの「記憶力」、つまり「コンテキストウィンドウ（AIが一度に処理できるデータの量）」の限界と呼びます。

Step5Previewは、100万トークンという圧倒的な記憶力を備えました（[参考資料 1](https://openrouter.ai/stepfun/step-5-preview)）。これは単に文字数を増やしたことにとどまりません。膨大な量の情報を一度に記憶することで、複雑なプログラミングコードを全体的に理解したり、数百ページの金融文書を貫く洞察を得たりするなど、「本当に仕事をするAI（Agentic AI）」としての能力が飛躍的に向上したことを意味します（[参考資料 3](https://platform.stepfun.ai/docs/en/guides/models/step-5-preview), [参考資料 9](https://www.stepfun.com/step-5-preview)）。

### 言い換えれば：「専門家委員会」方式

Step5Previewは、「混合専門家モデル（MoE、Mixture-of-Experts）」という賢い手法を採用しています（[参考資料 1](https://openrouter.ai/stepfun/step-5-preview)）。

簡単に例えると、学校にすべての科目を完璧にこなさなければならない天才生徒が一人いるのではなく、数学の専門家、英語の専門家、科学の専門家など、数多くの先生が待機していると考えてみてください。質問が来ると、すべての先生が駆けつけるのではなく、数学の質問には数学の先生だけが活性化して回答します。

Step5Previewは合計6,000億という膨大なパラメータ（AIの知識単位）を持っていますが、一度の質問で使用されるのは、そのうちの270億パラメータだけを選択的に使用します（[参考資料 5](https://therouter.ai/blog/step-5-preview-stepfun-api-integration-routing-guide/), [参考資料 9](https://www.stepfun.com/step-5-preview)）。おかげで、モデル全体の膨大な知識を維持しながらも、速度と効率という二兎を同時に追いかけることができるのです（[参考資料 11](https://braindetox.kr/en/posts/stepfun_step5_preview_agent_model_2026.html)）。

### 今、私たちのそばに来たAI

現在、Step5PreviewはAPIを通じてすぐ利用可能であり、テキストだけでなくビデオを含む映像データまで分析する能力を備えています（[参考資料 5](https://therouter.ai/blog/step-5-integration-routing-guide/), [参考資料 9](https://www.stepfun.com/step-5-preview)）。

業界の評価も非常に肯定的です。特定の指標において約44点程度の知能指数を記録し、現在市場に出ているオープンウェイト（モデルの内部情報が公開されたモデル）の中でも最上位圏の性能を示すというのが一般的な分析です（[参考資料 14](https://pandaily.com/stepfun-step-5-preview-600b-moe-1m-context.data)）。特にソフトウェアエンジニアリングや金融分野のように、精巧で専門的な作業において際立った強みを見せています（[参考資料 3](https://platform.stepfun.ai/docs/en/guides/models/step-5-preview)）。現在の利用コストは、100万出力トークンあたり約2.7ドル水準に設定されています（[参考資料 15](https://www.deai.org/news/stepfun-step-5-preview-api-open-weights-oct-15)）。

### 何を期待できるのか？

多くの開発者が注目する最大のイベントは、来る10月15日です。開発元のStepFunは、このモデルの重み（weights）を一般に完全に公開すると約束しました（[参考資料 6](https://aichoiceengine.com/ai-models/nemotron-3-ultra-vs-step-5-preview), [参考資料 9](https://www.stepfun.com/step-5-preview)）。これは誰でも自分のサーバーでこの強力なモデルを直接実行できることを意味します。記憶力が飛躍的に向上したAIモデルが一般化されたとき、私たちの日常的なオフィス環境がどのように変わるのかを見守ることは、非常に興味深い観戦ポイントです。

---

### MindTickleBytesのAI記者の視点
膨大なデータを一度に記憶する能力は、AIが単なるチャットボットを超え、実質的な業務アシスタントへと進化するための鍵となるでしょう。技術の発展速度には恐ろしさすら感じますが、結局私たちにとって重要なのは、この拡張された記憶力をどのように価値ある仕事に活用するかということでしょう。

## 参考資料
1. [Step5Preview- API Pricing & Providers | OpenRouter](https://openrouter.ai/stepfun/step-5-preview)
2. [StepFun: Step5Preview· Models · Pi | A terminal-based coding agent](https://pi.dev/models/openrouter/stepfun-step-5-preview)
3. [Step5Preview- StepFun Documentation](https://platform.stepfun.ai/docs/en/guides/models/step-5-preview)
4. [Step5Preview API Integration Guide: StepFun's 600B Agentic...](https://therouter.ai/blog/step-5-preview-stepfun-api-integration-routing-guide/)
5. [NVIDIA Nemotron 3 Ultra vs Step5Preview | AI Choice Engine](https://aichoiceengine.com/ai-models/nemotron-3-ultra-vs-step-5-preview)
6. [Step 5 Preview: Advancing the Pareto Frontier - stepfun.com](https://www.stepfun.com/step-5-preview)
7. [StepFun shares Step 5 Preview benchmarks, demos… · AGI Hunt](https://agihunt.info/en/p/1a11ba551ea1346a45979d41047)
8. [StepFun Step 5 Preview Technical Analysis — 600B MoE ...](https://braindetox.kr/en/posts/stepfun_step5_preview_agent_model_2026.html)
9. [pandaily.com/stepfun-step-5-preview-600b-moe-1m-context.data](https://pandaily.com/stepfun-step-5-preview-600b-moe-1m-context.data)
10. [StepFun's Step5Preview API ships; open weights promised October...](https://www.deai.org/news/stepfun-step-5-preview-api-open-weights-oct-15)