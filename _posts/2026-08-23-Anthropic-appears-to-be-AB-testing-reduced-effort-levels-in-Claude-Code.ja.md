---
layout: post
title: "私のAIが突然バカになった？Claude Codeの隠された実験の話"
description: "AIモデルの性能が突然落ちたと感じたことはありませんか？AnthropicのClaude Codeで発生した「努力レベル」の調整と、ユーザーが経験した不便さを通じて、AIの透明性問題を考察します。"
summary: "Anthropicはコスト削減と速度向上のため、Claude Codeの基本推論強度を密かに下げましたが、品質低下に対するユーザーからの不満が殺到し、これを復旧させました。"
tags: [AI, Anthropic, ClaudeCode, 人工知能, 技術倫理]
image: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code.jpg
image_alt: "Claude Codeのインターフェース画面と推論プロセスを示すグラフィック要素"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企業が技術を最適化する際は、ユーザーとの信頼関係のために変化の理由を透明に公開すべきです。実験的機能は常にユーザーの選択権の保証が優先されるべきでしょう。"
quiz:
  - question: "AnthropicがClaude Codeの基本推論レベルを下げた主な理由は何ですか？"
    choices: ["モデルのセキュリティ強化", "コスト削減および応答速度の向上", "より多くのデータを学習するため"]
    answer: 1
    explanation: "Anthropicは、ユーザーからのトークン消費量が多すぎるというフィードバックを反映し、応答速度の改善とトークン消費の削減を図ろうとしました。"
  - question: "Claude Codeにおいて「努力レベル（effort level）」が高いとどのようなことが起こりますか？"
    choices: ["より速く応答する", "思考の深さが増し、複雑な問題をより良く解決する", "無条件により多くのコストが発生する"]
    answer: 1
    explanation: "努力レベルは思考の深さと関連しており、より複雑な問題を解決する能力を向上させます。"
  - question: "Anthropicは最近発生した品質低下問題をどのように解決しましたか？"
    choices: ["ユーザーにより高い料金を課した", "4月7日に以前の水準に復旧させた", "AIモデルを完全に交換した"]
    answer: 1
    explanation: "Anthropicは当該措置が誤った妥協点であったことを認め、2026年4月7日に本来の高い推論水準へと設定を復旧させました。"
lang: ja
ref: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code
---

想像してみてください。毎日仕事を手伝ってくれる賢いAIアシスタントがいます。昨日までは複雑なコーディング問題も難なく解決してくれていたのに、今朝、突然あまりに単純な回答しか出さなかったり、重要な文脈を見落とし始めたりしたら、どれほど当惑することでしょうか。最近、人工知能企業Anthropicの開発者向けコーディングツール「Claude Code」のユーザーの間で、まさにこのような出来事が発生しました。

### なぜこれが重要なのか？

今回の事件は、AIを専門ツールとして活用する人々にとって大きな衝撃となりました。単にモデルが少し遅くなったという問題ではありませんでした。ユーザーが知らないうちにAIの「脳の回転」方式が強制的に変更され、その結果、業務生産性に即座な打撃が生じたためです。これは、私たちが毎日使用するAIサービスが、企業の内部ポリシーによっていつでも予告なしに性能が変わる可能性があることを示す、重要な事例です。

### わかりやすく解説：AIの「努力レベル」とは？

Claude Codeには**「努力レベル（Effort Level、AIが問題を解決するためにどれほど深く考えるかを決定する設定）」**という機能があります。

簡単に言えば、この努力レベルは学生が試験問題を解く際に費やす努力と似ています。「低い努力」レベルは問題を大まかに見てすぐに答えを書くことであり、「高い努力」レベルはすべての文章を注意深く読み、検討し、深く悩むことです。[出典: Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)

例えるなら、ベテラン料理人が丹精を込めて料理していたのに、突然、材料費と時間を惜しむためにインスタント食品レベルに調理方式を変えたようなものです。消費者側からすれば、当然ながら味の違いを感じずにはいられません。

Anthropicは2026年2月から3月の間に、何の告知もなしにClaude Codeの基本努力レベルを「高」から「中」に下げました。[出典: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/) Anthropic関係者の説明によると、これはユーザーから「トークン（AIが使用する言語単位）の消費が多すぎる」というフィードバックを反映し、応答速度を改善してコストを削減しようという意図によるものでした。[出典: Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)

しかし結果は悲惨でした。この調整により、AIの思考の深さが実に73%も減少し、複雑なプログラミング作業を行っていたユーザーたちは、性能が急激に低下したことを体感することになったのです。[出典: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)

### 現在の状況：相次ぐアップデートと混乱

性能が低下した原因は、大きく3つのアップデートが重なったためであることが判明しました。[出典: Anthropic Claude Code Quality Drop](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026) 特に3月には一部のユーザーを対象にしたA/Bテスト（2つ以上の案を無作為に表示して成果を比較する実験）が行われましたが、この過程でコード計画を40行に制限したり、必要な文脈情報を削除してしまったりするなどの問題が発生し、ユーザーからの反発を買いました。[出典: Anthropic A/B Tested Claude Code Plan Mode](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)

結局、Anthropicは自分たちの決定が「誤った妥協点」であったことを認め、4月7日に設定を以前の水準に復旧させました。[出典: Why Is Claude Code Slow?](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)

### 今後はどうなるのか？

今回の事件は、AIツールの透明性に対する強力な警告となりました。専門家たちは、プロフェッショナル向けのAIツールを提供する企業は、実験的な変化を適用する際に必ずユーザーの同意を得るか、最低限、事前告知を行うべきだと主張しています。[出典: Mike Ramos Criticizes Anthropic](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code) 今後、ユーザーはAIモデルが提供する「努力レベル」を自ら選択・調整できる環境をより強く要求することになるでしょう。

## MindTickleBytesのAI記者の視点

AIの性能は単なる数値ではなく、ユーザーの信頼と直結します。技術最適化の名の下に行われた「静かな変化」がどれほど大きな生産性低下を招きうるかを示した今回の事例は、AI企業が透明なコミュニケーションをなぜ最優先順位に置くべきなのかをよく物語っています。今後、より多くのユーザーがAIを業務の中核ツールとして活用するにつれ、このような政策的透明性は技術力と同じくらい重要な企業の競争力となるでしょう。

## 参考資料

1. [Claude Code's Thinking Depth Dropped 73% — Anthropic Admits](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)
2. [Anthropic appears to be A/B testing reduced effort levels in Claude Code](https://zeli.app/zh/story/49401549)
3. [Anthropic Claude Code Quality Drop: What Actually Happened](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026)
4. [Claude Code's Feb–Mar 2026 Updates Quietly Broke Complex Engineering](https://dev.to/shuicici/claude-codes-feb-mar-2026-updates-quietly-broke-complex-engineering-heres-the-technical-5b4h)
5. [Anthropic A/B Tested Claude Code Plan Mode Without Telling Users](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)
6. [An update on recent Claude Code quality reports \ Anthropic](https://www.anthropic.com/engineering/april-23-postmortem)
7. [Mike Ramos Criticizes Anthropic for Undisclosed A/B Test](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code)
8. [Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
9. [Why Is Claude Code Slow? Official Causes and Developer Fixes](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)
10. [Anthropic admits it dumbed down Claude with 'upgrades'](https://www.theregister.com/software/2026/04/24/anthropic-admits-it-dumbed-down-claude-with-upgrades/5228105)
11. [Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)
12. [Mystery solved: Anthropic reveals changes to Claude's harnesses](https://venturebeat.com/technology/mystery-solved-anthropic-reveals-changes-to-claudes-harnesses-and-operating-instructions-likely-caused-degradation)
13. [Anthropic is facing a wave of user backlash over reports of performance issues](https://finance.yahoo.com/sectors/technology/articles/anthropic-facing-wave-user-backlash-091348318.html)
14. [Anthropic explains Claude Code’s recent performance](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?ref=biztoc.com)