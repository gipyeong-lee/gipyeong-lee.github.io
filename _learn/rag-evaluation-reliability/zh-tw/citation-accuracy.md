---
layout: learn-module
title: 引用準確性與來源追溯
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:citation-accuracy
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/citation-accuracy/
- lang: en
  url: /learn/en/rag-evaluation-reliability/citation-accuracy/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/citation-accuracy/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/citation-accuracy/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/citation-accuracy/
module_id: m6
permalink: /learn/zh-tw/rag-evaluation-reliability/citation-accuracy/
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
id: m6
slug: citation-accuracy
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m5
objectives:
- 理解 RAG 系統中答案如何忠實地反映檢索到的文件內容。
- 學習引用（Citation）準確性的定義和測量方式。
- 利用 Ragas 框架定量評估答案的事實性（Faithfulness）和答案相關性（Answer Relevance）。
- 設計一個驗證模型答案來源追溯性的流程。
worked_examples:
- 範例 1：事實性分數計算。針對問題「A 公司 2025 年的銷售額是多少？」，生成了答案「A 公司 2025 年的銷售額是 100 億。」，並且上下文文件包含「A
  公司在 2025 年錄得 100 億銷售額。」。由於答案的所有資訊都存在於上下文中，因此事實性分數被評估為 1.0（最大值）。
- '範例 2: 識別引用準確度錯誤。針對問題「A公司創立於何年？」，若產生回答「A公司創立於1990年（參見文件1）。」，但文件1中明確指出「A公司創立於1995年」，則此為「事實扭曲」失敗類型，並判斷其引用準確度較低。'
lab:
  title: 使用 Ragas 自動評估答案忠實度實作
  steps:
  - 準備用於評估 RAG 系統的搜尋結果 (Context) 和生成的答案 (Answer) 資料集。
  - 安裝 Ragas 框架並載入答案資料集。
  - 使用 Ragas 的 `Faithfulness` 指標，計算資料集中每個問題-答案對的分數。
  - 單獨提取忠實度低於 0.7 的 30 個答案。
  - 人工審查提取的樣本，並標記為「引文遺漏」、「虛假引文」、「事實扭曲」中的相應失敗類型。
  safety:
  - 評估過程中使用的文件語料庫，請務必事先完成去識別化處理，以避免包含個人資訊或企業機密。
  - 呼叫外部 API 時，請設定費用上限，並固定種子 (Seed) 值以確保重現性，防止產生重複的 API 費用。
  deliverables:
  - 包含評估結果的 Jupyter Notebook 檔案 (.ipynb)
  - 忠實度分數分佈視覺化圖表
  - 包含人工審查記錄的失敗類型分類表
assignment:
  title: RAG 系統可靠性回歸評估報告撰寫
  deliverables:
  - 兩種以上 RAG 設定（例如：搜尋 Top-k 值變更）的忠實度統計比較結果
  - 30 個樣本的人工審查對照表
  - 提高系統引文準確度的改進方案建議書
  rubric:
  - 評估指標的定量產出方式是否準確明確？
  - 搜尋文件與生成答案之間的引文關係是否具有邏輯可追溯性？
  - 失敗類型分類是否與人工審查資料一致，並提供合理的依據？
quiz:
- question: 關於 Ragas 框架的「忠實度 (Faithfulness)」指標，下列敘述何者正確？
  choices:
  - 評估答案是否與問題相關。
  - 衡量答案的所有資訊是否都存在於提供的上下文文件中。
  - 評估答案的語法準確性。
  - 衡量答案是否包含外部知識庫的所有資訊。
  answer_index: 1
  explanation: 忠實度是衡量生成的答案主張是否基於檢索到的上下文的指標。
- question: 在引文準確度評估中，屬於「事實扭曲」失敗類型的情況為何？
  choices:
  - 在答案中包含了搜尋文件中沒有的內容
  - 遺漏了引文標記
  - 引文標記正確，但錯誤地解釋了原文的事實關係進行敘述
  - 答案完全偏離了問題的意圖
  answer_index: 2
  explanation: 事實扭曲是指即使引用了來源文件，卻以錯誤的方式摘要或修改原文資訊而生成的情況。
completion_criteria:
- 透過 Jupyter Notebook 完成自動化評估指標產出
- 提交至少 30 個答案樣本的人工審查及失敗類型分類記錄
- 撰寫包含評估結果和改進方案的最終報告
source_ids:
- S4
---

## RAG 系統的引用與事實性評估

RAG（Retrieval Augmented Generation）系統利用外部知識庫來降低 LLM 的幻覺（Hallucination）風險，但驗證生成的答案是否準確引用了檢索到的文件是必不可少的過程 [S4]。

### 1. 主要評估指標
* **事實性 (Faithfulness):** 測量生成的答案是否源於提供的檢索上下文（Context）。答案的所有主張都應基於檢索到的文件，如果僅憑外部知識或模型的預訓練知識回答，則分數會較低 [S4]。
* **答案相關性 (Answer Relevance):** 評估答案與給定問題的直接相關程度。這用於識別即使檢索到的資訊足夠，答案卻與問題意圖不符的情況。

### 2. 引用準確性驗證流程
引用準確性是識別答案中特定句子引用了檢索上下文中哪一部分，並確認其是否與原始文本的事實一致的過程。自動化評估框架 Ragas 提供指標，即使沒有參考數據（Ground Truth）也能評估事實性 [S4]。

### 3. 失敗類型分類
- **引用缺失:** 答案的事實關係存在於檢索文件中，但未標示引用。
- **虛假引用:** 標示引用了檢索文件中不存在的內容。
- **事實扭曲:** 引用標示正確，但錯誤地解釋了原文的意義而生成。
