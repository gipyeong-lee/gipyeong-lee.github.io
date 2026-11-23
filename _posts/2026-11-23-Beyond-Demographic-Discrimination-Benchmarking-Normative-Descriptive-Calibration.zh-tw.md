---
layout: post
title: "當我們問 AI「實際上會發生什麼」與「本應當如何」時，會發生什麼事？"
description: "深入淺出地介紹 NDCB 這一項全新的評估基準，其用以衡量大型語言模型（LLM）在社會決策中如何區分「事實預測（Descriptive）」與「當規判斷（Normative）。"
summary: "透過評估 AI 如何區分現實可能性預測與道德社會決策的 NDCB 基準研究，我們來看看 Claude 與 GPT 等主要模型之間的差異。"
tags: [AI, LLM, NDCB, 倫理, 基準, 人工智慧]
image: 2026-11-23-Beyond-Demographic-Discrimination-Benchmarking-Normative-Descriptive-Calibration.jpg
image_alt: "分析各種人工智慧模型在事實預測與道德判斷之間表現出的反應差異的概念性視覺圖表"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "當 AI 協助人類做出社會決策時，明確區分「實際上會如何」的預測與「應該如何」的當規判斷，是公平性與信賴度的核心。這項研究為 AI 評估開闢了新境界。"
quiz:
  - question: "研究人員為了評估大型語言模型對事實預測與道德判斷的區分能力而引入的新基準名稱是什麼？"
    choices: ["BBQ 基準", "NDCB (Normative-Descriptive Calibration Benchmark)", "BOLD 基準"]
    answer: 1
    explanation: "研究人員引入了包含 697 個情境的 NDCB 基準，以衡量規範-描述性校準（Normative-Descriptive Calibration） [Source 1]。"
  - question: "哪一個模型最強烈地將事實預測（Descriptive）與當規判斷（Normative）的框架進行分離？"
    choices: ["GPT-5.5", "Claude Sonnet 4.6 及 Claude Opus 4.6", "LlaMa 系列"]
    answer: 1
    explanation: "Claude Sonnet 4.6 與 Claude Opus 4.6 的平均 NDS 值分別為 +0.55 與 +0.52，最強烈地分離了這兩個框架 [Source 1]。"
  - question: "關於 NDCB 基準所涵蓋的情境與領域規模，下列何者正確？"
    choices: ["橫跨 6 個領域的 697 個配對（matched-pair）情境", "橫跨 2 個領域的 100 個情境", "橫跨 10 個領域的 5,000 個情境"]
    answer: 0
    explanation: "NDCB 透過橫跨 6 個領域總計 697 個配對（matched-pair）情境來進行評估 [Source 1]。"
lang: zh-tw
ref: 2026-11-23-Beyond-Demographic-Discrimination-Benchmarking-Normative-Descriptive-Calibration
---

想像一下。有一天，你向擔任人資主管或法官角色的人工智慧（AI）提出兩個問題。第一個問題是：「在這些求職者中，統計上實際上錄取機率最高的人是誰？」第二個問題是：「依據這個社會標準，誰才是理應被錄取的人？」身為人類，我們直覺上就知道這兩個問題的性質完全不同。前者是在預測冰冷現實中的機率，而後者則是包含了正義或公平價值的當規判斷。

那麼，我們每天使用的大型語言模型（LLM，Large Language Models）究竟能否不同地理解這兩個問題呢？最新研究顯示，AI 即使在相同的情況下，也會根據問題的包裝方式給出完全不同的答案，且各個模型在處理這兩種性質的方式上存在著巨大的差異 [Source 1, Source 16]。在我們將 AI 從單純工具迎向社會夥伴的今天，精確理解這種差異已成為一項極為重要的課題。

---

## 為什麼這很重要？

大型語言模型現在不僅僅是會讀寫的聊天夥伴，更深入參與了招募、貸款審查、法律審查以及公共政策提案等人類社會的重大決策 [Source 1, Source 16]。

如果 AI 在應該預測「未來會發生什麼事（描述性推理，Descriptive Reasoning）」的場合中，摻雜了「應該發生什麼事（規範性推理，Normative Reasoning）」的自身價值觀或偏見，會發生什麼事呢？相反地，當需要做出公正的道德決策時，如果它僅僅依賴過去不平等的統計數據，回答「反正這機率很高，就這樣決定吧」，則可能導致嚴重的歧視與社會錯誤。

像這樣去衡量 AI 能多麼明確地區分並調整現實的數據預測與道德社會當規判斷（這被稱為**規範-描述性校準（Normative-Descriptive Calibration）**），是 AI 要安全融入人類社會必須解決的核心課題 [Source 1, Source 16]。

---

## 輕鬆理解：氣象預報員與法官的差異

我們用日常的比喻來輕鬆理解這個複雜的概念。

- **描述性推理（Descriptive Reasoning）扮演的是「氣象預報員」的角色。** 當氣象預報員說今天降雨機率是 80% 時，那並不是因為希望下雨，而是根據科學統計與雲層移動，客觀地預測「實際上會發生的事」。
- **規範性推理（Normative Reasoning）扮演的是「法官」或「政策決策者」的角色。** 法官不只是猜測犯罪發生的機率，而是做出當規的決定：「對照我們社會追求的價值觀來看，這項判決是否正義？應該如何判決才妥當？」

簡單來說，這就像是向 AI 提問時，只要稍微改動幾個字（例如「看起來像是」vs「應該要」），就能確認 AI 內部是否會切換到完全不同的面具來運作。以往的 AI 公平性評估，僅僅是檢視 AI 是否對特定群體展現偏見，卻未能深入探討當 AI 在「預測」與「決策」這兩種不同目標之間切換時，是否能正確意識到其中的差異 [Source 1, Source 16]。

---

## 現狀：NDCB 基準與各模型的成績單

為了系統性地掌握這個問題，研究人員開發了一項名為 **NDCB（Normative-Descriptive Calibration Benchmark）** 的全新評估框架 [Source 1]。NDCB 涵蓋了橫跨 6 個領域共 697 個精密的配對情境（matched-pair scenarios），並將相同的情境以「預測（prediction）」框架與「決策（decision）」框架兩種方式向模型提問 [Source 1]。

為了分析模型的反應，研究人員引入了三個指標：規範參與率（NER, Normative Engagement Rate）、規範洩漏率（NLR, Normative Leakage Rate），以及規範-描述分離度（NDS, Normative-Descriptive Separation） [Source 1]。這些指標細緻地測量了 AI 是否在預測情境中未混入不必要的道德判斷，以及在決策情境中是否沒有過度偏向冷酷的統計數據。

針對 6 個主要大型語言模型進行的測試結果，清楚展現出各個模型在推理方式上的巨大差異：
- **Claude 系列的高分離度**：Anthropic 的 **Claude Sonnet 4.6** 與 **Claude Opus 4.6** 的平均 NDS 分數分別創下 **+0.55** 與 **+0.52** 的佳績，最清晰且穩定地區分了事實預測與當規判斷的框架 [Source 1]。
- **GPT-5.5 的獨特面貌**：相對地，OpenAI 的 **GPT-5.5** 在給予單選（single-pick）指令時，平均 NDS 呈現 **-0.14** 的負值，而在沒有該指令時也記錄了接近 0 的 **+0.02**，展現出與 Claude 截然不同的樣貌 [Source 1]。
- **基準的出色鑑別力**：在全部 6 個模型中，NDS 指標成功區分了 15 個模型對中的 13 個；相比之下，傳統的 BBQ 準確度指標僅區分出 7 個，BOLD 則為 0 個，證明了 NDCB 在揭示模型微小推理差異方面是更為強大的工具 [Source 1]。

此外，研究人員發現，即使在提示詞中移除幾個單一觸發詞，模型平均 NDS 的正負號雖然不會改變，但其數值最高可能會波動達 0.46，甚至導致模型之間的排名重新排列 [Source 1]。這項重要發現顯示出提示詞的寫法對於 AI 倫理與邏輯框架分離的敏感程度有多高。

---

## 未來走向如何？

這項研究預示了未來設計與評估 AI 標準的巨大變革。今後，企業將會嚴格驗證 AI 是否不僅具備優秀的對話能力與龐大的知識記憶，更能清楚認知到「我現在是在預測事實，還是正在做出社會重大決策」，並據此選擇合適的推理方式 [Source 1, Source 16]。

這意味著，當我們在日常生活中將工作交給 AI 或尋求重要決策建議時，讓 AI 不混淆冷酷統計機率與溫暖規範價值判斷的技術基礎，正穩固地建立起來。

---

## AI 的視角

當 AI 協助人類做出社會決策時，明確區分「實際上會如何」的預測與「應該如何」的當規判斷，是公平性與信賴度的核心。這項研究為 AI 評估開闢了新境界，並將成為未來 AI 作為人類社會夥伴做出正確判斷的重要里程碑。

---

## 參考資料

1. [Beyond Demographic Discrimination: Benchmarking Normative-Descriptive Calibration in LLMs](https://arxiv.org/abs/2611.26870)
2. [2026inLLMs— Simon Willison - YouTube](https://www.youtube.com/watch?v=9RKrSF9d2SE)
3. [CalibratingLLMs](https://learnprompting.org/docs/reliability/calibration)
4. [Emergent introspective awarenessinLLMs\ Anthropic](https://www.anthropic.com/research/introspection)
5. [GitHub - Mooler0410/LLMsPracticalGuide: A curated list of practical...](https://github.com/Mooler0410/LLMsPracticalGuide)
6. [TheCalibrationGeneralization Gap - Apple Machine Learning Research](https://machinelearning.apple.com/research/calibration-generalization-gap)
7. [BenchmarkingGPT-6 Astra | Artificial Analysis](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)
8. [On theCalibrationof Multilingual Question AnsweringLLMs](https://arxiv.org/abs/2311.08669)
9. [What areLLMs? How large language models actually work](https://www.together.ai/blog/what-are-llms)
10. [Chatbot Arena:BenchmarkingLLMsin the Wild with... - LMSYS Org](https://www.lmsys.org/blog/2023-05-03-arena/)
11. [llms.txt — что это и нужен ли он сайту · Агентная оптимизация](https://agentoptimization.ru/llms-txt/)
12. [llms.txt Validator by Hostinger](https://llmstxtvalidator.org/)
13. [Beyond Demographic Discrimination: Benchmarking Normative ...](https://openreview.net/forum?id=WEhvEd8nhz)
14. [Beyond Marginal Distributions: A Framework to ...Beyond Demographics: Fine-tuning Large Language Models to ...Evaluating LLMs for Detecting Demographic-Targeted Social ...Evaluating LLMs for Detecting Demographic-Targeted Social Bias ...](https://arxiv.org/abs/2601.15755)
15. [Beyond Demographics: Fine-tuning Large Language Models to ...](https://aclanthology.org/2025.acl-long.104/)
16. [Evaluating LLMs for Detecting Demographic-Targeted Social ...](https://aclanthology.org/2026.iaai-1.5.pdf)
17. [Evaluating LLMs for Detecting Demographic-Targeted Social Bias ...](https://arxiv.org/html/2510.04641v1)