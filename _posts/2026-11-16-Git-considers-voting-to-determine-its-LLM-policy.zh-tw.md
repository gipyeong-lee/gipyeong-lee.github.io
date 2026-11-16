---
layout: post
title: "開發者的必備工具 Git，以「投票」決定 AI 使用政策？"
description: "探討開源版本控制系統 Git 為決定大型語言模型（LLM）使用政策而考慮投票的背景，以及開源生態系統中民主化決策的過程。"
summary: "隨著 Git 考慮透過投票程序決定 AI（LLM）使用政策，開源社群正在尋找因應技術變遷的新民主治理模式。"
tags: [Git, LLM, OpenSource, AI Policy, Governance]
image: 2026-11-16-Git-considers-voting-to-determine-its-LLM-policy.jpg
image_alt: "描繪開發者們看著螢幕，並就投票與程式碼編寫進行討論的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "技術變遷越快，制定規則的方式就越需要民主與透明。Git 的這次嘗試將成為開源社群航向 AI 時代的重要里程碑。"
quiz:
  - question: "Git 目前正在考慮的 LLM 政策決定方式為何？"
    choices: ["最高管理層獨家決定", "投票（Voting）程序", "自動化 AI 演算法裁決"]
    answer: 1
    explanation: "Git 正考慮透過投票方式來決定與大型語言模型（LLM）相關的政策。"
  - question: "在某些開源儲存庫（例如 yt-dlp）中，開發人員必須遵守的代表性政策規定為何？"
    choices: ["NO AI / NO LLM POLICY", "所有程式碼由 AI 自動生成", "全面禁止商業使用"]
    answer: 0
    explanation: "部分開源專案要求貢獻者在提交時確認並遵守「NO AI / NO LLM POLICY」。"
  - question: "在開源生態系統中，建立政策與價值觀為何重要？"
    choices: ["為了加快軟體建置速度", "為了在社會與技術變遷中尋找適當的方向", "為了降低伺服器成本"]
    answer: 1
    explanation: "隨著社會與技術環境的變遷，我們必須系統性地探索並識別適當的政策與價值觀。"
lang: zh-tw
ref: 2026-11-16-Git-considers-voting-to-determine-its-LLM-policy
---

想像一下，在全世界數千萬名開發者每天都在使用的核心工具中，我們必須訂定如何在編寫程式碼時使用人工智慧（AI）的規則。如果要讓這個重要決定不由少數管理者在密室中做出，而是透過整個社群的「投票」來決定，那會是怎樣的情形？最近，全球開發者社群中出現了一個令人矚目的有趣動向：版本管理系統的標準 Git 為了制定與大型語言模型（LLM，Large Language Model，透過學習海量文字來像人類一樣撰寫文章與程式碼的 AI 技術）相關的政策，正考慮採用投票方式來決定 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

---

## 為什麼這很重要？

在軟體開發的世界裡，「Git」就像是管理建築物設計圖的公認檔案庫。任何人都可以透過這個檔案庫修改程式碼、新增功能，並與全世界的人協同合作。這是任何學習電腦科學或程式編寫的人都必須掌握的必備基礎知識 [[Source 2](https://www.youtube.com/watch?v=Yi5Y2_r0t9Y)]。如果打個比方，它就像是「國民圖書館」，當全世界無數的廚師共同修改一本巨大的食譜時，它能以零誤差記錄並管理每一次的修改歷程。

然而，隨著近年生成式 AI 的爆炸性成長，全球開發現場陷入了巨大的混亂。因為大家對於是否能直接拿 AI 寫好的程式碼來用、AI 產生的程式碼是否存在版權問題，或是在專案貢獻過程中允許使用 AI 到什麼程度，都沒有明確的標準。事實上，部分開源專案（例如以影片下載工具聞名的 yt-dlp 等）甚至要求貢獻者在提交程式碼或 Issue 時，必須勾選確認「我已閱讀 AI 使用政策（NO AI / NO LLM POLICY），並了解違反此政策可能會被儲存庫封鎖」的清單 [[Source 3](https://github.com/yt-dlp/yt-dlp/issues/17585)]。 

在這種情況下，像 Git 這樣核心的基礎設施專案竟然搬出「投票」這種民主程序來制定 AI 政策，意味著這可能成為未來無數開源專案建立 AI 時代規則的標準前例 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

---

## 輕鬆理解：制定規則的民主實驗

我們可以這樣比喻：想像一下，在一棟公寓大樓裡，居民們聚在一起制定飼養寵物的指南。有些人完全歡迎寵物，有些人則希望有嚴格的限制。如果此時管理處主任獨斷專行地訂定規則，居民們肯定會反彈。相反地，如果透過所有住戶參與的投票來決定規則，那麼大家對於結果就很容易心服口服。

Git 想要做的事也很類似。當技術發展速度太快且各方立場分歧時，這是一個探討社會成員該如何針對 AI 所帶來的政治、倫理影響力或偏見問題達成共識的過程 [[Source 5](https://arxiv.org/pdf/2410.24190)]。開源生態系統本來就是透過自發性參與和討論發展而來的，但在 AI 這道巨大浪潮面前，它正式將透明詢問並決定社群意願的制度化裝置（投票程序）搬上了檯面 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

從更廣闊的視角來看，這與民主社會在面對新技術時尋找適當政策與價值觀的過程如出一轍。正如社會成員必須依據各種指標來分析潛在結果並尋求更好的方向一樣，開發者社群也同樣正在技術變遷中實驗著系統化的決策結構 [[Source 15](https://iclr-blogposts.github.io/2025/blog/llm-democracy/)]。

---

## 現狀：我們走到哪裡了？

目前的軟體發展生態系統正經歷著激烈的變革期。隨著大型程式碼託管平臺的政策轉變，以及探討去中心化服務替代方案的呼聲日益高漲 [[Source 10](https://dbushell.com/2026/04/29/github-is-sinking/)]，作為開發工具基石的 Git 社群內部，對於是否接受 AI 也存在著正反兩方的爭論。 

一方面有人主張應充分利用 AI 來最大化生產力；另一方面則以程式碼品質、授權污染、資安風險等理由，要求進行嚴格的管制或限制。正是在這個階段，各方不再試圖以強權壓制或將這種衝突模糊處理，而是透過明確的投票程序來確立官方政策，相關討論已經正式展開 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

---

## 未來將如何發展？

Git 最終將採取哪種投票方式、確定什麼樣的 LLM 政策，正吸引著全球開源社群的高度關注。如果透過投票來決定政策的模式能夠成功落地，那麼其他無數的開源專案很有可能也會引入類似的治理模型。 

開發者將來能夠在透明公開的規則中，明確了解自己所貢獻的專案會以什麼標準來審查和接受由 AI 撰寫的程式碼。這可以說是由 Git 為我們上了一課：隨著技術的進步，制定規則的方式也必須跟著進化 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)]。

---

## 參考資料

1. [Git considers voting to determine its LLM policy](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/)
2. [We Need To Stop Lying About Git - YouTube](https://www.youtube.com/watch?v=Yi5Y2_r0t9Y)
3. [ok.ru not downloading any video · Issue #17585 · yt-dlp/yt-dlp · GitHub](https://github.com/yt-dlp/yt-dlp/issues/17585)
4. [Hidden Persuaders: LLMs’ Political Leaning and Their Influence on...](https://arxiv.org/pdf/2410.24190)
5. [Welcome to LWN.net [LWN.net]](https://lwn.net/)
6. [GitHub is sinking – David Bushell – Web Dev (UK)](https://dbushell.com/2026/04/29/github-is-sinking/)
7. [LLMs' Potential Influences on Our Democracy: Challenges and...](https://iclr-blogposts.github.io/2025/blog/llm-democracy/)