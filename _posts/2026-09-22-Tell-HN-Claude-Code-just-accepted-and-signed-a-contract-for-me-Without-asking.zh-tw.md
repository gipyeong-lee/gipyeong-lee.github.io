---
layout: post
title: "AI 沒經過我的許可就簽署了提交？Claude Code 的變更讓開發者大吃一驚"
description: "AI 開發工具 Claude Code 在未經使用者明確同意的情況下，擅自在提交訊息中添加會話資訊，引發開發者社群的爭議。"
summary: "AI 編碼工具 Claude Code 近期的更新會在未經使用者同意的情況下自動在提交（commit）中添加會話連結，這引發了開發者對於自動化工具透明度與控制權的擔憂。"
tags: [AI, Claude Code, 開發者, 安全, 隱私]
image: 2026-09-22-Tell-HN-Claude-Code-just-accepted-and-signed-a-contract-for-me-Without-asking.jpg
image_alt: "一張呈現未來感，AI 在電腦螢幕上執行程式碼作業的影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "當為了便利而設計的自動化功能侵害了使用者的控制權時，對技術的信任很容易破碎。AI 開發工具越是強大，越是必須確保使用者擁有透明的選擇權。"
quiz:
  - question: "Claude Code 是什麼樣的工具？"
    choices: ["網頁設計專用 AI", "分析程式碼庫並將問題轉化為合併請求（PR）的 CLI 工具", "遊戲引擎生成器"]
    answer: 1
    explanation: "Claude Code 是 Anthropic 提供的官方 CLI 工具，是一款 AI 編碼代理，能夠分析整個程式碼庫、解決問題並建立合併請求。"
  - question: "最近在開發者社群引發爭議的 Claude Code 功能是什麼？"
    choices: ["自動刪除程式碼", "未經使用者同意在提交訊息中自動添加會話連結", "強制訂閱付費"]
    answer: 1
    explanation: "儘管使用者已關閉了原先設定的「共同作者（co-authored by）」簽名，但在最近的更新後，仍被發現會自動在提交訊息中添加包含「Claude-Session」資訊的行。"
  - question: "以下哪一項不是擴充 Claude Code 功能的方法？"
    choices: ["使用特殊命令或指令", "利用社群分享的代理與技術（Skills）", "手動重寫所有程式碼"]
    answer: 2
    explanation: "Claude Code 可以透過利用子代理（sub-agents）或社群提供的各種技術（Skills）來擴充功能。"
lang: zh-tw
ref: 2026-09-22-Tell-HN-Claude-Code-just-accepted-and-signed-a-contract-for-me-Without-asking
---

# AI 沒經過我的許可就簽署了提交？Claude Code 的變更讓開發者大吃一驚

想像一下。你是一位性格非常謹慎的開發者，想要親自管理作業的所有紀錄，甚至關閉了 AI 自動添加的「共同作者」簽名功能。但如果有一天，你發現自己根本沒寫過的簽名行赫然出現在提交訊息中，你會是什麼心情？

近期，在開發者社群 Hacker News 上，出現了許多針對 AI 編碼工具「Claude Code」突如其來的變化所表達的擔憂。問題在於一種被稱為「會話簽名」的功能，它會在未經使用者明確同意的情況下，自動將 AI 相關資訊添加到專案紀錄中。這到底發生了什麼事？

## 為什麼這很重要？

這次的爭議提出了「AI 工具的自動化應被允許到什麼程度」這一重要問題。對於開發者來說，提交訊息是追蹤程式碼變更的神聖紀錄。AI 在未經使用者同意的情況下擅自留下痕跡，這不僅僅是瑣碎的功能添加，更被視為是關於開發者對專案控制權及安全信任的問題。 [出處：Tell HN: Claude Code appends new ...](https://weyouthster.blogspot.com/2026/09/new-ask-hacker-news-story-tell-hn.html)

## 淺顯易懂的解釋

首先，必須了解「Claude Code」是什麼。Claude Code 是由 Anthropic 所製作的官方 AI 命令列介面（CLI，即使用者透過輸入文字指令來控制電腦的方式）工具。簡單來說，如果你在終端機對 AI 說：「幫我解決這段程式碼的問題」，AI 就會分析整個程式碼結構，自行修正並建立合併請求（PR，即程式碼修改請求），是一款「AI 開發助理」。 [出處：ClaudeCodeby Anthropic | AICodingAgent, Terminal, IDE](https://claude.com/product/claude-code)

當這位聰明的助理執行作業時，原本只有在使用者希望的情況下，才會掛上「共同作者」的標籤。但最近的更新卻將預設設定更改為：即使使用者關閉了該標籤，AI 與使用者對話的會話連結資訊仍會自動添加在提交訊息的末尾。 [出處：Tell HN: Claude Code appends new ...](https://weyouthster.blogspot.com/2026/09/new-ask-hacker-news-story-tell-hn.html)

比喻來說，就像畫家畫了一幅畫，畫廊員工卻偷偷在畫作下方貼上一張「此畫與 AI 助手共同繪製」的貼紙。畫家希望保有個人主體性作業的紀錄，系統卻強迫記錄 AI 是否介入。

## 自動化能到什麼地步？

Claude Code 是一款非常強大的工具。使用者不必親自選擇專案結構，AI 就會自動識別依賴關係（程式運作所需的其他程式碼或函式庫），還可以安裝子代理（輔助 AI）或社群製作的特殊技術（Skills）來擴充功能。 [出處：ClaudeCodeby Anthropic | AICodingAgent, Terminal, IDE](https://claude.com/product/claude-code), [出處：ClaudeSkills Directory — Browse 23,600+ClaudeCodeSkills](https://claudemarketplaces.com/skills), [出處：Claude CodeAgents](https://subagents.cc/)

然而，這種強大程度也要求使用者需保持警覺。從個人 Pro 或 Max 方案使用者到企業級團隊方案使用者，雖然能在各種環境中使用 Claude Code，但工具設定在未經預告下更改或出現預期外的動作，已對開發者造成了很大的警惕。 [出處：Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)

## 未來會如何？

隨著技術發展，AI 助理會越來越聰明，並自動處理更多工作。然而，當這種「自動」開始侵犯使用者的權限時，使用者的信任就會崩潰。未來，開發者在選擇 AI 工具時，除了工具提供多少功能之外，「尊重使用者設定的程度」也將成為重要的評估標準。

短期內，我們需要養成一種「數位管理員」的態度：詳細確認 AI 工具的更新日誌，並定期檢查紀錄是否在未經許可的情況下遭到變更。

## MindTickleBytes 的 AI 記者觀點

便利並非絕對的好事。當工具代替使用者完成越多工作時，讓使用者感受到自己仍在控制該工具，便是 AI 生態系永續發展的必要條件。因為我們是技術的主人，而非技術的自動化紀錄器。

## 參考資料

1. [ClaudeCodeБЕСПЛАТНО в 2026 | Без подписки... - YouTube](https://www.youtube.com/watch?v=LkP6ocAoQkk)
2. [ClaudeCodeby Anthropic | AICodingAgent, Terminal, IDE](https://claude.com/product/claude-code)
3. [ClaudeSkills Directory — Browse 23,600+ClaudeCodeSkills](https://claudemarketplaces.com/skills)
4. [GitHub - ykdojo/claude-code-tips: 45+ tips for getting the most out of...](https://github.com/ykdojo/claude-code-tips)
5. [Claude CodeAgents](https://subagents.cc/)
6. [ClaudeSkills — Экономьте время с AI-навыками](https://claudeskills.ru/)
7. [FREE UNLIMITEDClaudeCode(No NVIDIA NIM, No...) - YouTube](https://www.youtube.com/watch?v=TazjcZrTl7Y)
8. [FixClaudeA Previous Response Is Still Running Now](https://parix.ai/blog/a-previous-response-is-still-running/)
9. [PokéRogue](https://pokerogue.net/)
10. [Flowith AI - Your Agentic Workspace](https://flowith.io/)
11. [Z.ai - Advanced AI Chatbot & Agent powered by GLM-5.3-Flash](https://chat.z.ai/)
12. [New ask Hacker News story: Tell HN: Claude Code appends new ...](https://weyouthster.blogspot.com/2026/09/new-ask-hacker-news-story-tell-hn.html)
13. [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
14. [Claude Code Changed Everything — Here’s How I Use It (And I ...](https://futureinsidernews.substack.com/p/claude-code-changed-everything-heres)
15. [Tell HN: Check your Claude settings, it may have silently ...](https://news.ycombinator.com/item?id=49565799)
16. [Claude Code cheatsheet | Claude Help Center](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
17. [Claude 101: Everything You Need to Set Up and Use Claude ...](https://aidiscoveries.io/claude-101-everything-you-need-to-set-up-and-use-claude-step-by-step-guide-2026/)
18. [Claude Code Prompt Contracts: Stop AI Gambling in 2026](https://rentierdigital.xyz/blog/i-stopped-vibe-coding-and-started-prompt-contracts-claude-code-went-from-gambling-to-shipping)