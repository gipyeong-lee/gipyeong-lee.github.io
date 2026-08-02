---
layout: post
title: "私のパスワードがAI学習データに？7.6ペタバイト規模のセキュリティ警告"
description: "AI学習データセットから数十万件のパスワードとAPIキーが無防備に露出しています。セキュリティ専門家が警告するAIエコシステムのセキュリティの穴を探ります。"
summary: "セキュリティ研究チームがAI学習プラットフォーム「ハギングフェイス（Hugging Face）」の7.6ペタバイトのデータをスキャンした結果、22万件以上の実際に機能するセキュリティ認証情報が露出していることを確認しました。"
tags: [AIセキュリティ, ハギングフェイス, データプライバシー, 情報保護]
image: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets.jpg
image_alt: "巨大なデータの海をデジタル虫眼鏡で調べるセキュリティ研究者の姿を象徴化したイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIモデルの性能と同じくらい重要なのが「データ衛生」です。オープンソースの共有文化が花開く時代であるほど、個人や企業のセキュリティ管理に対する警戒心が一層切実になります。"
quiz:
  - question: "セキュリティ研究員たちがハギングフェイスで発見した「実際に機能するセキュリティ認証情報」の件数は約いくつですか？"
    choices: ["約2千件", "約2万件", "約22万件"]
    answer: 2
    explanation: "研究の結果、約221,303件の機能可能なセキュリティトークンとパスワードが無防備な状態で露出していました。"
  - question: "今回のセキュリティスキャンを実施したデータの全体サイズはどのくらいですか？"
    choices: ["7.6ギガバイト", "7.6テラバイト", "7.6ペタバイト"]
    answer: 2
    explanation: "研究チームは1億8700万ファイルに及ぶ計7.6ペタバイト規模のデータをスキャンしました。"
  - question: "ハギングフェイスは今回のセキュリティ問題を解決するためにどのような努力をしていますか？"
    choices: ["サービスの全面中断", "トリュフ・セキュリティと提携してセキュリティスキャン機能を導入", "すべてのユーザーアカウントの強制削除"]
    answer: 1
    explanation: "ハギングフェイスはトリュフ・セキュリティと協力し、プラットフォーム内に「トリュフホグ（TruffleHog）」セキュリティスキャン機能を導入しました。"
lang: ja
ref: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets
---

# 私のパスワードがAI学習データに？7.6ペタバイト規模のセキュリティ警告

皆さんが日常で楽しんでいるアプリやソフトウェアが、実は誰かの些細なミスによってハッキングの脅威にさらされているとしたらどうでしょうか？最近の人工知能（AI）ブームとともに、世界中の開発者や企業がAI学習用データを共有するプラットフォームである「ハギングフェイス（Hugging Face）」が大きな注目を集めています。ところが、ここにアップロードされた膨大なデータの中に、本来隠すべき私たちの「秘密」が混ざっているという事実が明らかになりました。

セキュリティ研究チームがハギングフェイスの公開データセット全体をくまなく調査した結果、7.6ペタバイト（PB、1ペタバイトは1,000テラバイトに相当する巨大な容量です）という膨大なデータの中で、数十万件もの実際のパスワードやAPIキー（APIはプログラム間の対話窓口であり、キーはその窓口を開けることができる鍵です）がそのまま露出しているという衝撃的な事実を発見しました。[Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets)

## なぜこれが重要なのか？

この問題は単なる個人のミスを超えた深刻なセキュリティ課題です。今日、AIモデルは数多くの公開データを基に学習されます。しかし、学習データの中に開発者のパスワードや機密性の高いアクセスキーが含まれていれば、そのAIモデルを通じて機密情報が流出する可能性があります。さらに、悪意のある攻撃者が学習データを操作したり、該当ソフトウェアに悪性コードを仕込んだりする可能性も十分に存在します。

研究チームが発見した22万件余りの認証情報の中には、攻撃者がソフトウェアの更新プロセスに介入して悪性コードを仕込めるほど強力な権限を持つものもありました。[Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets) 私たちが毎日使用するソフトウェアがこのようなセキュリティの穴によって危険にさらされている可能性があるという点は、非常に憂慮すべき事態です。

## 分かりやすく例えると：『図書館の秘密のメモ』

この状況を図書館に例えてみましょう。世界中の誰でも自由に本を借りて読める巨大な図書館があると想像してください。ところが、ある開発者が誤って自宅の玄関の鍵番号と銀行口座のパスワードが書かれたメモを本の間にはさみ、そのまま返却してしまったようなものです。

さらに大きな問題は、この図書館が単に本を保管するだけでなく、その本を材料にして新しい「知的アシスタント」を作る工場のような役割も果たしているという点です。AIモデルを訓練させるということは、この図書館にあるすべての情報を詳しく調べ、パターンを学習するプロセスです。もし学習材料の中にパスワードが含まれていれば、AIはそのパスワードまでもまるで有益な情報かのように学習してしまう可能性があるのです。[Hugging Face security analysis: ~70,000 live secrets and API keys, private repos, and leaky pics! 🤖🤗💦🔑😈](https://it4sec.substack.com/p/hugging-face-security-analysis-70000)

## 現在の状況

幸いなことに、ハギングフェイスはこの問題を解決するために迅速に行動しています。セキュリティ専門企業である「トリュフ・セキュリティ（Truffle Security）」と手を組み、プラットフォームにアップロードされるデータに秘密情報が混入していないかを自動で検査する「トリュフホグ（TruffleHog）」スキャン機能を導入しました。[TruffleHog Partners With Hugging Face to Scan for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/trufflehog-partners-with-hugging-face-to-scan-for-secrets)

しかし、依然として注意が必要です。今回の研究でスキャンしたデータだけでも1億8700万ファイルに及ぶ7.6ペタバイトでした。[Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets) データをアップロードする際、セキュリティに対する意識がなく、無自覚にファイルを丸ごとアップロードする習慣が続く限り、情報漏洩事故はいつでも再発する恐れがあります。

## 今後はどうなるか？

これからはAI開発のプロセスにおいて「データ衛生（Data Hygiene、データを共有する前に有害な情報をふるい落とす衛生的な管理習慣）」が何よりも重要になるでしょう。データを公開する前に重要な情報が含まれていないか機械的に選別する作業が、必須のプロセスとして定着するはずです。

企業もまた、自分たちの貴重な開発コードが外部のAI学習データとして流出しないよう、さらに徹底したセキュリティポリシーを構築しなければなりません。もし皆さんが開発に携わっているなら、コードを共有したりデータをアップロードしたりする際、中にパスワードやAPIキーが隠れていないか再度確認する習慣を持つべきです。技術が発展するほど、私たちの情報もより細かく管理しなければ、安全なAI時代を享受することはできないでしょう。

## MindTickleBytesのAI記者の視点

AIの知能が高まるにつれ、私たちが無意識に漏らしている情報の価値と危険性も同時に高まっています。利便性という甘い果実の裏に隠れたセキュリティの穴をあらかじめ見つけ出し、塞ぐこと。それこそが真の意味での技術発展ではないでしょうか。

## 参考資料

1. [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets)
2. [TruffleHog Partners With Hugging Face to Scan for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/trufflehog-partners-with-hugging-face-to-scan-for-secrets)
3. [Hugging Face security analysis: ~70,000 live secrets and API keys, private repos, and leaky pics! 🤖🤗💦🔑😈](https://it4sec.substack.com/p/hugging-face-security-analysis-70000)