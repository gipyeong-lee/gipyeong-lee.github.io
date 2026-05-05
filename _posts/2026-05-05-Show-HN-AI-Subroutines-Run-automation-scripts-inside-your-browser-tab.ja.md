---
layout: post
title: "毎回AIに課金しますか？『一度教えるだけ』で無料で無限に繰り返す『AIサブルーチン』が登場"
description: "AIが毎回考えて行動する代わりに、人間が行った動作を『サブルーチン』として保存し、コストや遅延なくブラウザ内で直接実行する rtrvr.ai の新しい自動化技術を紹介します。"
summary: "人間のブラウザ作業をたった一度記録するだけで、その後はAI呼び出しコスト（トークン）や待ち時間なしに無限に繰り返してくれる賢いマクロ『AIサブルーチン』が公開されました。"
tags: [AI, 自動化, ブラウザ, rtrvr, ウェブエージェント]
image: 2026-05-05-Show-HN-AI-Subroutines-Run-automation-scripts-inside-your-browser-tab.jpg
image_alt: "ブラウザタブの中で複雑な作業が自動的に実行される様子を可視化したイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "考えるAIよりも『よく学習された』スクリプトの方が、はるかに経済的で正確な場合があります。AIサブルーチンは、まさにそのポイントを的確に突いています。すべてをAIの知能に任せるのではなく、知能によって作られた『最適パス』を技術で固定することこそが、真の効率化です。"
quiz:
  - question: "AIサブルーチン（AI Subroutines）の最大の特徴は何ですか？"
    choices: ["実行するたびに高額なAIトークン費用がかかる。", "作業を一度記録すれば、追加費用や遅延なしに無限に繰り返す。", "人間の介入が一切なく、AIが自らすべてを判断する。"]
    answer: 1
    explanation: "AIサブルーチンは、記録された作業を決定論的スクリプトに変換して実行するため、追加のトークン費用やAI推論の遅延が発生しません。"
  - question: "AIサブルーチンが既存のAIエージェントより優れている点は何ですか？"
    choices: ["セキュリティ認証（ログイン状態など）を自動的に活用する。", "複雑な論理的推論を常に実行する。", "常に新しい方法で仕事を処理する。"]
    answer: 0
    explanation: "ブラウザタブの内部で実行されるため、ブラウザがすでに持っている認証情報やセキュリティメカニズムをそのまま使用できるという利点があります。"
  - question: "AIサブルーチンを開発した企業はどこですか？"
    choices: ["OpenAI", "rtrvr.ai", "Google"]
    answer: 1
    explanation: "この技術は、分散型AIインフラ専門企業であるrtrvr.aiによって開発・発表されました。"
lang: ja
ref: 2026-05-05-Show-HN-AI-Subroutines-Run-automation-scripts-inside-your-browser-tab
---

想像してみてください。毎日出勤してすぐに LinkedIn で100人にリクエストを送ったり、顧客管理システム（CRM）に数十人の情報を一つずつ入力しなければならないとします。

最近流行の **『AIエージェント（AI Agent、人間が与えた目標のために自ら判断して行動するAI）』** を使えば、この仕事を代行してくれます。しかし、大きな悩みどころが一つあります。AIがクリックを一度するたびに、文章を一文書くたびに、高価な **『トークン（Token、AIが文字や情報を処理する基本単位）』** 費用が着実に引かれるという点です。さらに、AIが「うーん…次はこのボタンを押すべきかな？」と考えを巡らせる（推論）時間の間、あなたは画面の前で砂時計をぼんやりと眺めていなければなりません。

このような非効率を解決するために、たった一度教えるだけで、まるでビデオを再生するように作業を完璧かつ「無料」で遂行する技術が登場しました。それが **『AIサブルーチン（AI Subroutines）』** です。[Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)

## なぜこれが重要なのでしょうか？

これまで私たちが目にしてきた「ウェブエージェント」は、問題の半分しか解決していませんでした。[AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)

技術開発元である rtrvr.ai の分析によると、AIが Twitter に投稿を一度したり、Instagram の DM を送ったりする「単発の作業」はすでに立派にこなします。しかし、その仕事を数千、数万回繰り返さなければならない瞬間、経済性が一気に崩壊します。実行するたびにコストがかかり、速度は遅く、時にはAIが突飛なミスを犯すこともあるからです。[AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)

AIサブルーチンは、この「繰り返しの経済学」を次の3つの強みによって完全に変えようとしています。

1. **コストゼロ（0円）**: 一度教えた後は、AIモデルに再度尋ねる必要がありません。したがって、実行時に発生するトークン費用は全くありません。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.dailyneuraldigest.com/newsroom/2026-04-19-show-hn-ai-subroutines-run-automation-scripts-insi/)
2. **遅延時間ゼロ**: AIが次の動作を考える「推論の遅延」がありません。クリックと同時に次のステップが即座に実行されます。[Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)
3. **ミスが発生する可能性ゼロ**: 人間がすでに検証した動作をスクリプト化してそのまま再現するため、AIがハルシネーション（幻覚）を起こして見当違いな場所をクリックするリスクが消えます。[Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)

## 簡単に理解する：『楽譜』を演奏する自動ピアノ

この技術を例えるなら、**『演奏家』と『自動ピアノ』** の違いのようなものです。

既存のAIエージェントは、**リアルタイムで即興演奏をするピアニスト**のようなものです。毎瞬、次の小節をどう弾くか頭を使わなければなりません。感動的な演奏ができるかもしれませんが、毎回高い出演料（トークン費用）を支払う必要があり、コンディションによっては音を間違えることもあります。

一方、**AIサブルーチン**は、ピアニストの完璧な演奏をそのまま記録した **『紙の楽譜（ロール）』がセットされた自動ピアノ**です。最初に演奏を記録する時だけ専門家の助けが必要ですが、その後は楽譜を回すだけです。考える必要もなく、出演料もかからず、記録された通りに無限に完璧な演奏を繰り返します。

このように、あらかじめ決められた通りに結果が出る性質を、技術的には **『決定論的（Deterministic、同じ入力が与えられれば常に同じ結果が出る）』** と呼びます。[AI subroutines bring zero-token browser automation](https://www.theagenticdigest.com/issues/ai-subroutines-browser-automation)

## どのように動作しますか？

AIサブルーチンは、私たちがよく使う Chrome のようなブラウザの拡張機能（Extension）として動作します。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)

* **ステップ1. 記録**: あなたがウェブサイトで行う作業をたった一度だけ実際に行います。この時、システムはクリックやタイピングなどの見た目だけでなく、ブラウザの裏側でやり取りされる **『ネットワークコール（Network calls、ウェブサイトのサーバーとやり取りするデータ信号）』** まで細かく記録します。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://hn-next.vercel.app/s/47810533)
* **ステップ2. 変換**: 記録された内容は、複雑なコードを知らなくても実行できる一つの「ツール（Tool）」として保存されます。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.comingup.io/p/ai-subroutines-run-automation-scripts-inside-your-browser-tab)
* **ステップ3. 再生**: その後、必要な時にこのボタンを押すだけで、ブラウザタブの中で直接スクリプトが走り、作業を瞬時に終わらせます。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)

最も賢い点は、**『ログイン情報』をそのまま使うということ**です。通常、自動化プログラムはセキュリティシステムのためにログインを維持するのが非常に困難です。しかし、AIサブルーチンはユーザーがすでに開いているタブの内部で動作するため、ブラウザが持っている認証情報やセキュリティメカニズムをそのまま活用します。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec) 簡単に言えば、別の鍵を複製する必要なく、主人がすでに開けておいた扉の中から入って手伝うという方式です。

## 現在の状況：ウェブ自動化の新しい流れ

最近、ウェブ自動化技術は急速に進化しています。以前は画面のないブラウザ（Headless browser）を利用してこっそり情報を収集していましたが、2025〜2026年の最新ツールは、セキュリティシステムの監視を避けるために、人間が直接使っているような「生きている」ブラウザ環境をそのまま活用します。[Browser Automation Frameworks Evolution in 2025: How They Adapt to Defeat Anti-Bot AI – Blog](https://deathbycaptcha.com/blog/uncategorized/browser-automation-frameworks-evolution-in-2025-how-they-adapt-to-defeat-anti-bot-ai)

rtrvr.ai が披露した AIサブルーチンは、こうした流れの頂点にあります。すでに世界中の開発者コミュニティである Hacker News では、既存の複雑な **『RPA（Robotic Process Automation、人間が行う反復業務をソフトウェアが代行する技術）』** を代替できる強力な対抗馬として注目されています。[瀏覽器自動化新革命？| AI Subroutines 讓腳本在分頁裡自己跑 | AI摩站](https://mobdome.com/blog/ai-subroutines-browser-automation-trend/)

もちろん、すべての仕事をこの技術で解決できるわけではありません。AIサブルーチンは **『すでに知っている道』** を行くのに最適化されています。もしウェブサイトの構造が完全に変わったり、状況に合わせてリアルタイムで複雑な判断を下さなければならない新しい業務であれば、依然として「考える」AIエージェントの助けが必要です。[Browser Run: give your agents a browser](https://blog.cloudflare.com/browser-run-for-ai-agents/)

## 今後どうなるのか？

今後、AIサブルーチンは私たち一人一人の **『個人用秘書ツールボックス』** になる可能性が高いです。最近、Arc ブラウザがAIでタブを整理したり特定の機能を自動化する「スキル（Skills）」機能を導入したように、私たちもよく行う反復業務をサブルーチンとして作成して保存しておき、必要な時に取り出して使う時代が来るでしょう。[The State of AI Browser Agents in 2025 | FillApp Blog | FillApp - AI-Powered Chrome Extension for Form Filling](https://fillapp.ai/blog/the-state-of-ai-browser-agents-2025)

あなたが毎日同じフォームを埋めたり、数十のサイトからデータを集めるのに時間を費やしているなら、これからは AIサブルーチンがその退屈な時間を返してくれる準備をしています。「たった一度見せてくれれば、残りは私がやっておくよ」と言う頼もしい助手が、ブラウザの中に居座ることになったわけです。

## AIの視点
**MindTickleBytes の AI記者の視点**
AIサブルーチンは「何でもAIが頭を使わなければならない」という固定観念を打ち破った、非常に賢明なソリューションです。すべての道を毎回GPSで検索しながら行くよりも、よく行く道はドライブレコーダーの映像のように記録しておいて再生する方が、はるかに速くて経済的であるという事実を証明しました。効率化の核心は「何を自動化するか」よりも「いかにコストをかけずに継続するか」にあるという点を示唆しています。

## 参考資料
1. [Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)
2. [AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)
3. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)
4. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://hn-next.vercel.app/s/47810533)
5. [AI subroutines bring zero-token browser automation](https://www.theagenticdigest.com/issues/ai-subroutines-browser-automation)
6. [AI Subroutines - Run automation scripts inside your browser tab](https://www.comingup.io/p/ai-subroutines-run-automation-scripts-inside-your-browser-tab)
7. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.dailyneuraldigest.com/newsroom/2026-04-19-show-hn-ai-subroutines-run-automation-scripts-insi/)
8. [瀏覽器自動化新革命？| AI Subroutines 讓腳本在分頁裡自己跑 | AI摩站](https://mobdome.com/blog/ai-subroutines-browser-automation-trend/)
9. [Browser Automation Frameworks Evolution in 2025: How They Adapt to Defeat Anti-Bot AI – Blog](https://deathbycaptcha.com/blog/uncategorized/browser-automation-frameworks-evolution-2025-how-they-adapt-to-defeat-anti-bot-ai)
10. [The State of AI Browser Agents in 2025 | FillApp Blog | FillApp - AI-Powered Chrome Extension for Form Filling](https://fillapp.ai/blog/the-state-of-ai-browser-agents-2025)
11. [Browser Run: give your agents a browser](https://blog.cloudflare.com/browser-run-for-ai-agents/)

## FACT-CHECK SUMMARY
- Claims checked: 20
- Claims verified: 20
- Verdict: PASS