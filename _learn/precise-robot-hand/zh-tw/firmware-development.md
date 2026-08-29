---
layout: learn-module
title: 韌體開發與控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-tw
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
translation_run_id: 6d06f766b906424eb1f714f11e36dcf4
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- 理解 DYNAMIXEL 智慧致動器通訊與控制框架。
- 實現利用 OpenCR 控制板進行致動器與 FSR 感測器訊號獲取。
- 設計即時機器人控制狀態機與閉迴路回饋迴路。
- 編寫安全電源管理與扭力解除序列程式。
worked_examples:
- 1. 致動器目標位置/電流設定：使用 DYNAMIXEL SDK 設定 XM430 致動器的電流限制 (Goal Current)，並透過根據感測器值產生的 PID
  迴路來更新手指關節最終位置的範例。
- 2. FSR 電壓數據濾波：為去除 ADC 採集之原始數據雜訊，採用移動平均濾波器 (Moving Average Filter)，並將上限 (20N) 與下限
  (0.2N) 範圍正規化的程式實作 [S12]。
lab:
  title: 機器手整合控制與精密抓握實習
  steps:
  - 以三用電表 DC 模式確認各獨立分路電壓低於 1V 後，方可開始組裝。
  - 於 OpenCR 的 3.3V 感測器軌上烙接 FSR 電壓分壓電路並連接至 ADC 埠。
  - 使用 DYNAMIXEL SDK 掃描 11 台致動器 ID 並設定初始位置。
  - 無負載狀態下測試手指關節驅動指令，調整肌腱延伸率與張力。
  - 利用序列監控視窗視覺化 FSR 感測器數據，微調抓握力響應。
  safety:
  - 絕不可將 5V 或 12V 致動器電源作為 FSR 感測器電路的供電電源。
  - 系統通電時，絕不可將手置於手指可移動範圍內，並務必使用固定夾具。
  - 轉接器分路的陽極(+)端子絕不可彼此連接。
  - 維修/組裝接近前，必須物理斷開 3 個電源轉接器，並以儀器確認各分路電壓低於 1V。
  deliverables:
  - 包含即時感測器數據回饋的韌體原始程式碼
  - 電壓分壓數據正規化與校準數據表
  - 致動器回饋迴路正常運作紀錄檔
assignment:
  title: 抓握狀態機設計與實作
  deliverables:
  - 抓握與釋放狀態機圖表
  - 電流基礎扭力控制實作程式碼
  - 最終性能評估報告
  rubric:
  - 依據感測器數值，電流限制範圍 (0-2.3A) 是否穩定控制？
  - 當發出扭矩釋放命令時，物理張力是否會立即解除？
  - 代碼中是否明確規定了安全的硬件隔離程序？
quiz:
- question: 配置 FSR 402 傳感器和分壓電路時，推薦的電源軌是什麼？
  choices:
  - 12V 執行器電源軌
  - 5V 通用電源軌
  - OpenCR 3.3V 傳感器電源軌
  - 24V 外部輸入電源軌
  answer_index: 2
  explanation: 為了系統安全和保護 OpenCR ADC，FSR 分壓電路必須連接到 3.3V 傳感器電源軌。
- question: 維護機器手時，確認系統處於「無電狀態」的正確方法是什麼？
  choices:
  - 通過軟件發送扭矩釋放命令。
  - 使用萬用表電阻模式檢查接線狀態。
  - 使用萬用表直流電壓模式測量所有分支，確認電壓低於 1V。
  - 拆除電源分支保險絲。
  answer_index: 2
  explanation: 物理斷電後，必須使用萬用表直流電壓模式直接確認所有分支的殘餘電壓低於 1V。
- question: 可以將多個獨立電源適配器的正極(+)輸出並聯連接嗎？
  choices:
  - 為了電流疊加，這是必要的。
  - 絕對禁止。
  - 如果額定輸出電流相同，則可以。
  - 如果安裝了保險絲，則可以。
  answer_index: 1
  explanation: 絕對禁止將構成獨立分支的電源適配器的正極(+)輸出互相連接或集成。
completion_criteria:
- 使用萬用表驗證各分支獨立供電及保險絲保護已按 BOM 規範配置完成
- 確認通過 OpenCR ADC 精確獲取並過濾 5 個 FSR 傳感器的力信號
- 完全執行軟件扭矩釋放程序及物理斷電後的測量程序
- 抓取狀態機按預期處理執行器與傳感器數據，並提交最終報告
source_ids:
- S13
- S11
- S12
---

### 韌體架構與 DYNAMIXEL 控制
機器手的韌體於高速迴路中進行感測器數據採集並處理致動器指令。 `OpenCR 1.0` 控制器以 216MHz ARM Cortex-M7 處理器為核心 [S13]，無需外部橋接即可處理 DYNAMIXEL 協定 2.0 [S11]，將延遲減至最低。各致動器支援電流、速度、位置模式，機器手採用透過電流控制的扭力基礎抓握策略。

### FSR 力回饋系統
FSR 402 感測器具有與施加力成反比的電阻特性 [S12]。利用 OpenCR 的 12 位元 ADC [S13]，在 3.3V 感測器軌上架設 10kΩ 電阻與分壓電路。分壓電壓透過 `ADC值 = (V_in * R_fsr) / (R_fsr + R_ref)` 進行正規化，此數值將與手指肌腱張力連動，作為抓握力回饋使用。

### 安全控制例程
為確保安全，系統停止分為兩階段。軟體階段解除致動器扭力 (Torque Off) 以即時移除物理驅動力。維修前務必物理斷開 3 個獨立電源轉接器，並使用三用電表 DC 模式確認各分路皆低於 1V。
