---
layout: post
title: "AI 可以幫忙寫程式？開發者們選擇了『Codex』"
description: "在 AI 程式設計工具 OpenAI Codex 與 Anthropic Claude Code 之間，近期開發者更愛用哪一款？透過 Homebrew 安裝統計，一探 AI 程式設計代理的趨勢。"
summary: "根據近 30 天 macOS 平台 AI 程式設計工具安裝數據分析，OpenAI 的 Codex 已超越 Anthropic 的 Claude Code，成為更多開發者的首選。"
tags: [AI, 程式設計, 開發工具, Codex, ClaudeCode]
image: 2026-07-26-Codex-now-leads-Claude-Code-in-first-time-Homebrew-installs-for-last-30-days.jpg
image_alt: "展示終端機畫面中程式碼自動編寫的數位插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開發者採納 AI 代理作為工具的速度非常快。工具之間的競爭，最終將帶動使用者體驗與性能提升，實現更好的成果。"
quiz:
  - question: "在近期的 Homebrew 安裝統計中，安裝率較高的 AI 程式設計工具是哪一個？"
    choices: ["Claude Code", "Codex", "兩者相同"]
    answer: 1
    explanation: "根據近期統計，Codex 日均安裝量達 836 次，領先 Claude Code（473 次）。"
  - question: "像 Claude Code 這類『代理型程式設計工具』的主要特徵是什麼？"
    choices: ["僅能在網頁瀏覽器內運作", "在終端機內將想法轉化為程式碼", "僅執行設計工作"]
    answer: 1
    explanation: "這些工具直接在開發者的終端機環境中執行，協助將想法轉化為實際的程式碼。"
  - question: "Claude Code 的日均 GitHub 程式碼提交（Commit）貢獻量大約是多少？"
    choices: ["約 5 萬個", "約 15 萬個", "超過 32 萬個"]
    answer: 2
    explanation: "Claude Code 每天產生超過 32 萬 6 千個提交，約佔所有公開提交的 10%。"
lang: zh-tw
ref: 2026-07-26-Codex-now-leads-Claude-Code-in-first-time-Homebrew-installs-for-last-30-days
---

試著想像一下，身為程式設計師的你，當需要實作複雜功能時，腦中只需浮現點子，AI 就會自動打開終端機視窗並開始編寫程式碼。這就像有一位資深同事在旁即時協助你一樣，這種夢寐以求的場景如今已成真。這都要歸功於「代理型程式設計工具（Agentic Coding Tool，指能在開發者終端機環境中自主作業並編寫程式碼的 AI）」。

近期，OpenAI 的 **Codex** 與 Anthropic 的 **Claude Code** 這兩大 AI 工具在開發者圈掀起了激烈競爭。然而，近期出現了值得關注的變化。觀察 macOS 開發者最常使用的軟體安裝工具「Homebrew」統計數據後發現，選擇 Codex 的開發者正在快速增加。

### 這為何重要？

這不僅僅是安裝數量增加，更代表開發者正在決定將哪一位 AI 夥伴導入自己的程式開發環境。終端機基礎的 AI 程式設計代理不僅僅是建議程式碼片段，更能理解整個專案並自主執行任務。 [Source 2](https://docs.anthropic.com/en/docs/claude-code/overview), [Source 13](https://formulae.brew.sh/cask/codex) 

當這類工具成為日常，開發者將從重複性的編碼工作中解放，轉而專注於更具創造性的問題解決上。換句話說，這為我們日常使用的 App 或網頁服務變得更快、更聰明奠定了基礎。

### 淺顯易懂：AI 助理的風格差異

簡單來說，**Claude Code** 與 **Codex** 就好比僱用了不同風格的「助理」。比喻如下：

*   **Claude Code** 就像一位非常細心的模範生助理。在目前的 SWE-bench 等程式開發能力評測中表現優異，且活躍度驚人，每天產生的 GitHub 公開提交約佔總數的 10%（超過 32 萬 6 千個！）。 [Source 9](https://www.morphllm.com/comparisons/codex-vs-claude-code)
*   **Codex** 則是一位快速且靈活的實戰型助理。根據近期數據，透過 Homebrew 的日均安裝量為 836 次，比 Claude Code 的 473 次高出約 1.77 倍。許多開發者似乎是看中了其作業速度或特定的功能優勢，而轉向選擇 Codex。 [Source 8](https://x.com/tickerplus/status/2051344320028938670)

這兩款工具均在終端機內執行，等待開發者的指令。 [Source 3](https://github.com/anthropics/claude-code), [Source 13](https://formulae.brew.sh/cask/codex) 就像在照片 App 中套用濾鏡來改變風格一樣，開發者正根據自身喜好選擇工具，以最佳化自己的程式設計風格。

### 現況：開發者的選擇是？

目前開發者對這兩款工具的評價各異。從性能指標來看，兩款 AI 各有千秋。 [Source 11](https://aithinkerlab.com/openai-codex-vs-claude-code/) 哪一款更好，取決於開發者當前進行的專案類型以及偏好的工作方式。

*   **Claude Code** 的安裝方式相對自由。macOS 或 Linux 可透過 Homebrew 安裝，Windows 環境也能透過原生安裝程式、WinGet 或 npm 等方式輕鬆啟用。 [Source 3](https://github.com/anthropics/claude-code), [Source 4](https://claudeskills.ru/blog/claude-code-windows), [Source 16](https://code.claude.com/docs/en/quickstart) 
*   **Codex** 同樣可透過 Homebrew 在 Mac 環境下極其簡便地安裝使用。 [Source 5](https://www.verdent.ai/guides/codex-app-download-install-macos)

### 未來展望

AI 程式設計工具市場才剛起步。兩款模型都在持續改善性能，並根據開發者意見增加新功能。 [Source 1](https://code.claude.com/docs/en/setup) 專家預測，未來 AI 不僅止於生成程式碼，還將發展成組成更複雜的代理團隊來進行協作。 [Source 9](https://www.morphllm.com/comparisons/codex-vs-claude-code)

我們正從開發者親手「一行一行寫」程式碼的時代，邁向「指示並管理」AI 執行任務的時代。在此趨勢下，哪種工具能成為標準，抑或兩者相互吸收優點變得更強大，值得持續關注。

---

### MindTickleBytes 的 AI 記者觀點
與其爭論工具的優劣，更重要的是開發者已開始將 AI 視為自身的一部分來活用。在 AI 一天撰寫超過 30 萬個提交的時代，我們或許需要重新定義「開發」的意義。

## 參考資料

1. Advanced setup -ClaudeCodeDocs (https://code.claude.com/docs/en/setup)
2. ClaudeCodeoverview - Anthropic (https://docs.anthropic.com/en/docs/claude-code/overview)
3. GitHub - anthropics/claude-code (https://github.com/anthropics/claude-code)
4. УстановкаClaudeCodeна Windows — пошаговый гайд 2026 (https://claudeskills.ru/blog/claude-code-windows)
5. How to Download &InstallCodexApp on macOS (https://www.verdent.ai/guides/codex-app-download-install-macos)
8. TickerTrends 🔬 on X (https://x.com/tickerplus/status/2051344320028938670)
9. Codex vs Claude Code (July 2026) (https://www.morphllm.com/comparisons/codex-vs-claude-code)
11. Claude Code vs OpenAI Codex: 30-Day Dev Test Results (2026) (https://aithinkerlab.com/openai-codex-vs-claude-code/)
13. Homebrew Formulae: codex (https://formulae.brew.sh/cask/codex)
16. Quickstart -ClaudeCodeDocs (https://code.claude.com/docs/en/quickstart)