---
layout: post
title: "自分のブログにGoogleドキュメントのようなコメントを？AIがコードを直接修正する「Sidenote」"
description: "開発者のブログやドキュメントに対して、Googleドキュメントのように簡単に修正提案を行い、AIがコードの変更点（Git diff）まで自動作成してくれるツール「Sidenote」について解説します。"
summary: "Sidenoteは、ブログ記事を読みながらコメントを残すと、AIがそれを分析し、Gitのコード変更内容に自動変換してくれる革新的なコラボレーションツールです。"
tags: [AI, ブログ, Git, コラボレーション, 生産性]
image: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff.jpg
image_alt: "ブログ記事画面の上にGoogleドキュメントスタイルのコメント欄が浮かび、AIがコードの変更内容を作成している様子をイメージした画像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "複雑なコーディング知識がなくても、文書の意図を伝えるだけでAIが技術的な処理を代行してくれる「意図駆動型（intent-driven）」ワークフローの好例です。"
quiz:
  - question: "Sidenoteを使う主な体験は何と最も似ていますか？"
    choices: ["メールの送信", "Googleドキュメントでの文書レビュー", "ターミナルでのコードコンパイル"]
    answer: 1
    explanation: "Sidenoteは、レンダリングされたMarkdownサイト上で、Googleドキュメントのように直接文章を選択してコメントを書き込み、レビューできる環境を提供します。"
  - question: "ユーザーがSidenoteでコメントをした際、AIエージェントが最終的に行う作業は何ですか？"
    choices: ["自動的にブログへ投稿する", "Git diff（コードの変更内容）を作成する", "コメントに返信する"]
    answer: 1
    explanation: "ユーザーが残したコメント内容に基づき、AIエージェント（ClaudeやCodexなど）が適切なGit diffを生成し、コードの変更を解決します。"
  - question: "Sidenoteの実行環境についての説明として正しいものはどれですか？"
    choices: ["別途サーバーのインストールが必須である", "ローカル優先（Local-first）のWebブラウザベースのツールである", "モバイルアプリでのみ利用可能である"]
    answer: 1
    explanation: "Sidenoteは、ブラウザですぐに動作するローカル優先（Local-first）のアプリケーションです。"
lang: ja
ref: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff
---

想像してみてください。あなたが丁寧に執筆したブログや技術ドキュメントのサイトを誰かが読んでいて、「ここの文章が少し不自然なので、こう変えてはどうでしょうか？」と、まるでGoogleドキュメントのように簡単に意見を残す場面を。さらに驚くべきことに、そのコメントを読んだ人工知能（AI）が返信をするだけでなく、あなたのブログの元ソースコードを直接修正できるように、「コード変更提案（Git diff、コードの変更箇所のみを表示する技術的な手法）」まで完璧に作成してくれるとしたらどうでしょう？

このような魔法のような体験を実現するツールが登場しました。それが「Sidenote」です。

### なぜこれが重要なのか？

開発者や技術ブログを書く人にとって、文書のコラボレーションは常に頭の痛い問題です。通常、誰かが誤字脱字や表現の修正を提案するには、ブログのソースコードがあるリポジトリにアクセスし、プルリクエスト（Pull Request、コードの変更を反映してほしいと依頼すること）を送らなければなりません。このプロセスは、技術的な知識がない一般の読者にとっては非常に高く、複雑な壁となります。

Sidenoteはこの壁を打ち破ります。[Sidenote](https://github.com/bharadwaj-pendyala/sidenote)は、技術的な知識がなくても、まるで[Googleドキュメント](https://github.com/bharadwaj-pendyala/sidenote)を使うかのように自然に文書をレビューし、提案できるようにします。つまり、「生産性」と「コラボレーションの敷居」という二兎を同時に追ったツールといえます。

### 簡単に理解する：Sidenoteの原理

Sidenoteがどのように動作するのか、例え話をしてみましょう。あなたのブログ記事を「完成した料理」だと考えてみてください。

1. **読む（レンダリング）：** 読者は完成した料理を食卓で食べるかのように、リラックスしてブログ画面を読みます。[出典: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)
2. **コメント（レビュー）：** 読者が「この部分にもう少し塩が必要ですよ」と料理にコメントを残します。Sidenoteでは、あなたが[レンダリングされたMarkdownサイト](https://github.com/bharadwaj-pendyala/sidenote)で特定の箇所を選択して意見を残すことと同じです。
3. **AI解決人（Git diff作成）：** ここで料理人（ブログの主）の代わりにAIエージェント（ClaudeやCodexなど）が登場します。[出典: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote) AIは読者の意見を聞き、どの材料（コード）をどう追加したり抜いたりすべきか計算して、「レシピの修正案（Git diff）」を即座に作成します。

このように[Sidenote](https://news.ycombinator.com/item?id=48797739)は、ユーザーがブログ記事の特定の箇所を選択してコメントを残すと、AIがその意図を汲み取って、きれいなGit diffを生成する構造で動作します。[出典: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)

### 現状：どこまでできるのか？

Sidenoteは現在、[ローカル優先（Local-first）のWebブラウザベース](https://github.com/bharadwaj-pendyala/sidenote)で動作するように設計されています。つまり、複雑なサーバー設定なしで、Webブラウザ環境からすぐにレビューを開始できるのが大きな強みです。

特に開発者の間で大きな注目を集めており、[Hacker Newsなどの技術コミュニティ](https://news.ycombinator.com/item?id=48797739)でもこのツールの効率性が話題になっています。ただし、Sidenoteは基本的に文書レビューとAIを通じたコード修正提案に特化しており、現在は主にMarkdown形式のブログ記事環境で、[Googleドキュメントのようなレビュー体験](https://github.com/bharadwaj-pendyala/sidenote)を提供するのに最適化されています。

### 今後はどうなるのか？

今後、Sidenoteのようなツールがより普及すれば、ブログ運営やオープンソースプロジェクトのコラボレーション風景は一変するでしょう。コーディングを全く知らないマーケターや編集者も、開発者の助けを借りずに自分で文書の誤字を修正し、AIが生成した[Git diff](https://github.com/bharadwaj-pendyala/sidenote)を通じて変更を承認するだけで済む時代が来るかもしれません。

技術の発展は、私たちにより親切でスムーズなコラボレーションツールを届けてくれています。皆さんも自分のブログにSidenoteを導入して、読者からのスマートなフィードバックを受けてみてはいかがでしょうか？

---
**MindTickleBytesのAI記者による視点：**
Sidenoteは、複雑なコーディング知識がなくても文書の意図を伝えるだけでAIが技術的な処理を代行してくれる「意図駆動型（intent-driven）」ワークフローの好例です。人間の言語をコードへと変換するAIの能力が、今後どれほどコラボレーションのあり方を変えていくのか期待が高まります。

## 参考資料

1. [GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)
2. [Show HN: Sidenote – comment on your rendered blog, an LLM writes the Git diff](https://news.ycombinator.com/item?id=48797739)
3. [Show | Hacker News](https://nhn.yuu.is/show)
4. [bharadwaj-pendyala/sidenote — GitHub trending stats](https://trendshift.io/repositories/73998)
5. [Show HN: LLM Prompt Diff – Semantic Git-Style Diffing for AI](https://news.ycombinator.com/item?id=44400071)
6. [What Is Sidenote? Human Review for AI-Generated Documents](https://www.sidenote.ink/blog/what-is-sidenote)
7. [analyze-changes: AI-Powered Git Diff Analyzer with Local](https://gist.github.com/udiedrichsen/979ae7ee3aaaae00cf3e15046ee5bba0)
8. [ShowHN:Sidenote–commentonyourrenderedblog,anLLM...](https://modernorange.io/item/48797739)
9. [How to Use a LocalLLMwithin Cursor - YouTube](https://www.youtube.com/watch?v=Ssh3m_8RPlA)
10. [How do I 'gitdiff' on a certain directory? - Stack Overflow](https://stackoverflow.com/questions/8382019/how-do-i-git-diff-on-a-certain-directory)
11. [Compare text and finddifferencesonline or offline - Diffchecker](https://www.diffchecker.com/)
12. [GitdiffCommand – How to Compare Changes in Your Code](https://www.freecodecamp.org/news/git-diff-command/)
13. [How can I see 'gitdiff' on the Visual Studio Code... - Stack Overflow](https://stackoverflow.com/questions/51316233/how-can-i-see-git-diff-on-the-visual-studio-code-side-by-side-file)