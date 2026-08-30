---
layout: learn-module
title: 理解 RAG 架構
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:intro-rag-architecture
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/intro-rag-architecture/
- lang: en
  url: /learn/en/rag-evaluation-reliability/intro-rag-architecture/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/intro-rag-architecture/
module_id: m1
permalink: /learn/zh-tw/rag-evaluation-reliability/intro-rag-architecture/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: f439c689d3754cecbf386ffcc0c2bd7c
translation_run_id: 8cdc0b34e16948eaa3553f31f19ca27b
primary_category: ai-software
topics:
- retrieval-augmented-generation
- rag-evaluation
- information-retrieval
- llm-reliability
course_type: academic
published_at: '2026-08-30T15:42:37.390479+09:00'
id: m1
slug: intro-rag-architecture
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- 理解 RAG (Retrieval-Augmented Generation) 架構的核心組成部分。
- 識別大型語言模型 (LLM) 的知識限制以及基於檢索增強的必要性。
- 能夠解釋檢索-生成管道的結構流程。
worked_examples:
- '案例 1: 傳統 LLM 方式 - 當詢問「告訴我今天的新聞」時，模型可能無法識別訓練數據之後的事件，從而有產生錯誤資訊的風險。'
- '案例 2: RAG 方式 - 當詢問「告訴我今天的新聞」時，1) 檢索器 (Retriever) 透過外部搜尋引擎或即時新聞 API 收集相關報導，2) 並將其作為上下文
  (context) 包含在內傳遞給 LLM，從而生成準確的最新資訊回應。'
lab:
  title: RAG 架構流程視覺化與分析
  steps:
  - 打開 Jupyter Notebook 並繪製 RAG 基本管道的 3 階段（輸入、檢索、生成）結構圖。
  - 從開放授權文件語料庫中提取 5 個短文本，建立資料集樣本。
  - 編寫一個簡單的關鍵字匹配檢索器 (Retriever) 函數，使其返回符合問題的文件。
  - 編寫程式碼實現增強階段，將檢索到的文件注入提示模板。
  safety:
  - 絕不將實際個人資訊或機密文件用作語料庫數據。
  - 使用API時，請檢查呼叫次數限制（Rate Limit），並在測試程式碼中設定種子（seed）值以確保再現性。
  deliverables:
  - RAG 架構圖（包含在 Notebook 單元格內）
  - 簡易關鍵字搜尋器實作程式碼
  - 文件注入型提示生成結果
assignment:
  title: RAG 資訊檢索管道分析報告
  deliverables:
  - 說明所實作 RAG 管道運作原理的 Notebook
  - 說明搜尋器判斷文件相關性時可能發生的潛在失敗案例 3種
  rubric:
  - RAG 的 3個階段（檢索、增強、生成）是否被準確區分並說明？
  - 在檢索階段，關於檢索到不相關文件的可能性分析是否合理？
  - 是否遵循非公開數據安全指南進行實作？
quiz:
- question: RAG 相較於 LLM 學習方式的主要優點是什麼？
  choices:
  - 可以減少 LLM 的參數大小。
  - 可以讓模型的知識保持最新狀態並提供依據。
  - 加速模型的學習速度。
  - 對所有問題生成 100% 事實的答案。
  answer_index: 1
  explanation: RAG 透過參考外部文件，能夠反映最新資訊，並且可以從文件中找到生成答案的依據，因此可靠性較高。
- question: 檢索器 (Retriever) 的正確角色是什麼？
  choices:
  - 負責生成答案。
  - 負責重新訓練學習數據。
  - 檢索與問題相關的外部文件片段。
  - 管理使用者介面。
  answer_index: 2
  explanation: 檢索器負責從外部數據源中查找與使用者問題語義相似或相關性高的文件。
completion_criteria:
- 能夠說明 RAG 架構的組成要素。
- 確認實作的 RAG 管道程式碼正常運作，能夠檢索和增強相關文件。
- 在分析報告中說明 RAG 管道的局限性與改進方向。
source_ids:
- S1
- S2
---

## RAG (Retrieval-Augmented Generation) 架構概述

最新自然語言處理 (NLP) 和深度學習模型透過學習海量文本數據展現卓越性能，但對於模型訓練時未包含的最新資訊或特定領域的非公開數據，則會出現幻覺 (hallucination) 或不了解資訊的限制 [S1]。

### 透過檢索克服 LLM 的限制
RAG 是一種方法，它不是讓模型將所有知識記憶在參數 (parameter) 內部，而是在「適當的時機 (just-in-time)」檢索與問題相關的外部可信文件，並將其作為生成階段的輸入 [S2]。

### 核心組成部分
1. **檢索器 (Retriever)**：接收使用者的查詢 (query)，並從向量資料庫等中識別出相關性高的文件片段 (chunk)。
2. **增強 (Augmentation)**：將檢索到的文件與原始問題組合，建構要傳遞給 LLM 的提示 (prompt)。
3. **生成器 (Generator)**：基於增強的資訊生成事實基礎的響應。

這種結構有助於保持模型的知識更新，並使生成答案的依據可追溯，從而確保可靠性。
