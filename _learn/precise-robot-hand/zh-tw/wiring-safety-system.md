---
layout: learn-module
title: 配線與安全電源分路建構
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:wiring-safety-system
translations:
- lang: ko
  url: /learn/precise-robot-hand/wiring-safety-system/
- lang: en
  url: /learn/en/precise-robot-hand/wiring-safety-system/
- lang: ja
  url: /learn/ja/precise-robot-hand/wiring-safety-system/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/wiring-safety-system/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/wiring-safety-system/
module_id: M6
permalink: /learn/zh-tw/precise-robot-hand/wiring-safety-system/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 6d06f766b906424eb1f714f11e36dcf4
id: M6
slug: wiring-safety-system
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M5
objectives:
- 理解為驅動致動器配置獨立 12 V 電源分路的方法。
- 學習 ATOF 保險絲在過電流保護中的角色與選用原理。
- 習得安全電源管理與物理斷電協定。
- 建構 OpenCR 控制器與 FSR 感測器的安全電壓分壓電路。
worked_examples:
- 若偵測到異常發熱、氣味或煙霧，請勿靠近，並由危險區域外透過指定的建築配電盤斷路器或經認證的 upstream master disconnect 切斷 3 個轉接器的電源後撤離。若危險區域外無可操作的
  upstream 斷電手段，禁止系統通電。扭力解除不能代替切斷電源。維修與接近須在計畫停止後，確認物理斷開並驗證無電狀態下執行 [S11] [S25]。
- 範例 2：FSR ADC 電路電壓 - 使用 OpenCR 的 3.3 V 感測器軌連接 10 kΩ 分壓電阻與 FSR 402 [S13, S26]。感測器訊號電壓須保持在
  0~3.3 V 範圍內，且此電路必須與 12 V 致動器電源電路物理/電氣分離以進行保護。
lab:
  title: 電源分路線束製作與安全檢查
  steps:
  - 於每個轉接器輸出端烙接 ATO 串聯式保險絲座，並插入 10 A ATOF 保險絲 [S24, S25]。
  - 使用 Molex Micro-Fit 3.0 連接器製作致動器與感測器連接線束 [S14]。
  - 將 OpenCR 板與各致動器以 3 個分路分配佈線，並連接至各電源轉接器 [S13]。
  - 電源開啟前，以三用電表電阻模式檢查各轉接器輸出端子的絕緣狀態。
  - 電源開啟後，於電壓模式確認各分路皆為 12 V，斷電時務必移除所有 3 個轉接器。
  safety:
  - 維修前請將 3 個電源轉接器物理斷開。
  - 確認殘留電壓低於 1 V 後，方可更換零件。
  - 電源開啟時，手部勿置於可移動範圍內。
  - 所有接線處皆需絕緣，烙鐵作業時請佩戴防護眼鏡。
  deliverables:
  - 製作完成的電源分路線束照片
  - 各分路測量電壓紀錄表
  - 配線圖審核確認書
assignment:
  title: 安全配線設計報告
  deliverables:
  - 3 個電源分路的致動器配置設計方案（每分路 4 台/4 台/3 台）
  - 各分路過電流截斷計算書（峰值電流與保險絲額定比較）
  - 計畫停止後，維修與接近前將 3 個轉接器物理斷開，並確認各分路無電狀態的執行紀錄
  rubric:
  - 是否遵守電源獨立性與分離原則？
  - 保險絲與連接器額定是否符合負載？
  - 電源分離與殘留電壓確認協定是否符合安全指引？
quiz:
- question: 是否可將各電源轉接器的 12 V 輸出(+)並聯？
  choices:
  - 可以，電流供應能力會提高。
  - 不行，必須維持獨立分路。
  - 電壓一致時即可。
  - 加裝保險絲即可。
  answer_index: 1
  explanation: 各轉接器輸出必須保持獨立，絕對禁止並聯 [S15]。
- question: 機器手維護前，最優先執行的安全措施為何？
  choices:
  - 軟體扭力解除
  - 三用電表電阻測量
  - 3 個電源轉接器的物理斷開與殘留電壓確認
  - 按下計畫停止按鈕
  answer_index: 2
  explanation: 維修前務必物理斷開 3 個電源轉接器，並以三用電表確認殘留電壓低於 1 V。
- question: FSR 力感測器 ADC 電路應使用哪種電源軌？
  choices:
  - 12 V 致動器軌
  - 5 V 電源軌
  - 3.3 V 感測器軌
  - 24 V 電源軌
  answer_index: 2
  explanation: 為了保護 OpenCR 的 ADC 電路，必須使用 3.3 V 感測器軌 [S13]。
completion_criteria:
- 3 個獨立分路線束建構及保險絲安裝完成
- 各分路無負載電壓實測為 12 V
- 物理斷開電源後，所有測量節點殘留電壓皆小於 1 V 並完成紀錄
- 配線安全設計報告提交並通過
source_ids:
- S14
- S24
- S25
- S7
- S15
- S11
- S13
- S26
---

## 安全配線與電源分離原理

5 機器手系統使用了多個高扭力致動器，因此高效且安全的電源分配至關重要。本專案使用 11 個電源轉接器，將致動器以 4 台/4 台/3 台為單位分路佈置，旨在分散各分路的電流負載並提升電源穩定性 [S15]。

### 1. 電源獨立性確保
各轉接器的陽極(+)輸出必須維持獨立分路，嚴禁任意合線或綑綁。請在 [S15] 明示的轉接器額定輸出電流 (11.5 A) 範圍內，承載致動器峰值電流（XM430-W350-T 每 1 台 2.3 A）[S11]。 4 台單位分路的峰值電流合計為 9.2 A，在轉接器的連續輸出允許範圍內。

### 2. 過電流保護 (Protection Coordination)
於每個分路配置 10 A ATOF 保險絲，以保護線路或致動器異常時的過電流 [S25]。僅比較保險絲與負載/電源額定值無法保證安全性或動作順序。請審閱保險絲製造商的時間-電流曲線與電源 OCP 特性，以確認保護協調性。保險絲選用務必參考製造商提供的「Time-Current Curve」，且非負載電流低即代表安全 [S25]。

### 3. 控制電路分離
使用 DYNAMIXEL 連接埠內建的 OpenCR 控制板，藉由移除複雜的外部橋接電路來提升重現性 [S13]。FSR 力感測器為將電壓轉換為 ADC 輸入，須使用 3.3 V 感測器軌的供電分壓電路，並須與 12 V 致動器電源電氣分離 [S13]。

### 4. 作業安全守則
由於工作檯原型並非經認證的機械安全系統，在維修或修正作業前，務必物理斷開 3 個電源轉接器，並以三用電表 DC 電壓模式確認各分路殘留電壓低於 1 V [S7]。
