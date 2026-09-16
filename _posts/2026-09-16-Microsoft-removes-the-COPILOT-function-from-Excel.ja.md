---
layout: post
title: "Excelのセルに直接問いかけるAI関数、もうおさらば？"
description: "Excelのセルに直接コマンドを入力してデータを分析していた「=COPILOT()」関数が、2026年9月14日をもってサービス終了となります。今後はどのような方法でExcelでAIを活用できるのかをまとめました。"
summary: "Excelのセル内に直接自然言語を入力してAIから回答を得ていた「=COPILOT()」関数が、導入から1年を経てプレビュー版のままサービス終了となります。"
tags: [Microsoft, Excel, AI, Copilot, 生産性]
image: 2026-09-16-Microsoft-removes-the-COPILOT-function-from-Excel.jpg
image_alt: "Excel画面上で「=COPILOT()」関数が入力されたセルと、その横に表示されたAIの回答ウィンドウを示す画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "新しい機能が実験段階で整理されるのは、AIプラットフォームの戦略的効率化のための自然な過程です。サイドパネルを中心とした環境の方が、ユーザーにとってより直感的な体験を提供できるでしょう。"
quiz:
  - question: "「=COPILOT()」関数はいつから使用できなくなりましたか？"
    choices: ["2026年4月15日", "2026年9月14日", "2027年1月1日"]
    answer: 1
    explanation: "Microsoftは2026年9月14日をもって当該関数のサポートを終了しました。"
  - question: "今後はExcelでAIの支援を受けるためにどの機能を使用すべきですか？"
    choices: ["サイドパネル(Side pane)", "新しい「=AI()」関数", "外部の別プログラム"]
    answer: 0
    explanation: "Microsoftは今後、セル関数ではなく、Excelの「サイドパネル」を通じてAI作業を行うよう案内しています。"
  - question: "「=COPILOT()」関数はどれくらいの期間テストされましたか？"
    choices: ["約1ヶ月", "約6ヶ月", "約1年"]
    answer: 2
    explanation: "2025年8月に初めて紹介されてから約1年間、プレビューテストの過程を経ました。"
lang: ja
ref: 2026-09-16-Microsoft-removes-the-COPILOT-function-from-Excel
---

想像してみてください。複雑な表を前にして、Excelのセルに魔法の呪文を唱えるかのように「このデータで平均売上グラフを描いて」と入力すると、実際にAIが現れて問題を解決してくれる状況を。この1年間、Excelユーザーの間で実験的に導入されていた`=COPILOT()`関数は、まさにそのような利便性を提供しようとしていました。しかし残念なことに、今、私たちはこの「セルの中のAI」とお別れする時が来ました。

### なぜこれが重要なのか？

日常的にExcelを使用するアナリストやビジネスパーソンにとって、今回の変更は非常に大きな意味を持ちます。`=COPILOT()`関数は、ユーザーがExcelの特定のセルに自然言語で質問を投げかけ、データを参照して結果を得られるように設計されたツールでした。[Microsoft Support](https://support.microsoft.com/en-us/excel/functions/copilot-function)の説明によると、この機能はユーザーが数式をいちいち覚えなくても、AIを通じて結果をすぐにセルに入力できるようにする革新的な試みでした。

しかし今回のサービス終了のニュースは、単に一つの機能を削除することを超えて、Microsoftが自社のAI戦略をどのように調整しているかを示しています。多くの期待を集めていた[2027年の正式公開予定](https://www.techradar.com/pro/microsoft-is-dropping-its-excel-copilot-function-after-only-a-year-and-without-ever-getting-a-full-public-launch)が白紙となり、プレビュー期間を終えただけで歴史の彼方へと消えることになったからです。

### わかりやすい解説

なぜこのような関数を廃止するのでしょうか？次のように例えるとわかりやすいでしょう。あなたがリビングでテレビを見るとき、「リモコン」が2種類あると考えてみてください。一つはテレビ画面の端に大きく表示される「スマートホーム制御パネル」で、もう一つはテレビリモコンの小さな「数字ボタン」に直接入力して命令する方式です。

これまでの`=COPILOT()`関数は後者に近いものでした。セルという狭い空間に直接コマンドを入力する方式でしたね。しかし、MicrosoftはExcel画面の横に常に表示される「サイドパネル（Side pane）」方式を優先することに決定しました。簡単に言えば、複雑な命令はセルという狭い空間よりも、データ全体を俯瞰できるサイドパネルでやり取りする方がはるかに効率的だと判断したのです。狭い手帳にメモするよりも、ホワイトボード全体を活用する方がアイデアを共有しやすいのと似ています。

サイドパネルは、私たちがデータを操作する途中で別ウィンドウを開くことなく、すぐ横で対話を行える環境を提供します。これは、Excelを使用している間、作業の流れ（フロー）を中断することなくAIの支援を継続的に受けられる「共に作業するパートナー」のような構造です。一方、セルに入力する方式は結果だけがぽつんと置かれる形になるため、データの全体的な文脈をAIと共有しながら発展させるには多くの制約がありました。

### 現在の状況

Microsoftはこの機能を[2025年8月に初めて紹介](https://www.theregister.com/ai-and-ml/2026/08/17/excels-copilot-function-is-headed-for-the-recycle-bin/5288327)し、約1年間「インサイダー（Insider）」や「フロンティア（Frontier）」プログラムの参加者を対象にテストを行ってきました。しかし[2026年9月14日](https://www.linkedin.com/posts/billjelen_the-short-lived-copilot-function-made-for-activity-7495425203603226624-D6fH)をもって、当該機能は正式に終了しました。現在、この関数を呼び出してもAIは反応しません。

もちろん、ExcelからAIが完全に消えるわけではありません。Microsoftは既存のユーザーに対し、[サイドパネルを使用](https://m365admin.handsontek.net/frontier-copilot-function-excel-will-no-longer-available/)して同様のAI支援を受けることを推奨しています。アナリストは今、セルに数式を書く代わりに、サイドパネルを通じてより広い視野でAIと対話しながらデータを分析することになるでしょう。

### 今後はどうなるのか？

突然の機能削除により、これまで`=COPILOT()`関数をベースにマニュアルを作成したり、業務プロセスを構築していた企業は少し当惑するかもしれません。[一部の専門家は](https://www.refontelearning.com/blog/copilot-in-excel-feature-retired)、関連文書や内部ガイドを直ちに修正する必要があるとアドバイスしています。新しい業務スタイルに適応する過程で一時的な混乱があるかもしれませんが、サイドパネルという安定したプラットフォームへの移行は、長期的にはより優れた分析環境を構築するものと考えられます。

今後、MicrosoftはExcelだけでなくOffice製品群全体において、AIをより統合された形態で提供していく見通しです。今回の変化は「実験的なセル内関数」から「プラットフォーム全体を網羅するサイドパネル」への方向転換を意味します。私たちユーザーも変化する環境に合わせて、Excelインターフェース内でAIをより効果的に操作する方法を学ぶ時期に来ています。これは、マニュアル車からオートマ車に乗り換えるときのように、最初は少し慣れが必要ですが、慣れてしまえばはるかに快適な作業を体験できる変化といえるでしょう。

### MindTickleBytesのAI記者による視点

「セルの中のAI」というアイデアは非常に斬新でしたが、実際のワークシート環境ではより直感的なインターフェースが必要であったことを今回の事例が示しています。機能の撤退は失敗ではなく、より優れたユーザー体験（UX）を目指す進化の過程だと考えます。技術は進化を続け、私たちにとって最も適した場所を見つけ出している最中です。

## 参考資料

1. [Microsoft Cancels COPILOT Function in Excel | Bill Jelen... | LinkedIn](https://www.linkedin.com/posts/billjelen_the-short-lived-copilot-function-made-for-activity-7495425203603226624-D6fH)
2. [Microsoft Copilot | Windows Central](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot)
3. [Microsoft removes the COPILOT function from Excel | Hacker News](https://news.ycombinator.com/item?id=49706481)
4. [Microsoft is pulling the plug on Excel’s COPILOT function after...](https://tech.yahoo.com/ai/copilot/articles/microsoft-pulling-plug-excel-copilot-130240084.html)
5. [Frontier =COPILOT function in Excel will no longer available...](https://m365admin.handsontek.net/frontier-copilot-function-excel-will-no-longer-available/)
6. [Microsoft Kills Free Copilot Chat in Word, Excel and... - Office Watch](https://office-watch.com/2026/microsoft-removes-copilot-chat-word-excel-powerpoint-april-2026/)
8. [COPILOT Function | Microsoft Support](https://support.microsoft.com/en-us/excel/functions/copilot-function)
11. [Microsoft is ditching the COPILOT function in Excel before it even launches](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-is-ditching-the-copilot-function-in-excel-before-it-even-launches)
12. [Microsoft Pulls the Plug on Excel's COPILOT Function After One Year](https://mangodeveloper.com/articles/microsoft-pulls-the-plug-on-excels-copilot-function-after-one-year)
13. [Microsoft Just Killed a Copilot Excel Feature in 2026](https://www.refontelearning.com/blog/copilot-in-excel-feature-retired)
15. [Microsoft is dropping its Excel Copilot function after only a year - and without ever getting a full public launch | TechRadar](https://www.techradar.com/pro/microsoft-is-dropping-its-excel-copilot-function-after-only-a-year-and-without-ever-getting-a-full-public-launch)
16. [Excel's Copilot function is headed for the Recycle Bin](https://www.theregister.com/ai-and-ml/2026/08/17/excels-copilot-function-is-headed-for-the-recycle-bin/5288327)
18. [Microsoft is scrapping the =COPILOT function from Excel after only a year since its release](https://www.xda-developers.com/microsoft-is-scrapping-the-copilot-function-from-excel-after-only-a-year-since-its-release/)
19. [Microsoft is dropping its Excel Copilot function after only a year - and without ever getting a full public...](https://tech.yahoo.com/ai/copilot/articles/microsoft-dropping-excel-copilot-function-100500958.html)
20. [Excel's Copilot Function Is Headed for the Recycle Bin](https://ground.news/article/microsoft-is-retiring-excels-copilot-function-after-just-one-year)