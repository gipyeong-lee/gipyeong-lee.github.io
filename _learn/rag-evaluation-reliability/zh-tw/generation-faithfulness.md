---
layout: learn-module
title: 證據忠實度評估
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:generation-faithfulness
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/generation-faithfulness/
- lang: en
  url: /learn/en/rag-evaluation-reliability/generation-faithfulness/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/generation-faithfulness/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/generation-faithfulness/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/generation-faithfulness/
module_id: m5
permalink: /learn/zh-tw/rag-evaluation-reliability/generation-faithfulness/
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
id: m5
slug: generation-faithfulness
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- 理解證據忠實度(Faithfulness)的概念，並掌握其在RAG系統中的重要性。
- 利用Ragas框架，定量評估生成的答案是否基於檢索到的上下文(Context)。
- 利用自動化評估指標，分析幻覺(Hallucination)風險。
worked_examples:
- 範例1：若上下文為「蘋果富含維生素C」，而答案為「蘋果富含維生素C，對免疫力有益」，則「對免疫力有益」是上下文中沒有的資訊，因此證據忠實度分數會降低。
- 範例2：若上下文為「我們公司的創立日是2020年5月1日」，而答案為「本公司成立於2020年5月」，則資訊一致，因此具有較高的證據忠實度分數。
lab:
  title: 利用Ragas測量生成答案的證據忠實度
  steps:
  - 準備評估資料集（問題、檢索到的上下文、生成的答案）。
  - 安裝Ragas庫並匯入`Faithfulness`指標。
  - 將準備好的資料集轉換為Ragas的資料結構。
  - 組態基於LLM的評估器，計算資料集的證據忠實度分數。
  - 抽樣分析低分答案，並透過人工審查分析其與檢索到的上下文的差異。
  safety:
  - 不將包含非公開文件或個人資訊的資料集傳輸到外部LLM API。
  - 確認API請求次數限制，並使用快取(Cache)來控制成本。
  - 在人工審查時保持樣本資料的安全性。
  deliverables:
  - 整個資料集的平均證據忠實度分數報告
  - 針對低分答案的分析資料集
  - 自動評估結果與人工審查結果的比較分析
assignment:
  title: RAG管線可靠性評估報告
  deliverables:
  - 包含證據忠實度評估的Jupyter Notebook
  - 錯誤分類及幻覺發生頻率分析報告
  rubric:
  - 證據忠實度指標的實現是否正確？
  - 是否準確分類生成答案中的幻覺案例？
  - 是否確保了自動評估結果與人工審查的定性一致性？
quiz:
- question: 在 RAG 系統中，事實性（Faithfulness）是指什麼？
  choices:
  - 檢索到的上下文與問題的相關程度
  - 生成的答案基於檢索到的上下文資訊的程度
  - LLM 利用預訓練知識的程度
  - 答案與用戶問題準確匹配的程度
  answer_index: 1
  explanation: 事實性是評估生成答案是否依賴於從外部檢索到的上下文中的事實的指標。
- question: Ragas 框架的特點是什麼？
  choices:
  - 評估必須有人工註釋（Ground Truth）才能進行。
  - 支援無參考（reference-free）的評估方法。
  - 只評估檢索效率，不評估生成品質。
  - 不使用 LLM 作為評估者，只使用統計方法。
  answer_index: 1
  explanation: Ragas 的目標是建立一個無需參考即可評估的框架，並積極利用 LLM 作為評估者 [S3, S4]。
completion_criteria:
- 能夠使用 Ragas 函式庫定量測量生成答案的事實性。
- 在評估結果中，能夠分類至少 3 種幻覺發生類型。
- 能夠驗證自動化評估管道的結果與實際答案的一致性。
source_ids:
- S3
- S4
---

## 證據忠實度 (Faithfulness) 評估

RAG(Retrieval-Augmented Generation)系統的核心是LLM利用從外部知識資料庫中檢索到的資訊來生成答案。證據忠實度(Faithfulness)是指生成的答案是否忠實地反映了檢索到的上下文中所描述的資訊 [S3]。

### 1. 為何評估證據忠實度？
LLM傾向於根據預先學習的知識來回答，這可能會生成與檢索到的上下文無關的資訊，或扭曲上下文。這被稱為「幻覺(Hallucination)」，透過證據忠實度評估可以定量測量它 [S4]。

### 2. 評估框架：Ragas
Ragas提出了一個即使在沒有使用者註釋的情況下，也能在無參考基礎上(reference-free)進行評估的框架 [S3]。證據忠實度評估過程通常遵循以下步驟：
- **從答案中提取陳述**：從答案中分離出可驗證的事實陳述。
- **檢索證據**：確認每個陳述是從檢索到的上下文的哪個部分得出的。
- **驗證**：判斷提取的陳述是否與上下文資訊一致。

Ragas使用LLM作為評估者來自動化此過程 [S4]。
