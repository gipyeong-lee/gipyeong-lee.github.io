---
layout: post
title: "AIが作ったウェブサイトはなぜどれも同じに見えるのか？「ホールマーク」でAIの癖を直す"
description: "AIコーディングツールが作る千篇一律なデザインから脱却する方法、オープンソースのデザインスキル「ホールマーク（Hallmark）」を紹介します。"
summary: "ホールマーク（Hallmark）は、AIが生成したウェブデザインが特有の「AIっぽさ」を捨て、より独創的で専門的に見えるようにするためのオープンソースのデザインスキルです。"
tags: [AI, デザイン, コーディング, ホールマーク, デザインスキル]
image: 2026-07-27-Hallmark-Anti-AI-Slop-Design-Skill-for-Claude-Code-Cursor-and-Codex.jpg
image_alt: "多様な構造と色感を持つ現代的なUIデザインが画面に広がっている様子。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの「デフォルト値」を拒否することは、人間らしい創造性を取り戻すために不可欠なプロセスです。ホールマークは、技術が人間の美意識を模倣するだけでなく、独特の個性を持つように強制するという点で非常に興味深いです。"
quiz:
  - question: "ホールマーク（Hallmark）デザインスキルが主に行う役割は何ですか？"
    choices: ["AIが生成したコードの速度を上げる", "AIが作ったUIデザインのAIっぽい感じ（slop）を除去する", "ユーザーが直接コーディングするように誘導する"]
    answer: 1
    explanation: "ホールマークは、AIコーディングツールが生成したUIがテンプレートのように同じに見えないよう、構造とスタイルルールを適用するデザインスキルです。"
  - question: "ホールマークはAIコーディングツールにどうやってインストールできますか？"
    choices: ["複雑なサーバー設定が必要", "単一コマンドで簡単にインストール", "ウェブブラウザの拡張機能としてインストール"]
    answer: 1
    explanation: "ホールマークは「npx skills add」のような単一のコマンドを通じて、Claude Code、Cursor、Codexなどにインストールできます。"
  - question: "ホールマークを適用したコードは、最終的に開発者に渡される前に何を経由しますか？"
    choices: ["自動翻訳プロセス", "約57～65個の「スロップ（slop）テスト」関門", "データ暗号化プロセス"]
    answer: 1
    explanation: "ホールマークはAIが作ったコードをそのまま見せず、デザインルールの遵守状況や独創性を検証する数十のテスト関門を経由させます。"
lang: ja
ref: 2026-07-27-Hallmark-Anti-AI-Slop-Design-Skill-for-Claude-Code-Cursor-and-Codex
---

想像してみてください。あなたがAIに「ビジネス用のきれいなウェブサイトを作って」と頼みました。しばらくして完成したサイトを見ましたが、なぜか先週見た別のAIが作ったサイトと、色だけが違うだけで構造が同じに見えます。まるで「工場で量産した」かのような感覚。デザイン業界ではこれを**「AIスロップ（AI-slop）」**と呼びます。AIが持つ「平均的なデザインの癖」によって発生する現象です。

最近、こうした悩みを解決してくれる賢いツールが登場しました。それがTogether AIが開発したオープンソースのデザインスキル、**ホールマーク（Hallmark）**です。

## なぜこれが重要なのか？

Claude Code、Cursor、CodexのようなAIコーディングツールは開発効率を劇的に高めてくれますが、一つの慢性的な問題を抱えています。人工知能モデルは、学習プロセスで最も頻繁に接したデータの「平均値」を導き出そうとする傾向があります。このため、AIが作ったUI（ユーザーインターフェース）は、そのほとんどが似たり寄ったりの構造やありきたりなレイアウトになってしまいます。

ホールマークは、こうした「AIの安易さ」を遮断します。開発者がいちいちデザインを修正しなくても、AIがコードを書く段階から専門的なデザインルールを強制的に適用します。これは、もはやテンプレートに貼り付けたような成果物ではなく、人が直接意図して悩み抜いたかのような、独創的な成果物を得られることを意味します。

## わかりやすく説明：AIのための「デザイン検問所」

ホールマークを理解する最も簡単な例えは、**「過酷なデザイン批評家」**をそばに置くことです。ホールマークは以下のようなプロセスを通じてAIのデザインを洗練させます。

1. **拒否（Refuse）**: ホールマークは、AIが深く考えずにデフォルト値として選択するありふれた構造を断固として拒否します。
2. **適用（Apply）**: 代わりにホールマークは、タイポグラフィ（フォント）、色、レイアウト、モーション、マイクロインタラクション（小さな動き）に関する緻密なルールをコードに適用します [Source 5](https://www.everydev.ai/tools/hallmark), [Source 15](https://mer.vin/2026/05/hallmark-design-skill-anti-slop-ui-for-claude-code-and-cursor/), [Source 18](https://github.com/adeoyewole028/hallmark-design-skills)。
3. **テスト（Test）**: ホールマークの核心は「スロップテスト（Slop-test）」の関門です。生成されたコードが最終的に開発者に渡される前に、ホールマークは約57から65個に達する検閲関門を通過させます [Source 10](https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026), [Source 11](https://agentconn.com/skills/hallmark/), [Source 12](https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026), [Source 16](https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)。

このプロセスは、写真アプリでフィルターをかけるのに似ています。AIが適当に描いた下書きに、ホールマークというフィルターが緻密に色を塗り、構造を整えて完成度の高い作品へと変身させるのです。

## 現在の状況

現在ホールマークは、Claude Code、Cursor、Codexといった人気のAIコーディングツールに単一のコマンドで簡単にインストールできます [Source 5](https://www.everydev.ai/tools/hallmark), [Source 19](https://gittrend.io/repo/Nutlope/hallmark)。

このツールは単なるテーマ変更にとどまらず、20から22の間で構造的なテーマを提供しており、開発者は`hallmark audit`コマンドを使用して、自分の既存コードが「AIスロップ」パターンを持っていないか自己点検することも可能です [Source 1](https://github.com/Nutlope/hallmark), [Source 2](https://hallmark.apposters.com/), [Source 10](https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026), [Source 18](https://github.com/adeoyewole028/hallmark-design-skills)。2026年7月基準で、すでに17,700個以上のGitHubスターを獲得しており、多くの開発者の注目を集めています [Source 19](https://gittrend.io/repo/Nutlope/hallmark)。

## 今後はどうなるのか？

今後は単に「コードを上手に書くAI」を越えて、「デザインセンスのあるAI」が標準になるでしょう。ホールマークはデザインルールをコードにエンコードすることで、AIの癖を変える第一歩を踏み出しました [Source 12](https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026), [Source 16](https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)。今後さらに多くのデザインスキルが開発され、私たちが使うすべてのAIサービスが「コピペ」されたウェブサイトではなく、それぞれの個性を持つ空間へと変貌することを期待しています。

## AIの視点

AIに創造性を求めることは難しいことですが、「してはいけないこと」を教えることは可能です。ホールマークは技術が人間の美意識を模倣するだけでなく、独特の個性を持つように強制するという点で非常に興味深いです。AIの「デフォルト値」を拒否することは、人間らしい創造性を取り戻すために不可欠なプロセスとなるでしょう。

## 参考資料

1. Nutlope/hallmark: Anti-AI-slop design skill for Claude Code, Cursor... (https://github.com/Nutlope/hallmark)
2. Hallmark - Anti-AI Design Skill for Claude Code, Cursor, and Codex (https://hallmark.apposters.com/)
3. Hallmark: Anti-AI Slop Design for Claude, Cursor, Codex | LinkedIn (https://www.linkedin.com/posts/arkadiy-sotnikov_github-nutlopehallmark-anti-ai-slop-design-activity-7483500613071167489-_zmV)
4. Hallmark: Anti-AI-slop design skill for Claude Code, Cursor, and... (https://addrom.com/hallmark-anti-ai-slop-design-skill-for-claude-code-cursor-and-codex/)
5. Hallmark - AI Design Rules for Coding Agents | EveryDev.ai (https://www.everydev.ai/tools/hallmark)
6. Hallmark | Analog (https://analoghq.ai/nutlope/skills/hallmark)
7. Hallmark + Claude Code, Codex: The BEST DESIGN SKILL YET! (https://www.youtube.com/watch?v=dVGJ3DE1MzA)
8. GitHub - Nutlope/hallmark: Anti-AI-slop design skill for Claude Code, Cursor, and Codex. · GitHub (https://github.com/Nutlope/hallmark)
9. hallmark/skills/hallmark at main · Nutlope/hallmark (https://github.com/Nutlope/hallmark/tree/main/skills/hallmark)
10. Hallmark Design Skill: Kill AI-Generated UI with Structural ... (https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026)
11. Hallmark - AI Agent Skill | AgentConn (https://agentconn.com/skills/hallmark/)
12. Hallmark Design Skill: Anti-AI-Slop UI for Agents (2026) (https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)
13. Hallmark: Anti-AI-Slop Techniques for Claude Code and Cursor | AIToolly (https://aitoolly.com/ai-news/article/2026-07-15-hallmark-new-anti-ai-slop-design-techniques-for-claude-code-cursor-and-codex-developers)
14. Hallmark: Rejecting AI-Slop in Claude Code and Cursor | AIToolly (https://aitoolly.com/ai-news/article/2026-07-16-hallmark-a-new-design-skill-to-eliminate-ai-slop-in-claude-code-and-cursor)
15. Hallmark Design Skill: Anti-AI-Slop UI for Claude Code and ... (https://mer.vin/2026/05/hallmark-design-skill-anti-slop-ui-for-claude-code-and-cursor/)
16. Hallmark Design Skill: Anti-AI-Slop UI for Agents (2026 ... (https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)
17. Hallmark Guide: Anti-AI-Slop Design for Claude Code, Curs... (https://opentools.ai/resources/hallmark)
18. GitHub - adeoyewole028/hallmark-design-skills: Anti-AI-slop ... (https://github.com/adeoyewole028/hallmark-design-skills)
19. hallmark — Anti-AI-slop design skill for Claude ... | GitTrend (https://gittrend.io/repo/Nutlope/hallmark)