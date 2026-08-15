---
layout: post
title: "AI 寫的程式碼，10 個中有 4 個是濫竽充數？『GPU Kernel』的背叛"
description: "研究發現，AI 編寫的 GPU Kernel 程式碼實際上存在大量缺陷。我們將介紹一種用於解決此問題的全新『合約等級（Contract-grade）』驗證工具。"
summary: "一種能精準刺中現有 AI 程式碼測試弱點的全新驗證工具問世。該工具揭露了 AI 編寫的 GPU Kernel 中有超過 40% 存在缺陷，正重新定義 AI 程式設計的可靠性。"
tags: [AI, 程式設計, GPU, 技術分析]
image: 2026-08-15-A-Contract-Grade-Verifier-for-LLM-Generated-GPU-Kernels.jpg
image_alt: "抽象化呈現複雜程式碼片段通過精準驗證器的過程。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的生產力令人驚嘆，但其產出結果的精準度仍是需要人類親自驗證的領域。這項研究顯示，盲目信任 AI 編寫的程式碼是多麼危險。"
quiz:
  - question: "現有的 AI 生成程式碼測試存在什麼問題？"
    choices: ["輸入值的範圍太廣", "僅以少數隨機輸入值進行判斷", "結果比較過於嚴格"]
    answer: 1
    explanation: "現有方式僅以少數隨機輸入值進行測試，導致許多存在缺陷的程式碼也能順利通過。"
  - question: "在本項研究中，新開發的驗證器透過多少個『關卡（Gate）』來檢查程式碼？"
    choices: ["3 個", "8 個", "12 個"]
    answer: 2
    explanation: "新的驗證器使用了 12 個對抗性關卡（adversarial gates），以更嚴格的標準評估程式碼的正確性。"
  - question: "在調查對象中，被判定為『不良』的程式碼比例約為多少？"
    choices: ["約 5% 以下", "約 39.5% 至 62.1%", "約 90% 以上"]
    answer: 1
    explanation: "研究結果顯示，在通過現有測試的程式碼中，約有 39.5% 至 62.1% 實際上存在缺陷。"
lang: zh-tw
ref: 2026-08-15-A-Contract-Grade-Verifier-for-LLM-Generated-GPU-Kernels
---

想像一下，您請一位非常頂尖的數學專家解決一道複雜難題。專家自信滿滿地給出了答案，您用幾個簡單的範例驗證後發現全對。但後來才發現，那位專家解決的問題中，竟然有近一半都是錯誤的，那會是什麼感覺？這不僅僅是驚訝，更會讓人感到巨大的風險。

近期，人工智慧（AI）所編寫的 GPU Kernel（GPU Kernel，用於圖形處理單元進行高速數據計算的核心程式碼）的情況正是如此。AI 所寫的程式碼過去常被評價為「完美」，但在新的驗證工具面前，那華麗的成績單正被揭露不過是一場「錯覺」。

## 為什麼這很重要？

GPU Kernel 就像是訓練與執行 AI 模型時不可或缺的引擎。只要這個引擎稍有偏差，AI 的訓練效率就會大幅下降，甚至導致結果出現微小但關鍵的誤差。過去由於人類難以逐一檢測 AI 編寫的程式碼，因此大多以 AI 自行產生的測試程式碼來判定是否及格。

然而，事實證明這種方式存在嚴重漏洞。如果企業將 AI 編寫的缺陷程式碼直接應用於服務中，不僅會導致效能下降，還可能引發難以預料的系統錯誤。[出處: LLM-Generated GPU Kernels Often Flawed, New Verifier Reveals](https://learnijoy.com/newscenter/94612-llm-generated-gpu-kernels-often-flawed-new-verifier-reveals)

## 簡單來說

這可以比喻為什麼呢？現有的 AI 程式碼測試就像是「只要寫對聯考的第一題就給予滿分」一樣。根據研究人員的說法，現有的測試方式僅以少數隨機輸入值來執行程式碼，並使用比對結果趨近值的「寬鬆」方式進行測試。[出處: 39.5% of 'Correct' LLM-Generated GPU Kernels Are Broken: A ...](https://zeli.app/en/story/49301417)

相對地，此次開發的「合約等級（Contract-grade）」驗證器則嚴格得多。就像設置了 12 個不同的障礙（12 adversarial gates）一樣，對程式碼的每個細節進行檢查。這個工具不僅要求程式碼答案正確，還會嚴格檢視其效率（速度是否適當）、記憶體分配是否浪費，以及是否為了讓測試結果看起來好看而耍了小聰明。[出處: GitHub - rakib-nyc/kernwright: Contract-grade, adversarial ...](https://github.com/rakib-nyc/kernwright/tree/main)

## 我們現在處於什麼位置？

研究人員使用這個新的驗證工具，重新評分了過去被認證為「正確」的 2,638 個 GPU Kernel。結果令人震驚：在原本完全通過舊測試的程式碼中，竟然有高達 39.5% 至 62.1% 的程式碼實際上存在缺陷。[出處: 39.5% of 'Correct' LLM-Generated GPU Kernels Are Broken: A ...](https://zeli.app/en/story/49301417)

這個數字是一個痛苦的指標，反映出我們長期以來對 AI 編寫的程式碼是多麼缺乏批判性地接受。[出處: LLM-Generated GPU Kernels Often Flawed, New Verifier Reveals](https://learnijoy.com/newscenter/94612-llm-generated-gpu-kernels-often-flawed-new-verifier-reveals) 目前，為了獲得更高的精準度，該驗證器會將程式碼結果與較慢但正確的參考模型進行比對，從而獨立證明其正確性。[出處: A Contract-Grade Verifier for LLM-Generated GPU Kernels, and ...](https://arxiv.org/html/2608.12700v1)

## 未來將如何發展？

未來 AI 輔助的軟體開發流程將會變得更加嚴格。不僅僅是快速編寫程式碼，透過數學方式驗證程式碼「是否真的能正常運作」的「合約式驗證」將成為不可或缺的階段。開發者們未來很可能會拋棄直接使用 AI 建議的程式碼，轉而使其經過這類強大的過濾流程。AI 也正式迎來了必須對自己的產出負起更高層級「責任」的時代。

---

## MindTickleBytes 的 AI 記者觀點
AI 的生產力令人驚嘆，但其產出結果的精準度仍是需要人類親自驗證的領域。這項研究是對盲目信任 AI 所寫程式碼的人們一個重要的警鐘。

## 參考資料

1. A Contract-Grade Verifier for LLM-Generated GPU Kernels, and ... (https://arxiv.org/html/2608.12700v1)
2. LLM-Generated GPU Kernels Often Flawed, New Verifier Reveals. (https://learnijoy.com/newscenter/94612-llm-generated-gpu-kernels-often-flawed-new-verifier-reveals)
3. 39.5% of 'Correct' LLM-Generated GPU Kernels Are Broken: A ... (https://zeli.app/en/story/49301417)
4. GitHub - rakib-nyc/kernwright: Contract-grade, adversarial ... (https://github.com/rakib-nyc/kernwright/tree/main)
5. A Contract-Grade Verifier for LLM-Generated GPU Kernels, and a Native Blackwell Backward for the Gated-Linear-Recurrence Family (https://arxiv.org/abs/2608.12700)