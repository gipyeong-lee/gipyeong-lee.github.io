---
layout: post
title: "桌面上的 AI 超级计算机，NVIDIA DGX Spark 为何变慢了？"
description: "探究 NVIDIA 小型 AI 计算机 DGX Spark 的性能问题、核心特性及其在实际应用中的潜力。"
summary: "NVIDIA 超小型 AI 超级计算机 DGX Spark 在 Linux 环境下遭遇固件性能瓶颈，但目前正通过最新的软件更新寻求解决方案。"
tags: [AI, NVIDIA, DGXSpark, 人工智能, 科技]
image: 2026-11-04-Nvidia-DGX-Spark-encrypted-firmware-slows-inference-speed-to-35-on-Linux.jpg
image_alt: "放置在桌面上、设计时尚的小型计算机 NVIDIA DGX Spark"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是前沿 AI 技术走出数据中心的过程中所经历的成长期阵痛。为了充分释放硬件潜力，软件优化已变得比以往任何时候都更加关键。"
quiz:
  - question: "NVIDIA DGX Spark 支持的统一内存容量是多少？"
    choices: ["64 GB", "128 GB", "256 GB"]
    answer: 1
    explanation: "DGX Spark 配备了 128 GB 的 LPDDR5X 统一内存。"
  - question: "连接两台 DGX Spark 后，最多可以运行拥有多少参数的模型？"
    choices: ["1000亿个", "2000亿个", "4050亿个"]
    answer: 2
    explanation: "通过 NVIDIA ConnectX 技术连接两台设备，最多可处理拥有 4050 亿个参数的模型。"
  - question: "当推理速度变慢时，文中提到的有效解决方法是什么？"
    choices: ["重启硬件", "使用最新的 TensorRT-LLM 发布镜像", "更换网络线缆"]
    answer: 1
    explanation: "使用最新的 TensorRT-LLM 发布镜像 (1.2.0rc1) 后，初期设置中存在的推理速度缓慢问题得到了显著改善。"
lang: zh-cn
ref: 2026-11-04-Nvidia-DGX-Spark-encrypted-firmware-slows-inference-speed-to-35-on-Linux
---

想象一下：早上醒来，你对智能手机的 AI 助手说：“请帮我总结并整理今天需要处理的复杂工作资料。”过去，这项任务必须经过庞大的数据中心处理，但现在，放在桌上的一个小盒子就能轻松搞定一切。这听起来像梦一样，而 NVIDIA 推出的超小型 AI 超级计算机“DGX Spark”正在开启这种可能性。然而，最近有消息称，这款强悍的设备因与软件配合的问题而出现了性能下降。究竟发生了什么？

### 为什么这很重要？

DGX Spark 的重大意义在于，它将以往只有在数据中心才能看到的“Grace Blackwell”架构的强大性能带到了普通用户的桌面上 [[出处：Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)]。这意味着开发者、研究人员和机器人工程师无需租用昂贵的大型服务器机房，即可在本地环境中直接运行高性能 AI 模型 [[出处：NVIDIA Enters The AI PC Realm With DGX Spark & DGX Station...](https://wccftech.com/nvidia-enters-ai-pc-realm-dgx-spark-dgx-station-desktops-72-core-grace-cpu-blackwell-gpus-up-to-784-gb-memory/)]。

然而，无论硬件性能多么卓越，如果软件无法跟上，对用户而言也只是摆设。最近有报告称在某些环境下，推理（AI 生成回答的过程）速度显著变慢，这再次证明了软件优化对于释放硬件潜力的重要性 [[出处：TRT LLM for Inference- two Sparks example is VERY slow-DGX...](https://forums.developer.nvidia.com/t/trt-llm-for-inference-two-sparks-example-is-very-slow/348517)]。

### 通俗地比喻

为了理解 DGX Spark，我们以厨房为例。想象一位能力超群的厨师（Grace Blackwell 架构）进入了一个极小的厨房（150 × 150 × 50.5 毫米的机身） [[出处：Тест и обзор: NVIDIA DGX Spark — мини-ПК... - Hardwareluxx Russia](https://www.hardwareluxx.ru/index.php/artikel/hardware/komplettsysteme/58897-test-i-obzor-nvidia-dgx-spark-mini-pk-dlya-ii-v-realnykh-zadachakh.html)]。这位厨师具备处理海量食材（数据）的顶尖能力。

但厨师要做出佳肴，必须要有“食谱（软件/TensorRT-LLM）”。最近在 Linux 环境下出现的推理速度变慢问题，是因为厨师虽然能力强，却被要求执行错误的食谱。幸运的是，NVIDIA 通过提供新的食谱（最新的发布镜像），帮助厨师恢复了应有的速度 [[出处：TRT LLM for Inference- two Sparks example is VERY slow-DGX...](https://forums.developer.nvidia.com/t/trt-llm-for-inference-two-sparks-example-is-very-slow/348517)]。

### 目前状况如何？

目前，DGX Spark 正凭借 128 GB 的 LPDDR5X 统一内存完成着极其复杂的任务 [[出处：Laptop & Workstation Inference Systems | Artificial Analysis](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations)]。例如，使用 FP4 技术可以将“Qwen3.6-72B”这样的大型语言模型以 4 比特格式加载，仅占用约 35 GB 的内存。其余 90 GB 以上的内存可用于 AI 上下文记忆，即使在极长的对话中，也能在不损失速度的情况下智能响应 [[出处：Nvidia DGX Spark или AMD Ryzen AI Max+ 395... | Блог Serverflow](https://serverflow.ru/blog/stati/nvidia-dgx-spark-ili-amd-ryzen-ai-max-395-kakoy-mini-pk-dlya-lokalnykh-llm-vybrat/)]。

当然，并非所有用户都完全满意。科技博主 Jeff Geerling 指出，对于只想单纯运行语言模型的普通用户来说，这款机器的性价比尚有提升空间 [[出处：Dell's version of the DGX Spark fixes pain points - Jeff Geerling](https://www.jeffgeerling.com/blog/2025/dells-version-dgx-spark-fixes-pain-points/)]。作为专为专业人士设计的设备，对普通消费者而言可能有些“过剩”。

### 未来有何期待？

未来，华硕（ASUS）、戴尔（Dell）、惠普（HP）、联想（Lenovo）等大型制造商将继续基于 NVIDIA 的这一平台推出各具特色的版本 [[出处：NVIDIA Enters The AI PC Realm With DGX Spark & DGX Station...](https://wccftech.com/nvidia-enters-ai-pc-realm-dgx-spark-dgx-station-desktops-72-core-grace-cpu-blackwell-gpus-up-to-784-gb-memory/)]。此外，通过网络连接两台 DGX Spark，甚至可以运行高达 4050 亿参数的超大规模模型，其扩展潜力在未来只会进一步提升 [[出处：NVIDIA DGX Spark Система искусственного интеллекта | AliExpress](https://aliexpress.ru/item/1005010631725345.html)]。

### AI 的一句话点评

当硬件与软件完美融合时，技术才算真正完成。DGX Spark 目前展示了硬件领域的革命，但在软件细节的打磨上仍有提升空间。对于科技爱好者来说，密切关注 NVIDIA 多快能完善这些软件“食谱”，其精彩程度绝对不亚于设备本身带来的性能震撼。

## 参考资料

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