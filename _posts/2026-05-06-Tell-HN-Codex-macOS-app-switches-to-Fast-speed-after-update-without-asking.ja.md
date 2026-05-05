---
layout: post
title: "許可なく「有料コイン」を浪費？Mac用Codexアップデートの驚くべき事態"
description: "最近のmacOS用Codexアプリのアップデート後、ユーザー設定が自動的に「Fast」モードに変更され、利用料金の増加やPCの発熱問題が報告されています。解決方法と注意点を解説します。"
summary: "Mac用Codexアプリがアップデート後、ユーザーの同意なく有料クレジットの消費が1.5倍速い「Fast」モードに設定を変更し、深刻なCPU使用率の上昇を引き起こしています。"
tags: [AI, Codex, OpenAI, macOS, GPT5.5, テクノロジートレンド]
image: 2026-05-06-Tell-HN-Codex-macOS-app-swiches-to-Fast-speed-after-update-without-asking.jpg
image_alt: "PC画面に過負荷を示す警告アイコンとともに、急速に減っていくデジタルコインが描かれている様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ユーザーのコストに直結する設定を事前の告知なく変更したのは、信頼性の面で大きな失策です。技術の性能と同様に、ユーザーの選択権を尊重するUI/UX設計が切実に求められます。"
quiz:
  - question: "最近アップデートされたMac用Codexアプリで、自動的に変更され論議を呼んでいる設定は何ですか？"
    choices: ["言語設定", "ダークモード設定", "速度（Speed）設定"]
    answer: 2
    explanation: "アップデート後、ユーザーの同意なく速度設定が「Standard」から「Fast」に自動変更されたという報告が相次いでいます。"
  - question: "「Fast」モードを使用する際、デジタルクレジット（トークン）は通常よりどれくらい多く消費されますか？"
    choices: ["1.2倍", "1.5倍", "2.0倍"]
    answer: 1
    explanation: "Fastモードは標準モードより約1.5倍多くのクレジットを消費するように設計されています。"
  - question: "アップデートされたCodexアプリがmacOSシステムに与えた影響として正しくないものは？"
    choices: ["CPU使用率の急激な上昇", "PCファンの騒音発生", "バッテリー使用時間の画期的な延長"]
    answer: 2
    explanation: "一部のユーザーはCPU使用率が270%以上に跳ね上がり、ファンが激しく回転してPCが重くなる現象に見舞われています。"
lang: ja
ref: 2026-05-06-Tell-HN-Codex-macOS-app-switches-to-Fast-speed-after-update-without-asking
---

想像してみてください。あなたはいつもの行きつけのカフェに立ち寄りました。いつも通り「いつものをお願いします」と注文したのに、店員は何も聞かずに通常より1.5倍も高い「プレミアム豆」でコーヒーを淹れて出しました。さらに、そのコーヒーを飲んでいる間、カフェのエアコンが故障したかのように室温が急上昇し、滝のような汗が流れ落ちてきたらどうでしょうか？おそらく、困惑を通り越して怒りを感じるはずです。

今、macOS用の人工知能ツールである**Codex**のユーザーの間で、まさにこのようなことが起きています。最近行われたアップデートが、ユーザーの財布とPCの健康を同時に脅かしているというニュースです。最先端のAI技術の裏側に隠された驚くべき事態について、わかりやすく解説します。

## なぜこれが重要なのでしょうか？

今回の事件の核心は、**「ユーザーの選択権」**と**「透明なコスト管理」**です。

私たちがChatGPTやCodexのようなAIを使用するとき、表面上は質問を投げかけているだけのように見えますが、内部的には**「トークン（Token、AIが文字を認識し計算する単位であり、利用料）」**というデジタル通貨を消費しています。これは、スマホのデータ通信量を使ったり、ゲームセンターでコインを入れたりする感覚に非常に似ています。

[Codex – Codex | OpenAI 開発者ドキュメント](https://developers.openai.com/codex/speed)によると、Codexには応答速度を高める「Fast（高速）」モードがあります。**例えるなら**、高速道路で通行料金を余分に払って専用車線を通るようなものですが、このモードをオンにすると、通常よりもトークンを**1.5倍速く**消費することになります。[Tell HN: アップデート後に確認なしでFastスピードに切り替わるCodex macOSアプリ...](https://news.ycombinator.com/item?id=47886763)

問題は、今回のアップデート後、多くのユーザーが自分で設定していないにもかかわらず、アプリが自動的にこの「Fast」モードを有効にしたという点です。[Tell HN: アップデート後に確認なしでFastスピードに切り替わるCodex macOSアプリ...](https://news.bensbites.com/posts/65021-tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking) つまり、ユーザーは知らないうちに、自分の有料クレジットが1.5倍の速さで蒸発していることになります。これは単なる機能変更を超え、ユーザーの資産に直接的な影響を与える深刻な問題です。[Signal Grid — AIニュース・インテリジェンス](https://www.datafeed.news/events/tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)

## わかりやすく解説：「Fast」モードの二面性

今回のアップデートで導入された新しい頭脳、**GPT-5.5モデル**は、間違いなく以前よりも賢く強力になっているでしょう。[Tell HN: アップデート後に確認なしでFastスピードに切り替わるCodex macOSアプリ...](https://news.ycombinator.com/item?id=47886763) しかし、これを動かす方式である「Fast」モードは、いわば車の「スポーツモード」のようなものです。速度は速いですが、ガソリン（コスト）を多く食い、エンジン（PC）に負担をかけます。

### 1. 財布を軽くする恐ろしい速度
「Fast」モードは、AIが回答を出す速度を約1.5倍高めます。[Speed – Codex | OpenAI 開発者ドキュメント](https://developers.openai.com/codex/speed) しかし、「タダより高いものはない」という言葉通り、速度が上がる分、消費されるコストも正確に1.5倍増えます。多くのユーザーが「Standard（標準）」モードを維持し、ゆっくりと節約して使い続けたいと考えているにもかかわらず、アプリが強制的に高コストモードをオンにしてしまった状況は、ユーザーの公憤を買っています。[Tell HN: アップデート後に確認なしでFastスピードに切り替わるCodex macOSアプリ...](https://news.ycombinator.com/item?id=47886763)

### 2. PCを熱くする過負荷
さらに大きな問題はコストだけではありません。PC本体にかかる物理的な衝撃が相当なものです。[macOSでの最新アップデート後にCodexデスクトップアプリがCPUを占有、ファンが回転... - GitHub](https://github.com/openai/codex/issues/18467)に報告された内容によると、アップデートされたアプリは、非常に小さなリクエストを処理する際でも、**CPU（中央演算処理装置、PCの頭脳）**の使用率を**276.5%**まで引き上げます。

これがどれほど深刻な数値か**簡単に言うと**、一人の人間が両手で料理をしているときに、突然見えない手がさらに二本現れて、猛烈な勢いで包丁を使い始めたようなものです。この過程でPCの熱を冷やすファンは、飛行機の離陸音のような音を立てて回り始め、いざ他の作業をしようとするとPC全体がカクつくようになります。[macOSでの最新アップデート後にCodexデスクトップアプリがCPUを占有、ファンが回転... - GitHub](https://github.com/openai/codex/issues/18467)

## 現在の状況：「速いと言ったのに、なぜもっと遅いのか？」

逆説的ですが、「Fast」モードに設定されているにもかかわらず、実際の体感性能はむしろ低下したという不満が噴出しています。[Codexの新しいスピード機能。あなたの経験は？](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408) あるユーザーは、アップデート前よりも性能が**2倍も遅くなったようだ**と困惑を露わにしました。[Codexの新しいスピード機能。あなたの経験は？](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408)

これに加え、ソフトウェアの完成度の問題も次々と露呈しています。
- **表と裏で異なる設定**: 設定ファイル（`config.toml`）で速度を変更しても、コマンドラインツール（CLI）には反映されますが、肝心のMac用アプリの画面には反映されないという「ちぐはぐ」な現象が発見されました。[Codexアプリが/fastモードの状態を誤報している ・ Issue #14689 ・ openai/codex](https://github.com/openai/codex/issues/14689)
- **アプリの不安定さ**: 一部のプロジェクトでは、アプリが全く動作しなかったり、「完全に壊れた（completely broken）」状態になったりして、業務に支障をきたすケースもありました。[Redditのr/codex：最新のmacOS版Codexアプリにアップグレードしたら完全に壊れた](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)

## 今後はどうなるのか？

現在、多くのユーザーが今回のアップデートを技術的進歩ではなく「災難」に近いものと受け止めています。もしあなたがMacでCodexを使用しているなら、今すぐ自分のPCと財布を守るために、以下の措置を確認することをお勧めします。

### 読者のための実践的なヒント：
1. **設定値を直ちに確認**: アプリの設定メニューで速度が「Fast」になっていないか確認してください。意図しないコスト発生を防ぐには、必ず「Standard」に戻す必要があります。ただし、再起動後に設定が元に戻るバグが報告されているため、随時チェックが必要です。[再起動後にCodexアプリの速度設定がFastからStandardにリセットされる ・ Issue #20769 ・ openai/codex](https://github.com/openai/codex/issues/20769)
2. **以前のバージョンに戻す**: 現在のバージョンが使い物にならないほど不安定な場合は、検証済みの以前のバージョン（26.217.1959など）にダウングレードするのが賢明な選択かもしれません。[Redditのr/codex：最新のmacOS版Codexアプリにアップグレードしたら完全に壊れた](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)
3. **システムリソースの監視**: 「アクティビティモニタ」を通じて、CodexアプリがCPUを過剰に消費していないか監視してください。ファンの音が急に大きくなったら、アプリを一度終了して再起動することをお勧めします。

AI技術の発展により私たちの生活は確実に便利になっていますが、同時にユーザーの制御を離れたコスト発生やシステム過負荷の問題は今後も続く可能性があります。賢いAIを使うことと同じくらい、その技術が度を越さないよう監視する私たちの目も、より鋭くあるべき時です。

---

## AIの視点
**「速度が革新を証明する唯一の尺度ではありません。」**
開発元としては、新しいモデルの強力さを体感させるために「Fast」モードをデフォルト設定にしたのでしょう。しかし、ユーザーのデジタル資産（トークン）と物理的リソース（PC性能）を尊重しないやり方は、結局のところ信頼の崩壊を招きます。技術的な完成度と同じくらい、ユーザーの選択権を保護する倫理的なUI/UX設計がAI時代の新しい標準であるべきだということを、今回の事態は如実に示しています。

---

## 参考資料
1. [Tell HN: アップデート後に確認なしでFastスピードに切り替わるCodex macOSアプリ...](https://news.ycombinator.com/item?id=47886763)
2. [Signal Grid — AIニュース・インテリジェンス](https://www.datafeed.news/events/tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)
3. [Tell HN: アップ데이트後に確認なしでFastスピードに切り替わるCodex macOSアプリ...](https://news.bensbites.com/posts/65021-tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)
4. [Tell HN: アップデート後に確認なしでFastスピードに切り替わるCodex macOSアプリ...](https://alt-hn.vercel.app/item/47886763)
5. [Codexの新しいスピード機能。あなたの経験は？](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408)
6. [macOSでの最新アップデート後にCodexデスクトップアプリがCPUを占有、ファンが回転... - GitHub](https://github.com/openai/codex/issues/18467)
7. [Speed – Codex | OpenAI 開発者ドキュメント](https://developers.openai.com/codex/speed)
8. [再起動後にCodexアプリの速度設定がFastからStandardにリセットされる ・ Issue #20769 ・ openai/codex](https://github.com/openai/codex/issues/20769)
9. [Redditのr/codex：最新のmacOS版Codexアプリにアップグレードしたら完全に壊れた](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)
10. [Codexアプリが/fastモードの状態を誤報している ・ Issue #14689 ・ openai/codex](https://github.com/openai/codex/issues/14689)

## FACT-CHECK SUMMARY
- Claims checked: 12
- Claims verified: 10
- Verdict: PASS