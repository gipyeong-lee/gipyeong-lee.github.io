---
layout: learn-module
title: 機器手臂組裝
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:assembly
translations:
- lang: ko
  url: /learn/precise-robot-hand/assembly/
- lang: en
  url: /learn/en/precise-robot-hand/assembly/
- lang: ja
  url: /learn/ja/precise-robot-hand/assembly/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/assembly/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/assembly/
module_id: m6
permalink: /learn/zh-tw/precise-robot-hand/assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 86f63f17be15487197f653755bdf316f
id: m6
slug: assembly
phase_id: p2
estimated_hours: 15.0
prerequisites:
- m5
objectives:
- 理解機器手臂機構組裝的精密組件緊固原理。
- 熟悉肌腱 (Dyneema) 驅動系統的張力傳遞結構。
- 學習獨立電源分流組成與物理配線安全。
- 熟練 FSR 感測器與分壓電路之正確整合方式。
worked_examples:
- 範例 1：熔斷器容量計算。將 XM430 致動器 11 台（堵轉電流合計 9.2 A）連接至 1 個 12 V 分流時，選用 10 A 熔斷器較為適當。此規格可在適應正常運作範圍的同時，於配線過載時保護電路
  [S14, S26]。
- 範例 2：熱熔鑲件深度。M3 黃銅鑲件須垂直精確熱熔嵌入 PC-CF 輸出件中，需配合 4.4 mm 外徑使用 4 mm 導向孔 [S23]。歪斜將降低螺紋組裝精度，務必謹慎。
lab:
  title: 機器手臂機構組裝與配線實習
  steps:
  - 將 M3 熱熔鑲件安裝至手指連桿與手掌框架。
  - 將 igus JSM-0810-10 軸承與 8 mm 鋁合金軸安裝至手腕與關節軸。
  - 將 Dyneema 肌腱繞於捲筒上，並以適當張力連接至手指。
  - 使用 Micro-Fit 3.0 接頭對各致動器與手指感測器線束進行配線 [S9]。
  - 於各獨立 12 V 分流安裝 10 A 熔斷器，並確認各別電源連接 [S26, S25]。
  safety:
  - 通電前，務必使用萬用電表確認 3 個電源分流之絕緣狀態。
  - 肌腱張力測試期間，為防肌腱斷裂彈跳，務必配戴護目鏡。
  - 維修或接近零組件前，務必物理斷開 3 個電源供應器，並測量各分流電壓確認低於 1 V。
  - 絕不可將兩台以上電源供應器之正極 (+) 輸出並聯。
  deliverables:
  - 各關節無摩擦驅動確認影片
  - 各電源分流熔斷器安裝照片
  - 組裝完成機器手臂之配線圖與緊固扭力記錄
assignment:
  title: 機器手臂系統整合報告
  deliverables:
  - 完成組裝體 3 面圖與緊固點細節圖 (CAD)
  - 電源分流負載分配表與熔斷器容量驗證結果
  - 手指彎曲時肌腱張力資料記錄
  rubric:
  - 機構組裝精度與軸承摩擦最小化 (40%)
  - 獨立分流之獨立電源配線與遵守安全準則 (40%)
  - 提交技術規格之準確性 (20%)
quiz:
- question: 下列關於電源供應方式之敘述，何者正確？
  choices:
  - 將 3 個電源供應器之正極 (+) 端子並聯以增加電流容量。
  - 各電源供應器作為獨立分流使用，正極 (+) 端子電氣絕緣。
  answer_index: 1
  explanation: 為系統安全，各電源供應器作為獨立分流使用，嚴禁將正極 (+) 輸出並聯。
- question: 將 FSR 402 感測器連接至 OpenCR 主機板時，應使用之電壓為何？
  choices:
  - 3.3 V 感測器電源軌
  - 12 V 致動器電源軌
  answer_index: 0
  explanation: FSR 感測器分壓電路為將 ADC 訊號維持在 0-3.3 V 範圍內，務必連接至 3.3 V 感測器軌。
- question: 肌腱採用 Dyneema SK78 之主因為何？
  choices:
  - 低價且易於加工
  - 高斷裂負荷與極低運作伸長率，且體積小
  answer_index: 1
  explanation: Dyneema SK78 具極高強度與低伸長率，適合精密張力傳遞。
completion_criteria:
- 完成所有 5 個手指關節之物理組裝。
- 確認獨立 3 個電源分流之熔斷器安裝。
- 組裝完成後，各 3 個分流均確認處於無電狀態 (低於 1 V)。
source_ids:
- S19
- S20
- S21
- S23
- S18
- S17
- S26
- S15
- S27
- S16
- S14
- S9
- S25
---

### 精密組裝與線束系統

機器人手組裝是同時確保機械剛性與電子可靠性的精密工程。主要結構件由剛性與尺寸穩定性高的碳纖維填充 PC 線材 (PC-CF) 製作 [S21]，並設計透過 M3 黃銅熱熔埋入螺母，實現重複拆解與組裝 [S23]。

#### 腱驅動原理
腱將致動器的旋轉運動轉換為手指關節的屈曲運動。Dyneema SK78 材質在直徑 1.5 mm 下提供 230 daN 的高斷裂負載與低於 1% 的工作伸長率，最大化張力傳遞效率 [S18]。組裝時，滑輪邊緣的圓角處理是防止腱磨損的必要要素。

#### 獨立電源與安全分支
本系統使用 3 個獨立的 12 V 電源分支 [S17]。各分支在變壓器端電氣隔離，絕對禁止將正極(+)輸出並聯連接。各分支串聯配置 10 A ATOF 保險絲以防配線缺陷 [S26]。此設計確保了致動器堵轉電流總和能被安全承受。

#### 感測器介面
指尖的 FSR 402 感測器是電阻隨壓力變化的可變電阻體 [S15]。本教育用原型機不主張符合機械安全標準或認證，投入人員接觸環境前需經合格安全專家進行獨立審核 [S27] [S16]。
