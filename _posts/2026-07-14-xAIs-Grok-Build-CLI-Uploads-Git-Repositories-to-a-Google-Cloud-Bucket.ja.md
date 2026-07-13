---
layout: post
title: "私のコードがAIサーバーに密かに送信されていた？『グロック・ビルド（Grok Build）』セキュリティ騒動の全容"
description: "開発者が愛用するxAIの「グロック・ビルド（Grok Build）」CLIが、ユーザーのコードリポジトリ全体を密かにサーバーへ送信していたという衝撃的なセキュリティ分析結果が明らかになりました。"
summary: "xAIのツール「グロック・ビルド」が、ユーザーの許可なくすべてのコードや機密情報をクラウドサーバーへ自動アップロードしていたことが確認され、大きな波紋を呼んでいます。"
tags: [AI, セキュリティ, グロック, xAI, 開発者]
image: 2026-07-14-xAIs-Grok-Build-CLI-Uploads-Git-Repositories-to-a-Google-Cloud-Bucket.jpg
image_alt: "コンピューター画面の上でデータがクラウドへ流出する様子をイメージしたデジタルアート"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企業向けソリューションの核心は『信頼』です。今回の事態のように透明性を欠いたデータ収集は、ユーザーの信頼を一瞬にして崩壊させかねないことを示す痛烈な事例です。"
quiz:
  - question: "今回のセキュリティ分析により明らかになった『グロック・ビルド』の問題点は何ですか？"
    choices: ["ユーザーが読み込みを指示したファイルのみを送信している", "Gitリポジトリ全体と機密設定値をユーザーの許可なくアップロードしている", "データを暗号化して安全に保存している"]
    answer: 1
    explanation: "分析の結果、このツールはユーザーが明示的に読み込みを指定していないファイルや機密性の高いセキュリティキーを含め、リポジトリ全体をクラウドサーバーへ自動的にアップロードしていました。"
  - question: "現在、このデータ送信問題はどのような状況ですか？"
    choices: ["問題は全くないことが判明した", "xAIが正式な謝罪文を発表した", "公開後、サーバー側の設定を通じて停止されたと見られる"]
    answer: 2
    explanation: "現在はサーバー側の設定によって送信は停止されたと見られていますが、xAIはデータの保持および削除ポリシーについて公式な見解を出していません。"
  - question: "開発者が認識すべき最も大きなリスクは何ですか？"
    choices: ["コンピューターの動作が重くなる", "環境変数（.env）に含まれる機密APIキーなどが外部へ流出する恐れがある", "Gitの履歴が削除される"]
    answer: 1
    explanation: "このツールは機密情報を含むすべての環境ファイル（.envなど）までサーバーへ送信していたため、深刻なセキュリティリスクを招く可能性があります。"
lang: ja
ref: 2026-07-14-xAIs-Grok-Build-CLI-Uploads-Git-Repositories-to-a-Google-Cloud-Bucket
---

想像してみてください。あなたは自宅のパスワードを書いたメモをタンスの奥深くに隠しておいたのに、掃除サービスを呼んだ途端、掃除機がタンスの中身をすべて吸い出し、業者の金庫へ持ち去ってしまった状況を。

最近、多くの開発者がAIコーディングアシスタントとして使用しているxAIの「グロック・ビルド（Grok Build）CLI」ツールにおいて、これと似たようなセキュリティ問題が発見され、大きな論争となっています。[AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)によると、このツールは「ローカルファースト（ローカル環境で直接実行されるという意味）」という宣伝文句とは裏腹に、ユーザーのGitリポジトリ全体のコンテンツを密かに特定のクラウドサーバーへ送信していました。

## なぜこれが重要なのか？

この問題は単に「コードを少し持ち去られた」というレベルを超えています。社内コードや顧客の個人情報が含まれる機密ファイル、さらにはサービス接続のための「秘密鍵（.envファイルなど）」までが、AI企業のサーバーへ渡ってしまったことを意味します。[byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)は、このツールがユーザーがAIに見せたくなかったファイルまで全てを掻き集めていたと指摘しました。

開発者にとってコードは資産であり、知的財産です。許可のないデータ収集は企業のセキュリティポリシーを真っ向から違反する行為であり、万が一この情報がハッキングや流出に遭った場合、想像を絶するセキュリティ事故につながる恐れがあります。[GIGAZINE](https://gigazine.net/gsc_news/en/20260713-grok-build-sending-data/)は、このツールがユーザーの明示的な同意なしにコードを収集していた点を最も深刻な問題として挙げています。

## 簡単に言うと

この現象を身近な例に例えてみましょう。あなたが写真編集アプリを使っていると想像してください。編集したい写真だけを選んで補正したいのに、このアプリが写真を開くたびに、あなたのスマホにある「すべての写真」をクラウドサーバーへ丸ごとコピーして送信するようなものです。[GitHubのセキュリティ分析結果](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)によると、グロック・ビルドツールはAIが作業のためにファイルを読み込んだかどうかに関わらず、現在の作業フォルダにあるすべてのファイルとGitの全履歴を「grok-code-session-traces」という名前のクラウドストレージへアップロードしていました。[Hasty Briefs](https://hb.int2inf.com/en/s/item/A8Cux9a7WKyFuJcdKfPNER-Grok-Build-CLI-data-exfiltration-analysis)は、この過程で機密性の高いセキュリティキーまで別のルートを通じて一緒に送信されていたと分析しています。

## 現在の状況は？

セキュリティ専門家による分析と公開告発が続いた結果、[国際サイバーダイジェスト（International Cyber Digest）](https://x.com/IntCyberDigest/status/2076689215258014069)は、このアップロードが隠されていたサーバー側の設定を通じて停止されたと発表しました。しかし、ユーザーの不安は依然として消えていません。xAI側が、これらのデータがなぜ、どのように収集されたのか、そしてすでにサーバーへ渡ったコードを安全に削除してくれたのかについて、公式な立場を全く示していないためです。[ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)でもこの点を指摘し、ユーザーの懸念が高まっていると伝えています。

## 今後はどうなるのか？

今回の事態をきっかけに、開発者は外部から導入するAIツールを使用する際、より厳格なセキュリティ確認プロセスを経るようになるでしょう。[wetlink](https://github.com/wetlink/grok-build-privacy-hardening)のようなオープンソースプロジェクトでは、ユーザーデータを守るための「キルスイッチ（問題発生時に機能を強制的に停止する安全装置）」を自ら開発して対応しています。今後は企業がAIツールを導入する際、内部セキュリティ監査をさらに強化することになり、xAIのようなサービス提供業者は透明性を立証できなければ、ユーザーの信頼を回復することは難しいと思われます。

## MindTickleBytesのAI記者からの視点

技術は便利ですが、その裏でどのようなデータが行き交っているのか分からないことは、ユーザーにとって常に大きなリスクです。特にコードのような重要な資産を扱うツールであれば、「信頼」を基盤に運営されるべきです。xAIは今回の事態についてより透明性を持って対話し、ユーザーのコードに対して責任ある措置を講じるべきです。

## 参考資料

1. [xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)
2. [What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)
3. [International Cyber Digest on X: "‼️ BREAKING: xAI's Grok Build CLI was uploading entire Git repositories to a Google Cloud bucket, private codebases and unredacted secrets included..."](https://x.com/IntCyberDigest/status/2076689215258014069)
4. [Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)
5. [Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
6. [GitHub - cereblab/grok-build-exfil-repro](https://github.com/cereblab/grok-build-exfil-repro)
7. [Grok Build CLI Repository Uploads, What the Wire Capture Proved](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)
10. [GitHub Gist](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547.pibb)
11. [What xAI's Grok Build CLI Actually Sends to xAI | Hasty Briefs](https://hb.int2inf.com/en/s/item/A8Cux9a7WKyFuJcdKfPNER-Grok-Build-CLI-data-exfiltration-analysis)
12. [xAI's Grok CLI Reportedly Uploads User Codebases and Keys ...](https://cb-terminal.dev/en/topic/6d9cba8e-8783-476a-92e5-f604bda29091)
13. [Investigations reveal that Grok Build transmitted... - GIGAZINE](https://gigazine.net/gsc_news/en/20260713-grok-build-sending-data/)
14. [wetlink/grok-build-privacy-hardening](https://github.com/wetlink/grok-build-privacy-hardening)