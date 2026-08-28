---
layout: learn-module
title: 肌腱驅動機制設計
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:tendon-driven-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/tendon-driven-design/
- lang: en
  url: /learn/en/precise-robot-hand/tendon-driven-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/tendon-driven-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/tendon-driven-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/tendon-driven-design/
module_id: M2
permalink: /learn/zh-tw/precise-robot-hand/tendon-driven-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 6d06f766b906424eb1f714f11e36dcf4
id: M2
slug: tendon-driven-design
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- 理解肌腱驅動機制的基本動力結構與關節模擬原理。
- 學習用於精密機器手的肌腱材料 (Dyneema SK78) 特性。
- 熟悉肌腱的張力傳遞路徑與絞盤設計時的摩擦及磨損防護方法。
- 計算致動器的失速扭力與肌腱驅動時的機械增益。
worked_examples:
- '範例 1：肌腱驅動時的張力計算

  當致動器扭力 (τ) 為 1 N·m，絞盤半徑 (r) 為 0.01 m 時，肌腱張力 (T) 為 T = τ/r = 1/0.01 = 100 N。設計時須考慮
  Dyneema SK78 相對於斷裂負載 230 daN（約 2300 N）的安全係數 [S16]。'
- '範例 2：電源分路分配與保護

  總共 11 台致動器的失速電流合計為 25.3 A [S11]。若分配至 3 個分路，分別為 4 台、 4 台、 3 台，各分路的最大負載分別為 9.2 A、
  9.2 A、 6.9 A。僅比較保險絲與負載/電源額定值無法保證安全性或動作順序。請審閱保險絲製造商的時間-電流曲線與電源 OCP 特性，以確認保護協調性 [S24,
  S25]。'
lab:
  title: 肌腱張力與關節摩擦測量實習
  steps:
  - 使用提供的連桿與軸承組裝手指關節模型。
  - 連接肌腱並使用張力調整器設定初始張力。
  - 將三用電表設為 DC 電壓模式，物理斷開各分路的 12 V 電源轉接器輸出進行確認。
  - 電源開啟前，手動測量並記錄關節旋轉摩擦力。
  safety:
  - 在維修或接近設備前，須將 3 個絕緣電源轉接器物理斷開，並使用三用電表確認 DC 電壓低於 1 V。
  - 電源開啟時，絕不可接近手指的可移動範圍。
  - 必須佩戴耐衝擊防護眼鏡。
  deliverables:
  - 隨關節旋轉角度的肌腱張力測量數據
  - 摩擦力分析報告
  - 最終安全測量紀錄
assignment:
  title: 5 機器手肌腱路徑設計
  deliverables:
  - 機器手指肌腱路徑 CAD 圖檔
  - 肌腱摩擦與損失計算書
  - 各分路電源負載分配與保險絲保護設計圖
  rubric:
  - 肌腱路徑設計是否已將彎曲處的摩擦最小化？
  - 是否考量了 Dyneema SK78 的物理特性？
  - 3 個電源分路的負載分配是否適當反映了致動器失速電流？
  - 保險絲及電源短路防護設計是否符合 BOM 規格？
quiz:
- question: 使用 Dyneema SK78 肌腱的主要優點為何？
  choices:
  - 因高延伸率產生的衝擊吸收
  - 極低的運作延伸率與高斷裂負載
  - 比金屬輕的重量與低抗拉強度
  - 導電性
  answer_index: 1
  explanation: Dyneema SK78 的延伸率低於 1%，運作極為精確，且為斷裂負載極高的高性能纖維 [S16]。
- question: 使用 3 個 12 V 電源轉接器（各 11.5 A）的原因何者最為適當？
  choices:
  - 為了用單一電源驅動所有致動器
  - 為了將電壓增幅至 36 V 以提高扭力
  - 為了分散並承載致動器的總峰值電流，並透過個別分路保險絲進行保護
  - 為了消除電源雜訊
  answer_index: 2
  explanation: 僅比較保險絲與負載/電源額定值無法保證安全性或動作順序。請審閱保險絲製造商的時間-電流曲線與電源 OCP 特性，以確認保護協調性 [S11,
    S15, S25]。
completion_criteria:
- 所有實習數據與圖檔必須包含於最終報告中。
- 物理斷開電源後，須以測量證明 3 個分路的 DC 電壓皆低於 1 V。
- 肌腱路徑設計必須包含考量絞盤摩擦的解析。
source_ids:
- S9
- S10
- S16
- S11
- S15
- S24
- S25
---

## 肌腱驅動機制基礎

肌腱驅動 (Tendon-driven) 系統是一種透過肌腱（繩索）將遠端致動器的張力傳遞至關節來驅動的方式 [S9]。模仿生物手指的肌腱結構，將致動器移動至手掌或前臂，可減輕手指本身的質量，並實現精密的動作 [S10]。

### 1. 肌腱的選擇與張力傳遞
本設計採用高強度、低延伸率的纖維 Dyneema SK78 [S16]。此材料在直徑 1.5 mm 時具有 230 daN（約 230 kgf）的斷裂負載，運作延伸率低於 1%，適合精密的位置控制 [S16]。

### 2. 機械增益與致動器選型
XM430-W350-T 智慧致動器可提供 4.1 N·m 的失速扭力 [S11]。肌腱透過旋轉軸的絞盤半徑進行力轉換，因此致動器的扭力輸出會置換為肌腱的張力。整個系統使用 11 台致動器，峰值電流總和可達約 25.3 A [S11]。僅比較保險絲與負載/電源額定值無法保證安全性或動作順序。請務必審閱保險絲製造商的時間-電流曲線與電源 OCP 特性，以確認保護協調性 [S15, S24, S25]。

### 3. 安全與保護設計
每個 12 V 電源分路均透過獨立保險絲運作 [S15, S24]。 3 個電源轉接器額定皆為 11.5 A，總電流容量達 34.5 A，足以負載系統峰值電流 25.3 A [S11, S15]。設計時應確保分路總額定值高於致動器總峰值電流，以確保操作安全性。
