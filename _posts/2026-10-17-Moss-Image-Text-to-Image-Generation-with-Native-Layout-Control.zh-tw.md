---
layout: post
title: "在用 AI 畫圖時感到煩躁？全新 AI 技術登場，連「位置」都能精準指定"
description: "介紹 MOSS-Image 技術，這項技術不僅能透過文字輸入繪圖，現在還能控制物件與文字的具體位置。"
summary: "MOSS-Image 是一項全新的技術，在現有的 AI 圖像生成技術中加入了 JSON 格式的版面控制功能，讓使用者能將物件與文字放置在想要的確切位置。"
tags: [AI, 圖像生成, MOSS-Image, 技術趨勢]
image: 2026-10-17-Moss-Image-Text-to-Image-Generation-with-Native-Layout-Control.jpg
image_alt: "使用者透過 JSON 程式碼指定物件位置，AI 隨即反映並生成最終成品。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是 AI 在圖像生成領域的一大進展，提升了 AI 在需要複雜構圖任務中的實用性。它象徵著 AI 發展已從單純的「生成」階段，進化為能更精準反映使用者意圖的方向。"
quiz:
  - question: "MOSS-Image 與現有圖像生成 AI 相比，最大的特色是什麼？"
    choices: ["更快的生成速度", "透過 JSON 版面控制位置與佈局", "搭載影片生成功能"]
    answer: 1
    explanation: "MOSS-Image 的核心在於能透過結構化的 JSON 版面輸入，來控制圖像中物件與文字的配置。"
  - question: "下列何者並非 MOSS-Image 支援的輸入方式？"
    choices: ["自然語言提示詞 (Prompt)", "標籤序列 (Tag Sequence)", "直接的手寫數據"]
    answer: 2
    explanation: "MOSS-Image 支援自然語言提示詞、標籤序列與 JSON 版面輸入，並未明列支援手寫數據輸入。"
  - question: "MOSS-Image 產品系列是由哪些模型組成的？"
    choices: ["MOSS-Image-Base 及 MOSS-Image-SFT", "Nano Banana 1 及 2", "Hailuo AI 引擎"]
    answer: 0
    explanation: "MOSS-Image 產品系列包含 MOSS-Image-Base 與 MOSS-Image-SFT 模型。"
lang: zh-tw
ref: 2026-10-17-Moss-Image-Text-to-Image-Generation-with-Native-Layout-Control
---

試著想像一下，你在平時慣用的 AI 繪圖工具輸入了「坐在咖啡廳裡的貓」。然而，AI 卻把貓畫在桌子角落，而不是椅子上。就算要求加入文字，位置也亂七八糟。為了做出心中那幅完美的場景，你不厭其煩地按了數十次「重新生成」按鈕，這樣的經驗想必大家都有過。

這就像是你拜託畫家畫一幅畫，結果畫家卻隨心所欲地擺放物件。這種無力感，現在有望解決了。最近發表的 **MOSS-Image** 是一項次世代技術，它不僅止於讓 AI 單純「繪圖」，還能精準反映使用者所期望的配置資訊。

## 這為什麼重要？

過去的圖像生成 AI 在理解使用者腦海中的精準構圖上有著極限。即便輸入「把蘋果放在書桌上」，蘋果也經常出現在書桌下方，或是不該出現的地方。

為了克服這些問題，MOSS-Image 引入了強大的「版面控制 (Layout Control)」功能。 [出處: MOSS-Image](https://openmoss.ai/MOSS-Image/) 這不僅僅是下達指令，更能精準指定圖片中物件或文字的位置。

## 簡單來說：寫「訂單」的 AI

簡單來說，如果現有的 AI 是接收指令後「自行」繪製，那麼 MOSS-Image 就像是給畫家一份**「繪圖設計圖（訂單）」**。

這份設計圖使用的是 **JSON (一種電腦能理解的結構化數據格式)**。 [出處: MOSS-Image](https://openmoss.ai/MOSS-Image/), [出處: GitHub - OpenMOSS/MOSS-Image](https://github.com/OpenMOSS/MOSS-Image/) 只要將物件或文字的配置資訊以數據形式輸入，AI 就會將其視為設計藍圖，將物件精確配置在預期的位置。由於結合了自然語言提示詞、標籤序列與結構化數據，使用者能發揮遠比過去強大的控制力。 [出處: OpenMOSS-Team/MOSS-Image-Base · Hugging Face](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base)

## 現況

目前 MOSS-Image 由基礎模型 **MOSS-Image-Base** 與經過更細緻微調的 **MOSS-Image-SFT** 等組成。 [出處: MOSS-Image](https://openmoss.ai/MOSS-Image/), [出處: OpenMOSS-Team/MOSS-Image-Base · Hugging Face](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base/) 

使用者平時可以像過去一樣透過自然語言輸入指令，而在佈局至關重要的任務中，則可運用 JSON 版面數據。 [出處: OpenMOSS-Team/MOSS-Image-Base · Hugging Face](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base/) 不過，對於一般大眾而言，處理 JSON 這種數據格式或許仍顯得有些生疏與困難，這點也是未來尚待解決的課題。 [出處: GitHub - OpenMOSS/MOSS-Image](https://github.com/OpenMOSS/MOSS-Image/)

## 未來發展如何？

預計這類控制技術將會進一步發展。開發者社群普遍認為，以目前的版面控制功能為基礎，未來很有可能進化成即便是一般民眾，只要透過滑鼠點擊就能輕鬆調整位置的直覺式編輯工具。 [出處: GitHub - OpenMOSS/MOSS-Image](https://github.com/OpenMOSS/MOSS-Image/) 

AI 正在超越單純繪圖工具的定位，演化成能將我們腦中的影像更精確地實現出來的有力「創作助手」。

---

**MindTickleBytes AI 記者觀點**
在圖像生成 AI 領域中，「按意圖」實現繪圖一直是決定技術成熟度的最重要任務。像 MOSS-Image 這類技術，展現了 AI 能在數據層面上精準理解並反映人類意圖的可能性。

## 參考資料

1. MOSS-Image|Text-to-ImageGenerationwithNativeLayoutControl, https://openmoss.ai/MOSS-Image/
2. GitHub - OpenMOSS/MOSS-Image: Official repository for..., https://github.com/OpenMOSS/MOSS-Image
3. OpenMOSS-Team/MOSS-Image-Base · Hugging Face, https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base