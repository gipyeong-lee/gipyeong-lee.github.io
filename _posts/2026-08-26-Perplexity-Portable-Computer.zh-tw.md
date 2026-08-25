---
layout: post
title: "我的電腦變成 AI 專家了？Perplexity 的「Portable Computer」將帶來什麼變革"
description: "Perplexity 公布了本地 AI 代理平台「Portable Computer」。本文將簡單說明它是什麼，以及為什麼它如此重要。"
summary: "Perplexity 的「Portable Computer」是一項創新的平台，它不將敏感數據發送至雲端，而是直接在用戶的本地電腦上運行 AI 代理，同時兼顧了安全性與效能。"
tags: [AI, Perplexity, 人工智慧, 本地 AI, 安全性]
image: 2026-08-26-Perplexity-Portable-Computer.jpg
image_alt: "可視化在 NVIDIA DGX Spark 設備上運行的本地 AI 代理系統的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "減少對雲端的依賴並在個人化環境中掌控 AI，是邁向真正代理時代的必要步驟。"
quiz:
  - question: "Perplexity 的「Portable Computer」與既有的雲端 AI 最主要的區別是什麼？"
    choices: ["完全不需要網路連線", "不將數據發送至雲端，在本地環境進行處理", "訂閱費用昂貴得多"]
    answer: 1
    explanation: "Portable Computer 將代理運行所需的關鍵任務全部在用戶的本地硬體上執行，從而強化了數據隱私。"
  - question: "Portable Computer 平台建議使用什麼樣的硬體環境？"
    choices: ["一般入門級智慧型手機", "搭載 NVIDIA DGX Spark 及 RTX 的 Linux 電腦", "支援網頁瀏覽器的平板電腦"]
    answer: 1
    explanation: "為了處理高效能 AI 模型，該平台利用基於 NVIDIA DGX Spark 或搭載 RTX GPU 的 Linux 系統硬體。"
  - question: "當本地 AI 代理執行複雜任務時，會如何應對？"
    choices: ["強行僅在本地處理所有任務", "必要時將任務轉移至雲端基礎的頂尖模型", "立即中斷任務並顯示錯誤訊息"]
    answer: 1
    explanation: "基本上由本地處理，但若本地模型難以解決的任務，會將功能擴展（escalation）至雲端基礎的上層模型來解決。"
lang: zh-tw
ref: 2026-08-26-Perplexity-Portable-Computer
---

想像一下。早上起床，對著電腦裡的 AI 說：「請整理我昨天在公司寫的會議文件與相關資料，幫我寫一份要發給團隊成員的摘要報告。」過去，這些資料全部都要傳輸到網路彼端的雲端伺服器進行處理，但現在，這個過程僅在您房內的電腦中完成。

Perplexity 最近發表的「Portable Computer（攜帶式電腦）」正是夢想實現這樣的變革。它不只是協助網路搜尋的 AI，更開闢了一條新路徑——在保護您數據安全的同時，讓 AI 代理（接收用戶指令、自行調用工具與模型來執行任務的 AI）能直接在您的電腦上運作 [[Source 1](https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai)]。

## 為什麼這很重要？

過去要使用 AI，必須將敏感資訊發送至 Google 或 OpenAI 等大企業的雲端伺服器，這引發了對數據隱私與安全性的不安。此外，AI 模型每次執行任務所產生的伺服器使用費（Token 成本）也是一大負擔。

然而，Portable Computer 不同。運行代理的核心引擎，包括「代理框架（AI 代理能有機運用多種工具的架構）」、「協調器（指揮任務的管理員）」，以及在下方實際進行思考的「子代理 LLM（大型語言模型）」，全部都在用戶的本地硬體上運行 [[Source 7](https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/), [Source 8](https://x.com/perplexity_ai/status/2092268362386780270)]。也就是說，數據不會流向外部，安全性更高，且針對本地任務不需要額外的雲端使用費 [[Source 2](https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/), [Source 3](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs)]。

## 簡單理解

我們可以將 Portable Computer 比喻為**「在家裡下廚的總鋪師」**。

如果說既有的 AI 服務是向遠處的餐廳（雲端伺服器）下單等待送餐，那麼 Portable Computer 就等於是請了一位專業廚師（本地 AI 模型）進駐您家的廚房。食材（您的個人數據）不需要送出去，既新鮮又安全。

但有時候，難道不需要處理極其複雜的頂級料理嗎？這時，家裡的廚師會先嘗試解決，只有在需要非常高端的技術時，才會暫時向外部的米其林星級主廚（雲端基礎的頂尖模型）請求協助。Perplexity 的 Portable Computer 具備這種「步驟級路由（Step-level routing）」系統，平時在電腦內快速處理，只有在本地模型難以解決時，才聰明地尋求雲端協助 [[Source 1](https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai), [Source 5](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/)]。

在這裡，扮演廚師角色的 AI 模型為「Qwen 3.8 27B」或 Perplexity 額外訓練的「PPLX 27B」模型 [[Source 4](https://gizmodo.com/perplexity-launches-local-ai-model-that-will-run-on-your-gpu-instead-of-the-cloud-2000802883), [Source 6](https://www.computerworld.com/article/4213821/perplexitys-on-device-ai-offering-promises-data-control-and-lower-token-costs.html)]。27B（270 億參數）足以處理大多數複雜的事務工作，同時又能確保在 NVIDIA 的高性能硬體「DGX Spark」或 RTX GPU 環境中流暢運行 [[Source 4](https://gizmodo.com/perplexity-launches-local-ai-model-that-will-run-on-your-gpu-instead-of-the-cloud-2000802883), [Source 11](https://pc-tablet.com/perplexity-launches-portable-computer-local-ai-agent-for-private-workflows/193699/)]。

## 目前狀況

目前的 Portable Computer 目標客群是希望建構完全個人化 AI 工作流程的用戶。不過，硬體要求相當嚴格，必須具備搭載 NVIDIA DGX Spark 等高性能 GPU 的 Linux 機器環境 [[Source 2](https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/), [Source 3](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs)]。

這不只是下載模型來運行那麼簡單。該平台將 AI 模型、執行任務所需的各種工具、應用程式連接功能，以及能安全執行任務的「沙盒（安全性強化且隔離的執行環境）」打包為一個完整套件提供給用戶 [[Source 5](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/), [Source 7](https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/)]。

## 未來發展

能親手掌握數據控制權對企業環境極具吸引力。以 Portable Computer 為開端，未來隨著個人硬體效能提升，即使沒有雲端支援，更複雜的 AI 代理也將在我們的桌面上忠實地扮演個人秘書角色 [[Source 9](https://techgenyz.com/perplexity-portable-computer-nvidia-dgx-spark/)]。

透過這次發表，Perplexity 開啟了用戶能更細膩選擇 AI 使用方式的「在地優先（Local-first）」時代。或許在不久的將來，您的 GPU 將不僅是為了遊戲或圖形處理而存在的零件，它將成為您最聰明的個人 AI 代理的「大腦」。

## AI 的觀點
減少對雲端的依賴並在個人化環境中掌控 AI，是邁向真正代理時代的必要步驟。這將把數據的控制權交還給用戶，同時也將成為創造更緊密且值得信賴的人機協作環境之契機。

## 參考資料

1. Introducing Portable Computer - perplexity.ai: https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai
2. Portable Computer is Perplexity's new local AI agent - ZDNET: https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/
3. Perplexity partners with Nvidia to launch Portable Computer ...: https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs
4. Perplexity Launches Local AI Model That Will Run on Your GPU ...: https://gizmodo.com/perplexity-launches-local-ai-model-that-will-run-on-your-gpu-instead-of-the-cloud-2000802883
5. Perplexity and NVIDIA team up to release a local AI agent: https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/
6. Perplexity’s on-device AI offering promises data control and ...: https://www.computerworld.com/article/4213821/perplexitys-on-device-ai-offering-promises-data-control-and-lower-token-costs.html
7. Perplexity Ships Portable Computer on NVIDIA DGX Spark: Local ...: https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/
8. Perplexity on X: "Today we’re launching Portable Computer on ...: https://x.com/perplexity_ai/status/2092268362386780270
9. Perplexity Portable Computer Could Change AI Agents With ...: https://techgenyz.com/perplexity-portable-computer-nvidia-dgx-spark/
11. PerplexityLaunchesPortableComputerLocal AI Agent for Private...: https://pc-tablet.com/perplexity-launches-portable-computer-local-ai-agent-for-private-workflows/193699/