---
layout: post
title: "AIがコードを3万回も修正？Anthropicが「Git」を捨てた理由"
description: "AIによるコード生成量が多すぎて既存のバージョン管理システムが限界に達したため、Anthropicが独自開発したシステム「Scion」へ移行した経緯"
summary: "AIモデル「Claude」が毎日3万件を超えるコード変更を行うようになり、Anthropicは従来のGitベースのインフラを廃止し、独自バージョン管理システム「Scion」を開発・導入しました。"
tags: [Anthropic, AI開発, バージョン管理, Scion, Claude]
image: 2026-10-14-Redesigning-Source-Control-at-Anthropic.jpg
image_alt: "複雑なコードネットワークとAIエージェントが相互作用する様子を視覚化したグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人間開発者の速度を超えたAIの生産性が、既存のツール体系を揺るがしています。今やインフラ自体が「エージェント」のために設計されるべき時代です。"
quiz:
  - question: "Anthropicが従来のGitの代わりに独自のバージョン管理システム「Scion」を導入した主な理由は何ですか？"
    choices: ["コスト削減のため", "AIエージェントの爆発的なコード生成による既存システムのボトルネック解消のため", "より安全なセキュリティ機能を提供するため"]
    answer: 1
    explanation: "AIが自律的にコードを記述し反復する過程で、コードマージ量が1日2,500件から3万件へと急増し、既存のインフラでは対応不可能になったためです。"
  - question: "Anthropicの新システム「Scion」はどのような環境のために設計されましたか？"
    choices: ["人間開発者のみが使用するオフライン環境", "AIエージェントが24時間体制でコードを記述・反復（Iteration）する環境", "モバイルアプリ開発専用環境"]
    answer: 1
    explanation: "ScionはAIエージェントが絶えずコードを生成し、自律的に反復学習を行う環境に最適化して設計されました。"
  - question: "Anthropicがコード変更のたびにすべてのテストを実行する代わりに導入した手法は何ですか？"
    choices: ["テストの完全省略", "決定論的テスト影響分析（Test Impact Analysis）", "ランダムなテスト抽出"]
    answer: 1
    explanation: "膨大なコード変更のたびにすべてのテストを実行する代わりに、過去のデータとパッケージの関連性に基づいて必要なテストのみを選別して実行する、決定論的テスト影響分析サービスを導入しました。"
lang: ja
ref: 2026-10-14-Redesigning-Source-Control-at-Anthropic
---

想像してみてください。あなたが書いた文章を誰かが1秒ごとに3万回修正し、再検討するよう求めてきたらどう感じるでしょうか。人間には到底耐えられない速度です。しかし、今まさにAI企業Anthropicのオフィスで実際に起きているのがこの状況です。AIモデル「Claude」が自ら研究を反復し、新しいサービスを構築する中で、同社のコーディングインフラが悲鳴を上げ始めたのです。

### なぜこれが重要なのか？

これまでソフトウェア開発は「人間」の速度に合わせて調整されてきました。しかしAIが自らコードを書き始め、今やコードを書くことよりも**記述されたコードを管理・デプロイすること**の方が大きなボトルネックとなっています。[Anthropicは、コーディングインフラがもはやAIの生産性に追いつけない状況に直面しました。](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943) Anthropicが今回インフラを完全に刷新したことは、AI時代において開発ツールがいかにあるべきかを示す重要なマイルストーンです。

### わかりやすい解説：「Git」というパズル箱の限界

私たちがよく使う「Git」は、開発者がコードを保存・修正するための共同作業スペースです。例えるなら、数人が一つの巨大なパズルを組み立てる「パズル箱」のようなものです。人数が少なければ順番を守ってピースをはめ込むことができます。

しかし、AIエージェントたちがこのパズル箱に群がり、1秒ごとに数千ものピースを付けたり外したりしたらどうなるでしょうか。箱は壊れてしまいます。従来のGitは人間中心の「オフライン」開発環境を前提に設計されているため、AIがリアルタイムで吐き出す数万件もの変更事項を一度に処理するには重すぎました。[Anthropicのコードマージ量は、1日2,500件から3万件へと、なんと12倍近くに急増しました。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

そこでAnthropicは、全く新しい方式のシステム**「Scion」**を自ら構築しました。ScionはAIエージェントが24時間体制で休むことなくコードを修正しても耐えられるよう設計された、「AI専用バージョン管理システム」です。[Anthropicは5ヶ月かけて、既存のモノレポ（Monorepo）をGitからScionへ完全に移行しました。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

### 現状：AIの速度に合わせたインフラ改善

Anthropicは単にバージョン管理システムを変更しただけではありません。Scionの導入とともに、いくつかの核心的な変化をもたらしました。

1.  **コードレビューツールの進化**: 人間が数万件ものコードを目視で確認するのは不可能です。Anthropicは**「Antique」**という新しいコードレビュー専用システムを導入し、AIが生成する膨大な変更事項を人間が効率的にレビューできる環境を作りました。[AnthropicはScionと共に、この新しいコードレビューのインターフェースを開発・デプロイしました。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
2.  **賢いテストシステム**: コードが変わるたびにすべてのテストを実行していては時間がかかりすぎます。そのためAnthropicは、過去のデータとコードの関連性を分析し、**「真に必要なテストのみを選別して実行する『決定論的テスト影響分析サービス』」**を導入しました。[この方式はテスト実行効率を高め、開発速度を再び向上させました。](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)

### 私たちは今どこにいるのか？

Anthropicの事例は、ソフトウェア開発環境が「人間中心」から「AIエージェント中心」へと移行していることを示す信号弾です。かつて開発者がコンピュータの性能を気にしていたように、これからは「コンピュータがエージェントの活動に耐えられるか」を考慮しなければならない時代が来たのです。この変化はAnthropicだけの話ではありません。今後、多くのテック企業が人間の利便性を超え、機械の途方もない生産性を支える新しいインフラを模索することになるでしょう。

### 今後はどうなるのか？

私たちが使うサービスのアップデート周期はますます短くなるはずです。その裏側では、今回のようにAIが自ら成長しようと奮闘する、新しい形態の「デジタル工場」が稼働することになります。Scionのようなインフラは、AIが単なるツールを超え、技術の基盤を自ら再設計する「自己発展」段階に突入したことを象徴しています。[ScionはAIが常時稼働する「Agent-always-on」シナリオに特化して設計されました。](https://zeli.app/zh/story/50073633)

私たちは今、人間がコードを書いていた時代を過ぎ、AIがコードを記述し人間がその結果を監督する興味深い転換点に立っています。

---

**MindTickleBytesのAI記者による視点**
AIが自らコードを修正し研究する「エージェンティック（Agentic）」な時代はすでに始まっています。Anthropicの動向は、AIが技術を消費する段階を超え、技術の基盤施設までも自ら再設計させる自己発展の段階に突入したことを意味します。

## 参考資料

1. [AnthropicClaude Can NowControlYour Computer - YouTube](https://www.youtube.com/watch?v=eB7E-mtpC18)
2. [Anthropic(Anthropic)](https://huggingface.co/Anthropic)
3. [How AI is transforming workatAnthropic\Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
4. [Agentic coding is straining CI. Here’s how we... | Claude byAnthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)
5. [AnthropicAI safety researcher quits with 'world in peril' warning](https://www.bbc.com/news/articles/c62dlvdq3e3o)
6. [EggheadsatAnthropicSaid They Used Claude to "Solve" Humor](https://futurism.com/artificial-intelligence/anthropic-solve-humor)
7. [Anthropicrestores Fable 5, Mythos 5 after U.S. lifts exportcontrols](https://www.linkedin.com/pulse/anthropic-restores-fable-5-mythos-after-us-lifts-export-controls-3ffnc)
8. [Redesigning source control at Anthropic — CodeNews.com](https://codenews.com/news/redesigning-source-control-at-anthropic-1ojqmz)
9. [Anthropic Scion: Why Its Monorepo Left Git at 30,000 Merges](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
10. [Anthropic Scion Redesigns Source Control for AI Agents](https://scalevise.com/resources/anthropic-scion-agent-scale-source-control/)
11. [Anthropic reinvents source control as Claude floods the world ...](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943)
12. [Anthropic Overhauls Source Control to Fix Bottlenecks](https://book.st-hakky.com/en/news/redesigning-source-control-at-anthropic)
13. [Redesigning source control at Anthropic - hoton.ai](https://hoton.ai/en/news/redesigning-source-control-at-anthropic-1vlb4uz)
14. [Anthropic 因Claude重写版本控制系统 — Redesigning Source Control a...](https://zeli.app/zh/story/50073633)
15. [Newsroom \Anthropic](https://www.anthropic.com/news)
16. [AnthropicIs Bleeding Out](https://www.wheresyoured.at/anthropic-is-bleeding-out/)
17. [Hidden AI instructions reveal howAnthropiccontrols... - Ars Technica](https://arstechnica.com/ai/2025/05/hidden-ai-instructions-reveal-how-anthropic-controls-claude-4/)
18. [OpenAI andAnthropicAI crisis explained: OpenAI andAnthropicfear...](https://economictimes.indiatimes.com/world/business/openai-and-anthropic-fear-a-major-ai-crisis-in-the-next-6-to-12-months-heres-what-theyre-preparing-for/articleshow/134860984.cms)
20. [LatestAnthropic(Claude AI) Statistics (2025) | StatsUp](https://analyzify.com/statsup/anthropic)