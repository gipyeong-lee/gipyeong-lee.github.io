---
layout: post
title: "私のコードが密かにクラウドへ？Grok Build CLIのセキュリティ問題まとめ"
description: "開発者が使用するAIツール「Grok Build CLI」が、ユーザーの保存先リポジトリ全体を同意なく外部送信していた事実が判明しました。このセキュリティ問題の核心をまとめます。"
summary: "xAIのGrok Build CLIが、AIが参照していないファイルを含め、ユーザーのコードリポジトリ全体を外部サーバーへ密かに送信していた事実がセキュリティ研究により明らかになりました。"
tags: [セキュリティ, AI, 開発ツール, xAI, Grok]
image: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS.jpg
image_alt: "コンピュータ画面内のコードデータがクラウドサーバーへ送信される過程を抽象的に表現したイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開発ツールの利便性の裏に隠されたセキュリティ脆弱性は致命的です。信頼できる開発環境のために、透明なデータ処理ポリシーが最優先されるべきです。"
quiz:
  - question: "Grok Build CLIがコードを送信する仕組みについての説明として正しいものはどれか？"
    choices: ["AIが読み取りを許可したファイルのみ送信する", "リポジトリの全ファイルとgit履歴をすべて送信する", "ファイルを送信せずプロンプトのみを送信する"]
    answer: 1
    explanation: "Grok Build CLIは、ユーザーがAIに見せていないファイルを含め、リポジトリ内の全ファイルとgit履歴全体をバンドルして送信していることが確認されました。"
  - question: "今回のセキュリティ問題で判明したデータ送信先はどこか？"
    choices: ["ローカルコンピュータのテンポラリフォルダ", "xAIのGoogle Cloud Storage (GCS) バケット", "ユーザーの個人メールアドレス"]
    answer: 1
    explanation: "分析の結果、送信されたデータはxAIが管理する「grok-code-session-traces」という名称のGoogle Cloud Storage (GCS) バケットに送られていました。"
  - question: "このデータ送信について、ユーザーが知っておくべき点は何か？"
    choices: ["ユーザーが毎回承認しないと送信されない", "送信の有無をサービス提供者がリモートで切り替えられる", "コードのみ送信され、機密情報は一切含まれない"]
    answer: 1
    explanation: "セキュリティ研究によると、このデータアップロード機能はサービス提供元であるxAIがリモートでトグル（オン・オフ）できる構造になっています。"
lang: ja
ref: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS
---

想像してみてください。皆さんが人工知能（AI）ツールに対して「このファイルだけ読んでコードのエラーを見つけて」と頼んだとします。ところが、そのAIツールは許可したファイルだけでなく、コンピュータ内にあるプロジェクトリポジトリ全体のすべてのコードや、過去の修正履歴まで丸ごとコピーして外部サーバーへ送信していたとしたらどうでしょうか。

最近、開発者の間で大きな議論となったxAIの「Grok Build CLI（コマンドラインインターフェース、開発者がコマンドを入力してツールを実行する方式）」事件は、まさにそのような話です。コーディングを便利に助けてくれるはずのツールが、ユーザーのセキュリティの意思とは無関係にデータを密かに持ち出していたという事実が明らかになりました。

## なぜこれが重要なのか？

この問題は、単に「データが少し漏れた」というレベルの話ではありません。開発者のコードリポジトリには、企業の核心的なビジネスロジック、API（アプリケーションプログラミングインターフェース、ソフトウェア間の通信方式）のセキュリティキー、個人のアイデアなど、数多くの知的財産や機密情報が含まれているためです。

セキュリティ研究員がネットワークを直接分析した結果、このツールはユーザーがAIに見せたくないファイルまで含めてリポジトリ全体を外部クラウドへ送信していました。[Source 14](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) あるテストでは、12GB規模のリポジトリから、なんと5.1GBものデータが送信される現象が観測されました。[Source 14](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 自分のコードが許可なく外部サーバーに保存されているという事実は、多くの開発者にセキュリティに対する油断への警鐘を鳴らしています。

## わかりやすく説明：図書館の例え

このように考えると簡単です。皆さんが巨大な図書館（皆さんのコードリポジトリ）を持っていると仮定してみましょう。皆さんは司書（Grok AIツール）に「この本（特定のコードファイル）1冊だけ読んで要約して」と頼みました。

ところが司書は、皆さんが見せた本だけでなく、図書館全体にあるすべての本のコピーを密かに取り込み、自分の倉庫（xAIのクラウドサーバー）へ持ち去っていました。皆さんが「絶対に見てはいけない」と鍵をかけていた本まで含めてです。[Source 1](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) [Source 5](https://github.com/cereblab/grok-build-exfil-repro)

このように例えると、今回の事件は、AIツールがユーザーの「知的財産権」と「データ主権」をどのように扱っているかという根本的な信頼問題を突きつけています。単にコードを読むことを超え、リポジトリ全体をひとまとめ（git bundle）にして密かに送信する構造だったのです。[Source 2](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)

## 現状：何が判明したのか？

現在までにセキュリティ専門家が分析した事実は以下の通りです。

1. **データ全送信：** AIが特定のファイルを読み取る許可を与えたかどうかに関係なく、追跡中のすべてのGit（コードの変更履歴を記録するツール）リポジトリと修正履歴全体が、バンドルとして送信されます。[Source 1](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) [Source 4](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
2. **別のデータチャネル：** コードリポジトリのバンドル以外にも、コードを読み取る過程で環境変数ファイル（システム設定やセキュリティキーが含まれるファイル）などに保存されたセキュリティキーなどの機密情報が、別の通信路を通じて送信されている事実も確認されました。[Source 4](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
3. **リモート制御の可能性：** このアップロード機能は、提供側がリモートでオン・オフできる構造になっています。[Source 3](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)

ただし、一部の誤解を正す点もあります。コンピュータ内のすべてのファイルをすべて持ち去ったわけではなく、主にGitが追跡しているコードリポジトリの内容に集中していることが、ネットワーク分析を通じて判明しました。[Source 6](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)

## 今後はどうなるのか？

今回の事件は、開発者に大きな教訓を残しました。AIツールを導入する際は、単に「どれだけ便利か」を超えて、「自分のデータをどのように扱うか」を必ず確認しなければならないということです。

今後は、オープンソースツールや特定のAIクライアントがデータを送信する際に、ネットワーク通信を監視する「セキュリティ監査」が開発者の必須スキルになるものと見られます。今回の事件をきっかけに、xAI側がセキュリティポリシーを透明に公開し修正するのか、それとも開発者がより閉鎖的で安全な環境を好むようになるのかを見守る必要があります。開発者の皆さんは、今すぐ使用しているAIツールのデータ処理ポリシーを改めて確認することをおすすめします。

## 参考資料

1. What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub, https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
2. xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly, https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored
3. grok-upload-audit/README.md at main · MaydayV/grok-upload-audit, https://github.com/MaydayV/grok-upload-audit/blob/main/README.md
4. Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News, https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc
5. GitHub - cereblab/grok-build-exfil-repro, https://github.com/cereblab/grok-build-exfil-repro
6. Grok Build CLI Repository Uploads, What the Wire Capture Proved, https://www.penligent.ai/hackinglabs/grok-build-cli-repository/
14. Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota, https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/