---
layout: post
title: "AI 撰寫的使用說明書，真的能信嗎？：全新考驗『DoGBench』登場"
description: "透過評估 AI 軟體文件撰寫能力的首個基準測試 DoGBench，一探 AI 實際的技術文件寫作實力。"
summary: "用於評估 AI 撰寫與維護使用者導向軟體文件能力的指標性基準測試 DoGBench 已經問世，然而目前竟無任何 AI 模型得分超過 50%。"
tags: [AI, 軟體工程, DoGBench, 技術洞察]
image: 2026-10-13-DoGBench-The-first-user-facing-docs-generation-benchmark-No-model-scores-50.jpg
image_alt: "一名 AI 代理在複雜的軟體程式碼與文件串聯的數位螢幕前苦思的插畫"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "應對 AI 文件撰寫能力的過度樂觀持保留態度。同時兼顧技術準確性與讀者理解度的「專家級文件撰寫」，對 AI 而言仍是一項艱鉅的挑戰。"
quiz:
  - question: "DoGBench 是為了評估什麼而建立的基準測試？"
    choices: ["AI 的程式碼撰寫速度", "AI 撰寫與維護使用者導向軟體文件的能力", "AI 的數學問題解決能力"]
    answer: 1
    explanation: "DoGBench 旨在評估 AI 能否以專家水準撰寫並維護實際使用者所需的軟體文件。"
  - question: "目前是否有 AI 模型在 DoGBench 中取得 50% 以上的分數？"
    choices: ["有，部分模型超過 80%。", "沒有，目前沒有任何模型超過 50%。", "所有模型都獲得了 100% 的分數。"]
    answer: 1
    explanation: "截至目前為止，尚未有任何 AI 模型在 DoGBench 中獲得 50% 以上的分數。"
  - question: "DoGBench 的評估標準是如何設定的？"
    choices: ["透過隨機抽取的普通民眾投票", "參考專業技術作家與專案經理的標準", "由 AI 自行評分"]
    answer: 1
    explanation: "評估標準（rubrics）是根據實際專案經理與專業技術作家可接受的準則進行校準的。"
lang: zh-tw
ref: 2026-10-13-DoGBench-The-first-user-facing-docs-generation-benchmark-No-model-scores-50
---

試想一下，當你安裝了新購買的軟體更新，滿懷期待地打開使用說明書時，卻發現說明與實際程式碼完全不符，或是充斥著讓人摸不著頭緒的句子，你會作何感想？我們經常說：「現在 AI 什麼都會寫，技術作家（Technical Writer）的時代已經結束了。」但事實真的如此嗎？

近期，AI 業界出現了一個挑戰這種樂觀觀點的有趣試金石。這就是專門衡量軟體文件撰寫與維護能力的基準測試——**DoGBench (Documentation Generation Benchmark)**。

## 為何這件事很重要？

使用者導向的軟體文件不僅僅是功能的條列。它需要將複雜的技術內容轉化為一般使用者易於理解的語言，且每當程式碼變更時，文件也必須同步更新。如果文件過時或錯誤，使用者將面臨極大的困擾。

為了節省成本，開發團隊有時會出現將這項工作完全交給 AI 的趨勢。例如，知名企業如 Snowflake 等解僱技術作家團隊並強制推行 AI 導入的案例，就引發了巨大爭議 [[出處: DoGBench 官方網站](https://dogbench.ai/)] [[出處: DoGBench 基準測試相關討論](https://bhn.vercel.app/post/49928118)]。然而，過去一直缺乏合適的考卷來驗證 AI 是否真能撰寫出專家級的文件。DoGBench 正是為了填補這項「空白」而生，對於現場的實務工作者來說，是一項必備的工具 [[出處: DoGBench 簡介(arXiv)](https://arxiv.org/html/2609.39909)]。

## 簡單易懂的解釋

我們可以如何比喻 DoGBench 的作用呢？假設我們有一位「廚師（AI）」。讓剛學會基本功的廚師負責一家由挑剔的「美食家（專案經理與專業技術作家）」組成的餐廳，正是目前的現狀。

DoGBench 就像是完美還原了這家餐廳的廚房現場：

1. **提供情境**：以特定時間點的軟體程式碼狀態作為固定快照提供 [[出處: GitHub - Promptless/dogbench](https://github.com/Promptless/dogbench)]。
2. **指派任務**：拋出課題，例如：「此功能已更動，請更新文件」或「此處說明不足，請撰寫新文件」 [[出處: GitHub - Promptless/dogbench](https://github.com/Promptless/dogbench)]。
3. **專家審核**：由管理實際專案的老手們檢視 AI 撰寫的文件，並採用 Rubrics（評分標準）來評價，判斷是「這對我們的使用者來說寫得很棒（合格）」還是「內容寫得太複雜（不合格）」 [[出處: DoGBench 官方網站](https://dogbench.ai/)] [[出處: DoGBench 論文(arXiv)](https://arxiv.org/abs/2609.39909)]。

簡單來說，這就像是一場「論述考試」，不僅數學題目要對，連邏輯論述過程也必須通過評分者的標準。

## 現況：目前仍是「不及格」

那麼，現今最強大的 AI 模型表現如何？遺憾的是，結果非常冷酷。目前沒有任何 AI 模型能在 DoGBench 中取得 50% 以上的分數 [[出處: Vue HN 2.0](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49928118)] [[出處: DoGBench 官方網站](https://dogbench.ai/)]。

這也證明了許多人過去高估了 AI 的文件撰寫能力。AI 雖然擅長生成像樣的句子，但在精準理解程式碼脈絡、根據使用者視角撰寫精確且有用的指南方面，仍無法取代專家之手。

## 未來走向如何？

DoGBench 的出現傳遞了一個重要訊息。與其草率得出 AI 無所不能的結論，它更像是一個契機，讓我們開始思考「如何填補 AI 的不足並進行改善」。

未來，AI 模型不僅要提升語言流暢度，更需深入理解實務中運作的複雜程式碼生態系統，並朝著學習專業人士的文筆與邏輯結構方向發展。觀察「文件撰寫效能」是否會成為 AI 業界新的競爭指標，將會是非常有趣的事。

## AI 的觀點：MindTickleBytes AI 記者的觀點

「AI 寫得出好文章，與『寫出讓使用者容易理解的使用說明書』是完全不同層次的問題。DoGBench 的低分顯示，AI 技術距離完全取代『技術作家』這類熟練專家，仍有一段漫長的路要走。AI 不過是一位剛學會走路的初學者，我們應該給予這位作者更細緻的指導。」

## 參考資料

1. [DoGBench: Can Agents Meet Expert Standards for User-Facing Documentation?](https://dogbench.ai/)
2. [Vue HN 2.0 | DoGBench: The first user-facing docs generation benchmark...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49928118)
3. [DoGBench: Can Agents Meet Expert Standards for User-Facing Documentation? (arXiv)](https://arxiv.org/html/2609.39909)
4. [GitHub - Promptless/dogbench](https://github.com/Promptless/dogbench)
5. [DoGBench: The first user-facing docs generation benchmark. No model scores > 50% (VK)](https://vk.ru/wall-238001904_6746)
6. [DoGBench: Can Agents Meet Expert Standards for User-Facing Documentation? (Abstract)](https://arxiv.org/abs/2609.39909)
7. [DoGBench: Can Agents Meet Expert Standards for User-Facing Documentation? (PDF)](https://arxiv.org/pdf/2609.39909)
8. [DoGBench: The first user-facing docs generation benchmark. No model scores > 50% (Vercel)](https://bhn.vercel.app/post/49928118)
9. [DoGBench: The first user-facing docs generation benchmark. No model scores > 50% (int2inf)](https://hb.int2inf.com/en/s/item/YbQ72bpDgnXoyo7h3xWS2M-dogbench-documentation-agent-benchmark)