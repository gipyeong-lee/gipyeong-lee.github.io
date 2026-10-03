---
layout: post
title: "我的MacBook里竟然有2840亿参数的智能？Redis创始人打造的超高速AI引擎 ds4"
description: "介绍Redis创始人Salvatore Sanfilippo开源的AI推理引擎ds4。本文简述了在个人电脑上运行高性能AI模型DeepSeek V4 Flash的技术背景及其深远意义。"
summary: "Redis创始人Salvatore Sanfilippo开发了一款名为“ds4”的C语言推理引擎，让个人电脑也能快速运行大型AI模型。"
tags: [AI, 技术, Redis, 本地LLM, 编程]
image: 2026-10-03-From-the-creator-of-Redis-run-LLM-locally-with-ds4.jpg
image_alt: "象征开发者在个人笔记本电脑上运行大型AI模型的工作环境图片"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这一事件具有极高的象征意义，标志着大型AI模型的主导权正从科技巨头的云端API向个人本地环境转移。"
quiz:
  - question: "Salvatore Sanfilippo开发的ds4引擎的主要特点是什么？"
    choices: ["网页浏览器专用执行器", "由纯C语言编写的高速推理引擎", "基于Python的数据分析工具"]
    answer: 1
    explanation: "ds4是为了最大化性能而由纯C语言编写的推理引擎。"
  - question: "ds4引擎在个人MacBook上可运行的代表性模型是什么？"
    choices: ["DeepSeek V4 Flash", "图像生成模型Stable Diffusion", "语音转换模型Whisper"]
    answer: 0
    explanation: "ds4专为高效在本地运行DeepSeek V4 Flash等模型而设计。"
  - question: "ds4为了硬件加速，支持哪些技术？"
    choices: ["仅支持软件模拟", "支持Metal、CUDA、ROCm等多种平台", "仅在特定云服务器上运行"]
    answer: 1
    explanation: "ds4支持Metal、CUDA、ROCm等多种平台的加速。"
lang: zh-cn
ref: 2026-10-03-From-the-creator-of-Redis-run-LLM-locally-with-ds4
---

想象一下。早上醒来坐在笔记本电脑前，对人工智能说：“请根据昨天整理的方案，帮我制作一份会议资料。”通常，这类任务需要经过大型企业的服务器，不仅有隐私顾虑，速度也可能受限。但如果这个庞大的智能直接在你的笔记本电脑里运行，会怎样？

Redis（全球开发者钟爱的超高速数据存储库）的创始人Salvatore Sanfilippo，也就是大家熟知的“antirez”，发布了一项能让这个梦想成为现实的有趣技术，即“ds4”项目。[来源: LocalLLMInference](https://www.linkedin.com/pulse/open-rebellion-running-weight-models-locally-andrea-guaccio-a9wgf)

## 这为何重要？(Why It Matters)

此前，在我们的个人电脑上运行大型AI模型几乎是不可能的。人工智能模型拥有数千亿个参数（Parameter，即AI学习并调整的数值），通常只能通过谷歌或OpenAI等科技巨头拥有的服务器（云API）来使用。这对开发者或企业来说，不仅存在成本问题，在数据外传带来的安全方面也是一大阻碍。

然而，Sanfilippo推出的ds4打破了对“云API”的垄断，为在日常设备上运行高性能AI开辟了道路。[来源: LocalLLMInference](https://www.linkedin.com/pulse/open-rebellion-running-weight-models-locally-andrea-guaccio-a9wgf) 现在，无需将敏感数据发送到外部服务器，你就能在自己的笔记本电脑上直接运行智能AI模型了。

## 轻松理解 (The Explainer)

要理解ds4，需要掌握“推理引擎”的概念。人工智能完成学习后对问题进行回答的过程称为“推理”，而ds4就是专门负责这一过程的“汽车引擎”般的程序。

打个比方，如果人工智能模型是一本巨型百科全书，ds4就是能在该百科全书中以最快速度找到答案并读出来的“超高速阅读助手机器人”。为了将性能发挥到极致，Sanfilippo用“纯C语言”从零开始重写了这个机器人。[来源: ds4Review: antirez's Pure-C DeepSeek V4 Flash Engine — andrew.ooo](https://andrew.ooo/posts/ds4-antirez-deepseek-v4-flash-local-inference-review/) 使用编程语言的基石C语言，展现了他要毫无浪费地榨干硬件性能100%潜力的决心。

此外，该引擎能高效处理名为“DeepSeek V4 Flash”的大型模型。该模型拥有高达2840亿个参数，相当于调节并思考着相当于韩国总人口3万倍的数据量。[来源: DeepSeek V4 FlashLocal:Runa 284B Frontier Model on... | aratech](https://aratech.ae/blog/deepseek-v4-flash-local-ds4)

## 当前现状 (Where We Stand)

目前，ds4在苹果MacBook（尤其是搭载128GB RAM以上的机型）上表现出了令人瞩目的性能。[来源: DeepSeek V4 FlashLocal:Runa 284B Frontier Model on... | aratech](https://aratech.ae/blog/deepseek-v4-flash-local-ds4) 在搭载M3 Max芯片的MacBook上，它能以每秒生成26个词（token）的速度运行，且是在处理100万上下文长度的情况下达成的。[来源: ds4by antirez:localcoding agent on DeepSeek V4 Flash thatrunson...](https://artka.dev/en/blog/local-coding-agent/)

不仅如此，ds4在设计时就考虑到了兼容性，不仅支持苹果的“Metal（苹果图形加速技术）”，还支持英伟达的CUDA、AMD的ROCm等多种硬件环境。[来源: HackerNews– Telegram](https://t.me/hackernewslive/233253) 不仅是MacBook用户，拥有高性能显卡的PC用户也能从中受益。目前虽针对DeepSeek V4 Flash进行了优化，但也支持GLM 5.x或Qwen3.8 Flash Next等其他模型。[来源: HackerNews– Telegram](https://t.me/hackernewslive/233253)

## 未来展望 (What's Next)

未来，我们将从“租用AI”的时代迈向“在自己电脑上直接运行AI”的时代。随着ds4等技术的不断进步，即使在断网状态下，我们也能随时与笔记本电脑里的智能AI助手进行交流。

特别是开发者们，现在可以直接在自己的设备上运行“本地代码代理”，构建个性化的开发环境。[来源: ds4by antirez:localcoding agent on DeepSeek V4 Flash thatrunson...](https://artka.dev/en/blog/local-coding-agent/) 人工智能正变得越来越小巧、高效且强大，其舞台正从大型数据中心转移到你的桌面上。

## MindTickleBytes AI记者观点

通过Redis改变了全球服务器基础设施的Sanfilippo，这次开启了大型AI模型“本地化”的新纪元。对于习惯了大型科技公司API所提供便利的我们，ds4再次唤醒了“数据主权”和“性能优化”这些本质价值。

## 参考资料

1. [FromthecreatorofRedis;runLLMlocallywithds4| Modern Orange](https://modernorange.io/item/49936575)
2. [Vue HN 2.0 |FromthecreatorofRedis;runLLMlocallywithds4](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49936575)
3. [LocalLLMInference](https://www.linkedin.com/pulse/open-rebellion-running-weight-models-locally-andrea-guaccio-a9wgf)
4. [DeepSeek V4 FlashLocal:Runa 284B Frontier Model on... | aratech](https://aratech.ae/blog/deepseek-v4-flash-local-ds4)
5. [ds4Review: antirez's Pure-C DeepSeek V4 Flash Engine — andrew.ooo](https://andrew.ooo/posts/ds4-antirez-deepseek-v4-flash-local-inference-review/)
6. [ds4by antirez:localcoding agent on DeepSeek V4 Flash thatrunson...](https://artka.dev/en/blog/local-coding-agent/)
7. [Hacker News |FromthecreatorofRedis;runLLMlocallywithds4](https://nilaykhandelwal.com/item/49936575)
8. [FromthecreatorofRedis;runLLMlocallywithds4Comments...](https://vk.ru/wall-238001904_6824)
9. [antirez lanceds4: le moteur d'inférencelocalqui... — AI-master.dev](https://ai-master.dev/en/article/antirez-lance-ds4-le-moteur-dinference-local-qui-rend-deepseek-v4-flash-utilisab)
10. [HackerNews– Telegram](https://t.me/hackernewslive/233253)