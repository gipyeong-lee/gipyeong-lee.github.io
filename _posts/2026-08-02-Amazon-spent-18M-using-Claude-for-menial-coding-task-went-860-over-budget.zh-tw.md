---
layout: post
title: "AI 承擔「單純重複工作」卻燒掉 24 億韓元？原因為何？"
description: "透過亞馬遜（Amazon）在使用 AI Claude 的內部專案中，預算超支 860% 並浪費 180 萬美元的事件，探討 AI 導入過程中隱藏的成本與管理的重要性。"
summary: "亞馬遜在利用 AI Claude 進行單純工作自動化的專案中，發生了 5 個月內預算超支 860%，支出達 180 萬美元（約 24 億韓元）卻未能將專案發布的事件。"
tags: [AI, 技術, 亞馬遜, 成本, 自動化]
image: 2026-08-02-Amazon-spent-18M-using-Claude-for-menial-coding-task-went-860-over-budget.jpg
image_alt: "辦公桌上堆積的文件與旁邊放置印有人工智慧標誌的智慧型手機。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "此事件顯示若 AI 模型的「基於 Token 計費」結構未經妥善設計，可能成為巨大的財務黑洞。在引進技術的同時，建立成本追蹤機制是絕對必要的。"
quiz:
  - question: "亞馬遜在此次事件中，投入 AI 自動化專案的費用是多少？"
    choices: ["18 萬美元", "180 萬美元", "860 萬美元"]
    answer: 1
    explanation: "亞馬遜在失敗的 Claude AI 專案中總共支出 180 萬美元。"
  - question: "此 AI 專案超支了多少預算？"
    choices: ["500%", "860%", "1,800%"]
    answer: 1
    explanation: "該專案支出超過原定預算的 860%。"
  - question: "在此專案中，亞馬遜最大的管理疏失之一是什麼？"
    choices: ["AI 模型選擇錯誤", "5 個月內未察覺預算超支", "開發人力不足"]
    answer: 1
    explanation: "亞馬遜在長達 5 個月的時間裡，完全沒有察覺預算超支的情況。"
lang: zh-tw
ref: 2026-08-02-Amazon-spent-18M-using-Claude-for-menial-coding-task-went-860-over-budget
---

想像一下。您以為僱用了一位聰明的實習生，可以在辦公室角落默默幫忙處理文件歸檔。結果 5 個月後確認時，才發現這位實習生不僅沒有處理文件，還把整個辦公室的備品預算超支了 8 倍，而該完成的工作竟然連一件都沒做完，您會是什麼心情？

最近，全球最大電子商務企業亞馬遜（Amazon）確實發生了類似荒謬的事情。這是嘗試利用人工智慧（AI）提升工作效率，結果卻演變成巨大財務黑洞的案例。

### 這為何重要？

此事件不僅是「大企業失誤」的八卦，更清晰地展示了我們該如何看待並引進 AI。許多企業和個人認為只要引進 AI，成本就一定會降低，但此案例警告我們：「若沒有管理的 AI，反而可能成為無法控制的成本怪獸」。

現代 AI 模型是以「Token（代幣）」為單位來計算成本的。可以簡單將 Token 想成 AI 閱讀並理解數據時所使用的最小單位。這就像打開水龍頭使用多少水就付多少錢的方式，若管理疏失，一個小小的失誤就可能導致天文數字般的費用。

### 簡單理解

為什麼會發生這種事？此次專案是亞馬遜內部為了自動化商品數據與作者資訊匹配——即所謂的「單純重複工作」，試圖利用名為「Claude Sonnet」的 AI 模型進行作業 [[參考資料 1](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics), [參考資料 11](https://www.gadgetreview.com/an-amazon-internal-project-used-claude-sonnet-to-match-book-authors-and-accidentally-burned-1-8-million)]。

簡單比喻，就像我們想搭計程車去 5 分鐘路程外的便利商店，但計程車司機走錯路，繞著地球跑了 5 個月並持續累積車資。AI 在燃燒「Token」燃料的同時不斷執行作業，但系統沒有適時停止，導致費用持續產生 [[參考資料 11](https://www.gadgetreview.com/an-amazon-internal-project-used-claude-sonnet-to-match-book-authors-and-accidentally-burned-1-8-million)]。這位「實習生 AI」不僅沒交出正確的成果，專案最終甚至連發布都沒有做到 [[參考資料 4](https://betanews.com/article/amazon-claude-ai-cost-overrun/), [參考資料 8](https://www.ghacks.net/2026/07/31/leaked-amazon-documents-detail-1-8-million-overrun-on-a-single-claude-ai-task-missed-for-five-months)]。

### 目前狀況

根據內部文件，亞馬遜因該專案支出的費用高達 180 萬美元，約合 24 億韓元 [[參考資料 1](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics), [參考資料 9](https://theoutpost.ai/news-story/amazon-s-1-8-million-claude-blunder-exposes-hidden-costs-of-ai-deployments-across-tech-giants-29193/)]。這比原計畫預算超支了 860% [[參考資料 6](https://cybernews.com/ai-news/amazon-spending-ai-claude-cost/), [參考資料 7](https://aiweekly.co/alerts/amazon-engineers-flag-18m-claude-bill-860-over-budget)]。

更令人震驚的是，亞馬遜在長達 5 個月的時間裡，完全沒察覺到這筆驚人的預算浪費 [[參考資料 4](https://betanews.com/article/amazon-claude-ai-cost-overrun/), [參考資料 10](https://www.linkedin.com/posts/vasiliy-radostev-063947_leaked-amazon-documents-detail-18-million-activity-7489089129792696320-fRDT)]。這暗示了巨型企業內部的 AI 管理體系存在巨大漏洞 [[參考資料 11](https://www.gadgetreview.com/an-amazon-internal-project-used-claude-sonnet-to-match-book-authors-and-accidentally-burned-1-8-million)]。

### 未來展望

此案例為許多企業留下了重要的教訓。在引進 AI 時，「成本監控」應先於「技術成果」 [[參考資料 12](https://news.ycombinator.com/item?id=49115075)]。預計未來許多企業將針對 AI 專案導入更嚴格的即時成本追蹤系統。今後，「AI 使用得有多好」與「AI 使用費用管理得有多聰明」，將成為企業的核心競爭力。

### MindTickleBytes AI 記者觀點

此事件不僅僅是亞馬遜浪費金錢的案例，更是展現 AI 便利性背後隱藏「收費陷阱」的象徵性事件。企業在引進 AI 時，必須先建立能夠監控「誰、在何時、何地、消耗多少 Token」的智慧管理系統。因為即使是魔法般的技術，若無法妥善管理，隨時都可能成為掏空錢包的麻煩事。

## 參考資料

1. [Amazon accidentally spent $1.8 million using Claude for menial coding task, went 860% over budget — 'catastrophically expensive' coding blunders discovered in internal Amazon AI usage metrics | Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics)
2. [r/technology on Reddit: Amazon accidentally spent $1.8 million using Claude for menial coding task, went 860% over budget — 'catastrophically expensive' coding blunders discovered in internal Amazon AI usage metrics](https://www.reddit.com/r/technology/comments/1vay198/amazon_accidentally_spent_18_million_using_claude/)
3. [Amazon accidentally spent $1.8 million using Claude for menial coding task, went 860% over budget —'catast...](https://finance.yahoo.com/technology/ai/articles/amazon-accidentally-spent-1-8-160825610.html)
4. [Amazon's $1.8M Claude AI deployment went 860% over budget](https://betanews.com/article/amazon-claude-ai-cost-overrun/)
5. [Amazon accidentally spent $1.8M on a failed Claude AI tokens | Cybernews](https://cybernews.com/ai-news/amazon-spending-ai-claude-cost/)
6. [Amazon Engineers Flag $1.8M Claude Bill, 860% Over Budget | AI Weekly](https://aiweekly.co/alerts/amazon-engineers-flag-18m-claude-bill-860-over-budget)
7. [Leaked Amazon Documents Detail $1.8 Million Overrun on a Single Claude AI Task Missed for Five Months - gHacks Tech News](https://www.ghacks.net/2026/07/31/leaked-amazon-documents-detail-1-8-million-overrun-on-a-single-claude-ai-task-missed-for-five-months/)
8. [8 million on a singleClaudedeployment thatwent860%overbudget.](https://theoutpost.ai/news-story/amazon-s-1-8-million-claude-blunder-exposes-hidden-costs-of-ai-deployments-across-tech-giants-29193/)
9. [LeakedAmazonDocuments Detail $1.8Million Overrun on a Single...](https://www.linkedin.com/posts/vasiliy-radostev-063947_leaked-amazon-documents-detail-18-million-activity-7489089129792696320-fRDT)
10. [AnAmazonInternal ProjectUsedClaudeSonnet to... - Gadget Review](https://www.gadgetreview.com/an-amazon-internal-project-used-claude-sonnet-to-match-book-authors-and-accidentally-burned-1-8-million)
11. [Amazonaccidentallyspent$1.8MusingClaudeforamenialcoding...](https://news.ycombinator.com/item?id=49115075)