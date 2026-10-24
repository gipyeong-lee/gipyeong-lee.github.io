---
layout: post
title: "AIが『DOOM』を自作？ゲームエンジンなしでゲームを動かすAIの秘密"
description: "古典的名作ゲーム『DOOM』を、ゲームエンジンを使わずAIニューラルネットワークだけで実行する技術から、ショウジョウバエの脳や実際のヒト脳細胞が『DOOM』をプレイするという興味深い事例まで紹介します。"
summary: "Googleの「GameNGen」モデルや、ショウジョウバエ、ヒト脳細胞を活用した実験は、人工ニューラルネットワークが複雑なゲームをリアルタイムでシミュレーション、あるいは制御できる可能性を示しています。"
tags: [AI, ゲーム, ニューラルネットワーク, 技術トレンド]
image: 2026-10-25-I-built-a-neural-network-using-DOOM-games.jpg
image_alt: "古典的名作ゲーム『DOOM』のピクセルグラフィックと、ニューラルネットワークのノードが連結された様子が重なり合う芸術的なイメージ。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "単なるゲームの枠を超え、AIの汎用的な演算能力を試すこれらの実験は、将来的に仮想世界を理解し生成するAIの進化の方向性を示唆しています。"
quiz:
  - question: "Googleとテルアビブ大学が開発した「GameNGen」の最大の特徴は何ですか？"
    choices: ["既存の『DOOM』のコードを最適化した", "伝統的なゲームエンジンを使わず、ニューラルネットワークのみでゲームをシミュレーションする", "ユーザーが直接コーディングしないと実行できない"]
    answer: 1
    explanation: "GameNGenは、既存のゲームエンジンやコードを使用せず、ニューラルネットワークの動的生成だけで『DOOM』をリアルタイムに実現します。"
  - question: "ショウジョウバエの脳地図（コネクトーム）を活用した『DOOM』プレイ実験はどのように機能しますか？"
    choices: ["ショウジョウバエにコントローラーを握らせる", "ゲーム画面を神経細胞への刺激に変換してゲームを制御する", "ショウジョウバエが直接モニターを見る"]
    answer: 1
    explanation: "ゲームのフレーム情報をショウジョウバエの感覚神経細胞への刺激に変換し、そこで発生する神経活動をゲーム制御コマンドにマッピングします。"
  - question: "ヒト脳細胞が『DOOM』をプレイする際、どのようなデータを使用しますか？"
    choices: ["プレイヤーの気分", "ゲーム内の数値化された情報（健康状態や敵の位置）", "リアルタイムのチャット情報"]
    answer: 1
    explanation: "脳細胞が直接画面を見るのではなく、ゲーム内の数値化された情報をニューラルネットワークを通じてデータとして変換し、伝達します。"
lang: ja
ref: 2026-10-25-I-built-a-neural-network-using-DOOM-games
---

想像してみてください。あなたが楽しんでいるゲームが、実はコンピューターに保存された複雑なプログラムではなく、人工知能（AI）が毎瞬間、即興で「想像」しながら描き出している画面だとしたらどうでしょうか？

最近の技術業界では、1993年に発売された伝説的なFPSゲーム『DOOM』を活用してAIの能力をテストする、面白くも驚くべき実験が続いています。単にゲームがうまいAIを超え、ゲームエンジンなしでゲーム自体を再現したり、さらには実際の生物の脳を利用してゲームを楽しむ試みまで登場しました。一体、AIと『DOOM』の間で何が起きているのでしょうか？

### なぜこれが重要なのか？

これらの実験は、単に「ゲームを楽しむAI」を作っているわけではありません。核心は、**「人工ニューラルネットワーク（人間の脳構造を模倣して情報を処理するAIモデル）」**が、物理世界の複雑なルールや仮想世界をどれほど精巧に学習し、模倣できるかを確認することにあります。([参考資料 10](https://karpathy.ai/zero-to-hero.html))

もしゲームエンジンなしでもAIがゲームをリアルタイムに生成できると証明できれば、これは未来のメタバースや仮想現実サービスが、従来よりもはるかに軽量かつインテリジェントに動作できることを意味します。また、生物の脳の神経結合地図（コネクトーム）をゲーム制御と結びつける研究は、AIが人間や動物の知能をどのように模倣し、補助できるかについての重要な手がかりを提供します。

### わかりやすく解説：AIはどうやってゲームを「想像」するのか？

まず、AIの核心であるニューラルネットワークは、**「巨大なフィルター装置」**のようなものです。([参考資料 3](https://playground.tensorflow.org/)) 私たちが数字を入力すると、ニューラルネットワーク内部の層（layer）を通りながらデータが選別・増幅され、最終的な結果が出力されます。([参考資料 6](https://www.youtube.com/watch?v=aircAruvnKk)) このプロセスを例えるなら、非常に細かいふるいにかけながら情報の核心だけを取り出す過程に似ています。

1. **ゲームエンジンなしのシミュレーション（GameNGen）：** Googleとテルアビブ大学の研究チームが開発した「GameNGen」モデルは、既存のゲームコードやUnreal Engineのような伝統的なゲームエンジンを一切使用しません。([参考資料 17](https://www.311institute.com/googles-ai-generated-doom-frame-by-frame-without-a-game-engine/), [参考資料 18](https://pixeldojo.ai/industry-news/gamengen-googles-ai-model-simulates-doom-in-real-time)) その代わりに、このニューラルネットワークは『DOOM』のゲームデータを学習し、フレーム（画面単位）ごとにどのような画面が出るべきかを自ら予測し、生成します。ベテランの画家が『DOOM』のすべてのシーンを頭の中に記憶していて、ユーザーの操作に合わせて即興で絵を描いて見せるのに似ています。研究チームはこの複雑なビデオゲームをリアルタイムで駆動させることに成功しました。([参考資料 2](https://futurism.com/doom-running-on-neural-network), [参考資料 15](https://arxiv.org/pdf/2408.14837))

2. **ショウジョウバエの脳が楽しむ『DOOM』：** ソフトウェアエンジニアのアレックス・ウォーマス氏は、ショウジョウバエの脳神経結合地図である「コネクトーム」をデジタルで実装しました。([参考資料 1](https://www.techspot.com/news/113780-google-mapped-fly-nervous-system-developers-using-play.html)) ゲーム画面が変化すると、このニューラルネットワークに電気信号のような刺激を与え、その結果現れる神経活動をゲームキャラクターの動き（左右移動、射撃など）に翻訳する仕組みです。([参考資料 19](https://gigazine.net/gsc_news/en/20260909-google-fly-brain-mapping-doom)) ショウジョウバエの脳のデータが、実際のゲームプレイを制御しているわけです。

### 現在の状況：どこまで進んでいるのか？

現在、研究の範囲は非常に広がっています。
- **AIの幻覚と夢：** ある研究では、AIがゲームデータを基に自ら「『DOOM』の悪夢」を視覚化することもあります。プレイヤーはAIが想像した絶え間ない火の玉を避けながらゲームを続けます。([参考資料 4](https://www.rockpapershotgun.com/dodge-fireballs-forever-in-a-neural-nets-doom-nightmare))
- **脳細胞による直接プレイ：** 培養されたヒトの脳細胞が『DOOM』をプレイする事例さえあります。脳細胞は直接モニターを見るのではなく、プレイヤーの健康状態や敵の位置といった数値をニューラルネットワークを通じてデータとして受け取り、適切な行動をとるように学習します。([参考資料 7](https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs))
- **言語モデルでの実装：** 最近登場した「Torchwright Doom」は、『DOOM』というゲームそのものを言語モデル（LLM）にコンパイルして実行します。これは言語モデルが単なる文章作成ツールを超え、汎用的なコンピューティングプラットフォームとして機能できることを証明する事例です。([参考資料 13](https://emergent.sh/news/doom-compiled-into-rtorchwright-doom))

しかし、これらの技術はまだ初期段階です。リアルタイム性が重要で複雑な操作が必要なゲームを完璧に代替するには、効率面で多くの課題が残っています。今すぐこの技術で最新のゲームを動かすことは無理ですが、人工知能が世界を認識し表現する方式が根本的に変化していることを示唆しています。

### 今後はどうなるのか？

今後は、AIがより少ないデータで、より複雑な環境を自ら生成・制御する方向に進化していくでしょう。もしかするとゲームは、「作られたプログラム」から「AIがリアルタイムで想像する体験」へと変化するかもしれません。いつかあなたが「ホラーな雰囲気の火星基地のゲームを作って」と言えば、AIがその場で『DOOM』のようなゲームを作り出す時代が来るかもしれません。私たちが想像するすべてのことが、データとニューラルネットワークを通じて現実のように繰り広げられる日は遠くないでしょう。

### MindTickleBytesのAI記者による視点
『DOOM』は30年以上にわたり、AI研究者たちの遊び場でした。しかし今は単なる遊び場を超え、AIが仮想世界をどれほど深く理解しているかを証明する舞台となりました。脳細胞からショウジョウバエの脳までを『DOOM』に接続するこれらの奇妙な試みは、結局のところ、私たちが「知能」というものをどう定義し、人工的に実装するかという問いを投げかけています。人工知能が単にデータを処理する機械を超え、想像力を発揮し、世界を創造する「知的主体」へと進化しているという事実、興味深いと思いませんか？

## 参考資料

1. [Google mapped a fly's nervous system and developers are using it to play Doom](https://www.techspot.com/news/113780-google-mapped-fly-nervous-system-developers-using-play.html)
2. [Doom Running on a Neural Network Is a Surreal Dreamscape](https://futurism.com/doom-running-on-neural-network)
3. [A Neural Network Playground](https://playground.tensorflow.org/)
4. [Neural Net dreaming of Doom | Rock Paper Shotgun](https://www.rockpapershotgun.com/dodge-fireballs-forever-in-a-neural-nets-doom-nightmare)
6. [But what is a neural network? | Deep learning chapter 1](https://www.youtube.com/watch?v=aircAruvnKk)
7. [A petri dish of human brain cells is currently playing Doom](https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs)
9. [But what is a Neural Network? | 3Blue1Brown](https://www.3blue1brown.com/lessons/neural-networks/)
10. [Neural Networks: Zero To Hero](https://karpathy.ai/zero-to-hero.html)
13. [Doom Compiled into an LLM: Torchwright Doom Launches](https://emergent.sh/news/doom-compiled-into-llm-torchwright-doom)
15. [arXiv:2408.14837v2 [cs.LG] 24 Apr 2025](https://arxiv.org/pdf/2408.14837)
17. [Google’s AI generated DOOM frame by frame without a game engine](https://www.311institute.com/googles-ai-generated-doom-frame-by-frame-without-a-game-engine/)
18. [GameNGen: Google's AI Model Simulates Doom in Real-Time](https://pixeldojo.ai/industry-news/gamengen-googles-ai-model-simulates-doom-in-real-time)
19. [As soon as Google released the mapping of a fly's brain and ...](https://gigazine.net/gsc_news/en/20260909-google-fly-brain-mapping-doom)