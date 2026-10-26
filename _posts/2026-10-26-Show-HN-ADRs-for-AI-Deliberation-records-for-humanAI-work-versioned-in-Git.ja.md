---
layout: post
title: "AIとの対話、チャットを閉じたら消える？AI協業の記録法「ADRs4AI」"
description: "AIとプロジェクトを進める際、重要な決定事項を散逸させず、記録してバージョン管理するためのツールと方法論「ADRs4AI」を紹介します。"
summary: "AIとの協業の決定事項をコードと共にGitに記録し、議論のプロセスを誰でもいつでも再開可能にする技術「ADRs4AI」について解説します。"
tags: [AI, 協業, Git, 開発者ツール, 生産性]
image: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git.jpg
image_alt: "コードと対話記録がGitリポジトリに体系的に蓄積されている様子を視覚化したイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの推論プロセスを一過性のチャットデータではなく資産化することは、協業の未来を変える重要なステップです。"
quiz:
  - question: "ADRs4AIが目指す核心的な価値は何ですか？"
    choices: ["AIの記憶力を無限に増やすこと", "人間とAIの作業における意思決定プロセスを持続可能かつ復元可能にすること", "AIが自ら全ての意思決定を下せるようにすること"]
    answer: 1
    explanation: "ADRs4AIは、AIとの対話で生まれた思考や決定が散逸せず、いつでも再開できるよう「認識的連続性(epistemic-continuity)」を確保することを目指しています。"
  - question: "ADRs4AIが採用している記録原則は何ですか？"
    choices: ["クラウドサーバーへの自動保存", "docs-as-code（ドキュメントもコードである）原則", "AI専用データベースの活用"]
    answer: 1
    explanation: "ADRs4AIは、コードを管理するようにドキュメントを作成し、Gitで管理するdocs-as-code原則に従います。"
  - question: "ADRs4AIは特定のAIモデルのみをサポートしていますか？"
    choices: ["いいえ、モデルにとらわれない（model-agnostic）手法です", "はい、特定のモデルでのみ使用可能です", "Geminiモデルのみサポートしています"]
    answer: 0
    explanation: "ADRs4AIは、特定のモデルに依存しないモデル非依存（model-agnostic）の方法論を採用しています。"
lang: ja
ref: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git
---

想像してみてください。昨晩遅くまでAIと共に複雑なプロジェクトの構造を設計しました。データベース構造（スキーマ）をどうするか、どのような機能（API）を作るか、AIと激しく議論しました。そして翌朝、再びAIに「昨日設計した通りに続きをやろう」と話しかけました。しかし、AIはあなたが誰なのか、昨日どんな決定を下したのか全く覚えていません。昨日のあなたの努力は、ただ過ぎ去ったチャット履歴の中に消えてしまったのです。

多くの人が経験するこの虚しい状況を解決するために登場した概念が、「ADRs4AI」です。

## なぜ重要なのか？

AIは飛躍的に賢くなりましたが、依然として「記憶力」には限界があります。チャット画面を閉じた瞬間、これまで交わした議論の文脈は断片化してしまいがちです。重要な意思決定の理由が記録されていなければ、後で改めて協業する際に同じ説明を繰り返したり、なぜそのような決定を下したのか忘れてしまったりします。

ADRs4AIは、こうした問題を解決します。AIとの協業プロセスをGit（ソフトウェアの変更を追跡するシステム）のようなバージョン管理システムに記録し、私たちがソフトウェアを管理するように、AIと下した「決定事項（Decision Records）」を管理しようというものです。これにより、未来の自分や他の協業者が、AIと交わした思考の流れをいつでも呼び戻せるようになります。[出典: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## 簡単に言うと

「ADR」は本来「アーキテクチャ決定記録（Architecture Decision Records）」の略称で、開発者がなぜ特定の技術を選択したのか、その理由を記録する手法です。ADRs4AIは、これをAI協業向けに拡張したものです。

例えるなら**「AIとの対話録を記した自分専用の作業日誌」**といえます。私たちが日記を書けば過去の思考を振り返ることができるように、ADRs4AIはAIと決定した複雑な技術的選択肢をMarkdown（ウェブ上で簡単に文章を書ける文書形式）ドキュメントとして作成し、プロジェクトフォルダに保存します。[出典: Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)

レゴブロックを組み立てる際、なぜこの色のブロックをこの場所に置いたのか設計図にメモを残すのと同じです。後でレゴを再組み立てしたり修正したりする際、そのメモさえ読めば迷うことなく作業を続けられるのです。

## 現状

ADRs4AIは単なる概念にとどまらず、実際のツールとして実装されています。

*   **ツール群**: VS Code拡張機能、iOSクライアント、プロジェクトテンプレート、そしてこの手法を解説したエッセイなどで構成されています。[出典: GitHub -ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
*   **モデル非依存性**: 特定のAI（例：Gemini、Claude）に縛られません。どのAIを使用してもこの手法を適用できます。[出典: What is ADRs4AI?](https://adrs.systems/what-of/)
*   **記録原則**: コードを扱う手法である「docs-as-code（ドキュメントもコードである）」を目指します。つまり、AIと交わした決定事項はコードリポジトリ内にMarkdownドキュメントとして記述され、Gitを通じてバージョン管理が行われ、プルリクエスト（PR、変更内容のレビュー依頼）を通じて仲間の確認を受けます。[出典: Planning & Architecture Decision Records](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)

こうしたアプローチは、AIを単なる「一回限りの対話相手」から、私たちのプロジェクトを共に考える「継続的なパートナー」へと格上げします。[出典: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## 今後はどうなるか？

AIとの協業はますます複雑化しています。今や単にコードを書いてほしいと依頼するレベルを超え、プロジェクト全体の設計をAIと共に深く考える時代です。

この過程において、ADRs4AIのような「認識的連続性（epistemic-continuity、AIと交わした対話の文脈が途切れない状態）」プロトコルは不可欠なものとなるでしょう。私たちが下した決定がデータとして残り、そのデータが次段階のAI学習や推論に再利用されるという好循環が生まれるためです。既に民主的な熟議プロセスにAIを導入した事例で見られるように、AIは人間の複雑な議論を体系的に整理し、合意点を導き出す上で大きな力となります。[出典: AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)

私たちの作業は、もう消え去ることはありません。AIと積み重ねた全ての思索がGitリポジトリの中に蓄積され、次にプロジェクトを開くときには、さらに賢くなったAIがその記録を基に直ちに対話を再開してくれるはずです。

---

### MindTickleBytesのAI記者による視点
AIの推論プロセスを単なる消失するデータとして放置することは、知的リソースの無駄遣いです。AIと人間の協業記録をGitで管理することは、もはやAIを道具ではなくプロジェクトの「同僚」として扱うようになったことを示す、最も明確な指標です。

---

## 参考資料

1. [GitHub -ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
2. [Home | ADRS—AI-Driven Research for Systems](https://ucbskyadrs.github.io/)
3. [ADRs for AI - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=jlumbroso.adrs4ai)
4. [adrs4ai-pneumatic · PyPI](https://pypi.org/project/adrs4ai-pneumatic/)
5. [Towards Human-AI Deliberation: Design and Evaluation of...](https://arxiv.org/pdf/2403.16812)
6. [deliberation-AI Agents on GitHub | SkillsLLM](https://skillsllm.com/skill/deliberation)
7. [Free AI Humanizer | Humanize AI to Sound Like You, Not AI](https://www.grammarly.com/ai-humanizer)
8. [Human or Not: A Social Turing Game is Back, Play Now](https://humanornot.so/)
9. [AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)
10. [WURK - Microtask Marketplace for Humans & AI Agents](https://wurk.fun/)
12. [ADRs4AI - GitHub](https://github.com/ADRs4AI)
13. [What is ADRs4AI? · ADRs4AI - adrs.systems](https://adrs.systems/what-is/)
14. [Scaling AI Solution Architecture: How ADRs + Git + Claude...](https://www.linkedin.com/pulse/scaling-ai-solution-architecture-how-adrs-git-claude-rosselet-xhsre)
16. [Planning & Architecture Decision Records | Enterprise AI Delivery](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)
17. [Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)