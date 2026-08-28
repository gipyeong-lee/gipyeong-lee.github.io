---
layout: learn-module
title: 軸承與緊固零件安裝
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:bearing-fastener-install
translations:
- lang: ko
  url: /learn/precise-robot-hand/bearing-fastener-install/
- lang: en
  url: /learn/en/precise-robot-hand/bearing-fastener-install/
- lang: ja
  url: /learn/ja/precise-robot-hand/bearing-fastener-install/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/bearing-fastener-install/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/bearing-fastener-install/
module_id: M5
permalink: /learn/zh-tw/precise-robot-hand/bearing-fastener-install/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M5
slug: bearing-fastener-install
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M4
objectives:
- 理解精密機器人手製作所需的軸承與軸之機械公差與安裝原理。
- 學習使用熱壓入嵌件 (Heat-set insert) 以確保工程塑膠零件之緊固強度的方法。
- 使用適當扭力與緊固規格，使組裝間隙最小化。
worked_examples:
- 例題 1：確認外殼內徑 - iglide® JSM-0810-10 軸承外徑為 10 mm。因此外殼內孔需設計為 10 mm，且嵌件安裝時若未遵守 4.0 mm
  引導孔規格，可能導致嵌件鬆動或外殼損壞 [S17, S21]。
- 例題 2：M3 螺絲組裝 - M3x10 內六角螺絲使用 2.5 mm 六角扳手鎖緊，過大扭力會導致嵌件周圍樹脂產生裂痕，故固定於「無法再轉動的瞬間」即可，切勿施加過大力量
  [S20]。
lab:
  title: 機器人手關節精密組裝
  steps:
  - 1. 確認 PC-CF 列印件外殼的 4.0 mm 引導孔乾淨無雜質，並將嵌件垂直對齊。
  - 2. 將烙鐵加熱至適當溫度，將嵌件垂直緩慢下壓至與外殼表面平行。
  - 3. 將 iglide® 軸承壓入內孔，並插入 8 mm 鋁合金軸確認間隙與阻力。
  - 4. 使用 M3 螺絲完成連桿間緊固，並活動關節以驗證摩擦是否均勻。
  safety:
  - 烙鐵溫度極高，小心燙傷，加熱後應立即歸位。
  - 嵌件壓入過程產生的細微粉塵應避免吸入，請確保通風良好。
  - 作業時務必佩戴護目鏡。
  - 偵測到異常發熱、異味或冒煙時，請勿靠近，並由危險區域外切斷建築配電盤斷路器或認證的 upstream master disconnect 以中斷 3 個電源供應器之供電。若危險區域外無可操作的
    upstream 斷電手段，禁止系統通電。扭力釋放不可取代電源切斷。維修或接近設備必須在計畫性停止後物理斷開並驗證無電源狀態。
  deliverables:
  - 各關節摩擦試驗紀錄
  - 嵌件垂直對齊確認照
  - 已組裝連桿之自由度與間隙測量紀錄
assignment:
  title: 組裝公差與緊固力分析報告
  deliverables:
  - 關節組裝順序與扭力管理計畫書
  - 間隙發生時的解決方案（使用墊片 Shim 或修正公差）說明
  - 已組裝機器人手指之握持試驗預備數據
  rubric:
  - 是否明確描述嵌件安裝的垂直度？
  - 是否正確說明軸承與軸的公差概念？
  - 是否遵守組裝階段的安全守則？
quiz:
- question: iglide® J 軸承壓入外殼後內徑自動調整的原因為何？
  choices:
  - 因材料彈性，壓入後自動膨脹。
  - 因設計上使其在壓入外殼孔位後，可調整至精確尺寸。
  - 因為壓入前的內徑設計上總是小於基準值。
  answer_index: 1
  explanation: iglide® 套筒軸承在壓入前設計為大於基準值，當壓入正確尺寸的外殼內孔後，才會達到設計內的公差內徑 [S17]。
- question: 於 PC-CF 列印件使用黃銅熱壓入嵌件時，適當的引導孔尺寸為何？
  choices:
  - 3.5 mm
  - 4.0 mm
  - 4.4 mm
  answer_index: 1
  explanation: 依據數據表，HTBI-M3-BR 嵌件建議引導孔尺寸為 4.0 mm [S21]。
completion_criteria:
- 確認已組裝之 5 個手指關節摩擦阻力均勻，並提交測量紀錄。
- 以目視及測量確認所有嵌件與 PC-CF 外殼保持平行。
- 簽署並提交組裝安全守則承諾書及作業紀錄表。
source_ids:
- S17
- S18
- S20
- S21
---

### 軸承與軸的公差管理
為確保精密機器人關節的流暢運作與剛性，使用 iglide® J 套筒軸承 (JSM-0810-10) 及 8 mm 鋁合金精密軸 (AWMP-08)。套筒軸承設計為壓入 (press-fit) 外殼時內徑會自動調整，務必遵守外殼建議的內徑公差 [S17, S18]。間隙過大會導致關節精度下降，過窄則會增加摩擦力，降低致動器 (DYNAMIXEL XM430) 的電流效率。

### 熱壓入嵌件安裝
PC-CF (碳纖維強化 PC) 列印件若直接鎖入金屬螺絲，易因材料特性磨損螺紋。為此，使用黃銅材質的熱壓入嵌件 (HTBI-M3-BR) [S21]。嵌件插入 4.0 mm 引導孔後，透過加熱融化周圍樹脂進行緊固，即使反覆拆裝仍能維持高機械強度 [S21]。安裝時嵌件若傾斜，會導致已組裝的連桿對齊偏差，因此務必維持垂直。
