---
layout: post
title: "AI 回答速度比我說話還快？談談超高速語言模型「Mercury 2.5」"
description: "深入淺出解釋 Inception Labs 發布的超高速擴散式 AI 模型「Mercury 2.5」的性能與特點。"
summary: "隨著超高速 AI「Mercury 2.5」的問世，每秒可生成 770 至 1,107 個 token，即時對話式 AI 服務的響應速度預計將有突破性的提升。"
tags: [AI, Mercury 2.5, 人工智慧, LLM]
image: 2026-10-12-Mercury-25-LLM-hits-770-tokens-per-second.jpg
image_alt: "象徵數據在數位網路中快速流動的圖形影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Mercury 2.5 不僅僅是速度快，它透過基於擴散模型的並行處理技術，展現了全新的技術突破。這意味著 AI 將正式進入全面超越人類對話速度的時代。"
quiz:
  - question: "Mercury 2.5 與現有模型相比，最顯著的特點是什麼？"
    choices: ["價格更低廉", "壓倒性的文字生成速度", "僅限離線運行"]
    answer: 1
    explanation: "Mercury 2.5 每秒可生成 770 至 1,107 個 token，創下了較現有模型快約 7 倍的速度記錄。"
  - question: "Mercury 2.5 是基於哪種技術架構？"
    choices: ["Transformer 專用模型", "基於擴散（Diffusion）的模型", "順序簡單運算模型"]
    answer: 1
    explanation: "Mercury 2.5 是由 Inception Labs 開發的基於擴散的大型語言模型（dLLM）。"
  - question: "Mercury 2.5 的上下文窗口（Context Window）範圍是多少？"
    choices: ["26 萬 token", "10 萬 token", "50 萬 token"]
    answer: 0
    explanation: "Mercury 2.5 支援 260,000 token 的大規模上下文窗口。"
lang: zh-tw
ref: 2026-10-12-Mercury-25-LLM-hits-770-tokens-per-second
---

想像一下：你正在與朋友傳訊息聊天，對方在你話還沒說完時就已經給出了答案，甚至在你傳送長篇文章後，對方在 1 秒內就完成了摘要並回傳給你。這感覺就像身邊不是一個軟體，而是一個思考速度與你完全同步的人。

最近，人工智慧（AI）領域正將這一場景變為現實。Inception Labs 發布的全新語言模型「Mercury 2.5」就是主角。這個模型不僅聰明，更以「光速」進行對答，讓我們來看看它將如何改變日常生活。[出處：Inception Labs 部落格](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)

### 為什麼這很重要？(Why It Matters)

我們平常使用的 AI 聊天機器人，在輸出回答時有時需要一點「思考時間」。你是否見過螢幕上的文字逐字「噠噠噠」地顯現出來？這是因為目前的 AI 大多是按順序生成單字的。

然而，Mercury 2.5 完全顛覆了這種速度規則。根據人工智慧分析公司「Artificial Analysis」的測試，該模型每秒可生成約 770.4 個 token（AI 處理文字的最小單位）。[出處：Sam Codeman](https://www.samcodeman.com/writing/mercury-2-5-770-tokens-per-second-benchmark) 根據開發商報告，在特定環境下甚至能達到每秒 1,107 個 token。[出處：Pradha](https://www.pradha.id/read/mercury-25-inceptions-push-for-high-speed-diffusion-llms) 這比現有的 AI 模型快了整整 7 倍。[出處：AIPULSEN](https://aipulsen.com/artikel/14260)

簡單來說，現有 AI 需要思考 7 秒的內容，Mercury 2.5 僅需 1 秒即可完成。一旦這種速度普及，我們與 AI 進行語音對話時感受到的微小延遲（Latency）將消失無蹤。即時口譯機或程式編寫助手將能像真人一樣即時反應。[出處：TechBriefe](https://techbriefe.com/tech/ai/mercury-25-llm-achieves-770-tokens-per-second-in-inference-speed)

### 輕鬆解析 (The Explainer)

現有的大型語言模型（LLM）主要採用「Transformer（一種識別句中單字關係的 AI 架構）」。這就像是從書的第一句開始逐字逐句閱讀，速度上存在明顯限制。

反之，Mercury 2.5 使用了一種獨特的「擴散（Diffusion）」技術。[出處：OpenRouter](https://openrouter.ai/inception/mercury-2-5) 打個比方，如果現有的 AI 是逐字寫作的「誠實作家」，那麼 Mercury 2.5 就像是畫家，先構圖整體，再同時填充細節的「熟練畫家」。

這種技術在專業術語中被稱為「並行 token 生成與精煉（Parallel token generation and refinement）」。由於它能同時思考並修整多個單字，因此能更快地輸出成果。[出處：Benchable](https://benchable.ai/models/inception/mercury-2.5-20260908)

### 目前現狀 (Where We Stand)

目前的 Mercury 2.5 不僅速度快，還具備 260,000 token 的龐大上下文窗口（Context Window）。[出處：Blog Build Fast With AI](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review) 這意味著它可以一次讀取並記住數十本厚書的內容。此外，它還支援結構化資料輸出、工具使用以及複雜的邏輯推理，在實際業務中的應用價值極高。[出處：Blog Build Fast With AI](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review)

不過，技術數據會根據測量方式而有所差異，且在極其複雜的專業任務中，它是否能比現有的超大型模型表現更優異，仍需使用者的進一步驗證。[出處：6ic](https://6ic.com/news/mercury-25-llm-achieves-770-tokens-per-second-setting-new-benchmark-for-speed)

### 未來展望 (What's Next)

未來，AI 服務的競爭將不再止步於「有多聰明」，而是「反應有多快」。特別是在語音助手、即時諮詢、遊戲內 NPC（非玩家角色）等重視即時反應的領域，Mercury 2.5 這類模型的活躍令人期待。[出處：CallMissed](https://www.callmissed.com/blog/mercury-diffusion-llm-770-tok-voice-latency) 不久之後，你的智慧型手機裡將搭載反應更靈敏的 AI 助手，問話結束的瞬間就能聽到答案。

---

## 參考資料
1. Sam Codeman, [Mercury 2.5 770 tokens/sec benchmark](https://www.samcodeman.com/writing/mercury-2-5-770-tokens-per-second-benchmark)
2. 6ic, [Mercury 2.5 LLM achieves 770 tokens per second](https://6ic.com/news/mercury-25-llm-achieves-770-tokens-per-second-setting-new-benchmark-for-speed)
3. Pradha, [Mercury 2.5: Inception's push for high-speed diffusion LLMs](https://www.pradha.id/read/mercury-25-inceptions-push-for-high-speed-diffusion-llms)
4. TechBriefe, [Mercury 2.5 LLM achieves 770 tokens per second in inference speed](https://techbriefe.com/tech/ai/mercury-25-llm-achieves-770-tokens-per-second-in-inference-speed)
5. VK.ru, [Mercury 2.5 LLM reaches 770 tokens per second](https://vk.ru/wall-238001904_6156)
6. Inception Labs, [Introducing Mercury 2.5](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)
7. Kunal Ganglani, [Mercury 2.5 770 tokens/sec benchmark (2026)](https://www.kunalganglani.com/blog/mercury-2-5-770-tokens-benchmark)
8. Blog Build Fast With AI, [Mercury 2.5 AI model review](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review)
9. AIPULSEN, [Mercury 2.5 LLM achieves 770 tokens per second](https://aipulsen.com/artikel/14260)
10. CallMissed, [Mercury 2.5 diffusion LLM](https://www.callmissed.com/blog/mercury-diffusion-llm-770-tok-voice-latency)
11. Benchable, [Inception: Mercury 2.5 AI model details and benchmarks](https://benchable.ai/models/inception/mercury-2.5-20260908)
12. Telegram (Hacker News Feed), [Mercury 2.5 LLM reaches 770 tokens per second](https://t.me/hacker_news_feed/132200)
13. OpenRouter, [Mercury 2.5 API pricing and benchmarks](https://openrouter.ai/inception/mercury-2.5)