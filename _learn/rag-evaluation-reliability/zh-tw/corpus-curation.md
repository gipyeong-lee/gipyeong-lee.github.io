---
layout: learn-module
title: 評估用文件語料庫策展
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:rag-evaluation-reliability:corpus-curation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/corpus-curation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/corpus-curation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/corpus-curation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/corpus-curation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/corpus-curation/
module_id: m2
permalink: /learn/zh-tw/rag-evaluation-reliability/corpus-curation/
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
id: m2
slug: corpus-curation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- 理解 RAG 評估固定文件語料庫的重要性。
- 學習評估用文件數據的品質決定因素（準確性、多樣性、重複資料移除）。
- 掌握用於定量評估的文件-問題-答案配對（QA Pair）數據集建構策略。
- 學習防止數據洩漏（Data Leakage）的訓練/評估分割方法。
worked_examples:
- 範例 1：文件分塊 (Chunking) 策略。撰寫 Python 腳本的方法，以段落或語義單位分割文本，以避免在固定大小分割時上下文中斷。
- '範例 2：問題-答案資料結構。''{ ''question'': ''...'', ''ground_truth'': ''...'', ''context_chunk_id'':
  ''...'' }'' 格式的 JSON 物件生成範例。'
lab:
  title: 評估語料庫建置實作
  steps:
  - 取得要評估領域的開放授權文字檔 (.txt)。
  - 使用 Python 編寫一個腳本，用於讀取文字檔並將其分塊。
  - 為每個塊分配一個唯一識別碼 (ID)，並記錄元數據 (標題、來源)。
  - 從所編寫的塊中生成問題，並記錄作為答案依據的塊 ID，以構成 50 個 QA 對。
  - 將整個語料庫以 8:2 的比例分割成開發集和測試集，並儲存。
  safety:
  - 評估語料庫中不應包含個人資訊的文件。
  - 使用外部 API 時，設定請求數量上限以控制成本。
  - 工作時產生的資料透過 Git 進行版本管理，以確保可重現性。
  deliverables:
  - 已建置的文件語料庫檔案 (JSONL 格式)
  - 包含問題和正確答案的 QA 資料集 (JSON 格式)
  - 包含語料庫分割記錄的 Jupyter Notebook 檔案
assignment:
  title: 完成基於領域的 RAG 資料集
  deliverables:
  - 至少 100 個問題的 QA 資料集檔案
  - 資料集統計分析報告 (問題長度、塊長度等)
  - 包含資料分割過程的 Python 程式碼
  rubric:
  - 語料庫中重複塊的去除完成情況
  - 測試集和開發集的資料洩漏檢查
  - 答案依據的文件區段 (Chunk ID) 的準確映射情況
quiz:
- question: 在 RAG 系統中，防止「資料洩漏 (Data Leakage)」的最佳方法是什麼？
  choices:
  - 對所有文件生成相同的問題。
  - 分離管理開發集和最終評估用測試集。
  - 將整個檢索目標文件包含在訓練資料中。
  - 每次都重新生成評估集進行管理。
  answer_index: 1
  explanation: 評估集若在學習（或開發）過程中暴露於搜尋文件，則無法進行公正評估，因此必須嚴格區分用於評估的測試集。
- question: 在語料庫策劃過程中，「去除重複」為何重要？
  choices:
  - 為了提高 LLM 的生成速度
  - 為了節省磁碟儲存空間
  - 為了確保搜尋結果的多樣性並防止統計偏差
  - 為了降低文件的語義相似度
  answer_index: 2
  explanation: 重複資訊會導致搜尋引擎將搜尋結果傾向於特定資訊，並可能扭曲量化評估指標。
completion_criteria:
- 建立評估用文件語料庫（至少 100 個 chunk）完成
- 生成可驗證的 QA 資料集（至少 100 個問題）完成
- 確認遵守資料集分割政策
- 完成關於結果的同行審查或自我評估檢查清單
source_ids:
- S2
---

## 用於 RAG 評估的語料庫策劃

大型語言模型 (LLM) 在依賴其學習參數內的知識時存在幻覺的風險。檢索增強生成 (RAG) 透過允許模型即時存取外部知識來克服這些限制 [S2]。為了定量評估有效的 RAG 系統的可靠性，**固定且可控的評估文件語料庫 (Fixed Evaluation Corpus)** 至關重要。

### 1. 語料庫品質決定因素
- **準確性 (Factuality)：** 文件中的資訊必須是最新的且真實的。包含錯誤資訊的語料庫會導致生成錯誤的答案。
- **領域適用性：** 應包含與要評估的實際服務環境相似的主題和詞彙。
- **重複資料刪除 (De-duplication)：** 如果相同資訊在多個文件中重複，會損害檢索結果的多樣性，並可能對評估統計數據造成偏差。

### 2. 構建 QA 評估資料集
僅憑文件語料庫無法進行評估。必須構建「文件-問題-答案」對，以測量檢索器是否檢索相關文件，以及生成器是否基於這些文件提供準確的答案。
- **問題生成：** 使用 LLM 自動從文件中生成問題，或由領域專家直接撰寫。
- **答案定義：** 必須明確指定作為答案依據的文件區段 (Chunk)。

### 3. 資料分割與完整性
為了評估集的可靠性，必須嚴格分割**開發用 (Development Set)** 和**最終評估用 (Hold-out Test Set)**。必須防止評估集中包含的問題直接包含在檢索目標文件中而導致的「資料洩漏」現象。
