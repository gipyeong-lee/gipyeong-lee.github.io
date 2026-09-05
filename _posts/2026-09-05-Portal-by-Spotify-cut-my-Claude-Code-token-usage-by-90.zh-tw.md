---
layout: post
title: "只讓 AI 程式助手做『雜事』，成本竟降低了 90%？"
description: "透過 Spotify 公開的『門戶（Portal）』技術，深入了解如何大幅降低 AI 程式代理的 Token 成本。"
summary: "Spotify 透過開源技術『門戶（Portal）』與 AiKA 模式，將 AI 程式代理的重複性簡單工作委派給較廉價的模型，從而降低了 90% 的 Token 使用量。"
tags: [AI, 程式設計, Spotify, 成本節流, 效率化]
image: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90.jpg
image_alt: "將程式代理與程式碼庫之間的有效路徑數據流具象化的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "將無需複雜推理的簡單工作交給頂級 AI 模型是沒有效率的。這項技術是優化 AI 使用『性價比』的明智方法。"
quiz:
  - question: "Spotify 為降低 AI 程式代理成本而引入的核心技術名稱為何？"
    choices: ["Claude Code", "Portal", "AiKA"]
    answer: 1
    explanation: "Spotify 公開了『門戶（Portal）』，這是一個位於 AI 程式代理與程式碼庫之間的知識圖譜層。"
  - question: "在 Portal 的 AiKA 模式中，『code-writer』的主要角色是什麼？"
    choices: ["分析整個程式碼庫", "根據模式生成程式碼", "更新使用者文件"]
    answer: 1
    explanation: "code-writer 模式負責根據既有模式生成重複性程式碼的工作。"
  - question: "透過將簡單重複的工作委派給較廉價的模型，所獲得的 Token 使用量節省率為多少？"
    choices: ["50%", "70%", "90%"]
    answer: 2
    explanation: "將重複性高且 I/O（輸入/輸出）密集的工作路由至 Gemini 2.5 Flash 等較廉價的模型，降低了 90% 的 Token 使用量。"
lang: zh-tw
ref: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90
---

想像一下，您聘請了一位非常聰明的博士作為私人助理。但如果每天早上您只讓他做「按影印機按鈕」或「整理文件夾」之類的瑣事，會發生什麼事呢？而且您付給他的薪水還是博士等級的待遇。

最近在開發者之間引起熱議的「AI 程式代理（AI Coding Agent）」情況正是如此。將編碼工作交給擁有頂尖智慧的 AI，結果它花在單純讀寫文件這種「跑腿」工作上的成本，竟然比解決需要高度邏輯思維的問題還要多。這裡的成本是指每次 AI 理解並處理語句時所支付的「Token（計算 AI 運算單位的術語）」費用。為了打破這種低效率的情況，Spotify 的工程師們提出了新的解決方案。

## 為什麼這很重要？

隨著 AI 技術的飛速發展，許多開發者正透過 Claude Code 等 AI 程式代理大幅提升工作效率。然而，這裡有一個致命的絆腳石，那就是「成本」。AI 在解決非常複雜的邏輯問題時使用的最高性能模型，即所謂的「前沿模型（Frontier Model）」，其使用費用非常昂貴。

問題在於，當這聰明的 AI 頻繁讀取簡單文件，或編寫數十次都長得一模一樣的測試程式碼時，系統依然收取同樣昂貴的費用。Spotify 的這次案例，展示了如何不僅僅是「使用」AI，而是**「判斷該將什麼工作交給什麼等級的 AI 處理，才能最經濟且高效」**，這是一個重要的轉折點。這為在維持開發者生產力的同時，大幅降低營運成本提供了現實可行的路徑 [[參考資料 1](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]。

## 輕鬆理解：「聰明的交通轉運站」

Spotify 公開了一項名為「門戶（Portal）」的技術 [[參考資料 6](https://www.youtube.com/watch?v=TfZsMjB9PMo)]。簡單來說，Portal 就像是 AI 代理與程式碼（程式碼庫）之間的一個**「聰明的交通轉運站」**。過去，AI 為了翻找程式碼各處並閱讀所有內容，浪費了大量 Token [[參考資料 9](https://getpushtoprod.substack.com/p/how-to-reduce-90-of-claude-code-token)]。

Spotify 在這裡聘用了兩位名為「AiKA 模式」的特別員工來分擔工作 [[參考資料 11](https://github.com/spotify/portal-ai-plugins)]。

1. **bulk-reader（批量閱讀負責人）**：需要分析多個檔案時，不使用昂貴的 AI，而是交給性能適中但成本非常低廉的「Gemini 2.5 Flash」模型處理 [[參考資料 2](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]。
2. **code-writer（程式撰寫負責人）**：需要根據既有程式碼模式撰寫重複性程式碼時，同樣交給廉價模型處理 [[參考資料 2](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]。

安裝名為「shunt（分流）」的外掛後，昂貴的高性能 AI 模型只需專注於真正需要大腦的「創造性問題解決」，而其餘單純的重複性勞動則由廉價的 AiKA 模型分擔處理 [[參考資料 4](https://www.linkedin.com/posts/spotify-for-backstage_portal-by-spotify-cut-my-claude-code-token-activity-7501610054891274241-y4Db), [參考資料 11](https://github.com/spotify/portal-ai-plugins)]。

## 當前狀況

許多開發者在使用 AI 代理時，對每個月產生的龐大 Token 費用感到負擔 [[參考資料 12](https://www.youtube.com/watch?v=UslVzxAkiZ0)]。Spotify 的這次嘗試不僅止於理論，實際上還創造了**將程式代理 Token 使用量降低 90% 的驚人結果** [[參考資料 3](https://zeli.app/story/49571465), [參考資料 14](https://news.ycombinator.com/item?id=49571465)]。

目前該技術已開源並公開，任何人都可以使用，主要活躍於優化 Claude Code 環境中檔案 I/O（輸入/輸出）密集的工作 [[參考資料 6](https://www.youtube.com/watch?v=TfZsMjB9PMo), [參考資料 11](https://github.com/spotify/portal-ai-plugins)]。

## 未來發展？

未來，這將不再僅僅是討論「哪種 AI 更聰明」，而是**「該如何配置 AI」**將成為真正的競爭力。像 Spotify 的 Portal 一樣，以知識圖譜（將數據間關係視覺化的形式）形式管理複雜系統內部，並根據工作性質自動分配模型的系統，預計將會更多地出現。

開發者們現在不再只是苦惱「該如何指示 AI？」，而必須思考「該如何設計一個架構來節省昂貴的 AI，並明智地運用廉價的 AI？」。為了更聰明地使用聰明的 AI，現在正是需要有效「分工」的時候。

## MindTickleBytes 的 AI 記者觀點
AI 應用的成敗現在不取決於模型本身的性能，而是取決於管理整個系統效率的「運作手腕」。Spotify 的案例是展示如何透過有效配置最高性能 AI 來降低成本並最大化生產力的最佳典範。

## 參考資料
1. [Portal by Spotify cut my Claude Code token usage by 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
2. [Portal by Spotify cut my Claude Code token usage by 90%](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
3. [Spotify's Portal cut my Claude Code · Hacker News | Zeli](https://zeli.app/story/49571465)
4. [Portal by Spotify cut my Claude Code token usage by 90% ...](https://www.linkedin.com/posts/spotify-for-backstage_portal-by-spotify-cut-my-claude-code-token-activity-7501610054891274241-y4Db)
5. [Spotify’s Backstage Portal cut my Claude Code… | VibeLeaderboard](https://www.vibeleaderboard.ai/intel/7ff05f2d-e1d9-4b86-aa58-8d94a5fccd5f)
6. [Spotify cut Claude Code token usage by 90% with Portal](https://www.youtube.com/watch?v=TfZsMjB9PMo)
9. [How to Reduce 90% of Claude Code Token Usage - by John Kim](https://getpushtoprod.substack.com/p/how-to-reduce-90-of-claude-code-token)
11. [GitHub - spotify/portal-ai-plugins · GitHub](https://github.com/spotify/portal-ai-plugins)
12. [How To Save 90% of Claude Code Token Usage - YouTube](https://www.youtube.com/watch?v=UslVzxAkiZ0)
14. [PortalbySpotifycutmyClaudeCodetokenusage... | HackerNews](https://news.ycombinator.com/item?id=49571465)