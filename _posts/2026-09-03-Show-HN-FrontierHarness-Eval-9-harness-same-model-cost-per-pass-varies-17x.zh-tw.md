---
layout: post
title: "把編碼工作交給 AI，成本竟然差了 17 倍？揭開「Harness」的秘密"
description: "研究結果顯示，即便是使用相同的 AI 模型，根據所採用的編碼代理系統（Harness），成本差距竟高達 17.5 倍。"
summary: "針對 9 種 AI 編碼代理系統進行相同模型的測試，結果顯示雖然性能相近，但運作成本差距最高可達 17.5 倍。"
tags: [AI, 編碼, 成本節約, 生產力, 技術趨勢]
image: 2026-09-03-Show-HN-FrontierHarness-Eval-9-harness-same-model-cost-per-pass-varies-17x.jpg
image_alt: "可視化 AI 系統執行複雜編碼工作的圖形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這表明不僅是 AI 模型的智慧，用來運作模型的「系統設計（Harness）」對成本效率也起到了決定性的作用。"
quiz:
  - question: "在本研究比較 9 種 AI 編碼系統時，哪一項不是固定不變的因素？"
    choices: ["AI 模型", "軟體工程任務", "系統運作成本"]
    answer: 2
    explanation: "研究的核心在於測量當模型、任務與執行環境固定時，成本會如何變動。"
  - question: "透過更換 AI 編碼 Harness，下列哪一項不是可能改變的因素？"
    choices: ["任務成功率", "快取動作方式", "AI 模型的基本智慧"]
    answer: 2
    explanation: "Harness 僅是用於控制模型的方式，並不會提升模型本身的智慧。"
  - question: "執行相同任務時，根據 Harness 設定，成本差距最高達到了幾倍？"
    choices: ["約 5 倍", "約 17.5 倍", "約 30 倍"]
    answer: 1
    explanation: "研究結果顯示，在 12 種設定下，成本差距最高達到了 17.5 倍。"
lang: zh-tw
ref: 2026-09-03-Show-HN-FrontierHarness-Eval-9-harness-same-model-cost-per-pass-varies-17x
---

想像一下，你聘請了兩位聰明的秘書。兩位都在同一所大學接受同樣的教育，擁有相同的業務處理能力。然而，如果其中一人完成工作要花費 1 萬元，而另一人處理同樣的工作卻要花費 17 萬 5 千元，你會怎麼辦？

最近在人工智慧（AI）編碼領域出現了一個有趣的現象，就與此情況極為相似。隨著 AI 模型變得越來越聰明，委託其進行編碼工作的需求也變得普及，但研究揭示，根據處理該任務的「方式」，成本會有天壤之別。

## 為什麼這很重要？

企業或開發者在利用 AI 開發軟體時，最重要的因素無疑是「成本」與「結果」。過去我們只專注於「哪個 AI 模型更聰明？」，但現在，更高效地駕馭這些模型變得更加重要。如果有方法能讓 AI 在維持相同性能的同時節省超過 17 倍的成本，企業的生產力將會產生質的飛躍。

## 簡單理解：什麼是 Harness？

「Harness」（譯為編碼框架或測試夾具）這個術語可能讓你感到陌生。簡單來說，你可以將其視為**將 AI 模型投入編碼工作現場並進行管理的「系統殼層」**。

讓我們這樣比喻：
- **AI 模型**：具備卓越實力的「天才開發者」。
- **Harness**：為該開發者準備工具（電腦、參考書籍、搜尋工具等）、下達指令並確認產出成果的「專案經理」。

本次研究（[FrontierHarness Eval](https://frontierharness.org/)）分析了即便聘請了同一位天才開發者（相同的 AI 模型），根據負責管理的專案經理（Harness）不同，工作處理方式與花費成本會有何種差異。研究團隊動用了 9 種不同的 Harness，讓它們執行 30 個相同的軟體工程任務。[參考：Introducing FrontierHarness Eval — RUNTA](https://runta.com/blog/introducing-frontier-harness-eval/)

研究結果顯示，即使在模型與任務環境保持相同的情況下，根據 Harness 設定的不同，成功率、執行速度與快取（暫存資料）使用方式也大相徑庭。[參考：GitHub - frontier-harness-eval/eval](https://github.com/frontier-harness-eval/eval)

## 現況：成本差距達 17.5 倍

這項研究最令人震驚的結果是成本。研究團隊比較了 12 種 Harness 設定，結果顯示即使是相同的任務，成本差距竟然高達 **17.5 倍**。[參考：Samemodel. Similarpassrates. 17.5xcostdifferences across 12...](https://frontierharness.org/)

也就是說，委託同樣的編碼工作，根據使用的系統不同，原本只需花費 1 萬元的工作，最後可能會變成花費 17 萬 5 千元。這顯示單純模型聰明並不能解決所有問題。根據 Harness 的設計方式，AI 的判斷力會受到影響，透過減少不必要的提問，可以有效節省成本。[參考：GitHub - runta-dev/frontier-harness](https://github.com/runta-dev/frontier-harness)

## 未來走向？

這次的結果為生活在 AI 時代的我們提供了重要的啟示。未來，競爭將超越單純尋找「性能強大的 AI 模型」，轉向如何以最少動作實現最佳成果的「高效設計」競爭。

對使用者而言，在使用 AI 時，除了關注「這個模型有多聰明？」，現在還必須審視「這個 AI 運作的系統（Harness）有多高效？」。隨著該領域的研究愈發活躍，我們將迎來一個能以更低廉成本、更快速開發出更優質軟體的時代。

## MindTickleBytes 的 AI 記者觀點

AI 的智慧歸功於模型本身，但運用這些智慧並優化成本，則是人類的職責。這就如同有些經理聘請了聰明的人才，卻只讓對方處理大量的冗餘文書工作；而有些經理則能透過明確的指引，最大化工作效率。隨著技術日趨高深，最終決定企業與個人競爭力的，將會是駕馭系統的「運作智慧」。

## 參考資料

1. [Samemodel. Similarpassrates. 17.5xcostdifferences across 12...](https://frontierharness.org/)
2. [GitHub - runta-dev/frontier-harness-eval: Public results and task...](https://github.com/runta-dev/frontier-harness-eval)
3. [Introducing FrontierHarness Eval — RUNTA](https://runta.com/blog/introducing-frontier-harness-eval/)
4. [GitHub - frontier-harness-eval/eval: Public results and task ...](https://github.com/frontier-harness-eval/eval)
5. [GitHub - runta-dev/frontier-harness: Public results and task ...](https://github.com/runta-dev/frontier-harness)
6. [Show HN: FrontierHarness Eval – 9 种评测方案，同一模型，单次成本...](https://memedata.com/post/143010)
7. [HackerNews– Telegram](https://t.me/hackernewslive/231515)