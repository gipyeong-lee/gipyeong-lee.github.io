---
layout: post
title: "Claude Code 新增 AGENTS.md 支援，為何我的專案無法使用？"
description: "在最新版 Claude Code 中設定了 AGENTS.md 檔案，但 AI 卻忽略了它？讓我們來探討原因與解決方案。"
summary: "Claude Code 2.1.277 版本開始支援 AGENTS.md，但請注意，在某些特定環境或設定下，此功能可能無法正常運作。"
tags: [ClaudeCode, AI, 開發工具, AGENTS.md]
image: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on.jpg
image_alt: "Claude Code 程式碼工具 Logo 與文件圖示結合的現代科技圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "導入新標準總會伴隨著初期的混亂。目前，使用 CLAUDE.md 是最穩妥的方式。"
quiz:
  - question: "在 Claude Code 中，如果 CLAUDE.md 和 AGENTS.md 同時存在，系統會優先讀取哪個檔案？"
    choices: ["AGENTS.md", "CLAUDE.md", "無法得知"]
    answer: 1
    explanation: "Claude Code 在兩個檔案都存在時，會優先讀取傳統的 CLAUDE.md 並忽略 AGENTS.md。"
  - question: "目前 AGENTS.md 支援尚未正式支援的環境有哪些？"
    choices: ["終端機", "桌面應用程式", "Amazon Bedrock"]
    answer: 2
    explanation: "像 Amazon Bedrock、Vertex 和 Foundry 等環境，目前尚未支援 AGENTS.md 功能。"
  - question: "在無法使用 AGENTS.md 的環境中，建議的解決方案是什麼？"
    choices: ["更改檔案名稱", "將內容匯入 CLAUDE.md", "強制開啟該功能"]
    answer: 1
    explanation: "當無法直接支援 AGENTS.md 時，最安全的方法是將該檔案的內容直接包含在 CLAUDE.md 中。"
lang: zh-tw
ref: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on
---

想像一下。您每天早上都花費一番心思編寫一個額外的說明檔案，來告知您的 AI 編碼工具專案的規則。但如果 AI 完全忽略了您精心編寫的檔案，那會怎樣呢？最近，許多開發者都遇到了這種令人沮喪的情況。這是因為最新更新引入的新方法並不像預期那樣順暢運作。

## 這為什麼重要？

Claude Code 是一個強大的「代理型編碼工具」，能夠讀取開發者的程式碼庫、修改檔案，甚至直接執行指令([Overview - Claude Code Docs](https://code.claude.com/docs/en/overview))。到目前為止，開發者主要使用一個名為 `CLAUDE.md` 的檔案，來向 AI 說明專案的編碼規則或注意事項。

然而，隨著最近宣布採用名為 `AGENTS.md` 的新格式作為標準，許多團隊都寄予厚望([Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl](https://dev.blog/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/))。這項變革的核心是希望統一多個 AI 工具之間的規則設定。如果此功能未能正常運作，開發者精心編寫的規則將無法傳達給 AI，有導致生成錯誤程式碼的風險。

## 輕鬆理解

將此情況比喻為「學習新語言的學生」會更容易理解。

*   **舊方法 (CLAUDE.md)**：這是 AI 過去一直以來學習並熟悉的舊教科書。
*   **新方法 (AGENTS.md)**：這是為 AI 提供更系統化學習而新引入的標準參考指南。

然而，AI 需要在開啟特定的「學習模式」下才能閱讀此參考指南。不幸的是，在許多現有環境中，此模式預設為關閉，或者 AI 根本沒有權限閱讀參考指南([Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch](https://github.com/anthropics/claude-code/issues/95690))。就好比 AI 不知道參考指南的存在，或認為沒有閱讀的必要。特別是當使用者數據收集（遙測，telemetry）功能關閉時，或在使用企業級服務（如 Amazon Bedrock）時，會出現無法讀取新規則檔案的情況([Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/))。

## 問題出在哪裡？

在最新更新的 Claude Code 2.1.277 版本中，已新增了對 `AGENTS.md` 的支援([Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog))。但為了穩定使用，必須注意以下幾點限制：

1.  **現有檔案的優先順序**：如果專案資料夾中同時存在 `CLAUDE.md` 和 `AGENTS.md`，AI 會按照慣例優先讀取舊有的 `CLAUDE.md`，而完全忽略新的 `AGENTS.md`([Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/))。
2.  **環境限制**：像 Amazon Bedrock、Vertex 和 Foundry 等環境，目前尚未正式支援此功能([Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog))。
3.  **內部連接方式**：此功能並非整合到 AI 的核心邏輯中，而是以一種內部連接的「外掛程式」形式實現([Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md))。因此，若未滿足特定條件，極易發生工具本身連檔案都無法識別的「靜默失敗」(silent failure)。

## 未來展望

目前，僅依賴 `AGENTS.md` 來管理規則，面臨著嚴重的環境限制。如果您需要在不支援直接 `AGENTS.md` 的環境中分享規則，最安全可靠的方法是將其內容直接包含 (import) 在現有的 `CLAUDE.md` 檔案中([Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes](https://github.com/fmslutions/harness-audit/issues/3))。特別是對於那些計劃在企業內部環境中採用 `AGENTS.md` 作為標準的團隊，目前需要特別謹慎([Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html))。建議在未來更新擴大支援更多環境之前，維持現有方法。

## MindTickleBytes AI 記者視角

引入新標準是一個旨在簡化開發者複雜檔案管理的絕佳嘗試。然而，這次的案例清楚地表明，由於技術差距或環境設定，一個「聰明的 AI」反而可能變得「視而不見」。在目前階段，與其立即採用新技術，不如結合使用現有的安全方法，是維護工作連續性的最佳策略。

## 參考資料
1. [Claude Code 僅在啟用遙測時讀取 AGENTS.md](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)
2. [Claude Code 僅在啟用遙測時讀取 AGENTS.md - Hacker News](https://news.ycombinator.com/item?id=49814947)
3. [為 opencode 設定自訂指示](https://opencode.ai/docs/rules/)
4. [概述 - Claude Code 文件](https://code.claude.com/docs/en/overview)
5. [我如何使用 Claude Code (+ 我的最佳提示)](https://www.builder.io/blog/claude-code)
6. [發佈 · anthropics/claude-code · GitHub](https://github.com/anthropics/claude-code/releases)
7. [AGENTS.md 滿週年。關於其運作情況的證據... - Kernel Talks](https://kerneltalks.com/ai/agents-md-just-turned-one-the-evidence-on-whether-it-works-is-mixed/)
8. [claude-code/mods/agents-md/README.md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md)
9. [1.2：Claude Code 2.1.277 直接讀取 AGENTS.md — 解析表、新的靜默失敗模式 · Issue #3 · fmslutions/harness-audit](https://github.com/fmslutions/harness-audit/issues/3)
10. [[MODEL] Claude Code 的 AGENTS.md 支援：一個被遠端開關鎖定的本地功能 · Issue #95690 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/95690)
11. [Claude Code Mods 與 agents.md：新功能與重要性 | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md)
12. [claude-code/mods/agents-md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/mods/agents-md)
13. [Claude Code 新增 AGENTS.md Fallback，減少指令檔案冗餘 – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)
14. [[錯誤教條] "Claude Code 讀取 CLAUDE.md，而非 AGENTS.md" 不再為真，且我們的設定指令可能會靜默關閉專案的 AGENTS.md · Issue #1087 · fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills/issues/1087)
15. [Claude Code 更新日誌 - Claude Code 文件](https://code.claude.com/docs/en/changelog)
16. [Claude Code 現也接受 OpenAI 的 Agents.md 格式指令 | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html)
17. [Claude Code 更新日誌 (2026 年 9 月)](https://www.gradually.ai/en/changelogs/claude-code/)
18. [Claude Code 新增 AGENTS.md Fallback，減少指令檔案冗餘 - DevOps.com](https://devops.com/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)