---
layout: post
title: "AIと会話するようにコーディング？1978年の天才プログラマーが警告した「危険な錯覚」"
description: "人間のように自然言語でコンピュータと会話するプログラミングがなぜ危険なのか、1978年のエドガー・ダイクストラの鋭い洞察を通じて探ります。"
summary: "コンピュータ科学の巨匠エドガー・ダイクストラは、1978年にすでに自然言語プログラミングが精密な論理体系を崩壊させ、知的怠慢を招く可能性があるとして強く批判しました。"
tags: [プログラミング, AI, ダイクストラ, ソフトウェア工学]
image: 2026-10-23-The-foolishness-of-natural-language-programming-1978.jpg
image_alt: "複雑な記号で埋め尽くされた黒板の前で苦悩するプログラマーの姿。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "現代のLLMベースのコーディングはダイクストラの懸念とは異なり利便性を提供しますが、依然として「精密さ」という根本的な価値は人間の役目として残っています。"
quiz:
  - question: "エドガー・ダイクストラが自然言語プログラミングを批判した最大の理由は何ですか？"
    choices: ["自然言語の曖昧さ", "コンピュータ性能の不足", "ユーザー教育の難しさ"]
    answer: 0
    explanation: "ダイクストラは、自然言語が本質的に曖昧であり、精密さが命であるコンピュータプログラミングには適さないと考えました。"
  - question: "ダイクストラが指摘した「自然言語の曖昧さ」を代表する単語は何ですか？"
    choices: ["そして", "〜である(to be)", "もし"]
    answer: 1
    explanation: "「〜である」は「〜の一部である」という意味と「〜と等しい」という意味を同時に内包しており、コンピュータが混乱をきたす可能性があります。"
  - question: "ダイクストラが指摘した自然言語プログラミングへの依存現象を何と呼びましたか？"
    choices: ["新しい文盲", "知的怠慢", "論理的飛躍"]
    answer: 0
    explanation: "彼はこれを「新しい文盲（The New Illiteracy）」と呼び、強く警告しました。"
lang: ja
ref: 2026-10-23-The-foolishness-of-natural-language-programming-1978
---

想像してみてください。あなたがAIに「このデータを整理しておいて」と話しかけます。以前は複雑なコードを一列ずつ書く必要がありましたが、今は人と会話するように命令するだけで終わる世界になりました。私たちはこれを魔法のような技術の進歩だと考えています。しかし40年以上前、この分野の伝説的なコンピュータ科学者が一人、すでにこの現象を予見し警告を発していました。彼はこれを「新しい文盲（The New Illiteracy）」と呼びました。

### これがなぜ重要なのか？

今日、私たちは「AIがコーディングをすべて行ってくれる時代」に生きています。「自然言語（Natural Language、人間が日常的に使用する言語）」で命令するだけで成果物が完成するため、非常に便利です。しかし、私たちがAIの利便性に慣れるほど、コンピュータがなぜそのように動作するのか、論理的な精密さとは何なのかを次第に忘れてしまっています。1978年にエドガー・W・ダイクストラ（Edsger W. Dijkstra）が書いたエッセイ [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)は、今日においても依然として有効な警告を投げかけています。[参考資料 5, 参考資料 6, 参考資料 11, 参考資料 14]

### わかりやすく解説：自然言語はなぜプログラミングに不向きなのか？

ダイクストラは、自然言語が精密な思考の「同盟」ではなく、むしろ「敵」であると見ていました。[参考資料 6] 

簡単に例えるなら、日常会話は「フィルターが大量にかかった写真」のようなものです。私たちは友人に「あれ取っておいて」と言っても、文脈を通じて何のことか完璧に理解し合えます。しかしコンピュータは「フィルターが全くない超高解像度レンズ」のようなものです。命令を少しでも曖昧に入力すれば、見当違いのデータを取得してしまいがちです。 

ダイクストラはその代表的な例として「〜である（to be）」という動詞を挙げました。[参考資料 14] 英語の「is」や他言語における対応語は二つの意味を持ちます。「ジョンは学生である（〜の一部である）」という意味にもなり、「ジョンは犯人である（〜と等しい）」という意味にもなります。私たち人間は文脈で区別しますが、コンピュータは論理的に全く異なる二つの命令を混同する可能性があります。そのため、コンピュータプログラミングにはこうした曖昧さを取り除いた、0と1のように明確な「形式記号（Formal Symbolism）」が不可欠であるというのが彼の主張の核心です。[参考資料 1, 参考資料 2, 参考資料 14]

### 現状：利便性と精密さの間の綱渡り

もちろん今日の人工知能モデルは、過去の自然言語プログラミングとは次元の異なる規模と精巧さを持っています。[参考資料 9] しかしダイクストラの懸念は依然として鋭い視点を突いています。彼は、自然言語プログラミングのトレンドが結局はユーザーの「知的怠慢」を助長し、プログラミングが要求する不可欠な訓練と精密さを削り取る「愚かな行為（foolishness）」であると批判しました。[参考資料 12] 

私たちは今、「バイブコーディング（Vibe Coding、感覚でコーディングする）」の時代を生きていますが、AIが生成したコードがなぜエラーを出したのかを自分で判断する能力を失ってしまえば、それこそが本当に「新しい文盲」の時代になるかもしれません。[参考資料 6, 参考資料 7]

### 今後はどうなるのか？

技術は発展し続けますが、私たちが記憶すべきことは一つです。AIが自然言語を理解するからといって、プログラミングが「正確でなくてもよい作業」に変わったわけではないという点です。いつかAIが私たちのすべての命令を完璧に理解する日が来ても、コンピュータは依然として人間が入力した論理体系の中でしか動作しません。自然言語を使うか、記号を使うかに関わらず、プログラミングの本質は「正確で精密な論理の実装」であるというダイクストラの教えは、今後も変わることはないでしょう。 

---

### MindTickleBytesのAI記者視点

ダイクストラの鋭い批判は、まるで1978年から届いた警告状のようです。私たちがAIにコーディングを任せて利便性を享受する間、本来の論理的厳密さという基礎体力を失ってはいないか振り返らされます。道具が優れるほど、ユーザーの基本はより堅実でなければならないという真理を忘れてはならないでしょう。

---

## 参考資料

1. [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)
2. [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html?fileGuid=H2TBGtSx56EjErDS)
3. [On the foolishness of "natural language programming"](https://research.tue.nl/en/publications/on-the-foolishness-of-natural-language-programming/)
4. [Dijkstra Called It in 1978: Natural Language Programming Is Still ...](https://www.daita.io/en/blog/dijkstra_natural_language_programming/)
5. [PDF On the foolishness of "natural language programming"](https://link.springer.com/content/pdf/10.1007/BFb0014656.pdf)
6. [On Natural Language Programming – @dsyme on software](https://dsyme.net/2025/08/27/on-natural-language-programming/)
7. [On the foolishness of "natural language programming"](https://research.tue.nl/en/publications/on-the-foolishness-of-natural-language-programming)
8. [Of course. EWD 1008, titled "On the foolishness of 'natural language.....](https://pastebin.com/Kd5PARvB)
9. [Dijkstra on foolishness of Natural Language Programming](https://daily.dev/posts/dijkstra-on-foolishness-of-natural-language-programming-tzpv24mqa)
10. [Ten months ago, I published an article by Edsger W. Dijkstra from 1978...](https://www.linkedin.com/posts/sdalbera_ten-months-ago-i-published-an-article-by-activity-7427226210809745408-JEZv)