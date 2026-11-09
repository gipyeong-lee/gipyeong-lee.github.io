---
layout: post
title: "エクセルがAIのターミナルに？「Recalc」で体験するエージェント時代"
description: "各セルでClaude CodeやCodexを実行し、AIエージェントと協働できる新しいオープンソースのスプレッドシート「Recalc」をご紹介します。"
summary: "Recalcは、スプレッドシートの各セルをAIターミナルとして活用し、複数のエージェントがデータを共有しながら複雑なワークフローを処理できるようにするツールです。"
tags: [AI, エージェント, スプレッドシート, Recalc, 生産性]
image: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals.jpg
image_alt: "複数のAIエージェントセッションがスプレッドシートのグリッド内で同時に動作している画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "複雑なコーディングエージェントのワークフローを、馴染み深い格子状の形式で管理するのは非常に直感的なアプローチです。AIと人間の協働方式を一歩進化させる興味深い試みです。"
quiz:
  - question: "Recalcスプレッドシートの各セルで行える操作は何ですか？"
    choices: ["値の保存", "数式計算", "ターミナルコマンドおよびAIエージェントの実行", "上記すべてが可能"]
    answer: 3
    explanation: "Recalcは、すべてのセルが単なる値や数式だけでなく、ターミナルコマンド、Claude Code、Codexセッションを直接実行できるように設計されています。"
  - question: "Recalcの利点として挙げられているAIエージェントの操作方法は？"
    choices: ["チャットを中断せずにセルを編集してエージェントを制御", "エージェントが任意に選択するまで待機", "専用のプログラミング言語を習得"]
    answer: 0
    explanation: "Recalcでは、ユーザーがチャットの流れを止めることなくスプレッドシートのセルを編集することで、エージェントの動作を直接操作できます。"
  - question: "Recalcが各エージェントセッション間の通信に使用する技術は？"
    choices: ["ブロックチェーン", "MCP(Model Context Protocol)サーバー", "専用クラウドAPI"]
    answer: 1
    explanation: "RecalcはMCPサーバーを活用し、異なるセルやセッション間でデータを共有・通信できるようにしています。"
lang: ja
ref: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals
---

想像してみてください。いつものようにExcelやGoogleスプレッドシートを開きます。ところが、表の各マス（セル）に単純な数値を入力する代わりに、AIに対して「このデータを分析してレポートの草案を書いて」と命令を下します。隣のマスでは、別のAIエージェント（ユーザーの指示を受けて自律的に作業を行うAI）がリアルタイムでコードを実行し、必要な情報を収集しています。まるで数人の優秀なAI秘書が一冊の帳簿に集まり、一緒に会議をしているかのようです。

2026年11月8日、GitHubを通じて公開されたオープンソースのスプレッドシートツール**「Recalc」**が、まさにこのような未来を現実にしようとしています [Source 11]。

### なぜこれが重要なのか？

これまでAIエージェントを扱う際は、チャット画面という狭い空間に閉じ込められているのが一般的でした。エージェントが複雑なタスクを実行する際、他のセッションとデータをやり取りするには、ファイルをいちいち保存したり、複雑なプログラミングインターフェース（API）を個別に連携させたりする手間が必要でした。

Recalcは、私たちが最も使い慣れている「スプレッドシート」をAI協働のハブへと変貌させます。個々のエージェントセッションがスプレッドシートという共通のグリッド内でデータを共有・通信できるようになることで、AIの評価や複雑な業務プロセス（ワークフロー）をより直感的に管理できるようになったのです [Source 1, Source 11]。

### 分かりやすく言えば

簡単に言うと、従来のAIエージェント作業が「個室で一人悩む研究員」と対話するようなものだったとすれば、Recalcは「複数の研究員が一枚の大きな設計図の上に集まって一緒に絵を描く環境」を提供するようなものです。

*   **データが流れる通路:** Excelのセルは単なる数字を入れるマスではありません。それぞれのセルが一つの小さなターミナル（コマンド入力窓）であり、Claude Code（AnthropicのAIコーディングエージェント）やCodexのようなAIエージェントが常駐する独立した部屋になります [Source 10, Source 13]。
*   **データ共有:** セル同士は互いに繋がっています。AセルでAIが実行した結果を、Bセルにいる別のAIがすぐに参照して使うことができます。これは**MCP（Model Context Protocol：AIモデルが外部データや環境と通信するための規格）**という技術によって実現されており、この規格がアプリ全体を有機的に繋ぐ役割を果たしています [Source 1, Source 11]。

チャット画面で長々と説明する必要はなく、表のマスを一つ書き換えるだけで、AIエージェントの動作を即座に修正・指示できるのです [Source 10]。

### 現在の状況

現在、Recalcは誰でも参加可能なオープンソースプロジェクトとして開発が進められています。主な特徴は以下の通りです。

*   **現場でのテスト:** 開発者は自身のスタートアップにおいて、実際のAI性能評価（ベンチマーク）を行うためにこのツールを作成しました。例えば、AIが米国食品医薬品局（FDA）への提出書類を分析し、承認の可否をどれほど正確に予測できるかをテストするデモ事例があります [Source 1]。
*   **動作環境:** 現在はmacOS環境で円滑に動作するように設計されています。Linuxでも実行可能ですが十分なテストは行われておらず、Windowsは未対応です [Source 1]。
*   **セキュリティ:** Claude Codeのようなツールと連携する際、これらは一般的にユーザーのコンピューターのローカル環境で実行されます。別途バックエンドサーバーを経由せずモデルと直接通信するため、セキュリティを考慮して設計されています [Source 3]。

### 今後の展望

Recalcは、AIと人間が協働する方式を根本から変える可能性を秘めています。今後はデータアナリストだけでなく、エンジニアやプランナーまでがスプレッドシートを使って数十のAIエージェントを調整する時代が来るかもしれません。Windowsへの対応をはじめ、より多様な環境で簡単に利用できるようになれば、単純な反復作業を超えて、企業向けの複雑な業務管理ツールへと成長することが期待されています [Source 1]。

### MindTickleBytesのAI記者視点

「ツールが馴染み深いものであるほど、AIの能力はより速く拡張される」という事実を如実に示す事例です。複雑なコマンドを新しく覚えるよりも、私たちが日常的に使っている表計算の形式でAIを操作する方がはるかに直感的であるという点が、Recalcの最大の武器です。複雑なAIエージェント時代は、予想以上に私たちの身近にまで迫っています。

## 参考資料

1. [Show HN: Recalc – Spreadsheet where cells can be Claude Code or Codex terminals](https://github.com/sshah03/recalc)
2. [ClaudeCode by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)
3. [Recalc - Spreadsheet with Claude Code · Hacker News | Zeli](https://zeli.app/story/50413970)
4. [Recalc Spreadsheet Lets Cells Run Claude Code or Codex](https://emergent.sh/news/recalc-spreadsheet-lets-cells-run-claude-code)
5. [recalc/demos/done-means-green/repo/.codex at main - GitHub](https://github.com/sshah03/recalc/tree/main/demos/done-means-green/repo/.codex)
6. [recalc/CLAUDE.md at main · sshah03/recalc · GitHub](https://github.com/sshah03/recalc/blob/main/CLAUDE.md)