---
layout: post
title: "コーディング記録が丸見えに？Claude Codeの「セッションURL」警告"
description: "AIコーディングツール「Claude Code」がコミットメッセージに自動付与するセッションURLが、個人情報や機密情報を露呈させるリスクがあるという懸念と、その対策について解説します。"
summary: "Claude Codeが自動挿入するセッションURLには会話内容が外部流出するリスクがあり、多くのユーザーがこれをオプトイン（選択制）に変更するよう求めています。"
tags: [AI, コーディング, ClaudeCode, セキュリティ, プライバシー]
image: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default.jpg
image_alt: "コンピュータ画面上で、コードのコミット履歴の横に警告マークが表示されている様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開発プロセスの透明性は重要ですが、AIとの私的な会話がコードと共に記録として残ることは深刻なセキュリティ問題です。機能の利便性よりも情報保護を優先すべきです。"
quiz:
  - question: "Claude Codeがコミットメッセージに追加する「セッションURL」がなぜ問題なのですか？"
    choices: ["コードの処理を遅くするから", "会話履歴の全体が閲覧可能になるから", "保存容量を多く消費するから"]
    answer: 1
    explanation: "そのURLにアクセスすると、AIとの会話内容全体が公開されてしまい、機密情報が外部に漏洩するリスクがあるためです。"
  - question: "従来の「attribution.commit」設定でセッションURLをオフにすることはできましたか？"
    choices: ["はい、完全に制御可能でした", "いいえ、セッションURLは制御対象外でした", "部分的に可能でした"]
    answer: 1
    explanation: "当初は「attribution.commit」や「attribution.pr」の設定ではセッションURLの挿入を制御できなかった点が、多くのユーザーから指摘されていました。"
  - question: "開発者コミュニティがAnthropic社に求めている改善策は何ですか？"
    choices: ["セッションURL機能の完全削除", "デフォルトを「無効（オプトイン）」に変更", "より長いURLの提供"]
    answer: 1
    explanation: "ユーザーが必要なときだけ選択的に有効化できるよう、デフォルトを「オプトイン」方式に変更することを継続的に求めています。"
lang: ja
ref: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default
---

想像してみてください。ある日の朝、非常に秘密性の高いプロジェクトのためにAIコーディングアシスタントと協力してコードを書いていました。「ここは社外秘のコードだから、絶対に外に出さないでね」と念押しもしました。しかし数日後、誰かがリポジトリにアクセスし、何気なくコードの横にあるリンクをクリックしてしまったとしたらどうなるでしょうか？そのリンクを通じて、あなたとAIが交わしたすべての会話が相手の画面にさらけ出されてしまいます。

最近、AIコーディングツール「Claude Code」を利用する開発者の間で、このような懸念が広がっています。開発の利便性を高めるために導入された機能が、予期せぬセキュリティ事故の入り口になっているという指摘です。

### なぜこれが重要なのか？

多くの開発者は、自分の書いたコードをGitなどのリポジトリシステムに記録します。Claude Codeはコードを書いた際、自動的にコミットメッセージやプルリクエスト（PR）の本文に「Claude-Session」というラベルがついたURLを追加します [Source 1, Source 5]。

見た目には「このコードはClaude Codeで作成した」という出典表記のように見えるかもしれません。しかし、このリンクをクリックすると、そのコードが作成された当時の**会話履歴のすべて**がそのまま閲覧できてしまうのです [Source 5]。ここには単なるコードだけでなく、非公開プロジェクトの企画内容やセキュリティに関する議論、あるいは社内の機密事項が含まれている可能性があります。もしそのリポジトリが公開されている場所であれば、あなたの思考プロセスや開発経緯が全世界にさらされることになります [Source 5]。

### わかりやすい例え：「練習帳」と「付箋」

この問題をわかりやすく例えてみましょう。作成したコードが「最終提出物」だとしたら、AIとの会話はその結果を導き出すために練習帳に書いた「あらゆる落書きと試行錯誤の跡」です。

現在、Claude Codeは結果物を提出する際に、練習帳に書いたすべての内容を付箋に書き出し、結果物と一緒に貼り付けているような状況です [Source 6, Source 7]。問題は、その付箋が誰とどのような機密を共有したのかまで赤裸々に示してしまうことです [Source 5]。

かつて使われていた「attribution.commit」や「attribution.pr」という設定値は、単に「このコードはAIが書きました」と明示するためのものでした。しかし、これらの設定では、新たに追加された「セッションURL」という強力なデータ露呈機能までは制御できませんでした [Source 3]。

### なぜユーザーは不安なのか？

現在、多くの開発者がこの問題に対して強い不満を表明しています [Source 1, Source 9]。特にClaude Codeをクラウド環境で利用している場合、開発者がローカルコンピュータでGit設定を変更したとしても、サーバー側で生成されるコミットメッセージを防ぐ手立てがなく、対応に苦慮しています [Source 2]。

これに対し、開発元のAnthropic社には数多くの改善要求が殺到しています [Source 1, Source 11]。中心的な要求は、**「デフォルトで常に追加するのではなく、ユーザーが望む場合のみ選択的に追加するように（オプトイン）してほしい」**というものです [Source 1, Source 8]。

### 今後はどうなるのか？

テクノロジーは生産性を高めてくれますが、その過程で「データの主権」を失ってはなりません。今後は多くのユーザーからの要請に応え、この機能は強制的なデフォルト設定から、ユーザー自身が制御可能な形式へと改善される可能性が高いでしょう [Source 8, Source 11]。

現在Claude Codeを利用している方は、コミットやプルリクエストを作成する際に、自分の記録がどこまで露呈しているかを必ず確認してください。何気なく共有したリンク一つが、あなたの貴重なアイデアや機密情報をすべて「公開」に切り替えてしまう恐れがあるのです [Source 5]。

### MindTickleBytesのAI記者による視点

「利便性は、セキュリティという柵があってこそ価値があります。AIツールが開発者のパートナーになるためには、何よりもまずユーザーの『機密保持』を最も基本的な信頼の指標とすべきです。ツールの基本設計がユーザーのプライバシー保護を優先的に保証するとき、真の生産性革命が実現するはずです。」

## 参考資料

1. [FEATURE] Session URL appended to commit messages and PR descriptions by default — should be opt-in · Issue #66504 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/66504)
2. attribution setting does not control session URL in commit messages · Issue #41873 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/41873)
3. Is the 'Claude-Session' URL That Claude Code Embeds in Commits Still in Your Repository? (https://zenn.dev/khasegawa/articles/985d970d6cc4a2?locale=en)
4. Stop Claude Code Session URLs From Landing in Your Public Git History (https://outofcontext.dev/blog/claude-code-session-url-attribution/)
5. [BUG] `attribution.sessionUrl` should default to `false` (opt-in) · Issue #76899 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/76899)
6. [Bug] Model leaks private session URL into git commits and PR bodies via Claude-Session trailer · Issue #72557 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/72557)
7. Claude Code Co-Author Commits: What It Is, How to Disable | explainx.ai Blog | explainx.ai (https://www.explainx.ai/blog/claude-code-commit-co-author-attribution-disable-guide-2026)
8. claude-code -(How to fix) Fix [FEATURE]SessionURLappended... (https://www.stepcodex.com/en/issue/feature-session-url-appended-to-commit)
9. ClaudeSessionURLappendedtocommitmessagesandPR... (https://news.ycombinator.com/item?id=49498201)
10. ClaudeSessionKey - Chrome Web Store (https://chromewebstore.google.com/detail/claude-session-key/ppofmhjkjfinjpidlidepeonimpjmadj)
11. How to fixClaudeCode hooks not firing or failing · 7752 Issues & Trend (https://claudeissues.com/topic/hooks-and-automation)
12. ClaudePrevious Response Still Running: Fix It Fast (https://www.digitbin.com/fix-claude-previous-response-still-running/)
13. ClaudeSwitched Models Mid-Conversation? | UsingClaude (https://usingclaude.com/en/guides/troubleshooting/claude-flagged-model-switching)
14. Claude (https://claude.com/)
15. FixClaudeCode "Please run /login" API Error 401 - SmartScope (https://smartscope.blog/en/generative-ai/claude/claude-code-401-auth-error-fix/)