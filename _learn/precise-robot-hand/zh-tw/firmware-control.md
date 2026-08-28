---
layout: learn-module
title: 韌體與控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:firmware-control
translations:
- lang: ko
  url: /learn/precise-robot-hand/firmware-control/
- lang: en
  url: /learn/en/precise-robot-hand/firmware-control/
- lang: ja
  url: /learn/ja/precise-robot-hand/firmware-control/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/firmware-control/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/firmware-control/
module_id: m7
permalink: /learn/zh-tw/precise-robot-hand/firmware-control/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 86f63f17be15487197f653755bdf316f
id: m7
slug: firmware-control
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- 理解 DYNAMIXEL 智慧致動器運作原理與控制協定 (Protocol 2.0)。
- 掌握 OpenCR 控制器結構，並建置感測器與致動器介面。
- 設計 FSR 電壓分壓電路與實現 ADC 訊號處理流程。
- 利用狀態機 (State Machine) 將機器手臂之抓取與控制邏輯編寫為韌體。
worked_examples:
- 範例 1：FSR ADC 數值常態化。當 FSR 感測器連接至 OpenCR ADC 並輸出 0~4095 (12 位元) 數值範圍時，編寫程式碼將其轉換為 0.0~1.0
  之力度比例。（公式：`normalized = adc_value / 4095.0`）
- 範例 2：XM430 位置控制指令。使用 DYNAMIXEL SDK 編寫將 1 號關節移動至 2048 (中間值) 的指令。使用如 `packetHandler->write2ByteTxRx(portHandler,
  1, ADDR_GOAL_POSITION, 2048, &error);` 之呼叫體系。
lab:
  title: 機器手臂韌體實作與感測器校正
  steps:
  - 透過 USB 將 OpenCR 1.0 控制板與電腦連結並設定基礎通訊環境 [S16]。
  - 將各手指之 FSR 分壓電路焊接連接至 OpenCR 之 3.3V 感測器電源軌 [S16, S27]。
  - 使用萬用電表確認 FSR 於無負載與受壓時之電壓在 0-3.3V 範圍內。
  - 於韌體讀取感測器數值並輸出至 Serial Monitor，確認物理接觸時之數值變化。
  - 將單一致動器與固定夾具連結，並透過控制程式進行精密移動測試。
  safety:
  - 切勿將 5V 或 12V 致動器電源軌直接連接至 ADC 感測電路 [S16]。
  - 通電前重新檢查配線圖，並以萬用電表確認是否短路。
  - 於致動器無負載狀態下進行初步運作測試。
  - 若偵測到異常發熱、異味或煙霧，請勿靠近，應於危險區域外利用預先指定的建築物配電盤斷路器或認證的 3 upstream master disconnect 切斷供應電源後進行撤離。若危險區域外無可操作的
    upstream 斷電手段，請禁止系統通電。釋放力矩 (torque release) 不能取代切斷電源。維修與進入僅限於計畫性停機、進行物理隔離並確認無電源測量後方可執行
    [S17]。
  - 存取前，請將 3 個電源變壓器物理斷開，並確認 DC 電壓模式下各分路的電壓小於 1V。
  deliverables:
  - 感測器數據輸出序列日誌 (Serial Log)
  - 動作測試及校準完成之韌體原始程式碼
  - ADC 正規化公式定義書
assignment:
  title: 5 隻機器手臂系統整合控制報告
  deliverables:
  - 狀態機設計圖及邏輯詳細說明書
  - 整體 11 個致動器及 5 個感測器整合控制韌體
  - 動作驗證影片及握力分析圖表
  rubric:
  - 狀態機是否安全地執行抓取與釋放迴圈？
  - 感測器數據是否無雜訊且穩定地獲取？
  - 各電源分支設計是否遵守 BOM 的獨立分支原則？
  - 是否遵守並記錄安全守則（如物理電源隔離等）？
quiz:
- question: 在 OpenCR 控制器中，為了 FSR 電壓分壓電路應使用哪種電源軌？
  choices:
  - 12V 致動器電源
  - 3.3V 感測器電源
  - 5V 電源
  - USB 5V
  answer_index: 1
  explanation: 根據 OpenCR 手冊與相容性標準，FSR 電壓分壓器應僅使用 3.3V 感測器電源軌 [S16]。
- question: 在致動器電源分支轉接器有 3 個的情況下，正確的電源連接方式為何？
  choices:
  - 將 3 個轉接器的正極 (+) 輸出並聯以增加電流容量。
  - 將各轉接器配置為獨立分支並通過保險絲。
  - 將所有致動器連接至 1 個轉接器，其餘作為備用。
  - 組合變壓器輸出，升壓至 36V 後使用。
  answer_index: 1
  explanation: 嚴禁並聯正極 (+) 輸出，各轉接器必須維持為獨立分支，並透過保險絲保護以防止過電流 [S17]。
- question: 在機器手臂系統維修或進入前必須執行的必要步驟為何？
  choices:
  - 僅下達軟體力矩釋放指令。
  - 移除保險絲。
  - 物理斷開 3 個電源，並使用萬用電表確認各分路電壓小於 1V。
  - 按下控制器的 Reset 按鈕。
  answer_index: 2
  explanation: 力矩釋放無法取代切斷電源，必須物理斷開 3 個轉接器，並透過 DC 電壓測量進行確認。
completion_criteria:
- 整合控制韌體於迴圈內執行 5 隻機器手臂的抓取動作。
- 所有感測器皆能在 0-3.3V 範圍內正常擷取 ADC 訊號。
- 所有電氣連接皆符合包含保險絲的獨立分支設計標準。
- 安全審查報告包含無電源測量確認紀錄。
source_ids:
- S16
- S14
- S15
- S27
- S17
---

## DYNAMIXEL 智慧致動器控制
機器人手的每個關節使用 XM430-W350-T 致動器驅動 [S14]。該致動器提供位置、速度、電流回授，並透過 DYNAMIXEL Protocol 2.0 控制 [S14]。控制器 OpenCR 1.0 搭載 216MHz ARM Cortex-M7 處理器，無需額外的通訊橋接器，可直接與致動器通訊 [S16]。

## ADC 與感測器介面
指尖接觸力使用 FSR 402 感測器測量 [S15]。FSR 具有隨施加力增加而電阻減小的特性 [S15]。OpenCR 的 ADC 輸入解析度為 12 位元 [S16]，使用 3.3V 感測器電源軌構成電壓分壓電路 [S16, S27]。

10 kΩ 下拉分壓器使用 $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$ 公式。

此處 $R_{fixed}$ 使用 10kΩ 電阻 [S27]。為了安全起見，所有類比訊號的設計皆應不超過 0-3.3V 範圍 [S16]。

## 韌體結構
機器人手的控制系統實作為「待機」、「執行抓取」、「維持抓取」、「釋放」的狀態機。韌體在迴圈中定期輪詢感測器值，並分析致動器的電流與位置數據，以維持穩定的抓取力。
