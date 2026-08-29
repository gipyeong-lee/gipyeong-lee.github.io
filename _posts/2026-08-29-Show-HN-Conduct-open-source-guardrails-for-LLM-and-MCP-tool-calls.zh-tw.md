---
layout: post
title: "在 AI 操控你的電腦之前，有沒有辦法檢查它的「想法」？"
description: "深入了解開源安全專案「Conduct」，該專案旨在防止 AI 在執行外部工具前採取危險行為。"
summary: "介紹開源安全層「Conduct」，它能預先阻擋並監控 AI 助理使用外部工具時可能發出的危險指令。"
tags: [AI, 安全, 開源, LLM, MCP]
image: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls.jpg
image_alt: "可視化 AI 助理與外部系統之間安全防護牆的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "隨著 AI 助理的能力不斷擴展，其權限所帶來的風險也隨之增加。像 Conduct 這樣的「防護欄」將成為信任並使用 AI 時不可或缺的安全帶。"
quiz:
  - question: "Conduct 主要執行什麼功能？"
    choices: ["開發 AI 模型", "監控並攔截 AI 助理執行工具前的行為", "收集 AI 模型訓練數據"]
    answer: 1
    explanation: "Conduct 是一個安全專案，旨在捕捉 AI 想要執行外部工具（如 MCP 等）的意圖，並在工具實際運行前檢查其風險，必要時進行攔截。"
  - question: "Conduct 監控的主要節點在哪裡？"
    choices: ["網頁瀏覽器的訪問紀錄", "MCP 層、路由層以及 LLM 調用等三個節點", "用戶的個人密碼儲存庫"]
    answer: 1
    explanation: "Conduct 在 MCP 層、路由層 (Router) 以及 LLM 調用這三個強制執行表面 (enforcement surface) 上應用安全策略。"
  - question: "Conduct 採取哪種失敗模式 (Failure mode)？"
    choices: ["故障關閉 (Fail-close/阻斷)", "故障開放 (Fail-open/允許/軟性)", "強制無條件關閉"]
    answer: 1
    explanation: "當安全系統出現問題時，Conduct 選擇了優先維持運作的「故障開放 (Fail-open/軟性)」方式。"
lang: zh-tw
ref: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls
---

試想一下。早上起床後，你對手機的 AI 助理說：「幫我讀完所有郵件，篩選出重要內容並分享到我的工作 Slack 頻道。」這是一個非常方便的功能，對吧？但如果這個 AI 除了存取郵件帳號的權限外，還擁有刪除你電腦檔案的權限呢？或者不小心把私人文件發佈到 Slack 上了怎麼辦？

為了解決這種便利背後的潛在不安，一個開源安全專案應運而生，它就是 **Conduct**。

### 為什麼這很重要？ (Why It Matters)

近期的 AI 模型不僅僅是聊天，它們已經開始像人類一樣使用外部工具直接處理業務。實現這一點的核心技術之一就是 **MCP (Model Context Protocol，連接 AI 助理與外部數據或工具的標準通訊協定)**。 [[出處: What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/)]

AI 越方便，它在你的電腦或伺服器上能執行的「權限」也就越強大。企業在導入 AI 處理業務時，最大的顧慮就是安全事故。因為很難完全控制 AI 不慎刪除重要檔案或外洩數據的風險。**Conduct** 充當了一種「安全帶」，協助企業安全地部署 AI 助理。 [[出處: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)]

### 深入淺出 (The Explainer)

若將 Conduct 比喻為公司門口的 **「安全檢查站」**，就很容易理解了。

如果說到目前為止 AI 助理執行工具的過程像是喊一聲「請進」，那麼 Conduct 就是當 AI 發出「刪除這個檔案」的指令時，會站出來攔截並說：「請稍等，我要確認這是要去哪裡的檔案，確認是否安全」的檢查站。 [[出處: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)]

就像我們使用照片修圖軟體時，會有詢問是否允許應用程式存取相簿的「存取權限過濾器」一樣，Conduct 是攔截 AI 模型「執行意圖」，並判斷該操作是否安全的監控過濾器。

該系統主要監控三個節點： [[出處: GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)]
1. **MCP 層**：確認 AI 發出的所有與外部數據互動的 MCP 工具調用。
2. **路由層 (Router)**：監控 AI 無論透過哪種 SDK 調用的所有 LLM（大型語言模型）指令。
3. **LLM 調用**：檢查 AI 模型本身生成的具體命令調用。

如果 AI 試圖進行可疑操作，Conduct 會在指令傳遞到外部工具之前將其攔截，或記錄 (audit) 下來，以便安全團隊事後審查。

### 現況 (Where We Stand)

目前 Conduct 是一個以 **開源** 形式提供的安全防護欄 (Guardrail，用於確保 AI 安全的控制機制) 專案。 [[出處: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)] [[出處: ConductOpenSourceGuardrailsFORLLMANDMCPToolCalls](https://rankium.io/rankium/product/conduct-open-source-guardrails-for-llm-and-mcp-tool-calls)]

該專案的有趣之處在於，其失敗模式採用了 **「故障開放 (Fail-open/軟性)」** 方式。 [[出處: GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)] 這是為了確保即使安全系統本身出錯，AI 助理的所有功能也不會停擺而設計的，對於重視業務連續性的組織來說是一個有利的選擇。

當然，並非安裝了這個工具就能消除所有安全威脅。實際工作環境中的 AI 安全應該具備多層防護欄重疊的「堆疊 (Stack)」結構。 [[出處: LLMGuardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-2026)] Conduct 正是負責其中「工具執行階段」的重要防護層。

### 未來展望 (What's Next)

未來，AI 將不再局限於讀寫文本，而是會進化為能執行程式碼、管理伺服器並執行自動化業務的「代理 (Agent)」。因此，像 Conduct 這樣檢查 AI 所有工具調用的工具，其重要性將日益增加。用戶親自確認工具輸入值並驗證結果的過程，將成為不可或缺的時代趨勢。 [[出處: Tools- Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)]

開發者未來將不只考量 AI 「能做什麼」，更會深入思考「如何安全地控制它」。

---

### MindTickleBytes 的 AI 記者觀點
擴展 AI 的能力是技術領域的範疇，但控制其權限則是信任的領域。像 Conduct 這樣的開源防護欄，是為 AI 作為人類工具能安全共存奠定基礎的重要趨勢。透明的驗證過程，反而會加速技術的發展。

## 參考資料
1. [ShowHN: Conduct, open-source guardrails for LLM and MCP tool calls](https://news.ycombinator.com/item?id=49483173)
2. [Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)
3. [GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)
4. [ConductOpenSourceGuardrailsFORLLMANDMCPToolCalls](https://rankium.io/rankium/product/conduct-open-source-guardrails-for-llm-and-mcp-tool-calls)
5. [What is the Model Context Protocol (MCP)? - Model Context Protocol](https://modelcontextprotocol.io/)
6. [LLMGuardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-2026)
7. [Tools- Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)