---
layout: learn-module
title: 3D CAD 模型製作
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:cad-modeling
translations:
- lang: ko
  url: /learn/precise-robot-hand/cad-modeling/
- lang: en
  url: /learn/en/precise-robot-hand/cad-modeling/
- lang: ja
  url: /learn/ja/precise-robot-hand/cad-modeling/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/cad-modeling/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/cad-modeling/
module_id: m3
permalink: /learn/zh-tw/precise-robot-hand/cad-modeling/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 86f63f17be15487197f653755bdf316f
id: m3
slug: cad-modeling
phase_id: p1
estimated_hours: 15.0
prerequisites:
- m2
objectives:
- 理解 3D CAD 模型製作的設計限制與製造流程 (FDM)。
- 學習應用 PC-CF 線材提升結構剛性的技巧。
- 進行考慮熱熔鑲件與軸承公差的精密組裝設計。
worked_examples:
- '**鑲件孔設計**：由於 Accu-components 的 M3 鑲件外徑為 4.4mm，請在 3D CAD 中為輸出件建模 4.0mm 的導向孔 [S23]。列印後加熱插入鑲件，黃銅材質即可在塑膠內部定位，形成堅固的
  M3 內螺紋。'
- '**軸承外殼公差**：使用 igus 軸承 JSM-0810-10 時，10mm 外殼孔徑需設計為壓入後，內徑能與 8mm 精密軸密合且無間隙。過寬會導致軸向晃動，過窄則損壞軸承，請透過測試列印調整公差
  [S19, S20]。'
lab:
  title: 精密連桿設計與組裝驗證
  steps:
  - 將提供的肌腱路徑與關節機構進行 3D CAD 設計與模擬。
  - 將 PC-CF 線材裝入 FDM 印表機，並使用硬化鋼噴嘴列印試件 [S21]。
  - 確認輸出件之 4mm 導向孔後，植入熱熔鑲件 [S23]。
  - 組裝 8mm 鋁合金軸與軸承，確認連桿旋轉自由度並測量間隙 [S19, S20]。
  - 使用萬用電表檢查 3 個獨立電源分流之熔斷器座連接狀態，並檢查通電前熔斷器是否安裝妥當 [S25, S26]。
  safety:
  - 隨時配戴抗衝擊作業護目鏡。
  - 熱熔作業時請注意燙傷，並在通風良好處進行。
  - 通電時務必使用固定夾具，絕對不要將手伸入旋轉部位。
  - 維修或接近系統時，務必物理斷開 3 個電源供應器，並使用萬用電表確認低於 1V。
  deliverables:
  - 機器手臂整體組裝 3D CAD 模型檔
  - 包含鑲件與軸承公差調整之設計驗證報告
  - 各電源分流獨立連接狀態及熔斷器安裝檢查照片
assignment:
  title: 機器手臂機構設計與整合配線計畫
  deliverables:
  - 含所有連桿與關節之詳細 3D CAD 設計檔
  - BOM 與設計一致性確認報告
  - 含 3 個獨立分流與熔斷器配置之配線圖
  rubric:
  - 3D 設計是否符合層疊製造公差與黃銅鑲件規格 (4.4mm OD)？
  - 軸承外殼與軸間之間隙是否適當？
  - 在電氣配線圖中，12V 致動器電源與感測電路是否分離，且各分流是否設計 10A 熔斷器？
quiz:
- question: 若 PC-CF 線材輸出的模型需要螺紋，最合適的方法為何？
  choices:
  - 建模時直接將螺紋輸出。
  - 將黃銅熱熔鑲件加熱後植入。
  answer_index: 1
  explanation: 比起直接在 PC-CF 材質上建模螺紋，建議使用黃銅熱熔鑲件以提升重複組裝再現性 [S23]。
- question: 組成 3 個獨立 12V 電源分流時之注意事項為何？
  choices:
  - 將供應器正極 (+) 並聯以增加電流容量。
  - 各分流須透過獨立的 10A 熔斷器保護過電流。
  answer_index: 1
  explanation: 禁止將獨立電源供應器之正極 (+) 並聯，必須為各分流裝配獨立熔斷器進行保護 [S17, S26]。
- question: FSR 力感測器驅動應使用何種電壓源？
  choices:
  - OpenCR 的 3.3V 感測器電源軌
  - 12V 致動器電源軌
  answer_index: 0
  explanation: FSR 分壓電路必須由 3.3V 感測器電源軌供電，且應與致動器電源分離 [S16]。
completion_criteria:
- 3D CAD 設計檔已精確依據鑲件與軸承規格完成。
- 配線圖已確認 3 個獨立電源分流與熔斷器配置。
- 已繳交含設計與驗證報告的作業，並通過標準評量。
source_ids:
- S12
- S21
- S19
- S20
- S23
- S17
- S26
- S15
- S16
- S27
- S25
---

### 3D CAD 建模與製造設計

製作精密 5 指機器人手時，必須考量 FDM 層積製造特性的設計 (Design for Additive Manufacturing, DfAM)。含碳纖維的 PC-CF 線材具備優秀的機械剛性與尺寸穩定性，適合製作精密連桿 [S21]。

#### 核心設計考量
1. **公差管理與軸承安裝**：使用 8mm 精密鋁軸與 igus JSM-0810-10 軸承時，必須將外殼孔公差納入設計。由於軸承採用壓入 (Press-fit) 方式固定，設計時孔徑需比軸承外徑 (10mm) 微小，以確保組裝緊密 [S19, S20]。
2. **鎖固零件設計**：PC-CF 列印件不適合直接攻螺紋。為了確保重複拆裝的再現性，使用 HTBI-M3-BR 黃銅熱熔埋入螺母。為此，設計時必須配置 4mm 直徑的導引孔 [S23]。
3. **結構最佳化**：在腱驅動方式下，連桿可能會因張力而變形。應確保應力集中的關節部位壁厚，並將模型擺放方向調整為有利於層積方向的抗拉強度。

### 系統整合與安全
本專案的電氣系統由 3 個獨立的 12V 電源分支組成。致動器驅動時為了過電流保護，務必在每個分支安裝 10A ATOF 保險絲，致動器需按 4/4/3 的比例分配以管理尖峰電流 [S17, S26]。感測器訊號獲取時，FSR 402 感測器必須透過 3.3V 感測器電源軌的分壓電阻產生 ADC 輸入值，且必須與 12V 致動器電源完全隔離 [S15, S16, S27]。
