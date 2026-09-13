---
layout: post
title: "AIがアプリ作成からデプロイまで自律的に？Anthropicの秘密プロジェクト「Antspace」を暴く"
description: "AnthropicのClaudeがコードを書くだけでなく、ウェブサービスを直接デプロイする秘密のプラットフォーム「Antspace」の正体を分析します。"
summary: "AnthropicはClaude Code環境内に独自のデプロイプラットフォーム「Antspace」を隠しており、AIがアプリ開発からホスティングまでを直接行う垂直統合型のエコシステムを構築しています。"
tags: [Anthropic, Claude, AI, クラウド, Antspace, 開発]
image: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace.jpg
image_alt: "Claude Codeの開発環境であるFirecrackerマイクロVMと、その内部に潜む秘密のデプロイプラットフォームAntspaceを象徴する抽象的なイラスト。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Anthropicのこうした動きは、AIモデルが単なるテキスト生成ツールにとどまらず、開発エコシステム全体を掌握する『エージェント中心型プラットフォーム』へと進化していることを示しています。"
quiz:
  - question: "Anthropicが開発中の内部デプロイプラットフォームの名称は何ですか？"
    choices: ["Vercel", "Antspace", "Baku"]
    answer: 1
    explanation: "「Antspace」はAnthropicが開発した内部デプロイプラットフォーム（PaaS）です。「Baku」はプロジェクトビルダー環境のコードネームです。"
  - question: "Claude Code Web環境が実行される技術的基盤は何ですか？"
    choices: ["FirecrackerマイクロVM", "AWS Lambda", "Dockerコンテナ"]
    answer: 0
    explanation: "Claude Code Webは4つのvCPUと16GBのRAMを備えたFirecrackerマイクロVM上で動作します。"
  - question: "Anthropicが独自のデプロイプラットフォームを構築する理由は、何だと推測されていますか？"
    choices: ["単なる技術的な誇示", "垂直統合を通じたサービスエコシステムの掌握", "既存プラットフォームとの連携強化"]
    answer: 1
    explanation: "AIモデル、開発環境、そしてデプロイまでの全工程を垂直統合し、ユーザーが外部プラットフォームを使わなくても完璧なサービスを完成できるようにするための戦略だと分析されます。"
lang: ja
ref: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace
---

朝起きてAIに「今日思いついたアイデアでウェブサービスを1つ作って」と話し、コーヒーを飲んでいる間に完成品が世の中に公開されている……そんな未来を想像したことはありますか？現在は複数のツールを使い分け、複雑なプロセスを経る必要がありますが、Anthropicの最近の動きを見ると、この工程が非常にスムーズになりそうです。最近、セキュリティ専門家がClaude Code環境を分析したところ、Anthropicが隠していた驚くべきプロジェクトが発見されました。

### なぜこれが重要なのか？

これまでAIは主にコードを提案したり修正したりする「助手」の役割にとどまっていました。ユーザーはAIが提示したコードをコピーして自分のコンピュータに貼り付け、それをウェブサービスとして公開するために別のプラットフォーム（例：Vercel）を利用する必要がありました。しかし、Anthropicが「Antspace（アントスペース）」という独自のデプロイプラットフォームを準備しているという事実は、AIが**「考え、コードを書き、サーバーにアップロードするまで」**の全工程を単独で遂行する「ワンストップ開発者」へと進化していることを意味します[Source 1](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace), [Source 6](https://x.com/AprilNEA/status/2034209430158619084), [Source 11](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)。ユーザーは複雑な技術知識がなくても、AIだけでアイデアをサービスに転換できる時代が来ているのです。

### 分かりやすい解説：「キッチン」の進化

分かりやすく例えてみましょう。これまでのAI開発環境が**「食材を整えてくれる包丁」**だったとすれば、Antspaceは**「食材の準備から調理、配達まで全てこなす集中型キッチン」**のようなものです。

これまでは、皆さんが直接食材（コード）を受け取り、キッチン（クラウドプラットフォーム）まで走っていって調理（デプロイ）する必要がありました。しかしAnthropicは、Claudeというシェフに専用のキッチンを用意しました。これが「Baku（バク）」と呼ばれる専用環境です。ユーザーが「ウェブアプリを作って」と言うと、システムは瞬時に**「Firecracker（ファイアクラッカー）マイクロVM」**という仮想空間を作り出します[Source 2](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582), [Source 4](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace/blob/master/baku-analysis.md)。

簡単に言うと、Firecrackerは非常に軽量で高速な「仮想コンピュータ」です。一般的な仮想マシンが巨大な工場だとすれば、このマイクロVMは必要な機能だけを備えて瞬時に立ち上がる「組み立て式キッチン」のようなものです[Source 11](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)。その中で4つの頭脳（vCPU）と16GBのメモリを活用し、Claudeが自らアプリを構築し、デプロイまで一気に処理するのです[Source 2](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582)。

想像してみてください。キャンプ場に行ってテントを自分で張るのではなく、AIに「綺麗なテントを張って」と言うだけで魔法のように設置されるのと同じです。Antspaceは、まさにあなたのウェブサイトのための「自動テント設営サービス」といえるでしょう。

### 現在の状況：水面に現れた秘密

専門家によるリバースエンジニアリング（逆解析）によると、このシステムは単に既存の外部サービスを借りて利用する手法ではありませんでした。AnthropicはVercelなどの既存サービスのAPIを単につなぐレベルを超え、**基礎から直接デプロイプロトコルを構築**しています[Source 1](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace), [Source 3](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace)。

現在、AnthropicはClaude Codeを通じて、ユーザーが何を、どのように作っているのかについての膨大なデータを収集しています。このデータを基にAntspaceを最適化すれば、開発者がわざわざサーバー設定を調整しなくても、AIが勝手に最も効率的な環境にアプリを立ち上げてくれる時代が来るはずです[Source 5](https://x.com/mayazi/status/2034282767693873492)。

### 今後はどうなるか？

Anthropicの戦略は明確に見えます。ユーザーがClaudeに滞在する時間を増やし、単なる「対話」相手を超えて「生産」の中心地にすることです。将来的には、開発者が「このアプリをデプロイして」と一言言うだけで、Antspaceが裏で密かにサーバーを構築し、ドメインを接続してくれるでしょう。

ユーザーにとっては利便性が極大化しますが、一方で特定のAIエコシステムに依存することにもなります。Anthropicが構築しようとしているこの垂直統合型のエコシステムは、今後、他のAIモデルにとっても強力な基準点になるはずです[Source 5](https://x.com/mayazi/status/2034282767693873492), [Source 14](https://www.linkedin.com/posts/laserfocus_breaking-if-you-reverse-engineered-the-activity-7440048762829443072-of-K)。

### MindTickleBytesのAI記者視点

AIがコードを生成するレベルを超え、「デプロイ」という現実的なインフラまで直接統制し始めたということは、AIが単なる仮想世界のテキスト生成機ではなく、物理的なサービス（ウェブサイト）を運営する主体へとランクアップしたことを意味します。開発者の定義が「コードを直接書く人」から「AIのデプロイの方向性を決定する監督者」へと変わっているのかもしれません。私たちは今、何を作るかを超えて、どのAIにデプロイを任せるかを悩むべき時代に直面しています。

## 参考資料

1. [Anthropic's Hidden Vercel Competitor "Antspace" | AprilNEA](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace)
2. [Reverse-engineering Claude Code reveals Anthropica's undisclosed PaaS platform "Antspace": Built in Baku, self-hosted, full-stack ecosystem already taking shape | WEEX Crypto News](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582)
3. [GitHub - AprilNEA/reverse-engineering-claude-code-antspace: Anthropic's Hidden Vercel Competitor "Antspace" · GitHub](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace)
4. [reverse-engineering-claude-code-antspace/baku-analysis.md at master · AprilNEA/reverse-engineering-claude-code-antspace](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace/blob/master/baku-analysis.md)
5. [Maya Zehavi on X: "Anthropic is making the obvious play to build out a platform & own the entire stack from deployment, cloud & orchestration. But more importantly, Anthropic is gathering the user data about ppl are building with Claude so that they can offer a more optimized end to end platform." / X](https://x.com/mayazi/status/2034282767693873492)
6. [AprilNEA on X: "🧵 I just reverse-engineered the binaries inside Claude Code's Firecracker MicroVM and found something wild: Anthropic is building their own PaaS platform called "Antspace" (Ants + Space). It's a full deployment pipeline — hidden in plain sight inside the environment-runner https://t.co/QbPT9ILECG" / X](https://x.com/AprilNEA/status/2034209430158619084)
11. [ClaudeCode Scheduled Tasks and Project Antspace | Roman Peschke](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)
14. [BREAKING: If you reverse-engineered the binaries inside Claude...](https://www.linkedin.com/posts/laserfocus_breaking-if-you-reverse-engineered-the-activity-7440048762829443072-of-K)