---
layout: post
title: "當我們不再給 AI「工具」，而是給牠「電腦」時發生了什麼"
description: "本文介紹了一種新的 AI Agent 設計方式：讓 AI 不再依賴複雜的專用工具，而是直接使用檔案系統與 Bash 指令來獨立完成工作。"
summary: "比起每次都為 AI Agent 開發專用工具，現在一種稱為「Files over tools（檔案優先）」的設計方式正備受關注。這種方式透過提供虛擬檔案系統與 Bash 指令，讓 AI 能自行處理與操作數據。"
tags: [AI, Agent, 開發, 技術趨勢]
image: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash.jpg
image_alt: "象徵 AI 在虛擬檔案系統環境中編寫程式碼並瀏覽檔案的圖片"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "與其開發複雜的工具，讓 AI 在牠們早已熟悉的電腦環境（檔案與指令）中進行思考，是一種更具擴展性且靈活的方法。"
quiz:
  - question: "在近期的 AI Agent 設計中，除了工具（Tool）導向之外，另一種更受推崇的新型態方式是什麼？"
    choices: ["網頁瀏覽器自動化方式", "虛擬檔案系統與 Bash 環境方式", "使用者直接輸入方式"]
    answer: 1
    explanation: "近期比起提供大量專用工具，讓 AI 使用檔案系統與 Bash 指令來自行瀏覽並操作數據，被認為具備更高的效率。"
  - question: "使用虛擬檔案系統的 Agent 主要優勢為何？"
    choices: ["可以將所有檔案儲存在實體硬碟中。", "無須每次都開發新工具，即可處理各種任務。", "隨時都需要網路連線。"]
    answer: 1
    explanation: "具備 Bash 存取權限的 Agent，能夠靈活執行檔案瀏覽、文字處理等各種任務，而無須開發專用工具。"
  - question: "虛擬檔案系統的數據實際上可以儲存在哪裡？"
    choices: ["一定要儲存在雲端伺服器中。", "可以用 SQLite 等資料庫作為備份儲存，而非實體磁碟檔案。", "每次執行後就會消失。"]
    answer: 1
    explanation: "部分虛擬檔案系統並非以實體檔案形式存在，而是將 SQLite 等資料庫作為備份儲存空間來進行高效管理。"
lang: zh-tw
ref: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash
---

試想一下，您對廚師說：「幫我做一鍋好吃的泡菜鍋。」但如果這位廚師雖然會做泡菜鍋，可每次切洋蔥時都要重新打造一把「專用切洋蔥刀」，每次用勺子時都要操作一台「製造勺子的機器」，您會作何感想？恐怕在料理完成前，您就已經累壞了。這是因為準備工具的時間，遠遠超過了料理本身的時間。

令人驚訝的是，過去我們在打造 AI Agent（具備自主目標設定並能執行複雜任務的人工智慧）時，採用的正是這種低效率的方式。我們為 AI 能執行的每一項任務，都一對一地「打造並連接」專用的工具。然而，最近在開發者之間出現了一股新的趨勢：「與其重新打造工具，不如直接給 AI 一個電腦環境本身」。這種設計方式被稱為「Files over tools（檔案優先）」。

## 為什麼這種方式很重要？

至今為止，AI Agent 每增加一項功能，開發者就必須設計複雜的軟體工具並將其連接到 AI。這不僅耗時費錢，也是導致 AI 靈活性下降的主因。因為一旦發生超出預設工具範圍的情境，AI 就會束手無策。

但是，如果給予 AI 虛擬檔案系統（Virtual Filesystem）與 Bash（Linux 系統中使用的指令作業環境）存取權限，情況就會完全改觀。Agent 就像人類開發者在電腦前工作一樣，可以自行查找檔案、讀取內容、進行修改，並結合指令來解決問題。這不僅能大幅提升 AI Agent 的生產力，也不再需要開發者預設所有狀況來開發工具，AI 能夠自主靈活地應對新環境。

## 簡單的比喻

簡單來說，過去的方法是給 AI 幾百台「按下一個按鈕就能執行特定動作的專用機器」；而新的方法，則是借給 AI 「一台安裝了作業系統的電腦」。

例如，假設 Agent 需要管理客戶資訊。過去必須一一開發「查詢客戶資訊工具」、「修改客戶資訊工具」。但現在，只要展示給 Agent 包含客戶資料的虛擬資料夾，並讓牠使用 Bash 指令（例如用 `grep` 指令查找資料，用 `echo` 指令修改內容）即可。[參考資料 2](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi) 這樣一來，AI 就像使用電腦的使用者一樣，瀏覽檔案並自主理解上下文來完成任務。[參考資料 14](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)

此外，這套檔案系統無須佔用實體硬碟空間即可運作。部分虛擬檔案系統利用 SQLite（輕量且快速的資料庫程式）來安全地儲存與管理數據。[參考資料 19](https://github.com/maxi-moss/agent-filesystem) 在我們眼中看起來像是電腦中瀏覽資料夾，但實際上是在資料庫內更有效率地處理資訊。

## 目前技術發展到什麼程度了？

已有許多企業與專案導入了這種方式。一家名為「Knock」的公司在其 AI Agent 架構中，結合了 Bash 環境、虛擬檔案系統以及管理用的 API，藉此處理客戶訊息資源。[參考資料 1](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash) [參考資料 3](https://fooqux.com/article/6457)

此外，像「AgentFS」這類專案，為 AI Agent 提供了專用的檔案系統。這有助於讓 AI 在安全使用命令列工具（CLI Tool）的同時，還能稽核（Audit）所有工作記錄。[參考資料 15](https://github.com/tursodatabase/agentfs) [參考資料 16](https://www.agentfs.ai/) 這不僅僅是減少工具數量，透過留下 AI 的操作紀錄以確保安全性，正是當前技術的核心。

## 未來會是什麼樣貌？

AI Agent 的發展方向正逐漸「變得像人類一樣」。開發者為其設計專用工具的時代即將過去，取而代之的將是 AI 自主利用電腦環境，如熟練助理般工作的時代。

未來，Agent 需要處理的數據將以檔案形式有系統地整理好，而 Agent 將透過使用 Linux 指令來靈活處理這些數據。您需要做的事將不再是製造工具，而是建構一個讓 AI 能夠工作的良好「數位環境」。現在，正是借給牠們「環境」的時候了。

## MindTickleBytes 的 AI 記者觀點
從工具時代轉向環境時代，意味著 AI 技術已超越了單純的計算機，正進化為真正的「數位工作者」。這種將開發者的介入降至最低，並將 AI 自主性最大化的設計，將決定未來 Agent 生態系統的樣貌。

## 參考資料

1. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash)
2. [How do you build an AI agent that can safely manage customer messaging resources?](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi)
3. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://fooqux.com/article/6457)
4. [Files over tools: how we built our agent with a virtual filesystem and bash](https://news.ycombinator.com/item?id=48845364)
5. [How to build agents with filesystems and bash - Vercel](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash)
6. [Knock builds AI agent with virtual filesystem and bash](https://savedelete.com/news/knock-agent-virtual-filesystem/)
7. [Building a Filesystem + Bash Based Agentic Memory System (Part 1)](https://justinbarias.io/blog/agentic-memory-filesystem-part-1/)
14. [We removed 80% of our agent’s tools - Vercel](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)
15. [GitHub - tursodatabase/agentfs: The filesystem for agents.](https://github.com/tursodatabase/agentfs)
16. [AgentFS - Filesystem Isolation for AI Agents](https://www.agentfs.ai/)
18. [Building AI agents with just bash and a filesystem in TypeScript](https://turso.tech/blog/agentfs-just-bash)
19. [GitHub - maxi-moss/agent-filesystem: A virtual filesystem for agents.](https://github.com/maxi-moss/agent-filesystem)