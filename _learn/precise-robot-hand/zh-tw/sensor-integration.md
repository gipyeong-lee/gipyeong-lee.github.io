---
layout: learn-module
title: 感測器整合與反饋控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:sensor-integration
translations:
- lang: ko
  url: /learn/precise-robot-hand/sensor-integration/
- lang: en
  url: /learn/en/precise-robot-hand/sensor-integration/
- lang: ja
  url: /learn/ja/precise-robot-hand/sensor-integration/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/sensor-integration/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/sensor-integration/
module_id: M8
permalink: /learn/zh-tw/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M8
slug: sensor-integration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M7
objectives:
- 理解使用 FSR 402 感測器與 10 kΩ 電阻組成電壓分壓電路的原理
- 熟悉 OpenCR 控制器的 ADC 功能與輸入範圍 (0-3.3 V) 限制條件
- 習得感測器資料的濾波與校準技術
- 實作基於反饋的抓取控制演算法，並進行機器手接觸力控制實習
worked_examples:
- 範例 1：FSR 輸出計算。當 $R_{FSR}$ 為 5 kΩ 且 $R_{fixed}$ 為 10 kΩ 時，以 3.3 V 輸入為基準，$V_{out}
  = 3.3 \times (5 / (5 + 10)) = 1.1 V。此數值正常落於 ADC 輸入範圍 (0-3.3 V) 內。
- 範例 2：抓取力校正。若感測器數值因雜訊而波動，可應用簡單移動平均濾波器，以減少感測器數值的劇烈變動，維持抓取力穩定。
lab:
  title: 指尖 FSR 感測器電路配置與校正
  steps:
  - 將 OpenCR 的 3.3 V 感測器軌與 GND 連接至麵包板。
  - 將 FSR 402 與 10 kΩ 電阻串聯，配置分壓電路 [B4, B5]。
  - 將分壓接點連接至 OpenCR 的 ADC 接腳 [B2]。
  - 連接 PC 與 OpenCR，執行讀取感測器數值的測試程式碼。
  - 記錄無負載狀態與施加目標力時的 ADC 數值，編製校正表。
  safety:
  - 通電前務必使用三用電表確認 3.3 V 軌與 12 V 致動器軌無短路 [B2]。
  - 全程佩戴安全眼鏡，通電時請勿將手伸入機器手的活動範圍內。
  - 若偵測到異常發熱、異味或冒煙，請勿靠近。請於危險區外，透過事先指定的建物配電盤斷路器或認證的上游主斷路器 (upstream master disconnect)
    切斷 3 個變壓器之供電後撤離。若無危險區外可操作的上游斷路手段，禁止系統通電。扭力釋放不能替代電源切斷。維護與接近需在計畫停機後，確認物理隔離與無電源測量後方可進行。
  - 維修或接近感測器前，請將 3 個隔離電源供應器物理分離，並測量確認所有分支電壓低於 1 V。
  deliverables:
  - ADC 感測器讀取測試結果資料
  - 感測器校正表 (ADC 數值 vs 物理力)
  - 感測器資料濾波實作程式碼
assignment:
  title: 抓取力反饋控制演算法實作
  deliverables:
  - 反饋控制程式碼 (讀取感測器、目標值比較、馬達扭力調整)
  - 抓取測試結果圖表 (時間 vs 力)
  - 最終報告 (控制邏輯說明與抓取穩定性分析)
  rubric:
  - ADC 資料是否在 0-3.3 V 範圍內穩定測量？
  - 當感測器數值達到目標值時，馬達是否適當釋放或維持扭力？
  - 緊急情況下扭力釋放軟體功能是否正常運作？
  - 報告中是否詳述斷電確認程序？
quiz:
- question: 將 FSR 分壓訊號輸入 OpenCR 控制器的 ADC 接腳時，必須遵守的事項為何？
  choices:
  - 使用 12 V 致動器電源軌。
  - 僅使用 3.3 V 感測器電源軌。
  - 使用 5 V 電源軌。
  - 電源另外由外部供給。
  answer_index: 1
  explanation: OpenCR 的 ADC 輸入範圍為 0-3.3 V，為避免輸入超過此範圍的電壓，必須僅使用 3.3 V 感測器電源軌。
- question: FSR 感測器的電阻變化與物理力之間有何關係？
  choices:
  - 壓力增加，電阻值增加。
  - 壓力增加，電阻值減少。
  - 壓力變化與電阻值無關。
  - 壓力增加，電阻值按固定比例放大。
  answer_index: 1
  explanation: FSR 為壓力感測電阻器，其特性為施加壓力時電阻值減少。
- question: 進行機器手原型製作時，為維護或接近而切斷電源後，需確認的安全狀態為何？
  choices:
  - 確認已透過軟體釋放扭力。
  - 使用三用電表測量保險絲是否斷線。
  - 物理分離 3 個電源供應器，並使用 DC 電壓檔位測量各分支電壓是否低於 1 V。
  - 關閉電源開關後，使用電阻檔位測量導線狀態。
  answer_index: 2
  explanation: 切斷電源是指將 3 個電源物理分離，為確保安全，務必使用三用電表的 DC 電壓檔位直接確認所有分支低於 1 V。
completion_criteria:
- 通過 ADC 讀取 FSR 數值實習
- 抓取力反饋控制程式碼達到目標值 90% 以上
- 證明遵守所有安全守則 (物理斷電與測量電壓)
- 提交最終結果報告
source_ids:
- S3
- S12
- S26
---

## 感測器整合與接觸力反饋

機器手的精密抓取控制始於精確測量指尖作用力。FSR 402 感測器是一種壓力感測電阻器，其電阻值隨施加壓力增加而減少 [S12]。若要將其轉換為微控制器可讀取的電壓訊號，需要分壓電路。

### 1. 電壓分壓電路
將 FSR 感測器與 10 kΩ 分壓電阻串聯，並供應 3.3 V 感測器電源 [B4, B5, B2]。ADC 接腳連接至感測器與電阻的接點，輸出電壓 $V_{out}$ 計算如下：
10 kΩ 下拉分壓器使用 $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$

- OpenCR 控制器的 ADC 具有 12 位元解析度，輸入範圍限制在 0~3.3 V [B2]。超出此範圍的輸入可能會損壞電路元件，因此必須僅使用指定的感測器電源軌 (3.3 V) [B2]。

### 2. 控制迴路與反饋
測得的力資料作為 PID 控制演算法或自適應控制策略的輸入值 [S3]。機器手抓取物體時，肌腱驅動馬達 (DYNAMIXEL XM430-W350-T) 會參考感測器數值，微調扭力直到達到設定的目標接觸力 [B1, B4]。
