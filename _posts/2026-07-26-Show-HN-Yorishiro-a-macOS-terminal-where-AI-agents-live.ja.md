---
layout: post
title: "AIが画面の中に「生きる」？開発者の心強い味方となったターミナル「Yorishiro（依代）」"
description: "AIエージェントに身体と実在感を与える新しいmacOSターミナル「Yorishiro」を紹介します。"
summary: "Yorishiroは単なるコーディングツールを超え、AIエージェントが開発環境の中で開発者と共に存在し作業する体験を提供する、新しい概念のターミナルです。"
tags: [AI, 開発, ターミナル, macOS, Yorishiro]
image: 2026-07-26-Show-HN-Yorishiro-a-macOS-terminal-where-AI-agents-live.jpg
image_alt: "画面の中でAIエージェントが開発者と共に協働している様子をイメージしたターミナルインターフェースの画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ターミナルは、もはやコマンドを入力するだけの黒い画面ではありません。AIが私たちのそばに「存在」することで、開発はより人間的な協働の領域へと進化しています。"
quiz:
  - question: "Yorishiro（依代）の核心的な目的は何ですか？"
    choices: ["AIの演算速度を向上させること", "AIエージェントに身体と実在感を与えること", "ターミナルコマンドを自動的に暗記させること"]
    answer: 1
    explanation: "Yorishiroは、AIエージェントが単なるツールとして存在するのではなく、開発環境の中に「存在」しているかのような体験を提供する「Presence Harness」を目指しています。"
  - question: "Yorishiroは現在どのオペレーティングシステムをサポートしていますか？"
    choices: ["Windows専用", "macOS専用", "Linux専用"]
    answer: 1
    explanation: "現在、YorishiroはmacOS環境でのみ利用可能です。"
  - question: "Yorishiroと共に提供されるYorishiroProxyの役割は何ですか？"
    choices: ["ターミナルの色を変更する機能", "AIエージェントがプロキシ作業を制御できるように支援する機能", "ネットワーク速度を測定する機能"]
    answer: 1
    explanation: "YorishiroProxyはMCP（Model Context Protocol）サーバーとして機能し、AIエージェントが自動化されたセキュリティテストなどのプロキシ関連作業を直接制御できるように支援します。"
lang: ja
ref: 2026-07-26-Show-HN-Yorishiro-a-macOS-terminal-where-AI-agents-live
---

想像してみてください。朝、コンピュータの前に座って開発を始める時、そこには単なるコマンドを入力する黒い画面だけがあるわけではありません。画面の片隅でAIエージェントがあなたの作業フローを完璧に理解し、まるで傍らで一緒に悩んでくれる同僚のように居続けている姿を。映画の中でしか見たことのなかった「私の隣で生きているAIパートナー」という概念が、今、私たちの作業空間であるターミナルに入り込んでいます。

## なぜこれが重要なのか？

これまでAIは、私たちが本当に必要な時だけ質問して答えを得る「道具」に過ぎませんでした。しかし、開発環境におけるAIエージェントの役割が大きくなるにつれ、単に機能を実行するだけでなく、開発者と持続的にコミュニケーションをとる「パートナー」の必要性が高まっています。[参考資料 2](https://github.com/sktkkoo/Yorishiro) Yorishiro（依代）は、まさにこのような流れの中で誕生しました。これはAIを単なる性能向上のツールとして見るのではなく、私たちのそばに実在する存在として感じさせることで、開発の文法を変えようとする試みです。[参考資料 2](https://github.com/sktkkoo/Yorishiro)

## 分かりやすく説明すると

「依代（Yorishiro）」という名前は日本語に由来しており、神や霊魂が寄りつく物体を意味します。[参考資料 1](https://news.ycombinator.com/item?id=49008434) このターミナルは、その名前の通りAIエージェントが宿って生活できる「家」の役割を果たします。

簡単に例えるならこうです。従来のターミナルが単に電話をかけて用件だけを伝える「公衆電話ボックス」だったとすれば、YorishiroはAIエージェントが自分のデスクを持って座り、あなたの隣の席で一緒に働く「オフィス」です。AIがターミナルの中で単に命令を遂行するだけでなく、あなたが何をしているのかを理解し、その空間に「存在」することで、より緊密な協働が可能になるのです。[参考資料 8](https://github.com/sktkkoo/Yorishiro/) [参考資料 9](https://github.com/sktkkoo/Yorishiro/blob/main/docs/terminal.md)

## 現在の立ち位置は？

Yorishiroは現在、オープンソースで公開されているmacOS専用ターミナルです。[参考資料 1](https://news.ycombinator.com/item?id=49008434) 「libghostty」をベースに構築されており、MITライセンスに従っているため、誰でも自由に利用できます。[参考資料 12](https://github.com/usk6666/yorishiro-proxy) [参考資料 14](https://dev.to/gsalp/i-built-a-mac-os-terminal-that-detects-your-ai-coding-agents-heres-why-1nd) 特にユーザーのデータを追跡しない「テレメトリゼロ（zero telemetry）」ポリシーを固守しており、プライバシーを重視するユーザーにとっても魅力的な選択肢です。[参考資料 12](https://github.com/usk6666/yorishiro-proxy)

現在はClaude CodeやCodexなどの主要なコーディングエージェントと互換性があり、即座に連携が可能です。[参考資料 1](https://news.ycombinator.com/item?id=49008434) [参考資料 13](https://x.com/sunafukin_vrc/status/2077184531690635649) また、併せて提供される「YorishiroProxy」は、MCP（Model Context Protocol）という標準規格を使用しており、AIエージェントがネットワークセキュリティテストや複雑なプロキシ作業を自ら制御できるように支援します。[参考資料 12](https://github.com/usk6666/yorishiro-proxy)

## 今後はどうなるのか？

私たちがAIと共に過ごす時間は、今後さらに増えていくでしょう。[参考資料 2](https://github.com/sktkkoo/Yorishiro) Yorishiroは、このような未来に備えてターミナルをAIエージェントのための「専用生息地」へと発展させようとしています。単にターミナルウィンドウを立ち上げるだけでなく、AIが自分の作業環境を完全に理解し、主導的にサポートする環境が徐々に標準となるはずです。今後は開発者がいちいちコマンドを入力しなくても、隣の席にいるAIエージェントがあなたのコーディングの文脈を把握して先に動く「真の協働」の時代を期待できるでしょう。

## 参考資料

1. ShowHN:Yorishiro–amacOSterminalwhereAIagentslive (https://news.ycombinator.com/item?id=49008434)
2. sktkkoo/Yorishiro:Aterminalthat givesAIa body and alivingspace. (https://github.com/sktkkoo/Yorishiro)
8. GitHub - sktkkoo/Yorishiro: A terminal that gives AI a body ... (https://github.com/sktkkoo/Yorishiro/)
9. Yorishiro/docs/terminal.md at main · sktkkoo/Yorishiro · GitHub (https://github.com/sktkkoo/Yorishiro/blob/main/docs/terminal.md)
12. usk6666/yorishiro-proxy: AI-native MITM proxy - GitHub (https://github.com/usk6666/yorishiro-proxy)
13. 住人の宿るターミナル「Yorishiro」をOSSで公開しました。 AIに身体と... (https://x.com/sunafukin_vrc/status/2077184531690635649)
14. I Built a macOS Terminal That Detects Your AI Coding Agents ... (https://dev.to/gsalp/i-built-a-mac-os-terminal-that-detects-your-ai-coding-agents-heres-why-1nd)