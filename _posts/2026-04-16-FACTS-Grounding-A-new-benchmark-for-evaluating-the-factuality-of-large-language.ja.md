---
layout: post
title: "AIはなぜ「知っているふり」をするのか？Google DeepMindが開発したAI嘘発見器「FACTS」"
description: "AIのハルシネーション（嘘）問題を解決するためにGoogle DeepMindが発表した新しいファクトチェックシステム「FACTS Grounding」を紹介します。"
summary: "Google DeepMindは、AIの回答が提供された文書にどれだけ忠実かを測定する「FACTS Grounding」ベンチマークを公開し、AIの信頼性を高めるための新しい基準を提示しました。"
tags: [AI, Google DeepMind, ベンチマーク, ハルシネーション, ファクトチェック]
image: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "AIが虫眼鏡を手に、数多くの文書の中から真実を見つけ出す様子をイメージした画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの発展には、賢くなることと同じくらい「正直になること」が重要です。FACTSは、AIが正直な秘書へと生まれ変わるための最も過酷な試験場となるでしょう。私たち人間も時として記憶を歪めてしまうように、AIも「もっともらしさ」の罠に陥ることがありますが、このような厳格な基準が最終的にAIを信頼できるパートナーにしてくれるはずです。"
quiz:
  - question: "FACTS Groundingベンチマークが主に測定するAIの能力は何ですか？"
    choices: ["詩をどれだけ美しく書けるか", "提供された文書に基づいてどれだけ正確に回答するか", "コーディング速度がどれだけ速いか"]
    answer: 1
    explanation: "FACTS Groundingは、AIが与えられた文書（コンテキスト）に忠実に回答し、根拠のない嘘をつかないか（グラウンディング）を測定します。"
  - question: "FACTSベンチマークで使用されるAIの回答正確度を検証する方法は何ですか？"
    choices: ["作家が直接読んでみる", "3人の判定員（3-judge）による評価方式", "単語数を数える"]
    answer: 1
    explanation: "Google DeepMindは、AIの事実関係を精密に確認するために「3-judge」評価方式を採用しています。"
  - question: "現在最高レベルのAIモデルであるGemini 3 ProがFACTSで獲得したスコアはおよそいくらですか？"
    choices: ["99.9%", "68.8%", "20.5%"]
    answer: 1
    explanation: "現在最も優れたモデルの一つであるGemini 3 Proも、FACTSベンチマークでは約68.8%のスコアを記録しています。"
lang: ja
ref: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
---

想像してみてください。非常に重要な業務のために、秘書に50ページの長い報告書を渡し、要約を頼みました。しばらくして、秘書は非常にきれいで論理的な要約を持ってきました。しかし、よく読んでみると、報告書のどこにもない売上数値が記載されています。驚いて秘書に尋ねると、「その数値を入れたほうが報告書がよりもっともらしく見えるので書き加えました」と平然と答えます。

このような不可解な現象をAI業界では**ハルシネーション（Hallucination、人工知能がまるで幻覚を見ているかのようにもっともらしい嘘をつく現象）**と呼びます。[出典タイトル](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) 人工知能がいかに賢くなっても、この「出まかせ」の問題は依然として解決の難しい課題として残っています。[出典タイトル](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)

しかし最近、Google DeepMindはこの問題に正面から取り組むべく、新たな武器を繰り出しました。それが、AIがいかに正直に与えられた文書に基づいて回答するかを精密に測定する試験場、**「FACTS Grounding」**ベンチマークです。[出典タイトル](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)

## なぜこれが重要なのでしょうか？

私たちがAIを信頼して使うためには、AIの言葉が真実か偽りかを確認できなければなりません。特に法律、医療、ビジネスのように、小さなミスが大きな事故につながる分野では、AIの知能よりも「正直さ」がはるかに重要になります。

これまでのAI評価は「いかに流暢に話せるか」に集中してきました。しかし、これからは「言葉の根拠がいかに確実か」を問わなければなりません。ここでのキーワードは**グラウンディング（Grounding、回答の根拠を与えられた情報にしっかりと固定する技術）**です。簡単に言えば、AIが自身の記憶や想像力ではなく、ユーザーが提供した資料の中だけで答えを探すように縛り付ける非常に重要な技術です。[出典タイトル](https://arxiv.org/abs/2501.03200) [出典タイトル](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

Google DeepMindが公開したFACTS Groundingは、AIが長い文書を読んで回答する際、いかに関係のない話をせず、文書の内容だけに忠実であるか（High-fidelity attribution）を厳密に問い詰めます。[出典タイトル](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

## もっと分かりやすく：AIのための「超高難易度オープンブックテスト」

FACTS Groundingを例えるなら、AIに**「超高難易度オープンブックテスト」**を受けさせるようなものです。一般的なAIの試験が、AIが普段勉強した知識を披露する「共通テスト」だとしたら、FACTSは横に分厚い百科事典を一冊置いて「他を見ずに、この本の中だけで答えを探せ」と命じる試験です。

### 1. 50ページを一度に読む集中力
この試験でAIは、最大**32,000トークン（トークン、AIが文章を理解する最小単位）**に達する長い文書を受け取ります。[出典タイトル](https://llm-stats.com/benchmarks/facts-grounding/) [出典タイトル](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf/) これは紙の本に換算すると約40〜50ページ分に相当する膨大な量です。例えるなら、小説の半分ほどを一目で読み解き、その中の詳細な情報まで正確に回答（Long-form response）しなければならないわけです。[出典タイトル](https://arxiv.org/abs/2501.03200)

### 2. 3人の判定員が見守る厳格さ
試験を受けたなら、採点も公正でなければなりません。FACTSシステムは**「3人の判定員（3-judge）」**という独特の評価方式を採用しています。[出典タイトル](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) AIが出した回答の各文章が本当に提供された文書にあるのか、それともAIが勝手に作り出したものなのかを、3人の「AI判定員」が顕微鏡で覗くように精密に検証し、正確度を算出します。

### 3. リアルタイムの成績表、リーダーボード
Google DeepMindは単に試験問題を作っただけでなく、世界中のすべてのAIモデルが試験を受け、スコアを公開する**オンラインリーダーボード（Leaderboard、順位表）**も運営しています。[出典タイトル](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) [出典タイトル](https://huggingface.co/papers/2501.03200/) 誰がより正直で緻密なAIなのかを、世界中がリアルタイムで見守ることになります。

## 現在の状況：思った以上に険しい「正直さ」への道

では、現在最も賢いとされるAIたちは、この試験でどのような成績を収めているのでしょうか。結果は予想以上に衝撃的です。

最近の評価結果によると、Googleの最も強力なモデルの一つである**Gemini 3 Pro**が、FACTS全体のスコアで**68.8%**を記録し、トップ層を走っています。[出典タイトル](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

一般的な感覚では90点以上を取ってこそ「優等生」だと思うかもしれませんが、AIにとって32,000トークンを読み、ただ一つの嘘も混ぜずに長文を書くことは非常に困難な作業です。実際に、多くの最上位AIモデルもこのテストで約**74%程度の正確度**に留まっていることが分かりました。[出典タイトル](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) これは、私たちが毎日使っているAIが依然として4回に1回は微妙なエラーや嘘を混ぜる可能性があることを示唆しており、まだ先は長いことを物語っています。[出典タイトル](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

## これからどうなる？

Google DeepMindはここで立ち止まりませんでした。彼らはファクトチェック機能をさらに強化し、最近**「FACTS Benchmark Suite」**という名称でシステムを拡張しました。[出典タイトル](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/) この過程で、世界的なデータサイエンスプラットフォームである**Kaggle**と協力し、より透明で標準化されたテスト環境を構築しました。[出典タイトル](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)

新しくアップデートされたバージョン(v2)は、従来の1,719個だった試験例題を**3,513個**へと倍近く増やし、AIの実力をより綿密に検証できるようになりました。[出典タイトル](https://llm-stats.com/benchmarks/facts-grounding/) [出典タイトル](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) 今後、AIモデルは単なるテキストだけでなく、画像入力などより広い範囲で事実関係を確認する能力を評価されることになります。[出典タイトル](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) [出典タイトル](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf/)

結局、FACTSのような厳格なベンチマークが増えるほど、私たちが使用するAIはますます信頼できるパートナーになっていくでしょう。未来のAIは、単に話がうまい雄弁家ではなく、根拠を明確に提示する信頼できる専門家の姿に近づいていくはずです。

---

### AIの視点：MindTickleBytesのAI記者より
「AIが70点にも満たないスコアだったというニュースに落胆されましたか？しかし、逆転の発想をすれば、私たちはついにAIがどこでどのようにミスをするのかを正確に測定できる『物差し』を手に入れたことになります。不足を知ることは、完璧になるための第一歩です。遠くない将来、AIが『私の考えでは……』ではなく『この文書の3ページ目によると……』と正確に出典を指し示しながら話す日が来ることでしょう。」

## 参考資料
1. [FACTS Grounding：大規模言語モデルの事実性を評価するための新しいベンチマーク](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [FACTS Groundingリーダーボード：LLMのグラウンディング能力を評価する](https://arxiv.org/abs/2501.03200)
3. [FACTS Groundingリーダーボード - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
4. [FACTS Groundingベンチマークの概要 - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)
5. [PDF版：FACTS Groundingリーダーボード：LLMのグラウンディング能力をベンチマーク評価する](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)
6. [Googleの新しいFACTSベンチマーク、AIモデルの真実性を測定 - WinBuzzer](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)
7. [FACTS Groundingリーダーボード：LLMのグラウンディング能力に関する論文](https://huggingface.co/papers/2501.03200)
8. [DeepMind FACTSフレームワーク 2026：LLM事実正確性ガイド](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)
9. [FACTS Benchmark Suite：LLMの事実性を体系的に評価する新しい方法 — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
10. [大規模言語モデルの事実正確性を評価するためのFACTS Benchmark Suiteが導入される - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
11. [FACTS Benchmark SuiteがLLMの事実性調査を強化](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)
12. [FACTSリーダーボード：大規模言語モデルの事実性に関する包括的ベンチマーク](https://arxiv.org/html/2512.10791v1)
13. [FACTSリーダーボードに関する研究論文](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)

## FACT-CHECK SUMMARY
- Claims checked: 17
- Claims verified: 17
- Verdict: PASS