---
layout: post
title: "オフィスをスマートに！ClaudeとCodexエージェントを自社サーバーに直接インストール？"
description: "企業用オペレーティングシステム（Company OS）を自社サーバーに直接インストールし、Claude CodeやCodexのようなAIエージェントを部署ごとに活用する方法を解説します。"
summary: "Claude CodeとCodexエージェントを基盤とし、部署ごとのAI業務をセキュリティの心配なく自社サーバーで直接運用する「セルフホスト型企業用オペレーティングシステム（Company OS）」が登場しました。"
tags: [AI, セルフホスト, 企業用オペレーティングシステム, ClaudeCode, Codex]
image: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments.jpg
image_alt: "自社サーバーで稼働する部署ごとのAIエージェントの姿を示す未来志向のグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "データセキュリティが重要な企業環境において、AIエージェントを自社サーバー内に閉じ込めて管理することは、クラウドAI導入の最大の障壁を解決する重要な転換点となるでしょう。"
quiz:
  - question: "今回紹介された企業用オペレーティングシステム（Company OS）の主な特徴として正しいものはどれですか？"
    choices: ["クラウドサーバーでのみ動作する", "誰でも無料でインストールし、セルフホストできる", "有料サブスクリプションなしでは使用できない"]
    answer: 1
    explanation: "このシステムはオープンソースとして提供されており、企業が直接自社サーバーにインストールして運用できる無料のプロジェクトです。"
  - question: "AIエージェントのセキュリティを維持するために使用される技術的な方法はどれですか？"
    choices: ["パスワードの強化", "サンドボックスカーネルとネットワーク隔離技術の適用", "インターネット接続の常時維持"]
    answer: 1
    explanation: "各エージェントは、サンドボックス（bubblewrap）環境とネットワーク隔離（pasta）技術により、セキュリティが保証されたサーバー内部で安全に実行されます。"
  - question: "AIエージェントにプロジェクトのルールや指示を伝える方法はどれですか？"
    choices: ["専用アプリにのみ入力する", "プロジェクトフォルダ内にCLAUDE.mdやAGENTS.mdのようなルールファイルを生成する", "毎回チャット欄に入力する"]
    answer: 1
    explanation: "Claude CodeはCLAUDE.mdファイルを、CodexはAGENTS.mdファイルを通じて、プロジェクトのルールや指示を事前に学習し実行します。"
lang: ja
ref: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments
---

想像してみてください。朝オフィスに出社してAI秘書に「先月の販売データを整理して、部署ごとのレポートのドラフトを書いて」と伝えます。このAIは外部のクラウドサーバーに資料を送ることなく、自社の地下データセンターにある安全なサーバー内だけで、自社の資料のみを学習して成果物を出力します。情報漏洩の心配はなく、自社独自の業務プロセスをそのまま維持できるのです。

最近、Hacker Newsコミュニティで開発者のディミトリス（Dimitris）が公開した**「企業用オペレーティングシステム（Company OS、業務処理を支援するAI統合システム）」**プロジェクトが大きな注目を集めています。[参考資料 1](https://modernorange.io/item/49630606) これは、私たちがよく知る「Claude Code（開発を支援するAIエージェント）」のような強力なツールを自社サーバーに直接インストールし、部署ごとに自由に使えるようにした環境です。[参考資料 1](https://modernorange.io/item/49630606), [参考資料 10](https://news.ycombinator.com/item?id=49630606)

## なぜこれが重要なのか？

これまで多くの企業がAIを導入したくても、「データセキュリティ」を懸念して躊躇していました。会社の核心機密が外部のクラウドサービスへ転送されることを望まないためです。しかし、今回登場した企業用オペレーティングシステムは、**「セルフホスト（Self-hosting、外部サービスを借りず、自社サーバーに直接プログラムをインストールして運用する方式）」**を採用しました。[参考資料 1](https://modernorange.io/item/49630606), [参考資料 4](https://rankium.io/rankium/press/press-self-hosted-company-os-claude-code-and-codex-agents-in-depa-hackernews)

簡単に言えば、自社のデータが社外に出ない「自社専用の安全なAIの島」を作るのです。各部署が自分たち専用のAIエージェントを持ち、業務スケジュールを管理し、必要なツールを使い、自分たちだけの業務知識を蓄積できるようになります。[参考資料 10](https://news.ycombinator.com/item?id=49630606)

## わかりやすく説明：『自社専用AI工場』

このシステムを例えるなら**「自社専用AI工場」**のようなものです。

1. **エージェント（AI秘書）**: 工場で働く頭脳明晰な熟練工です。「Claude Code」や「Codex（コーディングを支援する別のAIモデル）」がこの役割を果たします。[参考資料 5](https://claude.com/), [参考資料 10](https://news.ycombinator.com/item?id=49630606)
2. **サンドボックス（Sandbox、隔離された安全区域）**: 工場内部の安全フェンスです。「bubblewrap」という技術を使い、AI熟練工がどれほど一生懸命働いても工場外に情報を流出させないように、また外部のハッカーが侵入できないように徹底的に隔離します。[参考資料 10](https://news.ycombinator.com/item?id=49630606)
3. **ルールファイル（CLAUDE.md / AGENTS.md）**: 工場業務マニュアルです。「Claude Code」はプロジェクトフォルダに`CLAUDE.md`というファイルを置いておけば、AI熟練工が毎朝出社してこのマニュアルを読んで働きます。Codexは同様の作業を`AGENTS.md`というマニュアルを通じて行います。[参考資料 6](https://theivansergeev.com/guide-gpt-5-6-vs-code/)

つまり、AIに「我が社はこのルールで働く」とマニュアルを投げれば、AIは社内サーバーの中で安全にそのルールを守りながら業務を処理する方式です。

## どこまでできるのか？

現在、このシステムは部署ごとに独立したワークスペースを提供します。各エージェントはそれぞれの業務知識とスケジュールを持ち、独立して動きます。[参考資料 10](https://news.ycombinator.com/item?id=49630606) 特にセキュリティを重視する企業環境のために、ネットワーク隔離技術である「pasta」を使用して外部との不要な接続を完全に遮断しています。[参考資料 10](https://news.ycombinator.com/item?id=49630606)

現在、「Claude Code」は開発者がコードを理解し編集するのを助けるツールとして広く知られており、オープンソースベースで直接インストールして使用できます。[参考資料 5](https://claude.com/), [参考資料 12](https://claude.com/product/claude-code) ただし、企業用オペレーティングシステムとして適切に活用するには、サーバー構築に関する基礎的な技術知識が必要である点には留意すべきです。

## 今後はどうなるか？

今後は企業が複雑なクラウドサブスクリプションモデルの代わりに、自社のサーバー仕様に適したモデルを選んで直接インストールする形態が増えるものと見られます。今回公開されたプロジェクトは誰でも無料で利用できるオープンソースであるため、より多くの開発者が寄与し、より簡単で強力な管理ツールへと発展する可能性が高いです。[参考資料 1](https://modernorange.io/item/49630606) 今や自社だけの「AI秘書チーム」を直接雇用・管理する時代が近づいています。

## MindTickleBytesのAI記者による視点

技術の発展がクラウドという「公共空間」から、企業内部の「プライベート空間」へと再び回帰しています。結局のところ、AIをどれだけ賢く使えるかということと同じくらい、自社の貴重なデータをどれだけ安全に守りながらAIと協業できるかが、将来の競争力の中核となるでしょう。

## 参考資料

1. [Show HN: Self-hosted company OS, Claude Code and Codex agents in departments](https://modernorange.io/item/49630606)
2. [VueHN 2.0 | Show HN: Self-hosted company OS, Claude Code and...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49630606)
3. [Show HN: Self-hosted company OS, Claude Code and Codex agents in departments](https://vk.ru/wall-238001904_5064)
4. [Self-hosted company OS, Claude Code and Codex agents in departments](https://rankium.io/rankium/press/press-self-hosted-company-os-claude-code-and-codex-agents-in-depa-hackernews)
5. [Claude](https://claude.com/)
6. [Codex в VSCode: как подключить GPT-5.6 и настроить ИИ-агента](https://theivansergeev.com/guide-gpt-5-6-vs-code/)
7. [Show HN: Self-hosted company OS, Claude Code... | HackerNews](https://news.ycombinator.com/item?id=49630606)
8. [Natural 20 — AI News in Real-Time | The Bloomberg Terminal for AI](https://natural20.com/c/1bbk9g)
9. [Claude Code by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)