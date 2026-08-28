---
layout: learn-module
title: 致動器與感測器整合
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:actuators-sensors
translations:
- lang: ko
  url: /learn/precise-robot-hand/actuators-sensors/
- lang: en
  url: /learn/en/precise-robot-hand/actuators-sensors/
- lang: ja
  url: /learn/ja/precise-robot-hand/actuators-sensors/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/actuators-sensors/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/actuators-sensors/
module_id: m5
permalink: /learn/zh-tw/precise-robot-hand/actuators-sensors/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 86f63f17be15487197f653755bdf316f
id: m5
slug: actuators-sensors
phase_id: p2
estimated_hours: 13.0
prerequisites:
- m4
objectives:
- 理解 DYNAMIXEL 智慧致動器的控制訊號與電源分配結構。
- 了解 FSR (力感測電阻) 感測器的運作原理，並於 OpenCR 控制器設計分壓電路。
- 習得致動器電源分流與個別熔斷器保護之重要性。
- 熟悉肌腱驅動系統的機構特性與電子控制回授之連動方式。
worked_examples:
- 範例 1：各致動器分流最大負載計算。若 1 台致動器堵轉電流為 2.3 A [S14]，配置 4 台致動器的分流，最大峰值電流為 4 * 2.3 A = 9.2
  A。此數值在 10 A 熔斷器額定內 [S26]，且未超過 11.5 A 電源輸出規格，屬安全範圍 [S17]。
- 範例 2：FSR 分壓電路 ADC 電壓計算。感測器電阻為 R_fsr，固定電阻為 R_fixed (10 kΩ) 時，ADC 輸入電壓 V_adc = 3.3V
  * (R_fixed / (R_fsr + R_fixed)) [S16, S27]。無接觸力時 (無限大電阻) V_adc 為 0 V；最大接觸時感測器電阻小於固定電阻，V_adc
  接近 3.3 V，完成力數據數位化。
lab:
  title: 致動器與 FSR 感測器整合測試
  steps:
  - 各電源供應器輸出端連接 ATO inline 熔斷器座並插入 10 A 熔斷器 [S25, S26]。
  - 將 DYNAMIXEL 致動器線束連接至熔斷器之後的電源分流 [S9]。
  - 使用 FSR 感測器與 10 kΩ 電阻組成分壓電路，連接至 OpenCR 的 3.3 V ADC 連接埠 [S16, S27]。
  - 使用萬用電表設定 DC 電壓模式，確認各分流輸出電壓為 12 V。
  - 利用軟體低速無負載旋轉致動器，並檢查通訊狀態。
  safety:
  - 維修前物理斷開 3 個電源供應器，確認電壓低於 1 V，證實處於無電狀態。
  - 通電期間，切勿將手伸入致動器活動範圍內。
  - 電路測試時務必配戴護目鏡。
  - 若偵測到異常發熱、異味或冒煙，請勿靠近，並透過危險區域外的預設建物配電盤斷路器或認證的 upstream master disconnect 切斷 3 個供應器的電源後撤離。若危險區域外無可操作的
    upstream 斷電手段，禁止系統通電。扭力解除不等於電源切斷。維修或接近設備必須在計畫停止後，物理斷開電源並確認無電後才可進行。
  deliverables:
  - 各分流電壓測量校準記錄表
  - FSR 感測器壓力-ADC 值特性曲線圖
  - 正常運作狀態下的機器手臂線束照片與配線圖
assignment:
  title: 電源系統設計與回授邏輯實作
  deliverables:
  - 致動器分流負載分配與熔斷器保護計算書
  - 利用 FSR 感測器資料之抓取力控制演算法（虛擬碼）
  - 最終配線與電源整合設計報告
  rubric:
  - 12 V 致動器與 3.3 V 感測器電源軌是否正確分離？
  - 各分流之最大峰值電流是否未超過熔斷器額定？
  - 教育用原型機不主張符合機械安全標準或經認證，投入人員作業環境前須由具資格的安全專家另行審查？
  - 是否理解並遵守電源物理斷開之安全規則？
quiz:
- question: FSR 電壓分壓電路之電源供應應選用何者？
  choices:
  - 12 V 致動器電源
  - OpenCR 3.3 V 感測器電源
  answer_index: 1
  explanation: FSR 感測器的 ADC 訊號應使用 OpenCR 之 3.3 V 感測器軌，並與 12 V 致動器電源電氣上完全分離。
- question: 各分流熔斷器保護的主要目的為何？
  choices:
  - 將電壓強制鎖定在 12 V
  - 若偵測到異常發熱、異味或冒煙，請勿靠近，並透過危險區域外的預設建物配電盤斷路器或認證的 upstream master disconnect 切斷 3 個供應器的電源後撤離。若危險區域外無可操作的
    upstream 斷電手段，禁止系統通電。扭力解除不等於電源切斷。維修或接近設備必須在計畫停止後，物理斷開電源並確認無電後才可進行
  answer_index: 1
  explanation: 配置於各分流的 10 A 熔斷器，在允許致動器峰值電流運作的同時，可於配線短路等故障發生時保護系統。
- question: 絕緣型電源供應器的各個獨立正極 (+) 輸出是否可以連結？
  choices:
  - 為加總分流電流，必須連結
  - 絕對禁止，各分流必須維持獨立
  answer_index: 1
  explanation: 為確保獨立分流結構，嚴禁將正極 (+) 輸出並聯，各輸出須以物理分離的電源線束運作。
completion_criteria:
- 確認各致動器分流皆可正常測得 12 V 電壓。
- 成功透過控制器擷取 FSR 感測器資料，並驗證隨接觸力變化之 ADC 數值變化。
- 能物理切斷系統電源，並在低於 1 V 狀態下安全進行維修。
- 提交所有實作作業與安全遵守誓約書。
source_ids:
- S14
- S15
- S16
- S17
- S27
- S26
- S25
- S9
---

若偵測到異常發熱、異味或冒煙，請勿靠近，並透過危險區域外的預設建物配電盤斷路器或認證的 upstream master disconnect 切斷 3 個供應器的電源後撤離。若危險區域外無可操作的 upstream 斷電手段，禁止系統通電。扭力解除不等於電源切斷。維修或接近設備必須在計畫停止後，物理斷開電源並確認無電後才可進行 [S14] [S16] [S17] [S15] [S27] [S26]
