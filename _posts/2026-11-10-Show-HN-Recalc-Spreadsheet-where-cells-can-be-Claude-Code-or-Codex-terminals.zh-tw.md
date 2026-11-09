---
layout: post
title: "如果 Excel 成為 AI 的終端機？透過「Recalc」體驗代理程式時代"
description: "介紹全新的開源試算表「Recalc」，讓每個儲存格都能運行 Claude Code 或 Codex，輕鬆與 AI 代理程式協作。"
summary: "Recalc 是一款將試算表中的每個儲存格作為 AI 終端機來運用的工具，能協助多個代理程式共享資料並處理複雜的工作流程。"
tags: [AI, 代理程式, 試算表, Recalc, 生產力]
image: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals.jpg
image_alt: "多個 AI 代理程式執行階段在試算表網格內同時運作的畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "以熟悉的網格形式管理複雜的程式開發代理程式工作流程，是非常直觀的做法。這是一次將 AI 與人類協作方式提升至新境界的有趣嘗試。"
quiz:
  - question: "在 Recalc 試算表的每個儲存格中可以進行什麼作業？"
    choices: ["儲存數值", "計算公式", "執行終端機指令及 AI 代理程式", "上述皆可"]
    answer: 3
    explanation: "Recalc 的設計初衷是讓所有儲存格不僅能輸入簡單數值或公式，還能直接執行終端機指令、Claude Code 以及 Codex 執行階段。"
  - question: "Recalc 提到的一種 AI 代理程式操控方式為何？"
    choices: ["透過編輯儲存格來控制代理程式，無需中斷對話", "等待代理程式隨機選擇", "學習專用程式語言"]
    answer: 0
    explanation: "Recalc 讓使用者無需干擾對話流程，僅需編輯試算表中的儲存格，即可直接操控代理程式的動作。"
  - question: "Recalc 用於不同代理程式執行階段之間通訊的技術是什麼？"
    choices: ["區塊鏈", "MCP (Model Context Protocol) 伺服器", "專用雲端 API"]
    answer: 1
    explanation: "Recalc 利用 MCP 伺服器來協助不同儲存格與執行階段之間共享資料並進行溝通。"
lang: zh-tw
ref: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals
---

試著想像一下：您像往常一樣打開 Excel 或 Google Sheets。但與其在表格的每個儲存格中輸入數字，您改為對 AI 下令：「分析這項資料並撰寫報告草稿」。在旁邊的儲存格中，另一個 AI 代理程式（接受使用者的指示並自動執行工作的 AI）則正在即時運行程式碼並搜尋必要的資訊。這感覺就像好幾位聰明的 AI 助理聚在同一本帳簿前共同開會一樣。

最近，於 2026 年 11 月 8 日透過 GitHub 公開的開源試算表工具**「Recalc」**，正將這樣的未來帶入現實 [Source 11]。

### 為什麼這很重要？

以往在處理 AI 代理程式時，我們通常被侷限在名為「對話框」的狹窄空間內。當代理程式執行複雜任務時，若要與其他執行階段交換資料，往往需要逐一儲存檔案，或是手動串接複雜的程式介面 (API)，非常繁瑣。

Recalc 將我們最熟悉的工具——「試算表」轉變為 AI 協作的中樞。隨著個別的代理程式執行階段能夠在試算表這個共同的網格中共享資料並溝通，無論是 AI 評測還是複雜的業務處理流程（工作流程），管理起來都變得更加直觀 [Source 1, Source 11]。

### 淺顯易懂的理解

簡單來說，如果以往的 AI 代理程式工作就像是在與一位「獨自在密室中苦思的研究員」對話，那麼 Recalc 就如同提供了一個「多位研究員在同一張大圖紙上共同繪圖」的環境。

*   **資料流動的通道：** 試算表的儲存格不再只是單純填入數字的格子。每個儲存格都是一個小型終端機視窗（指令輸入框），同時也是 Claude Code（Anthropic 的 AI 程式開發代理程式）或 Codex 等 AI 代理程式駐紮的獨立空間 [Source 10, Source 13]。
*   **資料共享：** 儲存格之間是互聯的。A 儲存格中由 AI 產生的結果，B 儲存格中的另一個 AI 可以直接取用。這是透過一項名為 **MCP (Model Context Protocol，AI 模型與外部資料或環境溝通的標準規範)** 的技術來達成，該規範發揮了將整個應用程式有機地黏合起來的作用 [Source 1, Source 11]。

無須在對話框中長篇大論，僅需編輯表格中的一格，就能立即修正或指示 AI 代理程式的行動 [Source 10]。

### 目前狀況

目前 Recalc 正作為一個任何人都可以參與的開源專案進行開發。其主要特點如下：

*   **實地測試：** 開發者是為了在自己的新創公司中進行實際的 AI 效能評測（基準測試）而製作此工具。例如，已有展示案例能測試 AI 預測美國食品藥物管理局 (FDA) 提交文件之通過與否的精準度 [Source 1]。
*   **作業環境：** 目前設計為在 macOS 環境下順暢運作。雖然理論上可在 Linux 上執行，但尚未經過充分測試，且目前尚未支援 Windows [Source 1]。
*   **安全性：** 與 Claude Code 等工具聯動時，這些工具通常是在使用者的電腦本地環境中執行。由於無須透過額外的後端伺服器，而是與模型直接通訊，因此在設計之初已將安全性納入考量 [Source 3]。

### 未來展望

Recalc 展示了徹底翻轉 AI 與人類協作方式的潛力。未來，不僅是資料分析師，連開發者與企劃人員都有可能使用試算表來調度數十個 AI 代理程式。若未來能擴大支援 Windows 等更多環境，使其在各種作業系統中都能輕鬆使用，預期它將不僅限於單純的重複性工作，更有望成長為複雜的企業級業務管理工具 [Source 1]。

### MindTickleBytes 的 AI 記者觀點

這是一個絕佳的案例，證明了「工具越熟悉，AI 的能力擴展得就越快」。比起學習全新的複雜指令，透過我們日常使用的表格編輯方式來操作 AI，顯然更加直觀，這正是 Recalc 最強大的武器。複雜的 AI 代理程式時代，比我們想像中還要更近地來到我們身邊。

## 參考資料

1. [Show HN: Recalc – Spreadsheet where cells can be Claude Code or Codex terminals](https://github.com/sshah03/recalc)
2. [ClaudeCode by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)
3. [Recalc - Spreadsheet with Claude Code · Hacker News | Zeli](https://zeli.app/story/50413970)
4. [Recalc Spreadsheet Lets Cells Run Claude Code or Codex](https://emergent.sh/news/recalc-spreadsheet-lets-cells-run-claude-code)
5. [recalc/demos/done-means-green/repo/.codex at main - GitHub](https://github.com/sshah03/recalc/tree/main/demos/done-means-green/repo/.codex)
6. [recalc/CLAUDE.md at main · sshah03/recalc · GitHub](https://github.com/sshah03/recalc/blob/main/CLAUDE.md)