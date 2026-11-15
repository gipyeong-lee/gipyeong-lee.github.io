---
layout: post
title: "AI 能一次做出複雜決策？Perplexity 決策模型「Decider v1.3」的祕密"
description: "帶您輕鬆了解 Perplexity 所發布的開權重多模態決策模型「Decider v1.3」的效能、分類與擷取能力，以及商業應用方式。"
summary: "Perplexity 推出了能一次執行分類、路由、評分與資訊擷取的開權重多模態決策模型「Decider v1.3」與「Decider Flash v1.3」。"
tags: [Perplexity, Decider, AI 模型, 多模態, 開權重]
image: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases.jpg
image_alt: "表現人工智慧決策模型的概念圖之插圖，能一目了然地分析與分類各種資料和文件"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Decider v1.3 展現了 AI 正從單純的對話夥伴，演進為能直接執行企業複雜決策與資料分類任務的強大實務夥伴。"
quiz:
  - question: "Perplexity 這次發布的決策模型 v1.3 系列之特徵，何者正確？"
    choices: ["只能處理文字", "一次執行分類、評分與資訊擷取", "必然會在途中裁切輸入資料 (Truncation)"]
    answer: 1
    explanation: "Decider v1.3 是一個多模態決策模型，能根據文字、結構化 JSON 與圖片，以單一路徑處理分類、路由、評分與資訊擷取。"
  - question: "Decider v1.3 在 63 個查詢分類任務中記錄的平均準確度為何？"
    choices: ["81.2%", "91.6%", "99.4%"]
    answer: 1
    explanation: "以較大模型為基準，在 63 個查詢分類任務中記錄了 91.6% 的平均準確度，證明了其效能超越自家生產環境的分類器。"
  - question: "作為 Decider v1.3 新增的核心功能之一，直接在文字中指認出特定資訊的能力是什麼？"
    choices: ["定位 (Locate)", "翻譯 (Translate)", "編譯 (Compile)"]
    answer: 0
    explanation: "Decider v1.3 透過新導入的「定位 (Locate)」功能，具備了直接從文字中擷取特定資訊的能力。"
lang: zh-tw
ref: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases
---

試想一下，在一個每天湧入數千筆客戶諮詢、文件與圖片的大型客服中心裡，承辦人員每次都要分類這到底是退款請求、一般諮詢還是緊急客訴，並進行評分，搞得精疲力竭。然而，現在出現了一個能在短短幾秒鐘內，比人類更準確地完成這項複雜且枯燥判斷工作的 AI。這就是 [Perplexity（基於 AI 的搜尋與對話平台）](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks) 所發布的開權重（Open-weight，任何人皆可檢視內部結構並加以利用的公開權重模型）多模態（Multimodal，能同時理解文字、圖片、聲音等多種形式資料的技術）決策模型**「Decider v1.3」**與**「Decider Flash v1.3」** [Source 2, Source 7]。

在這篇文章中，我們將逐步探討為什麼 Perplexity 推出的這款全新決策 AI 會備受關注，以及它將為我們的日常生活與商業帶來什麼樣的改變。

---

## 為什麼這很重要？

企業將 AI 導入商業應用時最頭痛的痛點，就是「判斷與決策」。比方說，這就像在巨大的工廠裡，為了逐一用手工檢驗無數零件是否不良而停工等待。過去，為了回答「這封電子郵件是垃圾郵件嗎？」、「這位客戶提交的文件符合規定嗎？」、「這則商品評論是正面還是負面？」這類問題，必須將各種不同的程式進行複雜的串聯。

然而，[Perplexity 的 Decider v1.3](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks) 在 63 個查詢分類（Query-classification，將使用者的提問或請求意圖按類型劃分的任務）任務中創下了 **91.6% 的平均準確度**，證明其效能比自家原有的生產環境分類器高出 6.54 個百分點 [Source 2]。 

它不僅僅是讀取文字並回答，還能以單一路徑同時處理**分類（Classification）、評分（Scoring）與資訊擷取（Extraction）** [Source 4, Source 6]，這讓企業能夠以更低的成本建構出快速且準確的自動化系統。

---

## 輕鬆理解：Decider v1.3 是如何工作的？

簡單來說，Decider v1.3 可以比擬為**「超高速法官」**或**「大型圖書館的天才圖書管理員」**。 

這個模型可以同時接收文字、結構化 JSON（用於儲存與交換資料的輕量級文字格式）、甚至是圖片等多種形式的資料 [Source 6]。並且，它會根據是非題、使用者預先設定的自訂選項、或是排序好的評分規條（Rubric，評估標準表）進行徹底審查，最後輸出機率值與打字完成的正解 [Source 6]。

### 用比喻來看核心功能
- **X 光安檢門**：就像機場安檢掃描行李一樣，Decider v1.3 能在龐大資料中毫無誤差地挑出違規事項或特定項目。
- **全新的「定位 (Locate)」功能**：新增了直接在文字中指認特定資訊的能力 [Source 1, Source 7]。這就像是在巨大的百科全書中，精準地用美工刀將寫有特定單字的頁面完美切下來尋找的技術一樣。

這所有過程都在單一模型內部有機地發生，這正是它與現有 AI 最大不同之處 [Source 4, Source 6]。

---

## 現狀：目前進展到哪裡？

[Perplexity Decider v1.3](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks) 是承襲前一代版本 v1、v1.1、v1.2 以及 Flash v1.2 優良血統而誕生的最新模型 [Source 2]。目前已知的技術特徵與規格如下：

1. **強大的多模態處理**：不僅是文字，連圖片與結構化資料都能同時進行評估 [Source 6]。
2. **龐大的上下文視窗**：提供高達 **256K（約 25 萬 6 千個）**的巨大上下文視窗（Context window，AI 一次能記憶與處理的資訊量），能夠整本書塞進去進行分析 [Source 6]。
3. **輸入資料的無損保留**：在訓練過程中使用了最長 **30,720 個 Token（權杖，AI 讀取與處理句子的基本單位）**長度的序列，並堅持絕不中途裁切（Truncation）輸入資料的原則 [Source 9]。
4. **靈活的提問限制**：提問數量沒有固定限制，在允許的長度極限內，可以一次拋出無數個問題 [Source 9]。

開發者與企業可以透過 OpenRouter 或 Vercel AI Gateway 等管道，輕鬆測試此模型並以 API 形式呼叫使用 [Source 6, Source 8]。

---

## 未來發展如何？

隨著 [Perplexity](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks) 以開權重模型形式全面開源 [Decider v1.3 與 Decider Flash v1.3](https://lapaasvoice.com/perplexity-open-sources-decider-v1.3-and-decider-flash-v1-3-with-new-locate-feature/) [Source 2, Source 7]，預計未來會有無數企業與開發者將這個「智慧型判斷引擎」移植到各自的服務中。

在客服中心自動分類系統、大規模合約與法律文件審查、即時內容審核等「正確判斷」決定商業成敗的領域中，Decider v1.3 預計將穩坐核心基礎設施的地位。AI 不僅止於口條流利，正以極快的速度蛻變為真正的「高效工作幕僚」。

---

## AI 的視角

MindTickleBytes AI 記者視角：AI 的發展已不只是寫文章寫得好，更正朝著做出「正確判斷」的精密性演進。Decider v1.3 證明了 AI 不再只是個愛聊天的機器，而是能成為陪伴企業最嚴苛決策者身邊、值得信賴的得力助手。

---

## 參考資料

1. [Perplexity Decider v1.3: Training, eval, and use cases](https://www.perplexity.ai/hub/blog/perplexity-decider)
2. [Perplexity Ships Decider v1.3 Classifier, 91.6% on 63 Tasks](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)
3. [Perplexity's Decider v1.3 lets one model · 21 HN comments | Zeli](https://zeli.app/story/50488464)
4. [Decider v1.3: Release, Decision Index Score, Performance ...](https://artificialanalysis.ai/decision-models/pplx-decider-v1-3)
5. [Decider V1.3 API, Pricing & Playground | Vercel AI Gateway](https://vercel.com/ai-gateway/models/pplx-decider-v1.3)
6. [Perplexity Open-Sources Decider v1.3 and Decider Flash v1.3 ...](https://lapaasvoice.com/perplexity-open-sources-decider-v1-3-and-decider-flash-v1-3-with-new-locate-feature/)
7. [DeciderV1.3(free) - API Pricing & Providers | OpenRouter](https://openrouter.ai/perplexity/pplx-decider-v1.3:free)
8. [perplexity-ai/pplx-decider-v1.3 · Hugging Face](https://huggingface.co/perplexity-ai/pplx-decider-v1.3)
9. [Perplexity Decider v1.2 27B Benchmarks & Pricing | BenchLM.ai](https://benchlm.ai/models/pplx-decider-v1.2)
10. [How To Use Decision Models for Evals – Hamel’s Blog](https://hamel.dev/blog/posts/decision-model-evals/)
11. [Perplexity Decider V1.2 API Pricing & Benchmarks | LMSpeed](https://lmspeed.net/model/pplx-decider-v1.2)