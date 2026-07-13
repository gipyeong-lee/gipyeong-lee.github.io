---
layout: post
title: "私のコードが丸ごとxAIサーバーに？「Grok Build」の衝撃的なデータ流出騒動"
description: "AI開発ツール「Grok Build CLI」がユーザーのローカルリポジトリを同意なしにサーバーへ送信していたことが判明しました。この問題の内容と、個人のセキュリティを守る方法について解説します。"
summary: "xAIの開発ツールであるGrok Build CLIが、ユーザーが選択したファイルだけでなくリポジトリ全体を無断でxAIサーバーにアップロードし、環境変数などの機密情報まで漏洩させていることがセキュリティ研究により確認されました。"
tags: [AI, セキュリティ, データ流出, Grok, xAI]
image: 2026-07-13-Grok-uploaded-my-user-directory-to-xAIs-servers.jpg
image_alt: "コンピューター画面からデータが外部サーバーへ送信される様子を象徴化したセキュリティ警告画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開発ツールはユーザーのコードを扱う以上、高いレベルの透明性が不可欠です。今回の事態は、AIツール使用時にデータの送信範囲を必ず確認すべきであることを強く示唆しています。"
quiz:
  - question: "Grok Build CLIがアップロードするデータの範囲はどこまでですか？"
    choices: ["ユーザーが質問した特定のファイルのみ", "AIが読み込んだファイルのみ", "ローカルリポジトリ全体"]
    answer: 2
    explanation: "調査結果によると、AIが読み込んだりアクセスしたりしていないファイルを含め、リポジトリ全体がサーバーへアップロードされていることが判明しました。"
  - question: "製品内で提供されている「データアップロード防止（opt-out）」機能をオンにすると、アップロードは遮断されますか？"
    choices: ["はい、完全に遮断されます", "いいえ、機能が正しく動作していません", "一部のファイルのみ遮断されます"]
    answer: 1
    explanation: "ユーザーが提供した設定オプションにもかかわらず、実際にはリポジトリのアップロードが停止しないことが確認されました。"
  - question: "今回の事態で特に注意すべき機密情報は何ですか？"
    choices: ["コンピューターの壁紙", ".envファイルに含まれるパスワードやAPIキー", "コンピューターのOS情報"]
    answer: 1
    explanation: "環境設定ファイルである「.env」ファイルが、隠蔽処理されることなくそのまま送信されており、セキュリティ上非常に危険な状態です。"
lang: ja
ref: 2026-07-13-Grok-uploaded-my-user-directory-to-xAIs-servers
---

想像してみてください。今朝、新しいAIコーディングツールをインストールして勉強を始めたとします。AIにいくつか質問を投げ、必要なコードの一部をいくつか読み込んだだけです。ところが実は、あなたのコンピューター内の全プロジェクトファイルと、その中に隠しておいたパスワードやサービス接続キー（APIキー）が、すべて遠くの会社サーバーへ送信されていたとしたらどうでしょうか？

最近、AI業界で非常に懸念されるニュースが報じられました。xAIが提供する開発ツール「Grok Build CLI（コマンドベースのAIインターフェースツール）」が、ユーザーの同意なしにローカルリポジトリ全体をサーバーへアップロードしている事実が判明したのです [[参考資料: Grok Build CLI Uploads Your Entire Repo to xAI Servers](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)]。

## なぜ危険なのか？

単にAIがコードを学習するレベルの話ではありません。このツールは、ユーザーがAIに見せようと選択したファイルだけを選んで伝送するわけではありません。**ユーザーのコンピューターにあるリポジトリ全体**を「Gitバンドル（Git bundle、コード履歴とファイル群を一つにまとめたデータ塊）」の形式で、xAIのクラウドサーバーにアップロードしているのです [[参考資料: xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored), [参考資料: Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)]。

最も致命的なのは、「.env」ファイルのようにサービス接続用のパスワードやセキュリティ権限が記載された機密設定ファイルまで、何の隠蔽処理（Redaction）もなくそのまま送信されているという点です [[参考資料: What xAI Grok Build CLI actually sends to xAI - a wire-level analysis...](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547?ref=upstract.com)]。もしあなたが開発者なら、個人のプロジェクトや会社の機密コードが、瞬く間に外部サーバーへ渡っていることになります。

## わかりやすく例えると

この状況を身近な例えで説明してみましょう。

あなたが図書館で司書（AI）に「この本一冊の内容だけ教えてくれる？」と尋ねたと仮定してください。ところが司書は、あなたの要望を聞くふりをしながら、実はあなたが持ってきたカバンを丸ごと奪い取り、カバンの中のダイアリー、個人的な手紙、さらには秘密の通帳まで全てコピーして持ち去ってしまった、という状況です。

文章内の単語の関係を把握し、文脈を理解するAI技術がどれほど優れていても、このプロセスにおいてユーザーのデータは「カバンの中身」のように、予告なしにサーバーへ渡されているのです。調査結果によると、テストのために使用した12GB規模のリポジトリから、なんと5.1GBにも及ぶデータが自動的にアップロードされていました [[参考資料: Grok Build CLI Uploads Your Entire Repo to xAI Servers](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)]。

## 現在の状況は？

さらに大きな問題は、ユーザーがこの機能をオフにしようとしても動作しないという点です。製品内の「データアップロード防止（opt-out）」機能をオンにしたにもかかわらず、実際のネットワークフローを分析すると、リポジトリのアップロードが停止しない事実が確認されました [[参考資料: xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)]。

これは外部ハッカーの仕業や、システムが突破された「データ流出事故」ではありません [[参考資料: Grok Build CLI Repository Uploads, What the Wire Capture Proved](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)]。しかし、ツール自体が設計段階からユーザーに隠れてデータを持ち出すようになっているという点は、ユーザーに大きな裏切りを感じさせています。現在開発者の間では、自分のリポジトリが実際にアップロードされていないか確認するための監査ツールまで登場している実情です [[参考資料: grok-upload-audit/README.md at main · MaydayV/grok-upload-audit](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)]。

## 今後はどうすべきか？

当面の間、xAIのデータ収集ポリシーに対する強い批判は続くと見られます。ユーザーの信頼が一度崩れると、それを取り戻すのは非常に難しいためです。今後はAIツールを使用する際、インストールしたプログラムがネットワークを通じてどのようなデータを外部へ送信しているのか（phone-home）、細かくチェックする習慣が必要です。

技術の発展に伴い、AIをコンピューターのフォルダーに直接接続して使用する環境が増えています。しかし、利便性よりも優先すべきことは「自分のデータをどれだけ安全にコントロールできるか」という基本的なセキュリティ原則です。今回の事態を機に、使用中のツールの権限を再度チェックしてみることをお勧めします。

## MindTickleBytesのAI記者による視点
イノベーションは透明性の上に成り立ってこそ価値があります。コードを扱うツールがユーザーのセキュリティを第一に考えないのであれば、どんなに優れた人工知能の性能も意味がありません。セキュリティは選択ではなく必須事項です。

## 参考資料

1. [Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)
2. [xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)
3. [Grok Build CLI Repository Uploads, What the Wire Capture Proved](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)
4. [grok-upload-audit/README.md at main · MaydayV/grok-upload-audit](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)
5. [Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
6. [What xAI Grok Build CLI actually sends to xAI - a wire-level analysis...](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547?ref=upstract.com)