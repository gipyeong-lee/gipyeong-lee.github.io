---
layout: learn-module
title: 建立問題-答案評估集
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:eval-set-generation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/eval-set-generation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/eval-set-generation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/eval-set-generation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/eval-set-generation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/eval-set-generation/
module_id: m3
permalink: /learn/zh-tw/rag-evaluation-reliability/eval-set-generation/
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
id: m3
slug: eval-set-generation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- 理解為 RAG 系統評估建立高品質問題-答案（QA）評估集的必要性。
- 掌握利用合成資料生成技術（Synthetic Data Generation）建立評估集的原理。
- 學習透過 TrueTeacher 等方法論評估模型生成答案的事實一致性之邏輯。
- 設計一個能在保持評估集品質的同時，生成對領域變更具備穩健性的資料集之流程。
worked_examples:
- 範例 1：從文件語料庫中提取關鍵片段。構成一個管線，該管線使用 LLM 從給定文件中提取語境上重要的事實句子，並以此為基礎生成「可回答的問題」和「虛假問題（Negative
  Sample）」。
- 範例 2：事實性驗證提示設計。一個精煉評估用真實值（Ground Truth）的過程，該過程指示 LLM 根據檢索到的文件回答問題，並判斷答案是否在事實上一致（True/False），此判斷基於生成的問題和檢索到的文件。
lab:
  title: 合成評估集生成實踐
  steps:
  - 載入準備好的開放授權文件語料庫，並將其分割為文字區塊。
  - 使用 LLM API 為每個區塊生成至少 100 組獨特的問答對。
  - 針對生成的問句，模擬搜尋系統以檢索前 k 個文件。
  - 建立一個評估管線，用於判斷檢索到的文件與生成的答案之間的事實一致性。
  - 將結果數據以 JSONL 格式儲存，並手動審查樣本 30 件以記錄數據品質。
  safety:
  - 在建立評估集過程中，使用外部 API 時必須設定費用上限（API Key Limit）。
  - 利用正規表達式過濾生成的數據集中是否包含原始文件的敏感資訊或個人資訊。
  - 不盲目相信模型評估結果，務必同時進行樣本的手動比對。
  deliverables:
  - 已建立 100 題以上的問答評估集 (JSONL 檔案)
  - 包含數據集生成與驗證程式碼的 Jupyter Notebook
  - 包含人工審查記錄的品質分析報告
assignment:
  title: RAG 可靠性評估集迴歸報告
  deliverables:
  - 分析生成評估集的統計分佈（問題長度、答案長度、文件參考頻率等）的儀表板
  - 以相同評估集比較兩種以上 RAG 設定（例如：檢索演算法變更、模型變更）的結果
  - 錯誤分類表（幻覺、上下文不相關等）撰寫與案例分析
  rubric:
  - 評估集是否均勻反映了整個文件語料庫的內容？
  - 合成數據生成管線是否以可重現的形式撰寫？
  - 錯誤類型分類是否具備具體且定量的依據？
  - 是否透過人工審查證明了自動評估指標的有效性？
quiz:
- question: TrueTeacher 方法論與現有合成數據生成方式的區別為何？
  choices:
  - 完全依賴人工撰寫的摘要。
  - 透過註釋模型生成的各種摘要來生成合成數據。
  - 僅使用小型模型作為訓練教師。
  - 僅透過手動撰寫數據集來提高準確性。
  answer_index: 1
  explanation: TrueTeacher 不依賴人工撰寫的摘要，而是透過使用大型語言模型（LLM）註釋模型生成的各種摘要來生成合成數據 [S5]。
- question: 在建立 RAG 評估集時，為何不單獨依靠模型自動評估來確定事實性？
  choices:
  - 因為模型自動評估比人工慢太多。
  - 因為模型自動評估不完美，無法完全過濾掉幻覺（Hallucination）。
  - 因為人工評估不需要成本。
  - 因為事實性評估不需要模型。
  answer_index: 1
  explanation: 自動化評估工具雖然效率高，但並不完美，因此為了驗證事實性，務必同時進行樣本人工審查和來源比對。
completion_criteria:
- 100 題以上問答評估集數據集建立完成
- 提交數據集品質分析及人工審查記錄
- 實作 RAG 管線效能評估的筆記本並撰寫結果報告
- 在 CI/CD 環境中配置可重新執行的評估套件
source_ids:
- S5
---

## 為 RAG 評估建立問題-答案（QA）評估集

為了可靠地衡量 RAG（檢索增強生成）系統的效能，精心設計的評估集是必不可少的。僅依賴人類編寫的問題和答案，在大規模評估時，在成本和可擴展性方面存在局限。

### 合成資料生成的必要性
根據最新的研究，TrueTeacher 方法論指出，可以利用 LLM 來生成模型產生的各種答案，並進行註釋以創建合成訓練資料 [S5]。此方法具有以下優點：
1. **成本效益**: 無需依賴人類直接編寫的摘要或答案，即可生成大規模資料集（例如：1.4M 範例）[S5]。
2. **多語言與可擴展性**: 不限於特定語言，並且對領域轉換（Domain-shift）表現出穩健性 [S5]。
3. **事實一致性評估**: 通過合成資料訓練的小型模型，可以成功地將大型 LLM 教師模型的知識進行蒸餾（Distillation），並用作高效的事實性評估工具 [S5]。

### 資料集構成策略
在建立評估集時，不應僅僅創建問題-答案對，還應構建能夠衡量「檢索結果是否包含推導答案所需的依據？」以及「模型是否無偏差地引用了這些依據？」的評估集。為此，在生成資料集時，必須系統地標記或驗證問題的複雜度、與檢索結果的相關性以及答案的事實一致性。
