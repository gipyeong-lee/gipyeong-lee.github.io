---
layout: post
title: "在開發者招聘考試中擊敗人類的 AI？Anthropic 開啟「自主工程」的新世界"
description: "Anthropic 的最新 AI Claude Opus 4.5 在開發者考試中擊敗了人類。了解 Anthropic 工程師如何與 AI 協作，以及他們打造安全 AI 的秘密。"
image: 2026-04-12-Engineering-at-Anthropic.jpg
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 編寫代碼並自行審查的時代已經到來。現在，工程不僅僅是編寫代碼，更將成為與 AI 一同設計更安全、更可靠系統的藝術。"
lang: zh-tw
ref: 2026-04-12-Engineering-at-Anthropic
---

# 比人類開發者更聰明？Anthropic 打造「會自我工作的 AI」世界

想像一下，你正在參加一場極其苛刻的軟體開發者招聘考試。在必須於 2 小時內編寫複雜代碼並解決性能問題的這場考試中，你身旁的應試者獲得了比所有人類候選人都要高的分數。然而，如果那名應試者不是人，而是人工智慧（AI）呢？

事實上，這種電影般的情節已在現實中發生。2025 年 11 月 24 日，AI 研究公司 Anthropic 發布了其最新模型「Claude Opus 4.5」，並公開了一個令人震驚的事實：這款 AI 模型在一場專為招聘實際工程師而設計的困難技術測試中，記錄的分數高於任何人類應聘者 [Anthropic 發佈最新 AI 模型 Claude Opus 4.5 - CNBC](https://www.cnbc.com/2025/11/24/anthropic-unveils-claude-opus-4point5-its-latest-ai-model.html)。

今天，我們將深入探討這家開發驚人 AI 的公司——Anthropic 的工程世界。他們是如何與 AI 共同工作的？為什麼全球的天才開發者都聚集於此？除了高超的編碼秘訣之外，讓我們一起看看他們夢想的未來。

## 為什麼這很重要？

這不僅僅關乎 AI 擅長編碼，更預示著我們工作方式的根本轉變。過去，開發者需要熬夜逐行輸入代碼；而現在，AI 負責起草，人類則轉向判斷方向是否正確以及是否「安全」。

Anthropic 不僅致力於打造「聰明的 AI」，更專注於開發「可靠（reliable）、可解釋（interpretable）且可控（steerable）」的 AI [首頁 \ Anthropic](https://www.anthropic.com/)。

打個比方，這不像是在製造一列只追求速度的失控火車，而是打造一輛煞車可靠且能精準聽從駕駛指令的高性能電動車。這意味著從系統深處開始設計「安全裝置」，以確保我們使用的金融或醫療服務不會突然出現異常行為或提供危險資訊。對於 Anthropic 而言，工程不僅僅是開發功能，更是一項為人類提供安全工具的使命 [工程 \ Anthropic](https://www.anthropic.com/engineering)。

## 輕鬆理解：Anthropic 工程師的「AI 同事」

Anthropic 的開發者絕非孤軍奮戰。他們與自己親手打造的強大 AI——Claude 組成團隊進行協作。讓我們用日常生活中常見的場景來比喻他們獨特的協作方式。

### 1. 24 小時不休息的「資深代碼審查員」
開發者會經歷將自己編寫的代碼交由他人審核的「拉取請求（Pull Request，請求將編寫的代碼合併至現有系統的階段）」過程。此時，Anthropic 工程師會像對待同事一樣使用專用的 Claude 插件（Claude Plugin） [工程 – Claude 插件 | Anthropic](https://claude.com/plugins/engineering)。

**想像一下：** 當你寫完報告準備下班時，一位世界頂尖專家級的秘書出現並仔細指出：「請等一下，第 3 頁的這個數據稍後可能會導致巨大的成本損失，第 5 頁的邏輯出錯機率很高。」當 Claude 收到「請檢查此代碼的錯誤處理和潛在性能問題」的請求時，它能在瞬間瀏覽數千行代碼並找出問題 [工程 – Claude 插件 | Anthropic](https://claude.com/plugins/engineering)。

### 2. 永不遺忘的「天才秘書」（上下文工程）
與 AI 對話時，有時會因為它似乎忘記了之前的內容而感到沮喪吧？為了探討這個問題，Anthropic 在「上下文工程（Context Engineering，優化 AI 一次能記憶和處理的信息量及方式的技術）」上投入了巨大心血 [Anthropic](https://www.anthropic.com/engineering/managed-agents)。

簡單來說，這就像是將一本厚厚的百科全書僅用一張便利貼總結出核心要點（Compaction），或是將必要內容單獨記錄在筆記本上，稍後能準確地再次翻閱（Memory tool）。得益於此，Claude 能夠完美記住並輔助長達數天、數週的複雜軟體專案的全過程，而不會遺漏任何細節 [Anthropic](https://www.anthropic.com/engineering/managed-agents)。

### 3. 自動展現團隊合作的「AI 特遣隊」
Anthropic 使用「多代理安全架（Multi-agent harness）」技術，同時運行多個 AI 代理（Agent，為達成特定目標而能自主判斷並行動的 AI 系統） [Anthropic | LinkedIn](https://www.linkedin.com/company/anthropicresearch)。

這就好比不把所有工作交給一名秘書，而是將設計師秘書、企劃師秘書、開發者秘書組合成一個「團隊」來執行任務。透過這個系統，AI 之間可以互相對話，設計網站畫面，甚至能自主判斷並執行人類需要耗費數天才能完成的複雜開發課題 [Anthropic | LinkedIn](https://www.linkedin.com/company/anthropicresearch)。

## 現狀：AI 改變的工作場所面貌

Anthropic 親自調查了其工作方式因 AI 產生的變化。2025 年 8 月，針對 132 名工程師和研究人員進行問卷調查，並進行了 53 次深度訪談，結果證實像「Claude Code」這樣的工具已經徹底改變了他們的日常生活 [AI 如何改變 Anthropic 的工作方式 \ Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)。現在，開發者已從單純的重複性工作中解脫，專注於更具創造性的設計。

憑藉這些創新的技術實力和工作文化，Anthropic 現已成為全球開發者最嚮往的「夢幻職場」。根據 2025 年的一份報告，OpenAI 和 Google DeepMind 等知名企業的頂級人才正在向 Anthropic 流動 [OpenAI 和 DeepMind 的工程師流向 Anthropic ...](https://fortune.com/2025/06/03/openai-deepmind-anthropic-loosing-engineers-ai-talent-war/)。目前 Anthropic 正在快速成長，在舊金山、倫敦等地有超過 426 個職位正在尋找新人才 [Anthropic 職缺](https://job-boards.greenhouse.io/anthropic?error=true)。

然而，他們不僅僅是在開發功能。Anthropic 聚集了如 Amanda Askell 等提示工程（Prompt Engineering，設計指令以引導 AI 給出最佳答案）專家。他們正在共同進行一項「哲學性工作」，精確磨合 AI 使其不僅僅是變聰明，更能確保其行為不違背人類的倫理與價值觀 [AI 提示工程：深度探討 - YouTube](https://www.youtube.com/watch?v=T9aRN5JkmL8)。

## 未來展望

Claude Opus 4.5 的出現宣告了「自主工程（Autonomous Engineering）」時代的序幕 [矽谷新霸主：Anthropic 的 Claude Opus 4.5 定義了自主工程的極限...](https://markets.financialcontent.com/wral/article/tokenring-2025-12-24-the-new-sovereign-of-silicon-anthropics-claude-opus-45-redefines-the-limits-of-autonomous-engineering)。現在，AI 已經超越了代為編寫指令代碼的水平，正在演變成即使在人類工程師睡覺時也能自主診斷問題並設計軟體的「自主夥伴」。

當然，Anthropic 在此過程中也不會忘記基礎建設（Infrastructure）的重要性：
- **服務網格（Service Mesh）：** 協助眾多 AI 服務互不干擾、流暢對話的交通調度系統。
- **可觀察性（Observability）：** 即時觀察並掌握系統內部狀態，判斷是否有「病灶」的能力。

透過構建這些堅實的基礎系統，他們正在打造一個讓 AI 可以安全、盡情發揮的運動場 [Anthropic 平台軟體工程師 | Accel Job Board](https://jobs.accel.com/companies/anthropic/jobs/73851338-software-engineer-platform)。

未來，我們將生活在一個由 AI 直接設計和審查的代碼所構成的世界。那個世界會有多安全和便利，將取決於 Anthropic 所追求的「可靠且可控的 AI」技術能在人類生活中紮根多深、多正。

---

### AI 的看法 (AI's Take)
Anthropic 的工程並非 AI 奪取人類工作的過程，而是一個美麗的協作過程，旨在幫助人類專注於更高層次的規劃問題解決以及「安全」這一本質價值。Claude Opus 4.5 所展示的成果僅僅是個開始，不久之後，AI 將成為我們身邊最可靠、最聰明，且最重要的是「值得信賴」的同事。你想與什麼樣的 AI 同事一起工作呢？

## 參考資料
1. [工程 \ Anthropic](https://www.anthropic.com/engineering)
2. [Anthropic 工程面試 (2026)](https://www.linkedin.com/pulse/anthropic-engineering-interviews-2026-tryexponent-tpn6c)
3. [Anthropic 職缺](https://job-boards.greenhouse.io/anthropic?error=true)
4. [工程 – Claude 插件 | Anthropic](https://claude.com/plugins/engineering)
5. [工程 \ Anthropic](http://boostcode.org/engineering.html)
6. [AI 提示工程：深度探討 - YouTube](https://www.youtube.com/watch?v=T9aRN5JkmL8)
7. [Anthropic](https://www.anthropic.com/engineering/managed-agents)
8. [Anthropic 課程](https://anthropic.skilljar.com/)
9. [首頁 \ Anthropic](https://www.anthropic.com/)
10. [Anthropic 平台軟體工程師 | Accel Job Board](https://jobs.accel.com/companies/anthropic/jobs/73851338-software-engineer-platform)
11. [Anthropic | LinkedIn](https://www.linkedin.com/company/anthropicresearch)
12. [AI 如何改變 Anthropic 的工作方式 \ Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
13. [來自 Anthropic 的提示工程工作台：真實案例與實用見解 | withLinda.dev](https://withlinda.dev/blog/mastery/prompt-engineering-guide-from-anthropic)
14. [矽谷新霸主：Anthropic 的 Claude Opus 4.5 ...](https://markets.financialcontent.com/wral/article/tokenring-2025-12-24-the-new-sovereign-of-silicon-anthropics-claude-opus-45-redefines-the-limits-of-autonomous-engineering)
15. [Anthropic 發佈最新 AI 模型 Claude Opus 4.5 - CNBC](https://www.cnbc.com/2025/11/24/anthropic-unveils-claude-opus-4point5-its-latest-ai-model.html)
16. [Anthropic 的 Claude 4.5 在 2 小時工程測試中擊敗所有人類...](https://www.businessinsider.com/anthropic-claude-opus-4-5-beats-every-human-engineering-test-2025-11)
17. [Cognizant 採用 Anthropic 的 Claude 以加速企業級 AI 應用...](https://news.cognizant.com/2025-11-04-Cognizant-Adopts-Anthropics-Claude-to-Accelerate-Enterprise-AI-Adoption-at-Scale-and-Deploys-Claude-to-Drive-Internal-AI-Transformation)
18. [OpenAI 和 DeepMind 的工程師流向 Anthropic ...](https://fortune.com/2025/06/03/openai-deepmind-anthropic-loosing-engineers-ai-talent-war/)

## FACT-CHECK SUMMARY
- Claims checked: 16
- Claims verified: 16
- Verdict: PASS