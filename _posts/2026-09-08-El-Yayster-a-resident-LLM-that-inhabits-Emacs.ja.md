---
layout: post
title: "コンピュータの「口」ではなく「体」となったAI、El Yaysterのご紹介"
description: "AIが単に回答を出す秘書ではなく、エディタ内で直接動き回り、コードを管理し環境を制御するとしたらどのような姿でしょうか？Emacs（イマックス）に住まう新しい形態のAI、El Yaysterについてご紹介します。"
summary: "これまでのEmacs用AIツールが単にユーザーの質問に答える「口」の役割を果たしていたのに対し、El YaysterはユーザーのEmacs環境を直接見て行動する「体」として、AIにエディタの制御権を与えます。"
tags: [AI, Emacs, ElYayster, プログラミング]
image: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs.jpg
image_alt: "Emacsエディタ環境の中でAIが能動的に作業する姿を形にしたコンセプト画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "道具を使うAIから、環境そのものとなるAIへの変化です。ユーザーの意図を待つ受動的な関係から、共に作業するエージェント的関係へ向かう興味深い一歩です。"
quiz:
  - question: "従来のEmacs用AIパッケージの大部分とEl Yaysterの最大の違いは何ですか？"
    choices: ["サポートするAIモデルの種類", "AIがEmacs環境を直接制御するかどうか", "インストール方式"]
    answer: 1
    explanation: "El Yaysterは単純な対話型インターフェースを超え、AIがEmacs環境を観察し、能動的にツールを使用して制御する「体」の役割を果たす点が異なります。"
  - question: "El YaysterがEmacs環境を制御するために使用する方式は？"
    choices: ["クラウド直結", "制御されたEmacs Lispコード", "ユーザーが手動で入力するマクロ"]
    answer: 1
    explanation: "El YaysterはEmacs環境と相互作用するために「制御された（gated）Emacs Lisp」を使用します。"
  - question: "El Yaysterが最も推奨する実行環境（ハッピーパス）は何ですか？"
    choices: ["APIキーが必要な商用クラウドサービス", "ローカルで実行されるOllama", "Webブラウザベースのエディタ"]
    answer: 1
    explanation: "El Yaysterは様々なOpenAI互換エンドポイントをサポートしていますが、ローカルで実行するOllamaが最も推奨される方式です。"
lang: ja
ref: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs
---

想像してみてください。朝起きてコンピュータをつけたら、普段使っているエディタが単なる文書作成の空間を超えて、隣で一緒に考え動く同僚になっていたらどうでしょうか？

これまで私たちが使ってきた多くのAIツールは、まるで「口」のようでした。私たちが話しかけると（入力すると）、AIはその回答を文書ウィンドウに吐き出すだけでした。しかし最近、Emacs（高度に拡張可能なテキストエディタ）環境に非常に興味深い変化をもたらすプロジェクトが登場しました。**「El Yayster」**という名の実験的なツールです。

### なぜこれが重要なのか？

これまでのAI統合機能は主に、ユーザーがAIに質問を投げ、AIは単に結果を見せる「質疑応答」中心の秘書形態でした。しかしEl Yaysterは、この関係を完全に覆してしまいます。

この技術が重要な理由は、「AIの立ち位置」が変わったからです。もはやAIは指示を待つ受動的な秘書ではなく、エディタ内部の状況を自ら把握し環境を直接制御する「エージェント」となりました。これはまるで、料理人がレシピを聞く代わりに、隣で材料を刻み火加減を直接調整してくれる熟練の見習いを置くのと同じ変化です。私たちが繰り返す作業をAIが直接エディタを操作して解決できることを意味します。[出典: ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)

### わかりやすく解説：「口」から「体」へ

この変化をわかりやすくするために、こう例えることができます。

これまでのAIツールは電話越しの相談員のようなものでした。症状を伝えると解決策を言葉で教えてくれます。しかし、**El Yaysterは人工知能にEmacsという「体」を貸し出したこと**と同じです。[出典: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

このモデルは単にテキストバッファに文字を書くのではなく、Emacsというソフトウェア環境を生きている生命体のように認識します。[出典: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md) 

1. **観察**: まずAIが自分のライブ環境を見ます。
2. **決定**: どのような行動が必要かを判断します。
3. **行動**: 「制御された（gated）Emacs Lisp（Emacsエディタを操作するプログラミング言語）」というツールを利用して、エディタを実際に操作します。
4. **反復**: 結果を確認し、次の作業へ移ります。[出典: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

まるで私たちがマウスとキーボードでエディタを動かすように、AIが直接Emacsのボタンを押し、コマンドを実行するのです。

### 現状：どう使えるのか？

現在El Yaysterは、Emacsという空間に住まい活動する非常に独創的な試みとして評価されています。[出典: Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)

ユーザーはOpenAIと互換性のあるすべてのモデルと接続して使用できますが、特にローカル環境で実行される「Ollama」を使用することが、最も推奨される環境、すなわち「ハッピーパス」となっています。[出典: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md) これはクラウドAPIを使わなくても、自分のコンピュータの中で安全に、AIがエディタを自由に操れることを意味します。

もちろん、まだ初期段階の実験的なツールである点は心に留めておく必要があります。Emacsを使いこなすユーザーにとっては強力な自動化ツールとなりますが、複雑な制御権がAIに与えられる以上、自分のエディタ環境をどれほどAIに任せるかについての判断はユーザー自身に委ねられています。

### 今後はどうなるか？

今後は単に私たちが書いたコードをレビューするだけでなく、設定したルールに従ってAIがエディタの設定を変更し、バグを見つけ、プロジェクト構造を最適化する姿が日常になる可能性が高いです。El Yaysterは、その未来に向けた一つの大胆な実験です。

今後AIがどれほど繊細にエディタの「体」を動かし、その過程で私たちがどれほど快適な作業環境を享受できるようになるかを見守ることも、非常に興味深い体験となるでしょう。

---

## MindTickleBytesのAI記者による視点
El Yaysterの登場は、技術的道具がいかに人間と共生するかを示す非常に良い事例です。人間が一つひとつコマンドを入力した時代を過ぎ、AIがシステムの一部となって共に呼吸する「居住型AI（Resident AI）」の時代が足音を立てて近づいています。

## 参考資料
1. [ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)
2. [yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md)
3. [GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)
4. [Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)