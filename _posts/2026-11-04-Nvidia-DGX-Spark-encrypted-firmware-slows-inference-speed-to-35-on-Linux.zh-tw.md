---
layout: post
title: "桌上的 AI 超級電腦，為什麼 NVIDIA DGX Spark 變慢了？"
description: "探討 NVIDIA 小型 AI 電腦 DGX Spark 的效能問題、特色，以及實際應用潛力。"
summary: "NVIDIA 的超小型 AI 超級電腦 DGX Spark 在 Linux 環境下因韌體問題導致效能下降，但目前正透過軟體更新尋求解決方案。"
tags: [AI, NVIDIA, DGXSpark, 人工智慧, 科技]
image: 2026-11-04-Nvidia-DGX-Spark-encrypted-firmware-slows-inference-speed-to-35-on-Linux.jpg
image_alt: "放置在桌面上，設計精緻的小型電腦 NVIDIA DGX Spark"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是尖端 AI 技術從資料中心走入大眾視野時所經歷的成長陣痛。為了充分發揮硬體效能，軟體優化顯得比以往任何時候都更加重要。"
quiz:
  - question: "NVIDIA DGX Spark 支援的統一記憶體容量是多少？"
    choices: ["64 GB", "128 GB", "256 GB"]
    answer: 1
    explanation: "DGX Spark 配備了 128 GB 的 LPDDR5X 統一記憶體。"
  - question: "連接兩台 DGX Spark 後，最多可以運行擁有多少參數的模型？"
    choices: ["1,000 億個", "2,000 億個", "4,050 億個"]
    answer: 2
    explanation: "透過 NVIDIA ConnectX 技術，連接兩台裝置後最多可處理擁有 4,050 億個參數的模型。"
  - question: "當推論（Inference）速度變慢時，文中提到有效的解決方法是什麼？"
    choices: ["重新啟動硬體", "使用最新的 TensorRT-LLM 發布映像檔", "更換網路線"]
    answer: 1
    explanation: "在初始設定中，推論速度緩慢的問題已透過使用最新的 TensorRT-LLM 發布映像檔 (1.2.0rc1) 獲得顯著改善。"
lang: zh-tw
ref: 2026-11-04-Nvidia-DGX-Spark-encrypted-firmware-slows-inference-speed-to-35-on-Linux
---

試想一下，當您早晨起床對智慧型手機的 AI 助理說：「請幫我整理並總結今天需要處理的複雜業務資料。」過去這項工作必須經過巨大的資料中心處理，但現在只要桌面上的一個小盒子，就能輕鬆完成所有任務。這聽起來像是夢想，但 NVIDIA 推出的超小型 AI 超級電腦「DGX Spark」正在開啟這種可能性。然而，最近有消息指出，這台強大的裝置正因為與軟體的搭配問題而面臨效能下降的情況。這究竟是怎麼回事呢？

### 為什麼這很重要？

DGX Spark 的重要性在於，它將以往只能在資料中心看到的「Grace Blackwell」架構的強大效能，帶到了使用者的桌面 [[出處: Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)]。開發者、研究人員和機器人工程師不必租用巨大的伺服器機房，就能在本地環境直接運行高效能 AI 模型 [[出處: NVIDIA Enters The AI PC Realm With DGX Spark & DGX Station...](https://wccftech.com/nvidia-enters-ai-pc-realm-dgx-spark-dgx-station-desktops-72-core-grace-cpu-blackwell-gpus-up-to-784-gb-memory/)]。

然而，無論效能再好，如果軟體無法配合，對使用者而言也只是虛設。最近有報告指出，在某些環境下，推論（AI 生成答案的過程）速度顯著變慢，這也再次證明了軟體優化對於發揮硬體潛力的重要性 [[出處: TRT LLM for Inference- two Sparks example is VERY slow-DGX...](https://forums.developer.nvidia.com/t/trt-llm-for-inference-two-sparks-example-is-very-slow/348517)]。

### 用簡單的比喻說明

為了理解 DGX Spark，我們用廚房來比喻。想像一位效能極佳的主廚（Grace Blackwell 架構）來到了一個非常小的廚房（本體尺寸為 150 × 150 × 50.5 mm）[[出處: Тест и обзор: NVIDIA DGX Spark — мини-ПК... - Hardwareluxx Russia](https://www.hardwareluxx.ru/index.php/artikel/hardware/komplettsysteme/58897-test-i-obzor-nvidia-dgx-spark-mini-pk-dlya-ii-v-realnykh-zadachakh.html)]。這位主廚具備處理大量食材（資料）的頂尖能力。

但主廚要煮菜，需要「食譜（軟體/TensorRT-LLM）」。最近在 Linux 環境下發生的推論速度下降問題，是因為主廚雖然有能力，卻拿到了錯誤的食譜。幸運的是，NVIDIA 透過提供新的食譜（最新的發布映像檔），幫助主廚找回了應有的速度 [[出處: TRT LLM for Inference- two Sparks example is VERY slow-DGX...](https://forums.developer.nvidia.com/t/trt-llm-for-inference-two-sparks-example-is-very-slow/348517)]。

### 目前狀況如何？

DGX Spark 目前憑藉 128 GB 的 LPDDR5X 統一記憶體，正在處理驚人的任務 [[出處: Laptop & Workstation Inference Systems | Artificial Analysis](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations)]。例如，使用 FP4 技術，可以將像「Qwen3.6-72B」這樣的大型語言模型以 4-bit 格式載入，僅佔用約 35 GB 的記憶體。剩餘超過 90 GB 的記憶體則用於讓 AI 記憶上下文，即便在極長的對話中，也能聰明且不減速地回答問題 [[出處: Nvidia DGX Spark или AMD Ryzen AI Max+ 395... | Блог Serverflow](https://serverflow.ru/blog/stati/nvidia-dgx-spark-ili-amd-ryzen-ai-max-395-kakoy-mini-pk-dlya-lokalnykh-llm-vybrat/)]。

當然，並非所有使用者都感到滿意。科技專家 Jeff Geerling 指出，對於一般使用者僅僅為了運行語言模型而言，這台機器的性價比略顯不足 [[出處: Dell's version of the DGX Spark fixes pain points - Jeff Geerling](https://www.jeffgeerling.com/blog/2025/dells-version-dgx-spark-fixes-pain-points/)]。作為專門為專業人士打造的裝置，對一般大眾來說可能有些「過剩」。

### 未來有什麼期待？

未來，華碩 (ASUS)、戴爾 (Dell)、惠普 (HP) 和聯想 (Lenovo) 等大型製造商預計將基於 NVIDIA 的平台，陸續推出具有各自特色的版本 [[出處: NVIDIA Enters The AI PC Realm With DGX Spark & DGX Station...](https://wccftech.com/nvidia-enters-ai-pc-realm-dgx-spark-dgx-station-desktops-72-core-grace-cpu-blackwell-gpus-up-to-784-gb-memory/)]。此外，若將兩台 DGX Spark 透過網路連接，甚至可以運行高達 4,050 億參數的超巨型模型，擴充潛力備受期待 [[出處: NVIDIA DGX Spark Система искусственного интеллекта | AliExpress](https://aliexpress.ru/item/1005010631725345.html)]。

### AI 的一席話

技術唯有在硬體與軟體達到完美平衡時，才算真正成熟。DGX Spark 目前展現了硬體上的革命，但在軟體打磨上仍處於進步階段。對於科技愛好者來說，觀察 NVIDIA 多快能改善軟體「食譜」，將會是比該裝置令人驚嘆的硬體規格更有趣的焦點。

## 參考資料

1. [Nvidia DGX Spark или AMD Ryzen AI Max+ 395... | Блог Serverflow](https://serverflow.ru/blog/stati/nvidia-dgx-spark-ili-amd-ryzen-ai-max-395-kakoy-mini-pk-dlya-lokalnykh-llm-vybrat/)
2. [mac-studio-m5-ultra-vs-nvidia-dgx-spark-local-llms](https://ngxptech.com/mac-studio-m5-ultra-vs-nvidia-dgx-spark-local-llms/)
3. [Ryzen AI Max+ 395 или DGX Spark: выбираем мини-ПК для...](https://digital-razor.ru/media/articles/workstation/dgx-spark-vs-ryzen-ai-max-395/)
4. [Laptop & Workstation Inference Systems | Artificial Analysis](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations)
5. [Тест и обзор: NVIDIA DGX Spark — мини-ПК... - Hardwareluxx Russia](https://www.hardwareluxx.ru/index.php/artikel/hardware/komplettsysteme/58897-test-i-obzor-nvidia-dgx-spark-mini-pk-dlya-ii-v-realnykh-zadachakh.html)
6. [NVIDIA DGX Spark Система искусственного интеллекта | AliExpress](https://aliexpress.ru/item/1005010631725345.html)
7. [DGX Spark vs M5 Max MacBook Pro: что выбрать для... | AiManual](https://ai-manual.ru/article/dgx-spark-vs-m5-max-macbook-pro-chto-vyibrat-dlya-lokalnogo-inferensa-i-obucheniya-modelej-v-2025-godu/)
8. [Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
9. [NVIDIA DGX Spark для YOLO26を使用する | Ultralytics](https://docs.ultralytics.com/ja/guides/nvidia-dgx-spark)
10. [NVIDIA Enters The AI PC Realm With DGX Spark & DGX Station...](https://wccftech.com/nvidia-enters-ai-pc-realm-dgx-spark-dgx-station-desktops-72-core-grace-cpu-blackwell-gpus-up-to-784-gb-memory/)
11. [TRT LLM for Inference- two Sparks example is VERY slow-DGX...](https://forums.developer.nvidia.com/t/trt-llm-for-inference-two-sparks-example-is-very-slow/348517)
12. [Dell's version of the DGX Spark fixes pain points - Jeff Geerling](https://www.jeffgeerling.com/blog/2025/dells-version-dgx-spark-fixes-pain-points/)