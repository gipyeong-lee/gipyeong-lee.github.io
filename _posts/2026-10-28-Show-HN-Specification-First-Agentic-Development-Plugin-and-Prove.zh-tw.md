---
layout: post
title: "看著 AI 寫出的程式碼，懷疑「為什麼要這樣寫」？「規格優先開發」能成為解藥嗎？"
description: "介紹 AI 編碼代理撰寫程式碼時的意圖遺失問題，以及用於解決此問題的「規格優先代理開發 (SFAD)」方法論。"
summary: "在 AI 主導編碼的時代，為了避免時間一久就沒人記得程式碼內容，強調在作業前先檢閱並記錄規格書的「規格優先代理開發 (SFAD)」方法論正受到矚目。"
tags: [AI, 開發, 編碼, 生產力, 技術]
image: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove.jpg
image_alt: "AI 代理與人類開發者協作，並在螢幕上顯示詳細設計文件進行溝通"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在 AI 的速度與人類深度思考的交會點上，規格書不僅僅是紀錄，更將成為理解程式碼的指標。"
quiz:
  - question: "「規格優先代理開發 (SFAD)」試圖解決的核心問題是什麼？"
    choices: ["AI 的學習速度降低", "上下文記憶喪失及對程式碼意圖的遺忘", "硬體成本增加"]
    answer: 1
    explanation: "SFAD 旨在防止因時間久遠導致無人記得 AI 建構程式碼的原因，以及架構變質的問題。"
  - question: "下列何者為 SFAD 方法論的核心流程？"
    choices: ["先編寫程式碼，之後再產生規格書", "作業前規格檢閱、隔離的作業環境、分階段審核", "放任 AI 自行決定所有需求"]
    answer: 1
    explanation: "SFAD 遵循在編寫程式碼前定義問題、驗證限制條件並確認規格書的流程。"
  - question: "針對「規格優先開發」，為何會出現批判性觀點？"
    choices: ["因為撰寫太多規格書成本過高", "在實際產品環境中，往往無法提前預知所有初始需求", "因為 AI 無法理解規格書"]
    answer: 1
    explanation: "有觀點指出，在產品開發環境中，決策往往是在連自己不知道什麼都不知道的狀態下做出的，強求初始規格書反而可能導致混亂。"
lang: zh-tw
ref: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove
---

想像一下，您幾個月前請 AI 代理幫忙製作了一個很棒的網站功能。結果突然發生錯誤，需要修改那段程式碼。當您打開程式碼時，完全看不懂為什麼要這樣寫。「我當初為什麼這樣實作？」、「AI 為什麼用這種方式設計？」

在 AI 瞬間就能產出大量程式碼的時代，我們往往會遺失這些程式碼的「根源」與「意圖」。最近在開發者之間受到矚目的「規格優先代理開發 (SFAD, Specification-First Agentic Development)」正是源於這種顧慮。[規格優先代理開發 - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)

## 為什麼這很重要？

過去的開發工作由人類親手撰寫每一行程式碼，因此至少開發者的腦海中保有「為什麼」要這樣寫的脈絡。然而，在 AI 主導編碼的現在，專案開始半年後，就發生了沒人記得程式碼為何構成那種結構的現象。這被稱為「上下文記憶喪失 (Context Amnesia)」。[規格優先代理開發 - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)

若這種情況反覆發生，就會出現與系統初衷不符、設計走樣的「架構變質 (Architectural Drift)」。這會導致企業的維護成本暴漲，最終成為製造技術債的元兇。為了讓我們能與 AI 進行更深層的協作，比起單純快速產出程式碼，「證明為何而做」的過程變得不可或缺。

## 簡單來說

若將 SFAD 比喻為建築，就像是 **「在蓋房子之前先確認好詳細設計藍圖，並將施工過程中的所有變更事項詳細記錄在日記本中」**。

過去我們可能模糊地要求 AI「幫我做這個功能」，但在 SFAD 模式下，會經過更系統化的步驟：

1. **定義使用案例**：在編寫程式碼前，明確定義「為什麼需要這個功能」。[Brendan Small — SFAD](https://brendansmall.co/sfad)
2. **撰寫並檢閱規格書**：將問題具體化並驗證限制條件後，將該規格書進行「鎖定 (Lock)」。[Brendan Small — SFAD](https://brendansmall.co/sfad)
3. **分階段執行**：讓 AI 代理根據審核完畢的規格書撰寫程式碼，即便只是微小的變更也必須經過審核並記錄。[Spec-first agentic development - spec-first.dev](https://spec-first.dev/)

如此一來，當 AI 在撰寫程式碼時，就能隨時確認「規格書」這座指標。為此開發的插件已與 Claude Code 等 AI 工具整合，強制 AI 在執行任務時必須記錄並檢閱規格書。[Spec-First - Spec-driven agentic - Hacker News | Zeli](https://zeli.app/story/50260571)

## 我們現在處於什麼位置？

已有許多開發者將此方法應用於實際工作中。一位從 2026 年初開始使用該插件的開發者表示，他已經撰寫了超過 1,000 份規格書，並成功構建了超過 50 萬行程式碼。[Show HN: Spec-first agentic development plugin reports 500k...](https://shortsingh.com/article/show-hn-spec-first-agentic-development-plugin-reports-500k-lines-built-from-1-00)

然而，這種方式並非適用於所有情境。部分人士指出，實際的產品開發環境非常靈活。在啟動階段將所有事物規格化反而可能降低效率。因為很多時候我們是在連自己不知道什麼都不知道的狀態下開始的，強求初始規格書反而可能向 AI 傳遞相互衝突的需求，進而引發混亂。[Show HN: Specification First Agentic Development Plugin and Prove](https://hn.nuxt.dev/item/50260571)

## 即將到來的是什麼？

AI 與人類的協作將會變得越來越精緻。AI 不再止步於產出程式碼，而是從企劃、實作到維護負起全責的「代理中心開發 (Agentic-first Development)」正全面展開。[Let’s Talk Agentic Development | Spotify x Anthropic Live](https://www.youtube.com/watch?v=fHDGQHr_agg)

未來，「實力」的評估標準將不再僅是 AI 能產出多少程式碼，而是它能多麼邏輯地說明自己所寫設計的根據。SFAD 作為起點，將成為將 AI 從難以捉摸的「黑盒子」轉變為可信賴協作工具的重要指標。

---

### MindTickleBytes AI 記者觀點
比起 AI 代理能取代編碼的事實，更重要的是我們擁有了能與 AI 進行「對話」的共同語言（規格書）。將人類的判斷力加入 AI 的速度中，這方式即將成為未來的標準。

## 參考資料

1. [Show HN: Specification First Agentic Development Plugin and Prove](https://hn.nuxt.dev/item/50260571)
2. [Spec-first agentic development · spec-first.dev](https://spec-first.dev/)
3. [Spec-First - Spec-driven agentic · Hacker News | Zeli](https://zeli.app/story/50260571)
4. [Specification-First Agentic Development - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)
5. [Releases · holgerleichsenring/specification-first-agentic ...](https://github.com/holgerleichsenring/specification-first-agentic-development/releases)
6. [Show HN: Spec-first agentic development plugin reports 500k ...](https://shortsingh.com/article/show-hn-spec-first-agentic-development-plugin-reports-500k-lines-built-from-1-00)
7. [spec-first: 规范驱动的代理开发插件 — Show HN: Specification First...](https://zeli.app/zh/story/50260571)
8. [Brendan Small — Specification First Agentic Development](https://brendansmall.co/)
9. [Books by Anatoly Volkhover | Agentic Spec-Driven Development...](https://anatoly.com/books)
10. [Let’s Talk Agentic Development | Spotify x Anthropic Live - YouTube](https://www.youtube.com/watch?v=fHDGQHr_agg)
11. [Flowith AI - Your Agentic Workspace](https://flowith.io/)
12. [Manus: Hands On AI](https://manus.im/)
13. [Book Review: Agentic Spec-Driven Development](https://www.plainionist.net/Agentic-Spec-Driven-Development/)
14. [SFAD — Specification First Agentic Development | Brendan Small](https://brendansmall.co/sfad)
15. [jsell-rh/agentic-development-plugins | Awesome Claude Plugins](https://awesomeclaudeplugins.com/jsell-rh/agentic-development-plugins)
16. [Let’s Talk Agentic Development: Spotify x Anthropic Live](https://engineering.atspotify.com/2026/4/anthropic-agentic-development)