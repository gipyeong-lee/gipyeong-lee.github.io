---
layout: learn-module
title: 傳感器集成與反饋控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-tw
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
translation_run_id: 6d06f766b906424eb1f714f11e36dcf4
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M8
slug: sensor-integration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M7
objectives:
- 理解使用 FSR 402 傳感器和 10 kΩ 電阻構成分壓電路的原理
- 熟悉 OpenCR 控制器的 ADC 功能及輸入範圍（0-3.3 V）限制條件
- 掌握傳感器數據的過濾與校準技術
- 實現基於反饋的抓取控制算法，並進行機器手接觸力控制實踐
worked_examples:
- 範例 1：FSR 輸出計算。當 $R_{FSR}$ 為 5 kΩ，$R_{fixed}$ 為 10 kΩ，且以 3.3 V 輸入為基準時，$V_{out} =
  3.3 \times (5 / (5 + 10)) = 1.1 V。此值正常處於 ADC 輸入範圍（0-3.3 V）內。
- 範例 2：抓取力校準。若傳感器值因噪聲而波動，可應用簡單移動平均濾波器，以減少傳感器值的劇烈波動並穩定保持抓取力。
lab:
  title: 指尖 FSR 傳感器電路構建與校準
  steps:
  - 將 OpenCR 的 3.3 V 傳感器軌和 GND 連接到麵包板。
  - 將 FSR 402 與 10 kΩ 電阻串聯，構建分壓電路 [B4, B5]。
  - 將分壓節點連接到 OpenCR 的 ADC 引腳 [B2]。
  - 連接 PC 與 OpenCR，並執行讀取傳感器值的測試代碼。
  - 記錄無負載狀態和施加目標力時的 ADC 值，編寫校準表。
  safety:
  - 接通電源前，務必使用萬用表確認 3.3 V 軌與 12 V 執行器軌之間是否存在短路 [B2]。
  - 務必隨時佩戴護目鏡；通電期間，切勿將手放入機器手的運動範圍內。
  - 若偵測到異常發熱、氣味或煙霧，請勿靠近。在危險區域外，請斷開預先指定的建築配電盤斷路器或認證的上游主斷路器，切斷 3 個適配器的電源後撤離。若危險區域外無可操作的上游斷電手段，則禁止對系統通電。扭矩釋放不能替代切斷電源。維護與接近操作僅能在規劃停機後，經過物理斷電及確認無電狀態後方可進行。
  - 維修或接近傳感器前，請物理斷開 3 個絕緣電源適配器，並測量確認所有分支的電壓低於 1 V。
  deliverables:
  - ADC 傳感器讀取測試結果數據
  - 傳感器校準表（ADC 值 vs 物理力）
  - 傳感器數據過濾實現代碼
assignment:
  title: 抓取力反饋控制算法實現
  deliverables:
  - 反饋控制代碼（傳感器讀取、目標值比較、電機扭矩調整）
  - 抓取試驗結果圖表（時間與力）
  - 最終報告（控制邏輯說明及抓取穩定性分析）
  rubric:
  - ADC 數據是否在 0-3.3 V 範圍內穩定測量？
  - 當傳感器值達到目標值時，電機是否適當地釋放或保持扭矩？
  - 緊急情況下的扭矩釋放功能是否能通過軟件正常運作？
  - 報告中是否技術性描述了斷電確認程序？
quiz:
- question: 將 FSR 分壓信號輸入到 OpenCR 控制器的 ADC 引腳時，必須遵守的事項是什麼？
  choices:
  - 使用 12 V 執行器電源軌。
  - 僅使用 3.3 V 傳感器電源軌。
  - 使用 5 V 電源軌。
  - 另外從外部供應電源。
  answer_index: 1
  explanation: OpenCR 的 ADC 輸入範圍為 0-3.3 V，因此為了確保不施加超過此範圍的電壓，必須僅使用 3.3 V 傳感器電源軌。
- question: FSR 傳感器的電阻值變化與物理力之間有什麼關係？
  choices:
  - 壓力增加時電阻值增加。
  - 壓力增加時電阻值減小。
  - 壓力變化與電阻值無關。
  - 壓力增加時電阻值按固定比例放大。
  answer_index: 1
  explanation: FSR 是一種壓力感應電阻器，具有受壓時電阻值減小的特性。
- question: 在機器手原型開發過程中，為了維護或接近而切斷電源後，需要確認的安全狀態是什麼？
  choices:
  - 確認是否通過軟件釋放了扭矩。
  - 使用萬用表測量保險絲是否斷路。
  - 物理斷開 3 個電源適配器，並使用直流電壓模式測量確認各分支電壓低於 1 V。
  - 關閉電源開關後，使用電阻模式測量導線狀態。
  answer_index: 2
  explanation: 切斷電源是指物理斷開 3 個電源，為了安全，必須使用萬用表的直流電壓模式直接測量確認所有分支電壓低於 1 V。
completion_criteria:
- 通過 ADC 讀取 FSR 值的實驗練習
- 抓取力反饋控制代碼達到目標值的 90% 以上
- 證明遵守所有安全守則（物理斷電及測量電壓）
- 提交最終結果報告
source_ids:
- S3
- S12
- S26
---

## 感測器整合與接觸力回饋

機器手精密抓取控制，始於準確測量作用於指尖的力。FSR 402 感測器是一種壓力感測電阻器，其電阻值會隨著施加壓力增加而減少 [S12]。為將其轉換為微控制器可讀取的電壓訊號，需要電壓分壓電路。

### 1。電壓分壓電路
將 FSR 感測器與 10 kΩ 分壓電阻串聯，並供應 3.3 V 感測器電源 [B4, B5, B2]。ADC 接腳連接至感測器與電阻的接觸點，輸出電壓 $V_{out}$ 計算方式如下：
10 kΩ 下拉分壓器使用 $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$

- OpenCR 控制器的 ADC 具有 12 位元解析度，且輸入範圍限制為 0~3.3 V [B2]。超出此範圍的輸入可能會損壞電路元件，因此必須僅使用指定的感測器電源軌 (3.3 V) [B2]。

### 2。控制迴路與回饋
測得的力數據將作為 PID 控制演算法或適應性控制策略的輸入值 [S3]。當機器手抓取物體時，腱驅動馬達 (DYNAMIXEL XM430-W350-T) 會參考感測器數值，微調扭矩直至達到設定的目標接觸力 [B1, B4]。
