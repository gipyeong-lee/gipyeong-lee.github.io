---
layout: learn-module
title: 性能測試與驗證
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
ref: learn:precise-robot-hand:testing-validation
translations:
- lang: ko
  url: /learn/precise-robot-hand/testing-validation/
- lang: en
  url: /learn/en/precise-robot-hand/testing-validation/
- lang: ja
  url: /learn/ja/precise-robot-hand/testing-validation/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/testing-validation/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/testing-validation/
module_id: M9
permalink: /learn/zh-tw/precise-robot-hand/testing-validation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 6d06f766b906424eb1f714f11e36dcf4
id: M9
slug: testing-validation
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
objectives:
- 設計用於驗證機器手精度與重複性的定量測試指標
- 評估利用 FSR 傳感器數據的抓取力控制算法的穩定性
- 分析 DYNAMIXEL 執行器反饋數據與實際物理動作之間的誤差
- 掌握機械缺陷及腱驅動機制的耐久性驗證程序
worked_examples:
- 範例 1：OpenCR ADC 電壓計算。當 FSR 電阻為 10 kΩ，串聯電阻為 10 kΩ 時，3.3 V 分壓器輸出為 V_out = 3.3 * (10k
  / (10k + 10k)) = 1.65 V。這適合 12 位 ADC 的範圍 [S13, S26]。
- 範例 2：保險絲保護協調。當執行器 4 台處於堵轉狀態時，電流總和為 9.2 A [S11]。由於 10 A 保險絲的冷電阻為 7.7 mΩ [S25]，正常運行時電壓降約為
  0.07 V，屬於可忽略水平；但在過電流情況下，精確響應需參考保險絲製造商的時間-電流曲線。
lab:
  title: 機器手集成功能測試
  steps:
  - 在每個電源分支物理隔離的狀態下，使用直流電壓模式測量 3 個適配器的輸出，確認輸出為 12 V。
  - 將機器手固定在安全夾具上，並將控制器（OpenCR）連接至 PC，將執行器扭矩釋放為 0。
  - 手動對每個手指的 FSR 傳感器施加壓力，並記錄 ADC 數據變化。
  - 在無負載狀態下，將各手指的最大運動範圍（ROM）重複動作 5 次，以確認是否存在腱干涉。
  - 測試結束後，務必將 3 個電源適配器從牆面插座斷開，並確認殘餘電壓。
  safety:
  - 測試時務必佩戴護目鏡。
  - 通電期間，請勿將手放入運動範圍內。
  - 若偵測到異常發熱、氣味或煙霧，請勿靠近。在危險區域外，請斷開預先指定的建築配電盤斷路器或認證的上游主斷路器，切斷 3 個適配器的電源後撤離。若危險區域外無可操作的上游斷電手段，則禁止對系統通電。扭矩釋放不能替代切斷電源。維護與接近操作僅能在規劃停機後，經過物理斷電及確認無電狀態後方可進行。
  - 未經電壓測量不得接觸系統。必須確認 DC 電壓低於 1 V。
  deliverables:
  - 手指抓取力傳感器校準記錄
  - 重複動作精度測量數據
  - 各電源分支的負載電流測量值
assignment:
  title: 機器手性能分析最終報告
  deliverables:
  - 性能測試結果分析報告
  - 基於數據的抓取控制算法代碼
  rubric:
  - 傳感器數據信噪比（SNR）分析的適當性
  - 重複動作測試中精度的定量化
  - 保護設計（保險絲）是否滿足系統保護意圖的理論思考
  - 設計規格與實際成品性能指標的比較
quiz:
- question: 在使用 FSR 402 傳感器和 OpenCR ADC 組成力測量電路時，下列哪項是正確的？
  choices:
  - FSR 分壓器僅使用 3.3 V 傳感器電源，並將模擬輸入信號保持在 0~3.3 V 範圍內
  - 由 FSR 和 10 kΩ 電阻組成分壓器，並使用 3.3 V 傳感器軌
  - ADC 信號必須始終在 0~5 V 範圍內
  - 由於 FSR 電阻恆定，因此不需要額外的分壓電阻
  answer_index: 1
  explanation: 使用 OpenCR 傳感器軌（3.3 V）將 ADC 輸入限制在 0~3.3 V 範圍內，並構建分壓電路以將電阻變化讀取為電壓變化 [S13,
    S26]。
- question: 管理 DYNAMIXEL XM430-W350-T 執行器的 12 V 電源分支的正確方法是什麼？
  choices:
  - 將 3 個適配器的正極(+)輸出捆綁在一起以疊加電力
  - 為每個適配器安裝 10 A 保險絲，並作為單獨的獨立分支使用
  - 由於電流低於保險絲額定值，無需安全驗證即可使用
  - 電源適配器輸出在沒有保險絲的情況下直接並聯連接
  answer_index: 1
  explanation: 各適配器輸出必須保持獨立，並安裝符合獨立分支要求的保險絲以防止過電流 [S15]。
- question: 在機器手驗證階段，最重要的安全程序是什麼？
  choices:
  - 通過軟件釋放扭矩等同於切斷電源
  - 務必使用萬用表確認 DC 電壓低於 1 V 後，方可接近維修
  - 保險絲充當計劃停機裝置，因此應拔掉保險絲
  - 通過連續性（Continuity）模式確認電源已切斷
  answer_index: 1
  explanation: 軟件釋放不能替代物理切斷電源，物理隔離後使用直流電壓模式測量確認無殘餘能量是必不可少的。
completion_criteria:
- 性能測試結果報告提交及獲得 70 分以上
- 所有 Lab 階段皆遵守安全準則及確認物理斷電
- 確認控制代碼中傳感器數據過濾功能的實現
source_ids:
- S1
- S11
- S16
- S12
- S13
- S26
- S15
- S25
---

## 性能測試與驗證理論

機器手的性能驗證是確認設計規格與實際物理行為之間一致性的過程 [S1]。主要指標如下：

### 1. 位置與抓取精度
重複性（Repeatability）是指機器手執行相同命令時，到達位置的誤差範圍。XM430-W350-T 執行器通過內部編碼器提供精確的位置反饋 [S11]，但最終指尖位置會因腱的伸長和摩擦而產生誤差。Dyneema 腱的伸長率低於 1%，這對確保重複性非常有利 [S16]。

### 2. 力控制與 FSR 傳感器信號處理
FSR 402 傳感器具有電阻隨所施加力減小的特性 [S12]。通過將其與 10 kΩ 電阻構成分壓電路，並用 OpenCR 的 12 位 ADC 測量 [S13, S26]。傳感器數據噪聲較大，因此需要應用移動平均濾波器（Moving Average Filter）來形成穩定的抓取力反饋迴路。

### 3. 過電流保護與電源穩定性
系統使用 3 個獨立的 12 V 電源分支 [S15]。每個分支由 10 A ATOF 保險絲保護 [S25]，必須分配電源以確保執行器峰值電流總和不超過保護額定值。這必須通過供應商提供的保險絲時間-電流曲線來驗證保護協調性。
