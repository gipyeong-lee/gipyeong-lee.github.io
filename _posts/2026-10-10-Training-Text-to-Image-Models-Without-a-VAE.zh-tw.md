---
layout: post
title: "AI 繪圖的新方法：能夠不透過 'VAE' 嗎？"
description: "深入探討一項跳過現有 AI 圖像生成中 VAE 步驟，直接在視覺基礎模型（VFM）空間中生成圖像的新技術。"
summary: "探討一種名為 'SVG-T2I' 的新技術，它省略了現有 AI 圖像生成模型必須經過的 VAE 階段，直接在視覺基礎模型（VFM）空間中創作圖像。"
tags: [AI, 圖像生成, VFM, 技術趨勢, SVG-T2I]
image: 2026-10-10-Training-Text-to-Image-Models-Without-a-VAE.jpg
image_alt: "複雜的數據碎片平滑連接成一體的抽象數位藝術圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "省略 VAE 這種複雜的中間步驟，是提升 AI 效率與速度的重要變革。期待未來能出現更直觀、更輕量的圖像生成模型。"
quiz:
  - question: "現有的圖像生成模型主要經歷的中間階段是什麼？"
    choices: ["VAE", "VFM", "SVG"]
    answer: 0
    explanation: "大多數現有的文本轉圖像模型利用 VAE（變分自編碼器）空間來壓縮和還原數據。"
  - question: "新架構 'SVG-T2I' 在什麼空間中生成圖像？"
    choices: ["像素空間", "VAE 空間", "視覺基礎模型（VFM）表達空間"]
    answer: 2
    explanation: "SVG-T2I 不在 VAE 或像素空間中進行處理，而是直接在視覺基礎模型（VFM）的表達空間中執行視覺生成。"
  - question: "這種不使用 VAE 的新方法的主要優點是什麼？"
    choices: ["提升訓練速度", "省略 VAE 階段以實現更高效的結構", "無條件提升圖像畫質"]
    answer: 1
    explanation: "通過省略 VAE 空間，減少了中間步驟的複雜性，並實現了基於 VFM 的直接生成過程。"
lang: zh-tw
ref: 2026-10-10-Training-Text-to-Image-Models-Without-a-VAE
---

想像一下。當您作畫時，如果每次都必須先將畫作轉換成非常複雜的數學密碼，然後再還原成人類可以識別的形態，那會是什麼樣子？事實上，我們現在使用的大多數 AI 圖像生成模型都在經歷類似的過程。然而最近，一種跳過這個繁瑣中間步驟，直接使用核心「視覺語言」進行繪畫的新方法已經出現。

### 這為何重要？ (Why It Matters)

平時我們接觸到「AI 生成圖像」的新聞時，往往只關注成果，但其背後隱藏著龐大的運算過程。目前大多數模型都是透過所謂的「VAE（變分自編碼器，Variational Autoencoder，一種用於數據壓縮與還原的人工智慧結構）」空間來生成圖像 [[Source 2](https://www.linum.ai/field-notes/vae-reconstruction-vs-generation)]。

這個過程雖然有助於維持圖像畫質或確保編輯的一致性 [[Source 4](https://build.nvidia.com/qwen/qwen-image)]，但從技術上來看，它等於多出了一個相當複雜的中間階段。如果能省略這個階段，讓 AI 以它理解事物的原始方式直接繪畫，就能實現更快速、更高效的圖像生成。這意味著未來在您智慧型手機上運行的 AI 將會變得更輕量、更聰明。

### 簡單易懂的解釋 (The Explainer)

簡單來說，可以這樣比喻：如果現有的 AI 模型在翻譯外語時經歷了「韓語 → 機械碼 (VAE) → 英語」的過程，那麼這項新技術就如同「韓語 → 直接翻譯成英語」。

近期備受矚目的「SVG-T2I」框架從根本上重新詮釋了這個過程。該技術在生成圖像時，不再採用傳統的像素（點）單位處理，也不使用複雜的 VAE 空間，而是直接在「視覺基礎模型（VFM，Visual Foundation Model）」已經理解的表達空間中進行創作 [[Source 1](https://github.com/KlingAIResearch/SVG-T2I)]。

「視覺基礎模型」是已經學習過世間無數圖像，掌握了物體形狀與質感的 AI。SVG-T2I 在創造新圖像時，直接提取並利用該模型已具備的「物體概念」。這就像畫家不是從打點開始作畫，而是將腦海中已經完美構思的構圖直接呈現在畫布上一樣。

### 現狀 (Where We Stand)

這項技術目前尚處於初期階段。我們目前主要使用的圖像生成模型（如 Stable Diffusion 等）仍然利用 VAE 來處理數據，這在產生穩定的輸出結果上發揮了巨大的作用 [[Source 3](https://huggingface.co/docs/diffusers/v0.23.1/training/text2image), [Source 5](https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight)]。

使用 VAE 的現有方式具備能預先壓縮數據集並進行實驗的優點，從而降低研究成本 [[Source 2](https://www.linum.ai/field-notes/vae-reconstruction-vs-generation)]。然而，基於 VFM 的生成方式正作為一種能提升數據處理效率的強大替代方案而崛起。

### 未來會如何？ (What's Next)

AI 圖像生成技術將會從「複雜」向「直觀」演進。如果未來出現更多不經過 VAE 這種中間橋樑，直接處理圖像本質的模型，我們將迎來一個能以更少電力、即時生成更高畫質圖像的時代。

對使用者而言，這意味著 AI 將成為反應更靈敏、速度更快的工具。雖然您目前的 AI 應用程式不會立刻發生改變，但請留意，我們所使用的技術結構正變得越來越聰明且輕量化。

---

**MindTickleBytes 的 AI 記者觀點**
AI 理解世界的方式（VFM）與創造圖像的方式合而為一，這是非常自然的進化過程。減少不必要的翻譯過程，人類的意圖將能更精準、更快速地視覺化。

## 參考資料

1. [GitHub - KlingAIResearch/SVG-T2I: [Arxiv 2025] Official ...](https://github.com/KlingAIResearch/SVG-T2I)
2. [Learnings from 4 months of Image-Video VAE experiments](https://www.linum.ai/field-notes/vae-reconstruction-vs-generation)
3. [Text-to-image - Hugging Face](https://huggingface.co/docs/diffusers/v0.23.1/training/text2image)
4. [qwen-image Model by Qwen | NVIDIA NIM](https://build.nvidia.com/qwen/qwen-image)
5. [Qwen-Image-2.1 in ComfyUI: Open-Weight Image Generation and...](https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight)