---
layout: learn-module
title: 自動評估框架 (Ragas) 應用
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:automated-eval-framework
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/automated-eval-framework/
- lang: en
  url: /learn/en/rag-evaluation-reliability/automated-eval-framework/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/automated-eval-framework/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/automated-eval-framework/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/automated-eval-framework/
module_id: m7
permalink: /learn/zh-tw/rag-evaluation-reliability/automated-eval-framework/
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
id: m7
slug: automated-eval-framework
phase_id: p2
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- 理解 RAG 管道的核心評估維度（檢索和生成質量）。
- 學習使用 Ragas 框架進行無參考（reference-free）的 RAG 性能自動評估方法。
- 通過定量指標分析並緩解幻覺（hallucination）風險。
worked_examples:
- 案例 1：Context Relevance 計算。Ragas 利用 LLM 從檢索到的上下文（Context）中提取回答問題實際所需的句子，並通過必要句子佔總上下文的比例來計算分數。
- 案例 2：Faithfulness 評估。由 LLM 判斷生成回答中的每個主張是否得到檢索到的上下文支持。不被支持的主張越多，幻覺分數就越高。
lab:
  title: 利用 Ragas 進行 RAG 性能定量評估實作
  steps:
  - 準備評估數據集（問題、檢索到的上下文、生成的回答）。
  - 在 Python 環境中安裝 `ragas` 庫。
  - 將評估數據集轉換為 `ragas` 的 Dataset 對象。
  - 調用 Ragas 的 `evaluate` 函數來計算 Context Relevance、Faithfulness 等指標。
  - 將結果視覺化並分析分數較低的查詢。
  safety:
  - 確認評估所用的文檔語料庫中不包含個人隱私或非公開數據。
  - 為避免 API 使用成本，測試時請積極使用本地模型或快取。
  - 自動評估結果僅為可靠性的輔助指標，實際模型品質確認應與人工抽樣審查及交叉驗證並行。
  deliverables:
  - 包含指標分數的評估結果資料框（Dataframe）
  - 低分查詢類型分析日誌
assignment:
  title: RAG 管道性能比較報告
  deliverables:
  - 兩種具有不同檢索設置（k值、嵌入模型等）的 RAG 管道的 Ragas 評估結果
  - 兩種設置之間的性能差異分析報告
  rubric:
  - Ragas 指標（Context Relevance、Faithfulness 等）是否正確實現？
  - 評估結果是否進行了定量比較並包含了邏輯解釋？
  - 是否至少分類了 3 種以上的幻覺類型並提出了改進方案？
quiz:
- question: Ragas 框架最大的特徵是什麼？
  choices:
  - 必須要有人工標準答案數據集
  - 能夠無需參考(reference-free)即可評估 RAG 管道
  - 僅評估檢索階段，不評估生成階段
  - 必須至少需要 10 個 GPU
  answer_index: 1
  explanation: Ragas 是一個利用 LLM 在沒有標準答案資料集的情況下自動評估檢索和生成品質的框架 [S3, S4]。
- question: Ragas 中測量的「Faithfulness」指標的定義是什麼？
  choices:
  - 檢索到的上下文與問題的相關程度為何？
  - 問題是否存在於文檔語料庫中？
  - 生成的答案是否基於檢索到的上下文？
  - 提問者對 LLM 的回答有多信任？
  answer_index: 2
  explanation: Faithfulness 是一項指標，用於衡量生成的答案在多大程度上忠實地基於提供的檢索上下文（防止幻覺）[S4]。
completion_criteria:
- 使用 Ragas 函式庫成功計算至少 10 個查詢的 4 種以上指標
- 實踐筆記本定期提交到 Git 儲存庫
- 效能比較報告包含至少 3 個錯誤分類案例
source_ids:
- S3
- S4
---

## RAG 評估的挑戰與 Ragas

RAG 系統由檢索模塊和基於 LLM 的生成模塊組成 [S3, S4]。評估這種結構是一項具有挑戰性的任務，因為需要同時考量檢索系統識別相關上下文（context）的程度、LLM 利用所提供上下文的忠實度（faithfulness），以及回答的質量 [S4]。

傳統的評估方式依賴於人工編寫標準答案（ground truth）並進行比較，但這不僅成本高昂且耗時，不適合快速反覆運算週期 [S3, S4]。

### Ragas 框架
Ragas（Retrieval Augmented Generation Assessment）是一個無需標準答案數據集即可評估 RAG 管道的框架 [S3, S4]。Ragas 會自動評估以下核心維度：

1. **檢索質量（Retrieval Quality）：** 測量檢索到的上下文與問題的相關性（Context Relevance），以及是否包含所有必要信息（Context Recall）。
2. **生成質量（Generation Quality）：** 測量生成的回答是否基於檢索到的上下文（Faithfulness），以及與問題的相關性（Answer Relevance）。

這些指標利用 LLM 作為「評委（judge）」，實現了無需參考數據的評估，並有助於縮短 RAG 開發週期 [S3, S4]。
