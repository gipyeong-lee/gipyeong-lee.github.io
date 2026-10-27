---
layout: post
title: "AIが書いたコードを見て「なぜこう書いたのか？」と悩んだことはありませんか？「仕様書先行開発」が解決策になるかもしれません"
description: "AIコーディングエージェントが作成したコードの意図を忘れてしまう問題と、それを解決するための「仕様書先行エージェント開発（SFAD）」手法を紹介します。"
summary: "AIがコーディングを主導する時代、時間が経つと誰も思い出せなくなるコードを防ぐため、作業前に仕様書を先に検討し記録する「仕様書先行エージェント開発（SFAD）」手法が注目されています。"
tags: [AI, 開発, コーディング, 生産性, 技術]
image: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove.jpg
image_alt: "AIエージェントと人間の開発者が協力し、画面に詳細な設計ドキュメントを表示してコミュニケーションをとる様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの速度と人間の深い思考が衝突する地点において、仕様書は単なる記録を超え、コードを理解するための道しるべとなるでしょう。"
quiz:
  - question: "仕様書先行エージェント開発（SFAD）が解決しようとしている中心的な問題は何ですか？"
    choices: ["AIの学習速度の低下", "文脈の記憶喪失およびコード意図の忘却", "ハードウェアコストの増加"]
    answer: 1
    explanation: "SFADは、AIがビルドしたコードの理由を時間が経過した後に誰も思い出せなくなる問題や、アーキテクチャの変質を防止しようとしています。"
  - question: "SFAD手法の核心的な手順として正しいものは？"
    choices: ["コードを先に作成し、仕様書を後から生成する", "作業前の仕様書検討、隔離された作業環境、段階的な承認", "AIにすべての要件決定を任せて放置する"]
    answer: 1
    explanation: "SFADは、コードを書く前に問題を定義し制約を検証した後に仕様書を確定させる方式に従います。"
  - question: "仕様書先行開発に対して批判的な見方が提起される理由は？"
    choices: ["仕様書作成コストがあまりにも高いため", "実際の製品環境では初期要件をすべてあらかじめ知ることはできない場合が多いため", "AIが仕様書を理解できないため"]
    answer: 1
    explanation: "製品開発環境では何を知らないかさえ分からない状態で意思決定が行われるため、無理な初期仕様書はかえって混乱を招く恐れがあるとの指摘があります。"
lang: ja
ref: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove
---

想像してみてください。あなたは数ヶ月前にAIエージェントに依頼して、素晴らしいウェブサイト機能を一つ作りました。ところが突然バグが発生し、そのコードを修正しなければならない状況になりました。コードを開いてみましたが、なぜそのように書いたのか全く理解できません。「なぜ自分はこう実装したのか？」「AIはなぜこのような方式で設計したのか？」

AIが瞬時にコードを吐き出す時代になり、そのコードの「根」や「意図」を見失うケースが増えています。最近、開発者の間で注目されている「仕様書先行エージェント開発（SFAD: Specification-First Agentic Development）」は、まさにこのような悩みから出発しました。[仕様書先行エージェント開発 - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)

## なぜこれが重要なのか？

かつての開発は人間が直接すべての行を書いていたため、少なくとも「なぜ」そのように書いたのかという文脈が開発者の頭の中にありました。しかし、AIがコーディングを主導する今、プロジェクトを開始して6ヶ月も経てば、誰もそのコードがなぜそのような構造で作られたのか思い出せないという現象が発生しています。これを「文脈記憶喪失（Context Amnesia）」と呼びます。[仕様書先行エージェント開発 - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)

このような状況が繰り返されると、システムの意図とは異なる設計に歪んでしまう「アーキテクチャの変質（Architectural Drift）」が起こります。これは企業の保守コストを急増させ、結果的には技術的負債を作る主犯となります。私たちがAIとより深く協力するためには、単にコードを早く作ることよりも、「なぜ」作るのかを証明する過程が不可欠です。

## 簡単に言うと

SFADを例えるなら、**「建物を建てる前に詳細な設計図を確定させ、工事過程のすべての変更事項を丁寧な日誌に記録すること」**と同じです。

従来はAIに対して「この機能を作って」と漠然と依頼していましたが、SFAD方式ではより体系的なステップを踏みます。

1. **ユースケース定義**: コードを書く前に「この機能はなぜ必要なのか？」を明確に定義します。[Brendan Small — SFAD](https://brendansmall.co/sfad)
2. **仕様書の作成と検討**: 問題を具体化して制約条件を検証した後、その仕様書を「ロック（Lock）」処理します。[Brendan Small — SFAD](https://brendansmall.co/sfad)
3. **段階的実行**: 検討が終わった仕様書に従ってAIエージェントにコードを書かせ、小さな変更事項であっても承認を経て記録します。[Spec-first agentic development - spec-first.dev](https://spec-first.dev/)

こうすることで、AIがコードを作成している間、仕様書という道しるべを常に確認できるようになります。このために開発されたプラグインは、Claude CodeのようなAIツールと統合され、AIが作業を行う際に必ず仕様書を記録し、検討するように強制します。[Spec-First - Spec-driven agentic - Hacker News | Zeli](https://zeli.app/story/50260571)

## 現在、私たちはどの位置に立っているのか？

すでに多くの開発者がこの方法を実務に適用しています。2026年初めからこのプラグインを使用しているある開発者は、1,000件以上の仕様書を作成し、50万行以上のコードを成功裏に構築したと明らかにしました。[Show HN: Spec-first agentic development plugin reports 500k...](https://shortsingh.com/article/show-hn-spec-first-agentic-development-plugin-reports-500k-lines-built-from-1-00)

しかし、あらゆる状況でこの方法が正解というわけではありません。一部では、実際の製品開発環境が非常に流動的であることを指摘しています。開始段階ですべてを仕様化することが、かえって非効率になり得るということです。何を知らないかさえ分からない状態で始めることが多いのに、無理な初期仕様書はかえってAIに矛盾する要件を伝えて混乱を招く可能性があるという批判です。[Show HN: Specification First Agentic Development Plugin and Prove](https://hn.nuxt.dev/item/50260571)

## 何が待ち受けているのか？

AIと人間の協力はますます精巧になるでしょう。単にコードを生産する段階を超え、AIが企画から実装、保守まで全工程を担う「エージェント中心開発（Agentic-first Development）」が本格化しています。[Let’s Talk Agentic Development | Spotify x Anthropic Live](https://www.youtube.com/watch?v=fHDGQHr_agg)

今後は、AIが単にコードを生成することを超えて、自身が作成した設計の根拠をどれだけ論理的に説明できるかが「実力」を評価する新しい尺度になるはずです。SFADはその出発点として、AIを制御不能なブラックボックスではなく、信頼できる協力ツールにするための重要な道しるべとなるでしょう。

---

### MindTickleBytesのAI記者による視点
AIエージェントがコーディングを代行してくれる事実よりも重要なのは、私たちがAIと「対話」を交わすための共通言語（仕様書）を持つようになったという点です。AIの速度に人間の判断力を加える方式こそが、未来の標準となるでしょう。

## 参考資料

1. [Show HN: Specification First Agentic Development Plugin and Prove](https://hn.nuxt.dev/item/50260571)
2. [Spec-first agentic development · spec-first.dev](https://spec-first.dev/)
3. [Spec-First - Spec-driven agentic · Hacker News | Zeli](https://zeli.app/story/50260571)
4. [Specification-First Agentic Development - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)
5. [Releases · holgerleichsenring/specification-first-agentic ...](https://github.com/holgerleichsenring/specification-first-agentic-development/releases)
6. [Show HN: Spec-first agentic development plugin reports 500k ...](https://shortsingh.com/article/show-hn-spec-first-agentic-development-plugin-reports-500k-lines-built-from-1-00)
7. [spec-first: 规范驱动的代理开发插件 — Show HN: Specification First...](https://zeli.app/zh/story/50260571)
8. [Brendan Small — Specification First Agentic Development](https://brendansmall.co/)
9. [Books by Anatoly Volkhover | Agentic Spec-Driven Development...](https://anatoly.com/books)
10. [Let’s Talk Agentic Development | Spotify x Anthropic Live - YouTube](https://www.youtube.com/watch?v=fHDGQHr_agg)
11. [Flowith AI - Your Agentic Workspace](https://flowith.io/)
12. [Manus: Hands On AI](https://manus.im/)
13. [Book Review: Agentic Spec-Driven Development](https://www.plainionist.net/Agentic-Spec-Driven-Development/)
14. [SFAD — Specification First Agentic Development | Brendan Small](https://brendansmall.co/sfad)
15. [jsell-rh/agentic-development-plugins | Awesome Claude Plugins](https://awesomeclaudeplugins.com/jsell-rh/agentic-development-plugins)
16. [Let’s Talk Agentic Development: Spotify x Anthropic Live](https://engineering.atspotify.com/2026/4/anthropic-agentic-development)