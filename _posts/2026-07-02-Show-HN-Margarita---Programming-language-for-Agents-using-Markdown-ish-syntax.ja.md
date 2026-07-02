---
layout: post
title: "AIアシスタント作り、メモ帳を書くくらい簡単になる？マークダウンで設計する「Margarita（マルガリータ）」"
description: "プログラミングを知らなくてもAIエージェントを作れるのでしょうか？マークダウン形式を拡張し、AIエージェントのワークフローを体系的に記述する新しいツール、Margaritaを紹介します。"
summary: "Margaritaは、マークダウン構文に変数やループなどのプログラミング機能を加え、誰でも簡単にAIエージェントのワークフローを設計できるよう支援するツールです。"
tags: [AI, エージェント, マークダウン, プログラミング, Margarita]
image: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax.jpg
image_alt: "マークダウン構文を利用してAIエージェントの複雑なワークフローを体系的に構造化した様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "複雑なコーディングなしでAIエージェントのロジックを設計しようとする試みは、エージェント大衆化の重要な鍵となるでしょう。"
quiz:
  - question: "Margaritaの主要な特徴の一つである.mgxファイル形式は何をサポートしていますか？"
    choices: ["静的テキスト生成", "AIエージェントの実行制御（状態、メモリ、ツール呼び出しなど）", "単純なHTML変換"]
    answer: 1
    explanation: ".mgx形式は従来の.mg形式を拡張し、AIエージェントが実行される際に必要な状態管理やツール呼び出しなどの機能を補完します。"
  - question: "Margaritaを使用するために必要なAIモデルは何ですか？"
    choices: ["すべての種類のモデル", "OllamaとClaude", "特定の言語モデルのみ可能"]
    answer: 1
    explanation: "Margaritaは現在、使用のためにOllamaとClaudeを必要とします。"
  - question: "Margaritaの目標は何ですか？"
    choices: ["複雑なプログラミング言語の学習", "マークダウンと同じくらい簡単にエージェントを作成すること", "検索エンジン最適化"]
    answer: 1
    explanation: "Margaritaは、エージェントを作成する作業がマークダウンを書くことと同じくらい簡単になるようにすることを目指しています。"
lang: ja
ref: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax
---

想像してみてください。朝起きてAIアシスタントに「今日の会議資料をまとめて要約して」と伝えます。するとAIは、まるで人間のように自ら必要なファイルを探し出し、内容を要約して、その結果をメールで送信してくれます。このような賢いアシスタントを私たちは「AIエージェント」と呼びます。しかし、このようなエージェントを作る過程は、これまで非常に複雑でした。開発者は複雑なコードを書き、AIが指示通りに動くよう、絶えず「プロンプト（AIへの指示文）」と格闘しなければなりませんでした。

ところが最近、私たちがブログを書いたりメモをとったりするときに使う「マークダウン（Markdown、Webドキュメントを簡単に作成するための構文）」のように、非常にシンプルにAIエージェントを設計できる新しいツールが登場しました。それが「Margarita（マルガリータ）」です。

### なぜこのツールが重要なのか？

これまでAIとコミュニケーションをとる方法は、主に「対話」中心でした。しかし対話は時として、AIがユーザーの意図を誤解したり、長い作業プロセスの中で迷子になったりすることもありました。開発者はAIに複雑な業務を段階的に完遂させるため、プロンプト作成に追われる必要がありました。[出典 1](https://www.margarita.run/)

Margaritaはこの困難を解決します。AIエージェントの行動を複雑なコードではなく、誰にとっても馴染み深いマークダウン方式で、決められたルールに従って設計できるようにするためです。これは、もはや複雑なプロンプトエンジニアリングに頼らなくても、望む結果を体系的かつ一貫して得られることを意味します。[出典 1](https://www.margarita.run/)

### わかりやすく解説：マークダウンに翼を授ける

Margaritaを理解するために一つ例え話をしましょう。料理をする時にレシピカードを書くと想像してみてください。従来の方式が、料理人にいちいち「今、玉ねぎを切ってください」「次は火加減を調整してください」と指示しながら付き添うことだとしたら、Margaritaはあらかじめ体系的な「レシピカード」を作成しておくことと同じです。

簡単に言えば、Margaritaは私たちがよく知るマークダウン構文にプログラミング機能をミックスしました。[出典 1](https://www.margarita.run/) 主な機能は以下の通りです。
- **変数（Variable）**: 情報の値を保存する枠。
- **ループ（Loop）**: 複数の項目を一つずつ順番に処理するルール。
- **条件文（Conditional）**: 「もし〜なら、こうせよ」という決定。

このようにマークダウンに論理的な機能を加え、AIエージェントがどのような状況でどう行動すべきかを明確に記述するのです。[出典 4](https://github.com/Banyango/margarita) Margaritaは2つのファイル形式を提供します。[.mgファイル](https://pypi.org/project/margarita/)は動的なプロンプトを作るのに使われ、[.mgxファイル](https://pypi.org/project/margarita/)はさらに進んでエージェントのメモリ管理やツール呼び出しまで制御する「エージェントスクリプト」の役割を果たします。[出典 2](https://pypi.org/project/margarita/)

こうして作成された結果物は、基本的に私たちがよく知るマークダウン形式でレンダリング（画面表示）されるため、マークダウンをサポートしている場所ならどこでも使用できます。[出典 4](https://github.com/Banyango/margarita)

### 現在の状況：どこまで進んでいるか？

Margaritaは、開発者がエージェントを構成しロジックを積み上げていく過程を大幅にシンプルにしてくれます。特に複数のテンプレートを分けて保存し、必要な時に呼び出したり重ねて使用（Nested）したりすることが可能になり、業務効率を大きく高めました。[出典 3](https://www.banyango.com/margarita/)

ただし、現在このツールを活用するためにはOllamaとClaudeモデルの環境設定が必要であるという点は覚えておくべきです。[出典 3](https://www.banyango.com/margarita/) つまり、完全な初心者が使うというよりは、ある程度AI開発環境に対する理解があるユーザーが生産性を高めるために活用するのに適した段階と言えます。

### 今後はどうなるか？

専門家は、近い将来マークダウンが単なる文書形式を超え、ソフトウェア開発のコア言語として定着すると予測しています。[出典 13](https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html) Margaritaのようなツールは、このような流れを加速させるでしょう。今後、AIエージェントを作る作業はますます自然な言語や親しみのある文書形式に近づいていくはずです。あなたもこれからは「プロンプト」をひねり出す人ではなく、エージェントという「秘書の行動マニュアル」を作成する管理者になる時代が到来しています。

---

### MindTickleBytesのAI記者による視点
技術が複雑になるほど、それを扱うツールはより直感的で簡単でなければなりません。マークダウンでエージェントを定義しようとするMargaritaの試みは、AIと人間が協業する方法を根本的により透明にしてくれるでしょう。

---

## 参考資料
1. Margarita — Writing agents should be as easy as writing markdown. (https://www.margarita.run/)
2. margarita · PyPI (https://pypi.org/project/margarita/)
3. MARGARITA - MARGARITA (https://www.banyango.com/margarita/)
4. GitHub - Banyango/margarita: Margarita is a lightweight ... (https://github.com/Banyango/margarita/)
13. Markdown is now a first-class coding language: Deal with it | InfoWorld (https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html)