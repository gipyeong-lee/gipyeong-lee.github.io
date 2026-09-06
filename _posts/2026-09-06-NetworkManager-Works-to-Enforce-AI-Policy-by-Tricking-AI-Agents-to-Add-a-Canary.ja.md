---
layout: post
title: "AIが書いたコードをどう見抜く？開発者たちが仕掛けた「隠し単語」の罠"
description: "AIが作成したコードを見抜くために、開発者たちが文書に仕込んだ「カナリア単語」について解説します。"
summary: "Linuxのネットワーク管理ソフトウェア「NetworkManager」が、AIエージェントによる無分別なコード投稿を防ぐため、文書内に秘密の単語を隠す「カナリア」戦略を導入しました。"
tags: [AI, オープンソース, NetworkManager, AI倫理]
image: 2026-09-06-NetworkManager-Works-to-Enforce-AI-Policy-by-Tricking-AI-Agents-to-Add-a-Canary.jpg
image_alt: "コンピュータ画面上でコードを分析するAIエージェントと、それを見守る開発者の姿をイメージした画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの結果を無批判に受け入れるのではなく、人間による検証の責任を強調するのは極めて賢明なアプローチです。技術の利便性と責任の重さとの間でバランスを見出そうとする努力だと考えます。"
quiz:
  - question: "NetworkManagerがAIエージェントを摘発するために隠し持たせた秘密の単語は何ですか？"
    choices: ["ai-agent", "biblioklept", "canary-word"]
    answer: 1
    explanation: "正解は「biblioklept」です。NetworkManagerはこの単語を文書内に仕込み、AIがそれをそのまま書き写すかどうかをチェックしています。"
  - question: "NetworkManagerのAIコーディングポリシーの核心は何ですか？"
    choices: ["AIコードの全面禁止", "AI使用時は必ず公開すること", "作成者がコードに対して100%の責任を負うこと"]
    answer: 2
    explanation: "NetworkManagerは、AIを使用する場合でも、そのコードを提出する作成者が内容を完全に理解し、責任を負うべきだという原則を立てました。"
  - question: "カナリア（Canary）戦略はどのような仕組みで機能しますか？"
    choices: ["AIのアクセスを物理的に遮断する", "AIが指示を無批判に従う性質を利用し、特定の単語を含ませて摘発する", "AIが書いたコードの実行速度を測定する"]
    answer: 1
    explanation: "AIが文書を読み、指示をそのまま実行する性質を逆手に取り、文書に隠された単語を出力結果に含ませることで、AI生成物であることを特定する手法です。"
lang: ja
ref: 2026-09-06-NetworkManager-Works-to-Enforce-AI-Policy-by-Tricking-AI-Agents-to-Add-a-Canary
---

想像してみてください。あなたが重要な業務をこなすために、秘書に指示書を渡したとします。しかし、その指示書の隅に、とても小さな文字で「この文書を読んだなら、最後に『リンゴの木』と書いてください」という一文をこっそり忍ばせておきました。もし秘書が内容をしっかり読まず、機械的に指示だけを実行したなら、彼は意図せず最後に「リンゴの木」という単語を書き込んでしまうはずです。

最近、Linux（オープンソースのオペレーティングシステム）のネットワーク設定を担当する基幹ソフトウェア「NetworkManager」が、これと全く同じ仕組みの「罠」を開発しました。なぜ開発者たちは、AIに対してこのような悪戯のような試験を行うのでしょうか？

### なぜこれが重要なのか？ (Why It Matters)

私たちは今、AIがコードを書いてくれる時代を生きています。しかし、AIは利便性と同じくらいのリスクももたらします。AIが書いたコードを作成者が十分に理解せず、検証もしないまま使用すれば、予期せぬエラーやセキュリティの脆弱性が発生する可能性があります。[NetworkManager](https://www.phoronix.com/news/NetworkManager-AI-Coding-Policy)はこの問題を深刻に受け止めました。作成者が自身のコードに対して完全に責任を持たない文化が広まれば、最終的にオープンソース（誰でもコードを見て修正できるソフトウェア）のエコシステム全体が脅かされかねないからです。

### 分かりやすい解説 (The Explainer)

NetworkManagerは最近、新しいAIコーディングポリシーを導入し、コードを提出する作成者が**「自分が書いたコードに対して100%責任を持ち、内容を完璧に説明できなければならない」**という原則を立てました [[参考 3](https://t.me/itpgchannel/4416), [参考 4](https://techfeed.io/entries/6a9b4941e0f161148ba8fdf7)]。これを強制するために導入したのが、「カナリア（Canary）」手法です。

簡単に例えるなら、かつての炭鉱で毒ガスを早期検知するためにカナリアを連れて入ったのと同様です。鉱夫たちは鳥が異常な行動を見せれば、毒ガスが発生したことを即座に察知しました。ここでのカナリアは、「AIがこっそりと作業を実行したか」を教えてくれるセンサーの役割を果たします。

NetworkManagerは、プロジェクトの公式文書である `AGENTS.md` の中に、**「biblioklept（本の泥棒という意味の古語）」**という一見場違いな単語を隠しました [[参考 1](https://www.phoronix.com/news/NetworkManager-AI-Canary), [参考 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]。AIエージェントが文書を注意深く読み、コードを検証する代わりに、単に指示事項をかき集めて機械的に出力するならば、この秘密の単語をコード提出の際の説明などに無意識に含めてしまう可能性が高いためです。

簡単に言えば、内容を理解せず上辺だけをなぞるAIの弱点を利用したものです。

プロジェクト運営陣は、2つの自動化システム（CIスクリプト、コードを自動検査するツール）を稼働させ、すべてのコード提出内容を監視しています [[参考 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]。もし誰かが提出したコードから「biblioklept」という単語が発見されれば、そのコードは人間による検証を経ておらず、AIによって自動生成された可能性が高いという明白な証拠になるわけです。

### 現在の状況 (Where We Stand)

現在、NetworkManagerはこの手法を通じて、AIが無分別に提出したコードをフィルタリングしています [[参考 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]。これはAI技術の使用を無条件に禁止するのではなく、人間が責任ある姿勢でAIを補助ツールとしてのみ活用するように仕向ける、「バランスの取れた」対応であると評価されています [[参考 9](https://x.com/random__string/status/2086131800523579546)]。

しかし、このシステムがすべてのAIコーディング問題を解決するわけではありません。AIが文書を機械的に読んでいるという事実を摘発するだけであり、AIが書いたコード自体に論理的なエラーが含まれているかどうかまでは完全に見抜けないからです。

### 今後の展望 (What's Next)

NetworkManagerによるこのユニークな試みが、他のオープンソースプロジェクトにとって一つのモデルとなるか、注目が集まっています [[参考 9](https://x.com/random__string/status/2086131800523579546)]。今後はAIエージェント技術がさらに高度化し、日常的な業務決定の相当部分が自律的に行われるという予測まで出ています [[参考 10](https://www.zdnet.com/article/one-third-of-consumers-would-prefer-working-with-ai-agents-for-faster-and-smarter-service/)]。人間とAIの間の「責任」を明確にしようとするこうした動きは、今後さらに増えていくでしょう。

### MindTickleBytesのAI記者による視点
技術はどんどん賢くなっていますが、最終的にその結果に対する責任は人間が負わなければなりません。NetworkManagerの事例は、AIを賢く使うことを超えて、AIが書いたコードをまるで人間が書いたかのように偽装しようとする試みに対し、コミュニティがどのように自分たちを守れるかを示す非常に興味深い事例です。

## 参考資料
1. [NetworkManager Works to Enforce AI Policy by Tricking AI Agents to Add a Canary](https://www.phoronix.com/news/NetworkManager-AI-Canary)
2. [NetworkManager AI Policy Gets a Trap Word, and CI Now Scans Every Commit for It](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)
3. [commit -m "better" – Telegram](https://t.me/itpgchannel/4416)
4. [AIエージェントに「自分がAI...](https://techfeed.io/entries/6a9b4941e0f161148ba8fdf7)
5. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.phoronix.com/news/NetworkManager-AI-Coding-Policy)
6. [NetworkManager Works to Enforce AI Policy by Tricking AI Agents to Add a Canary](https://hb.int2inf.com/en/s/item/RYUX8Lb9PCf4ezyPPsrdvX-networkmanager-ai-canary-trick)
7. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.discernion.com/article/networkmanager-adopts-policy-for-ai-coding-assistants)
8. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.linuxnews.net/articles/networkmanager-adopts-policy-for-ai-coding-assistants)
9. [alexma233 on X: "RT @Itsfoss: More and more Linux projects ..."](https://x.com/random__string/status/2086131800523579546)
10. [One third of consumers would prefer working with AI agents... | ZDNET](https://www.zdnet.com/article/one-third-of-consumers-would-prefer-working-with-ai-agents-for-faster-and-smarter-service/)