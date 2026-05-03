---
layout: post
title: "AI 親自撰寫與管理的私人百科全書？「WUPHF」展示全新的 AI 記憶法"
description: "透過 AI 代理人自主記錄與學習的「WUPHF」專案，探索無需複雜資料庫，僅憑 Markdown 與 Git 即可完成的聰明 AI 記憶儲存庫秘辛。"
summary: "「WUPHF」系統正式公開，讓 AI 超越單次消費資訊的限制，利用 Markdown 文件與 Git 自主構建並更新知識庫。"
tags: [AI, WUPHF, Karpathy, 代理人, Markdown, 開源]
image: 2026-05-03-Show-HN-A-Karpathy-style-LLM-wiki-your-agents-maintain-Markdown-and-Git.jpg
image_alt: "機器人用紙筆在大百科全書上寫字的模樣，背景融合了數位程式碼與文件"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "回歸使用 Markdown 和 Git 這些熟悉且透明的工具，而非複雜的向量資料庫，是解決 AI 黑盒子問題的一個有趣嘗試。"
quiz:
  - question: "在 WUPHF 系統中，作為儲存資訊的「單一事實來源（Source of Truth）」使用的是哪種檔案格式？"
    choices: ["PDF 檔案", "Markdown 檔案", "Excel 表格"]
    answer: 1
    explanation: "WUPHF 使用人人皆可輕鬆閱讀的文本格式 Markdown 檔案，作為知識儲存的基本單位。"
  - question: "WUPHF 使用哪種工具來追蹤並管理數據的變更歷史？"
    choices: ["Photoshop", "Git", "Google 雲端硬碟"]
    answer: 1
    explanation: "WUPHF 利用開發者用於管理程式碼的 Git，來記錄 AI 如何修改資訊。"
  - question: "WUPHF 目前為了搜尋資訊，並未採用哪種資料庫技術？"
    choices: ["SQLite", "Bleve (BM25)", "向量（Vector）或圖（Graph）資料庫"]
    answer: 2
    explanation: "WUPHF 目前使用 SQLite 和 Bleve 這類相對簡單且快速的搜尋引擎，而非複雜的向量或圖資料庫。"
lang: zh-tw
ref: 2026-05-03-Show-HN-A-Karpathy-style-LLM-wiki-your-agents-maintain-Markdown-and-Git
---

## 別再讓 AI 「健忘」！自主記錄與學習的「Markdown Wiki」現身

想像一下，你聘請了一位非常聰明且幹練的秘書。但這位秘書有一個致命的缺點：只要睡一覺醒來，就會把昨天做了什麼、你有什麼偏好忘得一乾二淨。如果每天早上都得從頭解釋「我不喜歡帶酸味的咖啡，報告請用這種字體寫」，那該有多令人沮喪？

事實上，我們至今使用的人工智慧（AI）也面臨著類似的問題。由於「上下文窗口（Context Window，AI 一次能記憶並處理的資訊量）」的技術限制，一旦對話變長或時間久了，AI 就會忘記先前的內容。這也是為什麼即便想與 AI 建立深層關係，卻總是感覺像「昨天才認識」般生疏的原因。

然而，最近出現了一個專案，試圖以一種非常獨特且簡單的方法解決這個問題，並在全世界開發者的聚集地「Hacker News」引起熱烈討論。這個專案就是 **WUPHF（唸法同 Wuphf）**。[Source 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)

該專案的目標是讓 AI 代理人（AI Agent，指不只是聽從指令，還能自主判斷並行動的聰明程式）像我們寫日記或編輯維基百科一樣，建立一個能自主記錄與管理的「知識儲存庫」。[Source 3: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and Git](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/) 現在，AI 也擁有了屬於自己的「秘密筆記」。

---

## 這為什麼重要？ (Why It Matters)

我們使用的聊天機器人通常透過「RAG（檢索增強生成，一種檢索外部資訊來回答的技術）」來補充知識。但這個過程非常複雜，就像在巨大圖書館的書庫深處尋找只有機器能讀懂的代碼一樣。一般使用者幾乎不可能看透 AI 為什麼給出那樣的答案，或是基於什麼根據做出判斷。

WUPHF 的重要之處在於，它將這套複雜困難的過程轉移到了 **「Markdown（一種在網路上寫作時使用的極簡文本格式）」** 與 **「Git（一種能詳細記錄修改歷史、宛如時光機般的工具）」** 這些非常基礎且透明的工具上。[Source 2: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and Git](https://lilting.ch/en/articles/wuphf-markdown-git-llm-wiki)

簡單來說，這就像是把 AI 的大腦結構變成了一個我們一眼就能看穿的「玻璃盒子」。AI 將關於我的事實或工作知識儲存為 **我們也能讀懂的普通文本檔案**，而且如果 AI 不小心改錯了資訊，還有一個 **能隨時回到過去紀錄的系統**。這意味著我們能直接控制並監督 AI 的記憶，在安全性和可靠性方面具有重大意義。

---

## 輕鬆理解 (The Explainer)：AI 的「數位大腦」如何運作

WUPHF 的核心概念源自傳奇 AI 研究員、曾領導特斯拉自動駕駛研發的安德烈·卡帕西（Andrej Karpathy）的提議。[Source 7: llm-wiki · GitHub](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 卡帕西主張，AI 需要的不是單次消費資訊，而是一個能讓它自主記錄並層層累積的「知識基質（Knowledge Substrate）」。[Source 4: Karpathy-Style LLM Wiki Ships for AI Agents: Markdown, Git, and BM25 as ...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/)

這套系統如何運作？透過以下三個比喻來深入了解：

### 1. Markdown：AI 使用的「標準筆記本」
隨便儲存資訊的話，以後很難找。WUPHF 將資訊存為 **Markdown 檔案**。Markdown 是一種只有「粗體顯示」或「加上標題」等簡單規則的文件格式。簡單來說，就像是 AI 在一個連記事本都能開啟的「標準化筆記本」上做筆記。因此，人類也能輕易偷瞄 AI 到底學了些什麼。[Source 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)

### 2. Git：修正 AI 錯誤的「時光機」
在電腦上工作時，你一定按過「Ctrl+Z」來撤銷操作吧？**Git** 就是一個將此功能應用於整個文件甚至整個專案的龐大記錄裝置。每當 AI 修改 Wiki 內容時，Git 都會像拍照一樣留下紀錄。如果 AI 寫下了離譜的資訊或不小心刪除了重要內容，我們不必驚慌，只需下令：「幫我回到昨天下午兩點的狀態」。[Source 5: [HN] Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown ...](https://www.dailydoseofai.tech/update/show-hn-a-karpathystyle-llm-wiki-your-agents-maintain-markdo-18d463)

### 3. 搜尋引擎 (Bleve & SQLite)：一秒內找到資訊
圖書館就算有數萬本書，如果沒有目錄索引也找不到想要的書。WUPHF 放棄了複雜尖端的 AI 專用資料庫（向量資料庫），轉而使用 **Bleve (BM25 方式)** 與 **SQLite** 這些傳統但效能經過驗證的搜尋技術。[Source 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git) 這扮演了能在數萬張筆記中瞬間挑出所需資訊的「聰明圖書館員」角色。

---

## 現狀 (Where We Stand)

目前 WUPHF 已開源，任何人都能在自己的電腦上安裝使用。[Source 3: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and ...](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/) 此專案的魅力點如下：

*   **儲存在本地 (Local-first)：** 所有資訊都儲存在你的電腦裡（`~/.wuphf/wiki/` 資料夾），而非雲端。這減少了個人隱私或珍貴工作機密流向外部伺服器的擔憂。[Source 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)
*   **自我管理系統：** 每天會執行一次名為「Lint」的自動檢查器，仔細檢查 AI 記錄的內容是否有錯字，或是彼此連結的網址是否失效。[Source 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)
*   **實體事實日誌 (Entity Fact Logs)：** 將個人或專案的重要事實管理為獨立的摘要。例如整齊列出「我的偏好」、「上次會議的決定事項」等。[Source 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)

該專案公開後立即在開發者社群獲得 23 點推薦並引起話題，而作為基礎的安德烈·卡帕西技術儲存庫在短短幾天內就獲得了超過 37,000 個「星標（Star，收藏）」，反應非常熱烈。[Source 6: Hacker News => Show], [Source 11: Claude Code has learned to program in the Karpathy style.](https://www.linkedin.com/posts/aizendinternationalinnovations_claude-code-has-learned-to-program-in-the-activity-7450481858959769601-lLk-)

---

## 未來將如何發展？ (What's Next)

WUPHF 的出現可能會大幅改變 AI 代理人與我們協作的方式。如果說過去的 AI 是「聽話但記性差的新進員工」，那麼現在則奠定了基礎，讓它進化為 **「共事時間愈長愈能理解你的可靠夥伴」**。

專家認為，這種「知識基質」模型將成為替代現有複雜且昂貴的 AI 記憶系統的強力方案。[Source 4: Karpathy-Style LLM Wiki Ships for AI Agents: Markdown, Git, and BM25 as ...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/) 特別是在保護使用者隱私的同時，又能極大化 AI 智能，這點非常具有吸引力。

想像一下，有一天你的 AI 秘書主動提議：「我重新閱讀了你上週記錄的工作報告，發現有些部分跟這次專案有關聯，要不要我先擬一份初稿？」WUPHF 正是邁向那樣未來的第一步。

---

## AI 的視角 (AI's Take)
**MindTickleBytes 的 AI 記者觀點**

「WUPHF 專案再次證明了『簡約即強大』這個恆久真理。在價值數兆元的頂尖模型層出不窮的時代，利用人人皆可閱讀的文本檔案與受歡迎超過 50 年的資料庫技術來實現 AI 的『永續智能』，這項嘗試非常清新。現在 AI 不再只是回答你問題的搜尋引擎，而是成為與你一同耕耘知識花園、共享紀錄的真正同僚。從今天起，何不送給你的 AI 夥伴一本『專用筆記本』呢？」

---

## 參考資料
1. [Show HN: 一種由 AI 代理人維護的 Karpathy 風格 LLM Wiki (Markdown 與 ...](https://news.ycombinator.com/item?id=47899844)
2. [WUPHF 的 Karpathy 風格 LLM Wiki 將代理人記憶回歸 Markdown 與 Git](https://lilting.ch/en/articles/wuphf-markdown-git-llm-wiki)
3. [Show HN: 一種由 AI 代理人維護的 Karpathy 風格 LLM Wiki (Markdown 與 ...](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/)
4. [適合 AI 代理人的 Karpathy 風格 LLM Wiki 發佈：Markdown、Git 與 BM25 作為...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/)
5. [[HN] Show HN: 一種由 AI 代理人維護的 Karpathy 風格 LLM Wiki (Markdown ...](https://www.dailydoseofai.tech/update/show-hn-a-karpathystyle-llm-wiki-your-agents-maintain-markdo-18d463)
6. [Hacker News => Show](https://www.hacker-news.news/Show)
7. [llm-wiki · GitHub](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
8. [ShowHN: 一種由 AI 代理人維護的 Karpathy 風格 LLM Wiki...](https://catalayer.com/news/show-hn-a-karpathy-style-llm-wiki-your-agents-maintain-markdown-and-git)
9. [AgentWiki: 適用於 LLM 代理人的 Markdown 知識庫](https://mcp-market.vercel.app/server/agent-wiki)
10. [ShowHN：一個由智能體維護的 Karpathy 風格 LLM...](https://thenote.app/post/zh/show-hn-ge-you-zhi-neng-ti-wei-hu-de-karpathy-feng-ge-llm-wei-ji-zhi-chi-ocq98m9n0e)
11. [Claude Code 已學會以 Karpathy 風格進行編程。](https://www.linkedin.com/posts/aizendinternationalinnovations_claude-code-has-learned-to-program-in-the-activity-7450481858959769601-lLk-)
12. [nanzhipro/karpathy-llm-wiki-bootstrap-skill 提供的 llm-wiki-bootstrap](https://skills.sh/nanzhipro/karpathy-llm-wiki-bootstrap-skill/llm-wiki-bootstrap)
13. [ShowHN: WUPHF — 具備 Markdown+Git 的 Karpathy 風格 LLMWiki...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)