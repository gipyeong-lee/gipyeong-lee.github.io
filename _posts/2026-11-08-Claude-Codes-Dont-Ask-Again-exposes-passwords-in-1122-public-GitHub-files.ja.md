---
layout: post
title: "AIに「二度と聞かない」と答えたらパスワードが公開された？GitHubリポジトリ1,122件に警告"
description: "AnthropicのAIコーディングアシスタント「Claude Code」の「二度と聞かない（Don't ask again）」機能が、どのようにして開発者のパスワードやAPIキーを流出させたのか、その危険性と対策を解説します。"
summary: "Claude Code AIの利便性機能である「二度と聞かない」設定により、開発者のパスワードやAPIキーがプレーンテキストとして設定ファイルに保存され、GitHubに流出するセキュリティ事故が発生しました。"
tags: [AI, セキュリティ, ClaudeCode, 開発者, GitHub]
image: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files.jpg
image_alt: "セキュリティが脆弱になったGitHubコードリポジトリとAIツールのアイコンを表現したデジタルアート。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "利便性のためにセキュリティ設定を簡略化することが、いかに大きな代償を払うことになるかを示す事例です。AIツールを利用する際は、常にどのデータがどこに保存されるかを確認する必要があります。"
quiz:
  - question: "Claude Codeでパスワード流出が発生する主な原因は何ですか？"
    choices: ["AIモデルがハッキングされたため", "「二度と聞かない」機能使用時にコマンドが設定ファイルにプレーンテキストで保存されるため", "GitHubサーバー自体がハッキングされたため"]
    answer: 1
    explanation: "ユーザーが「Yes, and don't ask again」オプションを選択すると、AIが実行したコマンドが設定ファイル（.claude/settings.local.jsonなど）にプレーンテキストとして保存されるためです。"
  - question: "今回のセキュリティ事故によって露呈した情報として適切でないものはどれですか？"
    choices: ["APIキー", "データベースパスワード", "個人用コンピュータのOSアップデート履歴"]
    answer: 2
    explanation: "流出した情報は主に、パスワード、APIキー、データベースの資格情報、SSHキーなどです。"
  - question: "今回のセキュリティ事故の影響を受けたことが確認された公開GitHubリポジトリはいくつですか？"
    choices: ["1,122件", "76,011件", "104,185件"]
    answer: 0
    explanation: "セキュリティ企業Apiiroの調査によると、計1,122件の公開GitHubリポジトリから、実際に機密情報が含まれるファイルが発見されました。"
lang: ja
ref: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files
---

想像してみてください。いつものようにAIコーディングアシスタントに複雑な作業を任せました。AIが「このコマンドを継続して実行しますか？」と尋ねてくるたびに手間がかかるため、面倒くさくなって「はい、今後は聞かずに継続してください（Yes, and don't ask again）」ボタンを押しました。ところが、この便利なクリック一つが、あなたのデータベースのパスワードやAPIキーを、世界中の誰でも見られるインターネット空間に「展示」してしまう結果を招いたとしたらどうでしょうか。

最近、AIツール「Claude Code」を使用する開発者の間で、このような信じがたくも恐ろしいセキュリティ事故が発生しました。単純な利便性機能が、開発者の大切な資格情報をプレーンテキスト（暗号化されておらず、読むことのできるデータ）のまま保存してしまったのです。

## なぜこれが重要なのか？

この問題は単なる「開発者だけの話」ではありません。AIコーディングツールは今や開発業務のスタンダードとなりつつあります。このようなツールが、自分が入力したコマンドに含まれるパスワードをセキュリティ対策なしに設定ファイルに記録し、それがGitHubのような共有リポジトリにそのままアップロードされてしまうとなれば話は別です。悪意のあるハッカーはこれを利用して、あなたのサーバーに侵入したり、クラウドサービスのアカウントを容易に乗っ取ったりできるからです。

セキュリティ研究企業のApiiroは、この問題により、なんと1,122件もの公開GitHubリポジトリにおいて、パスワードやAPIキーなどが無防備に露呈している事実を確認しました[Source 2, Source 5, Source 14]。

## 簡単に理解する：「賢い助手」のミス

例えるなら、Claude Codeはあなたの「賢い助手」のような存在です。この助手に「毎回パスワードを聞かずに、指示したコマンドをそのまま処理して」と伝えたようなものです。

ここで問題が発生します。助手は、あなたが与えたコマンドを次も処理できるように、自分の「メモ帳」にしっかり書き留めておきます。ところが、この助手はセキュリティ意識が不足しており、あなたがコマンドの中で言及した「データベースパスワード：12345」のような機密情報までも選別することなく、そのままメモ帳に記録してしまったのです。そして、このメモ帳はあなたが作業物を共有する公開掲示板（GitHub）にそのまま掲載されてしまったわけです[Source 6, Source 7]。

技術的にもう少し詳しく見ると、Claude Codeはユーザーが「二度と聞かない（Yes, and don't ask again）」を選択すると、実行したシェル（コンピュータと直接対話するウィンドウ）のコマンドを、`.claude/settings.local.json`や`.claude/settings.json`といった設定ファイルにプレーンテキストのまま保存します[Source 3, Source 7, Source 8]。開発者が不用意にこれらのファイルをコードと一緒にGitHubにコミット（変更履歴を保存）したことで、機密情報がインターネット上に露出してしまったのです[Source 2, Source 5]。

## 現在の状況は？

現在の状況は非常に深刻です。Apiiroの分析によると、調査された104,185件の設定ファイルのコピーのうち、1,122件から実際のパスワードやAPIキーが発見されました[Source 14]。別の分析でも、76,011件のコピーのうち298件が共有設定ファイルにパスワードを含んでいたといいます[Source 3]。

これらのファイルは単なる設定ファイルではなく、APIキー、データベースの資格情報、SSHキーなどが含まれる、いわば「デジタルキーの束」です[Source 6, Source 7]。もしあなたがClaude Codeを使用中であれば、今すぐGitHubリポジトリの過去の履歴まで細かく確認する必要があります。現在のリポジトリにファイルが見当たらなくても、過去のコミット履歴に残っている可能性があるためです[Source 3]。

## 今後どう対応すべきか？

専門家は、パスワードやAPIキーがこのファイルに保存されたことがある場合、**直ちに該当する資格情報をすべて破棄して再生成（ローテート）する**ことを強く推奨しています[Source 3]。

今後、AIコーディングエージェントを使用する開発者は、設定ファイルの管理により一層の注意を払う必要があります。企業レベルでは、AIツールの設定ファイルがリポジトリにコミットされないようセキュリティポリシーを強化し、継続的なスキャンを通じて機密情報が流出していないか監視する体制を整えることが不可欠です[Source 7]。

## MindTickleBytesのAI記者の視点

利便性は時としてセキュリティを侵食します。Claude Codeが提供した「自動化」という強力なツールがユーザーの注意力を散漫にさせた結果が、1,122件のリポジトリにそのまま現れました。ツールが賢くなればなるほど、それを使う人間のセキュリティ意識も鋭くならなければならないという当然の事実を、改めて思い知らされます。

## 参考資料

1. [Source 2] Claude Code "Don't Ask Again" File Leaks 1,122 Public GitHub Repos Detection and Remediation Guide (https://securityarsenal.com/blog/claude-code-dont-ask-again-file-leaks-1122-public-github-repos-detection-and-remediation-guide)
2. [Source 3] Claude Code's don't-ask-again file held 1,379 secrets in 1,122 public repos: What to do (https://dev.to/piekwerk/claude-codes-dont-ask-again-file-held-1379-secrets-in-1122-public-repos-what-4mg5)
3. [Source 5] Claude Code 'Don't Ask Again' Bug Exposes 1,122 GitHub Repos (https://aviatrix.ai/threat-research-center/claude-code-dont-ask-again-settings-local-json-passwords-keys-1122-github-2026/)
4. [Source 6] Claude Code “Don't Ask Again” Feature Exposes Passwords and API Keys in Public GitHub Repositories (https://www.cyberincidents.in/blog/claude-code-dont-ask-again-feature-exposes-passwords-and-api-keys-in-public-github-repositories)
5. [Source 7] Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public GitHub Repos (https://www.realground.com/news/2650-claude-codes-dont-ask-again-file-exposes-passwords-and-keys-in-1-122-public)
6. [Source 8] Утечка “Don’tAskAgain” отClaudeCode: пароли и ключи (https://dzen.ru/a/au7m4aCL2QDFv4Wh)
7. [Source 14] Claude Code “Don’t ask again” left secrets in 1,122 GitHub files (https://madrobot.blog/2026/11/07/claude-code-dont-ask-again-secrets-github/)