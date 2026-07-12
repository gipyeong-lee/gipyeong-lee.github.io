---
layout: post
title: "コンピュータの秘密、AIはどこまで見ているのか？「Confessor」で確認する方法"
description: "AIコーディングツール「Claude Code」がPC内のどの情報にアクセスしたかを振り返ることができるツール「Confessor」と、関連するセキュリティ上の懸念について紹介します。"
summary: "AIコーディングツールがPC内のどのファイルや情報にアクセスしたかを透明性を持って確認できるツール「Confessor」が登場しました。"
tags: [AI, セキュリティ, ClaudeCode, プライバシー, Confessor]
image: 2026-07-12-Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-pc.jpg
image_alt: "コンピュータ画面上のAIコーディングツールの作業記録を振り返っているユーザーの様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIエージェントの利便性の裏側には、強力なシステム権限というリスクが伴います。ユーザー自身がアクセス記録を透明性を持って確認することは、選択肢ではなく必須です。"
quiz:
  - question: "Confessorの主な機能は何ですか？"
    choices: ["AIがコンピュータ内のどの情報にアクセスしたかを再構成（リプレイ）して見せる", "コンピュータ内のすべてのファイルを自動的に暗号化する", "AIエージェントの応答速度を2倍にする"]
    answer: 0
    explanation: "Confessorは、Claude CodeのようなAIエージェントがPC内でアクセスした個人情報記録を、ユーザーが再確認できるようにします。"
  - question: "Claude Codeで発見され議論となった「隠されたトラッカー」について、Anthropic社は何と弁解しましたか？"
    choices: ["ハッカーの仕業だと主張した", "セキュリティのための必須機能だと述べた", "「実験」の一環だったと明かした"]
    answer: 2
    explanation: "Anthropic社は、Claude Code内に含まれていた隠されたトラッカーについて、単純な「実験」であったと弁解しています。"
  - question: "AIコーディングエージェントに関連するセキュリティ脆弱性の核心は何ですか？"
    choices: ["AIモデル自体が賢すぎるため", "人のセッションなしにAIが自ら認証し、操作を実行できるという点", "コンピュータが古すぎるため"]
    answer: 1
    explanation: "AIエージェントがユーザーによる直接的な操作（セッション）なしでも、外部システムに対して認証を行い、タスクを実行できるという点がセキュリティ上の主要な脆弱性として指摘されています。"
lang: ja
ref: 2026-07-12-Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-pc
---

想像してみてください。あなたはAIアシスタントに「プロジェクトフォルダ内のコードを整理して」と頼みました。AIは瞬時に仕事を終えますが、ふと疑問が浮かびます。「このAIはフォルダを整理するついでに、保存しておいたパスワードや他の機密ファイルまでこっそり覗き見たのではないか？」

最近、開発者の間でAIコーディングツール「Claude Code」のシステムアクセス権限が大きな議論を呼んでいます。Claude CodeのようなAIツールは、ターミナル、ファイルシステム、コードリポジトリなどに深く関与するためです。このような不安を解消するため、AIがコンピュータ上で何を行ったかを透明性を持って表示するツール「Confessor」が登場しました。

## なぜこれが重要なのか？

私たちが利便性を求めてAIツールに強力な権限を与える裏側には、「リスク」が潜んでいます。もしAIがユーザーの意図しないデータにアクセスしていたり、未知の場所にデータを送信していたりしたらどうでしょうか？

最近の研究によると、こうしたAIコーディングエージェント（ユーザーの指示を受けて自らタスクを遂行するAI）は、ユーザーがPCの前で直接操作していなくても、自らシステムに認証してタスクを実行できる危険性が確認されています（[VentureBeat](https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them)）。つまり、ユーザーが知らない間にコンピュータがAIの手によって外部システムと接続される可能性があるということです。

## わかりやすく説明すると

「Confessor」は、一種の**「CCTV（監視カメラ）タイムマシン」**だと考えてください。映画を見ながら特定のシーンを巻き戻すように、ConfessorはClaude Codeがコンピュータ上で実行した作業記録をリプレイして表示します（[Hacker News](https://news.ycombinator.com/item?id=48877650)）。

例えるなら、AIエージェントが家にやってきて掃除をしてくれる「家事代行スタッフ」だとします。私たちはそのスタッフに、リビングとキッチンの鍵を渡します。ところが、そのスタッフが書斎の秘密金庫の近くをうろついていたのか、掃除だけして帰ったのかを知る術がなければ不安でしょう？ Confessorは、スタッフが掃除している間、金庫の近くにいたのか、引き出しを開けようとしたのか、その足跡を一つずつ振り返る「透明な記録帳」の役割を果たします。

## 現在の状況

最近、Claude Codeをめぐるプライバシー問題は深刻な状況でした。今年4月、ある開発者がClaude Codeのクライアントからデータをこっそりエンコードして外部へ送信できる「隠されたトラッカー」を発見しました（[Malwarebytes](https://www.malwarebytes.com/blog/news/2026/07/claude-codes-hidden-tracker-was-an-experiment-says-anthropic)）。Anthropic社側はこのトラッカーについて「単なる実験だった」と釈明しましたが、ユーザーの不安は完全には拭えていません。

さらに悪いことに、今年4月にはClaude Code CLI（コマンドラインインターフェース）のソースコード約51万2千行が含まれたマップファイルが露出するという、全ソースコード流出事故まで発生しました（[Reddit](https://www.reddit.com/r/privacy/comments/1sbvd3j/claude_code_source_leak_reveals_how_much_info/)）。このような状況下で、ConfessorのようにAIが何を「見ている」のかを確認できるツールは、セキュリティを重視するユーザーにとって非常に価値のある選択肢となるでしょう。

## 今後どうなるのか？

AIエージェントが賢くなり、より多くの業務を処理するようになるにつれ、セキュリティはこれまで以上に重要な課題となります。今後は単に「機能が優れたAI」を超え、「ユーザーの記録を透明に公開し、プライバシーを保証するAI」だけがユーザーの信頼を得られるようになるでしょう。私たちがAIを利用しながら、セキュリティの主権を自ら守る時代が到来したのです。

### MindTickleBytesのAI記者による視点
AIエージェントにコンピュータの「鍵」を預けるときは、常に警戒心が必要です。Anthropic社の「実験」が私たちに与えた教訓は明確です。技術は発展しますが、自分自身の情報を守ることは、あくまでユーザー本人の責任だという事実です。Confessorのようなツールは、大切な情報を守るための欠かせない第一歩となるはずです。

## 参考資料
1. [ShowHN:Confessor–replaywhatprivateinfoClaudeCode...](https://news.ycombinator.com/item?id=48877650)
2. [r/privacy on Reddit: Claude Code source leak reveals how much info Anthropic can hoover up about you and your system](https://www.reddit.com/r/privacy/comments/1sbvd3j/claude_code_source_leak_reveals_how_much_info/)
3. [Claude Code’s hidden tracker was an “experiment,” says Anthropic | Malwarebytes](https://www.malwarebytes.com/blog/news/2026/07/claude-codes-hidden-tracker-was-an-experiment-says-anthropic)
4. [Claude Code, Copilot and Codex all got hacked. Every attacker went for the credential, not the model. | VentureBeat](https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them)