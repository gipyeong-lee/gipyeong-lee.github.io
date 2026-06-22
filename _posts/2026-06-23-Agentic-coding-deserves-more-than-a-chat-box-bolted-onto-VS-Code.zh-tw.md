---
layout: post
title: "AI 是我的程式設計助手？別再被關在聊天視窗裡的 AI 侷限了"
description: "用淺顯易懂的方式說明在 VS Code 等現有編輯器中單純加上聊天機器人，與從一開始就為 AI 設計的「代理型程式設計」IDE 之間的差異。"
summary: "超越單純的程式碼建議，具備自主規劃與執行能力的「代理型程式設計」已成主流。我們將探討為何將 AI 硬塞進現有編輯器的模式會遭遇瓶頸。"
tags: [AI, 程式設計, 代理人, 開發工具, 技術趨勢]
image: 2026-06-23-Agentic-coding-deserves-more-than-a-chat-box-bolted-onto-VS-Code.jpg
image_alt: "浮現在 VS Code 畫面上方的單純聊天視窗，與將整體程式碼有機串聯並自主作業的代理型 IDE 形成對比"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "代理型程式設計正在將開發者的角色從「親手編寫者」轉變為「提供方向與審核者」。工具的改變意味著思維的改變。"
quiz:
  - question: "現有的 VS Code 聊天模式與「代理型程式設計」IDE 之間最大的差異是什麼？"
    choices: ["聊天模式可以讓 AI 執行終端指令", "代理型 IDE 從一開始就被設計為讓 AI 與程式碼有機連結", "現有的編輯器速度快得多"]
    answer: 1
    explanation: "代理型 IDE 的特點在於其設計初衷即是讓 AI 能完美理解整體儲存庫的脈絡，並自主執行規劃、編寫與測試。"
  - question: "安德烈·卡帕西（Andrej Karpathy）所命名的「震動程式設計（Vibecoding）」是什麼意思？"
    choices: ["AI 自主完成發布的方式", "透過反覆修改提示詞來進行構建的方式", "完全不編寫程式碼的方式"]
    answer: 1
    explanation: "「震動程式設計」是指對 AI 下達提示詞，並根據回饋進行反覆修改，最終製作出成品的方式。"
  - question: "代理型程式設計的核心作用是什麼？"
    choices: ["簡單的語法檢查", "支援程式碼複製貼上", "自主執行規劃、執行、測試、部署等多階段任務"]
    answer: 2
    explanation: "代理型程式設計具備自主性，能與編譯器、偵錯器、版本控制系統等進行互動，自主處理複雜功能。"
lang: zh-tw
ref: 2026-06-23-Agentic-coding-deserves-more-than-a-chat-box-bolted-onto-VS-Code
---

想像一下，你正在做一道非常複雜的料理，身旁有一位非常聰明的助手。但這位助手卻完全不了解廚房的整體結構，只會聽從你發出的簡短指令來遞送材料。如果必須事事指示「把洋蔥切了」、「接下來切胡蘿蔔」，那麼作為發號施令的你，恐怕反而會更加疲憊。

我們現在開發軟體的方式正是如此。這就是將 AI 聊天機器人「外掛」在 VS Code 等現有編輯器上的模式。然而，開發現場現在正吹起一股新風潮，那就是「代理型程式設計（Agentic Coding）」。這項技術正在徹底改變開發的面貌。

## 為什麼這很重要？

至今為止我們所使用的 AI，就像是一個「非常聽話的實習生」。它會回答你的問題，並一點一點地幫你修改程式碼。但現在登場的不僅僅是實習生，而是與你並肩作戰的「自主夥伴」。

代理型程式設計的運作方式是，開發者只要丟出「幫我完成這個功能」的目標，AI 就會自行尋找所需的檔案、編寫程式碼，甚至執行測試 [[出處：Top 9 AI Coding Agent Ecosystems in VS Code](https://medium.com/@hasanmcse/top-9-ai-coding-agent-ecosystems-in-vs-code-2d3dbf13806b), [出處：AI Agentic Programming: A Survey of Techniques](https://arxiv.org/abs/2508.11126)]。這不僅僅是稍微提升一點生產力，而是軟體開發的範式從「我親手一磚一瓦砌成」，根本性地轉變為「由 AI 規劃，我負責審核與決策」的模式 [[出處：Anthropic's superpower, Roku acquired, agentic code review](https://tldr.tech/tech/2026-06-16)]。

## 淺顯易懂的理解

打個比方，如果現有的聊天式 AI 就像「照片 App 的簡單濾鏡」，那麼代理型程式設計就是「從拍攝、修圖到剪輯一手包辦的電影製作人」。

例如，透過擴充功能在 VS Code 中使用 AI，只是調整照片的色調而已。但「代理型 IDE（整合開發環境，具備開發所需一切工具的空間）」則是從一開始就為 AI 設計的電影攝影棚。在這個攝影棚裡，AI 對廚房的食材（整體程式碼儲存庫）瞭若指掌，當你說「今天午餐做牛排」時，它會自動取出牛肉、燒烤，連調製醬汁的過程都一手包辦 [[出處：The VS Code vs AI Agent IDE Shift Nobody Warned You About](https://medium.com/@hembitec/the-vs-code-vs-ai-agent-ide-shift-nobody-warned-you-about-7fa1a5a72912)]。

如果說安德烈·卡帕西（Andrej Karpathy）所說的「震動程式設計（Vibecoding，不斷發送提示詞並確認結果進行修改）」是給助手不斷下指令的方式，那麼代理型程式設計就是將料理的全程完整託付給對方 [[出處：VibeCoding vs Agentic Coding: What's the Difference and Which...](https://www.abhs.in/blog/vibe-coding-vs-agentic-coding-difference-2026)]。

## 當前局勢

目前許多開發者透過安裝 AI 擴充功能在現有的編輯器中使用 [[出處：I thought I was productive in VS Code until agentic coding showed me what I was missing](https://www.xda-developers.com/agentic-coding-ruined-normal-ides-like-vs-code-zed-pycharm/)]。微軟也順應趨勢，在 VS Code 中引入了代理模式等功能 [[出處：A Unified Experience for all Coding Agents - Visual Studio Code](https://code.visualstudio.com/blogs/2025/11/03/unified-agent-experience)]。

然而，明確的侷限性依然存在。因為被困在現有編輯器狹窄聊天視窗中的 AI，在深入理解並修改整體專案的上下文方面存在限制 [[出處：The VS Code vs AI Agent IDE Shift Nobody Warned You About](https://medium.com/@hembitec/the-vs-code-vs-ai-agent-ide-shift-nobody-warned-you-about-7fa1a5a72912)]。反之，像「Cursor」或「Windsurf」這些從一開始就以 AI 為中心設計的工具，能讓 AI 像在家裡一樣，在整個程式碼儲存庫中自由穿梭與作業。它們就像能夠熟練操作攝影棚所有設備的專家 [[出處：10 Best AI Coding Agents in 2026](https://openagents.org/blog/posts/2026-05-21-best-ai-coding-agents), [出處：The VS Code vs AI Agent IDE Shift Nobody Warned You About](https://medium.com/@hembitec/the-vs-code-vs-ai-agent-ide-shift-nobody-warned-you-about-7fa1a5a72912)]。

## 未來展望

未來，「支援 AI 的編輯器」與「AI 主導的 IDE」之間的界線將會變得更加清晰。開發者將不再滿足於僅具備程式碼行自動完成功能的工具，轉而追求一個能夠分析整個專案、預測潛在問題並自主執行複雜多階段任務的環境 [[出處：AI Agentic Programming: A Survey of Techniques](https://arxiv.org/abs/2508.11126)]。

最終，開發者的核心能力將不再是「打字速度有多快」，而是「能多敏銳地審核 AI 代理提出的結果，並引導至正確方向」。這意味著工具的改變終究改變了開發者這項職業的本質 [[出處：Anthropic's superpower, Roku acquired, agentic code review](https://tldr.tech/tech/2026-06-16)]。

## 參考資料

1. [10 Best AI Coding Agents in 2026 — Complete Guide & Comparison | OpenAgents Blog](https://openagents.org/blog/posts/2026-05-21-best-ai-coding-agents)
2. [Microsoft MAI-Code-1-Flash vs Claude Code: Coding Agent Strategy and Enterprise Control | Windows Forum](https://windowsforum.com/threads/microsoft-mai-code-1-flash-vs-claude-code-coding-agent-strategy-and-enterprise-control.428415/)
3. [Best Coding Agents for VS Code in 2026: Compared & Reviewed | Kilo.ai](https://kilo.ai/articles/coding-agents-for-vscode)
4. [The VS Code vs AI Agent IDE Shift Nobody Warned You About | Medium](https://medium.com/@hembitec/the-vs-code-vs-ai-agent-ide-shift-nobody-warned-you-about-7fa1a5a72912)
5. [How I configure VS Code for agentic coding - beyang.org](https://beyang.org/how-i-configure-vs-code-for-agentic-coding.html)
6. [I thought I was productive in VS Code until agentic coding showed me what I was missing | XDA-Developers](https://www.xda-developers.com/agentic-coding-ruined-normal-ides-like-vs-code-zed-pycharm/)
7. [Top 9 AI Coding Agent Ecosystems in VS Code | Medium](https://medium.com/@hasanmcse/top-9-ai-coding-agent-ecosystems-in-vs-code-2d3dbf13806b)
8. [Agentic coding deserves more than a chat box bolted onto VS Code | Hacker News](https://news.ycombinator.com/item?id=48571811)
9. [Download Visual Studio Code](https://code.visualstudio.com/download)
10. [Qoder - The Agentic Coding Platform](https://qoder.com/)
11. [VibeCoding vs Agentic Coding: What's the Difference and Which to Choose?](https://www.abhs.in/blog/vibe-coding-vs-agentic-coding-difference-2026)
12. [Claude Code vs Cursor Tab (2026): Autocomplete Comparison](https://claudecodeguides.com/claude-code-vs-cursor-tab-autocomplete-2026/)
13. [Anthropic's superpower, Roku acquired, agentic code review | TLDR Tech](https://tldr.tech/tech/2026-06-16)
14. [Agentic coding made programming fun again | Devas Life](https://www.devas.life/agentic-coding-made-programming-fun-again/)
15. [A Unified Experience for all Coding Agents - Visual Studio Code Blog](https://code.visualstudio.com/blogs/2025/11/03/unified-agent-experience)
16. [How I Used Agentic Mode in VS Code Insiders to Develop an App | LinkedIn](https://www.linkedin.com/pulse/how-i-used-agentic-mode-vs-code-insiders-develop-app-thangavelu-iknbf/)
17. [From Code Completion to Autonomous Development: The Evolution of Agentic Coding | Dev.to](https://dev.to/deniskisina/from-code-completion-to-autonomous-development-the-evolution-of-agentic-coding-223m)
18. [AI Agentic Programming: A Survey of Techniques | arXiv](https://arxiv.org/abs/2508.11126)
19. [GitHub Introduces Coding Agent For GitHub Copilot](https://github.com/newsroom/press-releases/coding-agent-for-github-copilot)
20. [Build with agents in VS Code | Visual Studio Code Docs](https://code.visualstudio.com/docs/agents/overview)