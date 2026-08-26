---
layout: post
title: "我的電腦能成為聰明的 AI 助理嗎？Perplexity 與 NVIDIA 挑戰「本地 AI」"
description: "Perplexity 與 NVIDIA 合作推出「可攜式電腦 (Portable Computer)」AI 代理，教您如何在沒有網路連線的情況下，在個人電腦上安全、無負擔地使用 AI"
summary: "Perplexity 與 NVIDIA 合作推出了 AI 代理平台「可攜式電腦 (Portable Computer)」，無需網路連線即可在個人電腦上直接執行。"
tags: [AI, 本地 AI, Perplexity, NVIDIA, 人工智慧]
image: 2026-08-27-Perplexity-partners-with-Nvidia-to-launch-a-local-AI-agent.jpg
image_alt: "在基於 NVIDIA GPU 的個人電腦上運作的 Perplexity AI 代理介面畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是降低對雲端依賴，並將數據主權交還給個人的重要轉捩點。在安全與成本效益方面，本地 AI 的吸引力將會與日俱增。"
quiz:
  - question: "Perplexity 與 NVIDIA 此次聯合發表的平台名稱是什麼？"
    choices: ["雲端電腦 (Cloud Computer)", "可攜式電腦 (Portable Computer)", "AI 本地中心 (AI Local Hub)"]
    answer: 1
    explanation: "答案是「可攜式電腦 (Portable Computer)」。這是一個無需網路連線，即可在個人設備上直接運作的 AI 代理平台。"
  - question: "使用該平台可以獲得什麼樣的成本優勢？"
    choices: ["免月費訂閱", "零 Token 費用", "豁免電費"]
    answer: 1
    explanation: "使用雲端 AI 服務時產生的「Token 費用」，在此平台下將不會產生。"
  - question: "此 AI 代理主要在什麼硬體環境下執行？"
    choices: ["網頁瀏覽器", "所有智慧型手機", "基於 NVIDIA GPU 的個人電腦與伺服器"]
    answer: 2
    explanation: "初期可在 NVIDIA DGX Spark 及搭載 NVIDIA RTX 顯示卡的 Linux 個人電腦等設備上執行。"
lang: zh-tw
ref: 2026-08-27-Perplexity-partners-with-Nvidia-to-launch-a-local-AI-agent
---

想像一下：早晨醒來，你對著電腦說：「幫我整理好今天會議所需的資料。」過去我們使用的大多數生成式 AI，都必須經過龐大的雲端（透過網路連接的遠端伺服器）處理。但現在，那個聰明的 AI 助理不再存在於網路彼端的伺服器中，而是直接在你的辦公桌電腦裡安全地處理任務，這樣的未來已近在眼前。

近期，以人工智慧搜尋服務聞名的 Perplexity 與圖形處理器（GPU）之王 NVIDIA 攜手合作，公開了全新的 AI 代理平台「可攜式電腦 (Portable Computer)」([Perplexity-NVIDIA 可攜式電腦發布](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs))。這項服務是一項革命性的嘗試，旨在將 AI 的運作方式從雲端中心轉向個人設備中心。

## 為何這很重要？

最大的改變在於成本與安全。過去要使用雲端 AI，每當 AI 產生一次回答，你都必須支付所謂「Token（AI 使用的字詞單位資訊量）」的相關費用。然而，「可攜式電腦」是藉由你電腦的硬體效能直接執行 AI，因此再也不需要支付這類 Token 費用([Perplexity 可攜式電腦發布](https://www.androidauthority.com/perplexity-portable-computer-local-ai-agent-3703083/))。

此外，在安全方面也具有突破性。傳統方式需要將使用者的作業內容傳送至外部伺服器，但現在 AI 模型、使用者數據，以及 AI 執行的任務本身都保留在設備內部，這在個人隱私保護方面讓人更加放心([Perplexity 與 NVIDIA 的本地桌面 AI 代理](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lhM3JydkVSRWVaUGZFWUJReU1pZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en))。

## 簡單易懂的解釋

若要比喻「可攜式電腦」的原理，就像是**「付費圖書館」與「個人書房」的差別**。

過去的雲端 AI 就像每次都要付費去外部圖書館借書閱讀；而「可攜式電腦」則如同直接把圖書館搬進你的房間。雖然初期需要購買設備成本，但一旦配置完成，無論何時使用 AI 都不會再產生額外費用。

在技術上，該平台不僅包含作為 AI 大腦的「模型」，還設計了判斷 AI 該做什麼的「指揮者 (Orchestrator)」以及「代理框架 (AI 代理的驅動環境)」，讓這些都在個人設備內部運作([Perplexity 本地 AI 行為](https://www.theregister.com/ai-and-ml/2026/08/26/now-perplexity-is-trying-to-get-into-the-local-ai-action/5292449))。換言之，即使網路斷線，AI 也能自主判斷並解決複雜的任務([Perplexity 可攜式電腦發布](https://x.com/wallstengine/status/2092262633068277776))。

## 現況

目前此平台優先在 NVIDIA 的硬體環境下進行優化並啟動。具體而言，適用於 NVIDIA 的 DGX Spark 系統，或是搭載 NVIDIA RTX 顯示卡的 Linux 電腦([NVIDIA DGX Spark 與本地 AI](https://www.gadgetvoize.com/2026/08/26/nvidia-pushes-local-ai-with-open-models-agents-and-perplexity-partnership/))。

發布初期支援「Qwen 3.8 27B」模型及經過額外訓練的「Qwen PPLX 27B」模型，未來也將支援 NVIDIA 的「Nemotron 3.5 Lightning (30B)」模型([Perplexity 與 NVIDIA 的本地 AI 代理](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/))。從一般資訊搜尋到處理複雜的工作流程，都能在本地直接執行，是其一大特色([Perplexity 可攜式電腦發布](https://aistart.ai/ainews/perplexity-local-ai-agent-nvidia))。

## 未來展望

預計未來，更多一般個人 PC 環境也能體驗到這種「本地 AI」。隨著 AI 技術越過雲端這道巨大的藩籬，深入使用者的設備中，即使在網路連線不穩定的環境下也能享受高效能 AI 帶來的便利，這樣的時代已經來臨([Perplexity 可攜式電腦發布](https://basic-tutorials.com/news/perplexity-portable-computer-ai-agent-now-runs-locally-on-nvidia-dgx-spark/))。未來我們在選擇個人電腦時，除了 CPU 或 RAM 之外，「能夠多快地執行何種 AI 代理」看來也將成為重要的購買標準。

---

## MindTickleBytes 的 AI 記者觀點
這次的嘗試降低了對雲端的依賴，將數據主權回歸給個人，是人工智慧發展的重要轉捩點。期待技術不僅僅帶來便利，更能更緊密且安全地融入個人日常生活。

## 參考資料
1. [Perplexity partners with Nvidia to launch Portable Computer, a fully local AI agent with zero token costs | VentureBeat](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs)
2. [Perplexity and NVIDIA team up to release a local AI agent | How-To Geek](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/)
3. [Perplexity launches a local AI agent with zero token costs - Android Authority](https://www.androidauthority.com/perplexity-portable-computer-local-ai-agent-3703083/)
4. [Perplexity and Nvidia partner for local-first AI platform | CNBC](https://www.cnbc.com/video/2026/08/25/perplexity-and-nvidia-partner-for-local-first-ai-platform.html)
5. [Wall St Engine on X: "PERPLEXITY LAUNCHES FULLY LOCAL AI AGENTS..."](https://x.com/wallstengine/status/2092262633068277776)
6. [NVIDIA Pushes Local AI With Open Models, Agents and Perplexity Partnership – Gadget Voize](https://www.gadgetvoize.com/2026/08/26/nvidia-pushes-local-ai-with-open-models-agents-and-perplexity-partnership/)
7. [Perplexity and Nvidia partner for local desktop AI agent - Overview | Google News](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lhM3JydkVSRWVaUGZFWUJReU1pZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en)
8. [Perplexity Launches Local AI Agent Portable Computer | The Outpost](https://theoutpost.ai/news-story/perplexity-portable-computer-brings-local-ai-agent-to-your-desktop-with-no-cloud-dependency-30115/)
9. [Perplexity partners With Nvidia to launch... | VMVirtualMachine.com](https://vmvirtualmachine.com/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs/)
10. [Portable Computer is Perplexity's new local AI agent - why... | ZDNET](https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/)
11. [World Leader in Artificial Intelligence Computing | NVIDIA](https://www.nvidia.com/)
12. [Perplexity and Nvidia Launch a Zero-Token-Cost Local AI Agent | AI Market Watch](https://www.ai-market-watch.com/news/perplexity-and-nvidia-launch-portable-computer-a-fully-local-ai-agent-with-zero--kyx83w)
13. [Perplexity Launches Fully Local AI Agent with Nvidia | AI News](https://aistart.ai/ainews/perplexity-local-ai-agent-nvidia)
14. [Now Perplexity is trying to get into the local AI action | The Register](https://www.theregister.com/ai-and-ml/2026/08/26/now-perplexity-is-trying-to-get-into-the-local-ai-action/5292449)
15. [Perplexity Portable Computer: AI agent now runs locally on NVIDIA DGX Spark | Basic Tutorials](https://basic-tutorials.com/news/perplexity-portable-computer-ai-agent-now-runs-locally-on-nvidia-dgx-spark/)
16. [Perplexity AI launches Portable Computer on-device AI agent | SiliconAngle](https://siliconangle.com/2026/08/25/perplexity-ai-launches-portable-computer-on-device-ai-agent/)