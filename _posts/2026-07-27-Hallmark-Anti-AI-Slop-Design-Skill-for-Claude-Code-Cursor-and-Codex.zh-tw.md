---
layout: post
title: "為什麼 AI 做出的網站都長得一樣？用「Hallmark」修正 AI 的習慣"
description: "AI 編碼工具產生的設計總是千篇一律，這裡介紹一種擺脫這種狀況的方法：開源設計技能「Hallmark」。"
summary: "Hallmark 是一種開源設計技能，能幫助 AI 生成的網頁設計擺脫特有的「AI 味」，使其看起來更獨特且專業。"
tags: [AI, 設計, 編碼, Hallmark, 設計技能]
image: 2026-07-27-Hallmark-Anti-AI-Slop-Design-Skill-for-Claude-Code-Cursor-and-Codex.jpg
image_alt: "畫面展示了各種具有不同結構與色彩的現代 UI 設計。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "拒絕 AI 的「預設值」是找回人類創造力的必要過程。Hallmark 最迷人之處在於，它不只是模仿人類的審美，更是強迫技術展現出獨特的個性。"
quiz:
  - question: "Hallmark 設計技能的主要功能是什麼？"
    choices: ["提升 AI 生成程式碼的速度", "去除 AI 生成 UI 設計中那種「AI 味」(slop)", "誘導使用者親自編碼"]
    answer: 1
    explanation: "Hallmark 是一種設計技能，能針對 AI 編碼工具生成的 UI 套用結構與樣式規則，避免它們看起來像罐頭模板。"
  - question: "如何將 Hallmark 安裝到 AI 編碼工具中？"
    choices: ["需要進行複雜的伺服器設定", "透過單一指令即可輕鬆安裝", "作為網頁瀏覽器擴充功能安裝"]
    answer: 1
    explanation: "Hallmark 可以透過像 `npx skills add` 這樣的單一指令，安裝到 Claude Code、Cursor、Codex 等工具中。"
  - question: "程式碼在最終交付給開發者之前，會經過 Hallmark 的什麼程序？"
    choices: ["自動翻譯程序", "約 57 到 65 道「反垃圾 (slop) 測試」關卡", "資料加密程序"]
    answer: 1
    explanation: "Hallmark 不會直接呈現 AI 生成的程式碼，而是會要求其通過數十道測試關卡，以驗證設計規則的合規性與原創性。"
lang: zh-tw
ref: 2026-07-27-Hallmark-Anti-AI-Slop-Design-Skill-for-Claude-Code-Cursor-and-Codex
---

想像一下：你要求 AI「為我的企業做一個簡潔的網站」。片刻之後，網站完成了，但不知為何，它看起來跟你上週看過的另一個 AI 生成網站一模一樣，除了顏色不同，結構簡直如出一轍。那種彷彿流水線生產的廉價感，設計界將其稱為 **「AI 垃圾 (AI-slop)」**。這是因為 AI 擁有特有的「平均化設計習慣」所導致的現象。

最近，一個聰明的工具出現，專門解決這個煩惱。它就是由 Together AI 開發的開源設計技能：**Hallmark**。

## 為什麼這很重要？

Claude Code、Cursor 和 Codex 等 AI 編碼工具雖然大幅提升了開發效率，卻有一個通病：人工智慧模型在學習過程中，傾向於導出最常見數據的「平均值」。這導致 AI 產出的 UI（使用者介面）大多結構相似，佈局顯得老套。

Hallmark 阻止了這種「AI 的懶惰」。開發者不需要逐一修改設計，Hallmark 從 AI 寫程式碼的階段就強制套用專業的設計規則。這意味著產出的成品不再是死板的模板，而是看起來像是由人類親自構思、精心設計的獨特作品。

## 簡單來說：AI 的「設計檢查哨」

理解 Hallmark 最簡單的比喻，就是讓一個 **「嚴格的設計評論家」** 在旁監督。Hallmark 透過以下流程優化 AI 的設計：

1. **拒絕 (Refuse)**：Hallmark 果斷拒絕 AI 隨意選擇的那些常見預設 (Default) 結構。
2. **應用 (Apply)**：取而代之的是，Hallmark 將排版（字體）、色彩、佈局、動態效果以及微互動 (Micro-interaction) 的精密規則植入程式碼中 [Source 5](https://www.everydev.ai/tools/hallmark), [Source 15](https://mer.vin/2026/05/hallmark-design-skill-anti-slop-ui-for-claude-code-and-cursor/), [Source 18](https://github.com/adeoyewole028/hallmark-design-skills)。
3. **測試 (Test)**：Hallmark 的核心在於「反垃圾測試 (Slop-test)」關卡。在程式碼最終呈現給開發者之前，Hallmark 會讓它通過約 57 到 65 道檢驗關卡 [Source 10](https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026), [Source 11](https://agentconn.com/skills/hallmark/), [Source 12](https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026), [Source 16](https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)。

這個過程就像是在照片應用中套用濾鏡。AI 隨手畫出的草圖，經過 Hallmark 這個濾鏡精細地著色與調整結構後，就搖身一變成了高品質的作品。

## 現況

目前，Hallmark 可以透過單一指令，輕鬆安裝到 Claude Code、Cursor 和 Codex 等熱門 AI 編碼工具中 [Source 5](https://www.everydev.ai/tools/hallmark), [Source 19](https://gittrend.io/repo/Nutlope/hallmark)。

這個工具不只是更換主題，它提供了 20 到 22 種結構化主題，開發者甚至可以使用 `hallmark audit` 指令，自行檢測手頭上的現有程式碼是否含有「AI 垃圾」模式 [Source 1](https://github.com/Nutlope/hallmark), [Source 2](https://hallmark.apposters.com/), [Source 10](https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026), [Source 18](https://github.com/adeoyewole028/hallmark-design-skills)。截至 2026 年 7 月，它已獲得超過 17,700 個 GitHub 星數，廣受開發者關注 [Source 19](https://gittrend.io/repo/Nutlope/hallmark)。

## 未來展望

未來，「會寫程式碼的 AI」將不再是唯一標準，「具備設計美感的 AI」才是。Hallmark 將設計規則編碼化 (encoding)，邁出了改變 AI 習慣的第一步 [Source 12](https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026), [Source 16](https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)。期待未來出現更多類似的設計技能，讓所有我們使用的 AI 服務不再是「複製貼上」的網站，而是各自擁有獨特個性的空間。

## AI 的觀點

要求 AI 具備創造力很難，但教導它「什麼不該做」是可行的。Hallmark 最迷人之處在於，它不只是模仿人類的審美，更是強迫技術展現出獨特的個性。拒絕 AI 的「預設值」，將成為找回人類創造力的必要過程。

## 參考資料

1. Nutlope/hallmark: Anti-AI-slop design skill for Claude Code, Cursor... (https://github.com/Nutlope/hallmark)
2. Hallmark - Anti-AI Design Skill for Claude Code, Cursor, and Codex (https://hallmark.apposters.com/)
3. Hallmark: Anti-AI Slop Design for Claude, Cursor, Codex | LinkedIn (https://www.linkedin.com/posts/arkadiy-sotnikov_github-nutlopehallmark-anti-ai-slop-design-activity-7483500613071167489-_zmV)
4. Hallmark: Anti-AI-slop design skill for Claude Code, Cursor, and... (https://addrom.com/hallmark-anti-ai-slop-design-skill-for-claude-code-cursor-and-codex/)
5. Hallmark - AI Design Rules for Coding Agents | EveryDev.ai (https://www.everydev.ai/tools/hallmark)
6. Hallmark | Analog (https://analoghq.ai/nutlope/skills/hallmark)
7. Hallmark + Claude Code, Codex: The BEST DESIGN SKILL YET! (https://www.youtube.com/watch?v=dVGJ3DE1MzA)
8. GitHub - Nutlope/hallmark: Anti-AI-slop design skill for Claude Code, Cursor, and Codex. · GitHub (https://github.com/Nutlope/hallmark)
9. hallmark/skills/hallmark at main · Nutlope/hallmark (https://github.com/Nutlope/hallmark/tree/main/skills/hallmark)
10. Hallmark Design Skill: Kill AI-Generated UI with Structural ... (https://dailyaiworld.com/blogs/hallmark-design-skill-anti-slop-2026)
11. Hallmark - AI Agent Skill | AgentConn (https://agentconn.com/skills/hallmark/)
12. Hallmark Design Skill: Anti-AI-Slop UI for Agents (2026) (https://explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)
13. Hallmark: Anti-AI-Slop Techniques for Claude Code and Cursor | AIToolly (https://aitoolly.com/ai-news/article/2026-07-15-hallmark-new-anti-ai-slop-design-techniques-for-claude-code-cursor-and-codex-developers)
14. Hallmark: Rejecting AI-Slop in Claude Code and Cursor | AIToolly (https://aitoolly.com/ai-news/article/2026-07-16-hallmark-a-new-design-skill-to-eliminate-ai-slop-in-claude-code-and-cursor)
15. Hallmark Design Skill: Anti-AI-Slop UI for Claude Code and ... (https://mer.vin/2026/05/hallmark-design-skill-anti-slop-ui-for-claude-code-and-cursor/)
16. Hallmark Design Skill: Anti-AI-Slop UI for Agents (2026 ... (https://www.explainx.ai/blog/nutlope-hallmark-anti-ai-slop-design-skill-july-2026)
17. Hallmark Guide: Anti-AI-Slop Design for Claude Code, Curs... (https://opentools.ai/resources/hallmark)
18. GitHub - adeoyewole028/hallmark-design-skills: Anti-AI-slop ... (https://github.com/adeoyewole028/hallmark-design-skills)
19. hallmark — Anti-AI-slop design skill for Claude ... | GitTrend (https://gittrend.io/repo/Nutlope/hallmark)