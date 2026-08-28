---
layout: learn-module
title: 機器人學概論
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:intro-robotics
translations:
- lang: ko
  url: /learn/precise-robot-hand/intro-robotics/
- lang: en
  url: /learn/en/precise-robot-hand/intro-robotics/
- lang: ja
  url: /learn/ja/precise-robot-hand/intro-robotics/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/intro-robotics/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/intro-robotics/
module_id: m1
permalink: /learn/zh-tw/precise-robot-hand/intro-robotics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 86f63f17be15487197f653755bdf316f
id: m1
slug: intro-robotics
phase_id: p1
estimated_hours: 10.0
prerequisites: []
objectives:
- 理解機器人學的定義與系統組件。
- 了解 5 機器手臂原型機中所使用的致動器與控制器之角色。
- 學習機器人系統的電源分流配置與物理斷路原理。
- 熟練力感測器 (FSR) 的運作原理與 ADC 資料擷取方式。
worked_examples:
- 致動器負載計算：將 4 台 XM430-W350-T 配置於 1 個分流時，峰值電流為 4 * 2.3 A = 9.2 A [S14]。此數值在 10 A 熔斷器的額定範圍內，且低於電源供應器的
  11.5 A 輸出額定，確保運行穩定 [S17, S26]。
- FSR 分壓器設計：在感測器與 10 kΩ 電阻串聯的分壓器中，當輸入 3.3 V 且感測器未受壓（高電阻狀態）時，ADC 數值接近 0 V；當受強力按壓使電阻驟降時，ADC
  數值則接近 3.3 V [S15, S27]。
lab:
  title: 電源分流配置與系統基本通電測試
  steps:
  - 將各 MEAN WELL 供應器的正極 (+) 端子連接 ATO inline holder 與 10 A 熔斷器，建立 3 個獨立分流 [S17, S25,
    S26]。
  - 將萬用電表設定為 DC 電壓模式，確認各分流輸出電壓為 12 V。
  - 將 OpenCR 控制器連接至 3.3 V 感測器電源軌，並利用 FSR 感測器與 10 kΩ 電阻組成分壓電路 [S16, S27]。
  - 通電後，使用 DYNAMIXEL Wizard 確認各肌腱致動器通訊是否正常 [S14, S16]。
  safety:
  - 通電前，請務必透過目視與電路圖重新驗證所有接線，勿使用萬用電表電阻檔位檢查。
  - 通電期間禁止接近系統，配線作業必須在完全無電狀態（物理斷開供應器）下進行。
  - 若偵測到異常發熱、異味或冒煙，請勿靠近，並透過危險區域外的預設建物配電盤斷路器或認證的 upstream master disconnect 切斷 3 個供應器的電源後撤離。若危險區域外無可操作的
    upstream 斷電手段，禁止系統通電。扭力解除不等於電源切斷。維修或接近設備必須在計畫停止後，物理斷開電源並確認無電後才可進行。
  - 隨時配戴護目鏡，切勿將身體部位伸入活動範圍內。
  deliverables:
  - 各分流 12 V 測量記錄照片
  - OpenCR ADC 感測器資料擷取程式碼
  - 獨立分流接線圖
assignment:
  title: 機器人系統安全設計報告
  deliverables:
  - 獨立電源分流配置圖
  - 致動器峰值電流對應熔斷器額定之合理性分析
  - FSR 分壓電路設計公式與計算
  rubric:
  - 致動器 11 台與電源分流 3 個的分配是否明確？
  - 3.3 V 感測器軌與 12 V 致動器軌之分離描述是否正確？
  - 斷電流程（物理斷開）描述是否精確？
quiz:
- question: 系統電源設計時，為何禁止將 12 V 輸出端子的正極 (+) 並聯？
  choices:
  - 因為電壓會上升至 24 V
  - 存在因供應器間電位差導致逆電流產生及獨立分流保護失效之風險
  - 因為會導致致動器通訊速度下降
  - 因為無法使用軟體扭力解除功能
  answer_index: 1
  explanation: 各電源供應器必須作為獨立分流運作，若將輸出端子連結，恐導致故障或使獨立熔斷器的安全保護功能失效。
- question: 使用 OpenCR ADC 連接埠讀取 FSR 訊號時，合適的供電電壓為何？
  choices:
  - 12 V 致動器電源軌
  - 3.3 V 感測器電源軌
  - 24 V 輸入電源
  - 非接觸式無線電源
  answer_index: 1
  explanation: OpenCR 的 ADC 使用 0~3.3 V 範圍，為保護感測器，必須由專用的 3.3 V 感測器電源軌供電。
- question: 系統檢查與維修時，切斷電源最安全的方法為何？
  choices:
  - 透過軟體指令解除致動器扭力
  - 移除熔斷器
  - 物理斷開 3 個電源供應器後進行電壓測量
  - 僅關閉控制器電源開關
  answer_index: 2
  explanation: 軟體指令或移除熔斷器無法確保完全無電。必須物理斷開供應器，並使用萬用電表測量確認電壓低於 1 V。
completion_criteria:
- 使用萬用電表確認各分流 12 V 電壓在正常範圍內，並繳交照片證明。
- 透過控制器確認 FSR 感測器隨接觸力變化的 ADC 數值變化，並取得合理數據。
- 理解並遵守物理斷電與電壓測量之安全停止程序。
source_ids:
- S1
- S14
- S16
- S17
- S25
- S26
- S15
- S27
---

## 機器人系統組成元件
機器人由感測(Sensor)、思考(Controller)、動作(Actuator)這三個核心要素組成 [S1]。本課程的 5 指機器人手使用 DYNAMIXEL XM430-W350-T 致動器，透過腱驅動方式來控制關節 [S14]，並透過 OpenCR 1.0 控制器處理這些致動器以及指尖 FSR 感測器的訊號 [S16]。

## 電力系統的安全設計
由於致動器在 12 V 電壓下需要 2.3 A 的堵轉電流 [S14]，考量系統整體負載，使用 3 個 MEAN WELL GST160A12-R7B 變壓器 [S17]。每個變壓器運行在獨立的 12 V 分支，分別負責 4 個 / 4 個 / 3 個致動器，這些分支的正極(+)輸出互不結合，在物理上是隔離的。每個分支都透過線路座 (0AFH0001Z) 安裝 10 A ATOF 保險絲，以在發生過電流時保護配線 [S25, S26]。這不僅僅是單純的停止功能，更是電氣安全的基本基礎。

## 感測器介面
FSR 402 感測器具有隨接觸力增加而電阻減小的特性 [S15]。將其與 10 kΩ 電阻組成分壓電路，並連接至 OpenCR 的 12-bit ADC 通道，即可將接觸力換算為電壓 [S16, S27]。此時感測器電路必須僅由 3.3 V 感測器電源軌供電，不得與致動器用的 12 V 電源軌混合使用。
