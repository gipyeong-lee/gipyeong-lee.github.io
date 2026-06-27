---
layout: post
title: "AIが自ら『試験問題』を作る？コーディングエージェントの新たな進化「Ornith-1.0」"
description: "Deep Reinforceが公開したオープンソースコーディングAI「Ornith-1.0」は、コーディング環境を自ら構築し問題を解決します。一般の方にも分かりやすく解説します。"
summary: "Ornith-1.0は、必要なテスト環境（スキャフォールド）を自ら設計し学習する能力を備えた最新のオープンソースコーディングAIモデルです。"
tags: [AI, コーディング, オープンソース, 技術トレンド]
image: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding.jpg
image_alt: "Ornith-1.0のロゴと共に、複雑なコーディングロジックが自ら再構成されるデジタルグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人間が作った枠組みに縛られず、AI自らが試行錯誤の基準を作る能動的な学習方式は、コーディングエージェントのレベルを一段階引き上げるでしょう。"
quiz:
  - question: "Ornith-1.0モデルが従来のコーディングAIと差別化される最大のポイントは何ですか？"
    choices: ["インターネット検索速度の向上", "問題解決のためのテスト環境（スキャフォールド）を自ら構築する", "画像生成機能の追加"]
    answer: 1
    explanation: "Ornith-1.0は強化学習を通じてコーディング問題を解決するだけでなく、その問題を検証するための環境（スキャフォールド）まで自ら設計します。"
  - question: "Ornith-1.0モデルはどのライセンスで公開されましたか？"
    choices: ["非公開の独自ライセンス", "GPLライセンス", "MITライセンス"]
    answer: 2
    explanation: "Ornith-1.0はMITライセンスで公開されており、研究用だけでなく商用目的でも自由に活用できます。"
  - question: "Ornith-1.0モデルの学習基盤となった従来のモデルは何ですか？"
    choices: ["Gemma 4とQwen 3.5", "GPT-4o", "Llama 3"]
    answer: 0
    explanation: "Ornith-1.0は既存の強力なモデルであるGemma 4とQwen 3.5をベースに、追加学習（ポストトレーニング）されました。"
lang: ja
ref: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding
---

想像してみてください。あなたが有能な開発者に複雑なソフトウェアのバグ修正を依頼したとします。ところが、その開発者は単にコードを直すだけでなく、そのバグが本当に直ったのかを確認するために必要なテストツールや環境まで、すべて自ら一瞬で作ってしまうとしたらどうでしょうか？ まるで魔法のようです。

最近、AI研究所のDeep Reinforceが公開した新しいAIモデルファミリー「**Ornith-1.0**」が、まさにこのような驚くべき能力を見せています。これまでもコーディングを行うAIは多く存在しましたが、Ornith-1.0は熟練エンジニアのように、問題を解決するための「舞台」を自ら設計するという点で、次元の異なる進化を遂げています。

## なぜこれが重要なのか？

これまで、ほとんどのコーディングAIは人間が決めたルールの中で答えを探すことにとどまっていました。しかし、現実世界のコーディングには「正解」が一つだけとは限りません。何が問題なのかを把握し、それを検証するテスト環境を構築し、修正後に再度確認するという複雑なプロセスが不可欠です。[出典: Ornith1.0: SelfLearningLLM forCoding| by Mehul Gupta | Medium](https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc)

Ornith-1.0のような「エージェント型コーディングモデル」は、AIが単に次の単語を予測するレベルを超え、ソフトウェアエンジニアリングの全工程を自律的に遂行できるようにします。さらに、これらのモデルはオープンソースとして公開されたため、世界中の開発者が企業規模に関係なく、最先端技術を自身のサービスに導入できるようになりました。[出典: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

## 分かりやすい例え：「自分でキッチンを作る料理人」

Ornith-1.0の核心は「**自ら作るテスト環境（セルフ・スキャフォールディング）**」にあります。

簡単に例えてみましょう。私たちが料理人を採用すると仮定します。従来のAIがレシピだけを見て料理するロボットだったなら、Ornith-1.0は料理をする前にキッチン設備から確認します。もしガスコンロが足りなければ自分でバーナーを設置し、材料の鮮度をチェックする道具がなければその道具まで自分で作ってから料理を始めるようなものです。

ここで「スキャフォールド（Scaffold、足場）」とは、コードが正しく動作するかを検証するためのテスト設計図のようなものです。従来のモデルは人間があらかじめ作っておいたテスト環境に依存していましたが、Ornith-1.0は**強化学習（Reinforcement Learning、正解を導くと報酬を得る方式で、試行錯誤を繰り返しながら学習する手法）**を通じて、問題の解決策とそれを検証する舞台を同時に最適化します。[出典: Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854) [出典: Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)

## 現在の到達点

Deep Reinforceは、ユーザーの環境に合わせて選択できるよう多様なモデルを公開しました。軽快で高速な9B（90億パラメータ）モデルから、巨大な規模を誇る397B（3,970億パラメータ）の「専門家混合（MoE、複数の小さなモデルを効率的に組み合わせた方式）」モデルまで、選択の幅が広がっています。[出典: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

性能も目を見張るものがあります。実際のコーディング問題の解決能力を測定する有名な試験台「SWE-Bench Verified」で82.4点という高得点を記録しました。これは既存のオープンソースモデルの中で、間違いなく最高水準です。[出典: Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854) [出典: Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)

## 未来の風景

Ornith-1.0の登場は、オープンソースAIエコシステムに大きな波紋を広げることが予想されます。巨大IT企業の独占的なモデルに依存していた時代が過ぎ去り、誰もが強力なコーディングツールを直接構築し、改善できる時代が開かれたのです。[出典: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

今後はAIが単にコードを書いてくれるだけでなく、ソフトウェア開発プロジェクト全体を指揮する「自律型エンジニア」へと発展していくでしょう。開発者はより創造的で設計的な思考に集中し、反復的で退屈な検証作業をAIエージェントが代わりに行う未来。その第一歩がOrnith-1.0と共に始まりました。[出典: DeepReinforce Releases Ornith-1.0 for Self-Scaffolding Coding Agents, TechGig](https://techgig.com/news/software-devops/deepreinforce-releases-ornith-1-0-for-self-scaffolding-coding-agents/132008000)

## 参考資料

1. [Ornith1.0—Open-SourceAgenticCodingModels](https://www.ornith.site/)
2. [Ornith1.0: SelfLearningLLM forCoding| by Mehul Gupta | Medium](https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc)
3. [IntroducingOrnith1.0-AgenticCodingLLMs - YouTube](https://www.youtube.com/watch?v=uD4-uy0GmHE)
4. [Ornith-1.0-adeepreinforce-ai Collection](https://huggingface.co/collections/deepreinforce-ai/ornith-10)
5. [IntroducingOrnith1.0-open-source- Art of Smart](https://www.artofsm.art/t/introducing-ornith-1-0/20592)
6. [DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)
7. [DeepReinforce releasesopen-sourceOrnith-1.0codingmodels...](https://digg.com/tech/f2u02pzq)
8. [deepreinforce-ai/Ornith-1.0-9B-GGUF · Hugging Face](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)
9. [Ornith-1.0: Self-ScaffoldingLLMsforAgenticCoding](https://deep-reinforce.com/ornith_1_0.html)
10. [DeepReinforceOpenSourcesOrnith-1.0CodingModels - Open...](https://www.opensourceforu.com/2026/06/deepreinforce-open-sources-ornith-1-0-coding-models/)
11. [LLM Explorer: AI Agent andOpen-SourceLanguage Model Directory](https://llm-explorer.com/)
12. [Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854)
13. [Saidul on X: "Open-source AI just raised the bar for coding agents..."](https://x.com/saidul_dev/status/2070154993240608844)
14. [🚨 AI News | TestingCatalog on X: "DeepReinforce has released Ornith-1.0..."](https://x.com/testingcatalog/status/2070153054679179400)
15. [Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)
16. [DeepReinforce Releases Ornith-1.0 for Self-Scaffolding Coding Agents, TechGig](https://techgig.com/news/software-devops/deepreinforce-releases-ornith-1-0-for-self-scaffolding-coding-agents/132008000)
17. [0xMarioNawfal on X: "DeepReinforce just launched Ornith-1.0..."](https://x.com/RoundtableSpace/status/2070211260898275530)
18. [deepreinforce-ai/Ornith-1.0-9B · Hugging Face](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)