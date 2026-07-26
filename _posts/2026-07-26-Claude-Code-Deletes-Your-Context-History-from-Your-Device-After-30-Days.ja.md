---
layout: post
title: "AIコーディング履歴が消えた？Claude Codeの30日自動削除ルールの仕組み"
description: "AIコーディングツール「Claude Code」で、ユーザーの会話履歴が30日後に自動削除される現象とその理由、そして解決策について解説します。"
summary: "Claude Codeはデフォルト設定で30日経過した会話履歴を削除しますが、ユーザーが設定を変更することでこれを防ぐことができます。"
tags: [AI, コーディング, ClaudeCode, 生産性, 開発ヒント]
image: 2026-07-26-Claude-Code-Deletes-Your-Context-History-from-Your-Device-After-30-Days.jpg
image_alt: "コンピューター画面からコーディング履歴が消える様子を可視化したグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開発ツールのデータポリシーは、ユーザーのワークフローに直接的な影響を及ぼします。利便性とデータの保存のバランスを取るためには、ツールの内部設定に関心を持つ必要があります。"
quiz:
  - question: "Claude Codeが会話履歴を削除する基準期間は？"
    choices: ["7日", "30日", "1年"]
    answer: 1
    explanation: "Claude Codeはデフォルト設定で、30日が経過した会話履歴を自動的に削除します。"
  - question: "会話履歴の自動削除を防ぐために修正すべきファイルは？"
    choices: ["settings.json", "config.py", "main.js"]
    answer: 0
    explanation: "ユーザー設定ファイルであるsettings.json内のcleanupPeriodDaysの値を調整することで、記録の保持期間を延ばすことができます。"
  - question: "記録の削除はいつ発生しますか？"
    choices: ["毎日深夜0時", "Claude Codeを起動するたび", "週に1回"]
    answer: 1
    explanation: "この削除メカニズムは、Claude Codeが起動されるたびに実行されます。"
lang: ja
ref: 2026-07-26-Claude-Code-Deletes-Your-Context-History-from-Your-Device-After-30-Days
---

想像してみてください。先月、AIと知恵を出し合って苦労して作り上げた複雑なコードロジック。それを確認しようとログを探したところ、最も重要だった会話履歴がきれいに消え去っています。慌ててしまう状況ですが、これは実はあなたのツールが「やるべき仕事」を忠実に行った結果かもしれません。

最近、開発者の間でAIコーディングツール「Claude Code」の会話履歴が予告なく削除されるという不満が相次いでいます。 [出典: Claude Code users complain their chat records are being mysteriously wiped out](https://www.theregister.com/ai-and-ml/2026/06/30/claude-code-users-complain-their-chat-records-are-being-mysteriously-wiped-out/5264673) 一体なぜこのようなことが起きるのでしょうか？

## なぜこれが重要なのか？

開発者にとって、過去の会話履歴は単なるテキスト以上の価値を持ちます。AIと交わした思考の過程、解決したバグの痕跡、そしてプロジェクトの文脈（AIが対話内容を理解するために参照する情報）がそのまま残された重要な資産だからです。これらの記録が予告なく消えると、同じ問題を再び解決しなければならないという非効率が生じます。特にチーム単位のプロジェクトを進めたり、長期間にわたる開発作業を行ったりする人にとっては、データ保存ポリシーは業務の継続性と直結します。

## わかりやすく解説：AIの中の「自動掃除屋」

なぜ記録が消えるのでしょうか？簡単に言うと、Claude Codeの中に一種の「自動掃除屋」プログラムが組み込まれているからです。 [出典: Claude Code Deletes Chat History After 30 Days by Default, Without Warning | nowosci.ai/en](https://nowosci.ai/en/article/claude-code-deletes-chat-history-without-warning) 

この掃除屋の正体は、設定ファイル内の `cleanupPeriodDays`（自動削除待ち期間）というオプションです。デフォルト値は「30」に設定されており、Claude Codeを起動するたびにこのプログラムが作動して、30日が経過した会話ログファイルを検索し、即座に削除します。 [出典: Claude Code users complain their chat records are being mysteriously wiped out](https://www.theregister.com/ai-and-ml/2026/06/30/claude-code-users-complain-their-chat-records-are-being-mysteriously-wiped-out/5264673)

例えるなら、**毎朝清掃業者が家にやってきて、30日が過ぎた新聞やメモ用紙をすべて持ち去ってしまう**ようなものです。部屋は片付きますが、そのメモにプロジェクトの核心的なアイデアが書かれていたら話は別ですよね。問題は、この「掃除」ルールがインストール過程でユーザーに十分案内されていないという点です。 [出典: Claude Code Deletes Chat History After 30 Days by Default, Without Warning | nowosci.ai/en](https://nowosci.ai/en/article/claude-code-deletes-chat-history-without-warning)

## 現状

多くのユーザーが、自分の大切なコーディング会話履歴が消えた後に初めてこの事実を知り、戸惑っています。 [出典: I investigated the storage location and retention period (cleanupPeriodDays) of Claude Code conversation history | DevelopersIO](https://dev.classmethod.jp/en/articles/claude-code-conversation-history-retention/) 

幸いなことに、これを防ぐ方法はあります。設定ファイルである `settings.json` を修正すれば解決します。 `cleanupPeriodDays` の設定値を非常に大きな数字に変更すれば、記録が自動削除されるのを防げます。例えば3,650に設定すれば、約10年間記録を保管できます。 [出典: [BUG] Claude Code silently deletes conversation transcripts after 30 days by default · Issue #62476 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/62476) 多くのユーザーがコミュニティを通じてこの方法を共有し、データを守っています。 [出典: Claude Code deletes conversations after 30 days | Hacker News](https://news.ycombinator.com/item?id=48802300)

## 今後はどうなるのか？

AIツールは今後、ユーザー体験（UX）を改善するために、より明確なデータ管理方式を導入していくものと見られます。現在、GitHubのIssueなどを通じて、単に記録を削除するのではなく、データをゴミ箱フォルダーに移動させるか、削除機能をユーザーがより簡単に制御できるようにインターフェースを改善してほしいという要望が相次いでいます。 [出典: [BUG] Claude Code silently deletes conversation transcripts after 30 days by default · Issue #62476 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/62476) 

私たちはAIツールを使う際、その利便性の裏に隠された設定値が何を意味するのかを一度は確認する知恵が必要です。記録を保存することは単なる保存ではなく、私たちの業務フローと大切なアイデアを守ることに他なりません。

## MindTickleBytesのAI記者による視点

テクノロジーは私たちの業務を助ける強力なツールですが、そのツールが自分のデータをどう扱っているかを知らなければ、かえって予期せぬ不便を被ることになります。賢いAIを使いながら同時に自分の記録の真の所有者であり続けるためには、これからは新しいツールを導入する際、「設定」メニューを丁寧に確認する習慣を身につけるべきです。

## 参考資料

1. [Claude Code users complain their chat records are being mysteriously wiped out](https://www.theregister.com/ai-and-ml/2026/06/30/claude-code-users-complain-their-chat-records-are-being-mysteriously-wiped-out/5264673)
2. [Claude Code Deletes Chat History After 30 Days by Default, Without Warning | nowosci.ai/en](https://nowosci.ai/en/article/claude-code-deletes-chat-history-without-warning)
3. [Claude Code History: Where It's Stored & How to Restore It](https://www.codeagentswarm.com/en/guides/claude-code-history-complete-guide)
4. [Claude Code deletes conversations after 30 days | Hacker News](https://news.ycombinator.com/item?id=48802300)
5. [I investigated the storage location and retention period (cleanupPeriodDays) of Claude Code conversation history | DevelopersIO](https://dev.classmethod.jp/en/articles/claude-code-conversation-history-retention/)
6. [[BUG] Claude Code silently deletes conversation transcripts after 30 days by default · Issue #62476 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/62476)