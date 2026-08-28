---
layout: learn-module
title: 效能測試與驗證
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
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M9
slug: testing-validation
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
objectives:
- 設計用於驗證機器手精度與重複性的定量測試指標
- 評估利用 FSR 感測器資料之抓取力控制演算法的穩定性
- 分析 DYNAMIXEL 致動器反饋資料與實際物理動作之間的誤差
- 習得機構缺陷與肌腱驅動機制的耐久性驗證程序
worked_examples:
- 範例 1：OpenCR ADC 電壓計算。當 FSR 電阻為 10 kΩ，且串聯電阻為 10 kΩ 時，3.3 V 分壓器輸出為 V_out = 3.3 * (10k
  / (10k + 10k)) = 1.65 V。這適合 12 位元 ADC 範圍 [S13, S26]。
- 範例 2：保險絲保護協調。當 4 台致動器處於失速狀態時，電流總和為 9.2 A [S11]。10 A 保險絲的冷電阻為 7.7 mΩ [S25]，因此正常運作時電壓降約為
  0.07 V，可忽略不計。但在過電流發生時，準確響應需參考保險絲製造商的時間-電流曲線。
lab:
  title: 機器手整合功能測試
  steps:
  - 在各電源分支物理隔離的狀態下，使用 DC 電壓檔位測量 3 個變壓器的輸出，確認數值為 12 V。
  - 將機器手固定在安全治具上，將控制器 (OpenCR) 連接至 PC，將致動器扭力釋放至 0。
  - 手動對各手指的 FSR 感測器施加壓力，並記錄 ADC 資料變化。
  - 在無負載狀態下，使各手指進行最大活動範圍 (ROM) 動作 5 次，檢查肌腱是否有干擾。
  - 測試結束後，務必將 3 個電源變壓器從牆面插座拔除，並確認殘餘電壓。
  safety:
  - 測試時請務必佩戴安全眼鏡。
  - 通電時，請勿將手伸入機器手的活動範圍內。
  - 若偵測到異常發熱、異味或冒煙，請勿靠近。請於危險區外，透過事先指定的建物配電盤斷路器或認證的上游主斷路器 (upstream master disconnect)
    切斷 3 個變壓器之供電後撤離。若無危險區外可操作的上游斷路手段，禁止系統通電。扭力釋放不能替代電源切斷。維護與接近需在計畫停機後，確認物理隔離與無電源測量後方可進行。
  - 未經電壓測量前請勿觸碰系統。必須確認 DC 電壓低於 1 V。
  deliverables:
  - 手指抓取力感測器校正記錄
  - 重複動作精度測試資料
  - 各電源分支負載電流測量數值
assignment:
  title: 機器手效能分析最終報告
  deliverables:
  - 效能測試結果分析報告
  - 基於資料之抓取控制演算法程式碼
  rubric:
  - 感測器資料信噪比 (SNR) 分析的適當性
  - 重複動作測試中精度的定量化
  - 對保護設計 (保險絲) 是否滿足系統保護意圖的理論探討
  - 設計規格與實際成品之效能指標比較
quiz:
- question: 配置利用 FSR 402 感測器與 OpenCR ADC 的力測量電路時，下列敘述何者正確？
  choices:
  - FSR 分壓器僅使用 3.3 V 感測器電源，並將類比輸入訊號維持在 0~3.3 V 範圍內。
  - 以 FSR 與 10 kΩ 電阻組成電壓分壓器，使用 3.3 V 感測器軌。
  - ADC 訊號必須永遠維持在 0~5 V 範圍內。
  - FSR 電阻固定，因此不需要額外的分壓電阻。
  answer_index: 1
  explanation: 必須使用 OpenCR 感測器軌 (3.3 V) 將 ADC 輸入限制在 0~3.3 V 範圍，並配置分壓電路將電阻變化讀取為電壓變化
    [S13, S26]。
- question: 管理 DYNAMIXEL XM430-W350-T 致動器 12 V 電源分支的方法，下列何者正確？
  choices:
  - 將 3 個變壓器的正極 (+) 輸出綁在一起進行電力加總。
  - 為各個變壓器裝設 10 A 保險絲，並作為獨立分支使用。
  - 因為電流低於保險絲額定值，無需安全驗證即可使用。
  - 電源變壓器輸出不經保險絲直接並聯連接。
  answer_index: 1
  explanation: 各個變壓器輸出必須保持獨立，且需配置對應獨立分支的保險絲，以防止過電流 [S15]。
- question: 機器手驗證階段最重要的安全程序為何？
  choices:
  - 軟體扭力釋放即等同於切斷電源。
  - 務必使用三用電表確認 DC 低於 1 V 後，方可接近進行維護。
  - 保險絲為計畫停機裝置，因此將保險絲拔除即可。
  - 以連續性 (Continuity) 檔位確認電源已切斷。
  answer_index: 1
  explanation: 軟體扭力釋放無法取代物理電源切斷，必須在物理分離後，使用 DC 電壓檔位確認無殘餘能量，此為必要程序。
completion_criteria:
- 提交效能測試結果報告並取得 70 分以上
- 所有 Lab 階段遵守安全準則，並確認完成物理斷電
- 確認已實作控制程式碼之感測器資料濾波功能
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

## 效能測試與驗證理論

機器手的效能驗證是確認設計規範與實際物理行為一致性的過程 [S1]。主要指標如下：

### 1. 位置與抓取精度
重複性 (Repeatability) 是指機器手執行相同指令時，抵達位置的誤差範圍。XM430-W350-T 致動器透過內部編碼器提供精確的位置反饋 [S11]，但最終指尖位置會因肌腱的伸長與摩擦產生誤差。Dyneema 肌腱伸長率低於 1%，在確保重複性方面具有優勢 [S16]。

### 2. 力控制與 FSR 感測器訊號處理
FSR 402 感測器的特性為電阻隨施加力而減少 [S12]。將其與 10 kΩ 電阻組成分壓電路，以 OpenCR 的 12 位元 ADC 測量 [S13, S26]。感測器資料雜訊較多，需應用移動平均濾波器 (Moving Average Filter) 以形成穩定的抓取力反饋迴路。

### 3. 過電流保護與電源穩定性
系統使用 3 個獨立的 12 V 電源分支 [S15]。各分支由 10 A ATOF 保險絲保護 [S25]，需分配致動器峰值電流總和以不超過保護額定值。需透過製造商提供之保險絲時間-電流曲線，驗證保護協調性。
