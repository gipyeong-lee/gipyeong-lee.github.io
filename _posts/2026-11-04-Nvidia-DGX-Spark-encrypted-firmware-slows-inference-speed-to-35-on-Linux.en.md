---
layout: post
title: "An AI Supercomputer on My Desk: Why Did NVIDIA's DGX Spark Slow Down?"
description: "Examining the performance issues, key features, and practical viability of NVIDIA's compact AI computer, the DGX Spark."
summary: "NVIDIA's ultra-compact AI supercomputer, DGX Spark, experienced performance degradation on Linux due to firmware issues, but recent software updates are providing solutions."
tags: [AI, NVIDIA, DGXSpark, Artificial Intelligence, Tech]
image: 2026-11-04-Nvidia-DGX-Spark-encrypted-firmware-slows-inference-speed-to-35-on-Linux.jpg
image_alt: "A sleek compact computer, the NVIDIA DGX Spark, placed on a desk"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "These are growing pains experienced as cutting-edge AI technology transitions outside the data center. Software optimization to fully unleash hardware capabilities has become more critical than ever."
quiz:
  - question: "What is the capacity of the unified memory supported by the NVIDIA DGX Spark?"
    choices: ["64 GB", "128 GB", "256 GB"]
    answer: 1
    explanation: "The DGX Spark is equipped with 128 GB of LPDDR5X unified memory."
  - question: "When linking two DGX Spark units, models with up to how many parameters can be executed?"
    choices: ["100 billion", "200 billion", "405 billion"]
    answer: 2
    explanation: "Connecting two units via NVIDIA ConnectX technology allows processing models with up to 405 billion parameters."
  - question: "What effective solution was mentioned when inference speed slowed down?"
    choices: ["Hardware reboot", "Using the latest TensorRT-LLM release image", "Replacing network cables"]
    answer: 1
    explanation: "Slow inference speeds in initial setups were significantly improved by using the latest TensorRT-LLM release image (1.2.0rc1)."
lang: en
ref: 2026-11-04-Nvidia-DGX-Spark-encrypted-firmware-slows-inference-speed-to-35-on-Linux
audio: 2026-11-04-Nvidia-DGX-Spark-encrypted-firmware-slows-inference-speed-to-35-on-Linux.en.mp3
industry: general
---

Imagine waking up in the morning and saying to your smartphone AI assistant, "Please summarize and organize the complex work materials I need to handle today." In the past, this task would have required processing through a massive data center, but now a small box sitting on your desk handles it effortlessly. While it sounds like a dream, the ultra-compact AI supercomputer 'DGX Spark' introduced by NVIDIA is opening up that exact possibility. However, reports have recently emerged that this powerful device is suffering from performance degradation due to software compatibility issues. What exactly is going on?

### Why does this matter?

The DGX Spark holds significant meaning because it brings the powerful performance of the 'Grace Blackwell' architecture—previously confined to data centers—right to a user's desk [[Source: Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)]. Developers, researchers, and roboticists can now directly run high-performance AI models in local environments without renting huge server rooms [[Source: NVIDIA Enters The AI PC Realm With DGX Spark & DGX Station...](https://wccftech.com/nvidia-enters-ai-pc-realm-dgx-spark-dgx-station-desktops-72-core-grace-cpu-blackwell-gpus-up-to-784-gb-memory/)].

However, no matter how impressive the hardware is, it is useless to users if the software fails to support it properly. Recently, a phenomenon where inference speed (the process of AI generating responses) slows down significantly was reported in certain environments. This case demonstrates how vital software optimization is to unlocking the full potential of hardware [[Source: TRT LLM for Inference- two Sparks example is VERY slow-DGX...](https://forums.developer.nvidia.com/t/trt-llm-for-inference-two-sparks-example-is-very-slow/348517)].

### Simply put, as an analogy

To understand the DGX Spark, let's use a kitchen analogy. Imagine an exceptionally talented chef (the Grace Blackwell architecture) working inside a very compact kitchen (the 150 × 150 × 50.5 mm chassis) [[Source: Test and Review: NVIDIA DGX Spark — Mini PC... - Hardwareluxx Russia](https://www.hardwareluxx.ru/index.php/artikel/hardware/komplettsysteme/58897-test-i-obzor-nvidia-dgx-spark-mini-pk-dlya-ii-v-realnykh-zadachakh.html)]. This chef has top-tier capability to process vast amounts of ingredients (data) at once.

However, for the chef to cook, a 'recipe (software / TensorRT-LLM)' is required. The recent issue with degraded inference speed in Linux environments occurred because, despite being capable, the chef was following an incorrect recipe. Fortunately, NVIDIA is helping the chef get back up to speed by providing a new recipe (the latest release image) [[Source: TRT LLM for Inference- two Sparks example is VERY slow-DGX...](https://forums.developer.nvidia.com/t/trt-llm-for-inference-two-sparks-example-is-very-slow/348517)].

### What is the current situation?

Currently, the DGX Spark is achieving impressive feats powered by its 128 GB of LPDDR5X unified memory [[Source: Laptop & Workstation Inference Systems | Artificial Analysis](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations)]. For example, using FP4 technology, large language models like 'Qwen3.6-72B' can be loaded in a 4-bit format, occupying only about 35 GB of memory. The remaining memory of over 90 GB is utilized for the AI to maintain context, enabling it to respond intelligently during very long conversations without slowing down [[Source: Nvidia DGX Spark or AMD Ryzen AI Max+ 395... | Serverflow Blog](https://serverflow.ru/blog/stati/nvidia-dgx-spark-ili-amd-ryzen-ai-max-395-kakoy-mini-pk-dlya-lokalnykh-llm-vybrat/)].

Of course, not all users are fully satisfied. Tech expert Jeff Geerling pointed out that the device leaves something to be desired in terms of price-to-performance if an average user buys it simply to run language models [[Source: Dell's version of the DGX Spark fixes pain points - Jeff Geerling](https://www.jeffgeerling.com/blog/2025/dells-version-dgx-spark-fixes-pain-points/)]. As a device specialized for professional use, it can be somewhat 'overkill' for the general public.

### What can we expect moving forward?

Moving forward, major manufacturers such as ASUS, Dell, HP, and Lenovo plan to continually release customized versions based on NVIDIA's platform [[Source: NVIDIA Enters The AI PC Realm With DGX Spark & DGX Station...](https://wccftech.com/nvidia-enters-ai-pc-realm-dgx-spark-dgx-station-desktops-72-core-grace-cpu-blackwell-gpus-up-to-784-gb-memory/)]. Furthermore, linking two DGX Spark units over a network allows running ultra-large models with up to 405 billion parameters, demonstrating even greater scalability in the future [[Source: NVIDIA DGX Spark Artificial Intelligence System | AliExpress](https://aliexpress.ru/item/1005010631725345.html)].

### AI's Perspective

Technology truly reaches completion only when hardware and software achieve perfect harmony. While the DGX Spark currently showcases a revolution in hardware, its software refinement remains a work in progress. For tech enthusiasts, watching how quickly NVIDIA improves this software 'recipe' will be just as fascinating as witnessing the impressive performance the device promises.

## References

1. [Nvidia DGX Spark or AMD Ryzen AI Max+ 395... | Serverflow Blog](https://serverflow.ru/blog/stati/nvidia-dgx-spark-ili-amd-ryzen-ai-max-395-kakoy-mini-pk-dlya-lokalnykh-llm-vybrat/)
2. [mac-studio-m5-ultra-vs-nvidia-dgx-spark-local-llms](https://ngxptech.com/mac-studio-m5-ultra-vs-nvidia-dgx-spark-local-llms/)
3. [Ryzen AI Max+ 395 or DGX Spark: Choosing a Mini PC for...](https://digital-razor.ru/media/articles/workstation/dgx-spark-vs-ryzen-ai-max-395/)
4. [Laptop & Workstation Inference Systems | Artificial Analysis](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations)
5. [Test and Review: NVIDIA DGX Spark — Mini PC... - Hardwareluxx Russia](https://www.hardwareluxx.ru/index.php/artikel/hardware/komplettsysteme/58897-test-i-obzor-nvidia-dgx-spark-mini-pk-dlya-ii-v-realnykh-zadachakh.html)
6. [NVIDIA DGX Spark Artificial Intelligence System | AliExpress](https://aliexpress.ru/item/1005010631725345.html)
7. [DGX Spark vs M5 Max MacBook Pro: What to Choose for... | AiManual](https://ai-manual.ru/article/dgx-spark-vs-m5-max-macbook-pro-chto-vyibrat-dlya-lokalnogo-inferensa-i-obucheniya-modelej-v-2025-godu/)
8. [Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
9. [Using NVIDIA DGX Spark with YOLO26 | Ultralytics](https://docs.ultralytics.com/ja/guides/nvidia-dgx-spark)
10. [NVIDIA Enters The AI PC Realm With DGX Spark & DGX Station...](https://wccftech.com/nvidia-enters-ai-pc-realm-dgx-spark-dgx-station-desktops-72-core-grace-cpu-blackwell-gpus-up-to-784-gb-memory/)
11. [TRT LLM for Inference- two Sparks example is VERY slow-DGX...](https://forums.developer.nvidia.com/t/trt-llm-for-inference-two-sparks-example-is-very-slow/348517)
12. [Dell's version of the DGX Spark fixes pain points - Jeff Geerling](https://www.jeffgeerling.com/blog/2025/dells-version-dgx-spark-fixes-pain-points/)