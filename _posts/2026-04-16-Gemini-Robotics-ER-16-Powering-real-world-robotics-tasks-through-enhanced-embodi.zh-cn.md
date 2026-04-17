---
layout: post
title: "机器人也开始学会'察言观色'了？谷歌全新机器人大脑 Gemini Robotics-ER 1.6 正式发布"
description: "本文将为您深入浅出地介绍谷歌 DeepMind 发布的最新机器人 AI 模型 Gemini Robotics-ER 1.6，以及它如何减少机器人错误并提升工业现场效率。"
summary: "谷歌 DeepMind 发布了最新 AI 模型 Gemini Robotics-ER 1.6，大幅提升了机器人的空间理解和任务成功判断能力，开启了机器人自主纠错及识别工业仪表盘的新时代。"
tags: [谷歌DeepMind, 机器人学, AI, Gemini, 机器人智能, 人工智能新闻]
image: 2026-04-16-Gemini-Robotics-ER-16-Powering-real-world-robotics-tasks-through-enhanced-embodi.jpg
image_alt: "机器人手臂在复杂的工业现场执行精密作业，并通过摄像头多角度分析周围环境"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "我们正跨入‘思考型机器人’的时代，机器人不再仅仅是听命行事，而是能够自主判断任务是否成功并理解周围环境的语境。这将成为机器人走出实验室、成为现实世界真正伙伴的重要转折点。"
quiz:
  - question: "Gemini Robotics-ER 1.6 相比之前的 1.5 或 Gemini 3.0 Flash，有哪些显著优势？"
    choices: ["计算速度快 100 倍", "空间及物理推理能力大幅提升", "增加了语言翻译功能"]
    answer: 1
    explanation: "相比之前的模型，Gemini Robotics-ER 1.6 在指向、物体计数及任务成功检测等空间和物理推理能力方面有了显著改进。"
  - question: "为了确认任务是否正确完成，机器人整合多台摄像机信息的功能名称是？"
    choices: ["多视图成功检测 (Multi-view success detection)", "超级视觉系统", "机器人之眼"]
    answer: 0
    explanation: "通过整合安装在天花板和机器人手腕上的多个角度的影像来确认任务完成情况的功能被称为‘多视图成功检测’。"
  - question: "本次发布的模型在工业现场非常实用的新能力之一是？"
    choices: ["清理工厂地面", "读取工业仪表盘（仪表）", "与其他机器人交流"]
    answer: 1
    explanation: "Gemini Robotics-ER 1.6 具备了全新的‘仪器读取 (Instrument reading)’能力，可以读取模拟仪表盘或透明管中的液位。"
lang: zh-cn
ref: 2026-04-16-Gemini-Robotics-ER-16-Powering-real-world-robotics-tasks-through-enhanced-embodi
---

想象一下。你让机器人“把桌子上的那个红色杯子拿给我”。机器人虽然努力伸出手臂，但由于被自己的手臂挡住了视线，实际上并看不清是否抓住了杯子。最终，机器人抓了个空却认为任务已完成，理直气壮地回来了。对于之前的机器人来说，“现实世界”就是这样一个充满了意外变量和视觉死角的棘手场所。虽然能很好地执行命令，但却缺乏确认自己是否做好了工作的“眼力劲（察言观色）”。

但现在，机器人终于开始学会“察言观色”了。谷歌 DeepMind 于 2026 年 4 月 14 日正式发布了充当机器人大脑的最新 AI 模型 **“Gemini Robotics-ER 1.6”** [Gemini Robotics-ER 1.6: What Google’s New Robotics Model Does](https://www.junia.ai/blog/gemini-robotics-er-1-6) [Google DeepMind Launches Gemini Robotics-ER 1.6 with Improved ...](https://www.rockingrobots.com/google-deepmind-launches-gemini-robotics-er-1-6-with-improved-spatial-reasoning-and-instrument-reading/)。该模型不仅能让机器人执行命令，更标志着机器人能够“推理”所处环境并自主判断任务成功与否，迈出了具有里程碑意义的一步。

## 为什么这很重要？

到目前为止，机器人更像是按照预定指令移动的“精密机器”。在工厂流水线等一切固定的环境中表现完美，但只要物体稍微倾斜或光线昏暗，它们很快就会迷失方向并停下来。尤其是机器人学界最大的课题之一，就是让机器人能够感知“我现在是否正确完成了这项工作？” [Google DeepMind Unveils Gemini Robotics-ER 1.6: A Leap in ...](https://www.humanoidsdaily.com/news/google-deepmind-unveils-gemini-robotics-er-1-6-a-leap-in-spatial-reasoning-and-industrial-utility)。

Gemini Robotics-ER 1.6 正是为了解决这一课题而诞生的。该模型赋予了机器人 **“具身推理 (Embodied Reasoning，即机器人物理理解自身身体结构与周围环境关系的能力)”** [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)。简单来说，机器人现在可以做出灵活的判断，比如：“啊，现在我的手臂挡住了视线看不见物体，我得稍微转一下头确认一下。”

这种变化预示着工业现场将迎来创新浪潮。因为机器人无需人类逐一干预即可自主规划复杂流程，即使发生错误也能立即察觉并重新尝试，说出“我再试一次！”之类的话 [GeminiRobotics-ER1.6— Google DeepMind](https://deepmind.google/models/gemini-robotics/gemini-robotics-er/)。

## 通俗易懂：Gemini Robotics-ER 1.6 的三大核心能力

谷歌 DeepMind 将本次模型的核聚焦在三个领域 [Google DeepMind Launches Gemini Robotics-ER 1.6 with Improved ...](https://www.rockingrobots.com/google-deepmind-launches-gemini-robotics-er-1-6-with-improved-spatial-reasoning-and-instrument-reading/)。让我们结合生活场景来详细了解一下：

### 1. 能够心领神会“帮我拿那个”的空间推理 (Pointing-based Reasoning)
以前，必须用“移动到 X 坐标 120，Y 坐标 50”等复杂的数字告诉机器人物体的位置。但搭载了 ER 1.6 模型的机器人，即使人类只是随手一指或说“把那个角落的东西拿过来”，它也能完美理解其中的语境。打个比方，这就好比一个每次都得输入地址才敢开车的初学者，现在变成了只要听到“停在那个蓝色招牌旁边”就能精准泊车的老司机。其识别指向、物体计数以及计算抓取物体的最佳角度的能力，比之前的模型要精细得多 [GeminiRobotics-ER1.6:Poweringreal-worldroboticstasks...](https://onmine.io/gemini-robotics-er-1-6-powering-real-world-robotics-tasks-through-enhanced-embodied-reasoning/) [Gemini Robotics: Bringing AI into the PhysicalWorld](https://arxiv.org/html/2503.20020v1)。

### 2. “如果我有好几只眼睛？”多视图成功检测 (Multi-view Success Detection)
这项功能是本次更新的核心，也是赋予机器人“眼力劲”的关键技术。机器人完成任务后，会同时分析安装在天花板上的摄像头影像和安装在自己手腕上的摄像头影像 [Google DeepMind Unveils Gemini Robotics-ER 1.6: A Leap in ...](https://www.humanoidsdaily.com/news/google-deepmind-unveils-gemini-robotics-er-1-6-a-leap-in-spatial-reasoning-and-industrial-utility)。这就像我们确认身后的物体时会照镜子或转身从多个角度观察一样。当移动被箱子挡住的物体时，如果一只眼睛（摄像头）看不见，它会用另一只眼睛斜睨确认，自主检查任务是否真的完美结束 [Google DeepMind Unveils Gemini Robotics-ER 1.6: A Leap in ...](https://www.humanoidsdaily.com/news/google-deepmind-unveils-gemini-robotics-er-1-6-a-leap-in-spatial-reasoning-and-industrial-utility)。

### 3. “模拟仪表盘也不在话下”仪器读取 (Instrument Reading)
老旧的工厂或设备中仍有许多指针式的模拟仪表盘或显示液位的玻璃管。对于传统机器人来说，这些只是毫无意义的图案或复杂的纹理，但 ER 1.6 能够观察并准确读取当前数值 [Gemini Robotics-ER 1.6: What Google’s New Robotics Model Does](https://www.junia.ai/blog/gemini-robotics-er-1-6)。无需安装昂贵的数字传感器，机器人巡检时就能报告“现在的压力太高了！”。这就像是让机器人考取了“安全管理员”证书一样。

## 现状：进展如何？

Gemini Robotics-ER 1.6 已经做好了投入实际应用的准备。特别是全球著名的机器人公司 **波士顿动力 (Boston Dynamics)** 的机器人也已经整合了这项 Gemini AI 技术并正在进行测试 [GoogleGeminiAI integrated into Boston Dynamicsrobots- Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lRcVBQMEVCSDJXV1M3RVlPOEV5Z0FQAQ?hl=en-US&gl=US&ceid=US:en)。

在性能方面也表现出了惊人的增长。根据谷歌的测试结果，1.6 版本在空间和物理推理能力上不仅超过了之前的 1.5 版本，甚至优于最新的通用 AI 模型 Gemini 3.0 Flash [GeminiRobotics-ER1.6:Poweringreal-worldroboticstasks...](https://onmine.io/gemini-robotics-er-1-6-powering-real-world-robotics-tasks-through-enhanced-embodied-reasoning/)。它甚至能够完成像精细折纸这样极其微妙的动作 [Google DeepMind’s new AI models helprobotsperform physicaltasks...](https://www.theverge.com/news/628021/google-deepmind-gemini-robotics-ai-models)。

目前，该模型已通过 Google AI Studio 和 Gemini API 向全球开发者开放。这意味着现在任何人都可以利用这个强大的“机器人大脑”来打造属于自己的智能机器人 [Google DeepMind Launches Gemini Robotics-ER 1.6 with Improved ...](https://www.rockingrobots.com/google-deepmind-launches-gemini-robotics-er-1-6-with-improved-spatial-reasoning-and-instrument-reading/) [Google DeepMind Gemini Robotics-ER 1.6 via Gemini API ...](https://www.siliconreport.com/google-deepmind-puts-gemini-robotics-er-1-6-into-the-gemini-api-7ccaf115118f7272)。

## 未来会怎样？

专家们评价此次发布为 **“空间推理和工业应用能力的巨大飞跃”** [Google DeepMind Unveils Gemini Robotics-ER 1.6: A Leap in ...](https://www.humanoidsdaily.com/news/google-deepmind-unveils-gemini-robotics-er-1-6-a-leap-in-spatial-reasoning-and-industrial-utility)。机器人正在从单纯默默执行命令的仆人，进化为能够自主判断形势、运用自如工具并审查结果的“智能体” [Google DeepMind Gemini Robotics-ER 1.6 via Gemini API ...](https://www.siliconreport.com/google-deepmind-puts-gemini-robotics-er-1-6-into-the-gemini-api-7ccaf115118f7272)。

在不远的将来，我们可能会在工厂见到自主管理流程并检查仪表盘的智能机器人，或者在家里见到能自主安排家务顺序并解决问题的可靠机器人助手。谷歌的 Gemini Robotics-ER 1.6 将是让机器人成为我们生活中真正伙伴的关键一步 [Google DeepMind LaunchesGeminiRobotics-ER1.6- Colitco](https://colitco.com/google-deepmind-gemini-robotics-er-1-6-1504202625/)。

---

### AI 视角 (AI's Take)
**MindTickleBytes AI 记者视角：** 赋予机器人“身体”不仅仅是增加机械装置，更是 AI 全身心地学习受物理定律支配的现实世界的过程。Gemini Robotics-ER 1.6 是一个强烈的信号，表明 AI 已经超越了屏幕上的文字和图片，开始理解并与我们立足的真实世界进行交互。拥有“眼力劲”的机器人最终将成为更懂人类的机器人。

---

## 参考资料
1. [GeminiRoboticsER1.6:EnhancedEmbodiedReasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)
2. [GeminiRobotics-ER1.6— Google DeepMind](https://deepmind.google/models/gemini-robotics/gemini-robotics-er/)
3. [GoogleGeminiAI integrated into Boston Dynamicsrobots- Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lRcVBQMEVCSDJXV1M3RVlPOEV5Z0FQAQ?hl=en-US&gl=US&ceid=US:en)
4. [GeminiRobotics-ER1.6:Poweringreal-worldroboticstasks...](https://onmine.io/gemini-robotics-er-1-6-powering-real-world-robotics-tasks-through-enhanced-embodied-reasoning/)
5. [GeminiRobotics-ER1.6|GeminiAPI | Google AI for Developers](https://ai.google.dev/gemini-api/docs/robotics-overview)
6. [GeminiRobotics: Bringing AI into the PhysicalWorld](https://arxiv.org/html/2503.20020v1)
7. [Building the Next Generation of Physical Agents withGemini...](https://developers.googleblog.com/en/building-the-next-generation-of-physical-agents-with-gemini-robotics-er-15/)
8. [Gemini Robotics-ER 1.6: What Google’s New Robotics Model Does](https://www.junia.ai/blog/gemini-robotics-er-1-6)
9. [Google DeepMind Unveils Gemini Robotics-ER 1.6: A Leap in ...](https://www.humanoidsdaily.com/news/google-deepmind-unveils-gemini-robotics-er-1-6-a-leap-in-spatial-reasoning-and-industrial-utility)
10. [Google DeepMind Launches Gemini Robotics-ER 1.6 with Improved ...](https://www.rockingrobots.com/google-deepmind-launches-gemini-robotics-er-1-6-with-improved-spatial-reasoning-and-instrument-reading/)
11. [Google DeepMind Gemini Robotics-ER 1.6 via Gemini API ...](https://www.siliconreport.com/google-deepmind-puts-gemini-robotics-er-1-6-into-the-gemini-api-7ccaf115118f7272)
12. [Google DeepMind LaunchesGeminiRobotics-ER1.6- Colitco](https://colitco.com/google-deepmind-gemini-robotics-er-1-6-1504202625/)
13. [Google unveilsGeminiRoboticsfor building general purposerobots](https://9to5google.com/2025/03/12/gemini-robotics/)
14. [Google DeepMind’s new AI models helprobots perform physical tasks...](https://www.theverge.com/news/628021/google-deepmind-gemini-robotics-ai-models)