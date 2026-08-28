---
layout: learn-module
title: 3D 列印與零件加工
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
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
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- 理解使用碳纖維強化 PC 耗材 (PC-CF) 製作零件及最佳化列印設定。
- 學習熱壓入嵌件 (Heat-set insert) 與套筒軸承的精密組裝公差管理。
- 理解用於肌腱驅動機制的 Dyneema 線材處理與絞盤結構設計。
- 習得確保機器人結構體尺寸穩定性與剛性的加工與緊固技巧。
worked_examples:
- 例題 1：PC-CF 耗材噴嘴選擇 - 考量碳纖維的高磨耗性，黃銅 (Brass) 噴嘴會迅速磨損導致列印品質下降與阻塞，務必確認選擇硬化鋼 (Hardened
  steel) 噴嘴 [S19]。
- 例題 2：嵌件孔設計 - Accu HTBI-M3-BR 嵌件外徑為 4.4mm，但官方建議孔徑為 4.0mm [S21]，因此 CAD 設計時將孔徑固定為 4.0mm，確保熱壓入時塑膠能充分進入嵌件滾花
  (knurling) 之間 [S21]。
lab:
  title: 手指結構製作與組裝實習
  steps:
  - 設定安裝硬化鋼噴嘴之 FDM 3D 印表機的碳纖維 PC 列印環境 [S19]。
  - 列印手指連桿與手掌框架，去除支撐並清理表面。
  - 以熱工具將熱壓入嵌件垂直安放入 4.0mm 引導孔 [S21]。
  - 依據軸承規格裁切 IGUS 精密鋁軸並進行端面倒角 [S18]。
  - 將套筒軸承壓入外殼後插入軸，確認間隙 [S17]。
  - 以 M3 內六角螺絲緊固結構與感測器支架 [S20]。
  safety:
  - 注意高溫噴嘴 (285°C) 及加熱床 (110°C) 造成的燙傷風險 [S19]。
  - 列印件後加工與倒角時，必須佩戴護目鏡。
  - 嵌件加熱時可能產生煙霧，請開啟換氣設備。
  - 通電前確認所有機械緊固狀態。
  deliverables:
  - 製作完成之 5 機器人手結構（連桿、手掌）。
  - 熱壓入嵌件垂直度與軸承間隙測量紀錄。
  - 最終緊固部位目視檢查報告。
assignment:
  title: 機器人手製作精度驗證
  deliverables:
  - 完成之結構體 CAD 數據與實際尺寸測量比較表
  - 組裝公差管理計畫書
  - 肌腱路徑結構的摩擦降低設計說明書
  rubric:
  - 熱壓入嵌件是否垂直安裝 (優/良/差)
  - 軸承與軸組裝後是否旋轉順暢 (合格/不合格)
  - 是否遵守 BOM 規範之零件額定值與規格 [B10, B11, B12, B13, B14]
quiz:
- question: 使用 PC-CF 耗材時，必須使用硬化鋼噴嘴的主要原因為何？
  choices:
  - 防止碳纖維磨耗導致黃銅噴嘴快速損壞
  - 耗材熔點低，一般噴嘴無法列印
  - 提升列印件表面光澤
  - 提升擠出速度
  answer_index: 0
  explanation: 碳纖維磨耗性極高，會迅速損壞一般黃銅噴嘴，故必須使用硬化鋼噴嘴 [S19]。
- question: 使用 M3 熱壓入嵌件 (Accu HTBI-M3-BR) 時，建議的引導孔直徑為何？
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: 依據官方數據表，建議孔徑為 4.0mm [S21]。
completion_criteria:
- 所有結構零件均以 FDM 3D 印表機製作完成 [B10]
- 熱壓入嵌件已正確安放入所有指定孔位 [B14]
- 鋁合金軸與套筒軸承的組裝間隙符合基準值 [B11, B12]
- 緊固時正確使用 BOM 指定的 M3 內六角螺絲 [B13]
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
PC (Polycarbonate) 具備優異剛性與耐熱性，添加碳纖維的 PC-CF 耗材可最大化剛性，適合結構零件製作 [S19]。但由於碳纖維的磨耗性，必須使用硬化鋼噴嘴 [S19]，且需以 285°C 左右的高溫列印 [S19]。

#### 精密組裝用的嵌件與緊固
為實現塑膠列印件的可反覆拆裝，使用熱壓入螺紋嵌件 [S21]。針對 M3 嵌件，CAD 設計時需預留 4.0mm 直徑的引導孔，以確保正確位置 [S21]。此外，免加油聚合物套筒軸承 (iglide J) 與 8mm 鋁合金軸組裝時，設計上需確保壓入後內徑達到最佳間隙 [S17]，因此對 8mm 軸徑的公差管理極為重要 [S17, S18]。

#### 肌腱驅動結構
Dyneema SK78 纖維在 1.5mm 直徑下具備 230 daN 的高斷裂負荷與 1% 以下伸長率 [S16]，是鋼索的優良替代品。由於肌腱在旋轉軸上會重複彎曲，設計結構時需對絞盤邊緣進行倒圓處理，以防止因摩擦導致斷裂。
