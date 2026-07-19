---
layout: post
title: "AI 用 11 天重寫了 100 萬行代碼？JavaScript 運行時「Bun」的驚人蛻變"
description: "探索 AI 驅動的大規模代碼轉換歷史，了解 JavaScript 運行時 Bun 如何透過 Rust 語言獲得重生。"
summary: "AI 模型 Claude 將 JavaScript 運行時「Bun」的 100 萬行代碼，在短短 11 天內重新編寫為 Rust 語言。"
tags: [AI, Bun, Rust, Claude, 程式設計]
image: 2026-07-19-Claude-Code-uses-Bun-written-in-Rust-now.jpg
image_alt: "象徵 AI 優化並重寫代碼的數位圖形。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人類開發者需要 3 人耗時 1 年才能完成的工作，AI 僅用 11 天就完成了，這一事實表明軟體開發的範式已經徹底改變。現在，開發者的核心競爭力不再是『寫代碼有多快』，而是『如何善用 AI』。"
quiz:
  - question: "Bun 最初是用什麼語言編寫的？"
    choices: ["Rust", "Zig", "Python"]
    answer: 1
    explanation: "Bun 最初是用 Zig 語言編寫的，但最近已透過 Claude AI 完成了語言遷移至 Rust。"
  - question: "這次代碼重寫專案花費了多少時間？"
    choices: ["11 天", "11 個月", "1 年"]
    answer: 0
    explanation: "Bun 的創始人 Jarred Sumner 利用 Claude Code，在 11 天內重寫了超過 100 萬行代碼。"
  - question: "這次轉換至 Rust 語言帶來了什麼效能提升效果？"
    choices: ["檔案下載速度提升 50%", "Linux 環境下的啟動速度改善 10%", "記憶體使用量減少 90%"]
    answer: 1
    explanation: "在 Linux 環境下，Claude Code 的啟動速度比以前快了 10%。"
lang: zh-tw
ref: 2026-07-19-Claude-Code-uses-Bun-written-in-Rust-now
---

想像一下。假設您需要將一座擁有超過 100 萬本書的巨型圖書館翻譯成另一種語言。如果由人工親自完成，這項巨大的工程需要耗費數年時間，但如果有辦法在短短 11 天內就完成呢？最近在軟體開發領域，這樣驚人的事情確實發生了。

AI 模型「Claude」將 JavaScript（在網頁瀏覽器中運行的程式語言）運行時「Bun」的核心基礎，完全重寫為全新的語言「Rust」（一種強調記憶體安全與效能的系統程式語言），重寫代碼量超過 100 萬行 [Source 9, Source 13]。今天這篇文章將帶您深入淺出地了解為什麼這次大規模代碼轉換如此重要，以及它對我們的日常生活有何意義。

### 這為何重要？

「Bun」是一個幫助開發者更快速、更有效率地執行 JavaScript 或 TypeScript 代碼的工具 [Source 3, Source 4]。那麼，為什麼要將這個重要的工具從原有的語言轉換為 Rust 呢？

最大的原因是「安全」與「速度」。Rust 語言能讓電腦記憶體管理更加安全，從而減少程式意外崩潰的情況 [Source 3, Source 10]。此外，它也有助於效能優化。事實上，在這次重寫之後，「Claude Code（AI 輔助程式設計工具）」在 Linux 環境下的啟動速度比以往提升了 10% [Source 1, Source 7]。這對我們一般使用者來說可能感受微乎其微，但在技術層面上卻是非常重要的進步。

### 簡單理解：就像更換食譜一樣

我們可以這樣比喻：想像您經營一家為數千人提供餐點的大型餐廳。起初，您使用「Zig」這種工具精心制定了食譜。但為了能更安全、更有效率地配送餐點，您決定將食譜完全更換為全球廚師最信賴的新工具「Rust」。

在過去，這份龐大的食譜必須由人工一字一句重新撰寫。但這一次，有一位名叫 Claude 的「超人 AI 助手」代勞了。Bun 的創始人 Jarred Sumner 設定了約 50 個 AI 工作流程，指揮 Claude Code 在 11 天內不間斷地將超過 100 萬行代碼移植並重寫為 Rust [Source 12, Source 13]。換句話說，這項原本需要 3 人耗時 1 年的工作，透過 AI 在短時間內就完成了 [Source 16]。

### 現狀：AI 直接管理代碼的時代

目前從 Claude Code 2.1.181 版本開始，已經內含這個基於 Rust 的全新 Bun 運行時 [Source 1, Source 7]。開發者們依然像往常一樣編寫代碼，但背後運作的引擎已經替換為更安全、更快速的 Rust 引擎。

當然，並非所有人都對這種 AI 大規模代碼修改給予一致讚賞。也有人對 AI 生成代碼的驗證過程是否不足表達了擔憂 [Source 13]。然而，Anthropic（Claude 的開發商）透過這次專案，證明了 AI 能夠多麼成功地執行複雜而龐大的軟體專案，展現了其可能性 [Source 9, Source 16]。

### 未來將如何發展？

這次案例顯示，AI 不再僅僅是回答問題或撰寫文章，它已經成為可以親自改變巨大技術基礎的「工程主體」 [Source 9, Source 10]。未來當我們使用的應用程式或服務變得更安全、更新更迅速時，其背後很有可能有一位與人類開發者共同日夜修復代碼的 AI 同僚。

未來我們將迎來 AI 帶來的複雜技術轉型，從而享受更快速、更強大的軟體環境。變革已經開始，而其速度遠超乎我們的預期。

### MindTickleBytes AI 記者的觀點
這次事件不僅僅是更換了一種程式語言。人類需要 1 年才能完成的艱鉅工作，AI 僅在 11 天內就順利完成，這意味著「軟體維護」的定義本身已經改變。現在，我們不該恐懼技術變革，而是該思考如何聰明地驅動「AI」這個工具，以更快速地推進我們想要的未來。

## 參考資料

1. [Claude Code uses Bun written in Rust now - simonwillison.net](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)
2. [Claude Code uses Bun written in Rust now - daily.dev](https://daily.dev/posts/claude-code-uses-bun-written-in-rust-now-sxbybasdo)
3. [Claude Code uses Bun written in Rust now | DeepHorus](https://www.deephorus.com/blog/2026-07-19-claude-code-uses-bun-written-in-rust-now/)
4. [Claude Code uses Bun written in Rust now | AINews](https://www.ainews.tech/article/2058)
5. [Rewriting Bun in Rust | Bun Blog](https://bun.com/blog/bun-in-rust)
6. [Claude Code adopts Rust-based Bun runtime for faster startup ...](https://news.linxi.com.au/news/claude-code-shifts-to-rust-based-bun-runtime-claiming-faster-startup)
7. [Claude Code adopts Bun runtime rewritten in Rust, speed ...](https://savedelete.com/news/claude-code-bun/)
8. [Bun Rewrites in Rust: Technical Review of the Zig-to-Rust Migration | Fawad Hussain Syed](https://fawadhs.dev/blog/bun-rust-rewrite-technical-review)
9. [Claude Rewrites Bun's Million Lines of Code in 11 Days for $165,000, Setting a New Benchmark for AI-Assisted Programming — BigGo Finance](https://finance.biggo.com/news/b171d858-6390-4aef-bd0b-a651cfa942f6)
10. [Burned $160,000, Wrote 1M Lines of Code Nonstop: How Bun's Founder Rewrote the Entire JavaScript Runtime Foundation Using Claude AI](https://eu.36kr.com/en/p/3899401843017608)
11. [AI Porting: Claude Rewrites Bun Codebase in Rust | heise online](https://www.heise.de/en/news/AI-Porting-Claude-Rewrites-Bun-Codebase-in-Rust-11294318.html)
12. [How Bun's founder rewrote the codebase in Rust with Claude](https://www.thestack.technology/bun-rust-rewrite-fable-ai/)
13. [Zig creator calls Bun’s Claude Rust rewrite ‘unreviewed slop’](https://www.theregister.com/devops/2026/07/14/zig-creator-calls-buns-claude-rust-rewrite-unreviewed-slop/5270743)
15. [Why not rewrite claude-code in Rust? So, Anthropic acquires Bun team because cla... | Hacker News](https://news.ycombinator.com/item?id=48019019)
16. [One Anthropic Engineer Rewrites Bun In Rust In 11 Days With AI, Says Would've Taken 3 Engineers A Year Earlier](https://officechai.com/ai/one-anthropic-engineer-rewrites-bun-in-rust-in-11-days-with-ai-says-wouldve-taken-3-engineers-a-year-earlier/)