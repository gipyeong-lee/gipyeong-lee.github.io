---
layout: post
title: "断网也能“灵活”自如地行动？谷歌全新“端侧”AI将带来的变革"
description: "为您通俗易懂地解释谷歌 DeepMind 发布的 Gemini Robotics On-Device 为何是机器人技术的全新转折点。"
summary: "无需联网即可在机器人内部直接运行的“Gemini Robotics On-Device”AI 现已发布，预示着更快速、更敏捷的机器人时代即将到来。"
tags: [谷歌, DeepMind, AI, 机器人技术, Gemini, 端侧, 技术趋势]
image: 2026-04-14-Gemini-Robotics-On-Device-brings-AI-to-local-robotic-devices.jpg
image_alt: "执行各种任务的机械臂及其内部运行的 AI 芯片构想图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "断开互联网这一‘生命线’后仍能自主判断的机器人的出现，意味着 AI 已走出‘云端’，真正降临到我们身边的物理世界。这不仅仅是性能的提升，更是机器人进化为能够守护人类安全的真正伙伴的关键契机。"
quiz:
  - question: "Gemini Robotics On-Device 的最大特点是什么？"
    choices: ["必须始终保持联网。", "AI 在机器人设备内部直接运行。", "必须由人通过控制器操作。"]
    answer: 1
    explanation: "正如‘端侧（On-Device）’之名，该模型无需互联网或云端连接，即可在机器人设备本身本地运行。"
  - question: "该模型基于谷歌的哪款端侧 AI 模型？"
    choices: ["Gemma", "PowerBot", "Cloud"]
    answer: 0
    explanation: "Gemini Robotics On-Device 是基于谷歌的端侧模型 Gemma 设计的。"
  - question: "Gemini Robotics On-Device 处理的 VLA（视觉-语言-动作）模型的作用是什么？"
    choices: ["仅翻译文本。", "仅绘画。", "集成处理观察（V）、理解（L）和行动（A）的过程。"]
    answer: 2
    explanation: "VLA 模型是指理解视觉信息（Vision） and 语言（Language），并将其转化为机器人具体行动（Action）的架构。"
lang: zh-cn
ref: 2026-04-14-Gemini-Robotics-On-Device-brings-AI-to-local-robotic-devices
---

**想象一下。** 在停电导致断网的工厂，或是在甚至无法接收通信信号的深层地下设施中，机器人需要执行紧急救援任务。到目前为止，大多数机器人的“大脑”（即 AI）都位于遥远的巨型计算机（云端），因此一旦断网，它们就会变成什么也做不了的“砖块”。就像大脑在首尔，身体在釜山，但电话线却被切断了一样。

但现在，机器人无需互联网这一“生命线”也能自主观察、判断和行动的时代正在开启。这要归功于谷歌 DeepMind 发布的新型 AI 模型——**“Gemini Robotics On-Device”**。[Gemini Robotics On-Device brings AI to local robotic devices](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

## 为什么这很重要？

我们在手机上调用 AI 助手时，偶尔会遇到响应延迟的情况对吧？这是因为声音需要通过互联网传送到遥远的服务器，处理完后再把答案传回来。专业术语称之为**延迟（Latency）**。

在日常对话中，1-2 秒的延迟不是大问题，但对于搬运重物或进行精密组装的机器人来说，1 秒的延迟可能会导致严重事故。**“Gemini Robotics On-Device”** 利用机器人体内的图形处理器（本地 GPU）直接运行 AI。[Google announces 'GeminiRoboticsOn-Device... - GIGAZINE](https://gigazine.net/gsc_news/en/20250625-gemini-robotics-on-device/)

**打个比方**，如果说以前的机器人是每次都要打电话问“妈妈，这个放哪儿？”的孩子，那么现在它就是具备了自主判断能力的“独立成年人”。这样一来，即使在网络不稳定或完全没网的地方，机器人也能持续工作，最重要的是它能即时响应，实现更敏捷、更安全的行动。[DeepMind's Gemini Robotics On-Device brings advanced AI to local robots](https://roboticsandautomationnews.com/2025/06/26/google-deepmind-launches-new-vision-language-action-model-to-put-ai-directly-into-local-robotic-devices/92669/)

## 通俗易懂：机器人的“眼、口、手”合而为一

要理解这项技术，必须了解一个核心概念：**VLA（Vision-Language-Action，视觉-语言-动作）**模型。[PDFGemini Robotics On-Device Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)

**简单来说**，它就像资深厨师的“眼”、“脑”、“手”完美联动的一体化系统：

1.  **视觉 (Vision)：** 机器人通过眼睛（摄像头）实时识别眼前的材料和工具。
2.  **语言 (Language)：** 完美理解人类自然的命令，如“把苹果削皮后放在盘子里”。
3.  **行动 (Action)：** 根据命令即时执行移动手臂抓住苹果并使用刀具的精密动作。

以前，这些过程要么是各自独立的，要么需要云端的协助，但 Gemini Robotics On-Device 在机器人内部一次性处理所有这些过程。[Gemini Robotics On-Device: Robotics AI Autonomy to the... - KingyAI](https://kingy.ai/news/gemini-robotics-on-device/) 借此，机器人可以像人一样发挥**“灵巧性 (Dexterity，机器人精细处理物体的能力)”**，即使是初次接触的任务也能快速适应。[Gemini Robotics On-Device brings AI to local robotic devices](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)

这就像我们不需要每次都打电话问父母“苹果怎么削？”，而是直接根据脑子里的知识动手削皮一样。

## 现状：轻量但强大的机器人大脑

Gemini Robotics On-Device 基于谷歌的 **“Gemma”** 模型构建。Gemma 是专为在设备内部轻快运行而设计的 AI 模型，此次的机器人版本则针对机器人控制进行了优化。[PDFGemini Robotics On-Device Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)

该模型的主要特点如下：

*   **无需网络即可运行：** 采用完全不需要云端连接的“无云”方式。[Google rolls out new Gemini model that can run on robots locally](https://techcrunch.com/2025/06/24/google-rolls-out-new-gemini-model-that-can-run-on-robots-locally/)
*   **针对双臂机器人优化：** 特别擅长处理像人一样拥有双臂的“双臂机器人 (bi-arm robots)”双手协作完成复杂任务。[Gemini Robotics On-Device brings AI to local robotic devices](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)
*   **通用性：** 不仅限于特定制造商的机器人，其设计灵活，可广泛应用于各种类型的机器人和环境。[Google Introduces Gemini Robotics On-Device AI Model, Can Adapt to Different Types of Robots](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pGX282NERoSGpuN1A2ZnpScUNDZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)
*   **执行复杂指令：** 处理如“拿起这个放入那个箱子并盖上盖子”之类的多步骤指令的能力远超现有的端侧模型。[Gemini Robotics On-Device also outperforms other on-device alternatives on more challenging out-of-distribution tasks and complex multi-step instructions.](https://yalladevelopment.services/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

目前，该模型仅面向谷歌信任的少数合作伙伴和测试人员开放，正处于严谨验证实际现场性能的阶段。[PDFGemini Robotics On-Device Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)

## 未来会怎样？

专家认为，这次发布将成为机器人行业的 **“游戏规则改变者 (Game Changer)”**。[Gemini Robotics: Google Brings AI to Local Robots](https://insighttechtalk.com/tech-news/gemini-robotics-on-device-google-ai-local-robots/) 因为它能一次性解决此前让人们对引入机器人犹豫不决的高昂维护成本、通信安全问题以及慢得令人抓狂的响应速度。

在不远的将来，我们将更频繁地看到在餐厅服务的机器人能即时避开客人的突然动作而不洒出食物，或者在没有信号的大型仓库角落默默整理库存的聪明机器人。[Google Launches Gemini Robotics On-Device AI: Robots Go Offline, Stay Smart](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pGX282NERoSGpmVzIxSXBIVlNDZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en)

谷歌 DeepMind 的这次尝试，将是 AI 从屏幕上的文字或图像进化为能在我们这样的物理空间中安全、敏捷行动的真正“伙伴”的重要一步。机器人不再仅仅是“机器”，而是能听懂我们的话并做出英明决策的“智能助手”，这一天似乎近在咫尺。

---

## 参考资料

1. [Gemini Robotics On-Device brings AI to local robotic devices](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)
2. [DeepMind's Gemini Robotics On-Device brings advanced AI to local robots](https://roboticsandautomationnews.com/2025/06/26/google-deepmind-launches-new-vision-language-action-model-to-put-ai-directly-into-local-robotic-devices/92669/)
3. [Google rolls out new Gemini model that can run on robots locally](https://techcrunch.com/2025/06/24/google-rolls-out-new-gemini-model-that-can-run-on-robots locally/)
4. [PDFGemini Robotics On-Device Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)
5. [Gemini Robotics On-Device brings AI to local robotic devices - AIPulse Lab](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)
6. [Gemini Robotics On-Device: Google Brings AI to Local Robots - Insight Tech Talk](https://insighttechtalk.com/tech-news/gemini-robotics-on-device-google-ai-local-robots/)
7. [Google Introduces Gemini Robotics On-Device AI Model, Can Adapt to Different Types of Robots - Google News](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pGX282NERoSGpuN1A2ZnpScUNDZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)
8. [Gemini Robotics On-Device also outperforms other on-device alternatives... - Yalla Development](https://yalladevelopment.services/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)
9. [Google announces 'GeminiRoboticsOn-Device... - GIGAZINE](https://gigazine.net/gsc_news/en/20250625-gemini-robotics-on-device/)
10. [Gemini Robotics On-Device: Robotics AI Autonomy to the... - KingyAI](https://kingy.ai/news/gemini-robotics-on-device/)
11. [Google Launches Gemini Robotics On-Device AI: Robots Go Offline, Stay Smart - Google News](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pGX282NERoSGpmVzIxSXBIVlNDZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en)