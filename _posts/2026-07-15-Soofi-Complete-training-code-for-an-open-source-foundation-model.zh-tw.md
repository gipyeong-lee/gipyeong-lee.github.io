---
layout: post
title: "AI 是「黑盒子」？以透明度為武器的歐洲 AI 新模型：Soofi"
description: "帶您輕鬆了解從訓練數據到程式碼完全公開的透明 AI 模型「Soofi S」，以及它背後的深刻意義。"
summary: "德國德國電信（Deutsche Telekom）旗下的 Soofi 團隊公開了專精於英語與德語的透明開源 AI 模型「Soofi S」。"
tags: [AI, 開源, 人工智慧, Soofi]
image: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model.jpg
image_alt: "由透明玻璃碎片匯聚成一具智慧大腦的數位藝術"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在企業視隱私為理所當然的 AI 產業中，他們做出了「完全公開」的破格選擇。這看起來是歐洲提升技術可信度的一項策略性嘗試。"
quiz:
  - question: "Soofi S 模型最核心的主張是什麼？"
    choices: ["壓倒性的參數數量", "極致的透明度與數據公開", "最強的韓語效能"]
    answer: 1
    explanation: "Soofi S 強調透明度，公開了包括訓練數據來源、訓練程式碼與超參數等開發過程中的所有細節。"
  - question: "Soofi S 30B-A3B 模型所採用的「專家混合（Mixture-of-Experts, MoE）」架構有何優點？"
    choices: ["始終使用所有參數", "在 300 億個參數中，每個 Token 僅啟用 30 億個，效率更高", "只能處理德語"]
    answer: 1
    explanation: "MoE 架構能有效從整體參數中選擇部分進行運算，兼顧效能與運算速度。"
  - question: "Soofi 專案目前聚焦於哪些語言？"
    choices: ["英語與韓語", "英語與德語", "德語與法語"]
    answer: 1
    explanation: "Soofi S 專注於英語與德語的雙語能力，尤其刻意增加了德語數據的訓練比例。"
lang: zh-tw
ref: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model
---

想像一下，如果您吃到一道絕世美味的料理，卻完全無法得知食譜，這會是什麼感覺？這是一道像是「黑盒子」般的料理，您不知道裡面用了什麼食材、烹調時間多久，或是用了什麼特殊的技巧。

目前人工智慧（AI）產業的現狀正是如此。雖然尖端 AI 模型每天層出不窮，但這些 AI 究竟「吃」了什麼數據長大、如何訓練而成，企業總是將其視為機密，包裹得嚴嚴實實。然而，歐洲現在出現了一個直接向這種「秘密主義」下戰帖的模型，那就是德國德國電信（Deutsche Telekom）旗下 Soofi 團隊所推出的開源 AI 模型——**「Soofi S」**。

## 為什麼這很重要？

或許您會想：「只要用效能好的 AI 就行了，不是嗎？」但在將 AI 導入企業運作或公共服務時，「可信度」至關重要。舉例來說，當您要讓 AI 摘要公司機密文件時，若不了解 AI 的內部運作機制，難免會感到不安。

Soofi S 公開了模型的權重（AI 大腦中的連結強度）、中間檢查結果，甚至連**訓練數據的來源記錄（Data provenance）**也都全數公開 [出處：[2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424), [出處：SoofiS: A SovereignFoundationModelfor German and English](https://www.emergentmind.com/videos/sovereign-open-source-bilingual-llm-cef87c5b)。這等同於以透明度為武器，讓使用者能夠完全信任並使用該 AI。

## 輕鬆理解技術特點

我們用比喻來簡化 Soofi S 的技術特色：

第一，**「連資優生的讀書秘訣都全盤托出」**。一般 AI 模型通常只公開成果，但 Soofi S 連模型的訓練程式碼與超參數（AI 學習環境的設定值）都一併開源 [出處：[2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424)。這就像考上榜首的學生公開了自己讀了哪些參考書、每天花多少時間學習的詳細計畫表一樣。

第二，採用了**「專家混合架構（Mixture-of-Experts, MoE）」**的聰明大腦運作方式。Soofi S 30B-A3B 模型的總參數高達 300 億個，但實際上回答問題時，只會啟用其中的 30 億個 [出處：SoofiS 30B activates 3B parameters per token, tops... | UncensoredHub](https://uncensoredhub.ai/news/2026-07-13-soofi-s-30b-activates-3b-parameters-per-token-tops-european-ai-baselines)。這就像我們去百貨公司時，不會逛完整個商場，而是直接前往目的地「鞋店」一樣。透過這種方式，能更有效率地快速生成回答。

第三，**「針對英語與德語的客製化教育」**。Soofi 團隊並未追求學習多種語言，而是集中在英語與德語 [出處：[2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424)。特別是在德語部分，訓練數據的佔比經過刻意提高，將德語處理能力發揮到極致 [出處：SOOFI (Soofi S) · innFactory AI Consulting - AI Strategy & Consulting](https://innfactory.ai/en/ai-models/soofi/)。

## 目前應用範疇

Soofi S 是透過學習約 27 兆個 Token（AI 讀取的最小語言單位，類似拼圖碎片）而誕生 [出處：Michael Fromm on X](https://x.com/effi288/status/2075904321707798699)。目前透過 Hugging Face（共享 AI 模型的開源平台），任何人皆可查閱相關模型、訓練程式碼與腳本 [出處：soofi-project · GitHub](https://github.com/soofi-project)。

不過，由於該模型採取完全公開策略，使用者仍需親自根據用途測試數據並確認安全性 [出處：Soofi-Project/Soofi-S-Base · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Base)。因為它與其說是「成品 AI」，更貼近於提供透明基礎的「基礎模型（Foundation model）」。這就像是拿到了工具箱，讓廚師能親自挑選食材、調配食譜。

## 未來展望

由歐洲研究人員開發並將基礎設施保留在歐洲的 Soofi 專案 [出處：Soofi-Project/Soofi-S-Instruct-Preview · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Instruct-Preview)，預計將引領「主權 AI（Sovereign AI，對數據與技術擁有主權的 AI）」的趨勢。這是希望能不依賴特定國家或大型科技企業，以自身的技術打造透明 AI 的決心 [出處：European researchers releaseSoofiS 30B-A3B, a hybrid Mamba MoE...](https://digg.com/tech/rtt1xh5r)。

未來 Soofi 專案計畫持續公開能證明模型效能的詳細基準測試分數 [出處：Soofi-Project/Soofi-S-Rhine-Preview · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Rhine-Preview)。我們距離那個能從原始碼層面證明 AI 是否聰明、是否值得信賴的時代，又更近了一步。

## MindTickleBytes 的 AI 記者觀點
隨著 AI 變得越來越聰明，人們開始感到恐懼：「這傢伙到底在想什麼？」Soofi 正以「透明度」這一技術解方來化解這種恐懼。一個開發過程全然透明的 AI，究竟能在社會中獲得多少信任，著實令人期待。

## 參考資料
1. [2607.09424] A Sovereign, Open-Source Foundation Model for German and English (https://arxiv.org/abs/2607.09424)
2. Soofi-Project/Soofi-S-Base · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Base)
3. SOOFI (Soofi S) · innFactory AI Consulting - AI Strategy & Consulting (https://innfactory.ai/en/ai-models/soofi/)
4. soofi-project · GitHub (https://github.com/soofi-project)
5. Soofi-Project (Sovereign Open Source Foundation Models) (https://huggingface.co/Soofi-Project)
6. Soofi-Project/Soofi-S-Rhine-Preview · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Rhine-Preview)
7. Soofi-Project/Soofi-S-Instruct-Preview · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Instruct-Preview)
8. Soofi:Completetrainingcodeforanopen-sourcefoundationmodel (https://modernorange.io/item/48918292)
9. SoofiS 30B activates 3B parameters per token, tops... | UncensoredHub (https://uncensoredhub.ai/news/2026-07-13-soofi-s-30b-activates-3b-parameters-per-token-tops-european-ai-baselines)
10. SoofiS: A SovereignFoundationModelfor German and English (https://www.emergentmind.com/videos/sovereign-open-source-bilingual-llm-cef87c5b)
11. European researchers releaseSoofiS 30B-A3B, a hybrid Mamba MoE... (https://digg.com/tech/rtt1xh5r)
12. Michael Fromm on X (https://x.com/effi288/status/2075904321707798699)