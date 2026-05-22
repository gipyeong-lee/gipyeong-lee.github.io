---
layout: post
title: "把編碼交給 AI 卻一團糟？從「設計圖 (Spec)」開始寫起就會大不相同"
description: "探索如何正確運用 AI 編碼助手 Claude Code，了解規格驅動開發 (SDD) 工作流。"
summary: "擺脫單純透過對話指示編碼的方式，優先編寫明確的設計圖並細分任務的「規格驅動開發 (SDD)」正成為 AI 編碼的新標準。"
tags: [AI編碼, Claude Code, 規格驅動開發, 軟體開發, AI生產力]
image: 2026-05-22-Show-HN-Spec-Driven-Development-Workflow-for-Claude-Code.jpg
image_alt: "以柔和插圖表現建築師攤開複雜藍圖並與機械手臂共同作業的樣貌"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人工智慧並非魔杖，而是優秀的幫手。我們再次體認到一個理所當然的真理：若要讓幫手發揮實力，我們必須先提供明確的「需求」藍圖。"
quiz:
  - question: "根據本文說明的「規格驅動開發 (SDD)」核心原則之一，為了防止 AI 產生混淆，每一階段會執行的操作是什麼？"
    choices: ["清除 AI 的上下文（記憶）", "購買效能更高的電腦", "將代碼編寫速度提升 2 倍"]
    answer: 0
    explanation: "在 SDD 工作流中，會在階段之間清除 AI 先前的對話脈絡（上下文），使 AI 能完全專注於特定的子任務。"
  - question: "指稱過去那種在沒有計畫的情況下，盲目要求 AI 編寫代碼的方式之術語為何？"
    choices: ["感覺編碼 (Vibe coding)", "規格驅動開發 (SDD)", "結對編程 (Pair programming)"]
    answer: 0
    explanation: "將沒有任何說明書、僅憑心情或感覺下達對話式指令的方式稱為「感覺編碼 (Vibe coding)」。"
  - question: "開發者 Pimzino 強調規格驅動開發中絕對不可妥協 (non-negotiable) 的必要過程是什麼？"
    choices: ["規劃階段與實作階段的分離", "無條件僅使用 Python 語言", "無視 AI 的錯誤"]
    answer: 0
    explanation: "Pimzino 強調，將設計（規劃）階段與實際編寫代碼的實作階段明確分開執行，是 AI 編碼成功的必要條件。"
lang: zh-tw
ref: 2026-05-22-Show-HN-Spec-Driven-Development-Workflow-for-Claude-Code
---

想像一下，為了建造夢想中的獨棟洋房，你聘請了資深的建築師與施工承包商。但到了現場你卻這麼說：「喂，幫我蓋一棟住起來舒服又漂亮的兩層樓房子就好。廚房要寬敞一點，採光要好。既然你是專家，就拜託你處理了！」

結果會如何呢？或許客廳正中央會莫名其妙放了個馬桶，或者通往二樓的階梯竟然荒唐地被天花板封死，最終蓋出一棟令人傻眼的房子。

到目前為止，我們在使用人工智慧 (AI) 編碼助手時，一直沿用精確的這種方式。我們對 ChatGPT 或 Claude 這樣的 AI 在對話框隨口丟一句「幫我做一個有這種功能的 App」，然後期待 AI 會像變魔術一樣，瞬間吐出完美的程式碼。專家們將這種沒有明確計畫或說明書、僅憑心情或感覺下達指令的方式稱為 **「感覺編碼 (Vibe coding)」** [[從感覺編碼到出貨：我的規格驅動工作流... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code), [使用 Claude Code 進行規格驅動開發：正確構建](https://solguruz.com/blog/spec-driven-development-with-claude-code/)]。

然而，最近在軟體開發者之間，一種處理「Claude Code (專為編碼設計的 AI 代理工具)」的全新方法正成為熱門話題。這就是 **規格驅動開發 (Spec-Driven Development，以下簡稱 SDD)**，它不盲目要求 AI 編寫代碼，而是要求先從精細的「設計圖 (Spec)」開始寫起 [[Claude Code 規格驅動開發實作指南](https://github.com/papaoloba/spec-based-claude-code)]。

## 為什麼這很重要？ (Why It Matters)

當 AI 號稱能包辦所有編碼工作時，我們曾歡呼作業速度將瞬間提升數十倍。但現實卻大不相同。只要專案稍微變得複雜，與 AI 的協作很快就會變成沉重的負擔 (cumbersome) [[Claude Code：規格驅動開發 (SDD)](https://mifkata.com/blog/2026/01/claude-code-spec-driven-development/)]。這是因為 AI 常會忘記前後脈絡，或者修好這一頭卻搞壞另一頭的情況不斷發生。

事實上，一位業界開發者坦言，導入 AI 助手並僅以對話方式下達指令時，生產力反而下降了 19%，經歷了所謂的「生產力放緩 (slowdown)」 [[從感覺編碼到出貨：我的規格驅動工作流... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)]。這是因為人類必須耗費更多時間去逐一找出被搞砸的代碼並進行收尾與除錯 (error correction)。

然而，在將工作方式轉變為「規格驅動開發 (SDD)」後，這 19% 的損失奇蹟般地轉化為實質的生產力提升 (real lift) [[從感覺編碼到出貨：我的規格驅動工作流... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)]。我們對 AI 的要求不是玩具，而是實際客戶可以使用、具備高度穩健性 (production-ready) 的程式。為此，維持專業開發慣例 (professional software development practices) 的 SDD 是必不可少的 [[Claude Code 規格驅動開發實作指南](https://github.com/papaoloba/spec-based-claude-code)]。

## 輕鬆理解 (The Explainer)

規格驅動開發 (SDD) 的核心在於將巨大的任務犀利地拆解為兩個維度 (two dimensions) [[Show HN: Claude Code 的規格驅動開發工作流](https://news.ycombinator.com/item?id=48231575)]。

**1. 徹底的事前調查 (Research)**
就像蓋房子前要檢查土地狀態一樣，投入多個 AI 代理對當前系統的狀態與問題進行多維度分析 [[實戰 Claude Code 規格驅動開發 | alexop.dev](https://alexop.dev/posts/spec-driven-development-claude-code-in-action/)]。

**2. 編寫堅實的設計圖 (Spec Creation)**
這是最重要的階段。根據調查結果，製作包含需求 (requirements) 與系統設計的說明書文檔 [[Show HN: Claude Code 的規格驅動開發工作流](https://news.ycombinator.com/item?id=48231575)]。這成了人類與 AI 之間堅不可摧的書面合約 (written spec contracts) [[Claude Code 規格驅動開發](https://greeto.me/blog/spec-driven-development-claude-code-in-action)]。

**3. 任務碎片化 (Task Decomposition)**
再聰明的 AI 也無法一次完成複雜的系統。將整體任務拆解成極小單位的子任務 (subtasks) [[Show HN: Claude Code 的規格驅動開發工作流](https://news.ycombinator.com/item?id=48231575)]。

**4. 階段性實作與驗證 (Implementation & Verification)**
按順序逐一執行拆解後的任務並編寫代碼。此時不採取一次性儲存，而是使用以具有意義的最小單位進行儲存的原子化提交 (atomic commits) 方式，以提升安全性 [[Claude Code 規格驅動開發](https://greeto.me/blog/spec-driven-development-claude-code-in-action)]。

**打個比方：**
在會議室白板上寫滿各種點子並結束討論後，現在必須具體專注於「窗戶設計」這一件事，但如果白板上還殘留著「屋頂顏色」或「管線位置」之類的塗鴉會如何？作業者難免會產生混淆。

因此，SDD 的原則是在每一階段結束後，都要 **「完全清除 AI 的上下文（記憶脈絡）(clear context)」** [[Show HN: Claude Code 的規格驅動開發工作流](https://news.ycombinator.com/item?id=48231575)]。讓腦袋變回一張白紙，只重新遞給它剛完成的「設計圖」與「當下的目標」。這樣一來，AI 就不會陷入幻覺（Hallucination，將錯誤資訊說得煞有其事的現象），而是能專注於眼前的任務。

## 現況如何？ (Where We Stand)

隨著這種方式的效果得到證實，全球開發者正陸續推出將此過程自動化的工具。

*   **ShipSpec：** 開發者無需親自撰寫設計圖，AI 會分析專案並自動生成 3 個文檔檔案作為設計圖 [[Show HN: Claude Code 的規格驅動外掛](https://news.ycombinator.com/item?id=46591238)]。
*   **sddw：** 讓負責編碼的 AI 親自為自己的任務編寫設計圖。幫助它自行制定計畫並以小單位 (atomic tasks) 處理工作 [[規格驅動開發工作流：如何從 AI 獲取生產等級代碼...](https://www.linkedin.com/pulse/spec-driven-development-workflow-how-get-code-from-ai-makarevych-xolxf)]。
*   **claude-code-spec-workflow：** 開發者 Pimzino 公開的這個套件在 GitHub 上獲得超過 3,700 個星，極受歡迎 [[GitHub - Pimzino/claude-code-spec-workflow: 自動化工作流...](https://github.com/Pimzino/claude-code-spec-workflow)]。Pimzino 強調：「將規劃階段與實作階段分開是不可妥協 (non-negotiable) 的必要條件」 [[使用 Claude Code 進行規格驅動開發 | Build This Now](https://www.buildthisnow.com/blog/guide/mechanics/spec-driven-development)]。

## 未來展望 (What's Next)

未來的開發者將不再是在電腦前熬夜，而是口述自己的點子。接著 AI 會分析該語音並撰寫完美的「設計圖 (Spec)」，在自主編寫代碼後完成測試。事實上，全球企業 Notion 已經在內部構建了這種方式的 AI 工作流 [[規格驅動開發：Notion 的 AI 工程工作流](https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering)]。

最終，人工智慧正超越單純接受命令的打字機，進化為能夠自我計畫與驗證的自我發展 AI 系統 (Self-Developing AI System) [[為 Claude 構建規格驅動工作流的配置驅動方法...](https://www.linkedin.com/pulse/config-driven-way-build-spec-driven-workflows-claude-code-makarevych-qjmwf)]。我們正告別衝動的「感覺編碼」，迎來成為繪製大藍圖的「總建築師」，指揮 AI「建築機器人」軍團的時代。

## AI's Take
人工智慧並非魔杖，而是優秀的幫手。我們再次體認到一個理所當然的真理：若要讓幫手發揮實力，我們必須先提供明確的「需求」藍圖。

## 參考資料
1. [實戰 Claude Code 規格驅動開發 | alexop.dev](https://alexop.dev/posts/spec-driven-development-claude-code-in-action/)
2. [GitHub - Pimzino/claude-code-spec-workflow: 自動化工作流...](https://github.com/Pimzino/claude-code-spec-workflow)
3. [為 Claude 構建規格驅動工作流的配置驅動方法...](https://www.linkedin.com/pulse/config-driven-way-build-spec-driven-workflows-claude-code-makarevych-qjmwf)
4. [從感覺編碼到出貨：我的規格驅動工作流... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)
5. [Claude Code 規格驅動開發](https://greeto.me/blog/spec-driven-development-claude-code-in-action)
6. [Claude Code：規格驅動開發 (SDD)](https://mifkata.com/blog/2026/01/claude-code-spec-driven-development/)
7. [Claude Code 規格驅動開發實作指南](https://github.com/papaoloba/spec-based-claude-code)
8. [使用 Claude Code 進行規格驅動開發：正確構建](https://solguruz.com/blog/spec-driven-development-with-claude-code/)
9. [使用 Claude Code 進行規格驅動開發 | Build This Now](https://www.buildthisnow.com/blog/guide/mechanics/spec-driven-development)
10. [使用 Claude Code 進行規格驅動開發：導引教程](https://www.datacamp.com/tutorial/spec-driven-development-with-claude-code)
11. [Show HN: Claude Code 的規格驅動開發工作流](https://news.ycombinator.com/item?id=48231575)
12. [Claude Code 規格工作流指南 (2026) | ClaudHQ](https://claudhq.com/claude-code-spec-workflow-guide/)
13. [規格驅動開發工作流：如何從 AI 獲取生產等級代碼...](https://www.linkedin.com/pulse/spec-driven-development-workflow-how-get-code-from-ai-makarevych-xolxf)
14. [ClaudeEngineer 太瘋狂了... 升級你的 Claude Code 工作流](https://www.youtube.com/watch?v=6Rg5M69bMgQ)
15. [Show HN: Claude Code 的規格驅動外掛](https://news.ycombinator.com/item?id=46591238)
16. [規格驅動開發：Notion 的 AI 工程工作流](https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering)