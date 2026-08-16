---
layout: post
title: "AI 正在監控我的電腦，如果「回饋」按鈕變成我的日記本怎麼辦？"
description: "探討月之暗面 (Moonshot AI) 的桌面代理 Kimi Work 在回饋報告過程中，所引發的個人隱私共享問題及其意義。"
summary: "月之暗面 (Moonshot AI) 的桌面 AI 代理「Kimi Work」被揭露在使用者提交回饋報告時，會自動同時傳送最近 5 個對話會話，使用者需提高警覺。"
tags: [AI, 資安, KimiWork, 月之暗面, 個人隱私]
image: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports.jpg
image_alt: "象徵 Kimi Work 桌面應用程式介面與資安警告的圖形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "當為了便利而設計的功能在缺乏透明度的情況下運作時，信任就會崩塌。開發商必須讓使用者清楚知曉他們正在分享什麼。"
quiz:
  - question: "Kimi Work 在提交回饋報告時會自動附加什麼資料？"
    choices: ["最近 5 個代理會話", "電腦中的所有檔案清單", "使用者的個人密碼"]
    answer: 0
    explanation: "Kimi Work 在使用者發送回饋報告時，會未經額外告知地將最近 5 個代理對話會話一併附加傳送。"
  - question: "下列何者不是 Kimi Work 的主要功能？"
    choices: ["讀取本機檔案", "控制網頁瀏覽器", "販售使用者的所有網頁搜尋紀錄"]
    answer: 2
    explanation: "Kimi Work 支援讀取本機檔案、控制瀏覽器、執行預約工作等，但並未提供其販售使用者搜尋紀錄的相關資訊。"
  - question: "Kimi Work 的「預約工作」功能基於什麼運作？"
    choices: ["cron (排程器)", "物理計時器", "隨機執行器"]
    answer: 0
    explanation: "Kimi Work 使用基於 cron 的排程器，支援準備早晨簡報或夜間執行腳本等自動化工作。"
lang: zh-tw
ref: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports
---

想像一下，有一位能完美輔助你工作的聰明秘書。早晨醒來，它已將今日工作整理得井井有條；當你沉睡時，它已完成堆積如山的數據分析。這位秘書不僅能直接讀取你電腦中的文件，還能代替你連接網站，尋找所需的資訊。月之暗面 (Moonshot AI) 推出的桌面 AI 代理「Kimi Work」，正是這樣的存在 [Source 6]。

然而，如果這位秘書偷偷翻閱你的日記，並將內容悄悄夾帶在寄給總部的報告中，你會作何感想？近期，資安專家在 Kimi Work 的運作方式中發現了一個令人震驚的事實。

## 這為何重要？

AI 代理擁有存取我們電腦深處的權限。它們具備直接讀取本機檔案、控制網頁瀏覽器，甚至在指定時間自動執行工作的能力 [Source 6, Source 12]。這雖然能將工作效率最大化，但也伴隨著強大的資安責任。

使用者通常在遇到錯誤並按下「發送回饋」按鈕時，會認為分享的內容僅限於當下遇到的狀況或螢幕截圖。然而，Kimi Work 在此過程中，未經告知便一併傳送了使用者的近期對話內容。這在個人隱私保護方面引發了極大擔憂。因為你與 AI 分享的敏感工作資料或個人對話，可能會無意間流向開發商的伺服器。

## 簡單來說：比喻為「秘書的報告」

讓我們用日常生活中的比喻來解釋這個情況。你對秘書說：「今天寫報告時，有個檔案打不開」，並發送了回饋。你以為只傳達了問題狀況，但這位秘書在將報告寄給公司總部時，竟將你過去幾天撰寫的所有日記（最近 5 個對話會話）一併複製並附在其中。

我們可以理解月之暗面為了改善使用者體驗而收集回饋資料的意圖，但核心問題在於過程缺乏透明度。使用者在完全不知情的情況下，便傳送了珍貴的資料。

## 目前狀況

Kimi Work 基於月之暗面強大的 AI 模型 Kimi K2.6，是由約 300 個下位代理群體 (swarm) 協作而成的桌面代理 [Source 5, Source 6]。它同時支援 Windows 和 macOS，並透過基於 cron（Linux/Unix 系統的任務排程器）的計畫功能，即使在使用者入睡後也能處理工作 [Source 6, Source 12]。

然而，根據近期的逆向工程（分析軟體內部結構與運作原理的工作）發現，當使用者提交回饋報告時，系統會在未經個別指引的情況下，自動附上最近 5 個會話的資料 [Source 1]。這可說是為了追求技術便利，而犧牲使用者隱私的典型案例。

## 未來將會如何？

AI 技術正朝著日益個人化、要求更多權限的方向發展。然而，這也是使用者信任最為關鍵的時刻。此次事件為 AI 開發商如何處理使用者資料，以及資訊公開的透明度敲響了警鐘。

若你未來使用 Kimi Work，在按下「回饋」按鈕前，務必再次思考近期是否有包含敏感資訊的對話內容。此外，使用者應更強烈地要求權限，以便能直接設定 AI 代理傳送資料的範圍與內容。

## MindTickleBytes 的 AI 記者觀點

技術帶來的便利往往需要以資安作為代價。但這個代價，絕不應在未經使用者明確事前同意下支付。若稱得上是真正的「智慧 AI」，難道不應協助使用者自行掌控分享內容嗎？使用者的隱私，絕不該成為技術發展的犧牲品。

## 參考資料

1. [KimiWork attaches raw agent sessions to feedback reports](https://news.ycombinator.com/item?id=49313711)
2. [KimiWork](https://www.kimi.com/ru/help/kimi-work)
3. [KimiCode CLI: How to Install and Run Moonshot's Agentic Coding...](https://apidog.com/blog/kimi-code-cli/)
4. [GitHub - MoonshotAI/Kimi-K3: Open Frontier Intelligence · GitHub](https://github.com/MoonshotAI/Kimi-K3)
5. [KimiWork: Moonshot's Local AI Agent Guide | Lushbinary](https://lushbinary.com/blog/kimi-work-local-ai-agent-knowledge-workers-guide/)
6. [Moonshot AI's KimiWork Brings 300 AI Agents to Your... - Decrypt](https://decrypt.co/370954/moonshot-ai-kimi-work-300-agents-desktop)
7. [KimiK3 за $29: китайские тарифы, KimiCode... - YouTube](https://www.youtube.com/watch?v=vDp4SLNDHLs)
8. [Kimi API Platform](https://platform.kimi.ai/)
10. [GitHub - MoonshotAI/kimi-code: KimiCode CLI — The Starting Point...](https://github.com/MoonshotAI/kimi-code)
11. [KimiWork - Nowledge Mem Integration | Nowledge Mem](https://mem.nowledge.co/integrations/kimi-work)
12. [Вышел KimiWork — ИИ-агент, который работает без сна / Хабр](https://habr.com/ru/news/1045120/)