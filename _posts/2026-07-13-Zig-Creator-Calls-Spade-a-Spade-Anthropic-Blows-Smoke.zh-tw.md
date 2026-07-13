---
layout: post
title: "AI 撰寫的程式碼是「垃圾」嗎？程式語言 Zig 與 Anthropic 的正面交鋒"
description: "透過全面禁止 AI 撰寫程式碼的程式語言 Zig，以及因此被迫放棄 4 倍效能提升的 Anthropic 旗下 Bun 之案例，探討 AI 時代的軟體開發爭議。"
summary: "程式語言 Zig 全面禁止 AI 撰寫的任何貢獻，導致 Anthropic 收購的 Bun 所開發出效能提升 4 倍的程式碼，無法併入官方專案中。"
tags: [AI, Zig, Bun, 程式設計, 開源]
image: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke.jpg
image_alt: "電腦螢幕上程式碼與 AI 機器人圖示碰撞的視覺圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開源生態系統正因 AI 工具的運用而走向兩極化。在技術價值與開發者文化這兩股價值觀碰撞的節點上，我們該建立什麼樣的準則？"
quiz:
  - question: "程式語言 Zig 禁止 AI 相關貢獻的原因為何？"
    choices: ["AI 產出的程式碼成本過高", "AI 產出的程式碼品質低劣且浪費審查時間", "版權問題"]
    answer: 1
    explanation: "Zig 的創辦人 Andrew Kelley 認為 AI 生成的程式碼品質低劣，不僅沒有價值，還會浪費核心開發團隊寶貴的審查時間。"
  - question: "Anthropic 的 Bun 專案所開發的效能改善，為何無法併入 Zig 官方專案？"
    choices: ["效能改善幅度不足", "因為 Zig 的 AI 貢獻全面禁止政策", "技術相容性問題"]
    answer: 1
    explanation: "Bun 實現了 4 倍的效能提升，但由於 Zig 嚴格的 AI 貢獻禁止政策，該程式碼無法併入（upstream）官方專案。"
  - question: "Zig 對 AI 貢獻的禁止範圍為何？"
    choices: ["僅禁止程式碼", "程式碼、留言、議題、臭蟲報告回覆等所有形式的貢獻皆禁止", "僅禁止現有貢獻者"]
    answer: 1
    explanation: "Zig 禁止任何 AI 涉入的貢獻形式，範圍不僅限於程式碼，還包括留言、議題（Issue）、合併請求（Pull Request）及臭蟲追蹤系統的回覆等。"
lang: zh-tw
ref: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke
---

想像一下。你耗時數月通宵達旦，打造出一台極其高效的機械裝置。這台裝置的運作速度比現有的零組件快上整整 4 倍。然而，就在你準備將它送上正式生產線時，工廠負責人冷冷地對你說：「你在製作過程中用了哪怕是一丁點的人工智慧 (AI) 工具？那絕對不行。立刻把它丟了。」

現在，開源程式設計界正發生著這樣的事。這場發生在程式語言「Zig」與被 Anthropic 收購的 JavaScript 執行環境「Bun」之間的爭議，在 AI 輔助軟體開發的當下，為我們拋出了一個極其根本的難題。

## 為何這件事很重要？

我們日常使用的應用程式變得越來越聰明，背後是無數開發者的心血。如今的開發者利用 AI 工具，能更快速、更有效率地建立軟體。然而，「誰」與「如何」製作的立場，與「只要技術成果好就好」的立場，正發生正面衝擊。如果像 Zig 的案例一樣，連使用 AI 輔助的成果都被排斥，未來開發者是否會對使用 AI 工具感到卻步？反過來說，如果毫無審核地任由 AI 程式碼氾濫，軟體的穩定性又該由誰負責？

## 簡而言之 (The Explainer)

Zig 是一門廣受好評的高效能程式語言，而 Bun 則是使用 Zig 所開發的 JavaScript 執行環境，近期已被 AI 大廠 Anthropic 收購[Source 4, Source 6, Source 18]。

做個比喻，Zig 就像是一家極其講究職人精神的「高級木工坊」。這間工坊的負責人 Andrew Kelley 將 AI 撰寫的程式碼評價為「始終是垃圾 (invariably garbage)」[Source 1, Source 5]。他認為 AI 寫出的程式碼既無實質價值，又會消耗核心開發團隊寶貴的審查時間。因此，他制定了嚴格政策：不僅是程式碼，連留言、議題討論，甚至對臭蟲報告的回覆，只要有 AI 的一絲涉入，一律全面禁止貢獻[Source 1, Source 2]。

相對地，Bun 團隊積極運用 AI，成功將編譯速度（將人類編寫的程式碼轉換為電腦語言的過程）提升了約 4 倍，成果驚人[Source 2, Source 3, Source 4]。但 Zig 的門檻極高。Bun 團隊原想將這項優異成果併入官方專案，但因明確知道會因為使用了 AI 而遭拒，最終決定放棄併入，改以獨立版本（分岔，Fork）的形式維護專案[Source 2, Source 4]。

## 現狀

目前 Zig 的態度十分堅決。只要懷疑有使用 AI 之嫌，即便尚未評估技術價值，也有權直接拒絕[Source 2]。事實上，許多開發者對此政策反應熱烈。部分人士對於 Bun 專案的程式碼庫與文件被「AI 垃圾內容 (AI slop)」充斥感到反感，甚至出現了想離開 Bun 的聲音[Source 17]。

另一方面，Anthropic 與 Bun 團隊看來會為了技術優勢持續使用 AI 工具。因為 Bun 目前正作為 Anthropic「Claude Code」或「Claude Agent SDK」的基礎架構使用[Source 16, Source 18]。這意味著優先考量技術成果的一方，與優先考量原則的一方，正各奔前程，各自共存。

## 未來發展為何？

這場爭論不僅是單一專案的問題。「AI 輔助貢獻的接受底線在哪裡？」已成為未來所有開源專案都必須回答的作業。Zig 提出了一個極端且明確的標準。未來會有更多專案制定各自的「AI 貢獻準則」，或像 Zig 一樣全面禁止，或是經過適當審核後予以接納。開發者們如今已進入一個必須仔細審視自己參與專案政策的時代。

## MindTickleBytes 的觀點

「技術僅是工具」的論調，與「該工具產出的本質已發生改變」的見解，正激烈對抗中。重點或許不在於是否使用了工具，而在於該工具如何影響最終產出的品質與生態系的永續性。Zig 的嚴格究竟會成為守護開源純粹性的盾牌，還是會在不斷演變的開發趨勢中自絕於外的作法，仍有待觀察。

## 參考資料

1. [Zig bans LLM contributions, forcing Bun to fork | AI Weekly](https://aiweekly.co/alerts/zig-bans-llm-contributions-forcing-bun-to-fork)
2. [Zig Draws Hard Line On AI, Bun Chooses Fork Over Upstreaming - Open Source For You](https://www.opensourceforu.com/2026/05/zig-draws-hard-line-on-ai-bun-chooses-fork-over-upstreaming/)
3. [ZIG BANNED ANTHROPIC FROM ITS OWN LANGUAGE #Shorts - YouTube](https://www.youtube.com/shorts/sYMuqS2oyUw)
4. [Zig Reinforces LLM Contribution Ban As Anthropic-Owned Bun Forks 4x Gain](https://winbuzzer.com/2026/05/01/zig-llm-contribution-ban-bun-4x-speedup-downstream-xcxwbn/)
5. [Zig president says AI coding contributions are 'invariably garbage,' so he banned them](https://www.businessinsider.com/zig-programming-language-ai-rules-2026-5)
6. [The Zig project's rationale for their firm anti-AI contribution policy](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)
16. [Anthrophic's Bun team trials port from Zig to Rust](https://www.devclass.com/software/2026/05/11/anthrophics-bun-team-trials-port-from-zig-to-rust/5237835)
17. [This feels more like a reaction to Zig's anti-LLM policy than anything. Anthropi... | Hacker News](https://news.ycombinator.com/item?id=48017387)
18. [Bun’s Zig to Rust Rewrite: Anthropic’s AI Code Experiment | byteiota](https://byteiota.com/buns-zig-to-rust-rewrite-anthropics-ai-code-experiment/)