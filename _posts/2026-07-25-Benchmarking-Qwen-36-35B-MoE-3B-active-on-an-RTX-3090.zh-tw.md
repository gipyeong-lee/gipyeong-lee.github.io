---
layout: post
title: "我的電腦能跑 AI 嗎？透過 Qwen 3.6 35B MoE 探索本地 AI 世界"
description: "我們將深入淺出地介紹如何在 RTX 3090 顯示卡上執行高性能 AI 模型 Qwen 3.6 35B MoE，並分享效能測試結果與本地 AI 的應用方式。"
summary: "在 RTX 3090 上執行 Qwen 3.6 35B-A3B 模型，每秒可生成超過 100 個 Token，體驗比一般的 27B 稠密模型更快的速度。"
tags: [AI, 本地LLM, Qwen, RTX3090, 硬體]
image: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090.jpg
image_alt: "在 RTX 3090 顯示卡上運作並測量 Qwen 3.6 AI 模型效能的畫面。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在本地環境中高效運行大型模型，在資料隱私與成本方面具有巨大的優勢。特別是利用 MoE 架構，可以巧妙地克服硬體限制。"
quiz:
  - question: "MoE (Mixture-of-Experts) 架構的模型之所以比一般的稠密模型更快，原因為何？"
    choices: ["因為它們總是使用所有參數", "因為它們一次僅處理約 3B (30億) 的活躍參數", "因為它們僅包含針對 RTX 3090 優化的程式碼"]
    answer: 1
    explanation: "MoE 模型在運作時僅從整個模型中挑選部分專家 (參數) 進行計算，因此即使是 35B 大小的模型，也僅使用約 3B 的活躍參數，運算速度極快 [Source 5]。"
  - question: "在 RTX 3090 上執行 Qwen 3.6 35B-A3B 模型時，效能表現如何？"
    choices: ["每秒 5~10 個 Token", "每秒 50~100 個以上的 Token", "每秒 1,000 個以上的 Token"]
    answer: 1
    explanation: "根據測試結果，依據設定的不同，每秒可展現 50 到 100 個以上的 Token 生成速度 [Source 2], [Source 5], [Source 7]。"
  - question: "若必須在效能更高的 27B 稠密模型與 35B-A3B MoE 模型之間做選擇，建議為何？"
    choices: ["35B 模型絕對較優", "若重視回答品質，建議選擇 27B 稠密模型", "兩者效能完全沒有差異"]
    answer: 1
    explanation: "27B 稠密模型在基準測試結果中比 MoE 模型領先約 1 到 10 分，因此在重視回答品質時推薦優先使用 [Source 3]。"
lang: zh-tw
ref: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090
---

想像一下，如果你每天使用的電腦裡，住著一位 AI 助理，即使沒有連上網路，也能在 1 秒內精準回答各種複雜問題。不用擔心個人資料外洩，在電腦內安全運作的「專屬 AI」，這已不再是科幻電影的情節。我們將以高中生也能聽懂的方式，為大家介紹近期發布的強大 AI 模型「Qwen 3.6 35B-A3B」如何讓這一切成為現實。

### 為什麼這很重要？ (Why It Matters)

過去的高性能 AI 模型體積過於龐大，一般使用者的電腦根本無法負擔。但現在情況不同了，隨著「本地 AI（不需網路連接，直接在使用者設備運作的 AI）」技術突飛猛進，僅靠家中的 RTX 3090 等顯示卡，就能充分體驗高品質的 AI 運作 [Source 8]。

本地 AI 受到矚目的原因主要有二。第一是**隱私**，資料不需傳輸至外部伺服器，直接在電腦處理，安全性更高。第二是**速度與經濟性**，不受網路速度影響，運作零延遲，模型只需下載一次，後續使用無須額外費用。本次測試的 Qwen 3.6 35B-A3B 模型，在本地 AI 環境中展現了極高的性價比與效能，因而受到廣泛關注 [Source 6]。

### 輕鬆理解 (The Explainer)

Qwen 3.6 35B-A3B 模型的核心，在於一種稱為 **MoE (Mixture-of-Experts，專家混合結構)** 的特殊設計。

舉個簡單的比喻：想像你在經營一座巨大的圖書館，若所有書籍都由一名管理員處理會過於勞累。因此，你聘請了多位各領域的專家管理員。在這裡，「35B」代表管理員的總數（總參數），而「3B active」則代表當問題傳入時，實際調用來尋找答案的專家管理員人數（活躍參數） [Source 5]。

傳統的「稠密模型 (Dense Model)」結構中，所有管理員每次都要參與工作；但在 MoE 模型中，則會根據問題內容，僅調用特定領域的專家。因此，該模型雖擁有 350 億個參數而顯得非常聰明，但在實際運算時，僅需處理 30 億個參數規模的計算量，從而能迅速產出結果 [Source 5]。

### 目前現況 (Where We Stand)

近期於 RTX 3090 顯示卡上進行的基準測試結果令人驚豔：

* **速度**：套用特定設定（UD-Q4_K_XL 量化）時，短問題每秒可生成約 101.7 個 Token（AI 生成文字的單位），長問題則為每秒 80.9 個 Token [Source 7]。在其他環境下也能穩定維持每秒 50~100 個 Token 的水準，遠快於 27B 稠密模型（每秒約 35 個 Token） [Source 5]。
* **侷限性**：當然，體積龐大且快速的 MoE 模型並非萬能。與 27B 稠密模型相比，在回答精確度（品質）方面，27B 稠密模型在基準測試中約領先 1 到 10 分 [Source 3]。簡而言之，若最重視速度則選擇 MoE 模型，若最重視回答品質，則建議選擇稠密模型 [Source 3]。
* **優化**：此外，針對 AI 訓練技術之一的「推論加速技術（Speculative Decoding）」，經確認在 RTX 3090 等環境下，對提升速度並無顯著幫助 [Source 4]。

### 未來發展 (What's Next)

未來，本地 AI 技術將變得更加輕量且智慧化。本次進行測試的專家們正積極分享各種設定技巧，讓模型能根據使用者的 PC 規格進行高效運作 [Source 3], [Source 11]。現在的使用者不僅僅是選擇優秀的模型，更進入了能根據個人顯示卡效能，選擇最優「量化（調整資料精度以縮小模型大小的技術）」等級，親手調教專屬 AI 環境的時代 [Source 2], [Source 14]。

### MindTickleBytes 的 AI 記者觀點

本地 AI 不僅僅是一項技術成就，更是一個重新奪回「設備主權」的過程。像 Qwen 3.6 35B-A3B 這種高效模型的出現，正加速推動一個未來——任何人無需昂貴的伺服器，也能在個人 PC 上享受高性能 AI。AI 不再是遠方巨頭伺服器上的產物，而將成為你辦公桌電腦中，與你共同思考的夥伴。

## 參考資料

1. [Qwen/Qwen3.6-35B-A3B · My RTX 3090 ran out of excuses: Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/discussions/37)
2. [Qwen 3.6-35B-A3B Local Hardware Guide — GPU & VRAM (2026) | Compute Market](https://www.compute-market.com/blog/qwen-3-6-local-hardware-guide-2026)
3. [GitHub - tfriedel/qwen3.6-rtx3090-lab: Benchmarks, compose files, and findings for running Qwen3.6 (27B dense + 35B-A3B MoE) on 4× RTX 3090](https://github.com/tfriedel/qwen3.6-rtx3090-lab)
4. [GitHub - thc1006/qwen3.6-speculative-decoding-rtx3090](https://github.com/thc1006/qwen3.6-speculative-decoding-rtx3090)
5. [Best Way to Run Qwen 3.6 35B MoE Locally: VRAM, Speed, Setup | InsiderLLM](https://insiderLLM.com/guides/best-way-run-qwen-3-6-35b-moe-locally/)
6. [I Benchmarked Qwen3.6–35B-A3B Model on 3090, 4090, 5090 and M5 Max. Here’s What Nobody Tells You. | Medium](https://medium.com/@ttio2tech_28094/i-benchmarked-qwen3-6-35b-a3b-model-on-3090-4090-5090-and-m5-max-heres-what-nobody-tells-you-62fbb2f4e64a)
7. [Qwen 3.6 Complete Guide: 27B Dense, 35B-A3B MoE, and Which to Use | InsiderLLM](https://insiderLLM.com/guides/qwen-3-6-local-ai-guide/)
8. [Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090](https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090)
9. [From 25 to 283 tok/s: Serving Qwen3.6 on Dual RTX 3090s](https://alexander-ollman.github.io/qwen3.6-on-rtx3090/qwen3.6-on-rtx3090.html)
10. [Qwen3.614B A3BFableVibes benchmarked and tested vs... - YouTube](https://www.youtube.com/watch?v=DBEd5dpxaNQ)
11. [Qwen/Qwen3.6-35B-A3B· Hugging Face](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
12. [Qwen3.635B-A3BonRTX3060 12GB: Local LLM | SpecPicks](https://specpicks.com/reviews/qwen-36-35b-a3b-rtx-3060-12gb-local-2026)
13. [ЗапускаемQwen3.635B-A3B+ opencode локально наRTX... / Хабр](https://habr.com/ru/articles/1026482/)
14. [Qwen3.627B vs35B-A3BMoEMTP наRTX5080 16GB... | AiManual](https://ai-manual.ru/article/rtx-5080-16gb-qwen36-27b-mtp-ili-35b-a3b-moe-mtp---chto-vyibrat-dlya-lokalnogo-kodinga/)