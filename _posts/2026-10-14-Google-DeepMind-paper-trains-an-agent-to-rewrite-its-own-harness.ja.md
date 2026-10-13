---
layout: post
title: "AIが自らその『知能の殻』を修正？自己進化するAIエージェントの時代"
description: "AIエージェントが人間の助けを借りずに、自らの動作方式である「ハーネス（harness）」を改善・進化させる最新技術研究について、分かりやすく解説します。"
summary: "Google DeepMindの最新研究は、AIエージェントが複雑な手動エンジニアリングなしで自らの動作環境（ハーネス）を修正・最適化し、自律的なソフトウェア開発への道を切り開いていることを示しています。"
tags: [AI, GoogleDeepMind, エージェント, AutoHarness, Evo2]
image: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness.jpg
image_alt: "AIエージェントが自らコードを記述し、自身の動作体系を修正する未来的な姿を描いたイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人間が一つ一つルールを決めていた時代は終わりを告げようとしています。AIが自身の限界を自ら認識し、修正していく能力こそが、真の自律的エージェントへと向かう最も重要な鍵となるでしょう。"
quiz:
  - question: "AIエージェントの「ハーネス（harness）」とは何ですか？"
    choices: ["AIの記憶装置", "モデルと作業の間を接続する『接着剤』の役割を果たすソフトウェア体系", "AIの学習データセット"]
    answer: 1
    explanation: "ハーネスは、AIモデルと解決すべきタスクの間で配管（plumbing）や接着剤（glue）の役割を果たし、AIが円滑に動作するように支援するソフトウェアの足場（scaffolding）です。"
  - question: "Google DeepMindのAutoHarness研究はどのような仕組みで動作しますか？"
    choices: ["人間が毎日新しいコードを直接入力します。", "Geminiが環境から受け取ったフィードバックを活用し、反復的な精製過程を経て自らコードを生成します。", "既存のルールをそのまま維持します。"]
    answer: 1
    explanation: "AutoHarnessは、Gemini-2.5-Flashが環境から得たフィードバックをもとに、反復的な改善過程を経て自ら最適なコードハーネスを作り出す方式です。"
  - question: "Evo2フレームワークの核心目標は何ですか？"
    choices: ["人間の介入を最大化する。", "AIの基本言語モデルを完全に入れ替える。", "タスク実行者（task executor）を変えずに、エージェントのワークフローとポリシーを改善する。"]
    answer: 2
    explanation: "Evo2はタスク実行者自体には触れず、エージェントのハーネス修正記録や評価データを学習データとして活用し、ワークフローとポリシーをより良い方向へ改善するフレームワークです。"
lang: ja
ref: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness
---

想像してみてください。あなたが新しい助手を採用しました。ところがこの助手は、仕事を与えるたびに「こうしたほうがもっと効率的ですよ」と言いながら、自ら仕事のやり方（マニュアル）をアップグレードし続けます。指示しなくても、自分専用の道具や記憶体系を自ら再整備するのです。これはSF映画の話ではありません。Google DeepMindが発表した最新の研究が示す、「自ら進化するAIエージェント」の姿です。

### なぜこの技術が重要なのか？

これまでAIエージェントを作る過程は、非常に苦痛でコストのかかる「手作業」の連続でした。エージェントが何らかのタスクを行うには、人間エンジニアがそのタスクのための具体的なルールや制約事項を一つ一つ定義しなければならなかったからです。この接続部分を作る過程を業界では「ハーネス（harness）」と呼びますが、実はこの過程こそがAIエージェント導入の最大の障壁となっていました。[出典: This AutoHarness paper(from Google DeepMind) is the most...](https://www.linkedin.com/posts/omarsar_this-autoharness-paper-from-google-deepmind-activity-7437877601853153280-uWyl)

しかし、今は違います。AIが自らその動作体系を修正・最適化できるようになれば、人間の介入なしでもAIエージェントが多様で複雑なタスクを自律的に遂行する世界が、急速に近づいてくるでしょう。これはAI技術が研究室レベルを超えて実務現場へ「拡張可能な（scalable）」形で配置される、重要な転換点となるはずです。

### 分かりやすく解説：AIの「接着剤」、ハーネス

技術的な話をもう少し簡単に紐解いてみましょう。AIエージェントは通常、「頭脳」の役割を果たす大規模言語モデル（LLM）と、この頭脳が外部世界と疎通できるよう手助けする「ハーネス」という枠組みで構成されます。[出典: AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329)

このように例えると簡単です。AIエージェントを「天才画家」としましょう。画家が絵を描くには筆も必要ですし（ツール）、キャンバスも準備しなければなりません（環境）。また、どんな絵を描くのかという指示（プロンプト）も明確である必要があります。ここで画家の道具箱と絵を描く過程を助ける作業台全体を「ハーネス」だと考えてください。従来は人間が一つ一つ筆を用意し、作業台の高さを調節してあげなければなりませんでしたが、これからは画家（AI）が自ら「今回の絵にはこの筆が必要だな」と言って、道具箱の構造そのものを変えてしまうのです。

Google DeepMindの**AutoHarness**は、Gemini-2.5-Flashモデルが環境から得たフィードバックを利用し、自らより良い「作業台」を設計するように導きます。[出典: AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329), [出典: AutoHarness | DAIR.AI Academy](https://academy.dair.ai/papers/autoharness)

また、**Evo2**というフレームワークは、エージェントがハーネスを修正する過程で得たデータを学習データとして再利用します。つまり、修正して実験した経験をデータとして蓄積し、自身のワークフロー（業務の流れ）を自ら強化するのです。[出典: Google DeepMind paper trains an agent to rewrite its own harness](https://runtimewire.com/article/google-deepmind-evo2-agent-harness-co-evolution)

### どこまで進んでいるのか？

現在AI研究分野では、自ら構造を改善するいくつかの興味深い方式が議論されています。

第一に、**AutoHarness**はエージェントがコードを直接記述し、自らハーネスを作り出します。人間が複雑なルールを手動で組むよりも、少量の反復的な精製過程を経た自動化されたハーネスのほうが効率的な性能を示すこともあります。[出典: [2603.03329] AutoHarness](https://arxiv.org/abs/2603.03329)

第二に、**Self-Harness**は、エージェントが外部の強力な支援や人間の助けなしに、独立して自身の動作環境を改善する新しいパラダイムです。[出典: [2606.09498] Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)

第三に、**RRSI（再帰的自己改善）**技術は、Google Cloud AI研究チームなどが発表したもので、プロンプト、ツール、記憶体系、制御フロー、さらには下位エージェント（sub-agents）まで、AIが直接書き直すようにします。[出典: Paper AutoHarness from DeepMind Changes AI Agents 1](https://www.youtube.com/watch?v=4Xczb2z3N_w)

現場の専門家たちは「モデル自体の性能差よりも、どのハーネスを使うかによる性能の格差のほうが大きい」と口を揃えます。どれほど賢いモデルでも、ツールを活用する方式が劣っていれば実力を発揮できないからです。[出典: Auto-Harness Synthesis - Just Understanding Data](https://understandingdata.com/posts/auto-harness-synthesis/)

### 未来の姿

これからのAIエージェントは静的な存在ではありません。今日出会ったAIと1,000日後のAIでは、その構造や記憶、ツールが全く異なっている可能性があります。[出典: The Harness That Learns You | XO Docs](https://docs.xo.builders/research/perspectives/the-harness-that-learns-you)

私たちは今、「AIに何をさせるか」を悩む段階を越えて、「AIが自らどのツールと方式を選択して問題を解決していくか」を見守る段階へと進んでいます。人間の介入が最小化された、真の意味での自律エージェントが私たちの日常をどのように変えていくのか、一緒に見守っていきましょう。

## 参考資料

1. [Google DeepMind - Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
2. [This AutoHarness paper(from Google DeepMind) is the most...](https://www.linkedin.com/posts/omarsar_this-autoharness-paper-from-google-deepmind-activity-7437877601853153280-uWyl)
3. [Google DeepMind](https://deepmind.google/)
4. [AI has grown beyond human knowledge, says Google's DeepMind unit](https://www.zdnet.com/article/ai-has-grown-beyond-human-knowledge-says-googles-deepmind-unit/)
5. [The Harness That Learns You | XO Docs](https://docs.xo.builders/research/perspectives/the-harness-that-learns-you)
6. [Google DeepMind paper trains an agent to rewrite its own harness](https://runtimewire.com/article/google-deepmind-evo2-agent-harness-co-evolution)
7. [AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329)
8. [[2603.03329] AutoHarness: improving LLM agents by ...](https://arxiv.org/abs/2603.03329)
9. [AutoHarness: LLM Agents That Build Own Scaffolding | aiHola](https://aihola.com/article/autoharness-llm-agent-code-harness)
10. [Auto-Harness Synthesis - Just Understanding Data](https://understandingdata.com/posts/auto-harness-synthesis/)
11. [AutoHarness | DAIR.AI Academy](https://academy.dair.ai/papers/autoharness)
12. [[2606.09498] Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)
13. [Paper AutoHarness from DeepMind Changes AI Agents 1](https://www.youtube.com/watch?v=4Xczb2z3N_w)