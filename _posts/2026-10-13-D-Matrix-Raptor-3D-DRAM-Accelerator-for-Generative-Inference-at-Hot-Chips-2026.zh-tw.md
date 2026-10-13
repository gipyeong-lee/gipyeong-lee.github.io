---
layout: post
title: "AI 為何能變得更聰明、更快速：『3D DRAM』的崛起"
description: "介紹 d-Matrix 的「Raptor」3D-DRAM 技術，這項新半導體技術將大幅提升生成式 AI 的推論速度。"
summary: "d-Matrix 發布的「Raptor」採用將運算單元與記憶體垂直堆疊的 3D-DRAM 架構，解決數據傳輸瓶頸，從而顯著改善 AI 的推論效能。"
tags: [AI, 半導體, d-Matrix, 3D-DRAM, HotChips2026]
image: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026.jpg
image_alt: "象徵半導體晶片層層堆疊之未來結構的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "將記憶體與運算單元在物理上緊密結合是 AI 加速器的未來。Raptor 作為 HBM 的替代方案，證明了其能源效率，並為 AI 推論基礎設施開啟了新的可能性。"
quiz:
  - question: "d-Matrix 發布的「Raptor」技術其核心結構為何？"
    choices: ["將 SRAM 水平排列", "將運算單元與 DRAM 垂直堆疊", "分散雲端伺服器"]
    answer: 1
    explanation: "Raptor 是一種 3D-DRAM 架構，透過 36 微米間距（pitch）將 TSMC 4nm 運算單元與客製化 DRAM 垂直堆疊在一起。"
  - question: "與傳統 HBM 相比，Raptor 技術的優勢為何？"
    choices: ["消耗更多電力", "約 1/10 等級的能源效率", "降低數據傳輸速度"]
    answer: 1
    explanation: "Raptor 實現了高效運算，其功耗僅為 HBM 的約 1/10。"
  - question: "Raptor 旨在解決的核心問題是什麼？"
    choices: ["數據傳輸時產生的「記憶體瓶頸」", "網路連線速度問題", "AI 訓練數據不足"]
    answer: 0
    explanation: "Raptor 是為了克服生成式 AI 基礎設施中，數據傳輸時產生的瓶頸，即所謂的「記憶體牆（Memory Wall）」問題而設計。"
lang: zh-tw
ref: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026
---

想像一下，您在圖書館裡想找一本非常重要的書。但那本書存放在建築物地下的深處倉庫，而閱覽室卻在頂樓。如果每借一本書都要上下樓梯幾十次，那會有多累？我們現在使用的生成式 AI 也面臨類似的處境。由於 AI 的「大腦」運算單元為了從儲存資料的倉庫（記憶體）提取數據而浪費能源，並因速度變慢而深受「記憶體瓶頸」之苦。

在近期舉辦的「Hot Chips 2026」學術大會上，半導體企業 d-Matrix 公開了一項解決此煩惱的有趣技術，即名為「Raptor」的 3D-DRAM 加速器。現在，AI 不需要再為了找數據而跑到遠處的倉庫了，因為書架就直接貼在 AI 大腦的下方。

## 這為何重要？

當生成式 AI 輸出複雜的回應時，實際上會極快速地重複無數次從記憶體提取大量數據並傳送至運算單元的過程。此過程中產生的數據傳輸，成為了阻礙 AI 效能的巨大障礙，專業術語稱之為「記憶體牆（Memory Wall）」。[出處 d-Matrix Raptor 3D-DRAM Architecture at Hot Chips 2026](https://www.partgenie.ai/insights/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026-9)

為了讓我們使用的智慧型手機 AI 助理功能變得更快，或讓即時生成複雜影像的 AI 服務變得更便宜，必須推倒這道牆。Raptor 正是為了突破該技術侷限而誕生。[出處 d-Matrix's Raptor puts stacked DRAM to work on inference bandwidth](https://runtimewire.com/article/d-matrix-raptor-stacked-dram-inference)

## 淺顯易懂的說明

做個簡單的比喻，傳統的 AI 晶片就像「廚房與餐廳距離遙遠的餐廳」。廚師（運算單元）想要做菜，必須走很遠的路到材料倉庫（記憶體）拿食材。相反地，Raptor 則是「廚師可以在旁邊隨手取得食材的最新式開放式廚房」。

Raptor 採用了將以台積電 4 奈米（nm）超微細製程製造的運算單元裸晶（半導體碎片）直接貼合在客製化 DRAM 上方的方式。[出處 Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card) 這被稱為「3D-DRAM」結構。由於記憶體被垂直堆疊在運算單元的正下方，數據必須移動的物理距離縮短到極致。[出處 d-Matrix stacks DRAM directly · Hacker News | Zeli](https://zeli.app/story/49695065)

多虧於此，Raptor 提供了每張卡 100TB/s（每秒兆位元組）驚人的數據傳輸頻寬，顯著減少了通用 AI 晶片普遍面臨的棘手瓶頸問題。[出處 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

## 現狀

根據 d-Matrix 技術長 Sudeep Bhoja 在 Hot Chips 2026 發表的內容，該技術是與 Meta 合作研發。[出處 Hot Chips 2026 - d-Matrix](https://www.d-matrix.ai/event/hot-chips-2026/) 目前的高效能 AI 晶片大多使用名為 HBM（高頻寬記憶體）的昂貴記憶體，而 Raptor 的一大特點是，即便以 HBM 約 1/10 的電力效率，也能發揮同等甚至更好的效能。[出處 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

不過，這項技術並非立即全面取代市場上的所有 HBM。目前 Raptor 專精於推論（Inference，指已訓練的 AI 實際產生回應的過程）效率，預計將在處理龐大數據的整體 AI 基礎設施中佔據一席之地。[出處 d-Matrix's Raptor Chip Hits 105 TB/s in Real Silicon Tests, But It's Not an HBM Replacement Yet](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p6bnJUdEVSRkNfcUU2bE9OWjlpZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)

## 未來展望

我們現在正從單純投入「更多電力」的時代，轉向透過「更有效率的結構」來加速 AI 的時代。若像 Raptor 這樣的 3D-DRAM 技術普及，您所使用的 AI 服務回應速度將會更快，同時耗電量也會降低。這意味著執行 AI 所需的社會成本將會降低。[出處 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

未來半導體業界將以多麼微小且聰明的方式結合記憶體與運算單元，以及 Raptor 所提出的這份新地圖能將人工智慧的未來引領至何處，非常值得期待。

## 參考資料

1. [d-Matrix Raptor 3D-DRAM Accelerator for Generative Inference](https://www.servethehome.com/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026/)
2. [d-Matrix Raptor 3D-DRAM Architecture at Hot Chips 2026](https://www.partgenie.ai/insights/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026-9)
3. [Hot Chips 2026 - d-Matrix](https://www.d-matrix.ai/event/hot-chips-2026/)
4. [Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card)
5. [Hot Chips 2026: d-Matrix Raptor 3D-DRAM - lukebest.github.io](https://lukebest.github.io/papers/hc2026-dmatrix-raptor-3d-dram)
6. [d-Matrix stacks DRAM directly · Hacker News | Zeli](https://zeli.app/story/49695065)
7. [D-Matrix Raptor 3D-DRAM Accelerator for Generative Inference at Hot Chips 2026](https://vk.ru/wall-238001969_5418)
8. [Hot Chips 2026 - Hot Chips 2026](https://hc2026.hotchips.org/?ref=vlsi.kr)
9. [d-Matrix Raptor: 3D-DRAM with 100 TB/s for AI inference](https://www.igorslab.de/en/d-matrix-raptor-3d-dram-over-100-tb-s-stacks-memory-beneath-compute-logic/)
10. [d-Matrix's Raptor 3D DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)
11. [Jobs and Employment at d-Matrix | Simplify Jobs](https://simplify.jobs/c/d-Matrix)
12. [d-Matrix's Raptor 3D DRAM performance - Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p6bnJUdEVSRkNfcUU2bE9OWjlpZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)
13. [d-Matrix's Raptor puts stacked DRAM to work on inference bandwidth](https://runtimewire.com/article/d-matrix-raptor-stacked-dram-inference)