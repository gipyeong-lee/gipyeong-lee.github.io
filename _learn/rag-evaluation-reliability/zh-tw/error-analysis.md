---
layout: learn-module
title: 失敗類型分類與錯誤分析
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:error-analysis
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/error-analysis/
- lang: en
  url: /learn/en/rag-evaluation-reliability/error-analysis/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/error-analysis/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/error-analysis/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/error-analysis/
module_id: m8
permalink: /learn/zh-tw/rag-evaluation-reliability/error-analysis/
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
id: m8
slug: error-analysis
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m7
objectives:
- 能夠識別和分類 RAG 系統中發生的失敗類型。
- 能夠區分和分析檢索（Retrieval）階段和生成（Generation）階段的錯誤。
- 能夠利用 Ragas 框架的指標連接自動評估和人工審查結果。
- 能夠基於錯誤分析數據，為 RAG 管道的效能改進提出方案。
worked_examples:
- 範例 1：對於問題「模型 A 的發布日期是什麼？」檢索器檢索到「模型 B 的規格」文件。這被歸類為「檢索失敗」，解決方案可能是調整嵌入模型或優化檢索查詢。
- 範例 2：對於問題「請解釋 X」，檢索器檢索到關於 X 的準確文件，但 LLM 回答了文件中沒有的資訊。這被歸類為「生成失敗（忠實度不足）」，必須透過提示工程（prompt
  engineering）來加強「僅使用提供的上下文」的約束。
lab:
  title: 收集失敗數據集與錯誤分析
  steps:
  - 儲存 RAG 系統的答案和檢索到的上下文（context），針對至少 50 個問題。
  - 針對每個項目，使用 Ragas 測量檢索相關性（Context Precision）和生成忠實度（Faithfulness）。
  - 提取指標分數最低的 20% 問題-答案對。
  - 為提取的樣本創建分類表，劃分為「檢索錯誤」、「生成錯誤」或「邏輯錯誤」之一。
  safety:
  - 絕不將個人資訊或私有數據包含在評估程式碼中。
  - 監控評估過程中使用的 API 呼叫次數和費用，以符合預算。
  - 在本地環境中執行資料分析，以防止資訊洩露。
  deliverables:
  - 已完成分類的錯誤分析 CSV 檔案
  - 搜尋和生成品質指標可視化的 Jupyter Notebook
assignment:
  title: RAG 錯誤分類與改進報告撰寫
  deliverables:
  - 錯誤分析結果摘要的 2 頁報告
  - 針對分類的失敗類型提出應對策略（搜尋優化或提示改進）建議
  rubric:
  - 失敗類型分類的準確性和合理性
  - 定量指標與人工審查結果之間的相關性分析能力
  - 改進策略的邏輯合理性
quiz:
- question: 在 RAG 系統中，當搜尋模組檢索到不相關的上下文時，會發生哪種失敗？
  choices:
  - 生成失敗
  - 搜尋失敗
  - 資料庫連接錯誤
  - 認證失敗
  answer_index: 1
  explanation: 搜尋模組負責識別與問題相關的文件，因此檢索到不相關的上下文是搜尋階段的失敗 [S3]。
- question: Ragas 框架的最大特點是什麼？
  choices:
  - 必須需要大量的人類註釋資料。
  - 可以進行無參考（Reference-free）評估。
  - 只能評估 LLM 生成品質。
  - 只能應用於即時串流系統。
  answer_index: 1
  explanation: Ragas 是一個無參考評估框架，即使沒有真實數據（ground truth），也能評估搜尋和生成品質 [S3]。
completion_criteria:
- 提交包含失敗類型的錯誤分類表
- 完成使用 Ragas 指標進行搜尋和生成品質的定量分析
- 撰寫並審查基於錯誤分析的管道改進建議書
source_ids:
- S3
---

## RAG 系統的錯誤分析概述

RAG（Retrieval Augmented Generation）架構由檢索模組和基於 LLM 的生成模組組成 [S3]。評估系統效能時，重要的是要將這兩個階段分開分析。錯誤主要分為檢索階段的問題和生成階段的問題。

### 1. 失敗類型分類
- **檢索失敗 (Retrieval Failure):** 檢索到不相關或不聚焦的上下文時 [S3]。
- **生成失敗 (Generation Failure):** LLM 無法忠實利用提供的上下文（Faithfulness）或生成與問題無關的答案時 [S3]。

### 2. 自動評估與人工審查的互補
像 Ragas 這樣的無參考（Reference-free）框架，無需人工註釋（ground truth）即可評估檢索和生成品質 [S3]。然而，僅憑自動評估指標，難以完全捕捉系統細微的幻覺（hallucination）或複雜的邏輯錯誤。因此，應通過量化自動指標提取優先級高的失敗樣本，並結合人工審查（Human Review）來確定實際原因。
