---
layout: post
title: "アーク(Arc) ブラウザが消える？上海の高校生がたった3週間で作った奇跡のMacブラウザ「ジグザグ(Zigzag)」"
description: "2026年12月で終了するアークブラウザの代替として、上海の高校生開発者がSwiftとWebKitでわずか3週間で開発した超軽量Macブラウザ「ジグザグ(Zigzag)」のすべて。"
summary: "アークブラウザ終了のニュースにショックを受けた上海の高校生がたった3週間で開発した、18MBの超軽量Macブラウザ「ジグザグ(Zigzag)」の特徴と開発の舞台裏。"
tags: [Zigzag, Arc, MacBrowser, WebKit, OpenSource]
image: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc.jpg
image_alt: "Macの画面に表示された、すっきりしたサイドバーとスプリットビュー機能を備えたジグザグブラウザのインターフェース画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "大企業のサービス終了決定に挫折せず、自らのコーディングで答えを見つけ出した高校生開発者の執念が光ります。重厚長大化した現代のブラウザエコシステムに一石を投じる軽量な代案です。"
quiz:
  - question: "ジグザグ(Zigzag)ブラウザを開発した開発者の背景は何ですか？"
    choices: ["シリコンバレーのベテランブラウザエンジニア", "上海出身の高校生", "ヨーロッパのオープンソース研究者"]
    answer: 1
    explanation: "ジグザグは、上海出身の高校生開発者ZigaoWangがアークブラウザの終了ニュースにショックを受けて、たった3週間で自ら開発したブラウザです [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
  - question: "ジグザグブラウザが基盤としているAppleのエンジンは何ですか？"
    choices: ["Chromiumエンジン", "WebKitエンジン", "Geckoエンジン"]
    answer: 1
    explanation: "ジグザグは、ChromiumやElectronではなく、Appleの純粋なWebKitエンジンとSwift言語で制作されています [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
  - question: "ジグザグブラウザのインストール容量はおよそどれくらいですか？"
    choices: ["約 18 MB", "約 871 MB", "約 1.5 GB"]
    answer: 0
    explanation: "ジグザグは不要な重さをそぎ落とし、約 18 MBという超軽量なインストール容量を誇ります [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
lang: ja
ref: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc
---

想像してみてください。毎朝パソコンを立ち上げて仕事やプライベートの整理をする際、自分にぴったりの特製引き出しのようにきれいに整理されたブラウザウィンドウを開きます。数多くのタブが横に並んでごちゃごちゃしていた過去とは異なり、画面のサイドに優雅に陣取るサイドバーとスペース（Space）ごとの分類は、デジタル作業の新世界でした。そんなある日、青天のへきれきのニュースが飛び込んできます。「あなたが毎日使っているそのブラウザが、間もなく幕を閉じます。」

開発元のThe Browser Companyが、革新的なインターフェースで世界中のユーザーから愛されたアーク（Arc）ブラウザを2026年12月22日までのサポートをもって完全に終了すると発表しました [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)。このニュースにMacユーザーは大きな混乱に陥りました。退屈な上部の横タブ方式にはもう戻れなかったからです [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。まさにその時、地球の反対側から一人の高校生開発者がこの絶望的な状況に真っ向から挑戦状を叩きつけました。たった3週間でアークユーザーが恋しがるすべての要素を詰め込んだ超軽量Macブラウザ、**ジグザグ（Zigzag）**が誕生したのです [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## なぜこれが重要なのか？

現代のウェブブラウザはますます重くなっています。数多くの機能を詰め込んでいるためRAMをブラックホールのように食いつぶし、バッテリーを猛スピードで消耗し、プログラムのインストール容量だけで数百メガバイトからギガバイトを超えることもしばしばです。実際に終了を控えたアークブラウザは、インストール容量が800MBを軽く超えています [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

一般ユーザーの立場からすれば、ちょっとウェブサーフィンをするためにパソコンのリソースの大部分をブラウザに明け渡さなければならないわけです。おまけに大企業のサービスが終了すれば、ユーザーは理由も分からないまま使い慣れたツールを失い、別の代替案を探してさまようことになります。

ジグザグは、こうした現代ソフトウェアの巨大さと閉鎖性に真っ向から反旗を翻します。インストール容量がわずか**18 MB**に過ぎず [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)、アカウント登録も不要で、テレメトリー（ユーザー行動追跡データ）や解析ツールを一切排除することで完全なプライバシーを保証しています [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。個人が作ったオープンソースプロジェクトであるため、誰も勝手にサービスを中断させることはできず、誰でもコードを修正し発展させることができます [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## わかりやすい解説：Macに最適化された専用スポーツカーを作る

例えるならこうです。既存の多くのブラウザが巨大なバスエンジンを積んであちこちに重い荷物を運ぶ大型トラックだとしたら、ジグザグはMacという精巧な道路構造に合わせて削り出された、軽快な軽量電気スポーツカーに例えることができます。要するに、不要な重さを思い切って削ぎ落とし、本当に必要な中核の走行性能にのみ特化したということです。

ジグザグは、GoogleのChromium（Chromeブラウザの骨組みとなるオープンソースエンジン）エンジンやElectron（ウェブ技術でデスクトップアプリを作れるようにするフレームワーク）をベースにした重いブラウザではありません [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。AppleがmacOSに標準搭載している純粋な**WebKit（ウェブページを画面に描画するコアエンジン）**エンジンを活用し、Mac専用のプログラミング言語である**Swift（Apple製デバイス向けアプリを作るプログラミング言語）**でゼロから書き上げられました [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

スマートフォンに写真加工アプリを入れるとき、どんな機種でも適当に動く重い汎用プログラムを使うより、iPhoneのコアシステム機能を直接活用して作った専用カメラアプリのほうが圧倒的に速く、バッテリー消費も少ないのと同じ理屈です。おかげで無駄なく軽快で、macOSと完全に一体化したかのような滑らかさを提供します。

ここに、アークブラウザのユーザーが最も熱狂したコア機能も余すところなく受け継がれています。
- **サイドバーとスペース（Spaces）**: ウィンドウの上部ではなく左側に縦に並ぶタブと、仕事用やプライベート用などで色を分けてスワイプしながら行き来できる空間管理機能 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
- **スプリットビュー（Split View）**: 1つのウィンドウで最大4つのページを同時に表示してマルチタスクを行える画面分割機能 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
- **ピーク（Peek）およびコマンドバー**: リンクを新しいウィンドウで開かずに軽くプレビューできるクイックリンクのプレビュー機能と、高速なコマンド実行バー [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)

---

## 現在の状況：たった3週間の開発、そして完璧な移行

この驚異的なブラウザを作り上げた主役は、上海出身の高校生開発者**ZigaoWang**です [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。彼は普段からアークブラウザを毎日愛用し、何の不満もなく満足していたため、The Browser Companyの突然の終了発表に大きなショックを受けたと明かしています [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。「再び退屈な上部タブに戻りたくない」というシンプルかつ強力な動機から、彼は過去3週間にわたって自らキーボードを叩き、ジグザグを設計しました [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

ユーザーが既存のブラウザから乗り換える際に直面する最大の苦痛は、「設定やログイン情報を再びセッティングする面倒臭さ」です。しかしジグザグはこの問題をワンクリックで解決しました。アークを含む他のブラウザから一度インポート（他のプログラムのデータを読み込む機能）を実行すれば、使用していたスペース、ピン留めされたタブ、閲覧履歴、保存されたパスワード、クッキーなどが丸ごと移行されます [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。ブラウザを立ち上げるやいなや、これまで利用していたウェブサイトにすぐにログインした状態で作業を続けることができます [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3)。

特にWebKitエンジンベースでありながら、**Chromeウェブストア（Chrome Web Store、Google Chromeの拡張機能をダウンロードするオンラインストア）**の拡張機能を直接インストールできる点は圧倒的な強みです [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。1PasswordやBitwardenなどのパスワードマネージャー、Dark Reader（ダークモード）、Return YouTube Dislike、Tampermonkeyなど、普段愛用している必須の拡張機能をそのまま持ち込んで使うことができます [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

さらに、uBlock OriginやEasylistフィルターに基づいた**強力な内蔵広告ブロック機能**が標準搭載されており、画面を邪魔する面倒なクッキーの同意ポップアップウィンドウを自動で拒否処理して視界から排除してくれます [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## 今後どうなるのか？

アークブラウザの公式サポート終了日である2026年12月22日が近づくにつれて [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)、代替案を探すユーザーの動きは一層慌ただしくなるでしょう。ウェブの巨人が主導するブラウザ市場において、高校生開発者がオープンソースとして発表したジグザグは、大企業中心のエコシステムに小さな地殻変動を起こしています。

ユーザーはもはや巨大企業の一方的なサービス終了通知に振り回される必要はありません。ソースコードが公開されており、誰でも貢献できるオープンソースプロジェクトであるだけに [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)、世界中の開発者が集まってさらに堅牢で安全なMac専用ブラウザへと成長していく可能性が高いです。軽くて速く、自分のプライバシーを守ってくれる自分だけのウェブサーフィン空間を探しているなら、ジグザグは来る冬の最も魅力的な選択肢となるでしょう。

---

## AIの視点

MindTickleBytesのAI記者による視点：技術の進歩は必ずしも巨大資本と数百人のエンジニアからのみ生まれるわけではありません。不便さに甘んじることなく、わずか3週間でコードによって解決し切った一人の高校生の情熱は、ソフトウェア本質的価値とは何かを私たちに思い出させてくれます。重厚長大化したビッグテックのサービスに疲労感を感じているなら、ジグザグのような軽やかで透明なオープンソースの躍進に注目してみるべきタイミングです。

---

## 参考資料

1. [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
2. [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
3. [Zigzag: A Lightweight Web Browser for Mac](https://zigzagbrowser.com/)
4. [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)
5. [[5-Minute Review] The Mac browser 'Zigzag Browser' that lets ...](https://note.com/1sht0s/n/n5aa2825dac32?hl=en)
6. [Hacker News => Show](https://www.hacker-news.news/Show)
7. [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)
8. [byearc: newbrowserssto replaceArc](https://byearc.com/)
9. [DownloadArc](https://arc.net/download)
10. [DiaBrowserReview 2026: Is It Worth It? Pricing vsArc| Macfolio](https://macfolio.com/blog/dia-browser-review)
11. [ZigzagBrowser: The polished,nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3)
12. [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)