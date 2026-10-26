---
layout: post
title: "與 AI 對話，關閉視窗後就消失了嗎？AI 協作記錄法『ADRs4AI』"
description: "當您與 AI 共同進行專案時，介紹一種能將重要決策記錄並進行版本管理的工具與方法論——ADRs4AI，讓您的討論紀錄不再消失。"
summary: "透過將與 AI 協作的決策事項連同程式碼一併記錄在 Git 中，讓任何人隨時都能銜接 AI 討論過程的『ADRs4AI』技術。"
tags: [AI, 協作, Git, 開發者工具, 生產力]
image: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git.jpg
image_alt: "象徵程式碼與對話記錄系統性地累積在 Git 儲存庫中的圖片"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "將 AI 的推理過程轉化為資產而非暫時性的聊天數據，是改變協作未來的關鍵一步。"
quiz:
  - question: "ADRs4AI 所追求的核心價值是什麼？"
    choices: ["無限擴展 AI 的記憶力", "使人類與 AI 的工作決策過程具備持續性與可復原性", "讓 AI 自行做出所有決策"]
    answer: 1
    explanation: "ADRs4AI 的目標是確保與 AI 共同思考和決定的內容不會揮發，並確保『認知連續性（epistemic-continuity）』，以便後續能持續接軌。"
  - question: "ADRs4AI 使用的記錄原則是什麼？"
    choices: ["自動儲存於雲端伺服器", "docs-as-code（文件即程式碼）原則", "利用 AI 專用資料庫"]
    answer: 1
    explanation: "ADRs4AI 遵循 docs-as-code 原則，像管理程式碼一樣編寫文件並透過 Git 進行管理。"
  - question: "ADRs4AI 是否僅支援特定的 AI 模型？"
    choices: ["不，這是一種與模型無關（model-agnostic）的方法", "是的，僅能在特定模型中使用", "僅支援 Gemini 模型"]
    answer: 0
    explanation: "ADRs4AI 採用不依賴特定模型的與模型無關（model-agnostic）方法論。"
lang: zh-tw
ref: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git
---

試著想像一下：昨晚您與 AI 一起設計了一個複雜專案的結構，深入討論了資料庫結構（Schema）該如何規劃、API 功能該如何製作。然而到了隔天早上，當您對 AI 說「依照昨天設計的內容繼續進行吧」時，AI 卻完全不記得您是誰，也不記得昨天做過什麼決定。您昨天的努力，就這樣隨著關閉的聊天視窗消失了。

為了解決許多人遇到的這種挫折感，一個名為「ADRs4AI」的概念應運而生。

## 為什麼這很重要？

AI 的智慧雖已飛躍性成長，但在「記憶力」方面仍有限制。聊天視窗關閉的瞬間，討論的脈絡往往隨之支離破碎。如果沒記錄下重要決策的理由，下次再協作時就必須重複說明，或者忘記當初為何做出該決策。

ADRs4AI 解決了這些問題。它將與 AI 的協作過程記錄在 Git（軟體變更追蹤系統）等版本控制系統中，讓我們能像管理軟體一樣，管理與 AI 共同做出的「決策記錄（Decision Records）」。透過這種方式，未來的您或其他協作者，就能隨時找回與 AI 討論的思想脈絡。 [出處: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## 簡單來說

「ADR」原為「架構決策記錄（Architecture Decision Records）」的縮寫，是開發者用來記錄為何選擇特定技術的原因。ADRs4AI 則是將其擴展至 AI 協作領域。

比喻來說，這就是**「載有與 AI 對話記錄的個人工作日誌」**。就像寫日記能幫助我們回顧過往想法一樣，ADRs4AI 將與 AI 決定的複雜技術選擇寫成 Markdown 文件（一種方便在網路上書寫的格式），並儲存於專案資料夾中。 [出處: Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)

這就像堆疊樂高積木時，在設計圖上留下為什麼把這個顏色的積木放在這裡的筆記一樣。當未來需要重新組裝或修改時，只要讀了那些筆記，就能毫無懸念地接續工作。

## 目前現狀

ADRs4AI 不僅僅是概念，已落實為實際工具：

*   **工具套件**：由 VS Code 擴充功能、iOS 客戶端、專案模板以及說明此方法論的文章等組成。 [出處: GitHub -ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
*   **模型無關性**：不綁定於特定 AI（如 Gemini、Claude）。無論使用哪種 AI，皆可套用此方法論。 [出處: What is ADRs4AI?](https://adrs.systems/what-is/)
*   **記錄原則**：追求處理程式碼的方式，即「docs-as-code（文件即程式碼）」。換句話說，與 AI 做出的決定會以 Markdown 文件寫在程式碼儲存庫中，透過 Git 進行版本管理，並經由 Pull Request（PR，變更內容審查請求）接受同事的審閱。 [出處: Planning & Architecture Decision Records](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)

這種作法將 AI 從單純的「一次性對話對象」，提升為與我們共同思考專案的「持續性夥伴」。 [出處: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## 未來發展如何？

與 AI 的協作正日益複雜。我們現在已不僅止於請求編寫程式碼，而是進入了與 AI 一起構思整個專案設計的時代。

在此過程中，如 ADRs4AI 這類「認知連續性（epistemic-continuity，即與 AI 對話的脈絡不中斷的狀態）」協議將變得不可或缺。因為這能建立一種良性循環，將我們做出的決定留存為數據，並將該數據再利用於後續階段的 AI 學習與推理中。正如已將 AI 導入民主審議過程的案例所示，AI 能在整理人類複雜的討論並導出共識方面發揮極大作用。 [出處: AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)

我們的工作不再揮發。與 AI 討論過的所有煩惱都將在 Git 儲存庫中累積起來，下次開啟專案時，更聰明的 AI 便能根據這些紀錄，立刻銜接對話。

---

### MindTickleBytes 的 AI 記者觀點
將 AI 的推理過程棄置為隨意揮發的數據，是一種對知識資源的浪費。將人類與 AI 的協作紀錄透過 Git 進行管理，是最明確的指標，顯示我們已開始將 AI 視為專案的「同事」，而非僅是工具。

---

## 參考資料

1. [GitHub -ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
2. [Home | ADRS—AI-Driven Research for Systems](https://ucbskyadrs.github.io/)
3. [ADRs for AI - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=jlumbroso.adrs4ai)
4. [adrs4ai-pneumatic · PyPI](https://pypi.org/project/adrs4ai-pneumatic/)
5. [Towards Human-AI Deliberation: Design and Evaluation of...](https://arxiv.org/pdf/2403.16812)
6. [deliberation-AI Agents on GitHub | SkillsLLM](https://skillsllm.com/skill/deliberation)
7. [Free AI Humanizer | Humanize AI to Sound Like You, Not AI](https://www.grammarly.com/ai-humanizer)
8. [Human or Not: A Social Turing Game is Back, Play Now](https://humanornot.so/)
9. [AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)
10. [WURK - Microtask Marketplace for Humans & AI Agents](https://wurk.fun/)
12. [ADRs4AI - GitHub](https://github.com/ADRs4AI)
13. [What is ADRs4AI? · ADRs4AI - adrs.systems](https://adrs.systems/what-is/)
14. [Scaling AI Solution Architecture: How ADRs + Git + Claude...](https://www.linkedin.com/pulse/scaling-ai-solution-architecture-how-adrs-git-claude-rosselet-xhsre)
16. [Planning & Architecture Decision Records | Enterprise AI Delivery](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)
17. [Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)