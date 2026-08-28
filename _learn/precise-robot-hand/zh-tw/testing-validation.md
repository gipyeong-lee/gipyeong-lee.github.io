---
layout: learn-module
title: 測試與驗證
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:testing-validation
translations:
- lang: ko
  url: /learn/precise-robot-hand/testing-validation/
- lang: en
  url: /learn/en/precise-robot-hand/testing-validation/
- lang: ja
  url: /learn/ja/precise-robot-hand/testing-validation/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/testing-validation/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/testing-validation/
module_id: m8
permalink: /learn/zh-tw/precise-robot-hand/testing-validation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 86f63f17be15487197f653755bdf316f
id: m8
slug: testing-validation
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m7
objectives:
- 建立系統性的測試程序以評估機器手臂驅動系統的效能。
- 為進行數據導向的精確驗證，分析感測器數據與致動器回授。
- 驗證機器手臂的機械耐用性及重複精度。
- 編寫系統整合後的安全操作指南。
worked_examples:
- '**範例 1：重複精度誤差分析**

  於目標點 50 度重複移動 100 次後收集編碼器數值，確認平均值為 50.02 度，標準差為 0.05 度。此數值在要求的精度範圍內。'
- '**範例 2：基於 FSR 的握力校準**

  無壓力時 ADC 值為 50，最大抓取 (20 N) 時為 3800，使用線性內插法從 ADC 值即時估算力 (N) [S15]。'
lab:
  title: 機器手臂運動範圍及握力驗證
  steps:
  - 確認各獨立分支之電源轉接器連接部電壓為 12 V。
  - 在軟體力矩釋放狀態下，檢查機器手臂連桿間是否有機械干涉。
  - 在無負載狀態下，逐步檢查各手指的運動範圍。
  - 分階段 (0.5 N, 1 N, 5 N) 施加壓力至 FSR 感測器，並記錄 ADC 訊號。
  - 通電測試結束後，物理斷開所有電源轉接器。
  - 使用萬用電表確認 3 個分支電壓已放電至 1 V 以下。
  safety:
  - 維修及進入前，請物理斷開 3 個絕緣電源轉接器，並測量確認處於無電源狀態。
  - 通電過程中，切勿將手伸入運動範圍，並於固定治具上進行測試。
  - 若偵測到異常發熱、異味或煙霧，請勿靠近，應於危險區域外利用預先指定的建築物配電盤斷路器或認證的 3 upstream master disconnect 切斷供應電源後進行撤離。若危險區域外無可操作的
    upstream 斷電手段，請禁止系統通電。釋放力矩不能取代切斷電源。維修與進入僅限於計畫性停機、進行物理隔離並確認無電源測量後方可執行。
  - 作業時請務必佩戴防衝擊安全護目鏡。
  deliverables:
  - 運動範圍及握力測試記錄數據檔
  - 重複精度統計分析報告
  - 各電源分支量測安全確認書
assignment:
  title: 撰寫最終效能驗證報告
  deliverables:
  - 系統整合驗證報告 (PDF)
  - 效能指標數值數據及視覺化圖表
  - 操作指南及問題排除程序書
  rubric:
  - 確認運動範圍及重複精度測量數據的一致性
  - 驗證利用 FSR 感測器數據之力量控制演算法有效性
  - 透過機械耐用性測試評估損壞與組裝穩定性
  - 安全指南遵循狀況及程序合理性
quiz:
- question: 系統安全維修程序中，何者為非？
  choices:
  - 執行軟體力矩釋放。
  - 計畫性停機後，維修/進入前物理斷開 3 個電源轉接器並測量確認各分支處於無電源狀態。
  - 物理斷開 3 個電源轉接器，並使用萬用電表 DC 電壓模式確認各分支殘餘電壓小於 1 V。
  - 以 DC 電壓模式測量確認各分支小於 1 V。
  answer_index: 2
  explanation: 電阻模式在測量通電電路或未放電的電容器時，可能會導致設備損壞及誤判。確認無電源狀態務必使用 DC 電壓模式。
- question: FSR 402 感測器與 OpenCR 板應用於電路配置時的注意事項為何？
  choices:
  - FSR 分壓器僅限使用 3.3 V 感測器電源，並將類比輸入訊號維持在 0~3.3 V 範圍內。
  - FSR 分壓電路必須僅使用 3.3 V 感測器電源。
  answer_index: 1
  explanation: OpenCR 的 ADC 輸入不得超過 0~3.3 V 範圍，因此必須使用穩定的 3.3 V 感測器電源。
completion_criteria:
- 提交測試與驗證階段的所有實驗數據並完成日誌分析。
- 遵守 3 個獨立電源分支的物理斷開及安全電壓測量程序。
- 重複精度與握力的量化評估指標達到目標範圍。
- 以最終報告證明所有機械零件與電子電路皆安全運作。
source_ids:
- S1
- S12
- S14
- S15
- S18
- S21
- S16
- S17
- S26
---

### 1. 機器手臂效能評估之關鍵指標
機器手臂的效能驗證為證明機械設計忠實度與控制演算法效果的過程 [S1]。主要評估指標如下：
- **重複精度 (Repeatability)：** 到達相同目標位置時的誤差範圍，透過 `XM430-W350-T` 致動器的高解析度編碼器回授進行計算 [S14]。
- **抓取穩定性 (Grasp Stability)：** 透過分析 `FSR 402` 感測器所測量之接觸力分佈，評估物件抓取時是否會滑動 [S15]。
- **耐用性 (Durability)：** 為確認肌腱 (`Dyneema SK78`) 與連桿 (`PC-CF`) 結構是否有疲勞損壞，執行重複負載測試 [S18, S21]。

### 2. 數據獲取與分析
透過 `OpenCR` 控制板的 ADC 即時收集 FSR 數據。使用 3.3 V 感測器電源，於 0~3.3 V 範圍內將力訊號轉換為最高 12-bit 解析度 [S16]。獲取數據時，為減少雜訊，應用移動平均濾波器等方法平滑化握力變化。

### 3. 電氣安全驗證
各致動器群組由獨立的 `12 V` 轉接器分支構成，並透過 `10 A` ATOF 保險絲進行過電流保護 [S17, S26]。系統的無電源狀態確認，務必使用 DC 電壓模式（小於 1 V）進行測量。
