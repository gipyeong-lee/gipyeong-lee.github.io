---
layout: learn-module
title: 軸承與緊固零件安裝
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-tw
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
translation_run_id: 6d06f766b906424eb1f714f11e36dcf4
id: M5
slug: bearing-fastener-install
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M4
objectives:
- 理解製作精密機器手時，軸承與軸的機械公差及安裝原理。
- 習得使用熱壓入嵌件 (Heat-set insert) 確保工程塑膠零件緊固強度的方法。
- 使用適當的扭力與緊固規格，以將組裝間隙最小化。
worked_examples:
- 範例 1：確認殼體內徑 - iglide® JSM-0810-10 軸承外徑為 10 mm。因此殼體孔徑須設計為 10 mm；若未遵守嵌件插入導引孔 4.0 mm，將導致嵌件晃動或殼體破裂
  [S17, S21]。
- 範例 2：M3 螺絲組裝 - M3x10 帽頭螺絲使用 2.5 mm 六角扳手鎖固。過大扭力會導致嵌件周邊樹脂龜裂，故應在「螺絲無法再轉動的瞬間」以最小力道固定
  [S20]。
lab:
  title: 機器手關節精密組裝
  steps:
  - 1. 確認 PC-CF 輸出件殼體內的 4.0 mm 導引孔潔淨無虞，並將嵌件垂直對齊。
  - 2. 將烙鐵加熱至適當溫度，緩慢垂直壓入嵌件，確保其與殼體表面平行。
  - 3. 將 iglide® 軸承壓入孔位，插入 8 mm 鋁合金軸確認間隙與阻力。
  - 4. 使用 M3 螺絲完成連桿間的鎖固，並測試關節運動，驗證摩擦力是否均勻。
  safety:
  - 烙鐵溫度極高，小心燙傷，加熱後應立即置於架上。
  - 嵌件壓入時產生的微細粉塵請勿吸入，務必徹底通風。
  - 作業時務必佩戴防護眼鏡。
  - 若偵測到異常發熱、氣味或煙霧，請勿靠近，並由危險區域外透過指定的建築配電盤斷路器或經認證的 upstream master disconnect 切斷 3
    個轉接器的供電並撤離。若危險區域外無可操作的 upstream 斷電手段，禁止系統通電。扭力解除不能代替切斷電源。維修與接近須在計畫停止後，確認物理斷開並驗證無電狀態下執行。
  deliverables:
  - 各關節摩擦測試紀錄
  - 嵌件垂直對齊照片
  - 組裝後的連桿自由度與間隙測量紀錄
assignment:
  title: 組裝公差與緊固力分析報告
  deliverables:
  - 關節組裝順序與扭力管理計畫書
  - 間隙出現時的解決方案（使用墊片 Shim 或修正公差）說明
  - 組裝完成的機器手連桿夾持測試預備數據
  rubric:
  - 是否明確描述了嵌件插入的垂直度？
  - 是否正確解釋了軸承與軸的公差概念？
  - 是否遵守組裝階段的安全規則？
quiz:
- question: 為何 iglide® J 軸承在壓入殼體後會調整內徑？
  choices:
  - 因軸承材料彈性，壓入時內徑會自動變大。
  - 因壓入過程設計為讓軸承內徑精確配合殼體孔徑公差。
  - 因壓入前的內徑製作得總是小於基準值。
  answer_index: 1
  explanation: iglide® 套筒軸承在壓入前製作得比基準值大，當壓入正確的殼體孔徑時，會形成符合設計公差的內徑 [S17]。
- question: 在 PC-CF 輸出件使用黃銅熱壓入嵌件時，適當的導引孔大小為何？
  choices:
  - 3.5 mm
  - 4.0 mm
  - 4.4 mm
  answer_index: 1
  explanation: 根據資料手冊，HTBI-M3-BR 嵌件的建議導引孔大小為 4.0 mm [S21]。
completion_criteria:
- 已確認 5 根手指關節的摩擦阻力均勻，並提交測量紀錄。
- 已完成所有嵌件是否與 PC-CF 殼體水平的肉眼與尺寸檢查。
- 誓約遵守組裝安全守則並提交作業紀錄簿。
source_ids:
- S17
- S18
- S20
- S21
---

### 軸承與軸的公差管理
為了確保精密機器手關節的平順運動與剛性，採用 iglide® J 套筒軸承 (JSM-0810-10) 與 8 mm 鋁合金精密軸 (AWMP-08)。套筒軸承設計為在壓入 (press-fit) 殼體時內徑會隨之調整，關鍵在於遵守殼體的建議內徑公差 [S17, S18]。若出現間隙，將導致關節精度下降；若過緊，則會增加摩擦力，降低致動器 (DYNAMIXEL XM430) 的電流效率。

### 熱壓入嵌件安裝
PC-CF (碳纖維強化 PC) 輸出件因材料特性，若直接鎖入金屬螺絲，螺紋易磨損。為此採用黃銅材質的熱壓入嵌件 (HTBI-M3-BR) [S21]。嵌件置入 4.0 mm 導引孔後加熱，熔化周邊樹脂進行緊固，即使反覆拆裝也能保持高度機械強度 [S21]。此時若嵌件傾斜，將導致組裝後的連桿對齊失準，故垂直度維持至關重要。
