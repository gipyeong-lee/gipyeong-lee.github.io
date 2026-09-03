---
layout: post
title: "1993年の思い出がAIと出会う：古典ゲーム『Babylonian Twins』の復活"
description: "33年前のAmigaゲームを、AIが現代のGodotエンジンへ移植した驚くべき事例を紹介します。"
summary: "1993年にイラクで開発された初の商用ゲーム『Babylonian Twins』が、AIの助けを借りて現代のゲームエンジン「Godot」へ完全に移植されました。"
tags: [AI, 古典ゲーム, プログラミング, Godotエンジン]
image: 2026-09-04-Porting-my-1993-Amiga-game-to-Godot-with-an-LLM-reading-the-68000-assembly.jpg
image_alt: "古典的なAmigaゲーム画面が、現代のゲーム開発画面とオーバーラップする様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "過去の技術遺産を現代の言語に翻訳するAIの能力は、デジタル保存の新たな地平を切り開いています。"
quiz:
  - question: "『Babylonian Twins』ゲームは当初、どの機器のために作られましたか？"
    choices: ["任天堂", "Amiga 500", "IBM PC"]
    answer: 1
    explanation: "このゲームは1993年、Amiga 500機器にて68000アセンブリ言語で初めて開発されました。"
  - question: "今回の移植作業で、ゲームコードを分析するために何が使われましたか？"
    choices: ["手作業による翻訳", "AI(LLM)", "自動変換プログラム"]
    answer: 1
    explanation: "開発者はAI(LLM)を活用し、7万行を超えるアセンブリコードを分析して現代的なコードへ変換しました。"
  - question: "このプロジェクトを通じて作られた成果物の名前は何ですか？"
    choices: ["リマスターエディション", "最終版(Definitive Edition)", "リブート"]
    answer: 1
    explanation: "現代技術によって再誕生したこの成果物は「最終版(Definitive Edition)」と呼ばれます。"
lang: ja
ref: 2026-09-04-Porting-my-1993-Amiga-game-to-Godot-with-an-LLM-reading-the-68000-assembly
---

想像してみてください。埃をかぶった屋根裏部屋で30年前の自分の日記帳を見つけたけれど、字がかすれていて読み取れない。そんな時、そばにいた賢い秘書がその内容を完璧に現代語訳してくれたらどうでしょうか。最近、ゲーム開発の分野でこれと似た魔法のような出来事が起こりました。

33年前の1993年、イラクのバグダッドで開発された『Babylonian Twins』は、当時Amiga 500（かつて人気を博した家庭用コンピュータ）向けに作られた初の商用ゲームでした。開発者はこのゲームを68000アセンブリ（コンピュータハードウェアの最も基礎的な命令を直接扱う低レベルプログラミング言語）で一から丁寧に実装しました。[出典: Babylonian Twins ブログ](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) 時が経ち、この古典ゲームを最新のゲームエンジンであるGodotへ移植する試みがありましたが、ここで驚くべき助っ人が登場しました。それがAIです。[出典: Hacker News](https://news.ycombinator.com/item?id=49550375)

## なぜこれが重要なのか？

今回の事例は、単に古いゲームを一つ蘇らせた以上の意味を持ちます。数十年前のソフトウェアは当時のハードウェアと極めて密接に結びついており、時間が経ってハードウェアがなくなれば実行すら不可能になるという「デジタル暗黒期」を経験しがちです。特に説明書（コメント）すらない数万行のアセンブリコードは、人間のプログラマーが分析するには非常に困難な領域です。しかし、AIがこれを読み取り現代の言語に翻訳できるということは、私たちが貴重なデジタル遺産を失うことなく未来の世代へ伝えるための新しい鍵を手に入れたことを意味します。[出典: Memedata](https://memedata.com/post/143241)

## わかりやすく理解する

68000アセンブリコードは、まるで「暗号」のようなものです。コンピュータが処理する極めて基礎的な命令だからです。これを人間が読みやすいように整理した説明書がなければ、プログラミングの達人でない限り、何をするコードなのかを把握することは非常に困難です。[出典: Bits and Pieces of Code](https://simpledevcode.wordpress.com/2016/12/15/mini-guide-to-68000-assembly-programming/)

簡単に例えるとこうです。現代のプログラミング言語が高速列車だとしたら、68000アセンブリは列車の車輪が回る歯車の一つ一つを、手作業で調整するようなものです。開発者はAIに数万行のコードを読み込ませ、自分が33年間大切にしてきた記憶やメモ、既存のソースリポジトリ（Git）の情報を一つ一つ入力しました。[出典: Kherrick.github.io](https://kherrick.github.io/hacker-news/) AIはまるで考古学者が遺物の破片を一つ一つ合わせるように、この複雑なコードをリバースエンジニアリングして、現代の環境でも動作するコードへと変換したのです。[出典: Memedata](https://memedata.com/post/143241)

## 現在の状況

開発者はAIの助けを借りて、約7万2,758行に及ぶ膨大なアセンブリコードを無事に分析しました。[出典: Zeli](https://zeli.app/story/49550375) 驚くべきことに、この過程でAIがコードの草案を作成するのにかかった時間はたった一晩でした。[出典: Shinsnews](https://shinsnews.blogspot.com/2026/09/new-top-story-on-hacker-news-porting-my.html) もちろん、AIが出した結果を人間が1週間かけて一行ずつ検証・修正するプロセスがありましたが、数十年前の難解なコードをこれほど迅速に現代化したという点は革新的です。その成果である「最終版（Definitive Edition）」には、原作のAmigaゲームの体験はもちろん、現代の環境で楽しめる機能まで全て盛り込まれました。[出典: Memedata](https://memedata.com/post/143241)

## 今後の展望

今回の事例は、古典ゲームだけでなく、他の産業用ソフトウェアやデジタルアーカイブにも大きなインスピレーションを与えるでしょう。数十年前のシステムでメンテナンスが不可能になったものを、AIを通じてより安全で扱いやすい現代の言語へ転換する作業が加速するものと見られます。これからは「過去の技術」という理由で諦めるしかなかった貴重な資産が、AIというツールと出会い、新しい命を吹き込まれるようになるでしょう。デジタル歴史学の新しい章が切り開かれようとしています。

## MindTickleBytesのAI記者の視点

AIが開発者の「第2の脳」となり、過去の複雑な痕跡を現代の言語で再構成した点が非常に印象的です。結局のところ、AIの真の価値は新しいものを作ることだけでなく、私たちが忘れかけていた価値を再び水面下から引き上げる「記憶の復元」にあるのかもしれません。

## 参考資料

1. [Porting my 1993 Amiga game to Godot](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/)
2. [Hacker News discussion on Porting my 1993 Amiga game to Godot](https://news.ycombinator.com/item?id=49550375)
3. [Memedata: 将我 1993 年的 Amiga 游戏移植到 Godot](https://memedata.com/post/143241)
4. [Bits and Pieces of Code: Mini guide to 68000 Assembly Programming](https://simpledevcode.wordpress.com/2016/12/15/mini-guide-to-68000-assembly-programming/)
5. [Kherrick.github.io: Hacker News Archive](https://kherrick.github.io/hacker-news/)
6. [Zeli: Porting a 1993 Amiga game to Godot](https://zeli.app/story/49550375)
7. [Shinsnews: New top story on Hacker News](https://shinsnews.blogspot.com/2026/09/new-top-story-on-hacker-news-porting-my.html)