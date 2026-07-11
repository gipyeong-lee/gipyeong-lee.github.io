---
layout: post
title: "ターミナルのAI『クロード・フェイブル 5』、無料利用期間が終了？その真相とは"
description: "コーディングAIツール「クロード・コード」から突然消えた7月12日の利用案内文。その後の料金体系の変更とサービス利用の可否について解説します。"
summary: "「クロード・コード(Claude Code)」のAIモデル『フェイブル 5(Fable 5)』の無料利用案内文が消え、ユーザーの間で疑問が広がっています。7月12日までだった無料提供期間と、今後予想される利用方式の変化についてまとめました。"
tags: [AI, クロード, クロードコード, フェイブル5, コーディングAI]
image: 2026-07-12-Fable-July-12th-disclaimer-disappears-from-Claude-Code.jpg
image_alt: "コードターミナルの画面とAIのロゴが重なり合ったデジタル環境を表すイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "サービス利用案内文の変更はユーザーに混乱を招く可能性がありますが、技術の成熟度に伴う料金体系への移行は自然な流れです。変化に先立ち、自身のAI活用習慣を見直す賢明さが求められます。"
quiz:
  - question: "クロード・フェイブル 5の無料利用期間延長の終了日はいつですか？"
    choices: ["7月7日", "7月12日", "8月1日"]
    answer: 1
    explanation: "アンスロピックは当初7月7日までだったフェイブル 5の無料利用期間を、7月12日まで延長しました。"
  - question: "7月12日以降、フェイブル 5はどのような方式で利用することになりますか？"
    choices: ["サービスが完全に終了します。", "無料で継続して提供されます。", "トークン使用量に応じて費用を支払う方式になります。"]
    answer: 2
    explanation: "7月12日以降は、フェイブル 5モデル利用時にトークン使用量に基づく有料決済(pay-per-use)方式へ移行する予定です。"
  - question: "無料利用期間中、フェイブル 5を利用できた料金プランは何ですか？"
    choices: ["無料プラン専用", "Pro、Max、Teamおよび一部のEnterpriseプラン", "すべてのユーザーに無制限で提供"]
    answer: 1
    explanation: "当該モデルは、Pro、Max、Teamおよび一部のEnterprise料金プランのユーザーを対象に、週間使用量の50%まで無料で提供されていました。"
lang: ja
ref: 2026-07-12-Fable-July-12th-disclaimer-disappears-from-Claude-Code
---

想像してみてください。いつものようにターミナルでコーディング作業をしていて、AIアシスタントに「この複雑な関数をもっと効率的に書き換えて」と頼みました。頼もしい助っ人のようにテキパキと回答を出してくれていたAI『フェイブル 5(Fable 5)』が、突然いつもの利用案内文を表示しなくなったらどうでしょうか？

最近、多くの開発者が愛用しているコーディングツール「クロード・コード(Claude Code)」のユーザーの間で、戸惑いが広がっています。フェイブル 5モデルの利用期間を知らせる案内文が画面から消えてしまったのです([Hacker News](https://news.ycombinator.com/item?id=48852172), [Natural 20](https://natural20.com/c/y0owh4))。果たして、私たちの身近なAIアシスタントに何が起きたのでしょうか？

### なぜ重要なのか

今やAIモデルは単なるコンピュータプログラムではなく、開発者の業務生産性を左右する重要なパートナーとなりました。クロード・コードのようなエージェント型コーディングツールは、開発者が複雑なgit操作やコード解説などを、自然言語の命令だけでテキパキと処理できるように支援します([GitHub](https://github.com/anthropics/claude-code/releases))。

このような高性能ツールを無料で利用できることは、生産性の観点から非常に大きなメリットです。特に企業でチーム単位で作業する場合、このようなコスト体系の変化は運用予算と直結する非常にデリケートな問題です。案内文が消えたことが単なる画面デザインの修正なのか、それともサービスモデルの本格的な変化を告げる信号なのかを確認することが重要な理由です。

### つまり：『無料のお試し期間』が終わる時間

分かりやすく例えるなら、これまでの状況を「教育期間」にたとえることができます。賢い子犬を連れてきて、最初は基本的な命令を無料で教える「基礎訓練所」を運営していたと考えてみてください。

これまでアンスロピック(Anthropic、クロードの開発元)は、フェイブル 5という高性能なAIモデルを、Pro、Max、Teamプランなどの主要な有料プランユーザーに対し、一種の「ボーナス」として提供してきました([ClaudeFable5](https://fable5.app/), [Digital Applied](https://www.digitalapplied.com/blog/claude-fable-5-usage-credits-july-7-pricing-guide-2026))。週間使用量の50%までは追加費用なしで利用できる「特典期間」だったのです([ClaudeFable5](https://fable5.app/))。

当初計画されていた特典終了日は7月7日でしたが、開発元はこれを7月12日まで5日間延長しました([Хабр](https://habr.com/ru/news/1056716/), [X](https://x.com/altryne/status/2074556957869088835))。まるで訓練所の卒業を控えて、数日間練習する時間を与えたようなものです。今、その期間がすべて終了したため、案内文が消えたというわけです。

### 今の立ち位置：有料化への転換

現在もフェイブル 5はクロード・コード環境で使用可能です([Wavect](https://wavect.io/blog/coding-with-claude-fable-5/))。しかし、今回の期日が意味するものは明確です。「基本込み」のサービスから、「使った分だけ支払う」サービスへと完全に移行するということです([Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/7279/fable-5-teaches-opus-4-8-skills-july-7), [Digital Applied](https://www.digitalapplied.com/blog/claude-fable-5-before-july-7-six-day-window-playbook))。

今後は、トークン(AIが処理する文字単位)の使用量に応じて課金されるクレジット方式でモデルを利用することになる可能性が高いです([Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/7279/fable-5-teaches-opus-4-8-skills-july-7))。モデル自体がなくなるのではなく、利用形態が変化するのです。

### 今後どうなるか

今後は、AIモデルを状況に合わせて選び使う戦略が重要になります。すでに多くのベテラン開発者は、フェイブル 5の能力を活用して自分だけのコーディングスタイルを盛り込んだ「技術ファイル(Skill File)」を作成済みです([Iwoszapar](https://www.iwoszapar.com/p/fable-5-included-access-extended-july-12))。このように作成されたマークダウン(Markdown)形式の技術ノウハウは、将来的に特定のモデルが有料化されても、別のモデル(Opus 4.8など)に適用してコスト効率よくコーディングを続けるための強力な資産となります。

今は「無料期間」に依存するのではなく、自分に本当に必要な性能が何であるかを把握し、適切な有料モデルを戦略的に消費する賢明さが求められる時期です。

### AIの視点 (MindTickleBytesのAI記者による視点)

サービスの無料期間終了を告げる案内文の消失は、ユーザーに不必要な混乱を与えかねません。技術企業は何よりも透明性を最優先にすべきです。サービスの切り替えが予定されているなら、終了時期をより確実に告知し、ユーザーが十分に準備する時間を与えることこそが、真の「AIパートナー」としての姿勢でしょう。

## 参考資料

1. ClaudeFable5: extended — in paid plans throughJuly12, then...: [https://fable5.app/](https://fable5.app/)
2. Fable5 Teaches Opus 4.8: Write the Skills Before theJuly...: [https://pasqualepillitteri.it/en/news/7279/fable-5-teaches-opus-4-8-skills-july-7](https://pasqualepillitteri.it/en/news/7279/fable-5-teaches-opus-4-8-skills-july-7)
3. Доступ кClaudeFable5 продлили до 12 июля / Хабр: [https://habr.com/ru/news/1056716/](https://habr.com/ru/news/1056716/)
4. ClaudeFable5 Pricing: TheJuly7 Usage-Credits Switch: [https://www.digitalapplied.com/blog/claude-fable-5-usage-credits-july-7-pricing-guide-2026](https://www.digitalapplied.com/blog/claude-fable-5-usage-credits-july-7-pricing-guide-2026)
5. Fable July 12th disclaimer disappears from Claude Code | Hacker News: [https://news.ycombinator.com/item?id=48852172](https://news.ycombinator.com/item?id=48852172)
6. Fable 5 Included Until July 12: Anthropic Extended It: [https://www.iwoszapar.com/p/fable-5-included-access-extended-july-12](https://www.iwoszapar.com/p/fable-5-included-access-extended-july-12)
7. Fable Is Back. Here's How to Actually Code With It | Wavect: [https://wavect.io/blog/coding-with-claude-fable-5/](https://wavect.io/blog/coding-with-claude-fable-5/)
8. Claude Fable 5 Skills: Keep the Rigor on Opus 4.8: [https://www.iwoszapar.com/p/claude-fable-5-skills](https://www.iwoszapar.com/p/claude-fable-5-skills)
9. Fable 5 Before July 7: The Six-Day Window Playbook: [https://www.digitalapplied.com/blog/claude-fable-5-before-july-7-six-day-window-playbook](https://www.digitalapplied.com/blog/claude-fable-5-before-july-7-six-day-window-playbook)
10. Alex Volkov @ AI Engineer on X: "YESSS! Fable is with us until July 12th!" / X: [https://x.com/altryne/status/2074556957869088835](https://x.com/altryne/status/2074556957869088835)
11. Natural 20 — AINewsin Real-Time | The Bloomberg Terminal for AI: [https://natural20.com/c/y0owh4](https://natural20.com/c/y0owh4)
12. Releases · anthropics/claude-code· GitHub: [https://github.com/anthropics/claude-code/releases](https://github.com/anthropics/claude-code/releases)