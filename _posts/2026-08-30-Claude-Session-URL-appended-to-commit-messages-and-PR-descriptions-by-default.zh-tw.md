---
layout: post
title: "我的編碼紀錄會被公開？警惕 Claude Code 的「會話 URL」風險"
description: "AI 編碼工具 Claude Code 在提交訊息中自動加入的會話 URL 可能會洩漏隱私與機密，我們將探討相關擔憂與應對方法。"
summary: "Claude Code 自動插入的會話 URL 有洩露對話內容的風險，許多使用者要求將其變更為選擇性開啟（opt-in）模式。"
tags: [AI, 編碼, ClaudeCode, 安全, 隱私保護]
image: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default.jpg
image_alt: "電腦螢幕中顯示程式碼提交紀錄，旁邊伴隨著風險警告標誌"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開發過程的透明度固然重要，但將與 AI 的私人對話連同程式碼一併「存檔」是嚴重的安全問題。資訊保護應優先於功能的便利性。"
quiz:
  - question: "Claude Code 在提交訊息中加入的「會話 URL」為何會構成問題？"
    choices: ["因為這會導致程式碼執行變慢", "因為它可能會洩露完整的對話紀錄", "因為這會佔用過多的儲存空間"]
    answer: 1
    explanation: "點擊該 URL 會公開與 AI 之間的所有對話內容，有導致敏感資訊外洩的風險。"
  - question: "原本的 'attribution.commit' 設定是否能關閉會話 URL？"
    choices: ["是的，可以完全控制", "不，會話 URL 不在控制範圍內", "部分可以控制"]
    answer: 1
    explanation: "初期許多使用者指出，即使設定了 'attribution.commit' 或 'attribution.pr'，也無法控制會話 URL 的插入。"
  - question: "開發者社群要求 Anthropic 進行的正確改進方向為何？"
    choices: ["完全刪除會話 URL 功能", "將預設值改為「不使用（opt-in）」", "提供更長的 URL"]
    answer: 1
    explanation: "使用者持續要求將預設值改為「選擇性開啟（opt-in）」模式，讓使用者在需要時才能啟用。"
lang: zh-tw
ref: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default
---

想像一下：今天早上，為了某個極機密的專案，你正與 AI 編碼助手腦力激盪、編寫程式碼。你甚至叮囑過：「這部分是公司內部機密，絕對不能外洩。」然而幾天後，如果有人進入儲存庫（Repository），無意間點擊了程式碼旁邊的連結，會發生什麼事？透過該連結，你與 AI 的所有對話將會一覽無遺地呈現在對方眼前。

近來，在使用 AI 編碼工具「Claude Code」的開發者之間，這類擔憂正日益擴大。許多人指出，為了開發便利性而引入的功能，竟成為了意料之外的安全事故通道。

### 這為什麼重要？

大多數開發者會將程式碼記錄在 Git 之類的儲存庫系統中。在此過程中，Claude Code 在編寫程式碼後，會自動在提交訊息（Commit，保存程式碼變更紀錄）以及合併請求（PR，請求合併程式碼）的內容中，加入帶有「Claude-Session」字樣的 URL [Source 1, Source 5]。

表面上，這看起來像是「這段程式碼是由 Claude Code 編寫」的來源標註。然而，點擊該連結後，製作該程式碼當時的**完整對話紀錄**將會原封不動地公開 [Source 5]。這不僅包含程式碼，還可能包含非公開專案的企劃內容、安全相關討論，甚至是公司內部的機密對話。如果該儲存庫是公開的，這意味著你的所有思考過程與開發細節都將公諸於世 [Source 5]。

### 簡單比喻：練習簿與便利貼

讓我們用個簡單的比喻來理解這個問題。如果我們編寫的程式碼是「最終成果」，那麼與 AI 的對話就是為了產出該成果而在練習簿上留下的「所有塗鴉與思考痕跡」。

目前 Claude Code 的做法是，當你提交成果時，會將練習簿上寫過的所有內容都寫在便利貼上，並貼在成果旁邊 [Source 6, Source 7]。問題在於，這些便利貼毫不保留地揭露了你曾與誰討論過什麼機密 [Source 5]。

過去開發者常用的「attribution.commit」或「attribution.pr」設定值，原本僅用於標註「此程式碼由 AI 編寫」。然而，這些設定無法控制後來新增、威力強大的資料洩漏功能——「會話 URL」 [Source 3]。

### 使用者為何感到不安？

目前許多開發者對此問題表達了強烈的不滿 [Source 1, Source 9]。特別是在雲端環境中使用 Claude Code 時，即使開發者在本地電腦修改了 Git 設定，也無法阻止伺服器端產生的提交訊息，這讓情況變得更加棘手 [Source 2]。

對此，針對 Claude 開發商 Anthropic 的改進要求正大量湧現 [Source 1, Source 11]。核心訴求是：**「不要預設開啟，請改為使用者有需要時才選擇性加入（opt-in）」** [Source 1, Source 8]。

### 未來會如何發展？

技術提升了我們的生產力，但在過程中，我們不應喪失對「資料主權」的掌控。未來，此功能很有可能會應廣大使用者的要求，從強制性的預設開啟，改進為使用者可自行控制的形式 [Source 8, Source 11]。

如果你目前正在使用 Claude Code，在建立提交或合併請求時，請務必確認你的紀錄暴露到何種程度。一個無意間分享的連結，就可能將你珍貴的創意與機密全部轉為公開 [Source 5]。

### MindTickleBytes AI 記者的觀點

「便利性只有在安全這道圍牆內才有價值。AI 工具若想成為開發者的夥伴，首先應將使用者的『機密維護』視為最基本的信任指標。當工具的底層設計能優先保障使用者保護資訊的權利時，真正的生產力革命才會實現。」

## 參考資料

1. [FEATURE] Session URL appended to commit messages and PR descriptions by default — should be opt-in · Issue #66504 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/66504)
2. attribution setting does not control session URL in commit messages · Issue #41873 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/41873)
3. Is the 'Claude-Session' URL That Claude Code Embeds in Commits Still in Your Repository? (https://zenn.dev/khasegawa/articles/985d970d6cc4a2?locale=en)
4. Stop Claude Code Session URLs From Landing in Your Public Git History (https://outofcontext.dev/blog/claude-code-session-url-attribution/)
5. [BUG] `attribution.sessionUrl` should default to `false` (opt-in) · Issue #76899 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/76899)
6. [Bug] Model leaks private session URL into git commits and PR bodies via Claude-Session trailer · Issue #72557 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/72557)
7. Claude Code Co-Author Commits: What It Is, How to Disable | explainx.ai Blog | explainx.ai (https://www.explainx.ai/blog/claude-code-commit-co-author-attribution-disable-guide-2026)
8. claude-code -(How to fix) Fix [FEATURE]SessionURLappended... (https://www.stepcodex.com/en/issue/feature-session-url-appended-to-commit)
9. ClaudeSessionURLappendedtocommitmessagesandPR... (https://news.ycombinator.com/item?id=49498201)
10. ClaudeSessionKey - Chrome Web Store (https://chromewebstore.google.com/detail/claude-session-key/ppofmhjkjfinjpidlidepeonimpjmadj)
11. How to fixClaudeCode hooks not firing or failing · 7752 Issues & Trend (https://claudeissues.com/topic/hooks-and-automation)
12. ClaudePrevious Response Still Running: Fix It Fast (https://www.digitbin.com/fix-claude-previous-response-still-running/)
13. ClaudeSwitched Models Mid-Conversation? | UsingClaude (https://usingclaude.com/en/guides/troubleshooting/claude-flagged-model-switching)
14. Claude (https://claude.com/)
15. FixClaudeCode "Please run /login" API Error 401 - SmartScope (https://smartscope.blog/en/generative-ai/claude/claude-code-401-auth-error-fix/)