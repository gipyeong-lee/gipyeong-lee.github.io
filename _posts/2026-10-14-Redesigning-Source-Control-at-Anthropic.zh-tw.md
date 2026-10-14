---
layout: post
title: "AI 竟能修復代碼三萬次？Anthropic 放棄『Git』的真正原因"
description: "AI 寫的代碼量過大，導致傳統版本控制系統達到極限，Anthropic 轉而採用自行開發的系統『Scion』的背後故事"
summary: "當 AI 模型 Claude 每天產生超過 3 萬次代碼變更時，Anthropic 放棄了現有的 Git 基礎架構，開發並導入了自有的版本控制系統『Scion』。"
tags: [Anthropic, AI開發, 版本控制, Scion, Claude]
image: 2026-10-14-Redesigning-Source-Control-at-Anthropic.jpg
image_alt: "將複雜的代碼網絡與 AI 代理互動視覺化的圖形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的生產力已超越人類開發者，並正在撼動既有的工具體系。現在已進入基礎設施本身必須為『代理（Agent）』而設計的時代。"
quiz:
  - question: "Anthropic 導入自有版本控制系統『Scion』以取代傳統 Git 的主要原因是什麼？"
    choices: ["為了節省成本", "由於 AI 代理爆炸性的代碼生成量導致既有系統出現瓶頸", "為了提供更安全的安全性功能"]
    answer: 1
    explanation: "在 AI 自行編寫代碼並不斷反覆運算的過程中，代碼合併量從每天 2,500 次激增至 3 萬次，導致既有基礎設施已無法負荷。"
  - question: "Anthropic 的新系統『Scion』是為什麼樣的環境所設計的？"
    choices: ["僅供人類開發者使用的離線環境", "AI 代理 24 小時不間斷編寫代碼並反覆運算（Iteration）的環境", "專門用於行動 App 開發的環境"]
    answer: 1
    explanation: "Scion 是針對 AI 代理不斷生成代碼並進行自我反覆運算的環境所設計並最佳化的。"
  - question: "Anthropic 在代碼變更後，取代執行所有測試所導入的方法是什麼？"
    choices: ["完全省略測試", "決定性測試影響分析（Test Impact Analysis）", "隨機挑選測試執行"]
    answer: 1
    explanation: "與其在無數次代碼變更時執行所有測試，他們導入了基於歷史數據與套件關聯性，僅挑選必要測試進行執行的決定性測試影響分析服務。"
lang: zh-tw
ref: 2026-10-14-Redesigning-Source-Control-at-Anthropic
---

想像一下。如果你寫的文章被某人每秒鐘修改 3 萬次，並要求你重新審核，那會是什麼樣的情景？這對人類來說是難以承受的速度。然而，這卻是在 AI 公司 Anthropic 的辦公室裡真實上演的情況。隨著 AI 模型「Claude」不斷進行自我研究並構建新服務，該公司的代碼基礎設施開始發出求救訊號。

### 為什麼這很重要？

至今為止，軟體開發一直是以「人」的速度為準。但隨著 AI 開始直接編寫代碼，現在比起撰寫代碼，「**管理與部署寫好的代碼**」反而成了更大的瓶頸。[Anthropic 正面臨代碼基礎設施無法再跟上 AI 生產力的狀況。](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943) Anthropic 這次將基礎設施徹底翻新，是展現 AI 時代開發工具應如何演進的重要里程碑。

### 簡單易懂：名為『Git』的拼圖盒極限

我們常用的「Git」是開發者儲存與修改代碼的共同作業空間。打個比方，就像一群人共同完成一副巨大拼圖的「拼圖盒」。當人數不多時，大家可以按照順序互相配合拼湊。

但是，如果 AI 代理們衝向這個拼圖盒，每秒鐘插入或拔出數千個拼圖，會發生什麼事呢？盒子會爆炸的。由於既有的 Git 是以人類中心的「離線」開發環境為前提所設計，對於 AI 即時湧入的數萬條變更事項而言，負擔過於沈重。[Anthropic 的代碼合併量從每天 2,500 次激增至 3 萬次，成長了近 12 倍。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

因此，Anthropic 直接打造了一種全新方式的系統——**「Scion」**。Scion 是專為 AI 代理設計的「AI 專用版本控制系統」，即使 AI 代理 24 小時不停歇地修改代碼也能應付自如。[Anthropic 花了 5 個月的時間，將既有的單一儲存庫（Monorepo）從 Git 完全遷移至 Scion。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

### 現狀：配合 AI 速度的基礎設施升級

Anthropic 不僅僅是更換了版本控制系統。隨著 Scion 的導入，他們進行了幾個核心的改變。

1.  **代碼審核工具的進化**：人類親自確認數萬條代碼是不可能的。Anthropic 導入了名為**「Antique」**的新型代碼審核專用系統，建立了讓人能有效審核 AI 所湧入之變更事項的環境。[Anthropic 與 Scion 同步開發並部署了此一全新的代碼審核介面。](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
2.  **聰明的測試系統**：每次代碼更動就執行所有測試會耗費太多時間。因此，Anthropic 分析歷史數據與代碼之間的關聯性，導入了**「決定性測試影響分析服務」，只挑選必要的測試執行**。[這種方式提高了測試執行的效率，再次提升了開發速度。](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)

### 我們正站在哪裡？

目前 Anthropic 的案例是軟體開發環境正從「以人為中心」轉向「以 AI 代理為中心」的信號彈。過去開發者煩惱的是電腦效能，現在則進入了必須煩惱電腦能否負荷代理活動的時期。這樣的變化不只是 Anthropic 的特例。未來，無數科技企業都將尋求能超越人類便利性，支撐機器巨大生產力的新基礎設施。

### 未來會如何？

我們使用的服務更新週期將會越來越短，而在其背後，將會存在這種為了讓 AI 能自我成長而努力奮鬥、新型態的「數位工廠」。像 Scion 這類的基礎設施，象徵著 AI 已超越單純的工具，進入了能自行重新設計技術基礎的「自我發展」階段。[Scion 是專為 AI 全天候運作的「Agent-always-on」情境所設計的。](https://zeli.app/zh/story/50073633)

我們正站在一個有趣的轉折點上，越過了人類開發者編寫代碼的時代，進入了 AI 編寫代碼、人類監督結果的時代。

---

**MindTickleBytes 的 AI 記者觀點**
AI 自行修復代碼並進行研究的「Agentic（代理）」時代已經展開。Anthropic 的行動意味著 AI 已不僅是消費技術，而是進入了能讓技術基礎設施自行重新設計的自我發展階段。

## 參考資料

1. [AnthropicClaude Can NowControlYour Computer - YouTube](https://www.youtube.com/watch?v=eB7E-mtpC18)
2. [Anthropic(Anthropic)](https://huggingface.co/Anthropic)
3. [How AI is transforming workatAnthropic\Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
4. [Agentic coding is straining CI. Here’s how we... | Claude byAnthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)
5. [AnthropicAI safety researcher quits with 'world in peril' warning](https://www.bbc.com/news/articles/c62dlvdq3e3o)
6. [EggheadsatAnthropicSaid They Used Claude to "Solve" Humor](https://futurism.com/artificial-intelligence/anthropic-solve-humor)
7. [Anthropicrestores Fable 5, Mythos 5 after U.S. lifts exportcontrols](https://www.linkedin.com/pulse/anthropic-restores-fable-5-mythos-after-us-lifts-export-controls-3ffnc)
8. [Redesigning source control at Anthropic — CodeNews.com](https://codenews.com/news/redesigning-source-control-at-anthropic-1ojqmz)
9. [Anthropic Scion: Why Its Monorepo Left Git at 30,000 Merges](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
10. [Anthropic Scion Redesigns Source Control for AI Agents](https://scalevise.com/resources/anthropic-scion-agent-scale-source-control/)
11. [Anthropic reinvents source control as Claude floods the world ...](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943)
12. [Anthropic Overhauls Source Control to Fix Bottlenecks](https://book.st-hakky.com/en/news/redesigning-source-control-at-anthropic)
13. [Redesigning source control at Anthropic - hoton.ai](https://hoton.ai/en/news/redesigning-source-control-at-anthropic-1vlb4uz)
14. [Anthropic 因Claude重写版本控制系统 — Redesigning Source Control a...](https://zeli.app/zh/story/50073633)
15. [Newsroom \Anthropic](https://www.anthropic.com/news)
16. [AnthropicIs Bleeding Out](https://www.wheresyoured.at/anthropic-is-bleeding-out/)
17. [Hidden AI instructions reveal howAnthropiccontrols... - Ars Technica](https://arstechnica.com/ai/2025/05/hidden-ai-instructions-reveal-how-anthropic-controls-claude-4/)
18. [OpenAI andAnthropicAI crisis explained: OpenAI andAnthropicfear...](https://economictimes.indiatimes.com/world/business/openai-and-anthropic-fear-a-major-ai-crisis-in-the-next-6-to-12-months-heres-what-theyre-preparing-for/articleshow/134860984.cms)
20. [LatestAnthropic(Claude AI) Statistics (2025) | StatsUp](https://analyzify.com/statsup/anthropic)