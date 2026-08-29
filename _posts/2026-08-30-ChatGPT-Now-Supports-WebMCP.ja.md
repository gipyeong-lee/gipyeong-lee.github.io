---
layout: post
title: "AIがウェブサイトの「従業員」に？ChatGPTの新たな変化、WebMCP"
description: "ChatGPTデスクトップアプリが対応を開始したWebMCP技術とは何か、そしてこれが私たちの日常やウェブブラウジング体験をどう変えるのか、分かりやすく解説します。"
summary: "ChatGPTデスクトップアプリがWebMCP標準を導入したことで、AIがウェブサイトの機能を直接制御し、業務を代行できる道が開かれました。"
tags: [AI, ChatGPT, WebMCP, ウェブ技術]
image: 2026-08-30-ChatGPT-Now-Supports-WebMCP.jpg
image_alt: "ChatGPTデスクトップアプリのウェブブラウジング画面と、AIがウェブサイトのツールを直接操作する様子を示す技術的なグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "WebMCPは、AIが単に文章を読むだけでなく、実際のウェブサイトの中で行動できるようにするための重要な架け橋です。ただし、真の自動化を実現するためには、信頼性の高いツール設計が不可欠となるでしょう。"
quiz:
  - question: "WebMCPが導入された後、ChatGPTデスクトップアプリで期待できる変化は何ですか？"
    choices: ["AIが直接ウェブサイトのツールを呼び出して業務を遂行する", "ウェブサイトのデザインをリアルタイムで変更する", "インターネット接続なしでブラウジングが可能になる"]
    answer: 0
    explanation: "WebMCPは、AIがウェブサイト内の機能を発見して直接呼び出し、商品購入や予約など、さまざまな作業を代行できるようにする標準技術です。"
  - question: "WebMCP機能を使用するために必要なものは何ですか？"
    choices: ["ChatGPT Enterpriseアカウント", "最新バージョンのChatGPTデスクトップアプリ", "ウェブサイトの管理者権限"]
    answer: 1
    explanation: "WebMCPを通じたサイトツール機能は最新バージョンのChatGPTデスクトップアプリでサポートされており、現在EnterpriseやEduワークスペースでは利用できません。"
  - question: "WebMCP技術の現在の段階に関する説明として正しいものはどれですか？"
    choices: ["すでに世界中のあらゆるウェブサイトで完璧に動作している", "実験的な段階であり、導入の初期である", "これ以上アップデートされない技術である"]
    answer: 1
    explanation: "WebMCPは現在実験的な段階であり、実際のサービスに適用され始めた初期段階であるため、今後の発展の可能性や採用範囲を見守る必要があります。"
lang: ja
ref: 2026-08-30-ChatGPT-Now-Supports-WebMCP
---

想像してみてください。朝起きてスマートフォンを開き、AIにこう言います。「この前チェックしたあのスニーカー、今セール中なら私のサイズで決済しておいて」。以前のAIであれば、商品ページのURLを見つけて価格情報を教えてくれる程度でしたが、これからはAIが自らショッピングサイトにアクセスし、「カートに入れる」から「決済」までを実行できる時代が訪れようとしています。

先日OpenAIは、ChatGPTデスクトップアプリの内蔵ブラウザに、**WebMCP(Web Model Context Protocol、ウェブ・モデル・コンテキスト・プロトコル)**という技術を導入したと発表しました。 [[出典: ChatGPT Now Supports WebMCP](https://news.ycombinator.com/item?id=49473417)] [[出典: OpenAIがデスクトップアプリでWebMCPをサポート、ウェブとAIの統合を深めます](https://gigazine.net/gsc_news/en/20260826-chatgpt-webmcp/)] 名前からして耳慣れないこの技術が一体何なのか、なぜ重要なのか、今から分かりやすく解説します。

## これがなぜ重要なのか？

これまで私たちが使ってきたAIは、主に「しゃべる図書館」のようなものでした。膨大な情報を検索して整理することはできましたが、実際にウェブサイト内でクリックしたりボタンを押したりするような「行動」をとることには限界がありました。

しかし、WebMCPが導入されたことで、AIは単なる相談役を超え、「ウェブサイトの従業員」のように働けるようになりました。 [[出典: WebMCPはAIエージェントをウェブサイト内の行動と接続します](https://www.searchenginejournal.com/webmcp-connects-ai-actions-inside-websites/587303/)] ショッピングサイトで商品を注文したり、レストランを予約したり、複雑なデータ検索を実行したりと、ユーザーがいちいちウェブサイトを巡回して行わなければならなかった反復作業を、AIが代行できるようになるのです。これは、私たちがデジタル機器を使う方法そのものが変わり得ることを意味します。 [[出典: ChatGPTデスクトップアプリにWebMCPサポートを追加](https://finance.biggo.com/news/6315a82e-acff-4f1d-bcd9-3a9501a125e8)]

## 分かりやすい例え：AIのためのレストランマニュアル

WebMCPを理解するために、「レストラン」を例に挙げてみましょう。

一般的なウェブサイトは、美味しい料理を作るレストランのようなものです。しかしこれまでのAIは、客ではなくレストランの外に立っている人だったため、店の中に入ることができませんでした。客が窓の外から「そこのメニューを見せて」と言えば、店主がメニューを持ってきてくれるという形でした。

しかし、**WebMCPは、このレストランに「AI専用の入り口」と「作業マニュアル」を作るようなものです**。AIがウェブサイト（レストラン）に訪問すれば、店内の構造を把握し、どのボタン（調理器具）を押せば注文が入るのか、どうやって決済するのか（料理の作り方）をマニュアル通りに実行できるようになるのです。 [[出典: Let AI agents drive your game servers with WebMCP](https://nodecraft.com/blog/development/letting-ai-agents-drive-your-game-servers-with-webmcp)]

簡単に言えば、AIがウェブサイト側で公開されているツール（Site Tools）を発見し、人間がクリックするように直接呼び出して、必要な作業を即座に処理できる通路を設けたことになります。 [[出典: ChatGPTの内蔵ブラウザがWebMCPをサポートします](https://www.linkedin.com/posts/igrigorik_chatgpt-built-in-browser-now-speaks-webmcp-activity-7498123362104360960-1V5E)]

## どこで使えるのか？

現在、この機能はChatGPTデスクトップアプリの内蔵ブラウザで提供されています。ユーザーは最新バージョンにアプリをアップデートするだけで、WebMCPをサポートしているウェブサイトにおいて、AIがツールを活用する機能を体験できます。 [[出典: Site tools | ChatGPT Learn](https://learn.chatgpt.com/docs/webmcp)]

もちろん、まだどこでも完璧に動作するわけではありません。導入初期の段階であり、実際のサービスに適用され始めたばかりであるため、すべてのウェブサイトがこの技術をサポートしているわけではないからです。 [[出典: WebMCPはAIエージェントをウェブサイト内の行動と接続します](https://www.searchenginejournal.com/webmcp-connects-ai-actions-inside-websites/587303/)] また現在、企業向け（Enterprise）や教育向け（Edu）ワークスペースではまだこの機能を使えないという制約もあります。 [[出典: Site tools | ChatGPT Learn](https://learn.chatgpt.com/docs/webmcp)] 専門家たちは、AIがウェブサイトをよりうまく活用するためには、ウェブサイト自体が構造を明確にしておくことが何よりも重要だと強調しています。 [[出典: ChatGPTの内蔵ブラウザがWebMCPをサポートします](https://www.linkedin.com/posts/igrigorik_chatgpt-built-in-browser-now-speaks-webmcp-activity-7498123362104360960-1V5E)]

## 今後の展望

今後はさらに多くのウェブサイトが、AIが簡単に訪れて業務を行えるよう、自らのサービス構造を公開していくものと見られます。開発者たちはすでにWebMCPを活用して様々なサイトツールを作っており、OpenAIもまた開発者のためのハッカソンを開催してエコシステムを拡大しています。 [[出典: ChatGPTのウェブブラウザがWebMCPサポートと新しい基本機能を得ました](https://daily.dev/posts/chatgpt-s-web-browser-gets-webmcp-support-and-new-primitives-hnhtsdeii)]

私たちは次第に「アプリを直接クリックする時間」を減らし、「AIに何をすべきか指示する時間」を増やすようになるでしょう。皆さんがよく利用するウェブサイトにAIのための「従業員用入り口」ができたかどうか確認してみるのも、興味深い体験になるはずです。

---

## 参考資料

1. [ChatGPT Now Supports WebMCP | Hacker News](https://news.ycombinator.com/item?id=49473417)
2. [Letting AI agents drive your game servers with WebMCP - Nodecraft](https://nodecraft.com/blog/development/letting-ai-agents-drive-your-game-servers-with-webmcp)
3. [ChatGPT built-in browser now speaks WebMCP and millions of... | LinkedIn](https://www.linkedin.com/posts/igrigorik_chatgpt-built-in-browser-now-speaks-webmcp-activity-7498123362104360960-1V5E)
4. [ChatGPT Now Supports WebMCP | Modern Orange](https://modernorange.io/item/49473417)
5. [WebMCP Connects AI Agents To Actions Inside Websites | Search Engine Journal](https://www.searchenginejournal.com/webmcp-connects-ai-actions-inside-websites/587303/)
6. [10 days for exploring what’s possible with WebMCP](https://webmcp.devpost.com/resources)
7. [🚨 Breaking 🚨 ChatGPT Now Supports WebMCP - by nekuda](https://nekuda.substack.com/p/breaking-chatgpt-now-supports-webmcp)
8. [Site tools | ChatGPT Learn](https://learn.chatgpt.com/docs/webmcp)
9. [WebMCP, which deepens the integration of AI and websites, now supports ChatGPT for desktop. - GIGAZINE](https://gigazine.net/gsc_news/en/20260826-chatgpt-webmcp/)
10. [ChatGPT Adds WebMCP Support for Site Tools | Digg](https://digg.com/tech/51drxazj)
11. [ChatGPT Desktop App Adds WebMCP Support; OpenAI Introduces Premium Seat for Business Users — BigGo Finance](https://finance.biggo.com/news/6315a82e-acff-4f1d-bcd9-3a9501a125e8)
12. [ChatGPT's Web Browser Gets WebMCP Support and New Primitives | daily.dev](https://daily.dev/posts/chatgpt-s-web-browser-gets-webmcp-support-and-new-primitives-hnhtsdeii)
13. [OpenAI Status](https://status.openai.com/)