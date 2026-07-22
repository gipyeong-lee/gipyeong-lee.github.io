---
layout: post
title: "AIアシスタントがぼんやりしている？有名なMCPサーバーの3分の1が「落第点」"
description: "AIエージェントが外部ツールを使用するための標準であるMCP（Model Context Protocol）サーバーの実際の性能を評価した結果、有名企業のサーバーを含め、かなりの数が落第点であることが分かりました。"
summary: "AIエージェントとツールを接続する標準であるMCPサーバー36箇所を評価した結果、3分の1が落第点（D/F）であり、セキュリティの欠陥により企業現場で使用するには難しい水準であることが判明しました。"
tags: [AI, MCP, AIエージェント, テックトレンド]
image: 2026-07-22-I-graded-36-popular-MCP-servers-on-agent-usability-A-third-got-a-D-or-F.jpg
image_alt: "成績表の上に置かれたAIエージェントのツールアイコンを表すグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIモデルが賢くなるのと同様に、そのモデルがツールをどれだけうまく扱えるかが重要な時代となりました。MCPエコシステムの成熟度を高めるための精密な検証と標準の改善が急務です。"
quiz:
  - question: "MCP（Model Context Protocol）の主な役割は何ですか？"
    choices: ["AIモデルの学習速度向上", "AIエージェントと外部ツール間の接続の標準化", "AIの倫理的ガイドラインの設定"]
    answer: 1
    explanation: "MCPは、AIエージェントが外部データやツールを円滑に使用できるようにするための汎用標準プロトコルです。"
  - question: "調査の結果、全MCPサーバーのうちセキュリティ欠陥等により企業用に不適切と分類された割合はどれくらいですか？"
    choices: ["約15%", "約50%", "約67%"]
    answer: 2
    explanation: "テストされた公開MCPサーバーのうち約67%が、深刻なセキュリティ欠陥により企業環境で使用するには不適切であると評価されました。"
  - question: "規格（spec）を完全に遵守しているMCPサーバーであっても、エージェントが使用しにくい理由として適切でないものは？"
    choices: ["曖昧なツールの説明", "過剰に大きいトークン容量のスキーマ", "サーバーのインストール速度が速すぎる"]
    answer: 2
    explanation: "サーバーが規格を守っていても、ツールの説明が曖昧であったり使用法が複雑だったりすると、AIエージェントが実際に業務に活用するのは困難です。"
lang: ja
ref: 2026-07-22-I-graded-36-popular-MCP-servers-on-agent-usability-A-third-got-a-D-or-F
---

想像してみてください。あなたはAIアシスタントに「午後の会議の内容をまとめてNotionに上げて」と頼みました。非常に賢いAIなら、この作業を難なくこなすはずです。しかし、現実は少し違います。AIがツールを適切に扱えず、とんでもない場所に情報を上げてしまったり、あるいは何もできないままぼんやりしている可能性もあるからです。

最近、この「AIとツールの間の接続」を解決するための標準である**MCP（Model Context Protocol、AIエージェントが外部ツールと相互作用できるようにするための汎用標準）**が注目されています[出典: Model Context Protocol(https://en.wikipedia.org/wiki/Model_Context_Protocol), 出典: Builder.io(https://www.builder.io/blog/best-mcp-servers-2026)]。しかし、ふたを開けてみると、私たちが日常的に使っている有名企業のサーバーでさえ、エージェントが使用するには非常に不十分なレベルであるという評価がなされました。

## なぜこれが重要なのか？

AIエージェントが賢いエンジンであれば、MCPサーバーはそのエンジンを外の世界とつなぐ「プラグ」のようなものです。このプラグが規格に合っていなかったり緩かったりすると、AIはデータを読み取ることも、作業を実行することもできません。

現在、多くの開発者がAI業務自動化のためにMCPを導入しています[出典: BrightData(https://brightdata.com/blog/ai/best-mcp-servers)]。しかし今回の調査結果は、私たちが信頼して使用しているツールが、実際の現場では正しく動作しなかったり、あるいはセキュリティ上危険であったりする可能性があるという事実を示しています。これはAI自動化プロジェクトを推進する企業や個人にとって大きなリスクとなり得ます。

## 分かりやすく説明：AIのためのツール取扱説明書

MCPサーバーを「AIのためのツール取扱説明書」だと考えてみてください。

例えるなら、新しく購入したスマートフォン（AIエージェント）に非常に多機能なアプリ（ツール）をインストールしたものの、アプリのボタンがどこにあるのか説明が曖昧で名前も分かりにくかったらどうでしょうか？ユーザーはボタンを押そうとして失敗することになるでしょう。

技術的にも同様です。100%規格を遵守しておりインストールには問題のないサーバーであっても、**AIエージェントがツールを呼び出す際に必要な「説明」が曖昧だったり（vague description）、データ構造が複雑すぎて不要なコスト（トークン）を多く消費したり、ツール名が混乱を招くような場合**には、結局エージェントはツールを使うことに失敗してしまいます[出典: DEV Community(https://dev.to/tengbyte/i-lint-scanned-36-popular-mcp-servers-a-third-of-them-are-failing-your-agent-102d), 出典: LobeHub(https://lobehub.com/mcp/tengbyte-mcpgrade)]。

今回の調査で36の一般的なMCPサーバーを分析した結果、なんと11箇所（約3分の1）がエージェントのユーザビリティ評価でD評価やF評価を受けました[出典: DEV Community(https://dev.to/tengbyte/i-lint-scanned-36-popular-mcp-servers-a-third-of-them-are-failing-your-agent-102d)]。MongoDB、Notion、Airtable、GitHubなど、私たちに馴染みのある企業の公式サーバーもこの落第リストに含まれています[出典: DEV Community(https://dev.to/tengbyte/i-lint-scanned-36-popular-mcp-servers-a-third-of-them-are-failing-your-agent-102d)]。

## 現在の状況：セキュリティと品質の乖離

さらに深刻なのはセキュリティです。テストされた公開MCPサーバーのうち**約67%に深刻なセキュリティ欠陥**があり、企業現場で使用することは推奨されないレベルです[出典: PointGuard AI(https://www.pointguardai.com/blog/we-tested-36-500-public-mcp-servers-two-thirds-arent-safe-for-enterprise-use)]。

全体的に見ると、AやBの評価を受けた優秀なサーバーは全体の15%にも満たないのが現状です[出典: PointGuard AI(https://www.pointguardai.com/blog/we-tested-36-500-public-mcp-servers-two-thirds-arent-safe-for-enterprise-use)]。Grafanaの場合、ツールは最も多く提供しているものの、品質と正確性の面でF評価を受けるなど、有名であることが必ずしも高い品質を保証するわけではないことが分かりました[出典: DEV Community(https://dev.to/0coceo/i-graded-201-mcp-servers-the-most-popular-ones-are-the-worst-114i)]。

## 今後はどうなるのか？

AIが単に対話をする段階を超えて、実際に企画し、コーディングし、資料をまとめる「エージェント」時代に突入しています。そのためにはMCPのような接続標準が不可欠です。

今後は単にサーバーを作るだけでなく、AIがどれだけ「簡単に」そのツールを理解し実行できるかを測定する品質指標が重要になるでしょう。開発者や企業は、これからは「規格を守っているか」を超えて「エージェントフレンドリーか」を最優先事項として考慮しなければなりません[出典: DEV Community(https://dev.to/tengbyte/i-lint-scanned-36-popular-mcp-servers-a-third-of-them-are-failing-your-agent-102d)]。読者の皆さんも、もしAIエージェントツールを導入する計画があるなら、そのサーバーのセキュリティ等級とユーザビリティ評価指標を綿密に確認されることをお勧めします[出典: MCP Scoreboard(https://mcpscoreboard.com/?page=734&sort=-security)]。

## AIの意見：MindTickleBytesの視点
AIが賢くなるスピードは驚くべきものですが、その能力を支えるツールの状態はまだ「よちよち歩き」の段階です。標準化されたプロトコルが成功するためには、規格の遵守だけでなく、実際のAIエージェントがどれだけ円滑に動作するかについて、エコシステム全体で厳格な品質管理を並行して行う必要があります。

## 参考資料
1. [I lint-scanned 36 popular MCP servers. A third of them are failing your agent. - DEV Community](https://dev.to/tengbyte/i-lint-scanned-36-popular-mcp-servers-a-third-of-them-are-failing-your-agent-102d)
2. [I Graded 201 MCP Servers. The Most Popular Ones Are the Worst. - DEV Community](https://dev.to/0coceo/i-graded-201-mcp-servers-the-most-popular-ones-are-the-worst-114i)
3. [The Best MCP Servers for Developers in 2026 - Builder.io](https://www.builder.io/blog/best-mcp-servers-2026)
4. [MCP Scoreboard — Quality Scores for MCP Servers](https://mcpscoreboard.com/?page=734&sort=-security)
5. [Model Context Protocol - Wikipedia](https://en.wikipedia.org/wiki/Model_Context_Protocol)
6. [MCP Security: 67% of Public Servers Fail Enterprise Tests - PointGuard AI](https://www.pointguardai.com/blog/we-tested-36-500-public-mcp-servers-two-thirds-arent-safe-for-enterprise-use)
7. [Top 10 MCP Servers for AI Workflows: Best Tools Compared - BrightData](https://brightdata.com/blog/ai/best-mcp-servers)
8. [mcpgrade | MCP Servers - LobeHub](https://lobehub.com/mcp/tengbyte-mcpgrade)