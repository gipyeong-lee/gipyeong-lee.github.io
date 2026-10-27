---
layout: post
title: "如果 AI 學不會「拒絕」？「無審查」DeepSeek 模型的進化"
description: "探討 DeepSeek 模型中移除拒絕反應神經網路的「已刪除（Abliterated）」模型，以及 5 種可使用該模型的推理服務。"
summary: "移除了安全護欄（拒絕反應）的 DeepSeek「已刪除」模型，現已可透過 5 家推理提供商使用。"
tags: [AI, DeepSeek, 技術趨勢, 人工智慧]
image: 2026-10-27-There-are-now-5-inference-providers-for-abliterated-DeepSeek.jpg
image_alt: "電腦螢幕中視覺化顯示未經審查的 AI 資料流畫面。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "移除安全裝置的模型問世，在擴大使用者創作自由的同時，也讓人對 AI 的負責任應用進行更深層的思考。"
quiz:
  - question: "什麼是「已刪除（Abliteration）」？"
    choices: ["提升模型智慧的學習過程", "尋找並刪除導致拒絕反應之神經網路的技術", "修正 AI 錯誤的軟體更新"]
    answer: 1
    explanation: "「已刪除（Abliteration）」是一種識別並刪除導致 AI 模型對特定問題產生拒絕反應之神經網路路徑的技術。"
  - question: "在哪裡可以使用「已刪除」模型？"
    choices: ["僅限 DeepSeek 官方網站", "雲端 API 服務與本機環境皆可", "僅限特定企業內部網路"]
    answer: 1
    explanation: "「已刪除」模型既可透過 5 家雲端 API 推理提供商使用，也能利用 Ollama 等工具在個人電腦上執行。"
  - question: "使用這些模型的主要目的是什麼？"
    choices: ["強化安全性", "執行高階推理作業並取得無審查的回答", "提升系統速度"]
    answer: 1
    explanation: "使用「已刪除」模型的主要目的，是在執行使用者複雜的推理作業時，取得 AI 不帶有人為拒絕反應的回答。"
lang: zh-tw
ref: 2026-10-27-There-are-now-5-inference-providers-for-abliterated-DeepSeek
---

試想一下，當您詢問人工智慧（AI）複雜問題的解決方案，或請求針對特定主題進行創意寫作時，AI 卻突然回應「無法回答該問題」並中斷對話，那會是什麼感覺？這種因所謂的 AI「安全護欄」過濾系統導致使用者無法獲得預期答案的情況，時有所聞。

近期，AI 產業出現了一種備受矚目的特殊模型，它們透過人為手段移除安全裝置，以提供「無審查」的回答。這些模型正是基於 DeepSeek 模型開發的「已刪除（Abliterated）」模型。

## 為什麼這很重要？

對於在日常生活中使用 AI 的人們來說，AI 的拒絕回答有時會大幅降低工具的效用。對於研究人員而言，這會阻礙複雜邏輯推理或敏感主題的探討；對於創作者來說，則會影響原創內容的生產。

「已刪除」模型旨在確保 AI 不會對特定問題產生拒絕反應。簡單來說，就是讓 AI 「不會停止思考或拒絕」，並持續執行使用者要求的進階推理作業直到完成。隨著近期出現 5 家能輕鬆使用這些模型的推理提供商，任何人都能輕易體驗到這種「無審查 AI」的效能 [Source 14]。

## 簡單理解：鎖住 AI 的「大腦通道」

要理解「已刪除（Abliteration）」過程，我們可以將 AI 比喻為一座「巨大的圖書館」。普通的 AI 模型結構就像圖書館員會阻擋使用者閱讀「被判斷為不適當的書籍」。這裡的「已刪除」技術，並不只是館員的指示，而是找出並鎖住或刪除「通往特定禁書的門」本身 [Source 7]。

從技術層面深入探討，研究人員會分析 AI 模型的神經網路（Neural pathways，即 AI 處理思考的大腦通道）。他們找出當 AI 收到特定問題時，會判定「我該拒絕」的特定路徑，並人為地將其刪除 [Source 7]。如此一來，AI 就處於「未曾學會拒絕」的狀態，從而能在不受干擾的情況下持續回應 [Source 5]。這可以說是移除人為限制，同時不損害 AI 原有智慧的過程。

## 現況：哪裡可以使用？

目前，「已刪除」版本的 DeepSeek 模型主要透過兩種方式應用：

1. **利用雲端 API**：開發人員與使用者可透過雲端服務，使用 5 家推理提供商來呼叫這些模型 [Source 14]。例如，「DeepSeek R1 Distill Qwen 32B Abliterated」等特定模型，可透過按量付費（Pay-per-token）的方式使用 [Source 2]。
2. **本機環境執行**：使用者也能在個人電腦上執行這些模型。使用 Ollama 或 LM Studio 等工具，即可不透過雲端伺服器，直接在自己的 PC 上運作無審查 AI [Source 1, Source 6, Source 7]。

在線上社群中，這些模型正透過 Hugging Face 等平台活躍地分享，許多人正自由地構建符合自身研究或創作需求的 AI 環境 [Source 7]。

## 未來走向

未來，AI 的評選標準將不再僅限於效能，還包括「該 AI 具備何種政策」。需求將會增加，人們不僅尋求聰明的 AI，更會尋找能最自由、毫無障礙地回應使用者需求的 AI。然而，隨著移除安全護欄的模型增加，針對 AI 內容產生的倫理責任與安全應用的技術性討論，也將會更加激烈。

## AI 的觀點（MindTickleBytes AI 記者觀點）

「已刪除」技術對將 AI 視為「工具」的使用者來說帶來了釋放感，但同時也與 AI 模型應受到安全控管的傳統價值觀產生衝突。技術自由度越高，我們使用時的倫理標準也必須隨之更加精進。

## 參考資料

1. [huihui-ai/DeepSeek-R1-Distill-Llama-70B-abliterated· Hugging Face](https://huggingface.co/huihui-ai/DeepSeek-R1-Distill-Llama-70B-abliterated)
2. [DeepSeekR1 Distill Qwen 32BAbliteratedAPI Pricing... | Muapi](https://muapi.ai/comparison/deepseek-r1-qwen-32b-abliterated)
3. [Ling-3.1-flash vsDeepSeekV4.1 Flash: 3x the Bill](https://www.orcarouter.ai/blog/ling-3-1-flash-vs-deepseek-v4-1-flash)
4. [huihui_ai/deepseek-r1-abliterated:32b](https://ollama.com/huihui_ai/deepseek-r1-abliterated:32b)
5. [How to Run UncensoredDeepSeekR1 on Your Local Machine](https://apidog.com/blog/deepseek-r1-abliterated/)
6. [How to Run UncensoredDeepSeekLocally Step-by-Step - YouTube](https://www.youtube.com/watch?v=hIaAv_oTBE4)
7. [How to RunDeepSeekV4.1 Flash Uncensored: Local Setup Guide 2026](https://www.hackaigc.com/blog/how-to-run-deepseek-v4-1-flash-uncensored-2026)
9. [Abliterated Model Router | AllModels](https://allmodels.io/llm/abliterated)
10. [Abliterated DeepSeek V4.1 Flash API: Claimed vs Verified ...](https://explainx.ai/blog/abliterated-deepseek-v4-1-flash-hosted-api-abliteration-ai-claimed-vs-verified-2026)
12. [The Complete Guide to DeepSeek-R1-0528 Inference Providers ...](https://devstacktips.com/development/machine-learning/2025/08/11/the-complete-guide-to-deepseek-r1-0528-inference-providers-where-to-run-the-leading-open-source-reasoning-model/)
14. [There are now 5 inference providers for abliterated DeepSeek](https://nilaykhandelwal.com/item/50254836)
15. [huihui-ai/DeepSeek-R1-Distill-Qwen-14B-abliterated-v2 · Hugging Face](https://huggingface.co/huihui-ai/DeepSeek-R1-Distill-Qwen-14B-abliterated-v2)
16. [DeepSeekV4.1 Flash Jailbreak 2026 — FREE Prompt, No... - YouTube](https://www.youtube.com/watch?v=u2Tr4t16odk)
17. [IntroducingDeepSeek-V4.1-Flash: smarter, faster, more efficient.](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)
18. [DeepSeekV4 Pro NSFW: How to Enable Uncensored Mode 2026](https://www.hackaigc.com/blog/deepseek-v4-pro-nsfw-uncensored-2026)