---
layout: learn-module
title: 致動器與控制器選擇
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
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M3
slug: actuator-controller-selection
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M2
objectives:
- 理解 DYNAMIXEL XM430-W350-T 致動器的額定電壓、電流與通訊特性。
- 熟知 OpenCR 1.0 控制器的 DYNAMIXEL 連接埠配置與 12V 電源分離結構。
- 設計使用 FSR 402 感測器與 10kΩ 電阻的分壓電路。
- 計算系統電力需求並建立獨立分路保險絲保護設計。
worked_examples:
- 例題 1：確認單一分路最大電流。若單一分路連接 4 個 XM430 致動器，失速電流總和為 4 * 2.3A = 9.2A。此數值滿足電源供應器 11.5A 額定值及
  10A 線路保險絲額定，維持安全範圍 [S11, S15, S25]。
- 例題 2：FSR 分壓電路電壓計算。在 3.3V 供應電壓下，若 FSR 電阻為 $R_fsr$，ADC 輸入電壓 $V_adc = 3.3 * (10k /
  (10k + R_fsr)) V$。根據感測器範圍 (0.2N~20N) 確認電阻變化，避免電壓超出 0~3.3V 範圍 [S12, S13, S26]。
lab:
  title: 電源分路配置與 ADC 感測器介面實習
  steps:
  - 在各 MEAN WELL 供應器輸出端連接 0AFH0001Z 保險絲座，並插入 0287010 10A 保險絲。
  - 將三用電表設定為 DC 電壓模式，確認各分路電壓是否穩定於 12V。
  - 在 OpenCR 的 3.3V 感測器導軌上，使用 10kΩ 電阻與 FSR 402 組成分壓電路。
  - 於非通電狀態確認分壓電路輸出電壓是否位於 0~3.3V 範圍內。
  safety:
  - 作業開始前，物理切斷 3 個供應器的 AC 電源，並以三用電表確認為 0V。
  - 隨時佩戴防撞護目鏡。
  - 通電期間絕對不得更改電路或觸碰配線。
  - 保險絲僅用於過電流切斷，非計畫性停止手段。
  deliverables:
  - 各分路 12V 輸出測量紀錄單
  - FSR 分壓電路組裝完成照
  - 配置完成之配線圖
assignment:
  title: 電源分路與保護設計審查
  deliverables:
  - 整體機器人手電流分路分配表（各分路分配之致動器）
  - 證明所選保險絲可在保護致動器失速電流的同時，不超過供應器容量的計算書
  rubric:
  - 獨立保險絲是否正確配置於各分路？
  - 致動器分路分配是否為 4/4/3 並符合規範？
  - 感測器電源是否由 3.3V 感測器導軌而非 12V 提供？
quiz:
- question: 使用 FSR 402 感測器與 10kΩ 電阻的分壓電路，正確電源連接為何？
  choices:
  - 12V 致動器電源
  - OpenCR 3.3V 感測器導軌
  - 5V 通用電源
  - OpenCR 12V 輸出
  answer_index: 1
  explanation: OpenCR 的 ADC 輸入操作電壓基準為 3.3V，因此分壓電路務必由 3.3V 感測器導軌供電 [S13]。
- question: XM430-W350-T 致動器的失速電流值為？
  choices:
  - 1.0A
  - 2.3A
  - 4.1A
  - 11.5A
  answer_index: 1
  explanation: 依據數據表，該致動器的失速電流為 2.3A [S11]。
- question: 電源分路設計中，絕對禁止的行為為何？
  choices:
  - 於各供應器輸出裝設保險絲
  - 將供應器的陽極(+)輸出並聯
  - 每分路使用 10A 保險絲
  - 使用絕緣型供應器
  answer_index: 1
  explanation: 供應器的陽極(+)輸出必須維持獨立分路，嚴禁並聯連接 [B3]。
completion_criteria:
- 於實習中透過三用電表驗證 3 個獨立分路的 12V 電壓
- 確認 FSR 402 感測器分壓電路之接線與 ADC 輸入電壓範圍
- 提交並通過電源分路與保護設計報告
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

#### 1. 致動器選擇與電力特性
為實現機器人手的精密驅動，選擇 DYNAMIXEL XM430-W350-T。該致動器於 12V 額定電壓下運作，失速 (Stall) 電流為 2.3A [S11]。機器人手總體由 11 個致動器組成，總失速電流總和達約 25.3A。因此，為穩定驅動，需具備獨立的供電體系。

#### 2. 控制器架構
OpenCR 1.0 搭載 216MHz ARM Cortex-M7 處理器，適合即時控制 [S13]。此控制器支援將 12V 致動器電源與邏輯/感測器電源物理分離的結構。由於 FSR 感測器等類比輸入需在 0~3.3V 範圍內處理，感測器分壓電路務必連接至 OpenCR 的 3.3V 感測器導軌 [S13]。

#### 3. 過電流保護與電源分路設計
使用 3 個 138W 輸出的 MEAN WELL GST160A12-R7B 電源供應器 [S15]。各供應器額定電流為 11.5A，據此建立 3 個獨立的 12V 分路。各分路內置 10A ATOF 保險絲以在發生過電流時保護電路 [S24, S25]。保險絲設定需低於 11.5A 額定電流，以達成保護協調。

#### 4. 感測器訊號獲取
FSR 402 具備壓力增加則電阻減少的特性 [S12]。將其連接至 10kΩ 固定電阻構成電壓分壓器，將力量變化轉換為電壓訊號，輸入至 OpenCR 的 12bit ADC 連接埠 [S12, S13, S26]。
