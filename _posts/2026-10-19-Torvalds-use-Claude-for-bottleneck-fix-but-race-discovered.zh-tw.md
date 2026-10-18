---
layout: post
title: "Linux 創始人 Linus Torvalds 將編碼工作交給 AI？結果出人意料..."
description: "探討 Linux 創始人 Linus Torvalds 為提升 Linux 核心效能，實驗性地運用 AI 工具「Claude Code」的過程，以及在開發中發現的技術限制。"
summary: "Linux 創始人 Linus Torvalds 為解決效能瓶頸，引入了 AI 編碼工具「Claude Code」，然而在生成的代碼中發現了致命的競態條件（Race Condition）錯誤。"
tags: [Linux, AI, Claude Code, Linus Torvalds, 編程]
image: 2026-10-19-Torvalds-use-Claude-for-bottleneck-fix-but-race-discovered.jpg
image_alt: "Linus Torvalds 在開發環境中使用 AI 編碼工具優化 Linux 核心原始碼的場景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 雖然能大幅提升開發者的生產力，但這個案例再次證明，對於核心技術的「驗證」環節，依然是人類不可或缺的職責。"
quiz:
  - question: "Linus Torvalds 試圖利用 AI 解決 Linux 核心的什麼問題？"
    choices: ["修正安全漏洞", "頁面快取（page cache）引用計數瓶頸", "網路速度下降"]
    answer: 1
    explanation: "Torvalds 試圖利用 AI 改進 Linux 核心的頁面快取（reference-counting）引用計數瓶頸問題。"
  - question: "Linux 核心審查人員在 AI 編寫的程式碼中發現了什麼問題？"
    choices: ["記憶體洩漏", "競態條件（Race Condition）", "錯誤的函式庫引用"]
    answer: 1
    explanation: "審查人員在程式碼發布僅 4 小時後，就發現了多個執行緒同時存取資源時產生的「競態條件（race condition）」錯誤。"
  - question: "關於這次 AI 應用專案的結果，下列敘述何者正確？"
    choices: ["生成了完美的程式碼並立即整合。", "在效能基準測試中表現優異，但發現了漏洞。", "AI 編寫的程式碼完全沒有效能提升。"]
    answer: 1
    explanation: "在合成基準測試中，讀取處理量提升了最高 23 倍，但因發現漏洞，最終並未進行實際整合。"
lang: zh-tw
ref: 2026-10-19-Torvalds-use-Claude-for-bottleneck-fix-but-race-discovered
---

想像一下，您打算更換一枚精心打磨數十年的精密手錶中的齒輪。如果不是親自動手修改，而是將設計工作交給一個非常聰明的人工智慧（AI），會發生什麼事呢？作業速度絕對會大幅提升，但會不會隱藏著我們未曾察覺的細小疏失呢？

最近，身為全球最著名開發者之一、Linux（電腦作業系統核心）創始人的 Linus Torvalds 就進行了這樣一項有趣的實驗。他運用 Anthropic 的 AI 編碼工具「Claude Code」來編寫改善 Linux 核心效能的程式碼。雖然結果令人驚豔，但也深刻揭示了人工智慧與人類協作時所面臨的現實課題。

## 為什麼這很重要？

Linux 是一項核心技術，廣泛應用於從 Android 手機到全球超級電腦、雲端伺服器等我們生活中的各個角落。因此，Linux 核心哪怕只有極微小的效能提升，都能同時提升全球無數裝置的處理速度。

這次嘗試是對「AI 是否能直接修改人類所創造出最高水準的複雜系統？」這一問題的挑戰。不僅止於請 AI 編寫程式碼，而是將優化效能的關鍵工作全權委託給 AI，這一點在開發者社群中引起了巨大的迴響。[出處: ZDNET](https://www.zdnet.com/innovation/linus-torvalds-uses-ai-to-write-linux-kernel-patch/)

## 簡單來說

這次 Torvalds 試圖與 AI 共同解決的問題，是 Linux 核心「頁面快取（page cache，將常用資料暫存於記憶體以快速讀取的技術）」中所發生的引用計數瓶頸（reference-counting bottleneck）現象。

簡單打個比方：在圖書館借書時，館員需要記錄借書人的名單並進行確認。當使用者只有一兩位時不成問題，但若成千上萬人同時湧入，館員面前就會排起長龍，造成瓶頸。在 Linux 系統中，當多個程式（處理程序）同時嘗試讀取資料時，也會面臨這種確認「誰正在使用該資料」的過程變慢的問題。

Torvalds 使用了「Claude Code」，讓 AI 編寫出繞過或優化此確認過程的程式碼。[出處: Linus Torvalds Uses Claude Code to Improve Linux Kernel](https://joho-todai.com/en/linus-torvalds-claude-code-linux-kernel-performance/) 令人驚訝的是，AI 不僅完成了這項作業的具體實作，還主動編寫了測試程式碼及相關說明文件。[出處: Linus Torvalds let Claude Code fix the Linux page cache. Then ...](https://daily.dev/posts/linus-torvalds-let-claude-code-fix-the-linux-page-cache-then-reviewers-found-a-race--weudloreo)

## 進展如何？

實驗結果相當令人振奮。在 Torvalds 的 Threadripper（高效能電腦處理器）系統上進行合成基準測試的結果顯示，資料讀取處理量竟然提升了最高達 23 倍。[出處: The New Stack](https://thenewstack.io/torvalds-claude-code-kernel/) 在一般筆記型電腦的環境下，小型讀取作業的速度也提升了近 3 倍，成果相當顯著。[出處: HwBusters](https://hwbusters.com/news/linus-torvalds-uses-ai-to-rework-the-linux-page-cache-tripling-small-read-throughput/)

然而，樂觀也就到此為止。Torvalds 建立了一個名為「noref-filemap-read-with-llm」的新核心分支並共享了成果，不到 4 小時，人類開發者就從程式碼中發現了致命的「競態條件（race condition）」。[出處: Verboo.ai](https://verboo.ai/en/blog/torvalds-claude-code-kernel)

「競態條件」簡單來說，就是當多個程式同時嘗試修改相同資料時，因為順序錯亂導致資料損壞或系統當機的錯誤。AI 寫出的程式碼看似極快且效能極佳，但卻存在破壞系統穩定性的漏洞。[出處: Linus Torvalds let Claude Code fix the Linux page cache. Then ...](https://thenewstack.io/torvalds-claude-code-kernel/)

## 未來會有什麼改變？

這次事件明確顯示，AI 可以成為優秀開發者的工具，但目前還無法完全取代人類嚴謹的驗證過程。Torvalds 通過這次實驗確認了 AI 在撰寫草稿或解決複雜問題時能提供極大幫助。

今後在開發現場運用 AI 進行效能優化的嘗試將會持續增加。然而，「越是 AI 編寫的程式碼，人類越需要進行更嚴謹的審查」這一新準則，將會成為開發者社群中不成文的常識。

## MindTickleBytes 的 AI 記者觀點

技術發展的速度遠超我們的想像。然而，正如再精密的機器，一枚小小的齒輪就能決定整體的命運，這次案例證明了人類的直覺與敏銳的驗證能力，在 AI 時代依然是無可替代的價值。AI 為我們插上了翅膀，但操縱方向舵的依然是人類的手。

## 參考資料

1. [LinusTorvaldsisusingAI to develop Linux kernel code now - ZDNET](https://www.zdnet.com/innovation/linus-torvalds-uses-ai-to-write-linux-kernel-patch/)
2. [Linus Torvalds let Claude Code fix the Linux page cache. Then ... - The New Stack](https://thenewstack.io/torvalds-claude-code-kernel/)
3. [Torvalds and Claude Code on the Linux kernel: the patch and ... - Verboo.ai](https://verboo.ai/en/blog/torvalds-claude-code-kernel)
4. [Linus Torvalds Uses Claude Code to Improve Linux Kernel ... - joho-todai.com](https://joho-todai.com/en/linus-torvalds-claude-code-linux-kernel-performance/)
5. [Linus Torvalds Uses Claude Code on a New Linux Kernel ... - blog.quadmeup.com](https://blog.quadmeup.com/2026/10/13/linus-torvalds-uses-claude-code-on-a-new-linux-kernel-performance-branch/)
6. [Linus Torvalds let Claude Code fix the Linux page cache. Then ... - daily.dev](https://daily.dev/posts/linus-torvalds-let-claude-code-fix-the-linux-page-cache-then-reviewers-found-a-race--weudloreo)
7. [Linus Torvalds Uses Claude Code to Rework the Linux Page ... - hwbusters.com](https://hwbusters.com/news/linus-torvalds-uses-claude-code-to-rework-the-linux-page-cache-tripling-small-read-throughput/)
8. [Linus Torvalds Uses Claude Code to Speed Up the Linux Kernel - krasa.ai](https://www.krasa.ai/news/linus-torvalds-claude-code-linux-kernel-page-cache-patch)