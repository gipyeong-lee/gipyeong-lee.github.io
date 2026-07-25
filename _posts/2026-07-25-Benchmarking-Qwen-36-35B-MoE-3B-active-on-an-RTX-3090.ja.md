---
layout: post
title: "マイPCでAIが爆速駆動？Qwen 3.6 35B MoEで知るローカルAIの世界"
description: "高性能AIモデル「Qwen 3.6 35B MoE」をRTX 3090グラフィックボードで実際に動かした性能テストの結果と、ローカルAIの活用法をわかりやすく解説します。"
summary: "RTX 3090でQwen 3.6 35B-A3Bモデルを実行すると毎秒100トークン以上の生成が可能で、一般的な27B密モデルよりもはるかに高速な体験が得られます。"
tags: [AI, ローカルLLM, Qwen, RTX3090, ハードウェア]
image: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090.jpg
image_alt: "RTX 3090グラフィックボード上で駆動するQwen 3.6 AIモデルの性能を測定する様子。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ローカル環境で大規模モデルを効率的に駆動することは、データプライバシーとコストの面で大きな利点があります。特にMoE構造を活用すれば、ハードウェアの制約を賢く乗り越えることが可能です。"
quiz:
  - question: "MoE（Mixture-of-Experts）構造のモデルが一般的な密モデル（Dense Model）よりも高速な理由は？"
    choices: ["すべてのパラメータを常に使用するため", "一度に3B（30億）程度の活性パラメータのみを処理するため", "RTX 3090に最適化されたコードのみが含まれているため"]
    answer: 1
    explanation: "MoEモデルはモデル全体のなかから一部の専門家（パラメータ）のみを選んで動作するため、35Bサイズのモデルであっても3B程度の活性パラメータのみを使用し、演算速度が速くなります [Source 5]。"
  - question: "RTX 3090でQwen 3.6 35B-A3Bモデルを実行した際の性能はどの程度ですか？"
    choices: ["毎秒5〜10トークン", "毎秒50〜100トークン以上", "毎秒1,000トークン以上"]
    answer: 1
    explanation: "テスト結果によりますが、設定次第で毎秒50から100トークン以上の生成速度を示します [Source 2], [Source 5], [Source 7]。"
  - question: "性能の高い27B密モデルと35B-A3B MoEモデルのどちらかを選択すべき場合、アドバイスは？"
    choices: ["無条件で35Bモデルが優秀", "回答品質を重視するなら27B密モデルを推奨", "両者に性能差は全くない"]
    answer: 1
    explanation: "27B密モデルはベンチマーク結果においてMoEモデルより1〜10ポイントほど上回るため、回答品質が優先される場合に推奨されます [Source 3]。"
lang: ja
ref: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090
---

想像してみてください。毎日使っているPCに入っているAIアシスタントが、ネット接続なしでも非常に複雑な質問に1秒で答えてくれるとしたらどうでしょう？個人情報流出の心配をせず、自分のPCの中だけで安全に動く「自分専用のAI」を持つことは、もはやSF映画の中の話ではありません。最近リリースされた強力なAIモデル「Qwen 3.6 35B-A3B」が、どのようにしてこれを現実にしているのか、高校生でもわかるように解説します。

### なぜこれが重要なのか？ (Why It Matters)

かつて、高性能なAIモデルは巨大すぎて、一般ユーザーのPCで動かすことなど到底考えられませんでした。しかし今は違います。「ローカルAI（ネット接続なしでユーザーの端末上で直接動作するAI）」技術が飛躍的に発展し、家庭にあるRTX 3090のようなグラフィックボードだけでも、レベルの高いAIを十分に体験できるようになりました [Source 8]。

ローカルAIが注目される理由は主に2つあります。1つ目は**プライバシー**です。データが外部サーバーへ送られずPC内で処理されるため、安心です。2つ目は**速度と経済性**です。ネット速度に左右されず、モデルを一度ダウンロードすれば追加費用なしで使い放題です。今回テストしたQwen 3.6 35B-A3Bモデルは、そうしたローカルAI環境において特に優れたコスパと性能を見せており、注目を集めています [Source 6]。

### わかりやすく解説 (The Explainer)

Qwen 3.6 35B-A3Bモデルの核心は、**MoE（Mixture-of-Experts、専門家混合構造）**という特別な設計にあります。

簡単に例えてみましょう。巨大な図書館を運営しているとします。すべての本を1人の司書が管理するのは無理ですよね。そこで、分野別の専門司書を何人も雇ったと想像してください。ここで「35B」は司書の総数（全体のパラメータ数）を指し、「3B active」は質問が入ったときに実際に答えを探すために呼び出す司書の数（活性パラメータ数）を意味します [Source 5]。

一般的な「密モデル（Dense Model）」がすべての司書が毎回働く構造だとしたら、MoEモデルは質問の内容に応じて、必要な分野の司書だけが働きます。おかげでモデルは350億個のパラメータを持つほど非常に賢い一方で、実際に頭を使うときは30億個分だけの計算で済むため、素早く結果を出せるのです [Source 5]。

### 現状 (Where We Stand)

実際にRTX 3090グラフィックボードで行ったベンチマークテストの結果は驚くべきものです。

* **速度**: 特定の設定（UD-Q4_K_XL量子化）を適用した場合、短い質問には毎秒約101.7トークン（AIが文字を生成する単位）、長い質問には80.9トークンを生成します [Source 7]。他の環境でも毎秒50〜100トークン水準を維持しており、これは27B密モデル（毎秒約35トークン）よりもはるかに高速です [Source 5]。
* **限界**: もちろん、単純に巨大で速いMoEモデルが正解とは限りません。27B密モデルと比較すると、回答の正確さ（品質）の面では、27B密モデルが1〜10ポイントほど高いベンチマーク結果を示しました [Source 3]。つまり、速度が最も重要ならMoEモデルを、回答品質が優先なら密モデルを選ぶのが賢明です [Source 3]。
* **最適化**: また、AI学習手法の一つである「推論加速手法（Speculative Decoding）」は、意外にもRTX 3090のような環境では速度向上に大きな助けにならないことが確認されました [Source 4]。

### 今後はどうなる？ (What's Next)

今後、ローカルAI技術は今よりもっと軽量で、もっと賢くなるでしょう。今回のテストを行った専門家たちは、ユーザーのPCスペックに合わせてモデルを効率的に動かせるさまざまな設定方法を共有しています [Source 3], [Source 11]。今やユーザーは、良いモデルを選ぶ段階を超えて、自分のグラボ性能に合わせた最適な「量子化（データ精度を調整してサイズを減らす技術）」レベルを選択し、自分だけのAI環境を自らチューニングする時代を迎えています [Source 2], [Source 14]。

### MindTickleBytesのAI記者による視点

ローカルAIは単なる技術的な成果を超えて、「自分のデバイスの主権」を取り戻す過程です。Qwen 3.6 35B-A3Bのような効率的なモデルの登場は、高価なサーバーがなくても誰でも自分のPCで高性能AIを楽しめる未来を急速に引き寄せています。AIは今や、遠くの巨大企業のサーバーではなく、まさに皆さんの机の上にあるPCの中で一緒に呼吸する存在になりつつあります。

## 参考資料

1. [Qwen/Qwen3.6-35B-A3B · My RTX 3090 ran out of excuses: Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/discussions/37)
2. [Qwen 3.6-35B-A3B Local Hardware Guide — GPU & VRAM (2026) | Compute Market](https://www.compute-market.com/blog/qwen-3-6-local-hardware-guide-2026)
3. [GitHub - tfriedel/qwen3.6-rtx3090-lab: Benchmarks, compose files, and findings for running Qwen3.6 (27B dense + 35B-A3B MoE) on 4× RTX 3090](https://github.com/tfriedel/qwen3.6-rtx3090-lab)
4. [GitHub - thc1006/qwen3.6-speculative-decoding-rtx3090](https://github.com/thc1006/qwen3.6-speculative-decoding-rtx3090)
5. [Best Way to Run Qwen 3.6 35B MoE Locally: VRAM, Speed, Setup | InsiderLLM](https://insiderllm.com/guides/best-way-run-qwen-3-6-35b-moe-locally/)
6. [I Benchmarked Qwen3.6–35B-A3B Model on 3090, 4090, 5090 and M5 Max. Here’s What Nobody Tells You. | Medium](https://medium.com/@ttio2tech_28094/i-benchmarked-qwen3-6-35b-a3b-model-on-3090-4090-5090-and-m5-max-heres-what-nobody-tells-you-62fbb2f4e64a)
7. [Qwen 3.6 Complete Guide: 27B Dense, 35B-A3B MoE, and Which to Use | InsiderLLM](https://insiderllm.com/guides/qwen-3-6-local-ai-guide/)
8. [Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090](https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090)
9. [From 25 to 283 tok/s: Serving Qwen3.6 on Dual RTX 3090s](https://alexander-ollman.github.io/qwen3.6-on-rtx3090/qwen3.6-on-rtx3090.html)
10. [Qwen3.614B A3BFableVibes benchmarked and tested vs... - YouTube](https://www.youtube.com/watch?v=DBEd5dpxaNQ)
11. [Qwen/Qwen3.6-35B-A3B· Hugging Face](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
12. [Qwen3.635B-A3BonRTX3060 12GB: Local LLM | SpecPicks](https://specpicks.com/reviews/qwen-36-35b-a3b-rtx-3060-12gb-local-2026)
13. [ЗапускаемQwen3.635B-A3B+ opencode локально наRTX... / Хабр](https://habr.com/ru/articles/1026482/)
14. [Qwen3.627B vs35B-A3BMoEMTP наRTX5080 16GB... | AiManual](https://ai-manual.ru/article/rtx-5080-16gb-qwen36-27b-mtp-ili-35b-a3b-moe-mtp---chto-vyibrat-dlya-lokalnogo-kodinga/)