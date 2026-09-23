---
layout: post
title: "Claude Codeの新しいAGENTS.md対応、なぜ私のプロジェクトでは動かないのか？"
description: "最新のClaude CodeでAGENTS.mdファイルを設定したのにAIが無視するなら？その理由と解決策を解説します。"
summary: "Claude Codeバージョン2.1.277からAGENTS.mdがサポートされましたが、特定の環境や設定ではこの機能が動作しない可能性があるため注意が必要です。"
tags: [ClaudeCode, AI, 開発ツール, AGENTS.md]
image: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on.jpg
image_alt: "コーディングツールであるClaude Codeのロゴとドキュメントファイルアイコンが融合した現代的なテクノロジーグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "新しい標準の導入には常に初期の混乱が伴います。現在はCLAUDE.mdを使用するのが最も確実な方法です。"
quiz:
  - question: "Claude CodeにおいてCLAUDE.mdとAGENTS.mdが同時に存在する場合、どちらのファイルが優先されますか？"
    choices: ["AGENTS.md", "CLAUDE.md", "不明"]
    answer: 1
    explanation: "Claude Codeは両方のファイルが存在する場合、従来の方法であるCLAUDE.mdを優先的に読み込み、AGENTS.mdは無視します。"
  - question: "AGENTS.mdのサポートが現在公式に提供されていない環境はどこですか？"
    choices: ["ターミナル", "デスクトップアプリ", "Amazon Bedrock"]
    answer: 2
    explanation: "Amazon Bedrock、Vertex、Foundryなどの環境では、まだAGENTS.md機能がサポートされていません。"
  - question: "AGENTS.mdを使用できない環境で推奨される解決策は何ですか？"
    choices: ["ファイル名を変更する", "内容をCLAUDE.mdへ取り込む（インポートする）", "機能を強制的にオンにする"]
    answer: 1
    explanation: "AGENTS.mdが直接サポートされない場合、そのファイルの内容をCLAUDE.mdに直接含める方法が最も安全です。"
lang: ja
ref: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on
---

想像してみてください。毎朝、AIコーディングツールにプロジェクトのルールを教えるために別の説明ファイルを作成しているとします。ところが、丁寧に書いたそのファイルをAIが完全に無視していたらどうでしょうか？最近、多くの開発者の間でこのような困惑する状況が発生しています。最新アップデートで導入された新しい方式が、期待通りスムーズに動作していないためです。

## なぜこれが重要なのか？

Claude Codeは、開発者のコードベースを読み取り、ファイルを修正し、コマンドまで直接実行する強力な「エージェント型コーディングツール」です([Overview - Claude Code Docs](https://code.claude.com/docs/en/overview))。これまで開発者は、AIにプロジェクトのコーディングルールや注意事項を伝えるために `CLAUDE.md` というファイルを主に使ってきました。

ところが最近、`AGENTS.md` という新しい形式を標準として採用するという発表があり、多くのチームが期待を寄せていました([Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl](https://dev.blog/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/))。この変化の核心は、複数のAIツール間でのルール設定を統一することですが、もしこの機能が正しく動作しなければ、開発者が苦労して作成したルールがAIに伝わらず、見当違いのコードが生成される危険性があります。

## わかりやすく解説

この状況を「新しい言語を学ぶ学生」に例えると理解しやすいでしょう。

*   **従来方式(CLAUDE.md)**: AIが以前から学習し、慣れ親しんだ既存の教科書です。
*   **新しい方式(AGENTS.md)**: AIがより体系的に学べるよう導入された新しい標準参考書です。

しかし、この参考書をAIが読み込むには、特定の「学習モード」がオンになっていなければなりません。残念ながら、現在の多くの使用環境ではこのモードがデフォルトでオフになっているか、AIがそもそも参考書を読み込む権限がない状態です([Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch](https://github.com/anthropics/claude-code/issues/95690))。まるでAIが参考書の存在自体を知らないか、読み込む必要性を感じていないかのようです。特に、使用データ収集（テレメトリ、telemetry）機能がオフになっている場合や、企業向けサービスであるAmazon Bedrockなどを使用している場合、この新しいルールファイルを全く読み込めない現象が発生しています([Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/))。

## どこで問題が発生しているか？

最新アップデートであるClaude Codeバージョン2.1.277から `AGENTS.md` のサポートが追加されました([Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog))。しかし、安定して使用するためには以下のいくつかの制約事項を必ず確認する必要があります。

1.  **既存ファイルの優先順位**: プロジェクトフォルダに `CLAUDE.md` と `AGENTS.md` が同時に存在する場合、AIは慣例通り既存の `CLAUDE.md` を優先的に読み込み、新しい `AGENTS.md` は完全に無視します([Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/))。
2.  **環境的な制約**: Amazon Bedrock、Vertex、Foundryなどの環境では、まだこの機能を公式にはサポートしていません([Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog))。
3.  **内部接続方式**: この機能はAIのコアロジックに統合されたものではなく、内部的に接続された一種の「プラグイン」形式で実装されました([Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md))。そのため、特定の条件が満たされなければツール自体がファイルを認識さえしない「サイレント・フェイラー（無言の失敗）」が発生しやすくなっています。

## 今後どうなるのか？

現時点では `AGENTS.md` だけを信じてルールを任せるには、環境的な制約が大きすぎます。直接サポートされていない環境でルールを共有したい場合は、既存の `CLAUDE.md` 内に該当する内容を直接含める（インポートする）方法が最も安全で確実です([Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes](https://github.com/fmslutions/harness-audit/issues/3))。特に企業内環境で `AGENTS.md` を標準として導入しようとしていたチームは、当面の間注意が必要です([Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html))。今後のアップデートでより多くの環境でサポートが拡大されるまでは、既存の方法を維持することを推奨します。

## MindTickleBytesのAI記者の視点
新しい標準の導入は、開発者の複雑なファイル管理を簡素化しようとする素晴らしい試みです。しかし、技術の格差や環境設定によって「賢いAI」が逆に「目隠し」されてしまう可能性があることを、今回の事例は如実に示しています。新技術を即座に導入するのではなく、既存の安全な方法を並行して用いることが、現時点では業務の継続性を守る最善の戦略です。

## 参考資料
1. [Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)
2. [Claude Code reads AGENTS.md only when telemetry is on - Hacker News](https://news.ycombinator.com/item?id=49814947)
3. [Set custom instructions for opencode.](https://opencode.ai/docs/rules/)
4. [Overview - Claude Code Docs](https://code.claude.com/docs/en/overview)
5. [How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)
6. [Releases · anthropics/claude-code · GitHub](https://github.com/anthropics/claude-code/releases)
7. [AGENTS.md Just Turned One. The Evidence on... - Kernel Talks](https://kerneltalks.com/ai/agents-md-just-turned-one-the-evidence-on-whether-it-works-is-mixed/)
8. [claude-code/mods/agents-md/README.md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md)
9. [1.2: Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes · Issue #3 · fmslutions/harness-audit](https://github.com/fmslutions/harness-audit/issues/3)
10. [[MODEL] Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch · Issue #95690 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/95690)
11. [Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md)
12. [claude-code/mods/agents-md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/mods/agents-md)
13. [Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)
14. [[incorrect-doctrine] "Claude Code reads CLAUDE.md, not AGENTS.md" is no longer true, and our setup command can silently switch a project's AGENTS.md off · Issue #1087 · fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills/issues/1087)
15. [Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)
16. [Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html)
17. [Claude Code Changelog (September 2026)](https://www.gradually.ai/en/changelogs/claude-code/)
18. [Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl - DevOps.com](https://devops.com/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)