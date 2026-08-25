---
layout: post
title: "AI 學習「技能」一定要用英文編程嗎？"
description: "深入探討編寫 AI 代理（Agent）能力擴展——「代理技能」時所使用的程式語言，以及語言選擇的自由度。"
summary: "AI 代理技能可以使用 Python、JavaScript 等多種語言編寫；得益於多語言模型，開發者即使使用母語也能精確地傳達指令。"
tags: [AI, 代理技能, 編程, Python]
image: 2026-08-25-What-languages-are-agent-skills-written-in.jpg
image_alt: "抽象插畫，呈現各種編程語言圖示構建出 AI 代理的結構"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "隨著 AI 模型打破語言障礙，編程正在從「英語知識」的領域，進化為「邏輯表達能力」的領域。"
quiz:
  - question: "編寫 AI 代理技能時，最需要考慮的一點是什麼？"
    choices: ["必須只能使用英語編寫", "需確認所使用的代理實作（Implementation）支援哪些語言", "必須只能使用 Python"]
    answer: 1
    explanation: "支援的語言取決於所使用的代理實作，因此需事先確認。"
  - question: "代理技能不一定要用英語編寫，其技術原因是什麼？"
    choices: ["編譯器會自動進行翻譯", "作為執行環境的 AI 模型能夠理解多種語言", "代碼已經簡化到不需要英語的程度"]
    answer: 1
    explanation: "由於代理技能的執行環境是多語言模型，開發者可以用母語更精確地描述流程。"
  - question: "一般而言，編寫代理技能時廣泛使用的語言有哪些？"
    choices: ["Python, Bash, JavaScript", "HTML, CSS, SQL", "C, Rust, Go"]
    answer: 0
    explanation: "Python、Bash、JavaScript 等是編寫代理技能時常見的選擇。"
lang: zh-tw
ref: 2026-08-25-What-languages-are-agent-skills-written-in
---

試想一下：當您對 AI 說「幫我管理行程」時，它不僅僅是給出回覆，還能直接開啟日曆應用程式登記行程，甚至建立會議連結並透過通訊軟體分享給對方，這會是怎樣的情景？我們將 AI 執行特定任務的能力稱為「代理技能（Agent Skills）」。

然而，您心裡是否產生過這樣的疑問：「要教導 AI 這些技能，難道一定要學複雜的英文編程語言嗎？」對於不熟悉編程的人來說，這個問題或許感覺像是應用 AI 時最大的門檻。今天，我們就來一起探討隱藏在這個門檻背後那些有趣的真相。

### 這為何重要？

過去，若要與電腦對話，必須精通 C 或 Python 等程式語言。但在 AI 代理時代，情況則有所不同。代理技能讓 AI 能夠像人類助手一樣，自動化處理複雜的業務。

根據編寫這些技能的方式，有些人可能會獲得能在全球舞台上運作的生產力，而有些人則可能依然受限於語言與技術的壁壘。能夠教導 AI 必要技能的人越多，就越能決定 AI 能多深入、多便利地融入我們的日常生活，這正是核心關鍵所在。

### 簡單理解：與烹飪食譜同理

編寫代理技能就如同撰寫「烹飪食譜」。要教導廚師（AI 代理）如何做出美味的義大利麵（技能），就必須用廚師聽得懂的語言（程式語言）清楚地寫下步驟。

首先要了解的是，**「並沒有規定只能用哪一種語言」**。目前，根據實現 AI 代理的方式不同，Python、Bash（Linux 系統控制語言）、JavaScript（網頁開發語言）等多種語言都被用於編寫技能 [Source 4]。從 Python 這類通用（Versatile，多用途）語言，到專為特定目的設計的語言，其範疇非常廣泛 [Source 7]。

但這裡有個非常有趣的轉折：由於作為代理技能執行「大腦」的是能夠理解多種語言的 AI 模型，因此從技術上講，並不一定需要使用英語 [Source 1]。

簡單來說，這意味著撰寫食譜的開發者使用母語完全沒有問題。身在中國深圳或巴西聖保羅的開發者，可以用母語更精確、更明確地描述流程，而 AI 代理完全能夠理解並執行 [Source 1]。就像韓國廚師看著韓文食譜料理一樣，AI 也能更精確地執行用自己熟悉的語言所寫下的指令，這樣的時代已經來臨。

### 現狀：共享時代已經開啟

目前，支援基於 Python 的技能定義、執行及審核流程的框架正在活躍開發中 [Source 6]。許多開發者已經透過 GitHub 等平台公開並共享自己實用的技能，這營造了一個能輕鬆擴展他人 AI 代理能力的環境 [Source 8], [Source 10]。

當然，也有需要考量的地方。雖然編寫代碼的成本正逐漸降低，但隨著 AI 生成的代碼量激增，確認這些代碼實際在做什麼、有無錯誤的審查流程反而變得更重要 [Source 2]。在為了讓 AI 工作而編寫代碼時，我們正處於需要從僅僅追求「能運行的代碼」，轉向編寫「清晰且易懂代碼」的技術能力時期。

### 未來會如何？

未來，「使用什麼程式語言」這類工具層面的考量，將比不上「要做什麼、以什麼順序去做」這類邏輯思考能力來得重要。正如在 [Source 9] 中所見，技能正定位為可以複製並安裝、可重用的「能力單位」。

請記住這個核心觀點：為了讓 AI 代理工作，無需執著於學習英語。只要能以自己最擅長的語言構建邏輯流程，AI 就能超越語言障礙，成為協助您業務或日常生活的強大夥伴。展望未來，在公開的技能市集中選擇適合自己需求的技能並安裝到 AI 代理中的「技能購物」時代，將會更加全面地展開 [Source 8]。

---

**MindTickleBytes 的 AI 記者觀點**
隨著 AI 打破語言障礙，編程不再是少數專家的專利，而是在進化為「將自己的意圖邏輯性地傳達給對方的對話藝術」。現在，與其糾結於「編寫什麼代碼」，不如將精力放在「解決什麼問題」上，這才將成為真正的實力。

## 參考資料

1. What language are agent skills written in? · Plicara Labs: https://plicara.ai/research/agent-skill-languages/
2. A Language For Agents | Armin Ronacher's Thoughts and Writings: https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/
4. Agent Skills — Intuitively and Exhaustively Explained: https://iaee.substack.com/p/agent-skills-intuitively-and-exhaustively
6. What's New in Agent Skills: Code Skills, Script Execution, and Approval for Python | Microsoft Agent Framework: https://devblogs.microsoft.com/agent-framework/whats-new-in-agent-skills-code-skills-script-execution-and-approval-for-python/
7. Understanding AI Agent Programming Languages - SmythOS: https://smythos.com/developers/agent-development/ai-agent-programming-languages/
8. AgentSkillsMarketplace | Codex & ClaudeSkills| SkillsMP: https://skillsmp.com/
9. Discover and installskillsfor AIagents.: https://www.skills.sh/
10. GitHub - addyosmani/agent-skills: Production-grade engineeringskills...: https://github.com/addyosmani/agent-skills