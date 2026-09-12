---
layout: post
title: "AI 幫我寫程式？透過 'Agents on Rails' 基準測試看 AI 的真實實力"
description: "AI 程式編寫代理程式在真實 Ruby on Rails 專案中的表現如何？我們將透過最新的基準測試結果，為您進行輕鬆且清晰的說明。"
summary: "「Agents on Rails」基準測試衡量了 AI 在實際 Ruby on Rails 專案中實現複雜功能的能力，頂尖模型創下了 35% 的成功率，證明了其實戰應用的可能性。"
tags: [AI, 程式設計, Ruby on Rails, Agents on Rails, 軟體開發]
image: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs.jpg
image_alt: "AI 代理程式的數據流在複雜程式碼檔案上方視覺化的景象"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的程式編寫能力正在飛速發展，但距離完美勝任實務中複雜的功能仍有一段距離。不過，35% 這個數字僅僅是一個開始。"
quiz:
  - question: "Agents on Rails 基準測試所使用的實際專案名稱為何？"
    choices: ["Writebook", "RailsApp", "CodeAgent"]
    answer: 0
    explanation: "Agents on Rails 使用一個名為 Writebook 的實際專案來測試 AI 代理程式的效能。"
  - question: "在最近發布的 'Stage 2' 基準測試中，表現最好的模型成功率為百分之多少？"
    choices: ["92%", "35%", "50%"]
    answer: 1
    explanation: "GPT-6 Astra 模型在 Stage 2 功能實現任務中創下了 35% 的成功率。"
  - question: "此基準測試之所以重要的原因為何？"
    choices: ["為了測量 AI 的圖形處理能力", "為了在類似實際工作環境的情況下測量 AI 的程式編寫效能", "為了測試 AI 的寫作能力"]
    answer: 1
    explanation: "此專案的目標是根據實際的 Ruby on Rails 程式碼庫，測量 AI 在解決開發者面臨的實務課題時的表現。"
lang: zh-tw
ref: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs
---

想像一下。早上起床後，您對 AI 助理說：「今天幫我們網站新增會員註冊功能，並檢查相關的安全問題。」在您喝一杯咖啡的時間裡，AI 寫好了複雜的程式碼，自行完成測試後回報：「所有工作已完成。」

這在幾年前還只是科幻電影中的情節，但現在我們離這個未來又更近了一步。那麼，目前的 AI 到底能在多大程度上代替開發者執行實際工作呢？我們將透過 Ruby on Rails（用於網頁應用程式開發的程式框架）基金會與 Evil Martians 最近公開的 **'Agents on Rails'** 基準測試結果，來看看它的真實實力。 [[參考資料: Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report), [參考資料: Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)]

## 這為什麼很重要？

到目前為止，許多 AI 模型都宣稱自己很會寫程式，但實際企業現場的專案遠比想像中複雜且棘手。既有的基準測試大多僅止於測試非常短且單純的程式碼片段。

'Agents on Rails' 之所以重要，是因為它是 **'實戰型測試'**。它直接拿取開發者實際使用的 'Writebook' 專案程式碼，要求 AI 執行修復 Bug、安全檢查、新增功能等實務中會遇到的任務。 [[參考資料: Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report), [參考資料: Agents on Rails benchmark: model picks by cost and score](https://tokenstead.ai/guides/agents-on-rails-first-benchmark-report)] 換句話說，這個結果就像是一張「實務成績單」，告訴我們如果現在將 AI 導入工作環境中，究竟能有多可靠。

## 簡單易懂的解釋

將這個基準測試比喻一下會更容易理解。

簡單來說，如果過去的 AI 效能測量方式像是考「小學生程度的英文單字測驗」，那麼 'Agents on Rails' 就好比是進入真正的英語系國家公司工作，必須像新進員工一樣撰寫報告並進行協作的「實務能力評核」。

AI 代理程式就像剛進公司的新人。在第 1 階段測試中，我們讓它們處理非常短且獨立的工作（尋找 Bug、解決安全問題等）；而在第 2 階段測試中，則是讓它們像真正的開發者一樣執行 **'功能實現的全過程'**。 [[參考資料: Agents on Rails: Stage 2. Can a model ship a feature?](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2), [參考資料: Agents on Rails: We ran 8 models against 21 atomic tasks to ...](https://www.linkedin.com/posts/ruby-on-rails-org_agents-on-rails-we-ran-8-models-against-activity-7493709649016188929-F2nq)]

在最近發布的第 2 階段結果中，表現最亮眼的 'GPT-6 Astra' 模型創下了 **35%** 的成功率。「咦？感覺比想像中低？」您可能會這麼覺得。但請試想，在複雜的實際工作中，AI 能獨自完成 35% 的成果，這意味著如果旁邊有熟練的開發者協助審查與修改，這將能大幅提升工作效率。

## 現況

目前 'Agents on Rails' 正針對 8 個主要的 AI 模型進行嚴格的驗證。 [[參考資料: Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)]

- **頂尖模型的活躍**：在第 1 階段測試中，'Claude Opus 5' 創下了 92% 的驚人成功率。 [[參考資料: Agents on Rails: the first benchmark report | Vuink.com](https://vuink.com/post/eholbaenvyf-d-dbet/2026/8/13/agents-on-rails-the-first-benchmark-report)]
- **多元的選擇**：'Kimi K3' 以頂尖模型一半的成本發揮了 90% 的效能，證明了其效率；而 'GPT-5.6 Luna' 則以最低的成本受到了關注。 [[參考資料: Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)]
- **侷限性**：然而，正如需要實現完整功能的第 2 階段測試所顯示的那樣，AI 在完全理解實務專案的全貌並毫無錯誤地完成程式碼方面，仍有待加強。

## 未來發展如何？

未來的 AI 程式編寫代理程式將會變得更加聰明。Rails 基金會不僅會評估模型的成功率，還會綜合考量它們對最新開發模式的反映程度，以及 Token 成本（AI 處理數據時產生的單位成本）是否合理等，並持續進行演化。 [[參考資料: Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)]

各位讀者需要注意的不僅僅是分數，更是 **'趨勢'**。從單純懂得語法的 AI，現在已經邁入能直接實現創造實際商業價值功能的階段。或許不久之後，當成功率從 35% 提升至 50%、70% 的那一刻，我們的工作方式將會徹底改變。

## MindTickleBytes 的 AI 記者觀點
本次基準測試證明了 AI 已不僅僅是程式編寫的「助手」，更在成長為「同事」。雖然 35% 這個數字並不完美，但 AI 已經開始理解並執行實際開發者的工作流程，這點比任何結果都更令人充滿希望。

## 參考資料

1. [Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report)
2. [Agents on Rails: The LLM Benchmark Project](https://rubyonrails.org/2026/8/12/llm-benchmarking-project)
3. [Agents on Rails: Stage 2. Can a model ship a feature?](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2)
4. [Agents on Rails: Grok 4.6, GLM 5.3, Gemini 3.7 Flash, and Opus 4.8](https://rubyonrails.org/2026/8/17/agents-on-rails-grok-4-6-glm-5-3-gemini-3-7-flash-and-opus-4-8)
5. [Agents on Rails: the first benchmark report | Vuink.com](https://vuink.com/post/eholbaenvyf-d-dbet/2026/8/13/agents-on-rails-the-first-benchmark-report)
6. [Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)
7. [Agents on Rails benchmark: model picks by cost and score](https://tokenstead.ai/guides/agents-on-rails-first-benchmark-report)
8. [Agents on Rails: We ran 8 models against 21 atomic tasks to ...](https://www.linkedin.com/posts/ruby-on-rails-org_agents-on-rails-we-ran-8-models-against-activity-7493709649016188929-F2nq)
9. [What the First Rails Agent Benchmark Tells You, and What It ...](https://www.convective.com/currents/what-the-first-rails-agent-benchmark-tells-you)
10. [Rails team's first "Agents on Rails" benchmark report: how well do models actually know Rails APIs?](https://www.rubyforum.org/t/rails-teams-first-agent-benchmark-report-how-well-do-models-actually-know-rails-apis/631)
11. [Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)