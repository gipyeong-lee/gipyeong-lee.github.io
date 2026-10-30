---
layout: post
title: "コーディング支援ツールがハッカーの入り口に？Claude Code拡張機能のセキュリティ問題"
description: "最近発見されたClaude Code拡張機能のサプライチェーン攻撃事例と、開発者が注意すべきセキュリティの脅威について解説します。"
summary: "公式Claude Code拡張機能の一部バージョンで遠隔接続可能なバックドアが発見されたため、開発者の注意が必要です。"
tags: [セキュリティ, AI, 開発者, ClaudeCode, サプライチェーン攻撃]
image: 2026-10-30-Backdoors-in-official-Claude-Code-extensions.jpg
image_alt: "コンピュータ画面内のコードと南京錠が描かれた、セキュリティ事故を象徴する画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "利便性のためにインストールしたツールが攻撃者の経路になり得ることを常に警戒しなければなりません。最新版へのアップデートは、もはや選択ではなく生存のための必須事項です。"
quiz:
  - question: "今回のセキュリティ問題の核心的な原因は何ですか？"
    choices: ["AIモデル自体の欠陥", "公式拡張機能の改ざんされたアップデート", "インターネット接続の不良"]
    answer: 1
    explanation: "Claude Code拡張機能の2.1.313バージョンが改ざんされ、悪意のあるコードが含まれていたことが今回の問題の核心です。"
  - question: "悪意のあるコードが実行する主な機能は何ですか？"
    choices: ["広告の表示", "持続的なSSH遠隔接続経路の開設", "コンピュータの速度向上"]
    answer: 1
    explanation: "該当の悪意のあるコードは、攻撃者が開発者のコンピュータに遠隔で接続できるようにSSHバックドアをインストールします。"
  - question: "ユーザーが取るべき対応は何ですか？"
    choices: ["コンピュータの買い替え", "最新バージョンへのアップデートおよびセキュリティ点検", "AIの使用中止"]
    answer: 1
    explanation: "Anthropicが対策としてリリースした2.1.314バージョンに直ちにアップデートし、関連するセキュリティガイドラインを確認する必要があります。"
lang: ja
ref: 2026-10-30-Backdoors-in-official-Claude-Code-extensions
---

想像してみてください。いつものようにコーディングの生産性を高めるため、信頼できる開発ツールのアップデートをクリックしました。しかし、そのアップデートが実はあなたのコンピュータの扉を大きく開け放ち、密かに泥棒を招き入れるものだとしたらどうでしょうか？

最近、世界中の開発者が使用している公式のClaude Code拡張機能でセキュリティ事故が発生しました。私たちが普段便利に使っていたツールが、実は攻撃者の遠隔接続の経路に変質していたのです。今回の事件は、私たちが何気なくインストールする「コード支援ツール」がいかに大きなセキュリティリスクを抱えているかを示す、痛恨の事例となりました。

## なぜこれが重要なのか

開発者にとって拡張機能は、業務効率化のための必須アイテムです。しかし、今回の事件は「公式」拡張機能だからといって無条件に安全ではないという事実を証明しました。[出典 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)、[出典 8](https://undercodenews.com/claude-code-extension-supply-chain-attack-malicious-update-exposed-up-to-5000-cursor-users-to-ssh-backdoors-and-remote-access-video/)によると、約5,000人のユーザーが今回改ざんされたバージョンをインストールしたと推定されています。

攻撃者はこの経路を通じて、ユーザーのGitメールアドレス、環境変数、OS情報などの機密データにアクセスできました。[出典 2](https://cursor.com/blog/claude-code-extension-security-notice)。単に情報を盗むだけでなく、あなたのコンピュータにいつでも再接続できる「非常口（バックドア）」まで作り置いていたという点が最大の脅威です。

## わかりやすい解説

今回の事件は「サプライチェーン攻撃（Supply-Chain Attack）」の典型的な姿です。これをわかりやすく例えるなら、毎日飲んでいるミネラルウォーター工場のシステムがハッキングされ、不純物が混ざった水が正規の流通ルートを通って、私たちの家の食卓まで届けられたようなものです。私たちは工場を信頼していたので、水が汚染されているとは疑いもしないはずです。

技術的には「SSH（Secure Shell、遠隔コンピュータを安全に制御する技術）バックドア」という方式が使われました。攻撃者はこの技術を逆手に取り、「リバースSSHトンネル」を作成しました。[出典 5](https://www.explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026)。簡単に言えば、泥棒が我が家の玄関の鍵を外しておき、いつでも好きな時にまた入れるように秘密の通路を一つこっそり開けておいたようなものです。

## 現在の状況

問題の発端は、公式Claude Code拡張機能の2.1.313バージョンでした。[出典 1](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)、[出典 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)。Cursorマーケットプレイスなどの主要ルートを通じて配布されたこのバージョンは、ユーザーのコンピュータ情報を収集し、攻撃者のサーバーと接続される悪意のあるコードを含んでいました。[出典 2](https://cursor.com/blog/claude-code-extension-security-notice)、[出典 6](https://www.rescana.com/post/claude-code-extension-2-1-313-cursor-marketplace-trojanized-ssh-backdoor)。

現在はCursor側で該当バージョンを直ちに削除し、措置を講じています。[出典 7](https://www.news9live.com/technology/tech-news/claude-code-extension-hacked-ssh-backdoor-cursor-users-at-risk-3020396)。Anthropic側も問題のバージョンを代替する2.1.314バージョンをリリースし、対応に乗り出しました。[出典 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)。ただし、一部の報告によると以前のバージョン（2.1.91〜2.1.196）でもコード追跡や位置情報の漏洩などの疑惑が提起されているため、注意が必要です。[出典 3](https://nowosci.ai/en/article/china-claude-code-backdoor-location-tracking)。

## 今後はどうなるか

今回の事件により、開発ツール市場全体でセキュリティ検証強化の必要性が高まるでしょう。開発者は今後、外部拡張機能をインストールする際により保守的な態度をとるようになり、セキュリティ専門家はマーケットプレイスに登録されるコードに対する自動化された分析システムをより厳格に要求することになるはずです。

読者の皆さんは、自身が使用しているIDE（統合開発環境）の拡張機能のバージョンを直ちに確認し、最新バージョンへのアップデートを忘れないようにしてください。セキュリティの第一歩は、小さな疑いと定期的な点検から始まります。

## AIの視点

AIコーディング支援ツールは私たちの生産性を劇的に高めてくれますが、それと同時に私たちが付与する権限も非常に強力です。今回の事件は、私たちに「利便性の代償」について改めて考えさせます。技術を活用しつつも、その技術が自分のコンピュータの主導権を奪うことがないよう監視する姿勢が、これまで以上に重要になっています。

## 参考資料

1. [Trojanized Claude Code Extension Plants an SSH Backdoor](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Security notice — malicious version of Anthropic.claude-code...](https://cursor.com/blog/claude-code-extension-security-notice)
3. [China Warns of Backdoor in Claude Code, Anthropic Admits](https://nowosci.ai/en/article/china-claude-code-backdoor-location-tracking)
4. [Backdoors in official Claude Code extensions - daily.dev](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)
5. [Claude Code Extension 2.1.313 SSH Backdoor: What To Check...](https://www.explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026)
6. [Trojanized Claude Code Extension 2.1.313 in Cursor...](https://www.rescana.com/post/claude-code-extension-2-1-313-cursor-marketplace-trojanized-ssh-backdoor)
7. [Claude Code extension hacked: SSH backdoor puts 5,000 Cursor...](https://www.news9live.com/technology/tech-news/claude-code-extension-hacked-ssh-backdoor-cursor-users-at-risk-3020396)
8. [Claude Code Extension Supply-Chain Attack: Malicious Update...](https://undercodenews.com/claude-code-extension-supply-chain-attack-malicious-update-exposed-up-to-5000-cursor-users-to-ssh-backdoors-and-remote-access-video/)