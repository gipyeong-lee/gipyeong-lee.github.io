---
layout: post
title: "我的 AI 助理變聰明了？如何正確使用 Claude Opus 5 與 Fable 5"
description: "介紹如何升級至 Anthropic 的最新 AI 模型 Claude Opus 5 與 Fable 5，並提供優化既有設定的技巧。"
summary: "為配合引入 Anthropic 的新 AI 模型，本文指導如何優化現有的設定檔案，並透過 Claude Code 的 /doctor 功能，將新模型的性能發揮至 100%。"
tags: [AI, Claude, Opus5, Fable5, 生產力]
image: 2026-07-28-Ask-HN-How-to-rewrite-Claudemd-and-install-the-skill-for-Opus5-and-Fable5.jpg
image_alt: "最新 AI 模型 Claude Opus 5 與 Fable 5 的標誌並排展示。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "技術的飛躍總是要求我們隨之調整。不要被工具牽著走，透過優化設定，讓 AI 成為你真正的節奏領跑者。"
quiz:
  - question: "建議使用什麼指令來調整既有的 CLAUDE.md 檔案，以適應最新模型？"
    choices: ["/update", "/doctor", "/optimize"]
    answer: 1
    explanation: "使用 Claude Code 提供的 /doctor 指令，可以針對新模型環境優化技能與 CLAUDE.md 檔案。"
  - question: "下列何者最符合 Claude Fable 5 的特點？"
    choices: ["專為簡易對話設計的模型", "最適合複雜與長週期專案的模型", "專精於影像生成的模型"]
    answer: 1
    explanation: "Claude Fable 5 是一款「Mythos 級別」模型，特別擅長主導複雜且長週期的專案，並能自行驗證成果。"
  - question: "導入 Opus 5 與 Fable 5 時，既有的資源（CLAUDE.md、技能等）該如何處理？"
    choices: ["直接使用即可", "需要根據最新模型進行更新", "應該刪除"]
    answer: 1
    explanation: "舊模型的設定可能無法與最新模型完全相容，因此需要進行重新設定或優化，以符合最新環境。"
lang: zh-tw
ref: 2026-07-28-Ask-HN-How-to-rewrite-Claudemd-and-install-the-skill-for-Opus5-and-Fable5
---

想像一下，你每天使用的 AI 助理突然升級到了最新型的「超級電腦」智慧等級。但當你像往常一樣下達指令時，它的反應卻不如以往聰明。為什麼會發生這種事呢？

Anthropic 最近推出的最新 AI 模型 **Claude Opus 5** 與 **Fable 5** 就是這種情況。這是因為你過去精心設定的助理「指南」與新模型的思維模式存在些許差異。這就像是讓一個已經變得非常聰明的學生，仍然在解「幼兒園等級的作業」。

### 為什麼需要更新？

AI 技術的發展不只是提升模型智慧數值的過程。過去，我們必須對 AI 下達非常具體的指令，而現在，最新模型具備更強大的自我思考與驗證能力。[Claude Fable 5](https://www.anthropic.com/claude/fable) 特別擅長執行複雜且長週期的專案，能提供如同與資深研究員合作般的驚人體驗([Claude Fable 5](https://miniapps.ai/claude-5-fable))。

然而，我們為舊模型編寫的設定檔（`CLAUDE.md`）或自定義技能，可能無法與新模型的工作方式完全相容([來源: Ask HN](https://news.mcan.sh/item/49080135))。換句話說，如果維持舊設定不變，你的助理將無法發揮 100% 的潛力，只能受困於過時的準則而無法展現應有的性能。

### 簡單理解：「馴服」高級助理

試著將 AI 模型的設定檔視為「交給助理的工作手冊」。如果舊手冊是為了執行「簡單雜務」而編寫的，那麼新手冊就必須更新到能具備「策略性決策」的能力。

- **比喻來說**：這就像是你把十年前給新進員工的工作手冊，直接交給現在的部門主管使用。主管希望看到宏觀視角並自行判斷，但手冊上卻只寫著「咖啡要這樣泡」，這效率會很高嗎？
- **設定優化**：Anthropic 建議修改準則，以便善用新模型的特徵，例如調整回應長度、自行判斷並拆解任務的能力等([來源: Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5))。

### 當前狀況：該如何開始？

首先要做的是尋求專家的協助。如果你正在使用 Claude Code，請輸入 `/doctor` 指令。該指令會檢查你的系統是否針對新模型環境進行了正確設定，並自動整理技能與 `CLAUDE.md` 檔案以符合最新環境([來源: The new rules of context engineering](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models))。

1. **更新設定**：你需要根據最新模型的需求，簡化並優化既有的 `CLAUDE.md` 與技能檔案([來源: Anthropic Releases Claude Opus 5](https://www.ghacks.net/2026/07/27/anthropic-releases-claude-opus-5-at-half-the-token-price-of-claude-fable-5/))。
2. **模型選擇**：在新的 Claude Code 工作階段中選擇模型，並根據任務的複雜度調整 effort（努力值）等級以優化性能([來源: Claude code update](https://thevibefather.com/blog/claude-code-opus-5-update-effort-guide))。

### 未來展望

像 Claude Fable 5 這類模型，未來將能理解多達 100 萬 Token（AI 一次能記憶的資訊單位，相當於數十本書的容量）的龐大上下文，並能自主編寫程式碼與完成驗證([來源: Fable5AI](https://fable5.io/))。未來我們將跨越單純的程式設計，迎來與 AI 助理共同設計你的點子，並自行找出與解決複雜錯誤的時代。現在你需要做的，僅僅是將這名強大助理的「手冊」更新至最新版本。

### MindTickleBytes 的 AI 記者觀點
技術總是跑得比我們想像中還快。比起更換工具，更重要的是改變我們操作工具的「提問方式」。用最新的設定喚醒你的 AI，去解決更大的難題吧。

## 參考資料
1. [Ask HN: How to rewrite `Claude.md` and install the skill for Opus5 and Fable5](https://news.mcan.sh/item/49080135)
2. [GitHub - DizzyMii/fable-skills: Six Claude Code skills](https://github.com/DizzyMii/fable-skills)
3. [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
4. [Prompting Claude Opus 5 - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
5. [Claude Opus 5 in Claude Code: A 2026 Guide - codersera.com](https://codersera.com/blog/claude-opus-5-claude-code-guide-2026/)
6. [Claude code update — Using Claude Opus 5 in Claude Code](https://thevibefather.com/blog/claude-code-opus-5-update-effort-guide)
7. [Writing Opus 5 / Fable 5 Prompts - GitHub](https://github.com/CodingCossack/writing-opus-5-fable-5-prompts)
8. [claude-skills/fable-mode/SKILL.md](https://github.com/henriquetell/claude-skills/blob/main/fable-mode/SKILL.md)
9. [GitHub - samirinyemi/fable5-skill-library](https://github.com/samirinyemi/fable5-skill-library)
10. [Hacker News | Ask HN](https://nilaykhandelwal.com/item/49080135)
11. [Claude Opus 5 Is Powerful. Your Setup Decides How Powerful](https://emergingai.substack.com/p/claude-opus-5-is-powerful-your-setup)
12. [Karpathy's CLAUDE.md Skills File: The Complete Guide](https://agentpedia.codes/blog/karpathy-claude-code-skills-guide)
13. [Migration guide - Claude Platform Docs](https://platform.claude.com/docs/en/about-claude/models/migration-guide)
14. [Claude](https://claude.com/)
15. [Claude Fable | Anthropic](https://www.anthropic.com/claude/fable)
16. [Fable5AI — Independent Model Guide & Prompt Workspace](https://fable5.io/)
17. [Claude Opus 5 review: great at coding (but I hate talking to it)](https://www.youtube.com/watch?v=dfre9hN0HCs)
18. [GitHub - alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
19. [Claude Fable 5 · Free AI Chatbot](https://miniapps.ai/claude-5-fable)
20. [Anthropic Releases Claude Opus 5 at Half the Token Price of Claude Fable 5 - gHacks TechNews](https://www.ghacks.net/2026/07/27/anthropic-releases-claude-opus-5-at-half-the-token-price-of-claude-fable-5/)