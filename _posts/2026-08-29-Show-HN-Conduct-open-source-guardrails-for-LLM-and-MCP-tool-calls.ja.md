---
layout: post
title: "AIがあなたのコンピュータを操る前に、『思考』を検問する方法はあるのか？"
description: "AIが外部ツールを実行する前に危険な行動を遮断するオープンソース・セキュリティプロジェクト『Conduct』について解説します。"
summary: "AIアシスタントが外部ツールを使用して作業する際、危険な命令を事前に遮断・監視できるオープンソース・セキュリティレイヤー『Conduct』を紹介します。"
tags: [AI, セキュリティ, オープンソース, LLM, MCP]
image: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls.jpg
image_alt: "AIアシスタントと外部システムの間でセキュリティを守る仮想ファイアウォールを可視化したイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIアシスタントの能力が拡張されるほど、その権限も危険なものとなります。Conductのような『ガードレール』は、AIを信頼して利用するために不可欠なシートベルトとなるでしょう。"
quiz:
  - question: "Conductは主にどのような機能を実行しますか？"
    choices: ["AIモデルの直接開発", "AIアシスタントのツール実行前の監視および遮断", "AIモデル学習データの収集"]
    answer: 1
    explanation: "ConductはAIが外部ツール（MCPなど）を実行しようとする意図を捉え、実際にツールが実行される前に危険性を点検し、必要に応じて遮断するセキュリティプロジェクトです。"
  - question: "Conductが監視する主要なポイントはどこですか？"
    choices: ["ウェブブラウザの閲覧履歴", "MCPレイヤー、ルーター、LLM呼び出しの3箇所", "ユーザーの個人パスワード保管庫"]
    answer: 1
    explanation: "Conductは、MCPレイヤー、ルーター、そしてLLM呼び出しという3つのenforcement surface（強制ポイント）でセキュリティポリシーを適用します。"
  - question: "Conductのフェイルモード（Failure mode）はどのような方式を採用していますか？"
    choices: ["Fail-close（遮断）", "Fail-open（許可/ソフト）", "無条件の強制終了"]
    answer: 1
    explanation: "Conductは、セキュリティシステムに問題が生じた際、優先的に動作を維持する『Fail-open（ソフト）』方式を採用しています。"
lang: ja
ref: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls
---

想像してみてください。朝起きてスマートフォンのAIアシスタントに「メールを全部読んで、重要な内容だけ選んで業務用のSlackチャンネルに共有して」と頼みました。非常に便利な機能ですよね？しかし、このAIがメールアカウントへのアクセス権限を超えて、あなたのコンピュータにあるファイル削除権限まで持っていたらどうでしょうか？あるいは、誤って非公開文書までSlackに上げてしまったら？

このような便利さの裏に潜む不安を解消するために登場したオープンソース・セキュリティプロジェクトがあります。それが**Conduct**です。

### なぜ重要なのか？ (Why It Matters)

最近のAIモデルは単に対話するレベルを超え、人のように外部ツールを使って直接業務を処理し始めました。これを可能にする核心技術の一つが**MCP（Model Context Protocol、AIアシスタントと外部データやツールを接続する標準通信規格）**です。 [[出典: What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/)]

AIが便利になるほど、そのAIが自分のコンピュータやサーバーで実行できる「権限」も強力になっています。企業が業務でAIを導入する際の最大の障壁はセキュリティ事故です。AIが誤って重要ファイルを消去したり、外部に流出させたりするリスクを完璧に制御することは難しいためです。**Conduct**は、企業がAIアシスタントを安全に配置できるよう支援する、一種の「シートベルト」の役割を果たします。 [[出典: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)]

### わかりやすく解説 (The Explainer)

Conductを例えるなら、会社の建物入り口にある**「セキュリティゲート」**のようなものです。

これまでAIアシスタントがツールを実行するプロセスが「どうぞ通過してください」と言うレベルだったとすれば、ConductはAIが「このファイルを削除して」という命令を下す際に**「少々お待ちください、どこへ行くどのようなファイルか確認します」**と遮るゲートの役割をします。 [[出典: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)]

別の例として、写真加工アプリを使うときにアプリが写真フォルダに直接アクセスすることを許可するか尋ねる「アクセス権限フィルター」があるように、ConductはAIモデルの「実行意図」を事前にキャッチして、その作業が安全かどうかを判断する監視フィルターです。

このシステムは主に3箇所を監視します。 [[出典: GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)]
1. **MCPレイヤー**: AIが外部データと送受信するすべてのMCPツール呼び出しを確認します。
2. **ルーター**: AIがどのSDKを経由しようと、呼び出されるすべてのLLM（大規模言語モデル）命令を監視します。
3. **LLM呼び出し**: AIモデルが生成した具体的な命令呼び出し自体を点検します。

もしAIが不審な行動を取ろうとすれば、Conductは外部ツールに命令が伝わる前にこれを遮断したり、記録（audit）を残してセキュリティチームが後で検討できるようにします。

### 現在の状況 (Where We Stand)

現在、Conductは**オープンソース**で提供されているセキュリティ・ガードレール（Guardrail、AI安全のための制御装置）プロジェクトです。 [[出典: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)] [[出典: ConductOpenSourceGuardrailsFORLLMANDMCPToolCalls](https://rankium.io/rankium/product/conduct-open-source-guardrails-for-llm-and-mcp-tool-calls)]

このプロジェクトの興味深い点の一つは、フェイルモードが**「Fail-open（ソフト）」**方式であることです。 [[出典: GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)] これはセキュリティシステム自体にエラーが生じてもAIアシスタントのすべての機能が停止しないように設計されたもので、ビジネス継続性を重視する組織にとっては有利な選択です。

もちろん、このツールをインストールするだけであらゆるセキュリティ脅威が消えるわけではありません。実際の業務環境におけるAIの安全性は、複数のガードレールが重なり合った「スタック」構造を持つべきです。 [[出典: LLMGuardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-2026)] Conductは、その複数層のうち「ツール実行段階」を担う重要なレイヤーといえます。

### 今後の展望 (What's Next)

今後は、AIが単にテキストを読んだり書いたりするだけでなく、コードを実行し、サーバーを管理して業務自動化を遂行する「エージェント」へと進化するでしょう。それに伴い、AIのすべてのツール呼び出しを検査するConductのようなツールの重要性はますます高まります。ユーザーが直接ツール入力値を確認し、結果を検証する過程が不可欠な時代が来ています。 [[出典: Tools- Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)]

開発者は今後、AIが「何ができるか」を超えて、「どうすれば安全に制御できるか」を悩むようになるはずです。

---

### MindTickleBytesのAI記者による視点
AIの能力を拡張するのは技術の領域ですが、その権限を統制するのは信頼の領域です。Conductのようなオープンソースのガードレールは、AIが人間のツールとして安全に共存できる基盤を整える重要な流れです。透明な検証プロセスこそが、技術の発展をむしろ加速させるでしょう。

## 参考資料
1. [ShowHN: Conduct, open-source guardrails for LLM and MCP tool calls](https://news.ycombinator.com/item?id=49483173)
2. [Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)
3. [GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)
4. [ConductOpenSourceGuardrailsFORLLMANDMCPToolCalls](https://rankium.io/rankium/product/conduct-open-source-guardrails-for-llm-and-mcp-tool-calls)
5. [What is the Model Context Protocol (MCP)? - Model Context Protocol](https://modelcontextprotocol.io/)
6. [LLMGuardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-2026)
7. [Tools- Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)