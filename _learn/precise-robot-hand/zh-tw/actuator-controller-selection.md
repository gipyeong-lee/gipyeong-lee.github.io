---
layout: learn-module
title: 致動器與控制器選型
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:actuator-controller-selection
translations:
- lang: ko
  url: /learn/precise-robot-hand/actuator-controller-selection/
- lang: en
  url: /learn/en/precise-robot-hand/actuator-controller-selection/
- lang: ja
  url: /learn/ja/precise-robot-hand/actuator-controller-selection/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/actuator-controller-selection/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/actuator-controller-selection/
module_id: M3
permalink: /learn/zh-tw/precise-robot-hand/actuator-controller-selection/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 6d06f766b906424eb1f714f11e36dcf4
id: M3
slug: actuator-controller-selection
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M2
objectives:
- 理解 DYNAMIXEL XM430-W350-T 致動器的額定電壓、電流與通訊特性。
- 熟悉 OpenCR 1.0 控制器的 DYNAMIXEL 連接埠架構與 12V 電源分離結構。
- 設計使用 FSR 402 感測器與 10kΩ 電阻的分壓電路。
- 計算系統電源需求並建立獨立分路保險絲保護設計。
worked_examples:
- 範例 1：確認各分路最大電流。若單一分路連接 4 台 XM430 致動器，失速電流合計為 4 * 2.3A = 9.2A。此數值滿足轉接器 11.5A 額定與串聯式保險絲
  10A 額定，維持在安全範圍內 [S11, S15, S25]。
- 範例 2：FSR 分壓電路電壓計算。在 3.3V 供應電壓下，當 FSR 電阻為 R_fsr 時，ADC 輸入電壓 V_adc = 3.3 * (10k / (10k
  + R_fsr)) V。依據感測器範圍 (0.2N~20N) 確認電阻變化，以校準確保不超過 0~3.3V 範圍 [S12, S13, S26]。
lab:
  title: 電源分路建構與 ADC 感測器介面實習
  steps:
  - 於每個 MEAN WELL 轉接器輸出端連接 0AFH0001Z 保險絲座並插入 0287010 10A 保險絲。
  - 將三用電表設為 DC 電壓模式，確認各分路電壓皆為穩定的 12V。
  - 使用 10kΩ 電阻與 FSR 402 在 OpenCR 的 3.3V 感測器軌上架設分壓電路。
  - 在無電源狀態下，確認分壓電路輸出電壓位於 0~3.3V 範圍內。
  safety:
  - 作業開始前，請物理斷開 3 台轉接器的 AC 電源，並確認三用電表顯示為 0V。
  - 必須隨時佩戴耐衝擊防護眼鏡。
  - 電源開啟時，絕不可更改電路或觸碰線路。
  - 明示保險絲僅用於過電流截斷，不得作為計畫停止手段。
  deliverables:
  - 各分路 12V 輸出測量紀錄表
  - FSR 分壓電路組裝完成照
  - 配置好的線路圖
assignment:
  title: 電源分路與保護設計審核
  deliverables:
  - 整個機器手的電流分路分配表（各分路致動器分配）
  - 證明選用保險絲在保護致動器失速電流的同時，不超過轉接器容量的計算書
  rubric:
  - 獨立保險絲是否已準確配置於各分路？
  - 致動器分路分配是否符合 4/4/3 之規定？
  - 感測器電源是否由 3.3V 感測器軌（而非 12V）供應？
quiz:
- question: 使用 FSR 402 感測器與 10kΩ 電阻的分壓電路，正確的電源連接為何？
  choices:
  - 12V 致動器電源
  - OpenCR 3.3V 感測器軌
  - 5V 通用電源
  - OpenCR 12V 輸出
  answer_index: 1
  explanation: 由於 OpenCR 的 ADC 輸入基於 3.3V 運作，電壓分壓電路務必由 3.3V 感測器軌供電 [S13]。
- question: XM430-W350-T 致動器的失速電流值為何？
  choices:
  - 1.0A
  - 2.3A
  - 4.1A
  - 11.5A
  answer_index: 1
  explanation: 根據資料手冊，該致動器的失速電流為 2.3A [S11]。
- question: 電源分路設計中絕對禁止的行為為何？
  choices:
  - 各轉接器輸出加裝保險絲
  - 轉接器的陽極(+)輸出並聯
  - 每分路使用 10A 保險絲
  - 使用絕緣型轉接器
  answer_index: 1
  explanation: 轉接器的陽極(+)輸出必須維持獨立分路，絕對禁止並聯 [B3]。
completion_criteria:
- 實習中已用三用電表驗證 3 個獨立分路的 12V 電壓
- 已完成 FSR 402 感測器分壓電路配線與 ADC 輸入電壓範圍確認
- 提交電源分路與保護設計報告並通過
source_ids:
- S4
- S5
- S11
- S13
- S15
- S24
- S25
- S12
- S26
---

### 致動器與控制器系統設計理論

#### 1. 致動器選型與電源特性
為了機器手的精密驅動，採用 DYNAMIXEL XM430-W350-T。此致動器於 12V 額定電壓下運作，失速 (Stall) 電流為 2.3A [S11]。整個機器手由 11 台致動器組成，總失速電流合計約達 25.3A。因此，為了穩定驅動，需要獨立的電源供應體系。

#### 2. 控制器架構
OpenCR 1.0 搭載 216MHz ARM Cortex-M7 處理器，適合即時控制 [S13]。此控制器支援將 12V 致動器電源與邏輯/感測器電源進行物理分離的架構。由於 FSR 感測器等類比輸入必須在 0~3.3V 範圍內處理，感測器分壓電路務必由 OpenCR 的 3.3V 感測器軌供電 [S13]。

#### 3. 過電流保護與電源分路設計
使用輸出 138W 的 MEAN WELL GST160A12-R7B 轉接器 3 台 [S15]。各轉接器額定電流為 11.5A，據此建立 3 個獨立的 12V 分路。每個分路均安裝 10A ATOF 串聯式保險絲，以在發生過電流時保護電路 [S24, S25]。保險絲應設定低於額定電流 11.5A，以達成保護協調性。

#### 4. 感測器訊號獲取
FSR 402 具有壓力增加時電阻降低的特性 [S12]。將其與 10kΩ 固定電阻以電壓分壓器連接，將力變化轉換為電壓訊號，並輸入至 OpenCR 的 12bit ADC 埠 [S12, S13, S26]。
