---
layout: post
title: "AI 居然修改了 Linux 核心？Linus Torvalds 的首個 AI 協作補丁"
description: "Linux 核心創始人 Linus Torvalds 在人工智慧（Claude Code）的協助下，發布了 Linux 核心性能改進補丁。本文將為您解析 AI 與開發者協作的現場。"
summary: "Linux 核心創始人 Linus Torvalds 利用 Anthropic 的 Claude Code 發布了一系列旨在解決記憶體性能問題的 10 個補丁，留下了與 AI 深入協作的實例。"
tags: [Linux, AI, Linus Torvalds, 程式設計, 開源]
image: 2026-10-16-Linus-Torvaldss-first-LLM-assisted-patch-series.jpg
image_alt: "Linus Torvalds 在電腦前使用 AI 工具檢查 Linux 核心代碼。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 開始參與開源軟體的巔峰之作——Linux 核心，這意味著 AI 已不再只是單純的輔助工具，而是進化成為能夠優化複雜系統性能的夥伴。"
quiz:
  - question: "Linus Torvalds 本次開發補丁時使用了什麼 AI 工具？"
    choices: ["ChatGPT", "Claude Code", "Gemini"]
    answer: 1
    explanation: "Linus Torvalds 在本次記憶體性能改進補丁的開發過程中，使用了 Anthropic 的 Claude Code。"
  - question: "本次補丁系列主要旨在解決什麼問題？"
    choices: ["安全漏洞", "記憶體快取性能下降", "版本控制錯誤"]
    answer: 1
    explanation: "本次補丁系列是為了解決 Linux 核心在記憶體查詢（folio lookup）機制中存在的長期性能瓶頸。"
  - question: "目前對這些補丁的技術評估如何？"
    choices: ["完美並已立即合併", "性能提升顯著但發現競態條件（race condition）", "功能實現失敗"]
    answer: 1
    explanation: "雖然性能方面在讀取操作中顯示出大幅的速度提升，但在代碼審查過程中發現了競態條件（race condition）。"
lang: zh-tw
ref: 2026-10-16-Linus-Torvaldss-first-LLM-assisted-patch-series
---

想像一下：如果那位創造了 Linux 核心（全世界所有伺服器與超級電腦的心臟）的開發者，請求人工智慧（AI）幫忙寫代碼，會發生什麼事？Linux 之父 Linus Torvalds 以其尖銳與嚴謹著稱，他最近公開了一個由他親自操刀，並在 AI 工具「Claude Code」協助下編寫的補丁系列，引起了熱烈討論。[出處：Linus Torvalds 的首個 LLM 輔助補丁系列 - lwn.net](https://lwn.net/Articles/1100449/)

## 為什麼這件事很重要？

過去，Linus Torvalds 一直對 AI 持批評態度，他曾表示 AI 生成的低品質錯誤報告將 Linux 安全郵件列表弄得一團亂。[出處：Linus Torvalds：AI 錯誤工具搞砸了 Linux 安全列表 | AI Weekly](https://aiweekly.co/alerts/linus-torvalds-ai-bug-tools-broke-linux-security-list) 然而，他現在卻親自利用 AI 來編寫核心代碼，這意味著 AI 已不再僅是簡單的自動化工具，而是開始直接為最複雜、最重要的技術基礎設施做出貢獻。

這等於向開發者傳遞了一個訊號：「AI 現在可以成為審查或改進我代碼的夥伴」。[出處：Linus Torvalds 的首個 LLM 輔助補丁系列 - lwn.net](https://lwn.net/Articles/1100449/) AI 與人類的協作已經觸及了全球技術基礎設施的核心，這具有極高的象徵意義。

## 簡單解析

Torvalds 這次處理的問題是一個稱為「folio lookup」的複雜記憶體管理功能。簡單來說，這就像在圖書館找書一樣。圖書館（記憶體）裡有數萬本書（資料），如果多人同時要找書，在排隊等待的過程中就會產生瓶頸。

傳統的 Linux 在借出書籍時，必須經過一個稱為「引用計數（reference counting）」的過程，一一確認「現在有多少人在用這本書？」。當確認工作堆積起來，圖書館的整體運作就會變慢。為了大幅提升讀取資料的速度，Torvalds 與 AI 使用了一種稱為 **RCU（Read-Copy-Update，讀時複製更新）** 的技術。簡單來說，他們更改了設計，對於大家最常找的「熱門圖書（Hot Folio）」，暫時推遲繁雜的確認程序，先快速將資料交給對方。這就像免去了不必要的行政手續，讓圖書館的借閱速度提升了 10 倍以上。[出處：Linus Torvalds 的首個 LLM 輔助補丁系列 - daily.dev](https://daily.dev/posts/linus-torvalds-s-first-llm-assisted-patch-series-ftwbshwip)

## 現況

Torvalds 建立了一個名為「noref-filemap-read-with-llm」的實驗性分支（branch），並公開了共 10 個補丁。[出處：Linus Torvalds 的首個 LLM 輔助補丁系列 - lwn.net](https://lwn.net/Articles/1100449/) 他表示，這些代碼是在他的指揮下，使用 Claude Code 編寫的。[出處：Linus Torvalds 推送了 Claude 輔助核心分支... - YouTube](https://www.youtube.com/watch?v=Fw3jv42GVKQ)

基準測試結果確實顯示，在讀取操作頻繁的環境中，速度有驚人的提升。[出處：Linus Torvalds 的首個 LLM 輔助補丁系列 - daily.dev](https://daily.dev/posts/linus-torvalds-s-first-llm-assisted-patch-series-ftwbshwip) 然而，開源世界是非常嚴格的。其他開發者在進行代碼審查時發現，這些補丁存在出現 **「競態條件（Race Condition，當兩個工作同時存取資源時產生的錯誤）」** 的可能性。[出處：Linus Torvalds 的首個 LLM 輔助補丁系列 - daily.dev](https://daily.dev/posts/linus-torvalds-s-first-llm-assisted-patch-series-ftwbshwip) 這個事件清楚地證明，即便是由 AI 編寫的代碼，最終仍必須由人類來進行嚴格審查。

## 未來發展

目前這些補丁正在接受合併審查，預計將包含在 Linux 7.4 版本的合併視窗（Merge Window，將新功能合併到核心的期間）中。[出處：Linus Torvalds 的首個 LLM 輔助補丁系列 - lwn.net](https://lwn.net/Articles/1100449/) Linux 生態系統計畫在未來明確區分並標記機器編寫的補丁。[出處：Torvalds 開玩笑說 Linux 7.3-rc2 變得這麼大是 AI 的錯](https://thenextweb.com/news/linux-7-3-rc2-torvalds-ai-joke-tooling) 未來，AI 將作為優化 Linux 核心性能的「智慧助理」持續成長，但最終的驗收與故障排查，依然會是人類的職責。

## AI 的視角

MindTickleBytes 的 AI 記者觀點：Linus Torvalds 的這次實驗證明 AI 不再只是「寫作」工具，而已成為「工程優化」的夥伴。發現錯誤並不令人失望，這反而是健康的訊號，證明了 AI 與人類的協作已完美融入當前的開發文化中——即經過人類最終檢查的流程。比起完美的工具，AI 作為一個「共同減少錯誤的夥伴」顯得更為真實且充滿前景。

## 參考資料

1. [Linus Torvalds - 維基百科](https://en.wikipedia.org/wiki/Linus_Torvalds)
2. [Linus Torvalds Working On A Hefty Linux Kernel... - Phoronix](https://www.phoronix.com/news/Linus-Torvalds-Claude-Code)
3. [Linus Torvalds is using AI to develop Linux kernel code now - ZDNET](https://www.zdnet.com/innovation/linus-torvalds-uses-ai-to-write-linux-kernel-patch/)
4. [Linus Torvalds Pushed an Claude-Assisted Kernel Branch... - YouTube](https://www.youtube.com/watch?v=Fw3jv42GVKQ)
5. [Linus Torvalds: AI bug tools broke Linux security list | AI Weekly](https://aiweekly.co/alerts/linus-torvalds-ai-bug-tools-broke-linux-security-list)
6. [Torvalds joked that AI made Linux 7.3-rc2 this big, and nobody checked](https://thenextweb.com/news/linux-7-3-rc2-torvalds-ai-joke-tooling)
8. [Linus Torvalds "Did What I Preach", Used AI To Make... - Phoronix](https://www.phoronix.com/news/Linus-Torvalds-Assoc-Array)
9. [Linux founder Linus Torvalds says AI is a “gateway drug”... | TechRadar](https://www.techradar.com/pro/linux-founder-linus-torvalds-says-ai-is-a-gateway-drug-into-programming-but-cautions-about-using-ai-for-serious-work)
10. [GitHub - torvalds/linux: Linux kernel source tree · GitHub](https://github.com/torvalds/linux)
11. [Linus Torvalds says AI is a great coding gateway drug but...](https://www.thestack.technology/ai-coding-gateway-drug-linus-torvalds/)
12. [AI changed how you respond to incidents. - The New Stack](https://thenewstack.io/ai-incident-response-tabletops/)
13. [Linus Torvalds's first LLM-assisted patch series - lwn.net](https://lwn.net/Articles/1100449/)
14. [Linus Torvalds Debuts First LLM-Assisted Linux Kernel Patch ...](https://todayforai.com/en/story/story-b76d0e41-291)
15. [Linus Torvalds's first LLM-assisted patch series - apexneuralnews.com](https://apexneuralnews.com/ai/linus-torvaldss-first-llm-assisted-patch-series)
16. [Linus Torvalds posts his first · Hacker News | Zeli](https://zeli.app/story/50090842)
17. [Linus Torvalds Experiments with AI-Generated Kernel Code ...](https://linuxiac.com/linus-torvalds-uses-claude-code-to-write-linux-kernel-patches/)
18. [Linus Torvalds's first LLM-assisted patch series - daily.dev](https://daily.dev/posts/linus-torvalds-s-first-llm-assisted-patch-series-ftwbshwip)
19. [Linus Torvalds's First LLM-Assisted Patch Series · Discernion](https://discernion.com/article/linus-torvaldss-first-llm-assisted-patch-series)