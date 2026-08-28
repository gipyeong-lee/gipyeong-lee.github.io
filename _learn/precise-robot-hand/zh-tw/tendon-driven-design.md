---
layout: learn-module
title: 肌腱驅動機制設計
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
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
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M2
slug: tendon-driven-design
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- 理解肌腱驅動機制的基本動力學結構與關節模擬原理。
- 學習用於精密機器人手的肌腱材料 (Dyneema SK78) 特性。
- 學習肌腱的張力傳遞路徑與絞盤設計時的摩擦及磨損防範法。
- 計算致動器的失速扭力與肌腱驅動時的機械增益。
worked_examples:
- "例題 1：肌腱驅動張力計算\n當致動器扭力 ($\tau$) 為 1 N·m 且絞盤半徑 ($r$) 為 0.01 m 時，肌腱張力 ($T$) 為 $T =\
  \ \tau/r = 1/0.01 = 100 N。設計時需考慮相對 Dyneema SK78 斷裂負荷 230 daN（約 2300 N）的安全係數 [S16]。"
- '例題 2：電源分路分配與保護

  總致動器 11 台的失速電流總和為 25.3 A [S11]。將其分配至 3 個分路中（分別為 4 台、 4 台、 3 台），各分路最大負載分別為 9.2 A、
  9.2 A、 6.9 A。4 台致動器分路的理論峰值 9.2 A 雖低於 10 A 保險絲與 11.5 A 電源額定，但此數值不能單獨確保安全性或動作順序。需同時檢視保險絲製造商的時間-電流曲線與電源供應器
  OCP 特性，確認保護協調 [S24, S25]。'
lab:
  title: 肌腱張力與關節摩擦測量實習
  steps:
  - 使用提供的連桿與軸承組裝手指關節模型。
  - 連接肌腱並使用張力器設定初始張力。
  - 將三用電表設定為 DC 電壓模式，物理斷開各分路的 12 V 電源供應器輸出進行確認。
  - 通電前手動測量並記錄關節旋轉摩擦力。
  safety:
  - 維修或接近設備前，物理斷開 3 個絕緣電源供應器，並使用三用電表確認 1 V 以下之 DC 電壓。
  - 通電期間絕對不得接近手指可活動範圍。
  - 必須佩戴防撞護目鏡。
  deliverables:
  - 隨關節旋轉角度變化的肌腱張力測量數據
  - 摩擦力分析報告
  - 最終安全計量紀錄
assignment:
  title: 5 機器人手肌腱路徑設計
  deliverables:
  - 機器人手指肌腱路徑 CAD 圖面
  - 肌腱摩擦與損失計算書
  - 各分路電源負載分配與保險絲保護設計圖
  rubric:
  - 肌腱路徑設計是否將彎曲部摩擦降至最低？
  - 是否考量 Dyneema SK78 的物理特性？
  - 3 個電源分路的負載分配是否適切反映了致動器失速電流？
  - 保險絲與電源短路防護設計是否遵守 BOM 規格？
quiz:
- question: 使用 Dyneema SK78 肌腱的主要優點為何？
  choices:
  - 高伸長率帶來的衝擊吸收能力
  - 極低的運作伸長率與高斷裂負荷
  - 較金屬輕的重量與低抗拉強度
  - 電導性
  answer_index: 1
  explanation: Dyneema SK78 的伸長率極低（小於 1%），可提升位置控制精度，且具備極高的斷裂負荷 [S16]。
- question: 使用 3 個 12 V 電源供應器（各 11.5 A）的原因，何者最為適切？
  choices:
  - 為了使用單一電源驅動所有致動器
  - 為了將電壓升壓至 36 V 以提升扭力
  - 為了分散處理致動器的總峰值電流並透過個別分路保險絲保護
  - 為了消除電源雜訊
  answer_index: 2
  explanation: 為了安全分散總計 11 台致動器的峰值電流，並透過各分路 10 A 保險絲保護，降低系統過電流風險 [S11, S15, S25]。
completion_criteria:
- 所有實習數據與圖面必須包含於最終報告中。
- 物理斷開電源後，需驗證 3 個分路的 DC 電壓低於 1 V。
- 肌腱路徑設計中需包含考量絞盤摩擦的分析。
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

肌腱驅動 (Tendon-driven) 系統是透過遠端的致動器，經由肌腱（線）將張力傳遞至關節進行驅動的方式 [S9]。模仿生物手指的肌腱結構，將致動器移動至手掌或前臂，藉此減輕手指自身的質量並實現精密的動作 [S10]。

### 1. 肌腱選擇與張力傳遞
本設計使用高強度低伸長率纖維 Dyneema SK78 [S16]。此材料在直徑 1.5 mm 時具有 230 daN（約 230 kgf）的斷裂負荷，操作伸長率小於 1%，適合精密位置控制 [S16]。

### 2. 機械增益與致動器選擇
XM430-W350-T 智慧致動器提供 4.1 N·m 的失速扭力 [S11]。由於肌腱透過絞盤半徑從旋轉軸轉換力量，致動器的扭力輸出會轉換為肌腱張力。全系統使用 11 台致動器，峰值電流總和最高可達 25.3 A [S11]。因此，為穩定供應，規劃了總計 3 個獨立的 12 V 電源分路，各分路透過獨立的 10 A 保險絲保護以防止過電流 [S15, S24, S25]。

### 3. 安全與保護設計
每個 12 V 電源分路均透過獨立保險絲運作 [S15, S24]。3 個電源供應器各具備 11.5 A 額定值，合計電流容量達 34.5 A，足以涵蓋系統 25.3 A 的峰值電流 [S11, S15]。分路總額定值設計為超過致動器總峰值電流，以確保運作安全。
