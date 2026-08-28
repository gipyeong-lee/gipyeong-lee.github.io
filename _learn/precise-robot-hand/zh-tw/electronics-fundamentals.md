---
layout: learn-module
title: 電子電路基礎
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:electronics-fundamentals
translations:
- lang: ko
  url: /learn/precise-robot-hand/electronics-fundamentals/
- lang: en
  url: /learn/en/precise-robot-hand/electronics-fundamentals/
- lang: ja
  url: /learn/ja/precise-robot-hand/electronics-fundamentals/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/electronics-fundamentals/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/electronics-fundamentals/
module_id: m4
permalink: /learn/zh-tw/precise-robot-hand/electronics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 86f63f17be15487197f653755bdf316f
id: m4
slug: electronics-fundamentals
phase_id: p2
estimated_hours: 12.0
prerequisites:
- m3
objectives:
- 理解 DYNAMIXEL 智慧致動器的電氣特性與電源系統。
- 學習利用 FSR 402 感測器設計分壓電路與 ADC 訊號擷取。
- 設計系統過電流保護之熔斷器基礎電源分流。
- 熟練電子電路絕緣與物理隔離原則。
worked_examples:
- 範例 1：分流電流總合計算。若單一分流分配 4 台致動器（每台堵轉電流 2.3 A），理論最大電流為 9.2 A。此數值在 10 A 熔斷器額定內，且未超過供應器
  11.5 A 輸出極限，可安全運作 [S14, S17, S26]。
- 範例 2：FSR 分壓器輸出計算。當 FSR 受力使電阻變為 10 kΩ 時，分壓節點電壓為 3.3 V * (10 kΩ / (10 kΩ + 10 kΩ))
  = 1.65 V。此數值在 OpenCR 12 位元 ADC 的有效範圍內，可實現精密力回授 [S15, S16, S27]。
lab:
  title: 電源分流配置與感測器輸入測試
  steps:
  - 將各 MEAN WELL 供應器輸出線串聯 0AFH0001Z inline holder 與 10 A ATOF 熔斷器 [S17, S25, S26]。
  - 使用萬用電表測量各分流 12 V 電壓是否在正常範圍。
  - 利用 OpenCR 3.3 V 接腳、10 kΩ 電阻與 FSR 402 在麵包板上組成分壓電路 [S16, S27]。
  - 確認感測器電壓在 0~3.3 V 範圍內，並觀察受壓時的電壓變化。
  safety:
  - 維修與接近設備前，務必物理斷開 3 個電源供應器，並使用萬用電表確認各分流 DC 電壓低於 1 V。
  - 電路組成中嚴禁通電。電壓測量必須在所有接線完成並固定於夾具狀態下進行。
  - 隨時配戴抗衝擊作業護目鏡。
  - 絕不可混淆致動器電源 (12 V) 與感測器電源 (3.3 V)。
  deliverables:
  - 各電路電壓測量資料表
  - FSR 力感測器力-電壓反應曲線圖
  - 過電流保護用各分流熔斷器接線照片
assignment:
  title: 電源分配與感測器資料收集設計
  deliverables:
  - 致動器分流電力分配計畫書
  - 含 OpenCR ADC 電路圖之配線圖
  - 熔斷器額定選用邏輯報告
  rubric:
  - 電源分流合計電流符合各供應器容許範圍
  - FSR 電路僅連接至 3.3 V 感測器軌
  - 熔斷器額定選用足以適當執行過電流保護
quiz:
- question: 下列何者為電源分流配置時之禁止行為？
  choices:
  - 各分流串聯 10 A 熔斷器
  - 將獨立供應器之正極 (+) 端子並聯
  - 將致動器以 4:4:3 比例分配
  - 將 FSR 感測器連接至 3.3 V 軌
  answer_index: 1
  explanation: 各供應器輸出應作為獨立分流使用，將電源供應器輸出並聯恐導致系統故障與火災風險，絕對禁止。
- question: 組成 FSR 402 感測器電壓分壓電路時，正確之注意事項為何？
  choices:
  - 必須使用 12 V 致動器電源軌。
  - 必須使用 5 V 電源以提高 ADC 解析度。
  - 必須使用 OpenCR 的 3.3 V 感測器電源。
  - 必須在無電阻狀態下僅連接 FSR。
  answer_index: 2
  explanation: FSR 感測器電壓訊號不可超過 OpenCR ADC 輸入範圍 (0~3.3 V)，務必使用 3.3 V 感測器電源。
completion_criteria:
- 使用萬用電表證明所有電源分流電路電壓低於 1 V 且已物理斷開。
- 完成熔斷器安裝與 3.3 V 電源分壓電路建置。
- 確認 FSR 感測器訊號可於 OpenCR ADC 之 0~3.3 V 範圍內正常擷取。
source_ids:
- S6
- S9
- S14
- S17
- S26
- S25
- S15
- S27
- S16
---

若偵測到異常發熱、異味或冒煙，請勿靠近，並透過危險區域外的預設建物配電盤斷路器或認證的 upstream master disconnect 切斷 3 個供應器的電源後撤離。若危險區域外無可操作的 upstream 斷電手段，禁止系統通電。扭力解除不等於電源切斷。維修或接近設備必須在計畫停止後，物理斷開電源並確認無電後才可進行 [S14] [S17] [S26, S25] [S26] [S15] [S27] [S16]
