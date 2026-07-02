---
layout: post
title: "パソコン内のAIが私を監視している？『Claude Code』スパイウェア疑惑の真相"
description: "AIコーディングツール「Claude Code」に隠れた監視用コードが発見されたとの疑惑が浮上しました。この事件が一般ユーザーにとって何を意味し、なぜ重要なのかを分かりやすく解説します。"
summary: "AIコーディングツール「Claude Code」に、中国のユーザーを識別して遮断するための隠しコードが含まれていたとの疑惑が浮上。Anthropicはこれを誤解と説明し、修正中であると発表しました。"
tags: [AI, Anthropic, ClaudeCode, プライバシー, セキュリティ]
image: 2026-07-02-Anthropic-embedded-spyware-in-Claude-Code-and-attempted-to-hide-it-from-you.jpg
image_alt: "コンピュータのターミナルウィンドウで、未知のコードデータが流れる緊張感のある様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "透明性は信頼の核心です。AI企業が技術的な利便性のためにユーザーの情報を密かに収集することは、決して正当化されるべきではありません。"
quiz:
  - question: "「Claude Code」で発見された隠しコードの主な目的は何であると疑われていますか？"
    choices: ["ユーザーのコーディング速度向上", "中国ユーザーの識別および遮断", "AIモデルの性能テスト"]
    answer: 1
    explanation: "報告によると、当該コードはユーザーの地理的位置を検知し、中国のユーザーを識別して遮断するために使用されていた疑いが持たれています。"
  - question: "Anthropicはこの論争に対してどのような立場を取りましたか？"
    choices: ["強く否定し、法的対応を予告", "意図的なスパイ行為であることを認める", "誤解であると釈明し、コードの修正（ロールバック）を発表"]
    answer: 2
    explanation: "Anthropicは当該論争を「誤解」と説明し、直ちに当該コードを削除すると発表しました。"
  - question: "疑惑によると、この隠しコードはユーザー情報をどのように送信しましたか？"
    choices: ["メールで直接送信", "ユーザーのプロンプトメッセージ内に情報を挿入して送信", "クラウドストレージに自動アップロード"]
    answer: 1
    explanation: "このコードは、ユーザーがAIと対話する際に入力するプロンプトメッセージの内部に、ユーザー関連情報を密かに挿入する方式で情報を送信していたという疑いがあります。"
lang: ja
ref: 2026-07-02-Anthropic-embedded-spyware-in-Claude-Code-and-attempted-to-hide-it-from-you
---

想像してみてください。普段愛用しているスマートフォンの翻訳アプリが、実はあなたが外国に行くたびに密かに位置情報を収集していたとしたら、どう感じますか？ユーザーの知らない間にアプリが裏で情報を抜き取っていた事実を知れば、私たちはそのアプリを信じて使い続けることは困難でしょう。最近、世界中の開発者から大きな信頼を得ていたAIコーディングツール「Claude Code」を巡り、これと似た衝撃的な論争が巻き起こりました。

## なぜこれが重要なのか？

今回の事件は、単なる「AI技術」の誤作動の問題を超え、「ユーザーの信頼」の根幹を揺るがす深刻な問題です。Claude Codeは、Anthropicが開発したエージェント（ユーザーの命令を代行するAIソフトウェア）型コーディングツールであり、開発者のコンピュータのターミナルで直接実行され、コードの分析や修正などを行うことで開発生産性を大幅に高めるツールです[Source 8, Source 10]。

多くの開発者にとってClaude Codeは有能な秘書のような存在ですが、この秘書がユーザーの会話を密かに盗み聞きし、特定の国のユーザーを選別して遮断していたという疑惑が浮上したのです。私たちがAIに下すあらゆる命令（プロンプト）に、ユーザーの個人情報が密かに含まれて送信されていたという事実は、AIツールを使うすべての人々にセキュリティとプライバシー保護に対する深い警戒心を呼び起こしています。

## 分かりやすく理解する：フィルターに隠された追跡機

今回の事件を非常に分かりやすく例えるなら、「写真アプリの隠しカメラ」と同じです。素敵な風景を撮るために使う写真アプリに、特定の地域で撮影するときだけ勝手にロゴを埋め込む隠し機能があったと考えてみてください。ユーザー本人は全く知らない間に、です。

この疑惑によれば、AnthropicはClaude Codeというプログラムの内部に隠された「検知コード」を密かに埋め込んでいました[Source 4, Source 7]。このコードはユーザーがどこから接続しているか（地理的位置）を確認します[Source 3]。もしユーザーが中国にいる場合、このコードが作動して当該ユーザーを自動的に遮断します[Source 3]。さらに、ユーザーがAIと対話する際に使用するプロンプトメッセージにユーザー関連情報を密かに混入させ、サーバーに送信していたという疑惑もあります[Source 4, Source 7]。

Redditのあるユーザーは、Anthropicがこのプロセスを隠すためにコードを複雑に難読化していたと主張し、これはユーザーに無断で情報を収集する悪意のあるソフトウェアである「スパイウェア」と何ら変わりないと指摘しました[Source 1, Source 2]。

## 現在の状況

論争が拡大すると、Anthropic側は公式見解を発表しました。AnthropicのClaude Code担当者は当該論争について「すべて誤解から生じたこと」とし、直ちに当該コードを削除すると発表しました[Source 5, Source 7]。実際にAnthropicは当該コードをロールバック（以前の状態に復元）している状況です[Source 7]。

問題のコードは、少なくとも3ヶ月以上Claude Codeの内部に隠されていたとされています[Source 5]。Anthropic側の釈明にもかかわらず、開発者コミュニティは、AIエージェントツールがコンピュータのコードベースを自由に操作する環境において、このような「目に見えない機能」をどのように検証すればよいのかについて、強い疑念を抱いています[Source 9]。

## 今後はどうなるのか？

今回の事件はAI業界全体に「透明性」の重要さを刻み込みました。今後、AIツールが私たちのコンピュータのコードやターミナル環境により深く関与するようになるにつれ、ユーザーはツールが裏でどのような動作を行っているのかを明確に知りたいと望むようになるでしょう。

ユーザーはこれからは、AI開発者が提供する技術的な利便性だけでなく、その背後に隠されたロジックがユーザーの情報を安全に取り扱っているのか、より注意深く観察するはずです。AI企業側も、ユーザーの信頼を失わないために技術的機能を実装する過程で、より高い水準の倫理的透明性を証明しなければならないという重い課題を背負うことになりました。

## MindTickleBytesのAI記者の視点

技術の発展は人間の生活を豊かにしますが、その発展を実現する過程での「隠れた手段」は毒になり得ます。Anthropicの今回の措置が単なる誤解で終わるのか、それともより深い信頼の亀裂をもたらすのかは、今後公開されるコード監査の結果とAnthropicの透明性ある後続措置にかかっています。AI時代における最も強力な武器は技術力ですが、最も重要な資産はユーザーの「信頼」であることを忘れてはなりません。

## 参考資料

1. [Claude Code attempts to detect Chinese users: Fair? | Cybernews](https://cybernews.com/ai-news/claude-code-steganography-china-users/)
2. [Anthropic Secretly Embedded Spyware in Claude Code to Target...](https://freedium-mirror.cfd/https://medium.com/p/35f1442e4278)
3. [Why Anthropic embedded ‘spyware’ in Claude Code and attempted to hide it from users in...](https://timesofindia.indiatimes.com/technology/tech-news/why-anthropic-embedded-spyware-in-claude-code-and-attempted-to-hide-it-from-users-in-/articleshow/132111399.cms)
4. [Anthropic's Claude Code is accused of quietly fingerprinting...](https://digg.com/tech/misirerb)
5. [Anthropic Admits "Claude Code Trojan Incident" Exposure, to...](https://eu.36kr.com/en/p/3876746033934341)
7. [Techmeme: Anthropic says it is rolling back a covert Claude Code...](https://www.techmeme.com/260701/p17)
8. [Claude Code overview - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
9. [Claude Code's Hidden China Signal - RuntimeWire](https://runtimewire.com/article/claude-code-s-hidden-china-signal)
10. [Claude Code by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)
11. [Установка Claude Code на Windows — пошаговый гайд 2026](https://claudeskills.ru/blog/claude-code-windows)