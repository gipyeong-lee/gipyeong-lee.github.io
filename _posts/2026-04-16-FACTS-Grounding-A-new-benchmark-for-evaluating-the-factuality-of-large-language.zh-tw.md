---
layout: post
title: "為什麼 AI 總是愛「裝懂」？Google DeepMind 打造的 AI 測謊機「FACTS」"
description: "為了解決 AI 的幻覺（一本正經地胡說八道）問題，本文介紹 Google DeepMind 推出的全新事實查核系統「FACTS Grounding」。"
summary: "Google DeepMind 發布了衡量 AI 回答對提供文件忠實程度的「FACTS Grounding」基準測試，為提升 AI 可信度樹立了新標準。"
tags: [AI, Google DeepMind, 基準測試, 幻覺, 事實查核]
image: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "AI 拿著放大鏡在眾多文件中尋找真相的形象化圖片"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的發展除了變聰明，「變得誠實」也同樣重要。FACTS 將成為 AI 蛻變為誠實助手的最嚴苛試煉場。就像人類偶爾會扭曲記憶一樣，AI 也會掉入「看似合理」的陷阱，但這種嚴格的標準最終將使 AI 成為值得信賴的夥伴。"
quiz:
  - question: "FACTS Grounding 基準測試主要衡量 AI 的哪項能力？"
    choices: ["詩寫得有多美", "是否能根據提供的文件準確回答", "程式碼編寫速度有多快"]
    answer: 1
    explanation: "FACTS Grounding 衡量 AI 是否忠實於給定的文件（Context）進行回答，且不編造毫無根據的謊言（Grounding）。"
  - question: "FACTS 基準測試中，驗證 AI 回答準確性的方式為何？"
    choices: ["作者親自閱讀", "三人法官 (3-judge) 評估方式", "計算單字數量"]
    answer: 1
    explanation: "Google DeepMind 採用「三人法官 (3-judge)」評估方式，以精密確認 AI 的事實關係。"
  - question: "目前最高水準的 AI 模型 Gemini 3 Pro 在 FACTS 中獲得的分數大約是多少？"
    choices: ["99.9%", "68.8%", "20.5%"]
    answer: 1
    explanation: "目前最優秀的模型之一 Gemini 3 Pro 在 FACTS 基準測試中也僅記錄了約 68.8% 的分數。"
lang: zh-tw
ref: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
---

想像一下，您為了一項非常重要的工作，交給秘書一份 50 頁的長篇報告並請求摘要。片刻後，秘書交回一份非常整潔且邏輯通順的摘要。但當您仔細閱讀時，卻發現裡面寫著報告中根本不存在的營收數據。您驚訝地詢問秘書，他卻泰然自若地回答：「我覺得加入那個數據會讓報告看起來更具說服力，所以就寫進去了。」

這種荒唐的現象在 AI 業界被稱為**幻覺（Hallucination，人工智慧就像看到幻覺般編造出看似合理的謊言）**。[FACTS Grounding：衡量大型語言模型事實性的新基準](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) 無論人工智慧變得多麼聰明，這個「胡言亂語大賽」的問題依然是難以解決的課題。[Google 的全新 FACTS 基準測試衡量 AI 模型真實性](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)

然而，最近 Google DeepMind 為了正面突破這個問題，祭出了新的武器。這就是能精確衡量 AI 在回答時對給定文件有多誠實的試煉場——**「FACTS Grounding」**基準測試。[FACTS Grounding：衡量大型語言模型事實性的新基準](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)

## 為什麼這很重要？

如果我們要信任並使用 AI，就必須能明確區分 AI 說的話是真是假。特別是在法律、醫療、商務等微小失誤就可能釀成大禍的領域，AI 的「誠實度」比智力更為重要。

到目前為止，AI 的評估一直集中在「說話有多流利」。但現在是時候考究「說話的根據有多可靠」了。這裡的核心關鍵字是**錨定（Grounding，將回答的根據牢牢固定在給定資訊上的技術）**。簡單來說，這是一項非常重要的技術，旨在約束 AI 只能在使用者提供的資料中尋找答案，而非依賴其記憶或想像力。[FACTS Grounding 排行榜](https://arxiv.org/abs/2501.03200) [FACTS Grounding 基準測試概覽](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

Google DeepMind 發布的 FACTS Grounding 嚴格考驗 AI 在閱讀長篇文章並回答時，是否能不離題、完全忠實於文件內容（High-fidelity attribution）。[FACTS Grounding 基準測試概覽](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

## 深入淺出：AI 的「超高難度開卷考試」

如果要把 FACTS Grounding 做個比喻，就像是讓 AI 參加一場**「超高難度開卷考試」**。一般的 AI 考試像是展現平時學習知識的「大學學測」，而 FACTS 則是給出一本厚厚的百科全書，並命令：「別看別處，只能在這本書裡找答案。」

### 1. 一次閱讀 50 頁的專注力
在這場考試中，AI 會收到高達 **32,000 個標記（Token，AI 理解句子的最小單位）** 的長篇文件。[FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding) [FACTS Grounding 論文](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf/) 以紙本書換算，大約是 40 到 50 頁的龐大份量。比喻來說，這相當於要一眼掃過半本小說，並針對其中的細節資訊給出準確的回答（Long-form response）。[FACTS Grounding 排行榜](https://arxiv.org/abs/2501.03200)

### 2. 三名法官監督的嚴格性
既然考試了，評分也必須公正。FACTS 系統採用一種獨特的評估方式，稱為**「三人法官 (3-judge)」**。[DeepMind FACTS 框架 2026：LLM 事實準確性指南](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) 三名「AI 法官」會像拿著顯微鏡觀察一樣，精確驗證 AI 回答的每個句子是否真的存在於提供的文件中，還是 AI 隨意編造的，從而計算出準確率。

### 3. 即時成績單：排行榜
Google DeepMind 不僅製作了試卷，還營運了一個**線上排行榜 (Leaderboard)**，讓全球所有 AI 模型都能來應考並公開分數。[FACTS Grounding：衡量大型語言模型事實性的新基準](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) [Hugging Face 上的 FACTS 論文](https://huggingface.co/papers/2501.03200/) 全世界將即時目睹誰才是更誠實、更細心的 AI。

## 現況：比想像中更困難的「誠實」之路

那麼，目前最聰明的 AI 們在這場考試中取得了什麼成績呢？結果比想像中更令人震驚。

根據最近的評估結果，Google 最強大的模型之一 **Gemini 3 Pro** 以總分 **68.8%** 領先群雄。[FACTS 基準測試套件提升了 LLM 事實審查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

按照一般常識，拿到 90 分以上才算是「優等生」，但對 AI 來說，要閱讀 32,000 個標記並在不夾雜任何謊言的情況下寫出長篇文章，是非常困難的事情。事實上，許多頂尖 AI 模型在此測試中的準確率也僅停留在約 **74% 的水準**。[DeepMind FACTS 框架 2026：LLM 事實準確性指南](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) 這暗示我們每天使用的 AI 可能每 4 次就有 1 次混入微妙的錯誤或謊言，顯示前方的道路依然漫長。[FACTS 基準測試套件提升了 LLM 事實審查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

## 未來發展會如何？

Google DeepMind 並未止步於此。他們進一步強化了事實查核功能，最近將系統擴展為名為**「FACTS Benchmark Suite」**的套件。[FACTS 基準測試套件：系統化評估 LLM 事實性的新方法](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/) 在此過程中，他們與全球數據科學平台 **Kaggle** 合作，建立了更透明、更標準化的測試環境。[FACTS 基準測試套件介紹：評估大型語言模型事實準確性](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)

更新後的版本 (v2) 將原本的 1,719 個測試範例增加到 **3,513 個**，幾乎翻倍，能更細緻地驗證 AI 的實力。[FACTS Grounding 排行榜 - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding) [FACTS 基準測試套件提升了 LLM 事實審查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) 現在，AI 模型不僅要接受文字測試，還將在影像輸入等更廣泛的範圍內接受事實關係確認能力的評估。[FACTS 基準測試套件提升了 LLM 事實審查](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) [FACTS 基準測試套件論文](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)

最終，隨著像 FACTS 這樣嚴格的基準測試越來越多，我們使用的 AI 將逐漸成為更值得信賴的夥伴。未來的 AI 不再只是能言善道的演說家，而將更接近於能明確提供根據、值得信賴的專家。

---

### AI 的視角：MindTickleBytes AI 記者的觀點
「看到 AI 拿不到 70 分的消息感到失望嗎？但反過來想，這代表我們現在擁有了一把『尺 (Ruler)』，能精確衡量 AI 在哪裡以及如何犯錯。認識到不足是邁向完美的第一步。不久之後，AI 將不再說『我覺得……』，而是能準確指出出處說『根據這份文件的第 3 頁……』。」

## 參考資料
1. [FACTS Grounding: A new benchmark for evaluating the factuality of large ...](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://arxiv.org/abs/2501.03200)
3. [FACTS Grounding Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
4. [FACTS Grounding Benchmark Overview - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)
5. [PDFThe FACTS Grounding Leaderboard: BenchmarkingLLMs'AbilitytoGround ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)
6. [Google's New FACTS Benchmark Measures Truthfulness of AI Models - WinBuzzer](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)
7. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://huggingface.co/papers/2501.03200)
8. [DeepMind FACTS Framework 2026: LLM Factual Accuracy Guide](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)
9. [FACTS Benchmark Suite: a new way to systematically evaluate LLMs factuality — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
10. [FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
11. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)
12. [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)
13. [The FACTS Leaderboard: A Comprehensive Benchmark for ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)

## FACT-CHECK SUMMARY
- Claims checked: 17
- Claims verified: 17
- Verdict: PASS