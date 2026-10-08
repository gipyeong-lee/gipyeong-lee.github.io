---
layout: post
title: "AI 竟能一次讀完數千本書？突破 100 萬 Token 限制的『Step5Preview』登場"
description: "我們將深入淺出地介紹突破記憶極限的新型 AI 模型 Step5Preview 的特性，以及 100 萬 Token 上下文視窗所代表的深層意義。"
summary: "由 StepFun 推出的 6000 億參數規模 MoE 模型 Step5Preview，能處理高達 100 萬 Token 的海量上下文，並展現出專為 Agent 任務設計的強大能力。"
tags: [AI, StepFun, Step5Preview, 大語言模型, 技術趨勢]
image: 2026-10-09-Step-5-Preview-a-1M-context-MoE-from-StepFun-shows-up-on-OpenRouter.jpg
image_alt: "可視化 AI 處理巨量數據海洋的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "一次記憶海量數據的能力，將成為 AI 從單純聊天機器人進化為實質工作助理的關鍵鑰匙。"
quiz:
  - question: "Step5Preview 最顯著的特徵之一是什麼？"
    choices: ["100 萬 Token 的上下文視窗", "僅能處理文字", "以免費開源形式公開的模型"]
    answer: 0
    explanation: "Step5Preview 是一個能夠一次輸入並處理高達 100 萬 Token 海量資訊的模型。"
  - question: "什麼是 MoE (Mixture-of-Experts) 架構？"
    choices: ["永遠使用所有參數的結構", "僅激活所需專家參數的結構", "與人類大腦結構完全無關的技術"]
    answer: 1
    explanation: "MoE 是一種僅根據特定狀況選擇性地使用專家參數，藉此提升效率的技術。"
  - question: "Step5Preview 的開放權重 (Open Weights) 預計發布日期為何？"
    choices: ["已公開", "2026 年 10 月 15 日", "2026 年 12 月 31 日"]
    answer: 1
    explanation: "StepFun 預計於 2026 年 10 月 15 日公開該模型的權重。"
lang: zh-tw
ref: 2026-10-09-Step-5-Preview-a-1M-context-MoE-from-StepFun-shows-up-on-OpenRouter
---

想像一下，您的辦公桌上堆疊了 50 本超過 1,000 頁的厚重會計報告。如果您問 AI 助理：「請找出過去 5 年公司財務流向中所有的異常徵兆並進行總結」，結果會如何呢？以前的 AI 必須將這些文件分批輸入，且往往在過程中遺忘之前的內容。然而，最近在 OpenRouter 上登場的「Step5Preview」，就是一位打破這種不可能的全新挑戰者。

### 為什麼這項技術很重要？

在日常生活中使用 AI 時，常會遇到令人沮喪的時刻。例如 AI 很快就忘記剛才說過的話，或是給予長篇文件時無法進行適當分析。專家們稱之為 AI 的「記憶力」，也就是「上下文視窗（Context Window，指 AI 能一次處理的數據量）」的極限。

Step5Preview 具備了 100 萬 Token 的壓倒性記憶力（[參考資料 1](https://openrouter.ai/stepfun/step-5-preview)）。這不僅僅是增加了字數上限。藉由一次記憶海量資訊，它能全面理解複雜的程式編碼，並從數百頁的金融文件中洞察先機，這意味著它作為「真正會工作的 AI（Agentic AI）」能力已獲得飛躍性的提升（[參考資料 3](https://platform.stepfun.ai/docs/en/guides/models/step-5-preview), [參考資料 9](https://www.stepfun.com/step-5-preview)）。

### 簡單來說：「專家委員會」模式

Step5Preview 使用了一種名為「混合專家模型（MoE, Mixture-of-Experts）」的聰明方式（[參考資料 1](https://openrouter.ai/stepfun/step-5-preview)）。

做個比喻，想像學校裡不僅僅只有一位必須通曉所有科目的天才學生，而是有數學專家、英文專家、科學專家等無數老師在旁待命。當問題提出時，並非所有老師一起蜂擁而上，而是只有數學問題時，數學老師才會被激活並回答。

Step5Preview 雖然總共有 6000 億個龐大的參數（AI 的知識單位），但每次提問時，實際上僅會選擇性地使用其中 270 億個參數（[參考資料 5](https://therouter.ai/blog/step-5-preview-stepfun-api-integration-routing-guide/), [參考資料 9](https://www.stepfun.com/step-5-preview)）。因此，它既能保有整個模型龐大的知識庫，同時又能在速度與效率上取得平衡（[參考資料 11](https://braindetox.kr/en/posts/stepfun_step5_preview_agent_model_2026.html)）。

### 觸手可及的 AI

目前 Step5Preview 可透過 API 直接使用，且具備了不僅分析文字，還能分析包含影片在內的影像數據能力（[參考資料 5](https://therouter.ai/blog/step-5-integration-routing-guide/), [參考資料 9](https://www.stepfun.com/step-5-preview)）。

業界的評價也非常正面。分析指出，它在特定指標上錄得了約 44 分的智商指數，被認為是目前市面上開放權重（Open Weights，模型內部資訊已公開的模型）模型中性能最頂尖的型號之一（[參考資料 14](https://pandaily.com/stepfun-step-5-preview-600b-moe-1m-context.data)）。特別是在軟體工程或金融領域等需要精確且專業的工作中，展現出不凡的強項（[參考資料 3](https://platform.stepfun.ai/docs/en/guides/models/step-5-preview)）。目前使用成本定價約為每 100 萬輸出 Token 約 2.7 美元（[參考資料 15](https://www.deai.org/news/stepfun-step-5-preview-api-open-weights-oct-15)）。

### 我們能期待什麼？

許多開發者最關注的活動日期是即將到來的 10 月 15 日。開發商 StepFun 承諾屆時將完全向大眾公開該模型的權重（weights）（[參考資料 6](https://aichoiceengine.com/ai-models/nemotron-3-ultra-vs-step-5-preview), [參考資料 9](https://www.stepfun.com/step-5-preview)）。這意味著任何人都能在自己的伺服器上直接運行這個強大的模型。當記憶力大幅增長的 AI 模型普及後，我們的日常辦公環境將會發生何種變化，將會是極具看頭的觀察重點。

---

### MindTickleBytes 的 AI 記者觀點
一次記憶海量數據的能力，將成為 AI 從單純聊天機器人進化為實質工作助理的關鍵鑰匙。雖然技術進步的速度令人驚恐，但對我們而言，最終重要的是如何將這份擴充的記憶力運用在有價值的工作上。

## 參考資料
1. [Step5Preview- API Pricing & Providers | OpenRouter](https://openrouter.ai/stepfun/step-5-preview)
2. [StepFun: Step5Preview· Models · Pi | A terminal-based coding agent](https://pi.dev/models/openrouter/stepfun-step-5-preview)
3. [Step5Preview- StepFun Documentation](https://platform.stepfun.ai/docs/en/guides/models/step-5-preview)
4. [Step5Preview API Integration Guide: StepFun's 600B Agentic...](https://therouter.ai/blog/step-5-preview-stepfun-api-integration-routing-guide/)
5. [NVIDIA Nemotron 3 Ultra vs Step5Preview | AI Choice Engine](https://aichoiceengine.com/ai-models/nemotron-3-ultra-vs-step-5-preview)
6. [Step 5 Preview: Advancing the Pareto Frontier - stepfun.com](https://www.stepfun.com/step-5-preview)
7. [StepFun shares Step 5 Preview benchmarks, demos… · AGI Hunt](https://agihunt.info/en/p/1a11ba551ea1346a45979d41047)
8. [StepFun Step 5 Preview Technical Analysis — 600B MoE ...](https://braindetox.kr/en/posts/stepfun_step5_preview_agent_model_2026.html)
9. [pandaily.com/stepfun-step-5-preview-600b-moe-1m-context.data](https://pandaily.com/stepfun-step-5-preview-600b-moe-1m-context.data)
10. [StepFun's Step5Preview API ships; open weights promised October...](https://www.deai.org/news/stepfun-step-5-preview-api-open-weights-oct-15)