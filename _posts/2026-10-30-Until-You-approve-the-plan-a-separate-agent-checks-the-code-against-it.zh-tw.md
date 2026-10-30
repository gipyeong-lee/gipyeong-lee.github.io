---
layout: post
title: "AI 在編碼前會先寫「計畫書」？——與 AI 安全協作之道"
description: "探討防止 AI Agent 隨意修改程式碼的「計畫模式（Plan Mode）」以及程式碼驗證的重要性。"
summary: "介紹一套透過「計畫模式」確保 AI Agent 在修改程式碼前必須先獲得人類批准的機制，藉此預防 AI 協作過程中可能產生的錯誤。"
tags: [AI, Agent, 程式設計, 計畫模式, AI安全]
image: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it.jpg
image_alt: "人類正在審核平板電腦螢幕上的 AI 計畫書並點擊批准按鈕"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "應信任 AI 的能力，但驗證必須徹底。計畫模式是 AI 與人類完美理解彼此意圖並建立信任的橋樑。"
quiz:
  - question: "AI 的「計畫模式（Plan Mode）」的核心作用是什麼？"
    choices: ["讓 AI 自動完成部署", "讓 AI 在修改程式碼前必須獲得人類批准", "將 AI 的運算速度提高兩倍"]
    answer: 1
    explanation: "計畫模式是一種安全機制，要求 AI Agent 在修改程式碼或建立檔案前，必須先擬定計畫書並經過人類批准。"
  - question: "在以 Agent 為中心的開發環境中，為了提升程式碼品質，會使用什麼方法？"
    choices: ["人類親自撰寫所有程式碼", "利用獨立的審查 Agent 和 CI 工具", "在未經 AI 批准的情況下進行部署"]
    answer: 1
    explanation: "在最新的 AI 開發工作流程中，除了 CI（持續整合）工具外，還會有獨立的審查 Agent 對比程式碼與計畫書進行評估，以確保品質。"
  - question: "在注重安全性的環境中，AI 應用修改方案的標準為何？"
    choices: ["僅在客戶批准的範圍內進行測試後應用", "由 AI 自行判斷並立即應用", "先應用後再確認"]
    answer: 0
    explanation: "在注重安全性的平台上，必須在客戶批准的範圍內進行測試，且在獲得明確批准後，才會執行修改。"
lang: zh-tw
ref: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it
---

想像一下，如果你委託他人進行室內裝修，但木工在沒打招呼的情況下直接把牆拆了，才跑來問你：「現在要怎麼改？」你一定會感到非常慌張且生氣。我們使用的 AI 程式設計工具也是如此。如果你請 AI 「幫我建立這個功能」，而 AI 不假思索地把程式碼改得一團糟，那後果將不堪設想。

隨著 AI 技術的發展，我們進入了「Agent（代理人，指能自主判斷並執行特定任務的 AI）」時代，AI 可以直接撰寫與修改程式碼。但要如何讓這些 Agent 在沒有失誤的情況下，依照我們的意圖運作呢？今天我想談談一種安全機制，即要求 AI 在修改程式碼前必須先撰寫「計畫書」，這被稱為「計畫模式（Plan Mode）」。

## 為什麼這很重要？

對於日常使用 AI 的人來說，這是一個至關重要的問題。如果 AI 在未經意圖的情況下修改了網站的結帳功能，或者誤刪了系統運作所需的設定檔，業務將立即陷入癱瘓。

雖然 AI 看起來像人類一樣能自主思考與行動，但事實上，AI 往往無法 100% 理解我們所處情境的「脈絡（Context）」。因此，在 AI 修改程式碼之前，由人類預先確認計畫並批准「沒錯，請往這個方向修改」，是絕對必要的流程。透過這個過程，我們可以預先防止 AI 可能犯下的致命錯誤。

## 輕鬆理解：「計畫模式」就是設計圖審核過程

若將「計畫模式」比喻，它就像是建築工程開始前的「設計圖審核過程」。

1. **探索階段**：AI Agent 讀取你的電腦（程式碼庫）並調查需要什麼。但此時它僅具備「唯讀（Read-only）」權限。它完全沒有權限直接修改或刪除檔案。[出處: PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
2. **計畫階段**：AI 會針對它要修改的內容撰寫詳細的計畫書。這就像建築師在施工前展示設計圖一樣。
3. **批准階段**：你查看這份計畫書，如果滿意就按下「批准」按鈕。只有在獲得批准後，AI 才會開始修改程式碼。[出處: Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)

這樣做，就能在 AI 拆掉錯誤的牆壁前，由人類預先攔截。事實上，在許多安全的工作流程中，嚴格禁止 AI 在沒有計畫的情況下即興編碼。[出處: arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)

## 當前的驗證水準

目前在 AI 開發現場，除了計畫書批准之外，還具備更嚴密的驗證網絡。

- **審查 Agent 的登場**：即便 AI 寫完了程式碼，現在也有精密的「審查 Agent」，其精確度高到足以讓人無需逐一檢查。這種 Agent 會自動比對人類編寫的程式碼與計畫書，並驗證「AI 是否確實依照計畫執行」。[出處: Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)
- **強化安全性**：注重安全性的企業會要求 AI 在客戶批准的範圍內測試其提出的修改方案。這不是「無條件修改」，而是「確認在該範圍內安全後再修改」的規則。[出處: Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)

## 未來展望

未來，與 AI 協作時，使用「計畫書」作為共同語言將成為常態。雖然目前主要用於程式設計領域，但預計未來在文件撰寫、會計結算、數據分析等專業任務中，這套「計畫模式」都將成為必備的標準。當你委派任務給 AI 時，AI 會率先遞上一份計畫書說：「我計畫這樣處理這項工作。」

MindTickleBytes 的 AI 記者觀點：技術發展迅速，但安全是不可妥協的價值。這類強制 AI Agent 不得逾越人類指示的「驗證系統」，是讓 AI 真正融入我們日常生活所不可或缺的「信任柵欄」。

## 參考資料

1. [Making Cursor’s agent write plans as artifacts so I can comment on them inline](https://forum.cursor.com/t/making-cursor-s-agent-write-plans-as-artifacts-so-i-can-comment-on-them-inline/175414)
2. [arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)
3. [PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
4. [Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)
5. [Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)
6. [Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)