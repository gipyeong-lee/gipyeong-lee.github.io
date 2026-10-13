---
layout: post
title: "AI 自行修改了數十萬行代碼？微軟耗資 1.6 億韓元（約 12 萬美元）的「Rust」大手術"
description: "微軟利用 AI 代理程式將 GitHub Copilot 的底層代碼完全重寫為 Rust。我們來探討這項耗資 12 萬美元的宏大實驗意義何在。"
summary: "微軟利用 AI 代理程式，成功將 GitHub Copilot 的底層軟體從 43 萬行的 TypeScript 重寫為超過 80 萬行的 Rust 代碼。"
tags: [AI, GitHub, Copilot, Rust, 軟體開發]
image: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K.jpg
image_alt: "象徵融合微軟與 GitHub 標誌的現代化開發環境圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "此案例展示了 AI 已超越單純工具的範疇，進化為能獨自完成複雜工程專案的主體。"
quiz:
  - question: "在此次微軟專案中，AI 代理程式扮演的核心角色是什麼？"
    choices: ["生成設計草圖", "將現有代碼轉換為 Rust", "物理安裝伺服器基礎設施"]
    answer: 1
    explanation: "AI 代理程式執行了將 GitHub Copilot 底層的 TypeScript 代碼重寫為 Rust 語言的任務。"
  - question: "此專案在過去被認為是不可能的，原因是為何？"
    choices: ["語言種類太多", "當時根本不存在 AI 代理程式", "因為這是規模龐大且極其複雜的重寫工作"]
    answer: 2
    explanation: "對於人類開發者而言，這類大規模系統的全面重寫是非常困難且低效的任務，在引進 AI 代理程式之前，這被視為無法實現的專案。"
  - question: "此專案的總 AI 運算費用大約是多少？"
    choices: ["約 12 萬美元（約 1.6 億韓元）", "約 5 萬美元", "無費用產生"]
    answer: 0
    explanation: "微軟為此次大規模代碼遷移支付了約 12 萬美元的運算及 Token 費用。"
lang: zh-tw
ref: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K
---

想像一下。您是一座巨大圖書館的圖書管理員，必須從零開始將圖書館整體的分類系統完全重組。將數十萬本書取出並按照新規則重新歸檔，這是一項單憑一人之力絕無法想像的龐大工程。然而，如果數千名人工智慧助理管理員同時投入，並在短短幾週內完成了這項任務，會是什麼樣的情景呢？

微軟（Microsoft）與 GitHub 最近就完成了類似的任務。他們將眾多開發者使用的 AI 工具「GitHub Copilot」的核心引擎，完全更換為另一種程式語言。

### 這為何重要？

「執行時期（Runtime，程式執行時所需的環境）」這個詞可能有點陌生。簡單來說，可以將其理解為在背後默默支持，確保我們每天使用的 GitHub Copilot App 或指令工具順暢運作的「基礎引擎」。引擎的更換，意味著 Copilot 將變得更快、更穩定地留在我們身邊。

最令人驚訝的是，這項專案並非由人工親手完成，而是由能夠自主思考與判斷的**「自主型 AI 編碼代理程式（Autonomous AI coding agents）」**所主導的 [[參考資料 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ), [參考資料 9](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/)].

### 輕鬆理解：更換「語言」的大手術

電腦程式語言就像我們使用的韓文或英文一樣。只是對電腦下指令的方式有所不同而已。此次，微軟將原本使用的「TypeScript（主要用於網頁開發的語言）」換成了名為「Rust」的語言。

比喻來說，如果 TypeScript 是可以自由書寫的「一般筆記本」，那麼 Rust 就像是「規則非常嚴格的數學公式集」。由於 Rust 非常重視代碼的安全性，一旦編寫完成，出錯機率比其他語言顯著降低。然而，由人類直接將數十萬行代碼轉換為如此嚴格的語言，這就如同將數千頁的論文，一字不差地按照新規則重新書寫一樣，是一項痛苦且耗時的工程。

為了執行這項任務，微軟的工程師雇用了一名聰明的助理——**AI 代理程式**。AI 代理程式如同老練的開發者，在閱讀現有代碼並理解其語境後，將其轉換為安全的 Rust 代碼。最終，高達 43 萬行的 TypeScript 代碼被成功重寫為超過 80 萬行的 Rust 代碼 [[參考資料 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ), [參考資料 12](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust)].

### 現況：AI 完成了不可能的任務

在過去，這個專案會被歸類為「不可能的計畫」，甚至根本不會開始。但藉由引進 AI 代理程式，這項龐大的遷移作業在歷經約 3 週的開發者工時以及 14.5 週內進行的 135 次更新後，順利畫下句點 [[參考資料 6](https://sygentai.com/blog/2026-09-21-google-shipped-an-open-agentic-orchestrator-and-what-it-actually-takes-off-your-), [參考資料 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ)].

過程中消耗了價值 12 萬美元（約 1.6 億韓元）的 Token（AI 處理費用）[[參考資料 9](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/), [參考資料 16](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)]. 雖然聽起來很昂貴，但考慮到若由數十名人類開發者耗費數月才能完成的大規模手術成本，就能看出 AI 的執行效率有多高。雖然過程中出現了數十個需要修正的錯誤，但最終在完整維持代碼品質的前提下，完成了成功的遷移 [[參考資料 12](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust), [參考資料 16](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)].

### 未來展望

此案例是象徵軟體開發未來發展的強力信號彈。未來將迅速從「開發者親手編寫代碼的時代」，邁向「開發者向 AI 代理程式提出目標並審核結果的時代」。

微軟的成功暗示了未來企業在將過時系統更換為現代化環境時，將會把 AI 代理程式列為必備工具。如果您使用的智慧型手機語音助理或工作通訊軟體，未來被更換為更快速、更安全的底層引擎，那麼在背後，或許就有著如本次一樣，由 AI 進行的巨大園藝作業。

---
**MindTickleBytes 的 AI 記者觀點**
AI 能自行修改並優化代碼，這不僅僅是成本問題。這意味著人類曾因技術限制而放棄的創意，現在有了名為「AI 代理程式」的翅膀，正式進入了夢想成真的時代。

## 參考資料
1. [MicrosoftagenticallyportsCopilotruntimetoRustfor$120K](https://www.devclass.com/devops/2026/09/19/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297592)
2. [Vue HN 2.0 |MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49763701)
3. [Unsealed Documents HighlightMicrosoftAnd OpenAI Concerns Over...](https://www.finanznachrichten.de/nachrichten-2026-09/69622107-unsealed-documents-highlight-microsoft-and-openai-concerns-over-use-of-news-content-020.htm)
4. [Microsoftand Citrix mix 'n' match fake desktops](https://www-theregister-co-uk.nproxy.org/2009/07/13/citrix_microsoft_virtual_pcs/)
5. [Rustin Visual Studio Code](https://code.visualstudio.com/docs/languages/rust)
6. [Google shipped an open agentic orchestrator, and what it actually...](https://sygentai.com/blog/2026-09-21-google-shipped-an-open-agentic-orchestrator-and-what-it-actually-takes-off-your-)
7. [AI Accelerates Code Production, Not Responsibility | LinkedIn](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ)
9. [MicrosoftAgenticallyPortsCopilotRuntimetoRust](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/)
10. [Vue HN 2.0 |MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49773998)
11. [Microsoftporte leruntimeCopilotversRustde façon... — Fellow](https://www.fellow.news/article/www.theregister.com-devops-2026-09-18-microsoft-agentically-ports-copilot-runtime-to-rust-for-120k-5297549)
12. [MicrosoftreescreveruntimedoCopilotemRust· NewsletterOficial](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust)
14. [MicrosoftagenticallyportsCopilotruntimetoRustfor$120K](https://modernorange.io/item/49773998)
15. [GoogleNews-Microsoft-Latest](https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFJ6ZGpRU0FtVnNLQUFQAQ?hl=en-US&gl=US&ceid=US:en)
16. [GitHub Engineers Use AI Agents toPortCodebasetoRust| LinkedIn](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)
17. [MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vk.ru/wall-238001904_5872)
18. [RuStore — каталог мобильных приложений и игр для Android](https://www.rustore.ru/)