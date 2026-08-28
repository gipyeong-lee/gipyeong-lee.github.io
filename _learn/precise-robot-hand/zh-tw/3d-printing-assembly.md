---
layout: learn-module
title: 3D 列印與零件加工
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:3d-printing-assembly
translations:
- lang: ko
  url: /learn/precise-robot-hand/3d-printing-assembly/
- lang: en
  url: /learn/en/precise-robot-hand/3d-printing-assembly/
- lang: ja
  url: /learn/ja/precise-robot-hand/3d-printing-assembly/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/3d-printing-assembly/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/3d-printing-assembly/
module_id: M4
permalink: /learn/zh-tw/precise-robot-hand/3d-printing-assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 6d06f766b906424eb1f714f11e36dcf4
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- 理解使用碳纖維強化 PC 線材 (PC-CF) 進行零件製作與最佳化列印設定。
- 習得熱壓入嵌件 (Heat-set insert) 與套筒軸承的精密組裝公差管理。
- 理解用於肌腱驅動機制的 Dyneema 線材處理與絞盤設計結構。
- 熟練確保機器人結構尺寸穩定性與剛性的加工與緊固技術。
worked_examples:
- 範例 1：PC-CF 線材噴嘴選擇 - 考量碳纖維的高磨蝕性，Brass (黃銅) 噴嘴會迅速磨損導致輸出品質下降與噴嘴阻塞，因此必須確認選用硬化鋼 (Hardened
  steel) 噴嘴 [S19]。
- 範例 2：嵌件孔設計 - Accu HTBI-M3-BR 嵌件外徑為 4.4mm，但官方推薦孔徑為 4.0mm [S21]，故 CAD 設計時將孔徑固定為 4.0mm，以利熱壓入時塑膠能充分滲入嵌件紋路
  (knurling) [S21]。
lab:
  title: 手指結構製作與組裝實習
  steps:
  - 設定配備硬化鋼噴嘴的 FDM 3D 列印機進行碳纖維 PC 線材列印環境 [S19]。
  - 輸出手指連桿與手掌框架後，進行支撐去除與表面整理。
  - 使用熱工具將熱壓入嵌件垂直安放於 4.0mm 導引孔 [S21]。
  - 依照軸承規格切割 IGUS 精密鋁合金軸並進行末端倒角 [S18]。
  - 將套筒軸承壓入殼體後，插入軸以確認間隙 [S17]。
  - 使用 M3 帽頭螺絲鎖固結構件與感測器支架 [S20]。
  safety:
  - 注意高溫噴嘴 (285°C) 與底板 (110°C) 造成的燙傷風險 [S19]。
  - 進行輸出件後加工與倒角時，務必佩戴防護眼鏡。
  - 嵌件加熱時可能產生煙霧，請啟動通風設備。
  - 通電前請確認所有機械緊固狀態。
  deliverables:
  - 製作完成的 5 機器手結構件（連桿、手掌）。
  - 熱壓入嵌件垂直度與軸承間隙測量紀錄。
  - 最終緊固部位肉眼檢測完成報告。
assignment:
  title: 機器手製作精度驗證
  deliverables:
  - 完成結構件的 CAD 數據與實際尺寸測量比較表
  - 組裝公差管理計畫書
  - 肌腱繞線結構的減摩擦設計說明書
  rubric:
  - 熱壓入嵌件是否垂直安放（優/良/差）
  - 軸-軸承組裝後是否能平順旋轉（合格/不合格）
  - 是否遵守 BOM 表中所列零件額定與型號規格 [B10, B11, B12, B13, B14]
quiz:
- question: 使用 PC-CF 線材時，必須使用硬化鋼噴嘴的主要原因為何？
  choices:
  - 為了防止碳纖維磨蝕性導致黃銅噴嘴快速磨損
  - 因線材熔點低，一般噴嘴無法列印
  - 為了增加輸出件表面光澤
  - 為了提高擠出速度
  answer_index: 0
  explanation: 碳纖維具有極高的磨蝕性，會迅速破壞一般黃銅噴嘴，故必須使用硬化鋼噴嘴 [S19]。
- question: 使用 M3 熱壓入嵌件 (Accu HTBI-M3-BR) 時，推薦的導引孔直徑為何？
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: 根據官方資料手冊，推薦的孔徑為 4.0mm [S21]。
completion_criteria:
- 所有結構零件皆已使用 FDM 3D 列印機製作完成 [B10]
- 熱壓入嵌件皆準確安放於所有指定孔位 [B14]
- 鋁合金軸與套筒軸承的組裝間隙符合基準值 [B11, B12]
- 緊固時正確使用了 BOM 規定的 M3 帽頭螺絲 [B13]
source_ids:
- S19
- S21
- S17
- S18
- S16
- S20
---

### 3D 列印與零件加工理論

#### 碳纖維強化工程材料 (PC-CF)
PC (Polycarbonate) 具備優異的剛性與耐熱性，添加碳纖維後的 PC-CF 線材更能將剛性最大化，適合製作結構用零件 [S19]。然而，由於碳纖維的磨蝕性，務必使用硬化鋼噴嘴 [S19]，且需在 285°C 左右的高溫下輸出 [S19]。

#### 為了精密組裝的嵌件與緊固
為了讓塑膠輸出件能進行重複的組裝與拆卸，採用熱壓入螺紋嵌件 [S21]。針對 M3 嵌件，CAD 設計時需預留 4.0mm 直徑的導引孔，以確保安放於精確位置 [S21]。此外，免潤滑聚合物套筒軸承 (iglide J) 與 8mm 鋁合金軸組裝時，壓入後內徑需達到最佳間隙，且與軸徑 8mm 的公差管理至關重要 [S17, S18]。

#### 肌腱驅動結構
Dyneema SK78 纖維在直徑 1.5mm 時具有 230 daN 的高斷裂負載與低於 1% 的延伸率 [S16]，是鋼纜的優質替代品。由於肌腱在旋轉軸上會反覆彎曲，絞盤邊緣需進行圓角處理，以防止因摩擦導致斷裂的結構設計至關重要。
