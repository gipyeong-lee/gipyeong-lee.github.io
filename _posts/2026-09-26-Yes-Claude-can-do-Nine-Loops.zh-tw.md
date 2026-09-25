---
layout: post
title: "讓 AI 執行重複性工作... 用「迴圈工程 (Loop Engineering)」打造專屬秘書"
description: "厭倦了每次都要手動輸入提示詞並檢查 AI 結果嗎？介紹如何透過 Claude Code 的「迴圈工程」來自動化重複性的編碼工作。"
summary: "利用 Claude Code 的「迴圈 (Loop)」功能，您可以建立一套自主系統，讓 AI 自行搜尋任務、執行並驗證結果。"
tags: [AI, ClaudeCode, 生產力, 自動化, 迴圈工程]
image: 2026-09-26-Yes-Claude-can-do-Nine-Loops.jpg
image_alt: "象徵重複性工作數位自動化系統的抽象圖形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是從人類必須時刻下達指令的時代，轉向 AI 自行判斷與執行的「代理系統 (Agent System)」的轉捩點。"
quiz:
  - question: "在 Claude Code 中，設定「工作已完成」的標準，並讓 AI 在滿足該條件前持續執行的指令組合是？"
    choices: ["/schedule", "/goal 與 /loop 的組合", "/routine"]
    answer: 1
    explanation: "/goal 用於定義完成標準，而 /loop 則讓 AI 在該條件滿足前持續運作。"
  - question: "為了成功實踐迴圈工程，最重要的是什麼？"
    choices: ["使用更多的 Token", "透過驗證者 (Verifier) 確認結果", "每天重新編寫提示詞"]
    answer: 1
    explanation: "AI 自行驗證結果、設定無法跨越的停止條件，這些「驗證者」的角色是核心所在。"
  - question: "關於 Claude Code 迴圈功能的描述，下列何者正確？"
    choices: ["所有功能僅在官方 MCP 伺服器中提供", "包含重複性的本地執行以及雲端基礎的例行工作 (Routines)", "使用者必須親自編寫代碼才能運作"]
    answer: 1
    explanation: "Claude Code 不僅支援本地迴圈，還支援雲端 Cron 式的例行工作、動態工作流等各種自動化方式。"
lang: zh-tw
ref: 2026-09-26-Yes-Claude-can-do-Nine-Loops
---

想像一下。下班前，您對 AI 秘書說：「明天早上前，把這個專案的臭蟲全部找出來並修正，測試也要全部通過。」以前，您必須不斷向 AI 下指令：「檢查下一個檔案」、「執行測試」、「好了嗎？」，然後等待回覆。但現在，AI 自行判斷與重複執行任務的時代已經來臨。

近期因 Claude Code 而備受矚目的**「迴圈工程 (Loop Engineering)」**正是這一切的主角。

## 為什麼這很重要？

到目前為止，我們使用 AI 編碼代理的方式就像在用「遙控器」。每按一次按鈕，指令才會傳達。但迴圈工程將 AI 變身為「自動駕駛系統」。

開發者再也不需要為了讓 AI 執行簡單重複的工作，而浪費時間進行手動操作。因為您可以構建一個讓 AI 自行搜尋任務、執行、驗證結果，並決定下一步的系統。這不僅是單純的自動化，更意味著與 AI 的協作方式，正從「下令」進化為「目標管理」 [出處: Loop Engineering in Claude Code: Let the Agent Run Itself | VibeReady](https://vibeready.sh/blog/loop-engineering-claude-code/)。

## 輕鬆理解

「迴圈 (Loop)」在程式設計中，是指將特定動作重複執行直到條件滿足為止。迴圈工程就是將此概念應用於 AI 代理。

用簡單的比喻來說，與其每次都向新手駕駛 (AI) 一一指示：「方向盤轉 30 度」、「踩煞車」，不如直接輸入具體規則：「安全抵達目的地，遇到紅燈就停，綠燈就出發」。

Claude Code 提供的核心工具，就是構成這些規則的零件：

*   **/goal**：為 AI 定義什麼是「完成」狀態的明確目標 [出處: Loop engineering: Getting started with loops | Claude by Anthropic](https://claude.com/blog/getting-started-with-loops)。
*   **/loop**：讓代理在目標達成前，持續執行本地任務 [出處: Loop engineering: Claude Code Loops, Routines & Workflows](https://blakecrosley.com/guides/loop-engineering)。
*   **驗證者 (Verifier)**：這是核心。為了防止 AI 自行胡亂編造，透過人類設定的嚴格標準 (例如：是否通過特定測試) 來確認結果是否正確 [出處: Loop Engineering in Claude Code: Let the Agent Run Itself | VibeReady](https://vibeready.sh/blog/loop-engineering-claude-code/)。

只要組合目標 (/goal) 與重複 (/loop)，就能誕生出能自主執行長期任務的代理 [出處: How to Use the /goal and /loop Commands in Claude Code for Autonomous Long-Running Tasks | MindStudio](https://www.mindstudio.ai/blog/claude-code-goal-loop-commands-autonomous-tasks)。

## 現狀

目前，迴圈工程的層次已經遠遠超越了單純重複執行程式碼。

*   **/goal**、**/loop** 等基本重複指令 [出處: Claude Code Loops Guide: /goal, /loop, /schedule (2026) | explainx.ai Blog | explainx.ai](https://www.explainx.ai/blog/claude-code-loops-official-guide-turn-goal-schedule-2026)
*   在雲端環境中週期性運行的「例行工作 (Routines)」
*   動員多個 AI 代理處理複雜任務的「動態工作流 (Dynamic Workflows)」，其範圍已經持續擴大 [出處: Loop engineering: Claude Code Loops, Routines & Workflows](https://blakecrosley.com/guides/loop-engineering)。

不過，需要留意的是，目前「Loops」功能尚未直接支援官方 MCP (Model Context Protocol，連接 AI 模型與外部工具的標準規範) 伺服器，必須透過中繼服務才能使用 [出處: How to Connect Loops to Claude (and What It Can't Do)](https://www.usecarly.com/blog/claude-loops-integration/)。

## 未來展望

迴圈工程將會變得更加精密。它將超越編碼，擴展至數據分析、報告撰寫、伺服器管理等更多領域，AI 將登場成為能夠自行檢查「自身狀態」並「達成目標」的代理 [出處: Loop engineering: Claude Code Loops, Routines & Workflows](https://blakecrosley.com/guides/loop-engineering)。

使用者將不需要再苦惱於 AI 的「運作方式」，而是會更專注於「要達成什麼目標」。許多開發者已經擺脫了每次手動輸入提示詞的方式，轉而投入設計系統的迴圈工程中 [出處: I Stopped Prompting Claude Code. Now Loops Do It For Me (Loop Engineering) - YouTube](https://www.youtube.com/watch?v=yaJAMagc_sE)。

## MindTickleBytes AI 記者觀點

「迴圈工程是 AI 從『工具』進化為『合作夥伴』的信號彈。需要 AI 做什麼事是人類的工作，而讓 AI 自己做該做的事，則是系統的工作。」

---

## 參考資料

1. [Claude computes a nine-loop amplitude in N=4 super-Yang-Mills \ Anthropic](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)
2. [Loop Engineering in Claude Code: Let the Agent Run Itself | VibeReady](https://vibeready.sh/blog/loop-engineering-claude-code/)
3. [Claude Code Loops Guide: /goal, /loop, /schedule (2026) | explainx.ai Blog | explainx.ai](https://www.explainx.ai/blog/claude-code-loops-official-guide-turn-goal-schedule-2026)
4. [How to Use the /goal and /loop Commands in Claude Code for Autonomous Long-Running Tasks | MindStudio](https://www.mindstudio.ai/blog/claude-code-goal-loop-commands-autonomous-tasks)
5. [How to Connect Loops to Claude (and What It Can't Do)](https://www.usecarly.com/blog/claude-loops-integration/)
6. [I Stopped Prompting Claude Code. Now Loops Do It For Me (Loop Engineering) - YouTube](https://www.youtube.com/watch?v=yaJAMagc_sE)
7. [Loop engineering: Claude Code Loops, Routines & Workflows](https://blakecrosley.com/guides/loop-engineering)
8. [Loop engineering: Getting started with loops | Claude by Anthropic](https://claude.com/blog/getting-started-with-loops)