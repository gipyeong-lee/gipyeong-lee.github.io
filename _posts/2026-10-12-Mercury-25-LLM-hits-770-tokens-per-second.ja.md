---
layout: post
title: "AIが私の言葉より速く答える？超高速言語モデル「Mercury 2.5」の物語"
description: "Inception Labsが公開した超高速拡散型AIモデル「Mercury 2.5」の性能と特徴を分かりやすく解説します。"
summary: "1秒間に770～1,107トークンを生成する超高速AI「Mercury 2.5」の登場により、リアルタイム対話型AIサービスの反応速度が劇的に改善される見通しです。"
tags: [AI, Mercury2.5, 人工知能, LLM]
image: 2026-10-12-Mercury-25-LLM-hits-770-tokens-per-second.jpg
image_alt: "データが高速で流れるデジタルネットワークを形取ったグラフィックイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Mercury 2.5は単に速度が速いだけでなく、拡散モデルに基づく並列処理という新しい技術的ブレイクスルーを示しています。これはAIが人間の会話速度を完全に追い越す時代が開かれたことを意味します。"
quiz:
  - question: "Mercury 2.5が従来のモデルと比較して持つ最大の特徴は何ですか？"
    choices: ["はるかに安い価格", "圧倒的なテキスト生成速度", "オフライン専用駆動"]
    answer: 1
    explanation: "Mercury 2.5は1秒間に770～1,107個のトークンを生成し、従来モデル比で約7倍の速度を記録しました。"
  - question: "Mercury 2.5はどのような技術方式に基づいていますか？"
    choices: ["トランスフォーマー(Transformer)専用モデル", "拡散(Diffusion)ベースのモデル", "逐次単純演算モデル"]
    answer: 1
    explanation: "Mercury 2.5はInception Labsが開発した拡散ベースの大型言語モデル(dLLM)です。"
  - question: "Mercury 2.5の文脈把握範囲(Context Window)はいくらですか？"
    choices: ["26万トークン", "10万トークン", "50万トークン"]
    answer: 0
    explanation: "Mercury 2.5は260,000トークンの大規模な文脈把握範囲をサポートします。"
lang: ja
ref: 2026-10-12-Mercury-25-LLM-hits-770-tokens-per-second
---

想像してみてください。友人とメッセンジャーで会話をしているとき、友人がこちらの質問が終わる前に正解を言い、送った長文を1秒で要約して返してくる状況を。まるで人間ではなく、自分と同じ速度で考える誰かが隣にいるかのようでしょう。

最近、人工知能(AI)業界でこうしたことが現実になっています。Inception Labsが発表した新しい言語モデル「Mercury 2.5」がその主人公です。単に賢いだけでなく、「光の速さ」で答えるこのモデルが私たちの日常をどう変えるのか、見ていきましょう。[出典: Inception Labsブログ](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)

### なぜ重要なのか？ (Why It Matters)

私たちが普段使っているAIチャットボットは、回答を出す際に時々「考える時間」が必要です。画面に文字が一つずつ「カタカタ」と現れるのを見たことがあるでしょう。これはAIが順を追って単語を作り出しているためです。

しかし、Mercury 2.5はこの速度の勢力図を完全に塗り替えました。AI分析企業「Artificial Analysis」の測定によると、このモデルは1秒間に約770.4トークン(AIが文字を処理する最小単位)を生成します。[出典: サム・コードマン](https://www.samcodeman.com/writing/mercury-2-5-770-tokens-per-second-benchmark) 開発会社の報告によると、特定の環境下では1秒間に1,107個まで可能だといいます。[出典: プラダ](https://www.pradha.id/read/mercury-25-inceptions-push-for-high-speed-diffusion-llms) これは従来のAIモデルより7倍も速い数値です。[出典: AIPULSEN](https://aipulsen.com/artikel/14260)

簡単に言えば、従来のAIが7秒間悩む分量を、Mercury 2.5はわずか1秒で終わらせるということです。このような速度が実現すれば、私たちがAIと音声で会話する際に感じていた微細な遅延時間(Latency)が解消されます。リアルタイム通訳機やコーディングアシスタントが、まるで実際の人間のよう即座に反応するようになるのです。[出典: TechBriefe](https://techbriefe.com/tech/ai/mercury-25-llm-achieves-770-tokens-per-second-in-inference-speed)

### 易しい解説 (The Explainer)

既存の大型言語モデル(LLM)は主に「トランスフォーマー(Transformer、文章内の単語間の関係を把握するAI構造)」という方式を使っていました。これは本を最初の文から終わりまで順番に律儀に読むようなもので、速度に明確な限界がありました。

一方、Mercury 2.5は「拡散(Diffusion)」方式というユニークな技術を使用します。[出典: OpenRouter](https://openrouter.ai/inception/mercury-2-5) 例えるなら、従来のAIが小説を一文字ずつ書き下ろす「誠実な作家」であれば、Mercury 2.5は画家が絵を描くときのように全体図を先に捉え、詳細な内容を一気に埋めていく「熟練の画家」に近いといえます。

この技術を専門用語で「並列トークン生成・精製(Parallel token generation and refinement)」と呼びます。複数の単語を同時に悩み、整えるため、はるかに速く結果を出せるのです。[出典: Benchable](https://benchable.ai/models/inception/mercury-2.5-20260908)

### 現状 (Where We Stand)

現在Mercury 2.5は、単に速いだけでなく、260,000トークンという巨大な文脈把握範囲(Context Window)を備えています。[出典: ブログ Build Fast With AI](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review) これは厚い本数十冊分もの情報を一度に読み込み、記憶できるという意味です。また、構造化されたデータ出力、ツール活用、複雑な論理的推論まで可能で、実務での活用度も高いです。[出典: ブログ Build Fast With AI](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review)

ただし、技術的な数値は測定方式によって差が出る可能性があり、非常に複雑な専門的作業において既存の巨大モデルと比較して実質的な性能優位を持つかどうかについては、ユーザーによるさらなる検証が必要な段階です。[出典: 6ic](https://6ic.com/news/mercury-25-llm-achieves-770-tokens-per-second-setting-new-benchmark-for-speed)

### 今後はどうなるか？ (What's Next)

今後のAIサービスは「どれだけ賢いか」を超えて「どれだけ速く反応するか」で競うことになるでしょう。特に音声アシスタントやリアルタイム相談、ゲーム内のNPC(ノンプレイヤーキャラクター)など、即座の反応が重要な分野でMercury 2.5のようなモデルの活躍が期待されます。[出典: CallMissed](https://www.callmissed.com/blog/mercury-diffusion-llm-770-tok-voice-latency) 皆さんのスマートフォンに、より速く反応するAIアシスタントが搭載され、質問を投げかけると同時に答えを聞く日がそう遠くないようです。

## 参考資料
1. サム・コードマン, [Mercury 2.5 770トークン/秒 ベンチマーク](https://www.samcodeman.com/writing/mercury-2-5-770-tokens-per-second-benchmark)
2. 6ic, [Mercury 2.5 LLM 1秒間に770トークン達成](https://6ic.com/news/mercury-25-llm-achieves-770-tokens-per-second-setting-new-benchmark-for-speed)
3. プラダ(Pradha), [Mercury 2.5: Inceptionの超高速拡散型LLM](https://www.pradha.id/read/mercury-25-inceptions-push-for-high-speed-diffusion-llms)
4. TechBriefe, [Mercury 2.5 LLM 推論速度 1秒間に770トークン達成](https://techbriefe.com/tech/ai/mercury-25-llm-achieves-770-tokens-per-second-in-inference-speed)
5. VK.ru, [Mercury 2.5 LLM 1秒間に770トークン到達](https://vk.ru/wall-238001904_6156)
6. Inception Labs, [Mercury 2.5 紹介](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)
7. クナール・ガングラニ(Kunal Ganglani), [Mercury 2.5 770トークン/秒 ベンチマーク (2026)](https://www.kunalganglani.com/blog/mercury-2-5-770-tokens-benchmark)
8. ブログ Build Fast With AI, [Mercury 2.5 AIモデルレビュー](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review)
9. AIPULSEN, [Mercury 2.5 LLM 1秒間に770トークン達成](https://aipulsen.com/artikel/14260)
10. CallMissed, [Mercury 2.5 拡散型LLM](https://www.callmissed.com/blog/mercury-diffusion-llm-770-tok-voice-latency)
11. Benchable, [Inception: Mercury 2.5 AIモデル詳細情報およびベンチマーク](https://benchable.ai/models/inception/mercury-2.5-20260908)
12. Telegram(Hacker News Feed), [Mercury 2.5 LLM 1秒間に770トークン到達](https://t.me/hacker_news_feed/132200)
13. OpenRouter, [Mercury 2.5 API価格およびベンチマーク](https://openrouter.ai/inception/mercury-2.5)