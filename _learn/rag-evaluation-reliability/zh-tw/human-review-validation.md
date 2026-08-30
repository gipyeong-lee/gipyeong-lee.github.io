---
layout: learn-module
title: 樣本人工審查與對照
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:human-review-validation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/human-review-validation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/human-review-validation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/human-review-validation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/human-review-validation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/human-review-validation/
module_id: m9
permalink: /learn/zh-tw/rag-evaluation-reliability/human-review-validation/
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
id: m9
slug: human-review-validation
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m8
objectives:
- 了解自動化 RAG 評估指標與實際事實性之間的差距。
- 設計人工審查模型生成答案的事實一致性 (Factual Consistency) 的協議。
- 了解 LLM 評估的局限性，並分析 TrueTeacher 等合成資料方法的意義 [S5]。
- 學習如何系統地分類錯誤類型並管理可靠性資料集。
worked_examples:
- 範例 1：自動評估指標 (例如：Faithfulness) 顯示 0.9 為高分，但人工審核結果發現包含檢索文件中未提及的內容。分析：將其分類為模型未使用檢索到的資訊，而是使用了內部權重中包含的過往資訊所產生的幻覺，並將此記錄於系統錯誤日誌中。
- 範例 2：設計由系統使用 TrueTeacher 模型自行評估回答事實性的情況。由人工抽樣調查 LLM 評估為「真」的回答中之部分內容，以測量 LLM 評估器的錯誤率
  (False Positive)，並將其標示於評估報告中 [S5]。
lab:
  title: 執行抽樣人工審核及錯誤分析
  steps:
  - 透過自動評估管線 (Ragas 等) 推導出 100 件回答的 Faithfulness 分數。
  - 隨機抽取分數最低的 10 件、中間水準的 10 件及分數最高的 10 件，建立審核集。
  - 比對回答、檢索文件 (Context) 與正確答案 (Ground Truth)，手動記錄是否存在「檢索遺漏」、「資訊扭曲」或「生成幻覺」。
  - 比較記錄到的人工判斷與自動評估分數，執行相關性分析。
  safety:
  - 務必確認審核對象數據集未包含實際個人資訊或敏感的非公開文件。
  - 審核完成的數據須安全地存放在本地儲存空間，不得上傳至未經驗證的外部 API。
  deliverables:
  - 包含至少 30 件人工審核紀錄的錯誤分類表 (CSV/Excel)
  - 分析自動指標與人工評估之間一致性的摘要報告
assignment:
  title: 撰寫 RAG 可靠性分析報告
  deliverables:
  - 透過人工審核分類出的失敗類型頻率表
  - 關於目前系統主要弱點（檢索階段或生成階段）的分析報告
  - 針對未來自動評估管線改善的建議
  rubric:
  - 錯誤類型是否已系統性分類？
  - 是否結合具體範例，合乎邏輯地論述了自動評估指標的局限性？
  - 人工審核數據是否適當地作為可靠性分析的依據被運用？
quiz:
- question: 僅憑自動化事實性評估指標難以確認系統可靠性的主要原因為何？
  choices:
  - 因為自動評估指標非常快速。
  - 因為模型生成的數據具有與人類撰寫數據不同的特徵，且自動評估器本身可能無法捕獲所有事實錯誤 [S5]。
  - 因為人工審核數據總是比自動評估指標更精準。
  - 因為數據集的規模很小。
  answer_index: 1
  explanation: 現有的摘要基礎評估數據集無法充分反映模型生成實際結果的複雜性，自動評估系統在特定情況下可能無法檢測出幻覺。
- question: TrueTeacher 方法與現有摘要數據集的使用方式有何不同？
  choices:
  - 僅依賴人類編寫的摘要。
  - 利用模型生成的各種摘要來生成用於事實性評估的合成數據 [S5]。
  - 不使用 NLI 模型。
  - 無法支援多語言。
  answer_index: 1
  explanation: TrueTeacher 不依賴人類編寫的摘要，而是使用 LLM 對模型生成的各種數據進行合成註釋，從而生成訓練數據 [S5]。
completion_criteria:
- 必須編寫至少 30 個數據樣本的人類審查日誌。
- 必須提交包含自動評估結果與人類審查結果對比分析的報告。
- 必須通過錯誤分類明確定義當前系統的弱點。
source_ids:
- S5
---

## 自動化評估的局限與人工審核的必要性

評估檢索增強生成 (RAG) 系統的品質時，像 Ragas 這樣的工具雖然能快速提供量化指標，但在完美捕捉模型生成回答中細微的事實錯誤方面仍有局限。特別是在複雜的語境中，很難區分 LLM 是在知識範圍內進行推論，還是依賴已學習的數據產生幻覺 (Hallucination)。

### 事實一致性評估

近期的研究利用自然語言推論 (NLI) 模型或大型語言模型 (LLM) 來評估摘要或回答的事實性。然而，傳統方法依賴人類撰寫的摘要數據集，這可能與實際模型生成結果的特性產生差異 [S5]。像 TrueTeacher 這樣的途徑，試圖透過利用 LLM 從模型生成的數據中產出合成的事實性評估數據，藉此克服上述限制 [S5]。

### 人工審核 (Human-in-the-Loop) 的角色

無論自動評估管線進化到何種程度，最終的可靠性驗證仍需人工審核。人工審核執行以下角色：
1. **自動評估指標的驗證：** 識別特定回答雖被評估為「相關」但實際上並非事實的情況。
2. **幻覺類型分類：** 診斷系統的結構性缺陷（檢索錯誤 vs. 生成模型錯誤）。
3. **回歸測試集的校準：** 根據人類審核過的數據，持續改善評估集的品質。
