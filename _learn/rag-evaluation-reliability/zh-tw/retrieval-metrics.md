---
layout: learn-module
title: 檢索品質指標 (召回率@k, MRR, nDCG)
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:retrieval-metrics
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/retrieval-metrics/
- lang: en
  url: /learn/en/rag-evaluation-reliability/retrieval-metrics/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/retrieval-metrics/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/retrieval-metrics/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/retrieval-metrics/
module_id: m4
permalink: /learn/zh-tw/rag-evaluation-reliability/retrieval-metrics/
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
id: m4
slug: retrieval-metrics
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- 理解檢索增強生成 (RAG) 管線中檢索階段的重要性。
- 學習召回率@k、MRR、nDCG 指標的概念及其在 RAG 系統評估中的意義。
- 分析檢索到的上下文相關性對後續答案生成品質的影響。
worked_examples:
- 對於問題，系統依序返回 [DocB, DocA, DocC]，若正確答案相關文件為 DocA，則 MRR 計算：DocA 為第 2 個，因此倒數排名為 1/2
  = 0.5。
- 當 k=3 時，若前 3 個檢索結果包含正確答案文件，則 Recall@3 = 1；若不包含，則 Recall@3 = 0。
lab:
  title: 檢索品質指標定量測量實作
  steps:
  - 使用評估集（問題、正確答案文件）準備 50 個樣本數據。
  - 執行檢索模組，接收每個問題的前 k (k=3, 5, 10) 個文件。
  - 使用 Python 直接實作 Recall@k、MRR、nDCG 函數，或使用函式庫計算。
  - 將各問題的指標結果整理成資料框並視覺化。
  safety:
  - 不將包含個人資訊或非公開文件的資料集傳輸到外部 API。
  - 實驗時設定 API 費用限制並利用快取優化請求數量。
  deliverables:
  - 包含各問題 Recall@k、MRR、nDCG 值的結果資料框 CSV
  - 顯示指標分佈的長條圖及箱形圖圖片
assignment:
  title: 檢索器(Retriever)性能比較報告
  deliverables:
  - 應用兩種檢索設定（例如：Sparse vs Dense Retrieval）的評估結果報告
  - 對性能較低的上位 5 個問題進行原因分析（錯誤檢索類型分類）
  rubric:
  - 是否準確計算 Recall@k、MRR、nDCG 指標？
  - 是否對檢索性能差異進行了統計學上顯著的解釋？
  - 是否系統地分類了失敗類型？
quiz:
- question: RAG 系統中檢索階段的品質對生成階段有何影響？
  choices:
  - 檢索品質與生成品質無關。
  - 相關性低的上下文會增加 LLM 產生幻覺的風險。
  - 檢索階段僅評估 LLM 的推理能力。
  - 檢索結果越多，生成品質總是越好。
  answer_index: 1
  explanation: 檢索階段若傳遞不相關的資訊，LLM 可能會基於此生成錯誤的答案或產生幻覺 [S3]。
- question: MRR 指標最高時為何時？
  choices:
  - 相關文件總是在最後出現時
  - 相關文件總是位於最頂端（第 1 位）時
  - 當沒有任何搜尋結果時
  - 當相關文件總是在中間出現時
  answer_index: 1
  explanation: MRR是正確文件排名倒數的平均值，因此當位於1上方時，其值達到最大(1)。
completion_criteria:
- 完成了Recall@k、MRR、nDCG的計算程式碼並應用於樣本資料。
- 比較了兩種搜尋策略並得出了定量分析結果。
- 分類了至少3種搜尋失敗類型並記載於報告中。
source_ids:
- S3
- S4
---

### RAG 檢索品質評估的重要性

RAG 系統會從外部資料庫檢索相關資訊，並將其傳遞給 LLM 以生成答案 [S3]。因此，如果檢索階段無法識別出高相關性且集中的上下文，即使 LLM 再強大，也很難生成準確的答案 [S3]。評估檢索品質是改進 RAG 架構整體性能的第一步。

### 主要檢索評估指標

1. **Recall@k (召回率)**：衡量在前 k 個檢索結果中是否包含實際的正確答案。換句話說，此指標用於確認所需的資訊是否已被檢索系統捕獲。
2. **MRR (Mean Reciprocal Rank，平均倒數排名)**：衡量使用者問題的正確答案（相關文件）在檢索結果列表中的位置。相關文件越早出現在列表中的第一個位置，MRR 值就越接近 1 並獲得高分。
3. **nDCG (normalized Discounted Cumulative Gain，歸一化折損累積增益)**：考量檢索結果順序的指標，相關性高的文件若位於頂部位置，將獲得更高的分數。相較於單純的包含與否（召回率），此指標能更精確地評估檢索結果的「排名準確性」。

這些指標在有參考數據（Ground Truth）的情況下對於系統改進至關重要，Ragas 等框架提供了能夠定量分析這些維度的工具 [S3, S4]。
