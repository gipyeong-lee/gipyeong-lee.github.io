---
layout: learn-module
title: 機器人機構設計
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:mechanism-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/mechanism-design/
- lang: en
  url: /learn/en/precise-robot-hand/mechanism-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/mechanism-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/mechanism-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/mechanism-design/
module_id: m2
permalink: /learn/zh-tw/precise-robot-hand/mechanism-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 86f63f17be15487197f653755bdf316f
id: m2
slug: mechanism-design
phase_id: p1
estimated_hours: 15.0
prerequisites:
- m1
objectives:
- 理解機器人手臂機構設計的核心原理：欠驅動 (Underactuated) 系統。
- 學習肌腱驅動方式的動力學特性，以及摩擦力與伸長率管理的重要性。
- 學習考慮剛性與尺寸穩定性的工程材料 (PC-CF) 選擇與設計手法。
- 奠定使用熱熔鑲件與軸承進行精密組裝設計之基礎。
worked_examples:
- 範例 1：肌腱張力傳遞分析。當肌腱工作伸長率為 1% 時，在 100 mm 距離下會產生 1 mm 的誤差。為達精密控制，利用致動器電流回授與感測器資料進行閉迴路控制是必要的
  [S14]。
- 範例 2：鑲件連結設計。將 HTBI-M3-BR 鑲件植入 PC-CF 輸出件時，必須嚴格遵守 CAD 設計時的導向孔徑 4 mm，才能實現無間隙組裝 [S23]。
lab:
  title: 機器人關節與肌腱模組組裝實習
  steps:
  - 配戴護目鏡並整理工作台。
  - 檢查 PC-CF 輸出件的導向孔狀態，必要時進行加工。
  - 使用烙鐵加熱熱熔鑲件，並垂直壓入輸出件中。
  - 將 igus 軸承安裝至手腕及關節外殼。
  - 將鋁合金軸穿過軸承，檢查間隙。
  - 將 Dyneema 肌腱繞於捲筒 (Capstan) 上，並固定於組裝好的關節上。
  safety:
  - 使用烙鐵時請注意高溫，並務必配戴護目鏡。
  - 肌腱張力測試期間，為防肌腱斷裂彈跳傷人，切勿將手伸入活動範圍內。
  - 系統組裝完成後，通電前請先以測量儀器確認處於物理斷開狀態。
  deliverables:
  - 已組裝的機器人關節模組
  - 軸承與軸間隙測量記錄
assignment:
  title: 5 機器手臂機構設計專案
  deliverables:
  - 整體機器手臂 CAD 組裝圖
  - 零件清單 (BOM) 與選用依據報告
  - 肌腱路徑最佳化設計圖
  rubric:
  - 所使用的零件是否符合規格 (BOM)？
  - 熱熔鑲件與軸承設計是否得當？
  - 是否實現無機構干涉的自由運動？
quiz:
- question: 肌腱驅動選擇 Dyneema SK78 的主要原因為何？
  choices:
  - 伸長率大且價格便宜
  - 提供低伸長率與高斷裂負荷，確保精度
  answer_index: 1
  explanation: Dyneema SK78 的伸長率極低（低於 1%），能提升機器人控制的重複精度 [S18]。
- question: 對於 PC-CF 輸出件進行重複螺絲組裝，建議的方法為何？
  choices:
  - 直接在輸出件上加工螺紋
  - 嵌入黃銅熱熔鑲件
  answer_index: 1
  explanation: 熱熔鑲件能顯著提升在 PC-CF 等工程塑膠中的螺紋耐用度 [S23]。
completion_criteria:
- 依據 BOM 規格完成各零件之文件化。
- 確認組裝完成之關節模組的功能性運動。
- 遵守安全準則並完成實習。
source_ids:
- S3
- S11
- S18
- S21
- S23
- S19
- S14
---

## 機器人機構設計原理

精密的 5 指機器人手設計的核心，在於實現欠驅動系統，以高效率控制超過致動器數量的自由度 (DoF) [S11]。這使得無需過度增加關節數量，即可穩定抓取各種形狀的物體 [S3]。

### 腱驅動動力學
腱 (Tendon) 驅動是將遠端馬達的張力傳遞至關節的方式。此時，腱的物理特性決定了控制的精度。本課程使用 `Dyneema SK78` 纖維，其在直徑 1.5 mm 下可承受 230 daN 的高斷裂負載，且工作伸長率 (Working stretch) 低於 1%，重複精度極佳 [S18]。

### 材質與結構設計
機器人手的框架與連桿要求高剛性與尺寸穩定性。FDM 方式的 `Prusament PC Blend Carbon Fiber` 是含碳纖維的 PC 材質，具備耐高溫與優秀的強度，適合製作工程級零件 [S21]。組裝時為了重複拆解與再組裝，不使用直接螺紋鎖合，而是使用 M3 黃銅熱熔埋入螺母 (OD 4.4 mm，長度 5.8 mm) 以確保螺紋耐用度 [S23]。旋轉軸使用無給油聚合物套筒軸承 (JSM-0810-10)，實現無需維護的平滑旋轉與摩擦管理 [S19]。
