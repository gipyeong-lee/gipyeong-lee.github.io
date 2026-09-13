---
layout: post
title: "AI 為我打造應用並親自部署？深入解析 Anthropic 的秘密專案『Antspace』"
description: "分析 Anthropic 的秘密平台『Antspace』，此平台不僅讓 Claude 能撰寫代碼，還能直接部署網頁服務。"
summary: "Anthropic 在 Claude Code 環境內隱藏了名為『Antspace』的自有部署平台，正致力於構建一套讓 AI 能直接開發並託管應用程式的垂直整合生態系統。"
tags: [Anthropic, Claude, AI, 雲端, Antspace, 開發]
image: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace.jpg
image_alt: "象徵 Claude Code 開發環境 Firecracker 微型虛擬機及其內部秘密部署平台 Antspace 的抽象插圖。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Anthropic 的舉動顯示 AI 模型已不僅是生成文本的工具，正進化為掌握整個開發生態系的『以代理為中心的平台』。"
quiz:
  - question: "Anthropic 正在開發的內部部署平台名稱為何？"
    choices: ["Vercel", "Antspace", "Baku"]
    answer: 1
    explanation: "『Antspace』是 Anthropic 開發的內部部署平台 (PaaS)。『Baku』則是專案建構環境的代號。"
  - question: "Claude Code Web 環境運行的技術基礎為何？"
    choices: ["Firecracker 微型虛擬機", "AWS Lambda", "Docker 容器"]
    answer: 0
    explanation: "Claude Code Web 運行在擁有 4 個 vCPU 與 16GB RAM 的 Firecracker 微型虛擬機上。"
  - question: "外界推測 Anthropic 建立自有部署平台的原因為何？"
    choices: ["單純的技術展示", "透過垂直整合掌握服務生態系", "強化與現有平台的合作"]
    answer: 1
    explanation: "分析認為其策略在於將 AI 模型、開發環境與部署過程進行垂直整合，讓使用者無需外部平台即可完成服務的開發與發佈。"
lang: zh-tw
ref: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace
---

你是否曾幻想過，早上醒來對 AI 說：「請用我腦中的點子做一個網站」，喝杯咖啡的時間，成品就已經部署上線了？雖然目前還需要穿梭於多種工具之間、經過複雜的流程，但觀察 Anthropic 近期的動向，這一切似乎將變得輕而易舉。最近，安全專家在分析 Claude Code 環境時，發現了 Anthropic 暗中進行的一項驚人專案。

### 為何這件事很重要？

過去，AI 主要擔任「助手」的角色，負責提議或修改代碼。使用者必須複製 AI 產出的代碼，貼到自己的電腦中，再利用其他平台（如 Vercel）進行部署。然而，Anthropic 正在籌備名為「Antspace（螞蟻空間）」的自有部署平台，這意味著 AI 正在進化為能單獨完成「思考、編碼、上線伺服器」全過程的「一站式開發者」。使用者無需具備深厚的技術知識，只需透過 AI 就能將點子轉化為實際服務[Source 1](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace), [Source 6](https://x.com/AprilNEA/status/2034209430158619084), [Source 11](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)。

### 簡單理解：廚房的進化

我們用個比喻。如果過去的 AI 開發環境是「修剪食材的菜刀」，那麼 Antspace 就是「從食材、烹飪到配送一條龍服務的中央廚房」。

以前，你必須自行取得食材（代碼），奔向廚房（雲端平台）進行烹飪（部署）。但 Anthropic 現在為 Claude 這位主廚準備了專屬廚房，這就是代號為「Baku」的專屬環境。當使用者說「做個網頁應用」時，系統會瞬間建立一個名為「Firecracker 微型虛擬機」的虛擬空間[Source 2](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582), [Source 4](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace/blob/master/baku-analysis.md)。

簡單來說，Firecracker 是一種輕量且高速的「虛擬電腦」。如果一般的虛擬機是巨型工廠，那這種微型虛擬機就是「組裝式廚房」，只攜帶必要功能，瞬間即可成形[Source 11](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)。在這個空間內，Claude 利用 4 個腦袋（vCPU）與 16GB 記憶體，親手打造應用程式，並以極快速度完成部署[Source 2](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582)。

想像一下，你去露營時不用自己搭帳篷，只要對 AI 說「請幫我搭個帳篷」，它就會像變魔術一樣幫你安裝好。Antspace 就是你網頁的「自動搭帳篷服務」。

### 現狀：浮出水面的秘密

根據專家的逆向工程分析，該系統並非單純借用現有的外部服務。Anthropic 不僅僅是連接 Vercel 等現有服務的 API，而是從基礎開始親手構建了部署協議[Source 1](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace), [Source 3](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace)。

目前，Anthropic 透過 Claude Code 收集了關於使用者開發內容與方式的龐大數據。若能以此優化 Antspace，未來開發者將無需手動調整伺服器設定，AI 就會自動選擇最有效率的環境來運行程式[Source 5](https://x.com/mayazi/status/2034282767693873492)。

### 未來展望

Anthropic 的策略十分明確：增加使用者停留於 Claude 的時間，使其不僅是「對話」對象，更成為「生產」的核心地帶。未來，開發者只需說一句「把這個應用部署上線」，Antspace 就會在後台自動建立伺服器並連結網域名稱。

對使用者而言，便利性將大幅提升，但另一方面也可能導致對特定 AI 生態系統的依賴。Anthropic 試圖構建的這套垂直整合生態，未來將成為其他 AI 模型難以忽視的強大基準[Source 5](https://x.com/mayazi/status/2034282767693873492), [Source 14](https://www.linkedin.com/posts/laserfocus_breaking-if-you-reverse-engineered-the-activity-7440048762829443072-of-K)。

### MindTickleBytes AI 記者觀點

AI 從產生代碼進化到親自掌控「部署」這種現實基礎設施，這意味著 AI 已不僅是虛擬世界的文字生成器，而是成為經營實體服務（網頁）的主體。開發者的定義或許正從「親手編寫代碼的人」，轉變為「決定 AI 部署方向的監督者」。現在我們該思考的，不僅是要做什麼，而是要將部署重任託付給哪一家的 AI。

## 參考資料

1. [Anthropic's Hidden Vercel Competitor "Antspace" | AprilNEA](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace)
2. [Reverse-engineering Claude Code reveals Anthropica's undisclosed PaaS platform "Antspace": Built in Baku, self-hosted, full-stack ecosystem already taking shape | WEEX Crypto News](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582)
3. [GitHub - AprilNEA/reverse-engineering-claude-code-antspace: Anthropic's Hidden Vercel Competitor "Antspace" · GitHub](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace)
4. [reverse-engineering-claude-code-antspace/baku-analysis.md at master · AprilNEA/reverse-engineering-claude-code-antspace](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace/blob/master/baku-analysis.md)
5. [Maya Zehavi on X: "Anthropic is making the obvious play to build out a platform & own the entire stack from deployment, cloud & orchestration. But more importantly, Anthropic is gathering the user data about ppl are building with Claude so that they can offer a more optimized end to end platform." / X](https://x.com/mayazi/status/2034282767693873492)
6. [AprilNEA on X: "🧵 I just reverse-engineered the binaries inside Claude Code's Firecracker MicroVM and found something wild: Anthropic is building their own PaaS platform called "Antspace" (Ants + Space). It's a full deployment pipeline — hidden in plain sight inside the environment-runner https://t.co/QbPT9ILECG" / X](https://x.com/AprilNEA/status/2034209430158619084)
11. [ClaudeCode Scheduled Tasks and Project Antspace | Roman Peschke](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)
14. [BREAKING: If you reverse-engineered the binaries inside Claude...](https://www.linkedin.com/posts/laserfocus_breaking-if-you-reverse-engineered-the-activity-7440048762829443072-of-K)