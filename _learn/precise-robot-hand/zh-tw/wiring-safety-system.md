---
layout: learn-module
title: 配線與安全電源分離建構
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
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M6
slug: wiring-safety-system
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M5
objectives:
- 理解為致動器驅動配置獨立 12 V 電源分路的方法。
- 學習用於過電流保護之 ATOF 保險絲的角色與選定原理。
- 習得安全電源管理與物理斷電協定。
- 配置 OpenCR 控制器與 FSR 感測器的安全分壓電路。
worked_examples:
- 偵測到異常發熱、異味或冒煙時，請勿靠近，並由危險區域外切斷建築配電盤斷路器或認證的 upstream master disconnect 以中斷 3 個電源供應器之供電。若危險區域外無可操作的
  upstream 斷電手段，禁止系統通電。扭力釋放不可取代電源切斷。維修或接近設備必須在計畫性停止後物理斷開並驗證無電源狀態 [S11] [S25]
- 例題 2：FSR ADC 電路電壓 - 使用 OpenCR 的 3.3 V 感測器導軌連接 10 kΩ 分壓電阻與 FSR 402 [S13, S26]。感測器訊號電壓需位於
  0~3.3 V 範圍內，此電路必須與 12 V 致動器電源電路在物理上與電氣上分離。
lab:
  title: 電源分路線束製作與安全點檢
  steps:
  - 各供應器輸出端焊接 ATO 線型保險絲座，並插入 10 A ATOF 保險絲 [S24, S25]。
  - 使用 Molex Micro-Fit 3.0 接頭製作致動器與感測器連接線束 [S14]。
  - 將 OpenCR 板與各致動器以 3 個分路分配配線，並連接至各供應器 [S13]。
  - 通電前，使用三用電表電阻模式確認各供應器輸出端之絕緣狀態。
  - 通電後，於電壓模式確認各分路為 12 V，斷電時務必拆除 3 個供應器。
  safety:
  - 維修前物理斷開 3 個電源供應器。
  - 殘留電壓低於 1 V 經三用電表確認後方可更換零件。
  - 通電中不可將手伸入活動範圍。
  - 所有接點應完成絕緣處理，焊接時須佩戴護目鏡。
  deliverables:
  - 製作完成之電源分路線束照片
  - 各分路測量電壓紀錄單
  - 配線圖審查確認書
assignment:
  title: 安全配線設計報告
  deliverables:
  - 3 個電源分路致動器分配設計案 (每分路 4/4/3 台)
  - 各分路過電流切斷計算書 (峰值電流與保險絲額定比較)
  - 計畫性停止後維修或接近設備前，必須物理斷開 3 個電源供應器，並以儀表確認處於無電源狀態
  rubric:
  - 是否遵守電源獨立與分離原則？
  - 保險絲與連接頭規格是否適宜負載？
  - 電源分離與殘留電壓確認協定是否符合安全指導？
quiz:
- question: 各電源供應器的 12 V 輸出(+)是否可並聯使用？
  choices:
  - 可以，電流供應能力提升。
  - 不行，必須維持獨立分路。
  - 只要電壓相同即可。
  - 只要加上保險絲即可。
  answer_index: 1
  explanation: 各供應器輸出必須維持獨立，絕對禁止並聯連接 [S15]。
- question: 機器人手維修前最重要的安全措施為何？
  choices:
  - 軟體扭力釋放
  - 三用電表電阻測量
  - 物理斷開 3 個電源供應器並確認殘留電壓
  - 按下計畫性停止鈕
  answer_index: 2
  explanation: 維修前務必物理斷開 3 個電源供應器，並以三用電表確認各分路殘留電壓低於 1 V。
- question: FSR 力量感測器 ADC 電路應使用哪種電源導軌？
  choices:
  - 12 V 致動器導軌
  - 5 V 電源導軌
  - 3.3 V 感測器導軌
  - 24 V 電源導軌
  answer_index: 2
  explanation: 為保護 OpenCR ADC 電路，必須使用 3.3 V 感測器導軌 [S13]。
completion_criteria:
- 完成 3 個獨立分路線束配置與保險絲安裝
- 確認各分路無負載時電壓測量為 12 V
- 物理斷開電源後，紀錄所有測量節點殘留電壓皆低於 1 V
- 提交並通過配線安全設計報告
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

## 安全接線與電源分離原則

5支機器手系統使用多個高扭力致動器，因此高效且安全的電源分配至關重要。本專案使用 11 個電源變壓器，將致動器按 4 台/4 台/3 台為單位分組配置，旨在分散各分路的電流負載並提升電源穩定性 [S15]。

### 1. 電源獨立性確保
各變壓器的正極(+)輸出必須保持獨立分路，嚴禁任意合併或捆綁。設計上需確保在 [S15] 所述之變壓器額定輸出電流(11.5 A)內，能容納致動器峰值電流(XM430-W350-T 1 台總計 2.3 A) [S11]。4 台分組之峰值電流總和為 9.2 A，在變壓器之連續輸出容許範圍內。

### 2. 過電流保護 (Protection Coordination)
各分路配置 10 A ATOF 保險絲，以保護系統免受配線或致動器故障時產生之過電流損害 [S25]。由於 ATOF 保險絲於額定電流之 110%~135% 水準動作，故能針對 9.2 A 之峰值電流提供穩定保護。惟保險絲之選定務必參考製造商提供之「時間-電流曲線」(Time-Current Curve)，負載電流低不代表絕對安全 [S25]。

### 3. 控制電路分離
使用內建 DYNAMIXEL 連接埠之 OpenCR 控制板，移除複雜外部橋接電路，以提升重現性 [S13]。FSR 力感測器為將電壓轉換為 ADC 輸入，採用由 3.3 V 感測器軌供電之分壓電路，且必須與 12 V 致動器電源在電氣上隔離 [S13]。

### 4. 作業安全須知
由於桌面原型並非認證之機械安全系統，進行維修或修改作業前，務必物理性拔除 3 個電源變壓器，並使用三用電表之直流電壓模式確認各分路之殘餘電壓低於 1 V [S7]。
