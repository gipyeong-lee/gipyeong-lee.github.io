---
layout: post
title: "停止對 AI 說「拜託了」？超越「氛圍編碼」，邁向真正的工程學"
description: "透過為 AI 開發代理引入「代理技能 (Agent Skills)」，了解如何讓編碼變得更系統化、更專業。"
summary: "對 AI 下達模糊指令的「氛圍編碼 (Vibecoding)」時代即將結束，直接將經過驗證的工程程序學習給 AI 代理的「代理技能」框架正受到矚目。"
tags: [AI, 編碼, 開發者, 生產力, 代理技能]
image: 2026-09-02-AI-Coding-Agent-Skills-for-Real-Engineers.jpg
image_alt: "各種軟體開發流程圖示與 AI 代理有機連接的現代數位工作流程圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "依賴直覺的 AI 開發正進化為精密的標準程序。這是將 AI 從單純工具轉變為團隊一員的必要過程。"
quiz:
  - question: "AI 開發方式中，「氛圍編碼 (Vibecoding)」的特徵是什麼？"
    choices: ["遵守嚴格的品質檢核閘道", "以對 AI 下達模糊指令的方式", "系統化的自動化過程"]
    answer: 1
    explanation: "氛圍編碼是指在沒有具體工程程序的情況下，對 AI 說「拜託了」之類模糊指令進行編碼的方式。"
  - question: "將「代理技能 (Agent Skills)」安裝到專案時，主要使用的路徑在哪裡？"
    choices: ["/root/data", "/.claude/skills", "/home/ai/config"]
    answer: 1
    explanation: "代理技能安裝在專案的本地目錄中，主要是 '.claude/skills'，以便使用。"
  - question: "正確排列 AI 編碼代理的發展過程為何？"
    choices: ["自動完成(2024) -> 多檔案編寫(2025) -> 系統化工程框架(2026)", "系統化工程框架(2024) -> 自動完成(2025) -> 多檔案編寫(2026)", "多檔案編寫(2024) -> 系統化工程框架(2025) -> 自動完成(2026)"]
    answer: 0
    explanation: "AI 編碼工具已從 2024 年的自動完成、2025 年的多檔案編寫，發展至 2026 年系統化的代理工程框架。"
lang: zh-tw
ref: 2026-09-02-AI-Coding-Agent-Skills-for-Real-Engineers
---

想像一下。今天早上，您想將專案中一項複雜的功能交給剛加入團隊的初級開發人員。但是，如果您對該開發人員說：「呃……就拜託您隨便做個帥氣一點的成果出來」，會發生什麼事呢？幾天後，您可能會收到一段完全背離意圖、甚至難以維護的混亂程式碼。

最近出現在我們身邊的「AI 編碼代理」其實也沒什麼不同。過去，許多人在指揮 AI 寫程式時，都依賴「拜託寫好一點」這種模糊指令，也就是所謂的 **「氛圍編碼 (Vibecoding，指在沒有具體工程程序的情況下，對 AI 憑直覺進行指示的編碼方式)」** [Source 1, Source 6, Source 9]。然而，那個時代即將過去。

## 為什麼這很重要？

「氛圍編碼」雖然看起來能在眼前快速產出程式碼，但在實務現場卻隱藏著巨大的風險。因為難以追蹤是誰、透過什麼流程編寫了程式碼，且當問題發生時，也沒有解決問題的標準程序[Source 1]。

比喻來說，這就像駕駛汽車時，不遵守交通號誌或車道等法規，僅憑駕駛員的心情隨意駕駛一樣。發生事故時難以釐清原因，在旁人看來也極度不安。如果我們希望所使用的 AI 代理不僅僅是一個生成程式碼的「自動生成器」，而是能像實際管理產品、進行維護的「真正工程師」一樣行動，就需要建立一套系統化的體系。進入 2026 年後出現的「代理工程框架」，正徹底改變透過 AI 進行軟體開發的方式，使其變得更加系統化 (systematic) [Source 16]。現在，開發人員不再任由 AI 隨意寫程式碼，而是將資深開發者數十年累積的專業知識，以「技能 (Skills)」的形式教授給 AI。

## 輕鬆理解：什麼是「代理技能」？

**代理技能**簡單來說，就是傳達給 AI 代理的 **「超精密業務手冊」** [Source 5]。

比喻來說，這就像給新進開發人員一份公司使用的 **「業務指南」**。與其只說「寫程式吧！」，不如明確指出具體的程序：「先依照這種順序建立計畫，必須通過這個品質檢核階段，若發生問題則以這種方式修改」[Source 2]。

裝備了這種「技能」的 AI 會以下列方式運作：

1. **安裝**：開發人員將自己想要的特定工程程序（技能）安裝在專案內部的資料夾（例如：`.claude/skills`）[Source 5, Source 8, Source 14]。
2. **命令**：當開發人員輸入斜線指令（例如：`/run-tdd`）時，AI 就會完美執行該技能中記錄的程序[Source 5, Source 10]。
3. **執行**：AI 會自行規劃、檢視中間結果，並努力維持人類工程師所期待的品質水準[Source 2]。

這就像為照片應用程式套上數十種濾鏡一樣，讓您可以自由組合 AI 代理所需的專業工程技能來使用[Source 7]。

## 現狀：進展到什麼程度了？

AI 編碼工具的發展正以驚人的速度飛躍[Source 19]。

*   **2024 年**：從單純的自動完成 (Autocomplete) 層級的輔助工具開始[Source 16]。
*   **2025 年**：隨著 Claude Code 等工具登場，發展到可以同時處理多個檔案的層級[Source 16]。
*   **2026 年**：目前已經到達透過代理技能將 AI 的行動方式本身「標準化」的階段[Source 16]。

許多專家已經引進這些代理技能，每天在實際生產環境中進行編碼[Source 1, Source 13]。那個不再需要對 AI 說「隨便怎麼做都好」的時代已經來臨。

## 未來會如何發展？

未來，AI 代理將會越來越像團隊中專業的同事。不僅限於編碼技能，預計在銷售、行銷、法律等各領域中，具備各自自動化工程技能的 AI 代理都將大顯身手[Source 16]。

在軟體開發領域，將會有更多人為開源代理技能生態系做出貢獻，每個團隊也將建立起蘊含自身「開發哲學」的技能組合。現在，開發人員的能力與其說是取決於「親手寫程式碼」，不如說是取決於「能教導 AI 多精確、多高效的工程程序（技能）」，這句話一點也不為過。

---

**MindTickleBytes 的 AI 記者觀點**

期待 AI 擁有「氛圍」雖然浪漫，但在商業上卻很危險。引進代理技能是將 AI 從單純聽命行事的「工具」，轉變為值得信賴且「可驗證的專業人力」的第一步。現在，編碼已經超越了「如何實作」的問題，演變成「採取何種程序」的問題。

## 參考資料
1. [GitHub - mattpocock/skills: Skills for Real Engineers](https://github.com/mattpocock/skills)
2. [Production-grade engineering skills for AI coding agents](https://github.com/addyosmani/agent-skills)
3. [Skills For Real Engineers — AI agent skills | Surf Skills](https://surfskills.surf/s/mattpocock/skills)
4. [AI Coding for Real Engineers](https://www.aihero.dev/cohorts/ai-coding-for-real-engineers-m0k0w)
5. [AI Skills for Real Engineers](https://www.aihero.dev/skills)
6. [Matt Pocock Skills: AI Agent Tools for Real Engineering](https://aitoolly.com/ai-news/article/2026-04-29-matt-pocock-releases-skills-repository-professional-ai-agent-workflows-for-real-world-engineering-an)
7. [Skills for Real Engineers: Empower AI coding agents](https://www.opensourcealternatives.to/item/skills-for-real-engineers)
8. [GitHub - kroffske/grillme: Skills for Real Engineers](https://github.com/kroffske/grillme)
9. [Matt Pocock 的 Agent Skills 16 個 — Real Engineering, Not Vibe Coding](https://qjc.app/blog/matt-pocock의-agent-skills-16개-real-engineering-not-vibe-coding)
10. [Discover and install skills for AI agents.](https://www.skills.sh/)
12. [Полный гайд по Qwen CLI: настраиваем MCP, Agent Skills и Rules](https://frontendtales.ru/ru/blog/vibecoding-with-qwen-cli)
13. [Skills for Real Engineers — навыки для AI-агентов от Мэтта Пакокка](https://ai4coding.ru/solutions/mattpocock-skills)
14. [Emil Design Eng | ClaudeCodeSkills](https://claudemarketplaces.com/skills/emilkowalski/skill/emil-design-eng)
15. [AI Engineering Trends in 2025: Agents, MCP and Vibe Coding](https://thenewstack.io/ai-engineering-trends-in-2025-agents-mcp-and-vibe-coding/)
16. [Agent Skills Framework Revolution: Vibe Coding to Real Engineering](https://byteiota.com/agent-skills-framework-revolution-vibe-coding-to-real-engineering/)
17. [What It Takes to Build AI Skills Engineers Need in 2025](https://ralabs.org/blog/what-it-really-takes-to-build-ai-skills-that-matter/)
19. [Latest AI Coding Tools | agprojects](https://agprojects.tech/blog/latest-ai-coding-tools-what-s-new-in-2025)