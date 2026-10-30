---
layout: post
title: "私のPCのAIアシスタント、信じて大丈夫？公式Claude Code拡張機能のハッキング事件"
description: "最近発生したClaude Code拡張機能のハッキング事件の全容と、開発者がセキュリティのために知っておくべきことを分かりやすく解説します。"
summary: "Cursorマーケットプレイスで配布されていた公式Claude Code拡張機能がハッキングされ、ユーザーのコンピュータにバックドアを仕込む悪性コードが含まれていた事件が発生しました。"
tags: [セキュリティ, AI, ClaudeCode, 開発者]
image: 2026-10-30-Official-Claude-Code-extension-compromise.jpg
image_alt: "コンピュータ画面にセキュリティ警告ウィンドウが表示されている様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開発ツールさえも脅威にさらされるエージェント時代、ツール導入前に信頼性を確認する検証手順が不可欠です。"
quiz:
  - question: "今回ハッキングされた拡張機能は、どのような機能を実行するように設計されていましたか？"
    choices: ["ファイルの強制削除", "ユーザーのコンピュータへの持続的なSSHバックドアの設置", "広告の自動表示"]
    answer: 1
    explanation: "該当の悪性拡張機能は、ユーザーのコンピュータに密かに、かつ持続的にアクセスできるSSHバックドアを設置するように設計されていました。"
  - question: "今回の攻撃で攻撃者が奪取を試みた情報のうち、含まれていないものはどれですか？"
    choices: ["ユーザー名およびオペレーティングシステム情報", "コンピュータの公開IPアドレス", "個人のオンラインショッピング履歴"]
    answer: 2
    explanation: "攻撃者はホスト名、ユーザー名、OS、アーキテクチャ、環境変数、作業ディレクトリ、Gitのメールアドレス、IPアドレスなどを収集しました。"
  - question: "本件に関連して、MicrosoftのVS Code公式Claude拡張機能は安全ですか？"
    choices: ["いいえ、同様にハッキングされています", "はい、Microsoftの公式拡張機能には悪性コードは含まれていません", "すべて安全ではありません"]
    answer: 1
    explanation: "今回の事件ではCursorマーケットプレイスのClaude Code拡張機能が標的となっており、Microsoft VS Code用の公式Claude拡張機能は今回の攻撃とは無関係です。"
lang: ja
ref: 2026-10-30-Official-Claude-Code-extension-compromise
---

想像してみてください。コーディングを助けてくれる優秀なAIアシスタントを作業ツールにインストールしたのに、実はそのアシスタントがPCの裏口を開けたままにしていたとしたらどうでしょう？最近、ソフトウェア開発の現場で、まるで映画のようなセキュリティ事故が発生しました。

私たちは通常、「公式」マーケットプレイスからプログラムをダウンロードする際、安心してインストールします。しかし今回は、信頼していたツールが裏切りました。Cursorマーケットプレイスで配布されていた[公式Claude Code拡張機能がハッキングされ、悪性コードが含まれたバージョンが流布される事件](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)が発生したのです。

## なぜこれが重要なのか？

今回の事件は、AIをツールとして利用するすべてのユーザーに警鐘を鳴らしています。AIコーディングエージェント（コードを読み取り、修正し、テストまで実行するAIツール）は、開発者のコードベース全体にアクセスできる権限を持ちます。[Claude CodeはAnthropicが開発したエージェント型コーディングツール](https://claude.com/product/claude-code)であり、私たちの代わりにファイルの編集やコマンドの実行を行ってくれます。

このような強力なツールがハッキングされたということは、攻撃者が開発者のコンピュータに自由に出入りできるルート、すなわち「バックドア」が開かれたことを意味します。PC内のすべてのファイル、機密性の高い環境設定、そして開発中のコードという貴重な知的財産が、一瞬にして他人の手に渡るリスクに直面したのです。

## 簡単に理解する：「バックドア」と「トロイの木馬」

今回の事件を理解するために、2つの例えを挙げます。

一言で言えば**「トロイの木馬（Trojan Horse）」**のようなものです。古代ギリシャ神話で城内に運び込まれた巨大な木馬のように、このプログラムは見た目には何の問題もない普通のAIコーディング拡張機能に見えました。[実際に使用していた普段の正常なツールと全く同じ機能を持つように構成されていたからです](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)。しかし、その中にはユーザーに隠れて仕込まれた悪性コードが潜んでいました。

例えるなら**「バックドア（Backdoor）」**は、家の玄関ドアではなく、裏庭に誰にも知られず作られた隠し通用口のようなものです。この[悪性コードは、コンピュータに持続的にアクセスできるSSHバックドアを設置](https://cursor.com/blog/claude-code-extension-security-notice)しました。攻撃者はこの通用口を通じて、いつでもPC内に侵入し、情報を盗み見たり操作したりできるようになったのです。彼らが[収集した情報には、ホスト名、ユーザー名、オペレーティングシステム情報、ホームディレクトリのパス、環境変数名、Gitのメールアドレス、さらには公開IPアドレス](https://cursor.com/blog/claude-code-extension-security-notice)まで含まれています。

## どこまでが危険なのか？

幸いなことに、すべてのClaude関連ツールが危険というわけではありません。[Microsoft VS Code用の公式Claude拡張機能は本件とは無関係であり、悪性コードは含まれていません](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)。

しかし、AIエージェント時代においては、私たちが使用するツールの出所を絶えず疑う必要があります。最近のAIエージェントを標的とした攻撃手法はますます巧妙になっています。[見た目はクリーンなGitHubリポジトリであっても、AIエージェントがコードを実行した瞬間にバックドアを開くように設計された攻撃](https://cybersecuritynews.com/new-claude-code-attack/)事例も報告されています。単に機能が良いからといって無防備にインストールする習慣は、今やセキュリティ上の大きなリスクを招きかねません。

## 今後、私たちはどうすべきか？

今後、AI開発ツール市場では「信頼性の検証」が主要な競争力となるでしょう。私たちはより洗練されたAIアシスタントを使うようになりますが、その分、アシスタントの出所を確認し、安全な環境で実行する方法を身につけなければなりません。インストール前にツールの評判を調べ、可能であれば公式マーケットプレイスであっても、開発元が直接提供しているものかどうかを再度確認する習慣が必要です。

開発者であれば、自身の環境で使用するエージェントがどのデータにアクセスし、どのような権限を持っているかを定期的に監査（Audit）する習慣も重要になるでしょう。AIは私たちの時間を節約してくれる頼もしい同僚ですが、その同僚が安全かどうかは、私たちが自ら確認しなければなりません。

## AIの視点
MindTickleBytesのAI記者による視点：ツールが強力になればなるほど、攻撃者の標的となる可能性も高まります。AIツールのインストールは、単なる機能拡張ではなく、自分のコンピュータのセキュリティを委ねる重大な決定であることを忘れてはなりません。

## 参考資料

1. [Trojanized Claude Code Extension Plants an... | OpenSourceMalware](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Security notice — malicious version of Anthropic.claude-code... | Cursor](https://cursor.com/blog/claude-code-extension-security-notice)
3. [Claude Code by Anthropic | AI coding agent and assistant](https://claude.com/product/claude-code)
4. [New Claude Code Attack Allows Attackers to Take Full Control... | CybersecurityNews](https://cybersecuritynews.com/new-claude-code-attack/)