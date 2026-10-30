---
layout: post
title: "我的編碼 AI 竟是駭客通道？小心已變「木馬」的 Claude Code 擴充功能"
description: "近期偽裝成開發工具、滲透使用者電腦的惡意軟體威脅急劇增加。快來了解冒充 Claude Code 擴充功能的攻擊本質與預防方法。"
summary: "近期出現多起駭客案例，攻擊者偽裝成官方開發工具，透過惡意擴充功能與假冒的原始碼外洩版本，在開發者的電腦中植入後門並竊取資訊。"
tags: [安全, AI, 開發者, ClaudeCode, 惡意軟體]
image: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor.jpg
image_alt: "電腦螢幕上顯示木馬圖示與警告訊息的網路安全相關插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "利用開發者渴望藉助 AI 能力的心態，將其作為犯罪工具是非常卑劣的手段。使用技術時，務必確認官方管道，維持良好的數位衛生習慣至關重要。"
quiz:
  - question: "近期針對開發者的攻擊者，主要目標是什麼？"
    choices: ["AI 模型本身的權重", "開發者的帳號認證資訊 (Credential)", "AI 的伺服器電費"]
    answer: 1
    explanation: "近期攻擊 AI 編碼工具的主體，大多集中於竊取使用該工具之開發者的電腦與帳號資訊，而非 AI 模型本身。"
  - question: "下列何者並非惡意軟體入侵的主要途徑？"
    choices: ["Claude 官方網站 (claude.com)", "植入木馬的假「Claude Code 外洩」儲存庫", "假冒 Claude AI 網站的廣告"]
    answer: 0
    explanation: "官方網站是安全的，惡意軟體通常透過冒充官方的假網站，或非官方的原始碼外洩儲存庫進行散播。"
  - question: "關於冒充擴充功能的攻擊特徵，下列何者正確？"
    choices: ["僅會彈出簡單的廣告視窗", "在使用者電腦安裝 SSH 後門，嘗試進行持續性的遠端存取", "拖慢 AI 的回答速度"]
    answer: 1
    explanation: "攻擊者會在受感染的電腦中植入 SSH 後門，讓開發者在不知情的情況下，持續遭到遠端存取並外洩數據。"
lang: zh-tw
ref: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor
---

想像一下，你安裝了一個能提升編碼效率的 AI 工具，並興致勃勃地準備開始工作。但事實上，該工具卻悄悄為你的電腦打開了大門，留下了一個讓駭客隨時能闖入的「秘密通道」，那會是什麼樣的情景？最近，這場惡夢正真實地在開發者之間上演。

近期，針對如 [Claude Code](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak) 等熱門 AI 編碼工具的網路攻擊日益猖獗，攻擊者試圖藉此竊取開發者資訊並奪取系統權限。

## 這為何如此重要？

這個問題帶來的風險遠超一般的「病毒」。AI 編碼工具能夠存取我們編寫的原始碼、雲端存取權限、資料庫密碼等高度敏感資訊。

若駭客透過這些工具入侵你的電腦，威脅將不僅限於開發者個人，甚至可能導致該開發者所參與的整個企業安全網遭到破壞。事實上，從 2025 年到 2026 年，[不僅是 Claude Code，包括 GitHub Copilot、OpenAI Codex 等主流 AI 編碼代理皆曾先後暴露在安全威脅之中。](https://moccet.ai/news/tech/claude-code-copilot-and-codex-all-got-hacked-every-attacker-went-for-the-credent) 攻擊者的目標並非損壞 AI 模型本身的效能，而是直接瞄準使用該模型的**開發者帳號認證資訊 (Credential，即使用者辨識與存取權限資訊)**。

## 簡單理解

這次攻擊的核心策略是**「特洛伊木馬」**。如同希臘神話中特洛伊軍隊將士兵藏在華麗木馬中潛入城內，駭客也將惡意軟體偽裝成極具吸引力的 AI 擴充功能或原始碼進行包裝。

1. **偽裝戰術**：駭客製作出與 Claude 官方網站如出一轍的 [假網站](https://www.notebookcheck.net/Fake-Claude-AI-website-is-pushing-a-Windows-backdoor-through-Google-search-results.1291664.0.html)，或是散布標榜為「原始碼外洩」的檔案。
2. **滲透**：當開發者下載並執行這些檔案後，其中的程式便會安裝 [Beagle Windows 後門](https://www.linkedin.com/posts/bleepingcomputer_cybersecurity-windowssecurity-malware-activity-7458094379153502208-JG7C)或是 Vidar 等惡意軟體。
3. **秘密通道**：這些惡意軟體會植入 [SSH 後門 (Backdoor，即為秘密存取系統而留下的後門)](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)，建立起「反向 SSH 通道」，讓外部駭客能像電腦主人一樣，隨時長驅直入。

比喻來說，我們安裝工具的行為，最後竟變成了親切地對駭客說：「我們家的密碼在這裡喔」。在我們打開大門的那一刻，駭客便能隨意進出我們的家 (電腦)，偷走珍貴的資產 (資料)。

## 現況

情況比想像中嚴峻。今年 4 月，[數萬人因聽聞「Claude Code」原始碼外洩而爭相下載檔案，但其中有相當多數包含了竊取資訊的惡意軟體。](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/?ref=biztoc.com)

安全研究機構 Zscaler [警告，已經發現偽裝成 anthropic.claude-code@2.1.313 版本的木馬擴充功能。](https://github.com/nirholas/fresh-start) 該擴充功能在安裝瞬間便會與駭客伺服器連線並掌控使用者的系統。目前，攻擊者甚至利用 Google 搜尋廣告，將假網站推送到搜尋結果的前幾名，手段極其狡猾。

## 未來展望

AI 編碼工具將成為開發流程中不可或缺的必需品，因此攻擊者的目標也將更加精準。關鍵在於：**僅使用 [Anthropic 官方提供的 CLI (命令列介面) 工具](https://github.com/nirholas/fresh-start)**，絕對不要下載非官方管道流出的原始碼。

未來，在安裝工具時檢查數位簽章，或是確認是否為經過可信任開發者社群驗證的官方版本，將成為開發者的必備職能。安全並非僅是技術問題，而是從每天實踐的微小習慣開始。

## AI 的觀點

利用開發者想將聰明的 AI 視為夥伴的心態來進行犯罪，是非常卑劣且惡意的行徑。然而，這次事件也是一面鏡子，映照出我們對於便利背後的「安全」是多麼掉以輕心。安全永遠比便利重要。透過官方管道使用工具，這才是最快速且安全的開發開端。

## 參考資料

1. [Trojanized Claude Code Extension Plants a Persistent SSH Backdoor](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Claude Code Leak: Critical AI Security Threat 2026](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak)
3. [Fake Claude AI website is pushing a Windows backdoor through Google search results](https://www.notebookcheck.net/Fake-Claude-AI-website-is-pushing-a-Windows-backdoor-through-Google-search-results.1291664.0.html)
4. [Claude AI Site Spreads Beagle Windows Backdoor via Trojanized](https://www.linkedin.com/posts/bleepingcomputer_cybersecurity-windowssecurity-malware-activity-7458094379153502208-JG7C)
5. [Fake Claude Code source downloads actually delivered malware](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/?ref=biztoc.com)
6. [GitHub - nirholas/fresh-start: The original nirholas/claude-code before...](https://github.com/nirholas/fresh-start)
7. [AI Coding Agents Hacked: Claude Code, Copilot... | Moccet TechNews](https://moccet.ai/news/tech/claude-code-copilot-and-codex-all-got-hacked-every-attacker-went-for-the-credent)