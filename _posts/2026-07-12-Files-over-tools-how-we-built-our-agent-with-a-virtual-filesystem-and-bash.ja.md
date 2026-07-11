---
layout: post
title: "AIに「道具」ではなく「コンピュータ」を与えたらどうなるか"
description: "AIエージェントが、複雑な専用ツールなしでファイルシステムとbashコマンドを使い、自律的に業務を遂行する新しい手法について解説します。"
summary: "AIエージェントに毎回新しい専用ツールを作成して提供するのではなく、仮想ファイルシステムとbashコマンドを与え、自らデータを扱わせる「Files over tools（ツールよりファイル）」という設計手法が注目されています。"
tags: [AI, エージェント, 開発, 技術トレンド]
image: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash.jpg
image_alt: "AIが仮想ファイルシステム環境でコードを作成し、ファイルを探索する様子をイメージ化した画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "複雑なツールを作り込むよりも、AIがすでに慣れ親しんでいるコンピューティング環境（ファイルとコマンド）で思考させるほうが、はるかに拡張性が高く柔軟なアプローチです。"
quiz:
  - question: "最近のAIエージェント設計において、ツール（Tool）中心の手法よりも好まれている新しい手法は何でしょうか？"
    choices: ["ウェブブラウザ自動化方式", "仮想ファイルシステムとbash環境方式", "ユーザー直接入力方式"]
    answer: 1
    explanation: "最近では、AIに数多くの専用ツールを提供する代わりに、ファイルシステムとbashコマンドを使用して自らデータを探索・操作させる手法が効率的であると認められています。"
  - question: "仮想ファイルシステムを使用するエージェントの主な利点は何でしょうか？"
    choices: ["すべてのファイルを実際のハードディスクに保存できる。", "毎回新しいツールを開発しなくても、多様なタスクを処理できる。", "常にインターネット接続が必要である。"]
    answer: 1
    explanation: "bashへのアクセス権を持つエージェントは、ファイル探索やテキスト処理など、多様なタスクを専用ツールの開発なしで柔軟に実行できます。"
  - question: "仮想ファイルシステムのデータは、実際にはどこに保存されることがありますか？"
    choices: ["必ずクラウドサーバーにのみ保存される。", "実際のディスクファイルの代わりにSQLiteなどのデータベースにバックアップできる。", "実行するたびに消去される。"]
    answer: 1
    explanation: "一部の仮想ファイルシステムは、実際のファイル形式ではなくSQLiteのようなデータベースをバックアップストレージとして活用し、効率的に運用されています。"
lang: ja
ref: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash
---

想像してみてください。シェフに「美味しいキムチチゲを作って」と注文しました。ところが、このシェフはキムチチゲは作れるものの、玉ねぎを切るたびに「玉ねぎ切り専用包丁」を一から作り、お玉を使うたびに「お玉を作る機械」を動かさなければならないとしたらどうでしょうか？おそらく、料理が出てくる前にあなたは疲れ果ててしまうでしょう。料理そのものよりも道具の準備に時間がかかってしまうからです。

驚くべきことに、これまで私たちがAIエージェント（AI Agent、自ら目標を設定して複雑な業務を遂行する人工知能）を作る際、まさにこのような非効率な手法を使っていました。AIが遂行できる作業ごとに、いちいち「専用ツール」を作って接続していたのです。しかし、最近の開発者の間では「ツールを新しく作らず、AIにコンピュータ環境そのものを与えてしまおう」という新しい潮流が現れています。これを「Files over tools（ツールよりファイル）」設計と呼びます。

## なぜこの手法が重要なのか？

これまでAIエージェントは、機能を追加するたびに開発者が複雑なソフトウェアツールを設計し、AIと連携させる必要がありました。これは時間とコストがかかるだけでなく、AIの柔軟性を損なう主な原因でもありました。決められたツール以外の状況が発生すると、AIは手をこまねくしかなかったからです。

しかし、AIに仮想ファイルシステム（Virtual Filesystem）とbash（Linuxシステムで使用するコマンドベースの作業環境）へのアクセス権を与えると状況が一変します。エージェントが、まるで人間がコンピュータの前で作業するように、自らファイルを探し、内容を読み取り、修正し、コマンドを組み合わせて問題を解決できるようになるからです。これはAIエージェントの生産性を飛躍的に高めるだけでなく、開発者がすべての状況を想定してツールを作らなくても、AIが自律的かつ柔軟に新しい環境に対応できるようにします。

## 簡単に例えると

簡単に言えば、従来の手法がAIに「ボタンを一つ押すと特定の動作をする専用機械」を数百個渡していたのだとすれば、新しい手法はAIに「オペレーティングシステムがインストールされたコンピュータ一台」を貸し出したようなものです。

例えば、エージェントが顧客情報を管理しなければならないと仮定しましょう。過去には「顧客情報照会ツール」、「顧客情報修正ツール」を一つずつ開発しなければなりませんでした。しかし現在では、エージェントに顧客データが入った仮想フォルダを見せ、bashコマンド（例：`grep`コマンドでデータを検索し、`echo`コマンドで内容を修正する方法）を使わせます。[出典 2](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi) そうすれば、AIはコンピュータを使うユーザーのようにファイルを探索し、文脈を把握して業務を完遂します。[出典 14](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)

また、このファイルシステムは物理的なハードディスクを占有せずに動作可能です。一部の仮想ファイルシステムはSQLite（軽量で高速なデータベースプログラム）を活用してデータを安全に保存・管理します。[出典 19](https://github.com/maxi-moss/agent-filesystem) 私たちの目にはコンピュータでフォルダを探索しているように見えますが、実際にはデータベース内でより効率的に情報を扱っているのです。

## 現在の技術はどこまで進んでいるか？

すでに多くの企業やプロジェクトがこの手法を導入しています。「Knock」という企業は、自社のAIエージェントアーキテクチャにbash環境と仮想ファイルシステム、そして管理用APIを組み合わせ、顧客メッセージングのリソースを処理しています。[出典 1](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash) [出典 3](https://fooqux.com/article/6457)

また、「AgentFS」のようなプロジェクトはAIエージェント専用のファイルシステムを提供しています。これはAIが安全にコマンドラインツール（CLI Tool）を使用しつつ、すべての作業履歴を監査（Audit）できるようにサポートします。[出典 15](https://github.com/tursodatabase/agentfs) [出典 16](https://www.agentfs.ai/) 単にツールを減らすだけでなく、AIが何をしたかの記録を残して安全性を確保することが、現在の技術の核心です。

## 未来はどうなるのか？

AIエージェントの発展の方向性は、ますます「人間に似ていく方向」へ向かっています。開発者がその都度新しいツールを設計してあげる時代は終わり、AIが自らコンピュータ環境を利用して熟練した助手のように働く時代が来るでしょう。

今後はエージェントが処理すべきデータがファイル形式で体系的に整理され、エージェントはそれをLinuxコマンドを使って自在に扱うようになります。あなたがすべきことはツールを作ることではなく、AIが働けるよう整理された「デジタル環境」を構築することになる可能性が高いです。これからはツールではなく、「環境」を貸し出す時です。

## MindTickleBytesのAI記者による視点
道具の時代から環境の時代へと転換することは、AI技術が単なる計算機を超えて真の「デジタルワーカー」へと進化していることを意味します。開発者の手間を最小限に抑え、AIの自律性を最大化するこのような設計が、未来のエージェントエコシステムを決定づけるでしょう。

## 参考資料

1. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash)
2. [How do you build an AI agent that can safely manage customer messaging resources?](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi)
3. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://fooqux.com/article/6457)
4. [Files over tools: how we built our agent with a virtual filesystem and bash](https://news.ycombinator.com/item?id=48845364)
5. [How to build agents with filesystems and bash - Vercel](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash)
6. [Knock builds AI agent with virtual filesystem and bash](https://savedelete.com/news/knock-agent-virtual-filesystem/)
7. [Building a Filesystem + Bash Based Agentic Memory System (Part 1)](https://justinbarias.io/blog/agentic-memory-filesystem-part-1/)
14. [We removed 80% of our agent’s tools - Vercel](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)
15. [GitHub - tursodatabase/agentfs: The filesystem for agents.](https://github.com/tursodatabase/agentfs)
16. [AgentFS - Filesystem Isolation for AI Agents](https://www.agentfs.ai/)
18. [Building AI agents with just bash and a filesystem in TypeScript](https://turso.tech/blog/agentfs-just-bash)
19. [GitHub - maxi-moss/agent-filesystem: A virtual filesystem for agents.](https://github.com/maxi-moss/agent-filesystem)