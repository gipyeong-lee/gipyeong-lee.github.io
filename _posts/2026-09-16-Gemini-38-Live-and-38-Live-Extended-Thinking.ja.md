---
layout: post
title: "AIと「会話」するということ、Gemini 3.8 Liveが変える風景"
description: "Googleが新たに発表したGemini 3.8 LiveとExtended Thinkingが、私たちの音声AIアシスタントの使用体験をどのように賢く、自然に変えていくのかを分かりやすく解説します。"
summary: "Googleの最新音声モデルGemini 3.8 LiveとExtended Thinkingは、リアルタイム音声会話能力を大幅に強化し、AIが複雑なタスクを実行しながらも会話の流れを途切れさせないようサポートします。"
tags: [AI, Google, Gemini, 音声認識, テックトレンド]
image: 2026-09-16-Gemini-38-Live-and-38-Live-Extended-Thinking.jpg
image_alt: "スマートフォンを通じて自然に会話する人とAI音声アシスタントの様子をイメージしたイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人間の会話とは、単に情報をやり取りするだけでなく「思考の流れ」を共有するプロセスです。今回のモデルは、AIが人間のこの流れを妨げることなく、共に悩むことができるレベルに一歩近づきました。"
quiz:
  - question: "今回発表された「Extended Thinking」モデルの最大の特徴は何ですか？"
    choices: ["画像だけを認識できる", "作業の進行状況を自ら説明し、会話の流れを維持する", "テキストでのみ会話が可能である"]
    answer: 1
    explanation: "Extended Thinkingモデルは、AIが複雑なタスクを処理している間も会話が途切れないよう、自身の思考や作業の進行状況を音声で説明する機能が強化されました。"
  - question: "Gemini 3.8 Liveモデルが処理できる入力データの種類は何ですか？"
    choices: ["音声データのみ", "テキストのみ", "音声、画像、ビデオ、テキスト"]
    answer: 2
    explanation: "新しいモデルは音声だけでなく、画像、ビデオ、テキストまで含めたマルチモーダル入力をサポートしています。"
  - question: "今回のモデルがArtificial AnalysisのSpeech-to-Speechランキングで記録した総合スコアは何点ですか？"
    choices: ["70.5点", "82.6点", "90.0点"]
    answer: 1
    explanation: "Gemini 3.8 Live Extended Thinkingモデルは、Artificial Analysisの音声会話品質指数で82.6点を記録し、総合1位を獲得しました。"
lang: ja
ref: 2026-09-16-Gemini-38-Live-and-38-Live-Extended-Thinking
---

想像してみてください。朝起きてスマートフォンに向かって「今日は会議が多いから、昼食の時間に合わせて一番近いレストランを探して予約しておいて」と話しかけます。これまでのAIアシスタントなら、レストランを探して予約する間「少々お待ちください」と止まったり、会話が途切れたりしがちでした。しかしこれからは、AIがまるでそばにいる有能な秘書のように「レストランを探しています。良さそうなところがいくつかありますが、12時30分に予約可能な場所でよろしいですか？」と、途切れることなく会話を続ける世界が到来しています。

Googleが最近発表した「Gemini 3.8 Live」と「Gemini 3.8 Live Extended Thinking」は、まさにこのような未来を現実のものにする、最も先進的な音声会話モデルです[出典 1](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) [出典 4](https://9to5google.com/2026/09/15/gemini-3-8-live-announced/)。

## なぜこれが重要なのか？

これまで私たちが使用していた多くの音声AIは、質問を投げかけるとデータを検索して回答を生成する間、会話が一時停止しているような感覚を与えていました。これは、料理人が料理を作っている間、厨房から音が全く聞こえず、料理が完成して初めてまた声が聞こえてくるようなものでした。

しかし今回リリースされたモデルは、「リアルタイム音声エージェント」のために設計されています[出典 3](https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/)。ユーザーとAIが会話している途中でも、AIが自ら複雑なタスクを実行し、その内容をユーザーにフィードバックすることで、会話の文脈が損なわれないようサポートします[出典 1](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)。これは、AIとのより自然で深いコラボレーションが可能になることを意味します。

## 簡単に理解する

この技術を理解するために、2つの例えを紹介します。

1つ目は、**「考えながら話す」**です。「Gemini 3.8 Live Extended Thinking」モデルは、私たちが悩む時に独り言を言うのと似ています。AIが複雑なリクエストを処理する際、「今、データを調べています」あるいは「この情報を処理するのに少し時間がかかっています」と進捗状況を音声で伝えてくれます[出典 8](https://www.linkedin.com/posts/googledeepmind_meet-gemini-38-live-and-38-live-extended-activity-7505673159484887041-kOy1)。こうすることで、ユーザーはAIが応答を諦めたのではなく、今一生懸命作業中であることを知ることができます。

2つ目は、**「目と耳を持つ魔法使い」**です。これらのモデルは単に声を聞くだけではありません。音声、画像、ビデオ、そしてテキストまでを一度に理解できる「マルチモーダル（Multimodal：多様な形態のデータを同時に理解する技術）」AIです[出典 2](https://deepmind.google/models/model-cards/gemini-3-8-audio/)。まるで目と耳の両方を持つ人が状況を総合的に判断して会話に参加するのと同じです。これは、最大128K（約12万8千個）トークンという膨大な量の情報を一度に記憶し分析できるために可能なことです[出典 2](https://deepmind.google/models/model-cards/gemini-3-8-audio/)。

## 現在の状況

現在、Googleのこれらのモデルは既に驚くべき成果を見せています。「Artificial Analysis」という機関の評価によると、「Gemini 3.8 Live Extended Thinking」モデルは「音声会話品質指数（Speech-to-Speech Quality Index）」で総合1位を獲得しました[出典 10](https://jetstream.blog/2026/09/16/gemini-3-8-live/)。82.6点という高いスコアを記録し、業界最高レベルの性能を証明したのです[出典 7](https://tech-insider.org/gemini-3-8-live-extended-thinking-launch-2026/) [出典 12](https://modelora.ru/news/google-vypustila-gemini-3-8-live-2026-09-15)。

また、世界的に97以上の言語をサポートしているため、韓国語はもちろん、様々な言語のユーザーがAIアシスタントとより便利にコミュニケーションをとれるようになりました[出典 11](https://ai-manual.ru/article/gemini-38-live-i-38-live-extended-thinking-golosovyie-ai-agentyi-s-parallelnyim-myishleniem/) [出典 15](https://zerohour.day/item/36f0b78f2fd7dd1a9afa956fc24789a35710f898)。GeminiアプリやGoogle AI Studioを通じて、この技術を直接体験することができます[出典 8](https://www.linkedin.com/posts/googledeepmind_meet-gemini-38-live-and-38-live-extended-activity-7505673159484887041-kOy1)。

## 今後はどうなるか？

Googleはここ数ヶ月間、ほぼ3週間ごとに主要なGeminiモデルをアップデートするという速い動きを見せています[出典 5](https://shattered.io/gemini-3-8-live-extended-thinking-launch-2026/)。これは、AIが私たちが使用する日常的なデバイスにいかに急速に溶け込んでいるかを示しています。

今後、AIアシスタントは単なる命令伝達機を超え、私たちが業務を行ったり悩み事を分かち合ったりする際に共に考え、アドバイスをくれる真の「パートナー」へと発展するでしょう。今回のアップデートは、AIとの会話が技術的な通信を超え、人間的な相互作用により近づくための重要なマイルストーンとなるはずです。

## MindTickleBytesのAI記者からの視点
人間の会話とは、単に情報をやり取りするだけでなく「思考の流れ」を共有するプロセスです。今回のモデルは、AIが人間のこの流れを妨げることなく、共に悩むことができるレベルに一歩近づきました。

## 参考資料
1. [Gemini 3.8 Live & Gemini 3.8 Live Extended Thinking - The Keyword](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)
2. [Gemini 3.8 Audio (Live, Live Extended Thinking) - Model Card](https://deepmind.google/models/model-cards/gemini-3-8-audio/)
3. [Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking for Production-Grade Voice Agents](https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/)
4. [Gemini 3.8 Live Extended Thinking powers Gemini Live, Gmail](https://9to5google.com/2026/09/15/gemini-3-8-live-announced/)
5. [Gemini 3.8 Live & Extended Thinking: Google Voice AI [2026]](https://shattered.io/gemini-3-8-live-extended-thinking-launch-2026/)
7. [Gemini 3.8 Live Launch: 82.6 Voice AI Score [2026]](https://tech-insider.org/gemini-3-8-live-extended-thinking-launch-2026/)
8. [Meet Gemini 3.8 Live and 3.8 Live Extended Thinking: our best...](https://www.linkedin.com/posts/googledeepmind_meet-gemini-38-live-and-38-live-extended-activity-7505673159484887041-kOy1)
10. [「Gemini 3.8 Live/3.8 Live Extended Thinking」正式発表 – Jetstream](https://jetstream.blog/2026/09/16/gemini-3-8-live/)
11. [Gemini 3.8 Live и 3.8 Live Extended Thinking... | AiManual](https://ai-manual.ru/article/gemini-38-live-i-38-live-extended-thinking-golosovyie-ai-agentyi-s-parallelnyim-myishleniem/)
12. [Google DeepMind выпустила Gemini 3.8 Live и Extended Thinking...](https://modelora.ru/news/google-vypustila-gemini-3-8-live-2026-09-15)
13. [Gemini 3.8 Live: Google Splits Its Voice Line in Two](https://www.orcarouter.ai/blog/gemini-3-8-live-release)
14. [Gemini 3.8 Live Extended Thinking Pricing, Specs & Sources](https://benchlm.ai/models/gemini-3-8-live-extended-thinking)
15. [Google launches Gemini 3.8 Live to take on OpenAI's GPT-Live-1 at...](https://zerohour.day/item/36f0b78f2fd7dd1a9afa956fc24789a35710f898)