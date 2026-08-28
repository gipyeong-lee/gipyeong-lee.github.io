---
layout: learn-module
title: 韌體開發與控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:firmware-development
translations:
- lang: ko
  url: /learn/precise-robot-hand/firmware-development/
- lang: en
  url: /learn/en/precise-robot-hand/firmware-development/
- lang: ja
  url: /learn/ja/precise-robot-hand/firmware-development/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/firmware-development/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/firmware-development/
module_id: M7
permalink: /learn/zh-tw/precise-robot-hand/firmware-development/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- 理解 DYNAMIXEL 智慧致動器通訊與控制架構。
- 實現應用 OpenCR 控制板之致動器與 FSR 感測器訊號獲取。
- 設計即時機器人控制狀態機與閉迴路回饋迴路。
- 規劃安全電源管理與扭力釋放序列程式設計。
worked_examples:
- 1. 致動器目標位置/電流設定：使用 DYNAMIXEL SDK 設定 XM430 致動器之電流限制 (Goal Current)，並透過 PID 迴路根據感測器數值更新手指關節最終位置的範例。
- 2. FSR 電壓數據濾波：為去除 ADC 原始數據雜訊，套用移動平均濾波器 (Moving Average Filter)，並將上限 (20N) 與下限 (0.2N)
  範圍正規化的程式實作 [S12]。
lab:
  title: 機器人手整合控制與精密抓取實習
  steps:
  - 確認各獨立分路電壓低於 1V 後方可開始組裝。
  - 於 OpenCR 之 3.3V 感測器導軌焊接 FSR 分壓電路並連接至 ADC 埠。
  - 使用 DYNAMIXEL SDK 掃描 11 台致動器 ID 並設定初始位置。
  - 在無負載狀態測試手指關節驅動命令，調整肌腱伸長率與張力。
  - 透過序列埠監控器視覺化 FSR 感測器數據，微調抓取力回饋反應。
  safety:
  - 絕對不可將 5V 或 12V 致動器電源用於 FSR 感測器電路。
  - 系統通電中絕對不可接近手指活動範圍，應使用固定夾具。
  - 絕對不可將電源分路供應器的陽極(+)連接在一起。
  - 在維修或組裝存取前，必須物理斷開 3 個電源供應器，並以儀表確認各分路低於 1V。
  deliverables:
  - 包含即時感測器數據回饋的韌體原始程式碼
  - 電壓分壓數據正規化與校正數據表
  - 致動器回饋迴路正常運作紀錄
assignment:
  title: 抓取狀態機設計與實現
  deliverables:
  - 抓取與解除抓取狀態機圖表
  - 實現基於電流之扭力控制程式碼
  - 最終效能評估報告
  rubric:
  - 根據感測器數值的電流限制範圍 (0-2.3A) 是否穩定受控？
  - 在執行扭力釋放指令時，物理張力是否立即解除？
  - 程式碼中是否明確記載了安全的硬體隔離程序？
quiz:
- question: 配置 FSR 402 感測器與分壓電路時，建議的電源軌為何？
  choices:
  - 12V 致動器電源軌
  - 5V 通用電源軌
  - OpenCR 3.3V 感測器軌
  - 24V 外部輸入軌
  answer_index: 2
  explanation: 為了系統安全與保護 OpenCR ADC，FSR 分壓電路必須連接至 3.3V 感測器電源軌。
- question: 維護機器手時，確認系統處於「無電源狀態」的正確方法為何？
  choices:
  - 透過軟體發送扭力釋放指令。
  - 使用三用電表電阻檔位檢查接線狀態。
  - 使用三用電表 DC 電壓檔位測量所有分支電壓是否低於 1V。
  - 拆除電源分支保險絲。
  answer_index: 2
  explanation: 物理斷電後，務必使用三用電表 DC 電壓檔位直接確認所有分支的殘餘電壓是否低於 1V。
- question: 是否可以將多個獨立電源供應器輸出的正極(+)端並聯連接？
  choices:
  - 為了電流加總需要這麼做。
  - 絕對禁止。
  - 若額定輸出電流相同則可以。
  - 若裝設保險絲則可以。
  answer_index: 1
  explanation: 構成獨立分支的電源供應器，其正極(+)輸出絕對不可互相連接或整合。
completion_criteria:
- 已使用三用電表驗證各分支獨立供電及保險絲保護配置符合 BOM 規範
- 確認已透過 OpenCR ADC 取得並濾波 5 個 FSR 感測器的精確力訊號
- 確實執行軟體扭力釋放常式與物理斷電後的測量程序
- 抓取狀態機已按預期處理致動器與感測器資料，並提交最終報告
source_ids:
- S13
- S11
- S12
---

### 韌體架構與 DYNAMIXEL 控制
機器人手的韌體在高頻迴路中取得感測器數據並處理致動器命令。`OpenCR 1.0` 控制器基於 216MHz ARM Cortex-M7 處理器 [S13]，直接處理 DYNAMIXEL 通訊協定 2.0 [S11] 以極小化延遲。各致動器支援電流、速度與位置模式，機器人手採用基於電流控制的扭力抓取策略。

### FSR 力量回饋系統
FSR 402 感測器電阻與所施力量成反比 [S12]。使用 OpenCR 的 12 bit ADC [S13]，於 3.3V 感測器導軌配置 10kΩ 電阻分壓電路。分壓後電壓透過 `ADC值 = (V_in * R_fsr) / (R_fsr + R_ref)` 正規化，此數值與肌腱張力連動，用作抓取力回饋。

### 安全控制常規
為求安全，系統停止分為兩階段。軟體階段將致動器扭力釋放 (Torque Off) 以消除物理驅動力。維修前務必物理斷開 3 個獨立電源供應器，並使用三用電表 DC 模式驗證所有分路低於 1V。
