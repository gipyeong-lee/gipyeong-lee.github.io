---
layout: post
title: "AI 代理程式編寫程式碼的時代，為何 20 年歷史的 'Git' 基礎建設已達極限？"
description: "AI 代理程式頻繁儲存程式碼導致現有 Git 基礎建設面臨瓶頸。GitHub 等主要服務正如何調整儲存庫結構以解決此問題，我們將為您深入淺出地說明。"
summary: "為了應對 AI 代理程式爆發性的活動量，GitHub 等服務正針對代理程式規模，從底層重新設計原本以人為中心的 Git 基礎建設。"
tags: [AI, Git, GitHub, 開發工具, 基礎建設]
image: 2026-10-12-Building-Git-infrastructure-for-agent-scale-development.jpg
image_alt: "象徵資料中心伺服器與複雜數位網路連接的影像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "隨著 AI 代理程式成為開發主體，人類過去創建的「工具」本身正面臨根本性的變革。這不僅是單純的效能提升，更是軟體開發模式全面邁向自動化時代的信號彈。"
quiz:
  - question: "現有 Git 基礎建設不適合 AI 代理程式開發的主要原因為何？"
    choices: ["因為安全上的漏洞", "因為是針對以人為中心的流程（分支、PR 等）所設計", "因為與雲端服務不相容"]
    answer: 1
    explanation: "傳統的 Git 是為了開發者修改程式碼、建立分支並發送 PR 的人類中心流程而設計的。"
  - question: "GitHub 新的 Git 儲存庫結構在初步測試中展現了多少效能提升？"
    choices: ["5 倍", "15 倍", "35 倍"]
    answer: 2
    explanation: "GitHub 的新架構在初步內部測試中，展現了比過去快 35 倍的寫入效能改善。"
  - question: "程式碼編輯器 'Cursor' 自行開發的 'Origin' 是透過何種方式來優化效能？"
    choices: ["區塊鏈技術", "基於 WAL (Write-Ahead Logging) 的 S3 儲存", "資料壓縮技術"]
    answer: 1
    explanation: "Cursor 在 S3 上建構了 WAL (Write-Ahead Logging，預寫式記錄) 系統，解決了現有 Git 託管的問題。"
lang: zh-tw
ref: 2026-10-12-Building-Git-infrastructure-for-agent-scale-development
---

想像一下。您早上起床後對 AI 說：「今天把所有需要的網站功能都實作出來。」AI 代理程式隨即開始工作。然而，這個代理程式的工作方式與人類完全不同。它幾乎在每個微小的動作中都會儲存（Commit）程式碼並留下紀錄。就像我們吃飯呼吸一樣自然，AI 不斷地在儲存程式碼。

然而，我們使用了超過 20 年的程式碼管理工具「Git」，卻無法跟上這種 AI 的速度。這就像是成千上萬台高速列車同時行駛在過去人類行駛的狹窄自行車道上。為了克服這個問題，作為軟體開發心臟的 Git 基礎建設正被徹底重寫。

## 這為什麼很重要？

軟體開發正從「人類」主導的時代，跨越到「AI 代理程式」主導的時代。但我們使用的 Git 是為 20 年前人類編寫和管理程式碼的方式所優化的。人類一天儲存數十次，與 AI 代理程式在短短幾分鐘內執行並儲存數千次操作，這完全是不同層級的問題。

如果無法解決這個問題，AI 代理程式的工作速度將會受限於物理基礎建設的瓶頸而停止。如果開發基礎建設不改變，未來的智慧開發代理程式也將無法發揮其應有的效能。因此，這項技術變革將成為決定未來軟體能以多快、多穩定速度製造出來的關鍵鑰匙。

## 輕鬆理解：為什麼現在的 Git 很慢？

我們一直以來使用的 Git 是徹徹底底為「人類」所設計的。[參考資料 7](https://www.linkedin.com/posts/atharvapandey_origin-is-hosted-on-github-quite-funny-activity-7497924180622004224-p_BB) 也就是人類編寫程式碼、分割分支，並向同事請求審閱（PR）的一系列過程。

然而，AI 代理程式則不同。它們幾乎在每次作業時都試圖建立檢查點或儲存程式碼。[參考資料 1](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/) 換句話說，它們在緊密的作業循環中不斷嘗試寫入資料。既有的 Git 基礎建設在處理這種「高頻寫入」時會面臨巨大的瓶頸。

簡單比喻，這就像是原本只有一名開發者通過的旋轉門，現在同時湧入數千名人群。由於狹窄的門一次只能通過一人，無法處理數千名 AI 的資料，系統自然會發出悲鳴。

因此，企業正在尋找新的方法。例如，基於 AI 的程式碼編輯器「Cursor」開發了名為「Origin」的自有託管系統。[參考資料 6](https://www.explainx.ai/blog/cursor-origin-git-hosting-block-buzz-projects-august-2026) 該系統在 S3（雲端儲存）上使用了「WAL (Write-Ahead Logging，預寫式記錄)」方式。

用另一個比喻來說，這就像在餐廳點餐時，不需要每次點餐都跑去廚房請求製作料理，而是先把訂單（日誌）快速記錄在紙上，稍後再一次性製作料理的方式。多虧了這一點，記錄的保存變得更加快速且穩定。

## 現況：準備迎接「35 倍」奇蹟的技術

GitHub 目前正從零開始設計適合這種代理程式時代的全新 Git 儲存庫結構。[參考資料 3](https://www.theregister.com/devops/2026/10/09/so-long-spokes-github-rewrites-storage-to-restore-reliability-just-in-time-for-agentic-hordes/5302148) 因為原本人類使用的基礎建設，根本無法應付日益增加的 AI 代理程式活動量。

令人驚訝的消息是，已經出現了顯著的成效。根據 GitHub 的初步內部測試，重新設計的架構展現了比過去方式快上 **35 倍的寫入效能**。[參考資料 3](https://www.theregister.com/devops/2026/10/09/so-long-spokes-github-rewrites-storage-to-restore-reliability-just-in-time-for-agentic-hordes/5302148) 35 倍這個數字不僅僅是小幅改進，而是展現了要突破基礎建設根本極限的強烈意志。業界分析認為，GitHub 正透過這種基礎建設的重構，試圖搶佔代理程式中心的開發環境市場。[參考資料 2](https://www.c-sharpcorner.com/article/github-is-building-git-infrastructure-for-agent-scale-development)

## 未來將如何發展？

我們即將迎來名為「代理程式規模軟體開發 (Agent-scale Software Development)」的新現實。[參考資料 9](https://qiita.com/yoshioterada/items/e796d7255e0a4efdb9f9) 未來，會有更多的開發工具和平台為了讓 AI 代理程式能夠盡情讀寫程式碼而改建其基礎建設。

這不僅僅是提升 Git 的效能，還將創造一個讓更多多代理程式系統能夠輕易協作的環境。[參考資料 8](https://www.youtube.com/watch?v=lW5xEm7iSXk) 作為使用者的各位，未來可能會更頻繁地見證 AI 在極短時間內實作出更複雜、更龐大軟體的場景。開發基礎建設的靜默創新，正成為讓我們眼前的 AI 服務變得更聰明、更快速的基石。

## MindTickleBytes AI 記者視角

對於非開發者的一般大眾來說，「Git」可能是一個陌生的詞彙。但在這個 AI 改變我們日常生活的時代，改變 AI 工作方式的 Git 是非常重要的變革。在我們看不見的資料中心深處，AI 代理程式已經開始進行基礎建設的重組，以便比人類快上數十倍地堆疊程式碼。這顯示了技術的發展不僅停留在外表看得到的功，而是從基層建設開始發生根本性的變化。

## 參考資料

1. [Building Git infrastructure for agent-scale development](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/)
2. [GitHub Is Building Git Infrastructure for Agent-Scale Development](https://www.c-sharpcorner.com/article/github-is-building-git-infrastructure-for-agent-scale-development)
3. [So long, Spokes: GitHub rewrites storage to restore reliability, just in time for agentic hordes](https://www.theregister.com/devops/2026/10/09/so-long-spokes-github-rewrites-storage-to-restore-reliability-just-in-time-for-agentic-hordes/5302148)
4. [Startup Entire Launches Distributed Git Network for the...](https://daily.dev/posts/startup-entire-launches-distributed-git-network-for-the-agent-era-bgrcebmrv)
5. [Cursor Origin: How Its New Git Hosting Actually Works | explainx.ai](https://www.explainx.ai/blog/cursor-origin-git-hosting-block-buzz-projects-august-2026)
6. [GitHub’s Scale: Mind Boggling, Alternatives Limited | LinkedIn](https://www.linkedin.com/posts/atharvapandey_origin-is-hosted-on-github-quite-funny-activity-7497924180622004224-p_BB)
7. [n8n Just Made MultiAgent AI Way Easier: New AI Agent... - YouTube](https://www.youtube.com/watch?v=lW5xEm7iSXk)
8. [GitHubが「AIエージェント時代」を見据えて、Git... - Qiita](https://qiita.com/yoshioterada/items/e796d7255e0a4efdb9f9)
9. [AI Workflow Automation Platform - n8n](https://n8n.io/)