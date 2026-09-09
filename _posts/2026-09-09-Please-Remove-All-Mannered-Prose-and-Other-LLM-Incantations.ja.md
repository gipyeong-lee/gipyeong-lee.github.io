---
layout: post
title: "AIが「かっこつけ」て回りくどい言い回しをするなら？この一文だけで十分です"
description: "AIが不要な比喩や華麗な修飾語を多用する「AIっぽい話し方」を排除し、簡潔に回答を得る方法を紹介します。"
summary: "Anthropicが公式ガイドを通じて、Claude Fable 5.1モデルの不要な修飾語や比喩を取り除く魔法のコマンド「Please remove all mannered prose」を公開しました。"
tags: [AI, Anthropic, Claude, プロンプトエンジニアリング, ヒント]
image: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations.jpg
image_alt: "AIが作成した複雑で華麗な文章が消去され、簡潔で明確な文章に変わる様子を象徴するグラフィック。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの「気取り」はユーザーに不要な認知負荷を与えます。本質を隠す修飾語を取り除くことは、AI活用の基本です。"
quiz:
  - question: "Anthropicが定義した「マナード・プローズ（mannered prose）」とは何ですか？"
    choices: ["AIが使用する技術的なエラー", "必要以上に比喩や華麗な修辞的表現が入った文章", "AIが回答を拒否する現象"]
    answer: 1
    explanation: "マナード・プローズとは、簡単に言える内容をAIが不要に比喩や華麗な文体で飾って回答する現象を指します。"
  - question: "提供されたコマンド「Please remove all mannered prose」はどこに入れると効果的ですか？"
    choices: ["個別の質問の最後やシステムプロンプトに追加", "コンピュータの設定メニューに入力", "必ずコードブロック内に入力"]
    answer: 0
    explanation: "このコマンドは個別のリクエストに含めるか、AIの役割を指定するシステムプロンプトに追加して使用できます。"
  - question: "AIがこのコマンドを正しく理解するために、必ずスペース（分かち書き）を守る必要がありますか？"
    choices: ["はい、スペースが必須です", "いいえ、スペースなしで続けて書いても効果があります", "大文字だけで入力する必要があります"]
    answer: 1
    explanation: "驚くべきことに、このコマンドはスペースをすべて省略した形（Pleaseremoveallmanneredprose）で入力しても十分に機能します。"
lang: ja
ref: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations
---

想像してみてください。忙しい朝、AIアシスタントに「今日の会議の主要な議題を3つだけまとめて」と頼みました。するとAIが「今日の会議は、まるで巨大な嵐の前夜のようでした。3つの主要議題という羅針盤が、我々の方向を案内してくれることでしょう...」と、比喩や修飾語を延々と並べ立てます。本題が知りたいユーザーにとっては、もどかしい限りですよね。

最近、AIモデルによるこうした「AIっぽい話し方」が、ユーザーに疲れを与えています。Anthropicが最近発表した最新モデル「Claude Fable 5.1」のガイドにおいて、この問題を解決できる意外とシンプルな解決策を公式に提示しました。

## なぜこれが重要なのか？

私たちがAIを使う最大の理由は「効率性」です。しかし、AIが人間らしく見せようとして過度な比喩を混ぜたり、文章を不要にねじ曲げたりすると、重要な情報を見つけるのが難しくなります。[Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)によると、AIが使うこうした華麗な文体は、著者が意図していない意味まで引き込んでしまい、読み手は本来しなくてもいい解釈作業を行うという不必要な手間を強いられます。今回の公式ガイドは、ユーザーがAIをより賢く、簡潔に使える権利を取り戻したという点で大きな意味を持ちます。

## 分かりやすく言うと

Anthropicは、こうした現象を「マナード・プローズ（Mannered Prose）」と名付けました。[Source 4](https://x.com/MaxForAI/status/2095131767229517917) 簡単に言えば、一言でスッキリまとめられる内容を、AIがわざわざ比喩や美辞麗句を持ち出して「かっこつけ」ながら長々と引き延ばす書き方のクセを意味します。

Anthropicの開発陣は、Claude Fable 5.1が以前のモデルより改善されたにもかかわらず、依然として文章が長すぎたり複雑すぎたりする場合があることを認めました。[Source 4](https://x.com/MaxForAI/status/2095131767229517917) そこで彼らは、この「AIっぽい話し方」を取り除くための魔法のようなコマンドを公式文書に追加したのです。

それが**「Please remove all mannered prose（すべてのマナード・プローズ、すなわち過度に飾られた文体を取り除いてください）」**という文章です。[Source 1](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)

例えるなら、AIは今「基本的なマナー教育」は終えたものの、たった今「文学の授業」を受けて帰ってきたばかりで、すべての答えに詩的な表現を混ぜたい状態です。このコマンドはAIに「芸術家ごっこは終わりにして、さっさとアシスタントの本業に集中して！」と伝える強力なスイッチなのです。

## 現状

現在、このプロンプトは非常に効果的であると評価されています。[Source 5](https://paddo.dev/blog/a-dial-worth-turning/) ユーザーたちはこのコマンドを質問の最後につけたり、あらかじめAIに指示を出す「システムプロンプト」に入れておくだけで、AIの口調が見違えるほど簡潔になることを確認しました。[Source 6](https://x.com/Voxyz_ai/status/2095260094795583807)、[Source 11](https://t.me/dailyprompts/9362)

さらに驚くべきことに、AIはこの文章の意味を非常に深く理解しているため、スペースをすべて無視して「Pleaseremoveallmanneredprose」と繋げて書いても賢く認識し、華麗な修飾語を取り除いてくれるのです。[Source 9](https://apidog.com/blog/prompting-claude-fable-5-1/)、[Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)

## 今後はどうなるのか？

今後、AIサービスはユーザーがわざわざこうした「口調を直す」コマンドを入力しなくても済むよう改善されるでしょう。Anthropicによる今回のガイド更新は、AI企業がユーザーの声に耳を傾け、AIの知能だけでなく「コミュニケーションの効率性」まで考えているというシグナルです。

これからはAIに対して「きれいな言葉を使わなくていいから、核心だけ話して」と面倒に説明する必要はありません。あの一文さえあれば、あなたのAIアシスタントははるかに有能なビジネスパートナーへと変身するでしょう。

## MindTickleBytesのAI記者視点

AIが人間のようにうまく話せるようになったのは技術的な成果ですが、ビジネス環境において最も価値のある能力は、依然として「明確な情報伝達」です。Anthropicが自らこの問題を解決するプロンプトを公開したことは、AIが自らを律する能力こそが、AI技術の真の成熟度を測る尺度になりつつあることを示しています。

## 参考資料

1. [Matthew Ritch, "Please Remove All Mannered Prose" and Other LLM Incantations](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)
2. [Ian Nuttall, "A prompt to stop Claude from speaking in parseltongue"](https://x.com/iannuttall/status/2095203215734178066)
3. [Max For AI, "有意思，Anthropic亲自下场教你怎么去掉Claude味了"](https://x.com/MaxForAI/status/2095131767229517917)
4. [Paddo, "A Dial Worth Turning: Claude Opus 5's Prose, and the Style Guide Anthropic Wrote Against Its Own Model"](https://paddo.dev/blog/a-dial-worth-turning/)
5. [Vox, "You removed the “It’s not X, it’s Y” lines. 𝗜𝘁 𝘀𝘁𝗶𝗹𝗹 𝗿𝗲𝗮𝗱𝘀 𝗹𝗶𝗸𝗲 𝗔𝗜."](https://x.com/Voxyz_ai/status/2095260094795583807)
6. [HN blogs - 8/9/26](https://hnblogs.substack.com/p/hn-blogs-8926)
7. [APIDog, "Prompting Claude Fable 5.1: Every Behavior Shift and the Line That..."](https://apidog.com/blog/prompting-claude-fable-5-1/)
8. [Telegram, "@dailyprompts"](https://t.me/dailyprompts/9362)
9. [Dzen, "Гайд по созданию промптов в Fable 5.1"](https://dzen.ru/a/apkFgUgF0B8ig_B6)
10. [Vibecoding, "Вычурность из текстов Claude убирает одна строка"](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)
11. [VC.ru, "Вышел Claude Fable 5.1 - я уже потестила"](https://vc.ru/chatgpt/3117274-obzor-fable-5-1-ot-anthropic-i-ozhidaniya-ot-astra-ot-openai)