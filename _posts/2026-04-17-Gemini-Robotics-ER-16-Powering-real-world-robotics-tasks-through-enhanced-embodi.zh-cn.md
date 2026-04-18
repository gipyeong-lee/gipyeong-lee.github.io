---
layout: post
title: "如果机器人拥有了“常识”？谷歌发布全新 AI 模型 Gemini Robotics-ER 1.6"
description: "机器人能否超越简单的指令执行，进入自主判断和确认的时代？为您通俗易懂地解读谷歌 DeepMind 发布的最新机器人 AI 模型 Gemini Robotics-ER 1.6 带来的变革。"
summary: "谷歌 DeepMind 发布了 Gemini Robotics-ER 1.6，为机器人赋予了类似人类“常识”的推理能力，将工业现场的自主性提升到了一个新高度。"
tags: [谷歌DeepMind, 机器人AI, Gemini, 人工智能, 技术趋势]
image: 2026-04-17-Gemini-Robotics-ER-16-Powering-real-world-robotics-tasks-through-enhanced-embodi.jpg
image_alt: "在工业现场检查仪表并执行任务的智能机器人形象"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这标志着 AI 已从单纯理解屏幕上的文本和图像，进化到在现实物理世界中成为人类“手脚”并直接行动的阶段，是一个重要的里程碑。这意味着 AI 正在超越简单的自动化，演变为具有物理实体的“智能体（Agent）”。"
quiz:
  - question: "与旧版本或 Gemini 3.0 Flash 相比，Gemini Robotics-ER 1.6 特别强化了哪项能力？"
    choices: ["外语翻译能力", "空间及物理推理能力", "音乐创作能力"]
    answer: 1
    explanation: "Gemini Robotics-ER 1.6 在空间推理、物体指向、计数以及任务成功检测等物理世界推理能力方面，较之前版本有了显著提升。"
  - question: "本次模型强调的新功能之一，机器人自主确认任务是否完成的功能是？"
    choices: ["成功检测 (Success Detection)", "自动充电 (Auto Charging)", "语音识别 (Voice Recognition)"]
    answer: 0
    explanation: "机器人自主判断是否真正完成了所下达指令的“成功检测”功能，是提高自主机器人可靠性的核心要素。"
  - question: "波士顿动力的“Spot”机器人通过该模型实现了哪项新的工业任务？"
    choices: ["送咖啡", "读取工业仪表（计量器）", "工厂地面清洁"]
    answer: 1
    explanation: "搭载 Gemini Robotics-ER 1.6 的 Spot 机器人现在能够读取工厂内的压力表或视镜，并自主检查设备状态。"
lang: zh-cn
ref: 2026-04-17-Gemini-Robotics-ER-16-Powering-real-world-robotics-tasks-through-enhanced-embodi
---

我们身边的机器人其实并没有想象中那么聪明。工厂里的机械臂只能机械地移动到固定位置，扫地机器人偶尔会被低矮的门槛卡住，无法彻底清扫，甚至动弹不得。它们所缺乏的正是我们人类拥有的**“常识”**。

比如“去拿杯子时如果前面有障碍物要绕过去”或者“地板上有水可能会滑，要小心”这种极其自然的逻辑。对于目前的机器人来说，这种判断仍然是极其困难的课题。

然而，2026 年 4 月 14 日，谷歌 DeepMind（Google DeepMind）发布了一个可以为机器人植入这种“常识”的新大脑，即 **Gemini Robotics-ER 1.6** [Gemini Robotics-ER 1.6: 谷歌新款机器人模型的功能解析](https://www.junia.ai/blog/gemini-robotics-er-1-6) [DeepMind 的 Gemini Robotics-ER 1.6 让 Spot 能够读取仪表 - WinBuzzer](https://winbuzzer.com/2026/04/16/google-deepmind-gemini-robotics-er-1-6-autonomous-industrial-inspections-xcxwbn/)。今天我们将深入浅出地探讨为什么这款人工智能被誉为改变机器人技术未来的“游戏规则改变者”，以及它将为我们的生活带来哪些变化。

## 为什么这很重要？

到目前为止，机器人大多是根据计算机代码编写的精确“手册”来行动的。但我们生活的现实世界非常复杂，存在无数变量。一旦遇到手册中没有的突发情况，机器人往往会停止工作或做出令人费解的行为。

Gemini Robotics-ER 1.6 为机器人赋予了 **具身推理 (Embodied Reasoning)** 能力 [Gemini Robotics-ER 1.6: 通过增强的具身推理助力现实世界机器人任务](https://deepmind.google/blog/gemini-robotics-er-1-6/) [DeepMind 的 Gemini 1.6 为机器人带来指向点击现实... | ...](https://robohorizon.com/en-us/news/2026/04/deepminds-gemini-16-gives-robots-point-and-click-reality/)。简单来说，“具身推理”是指机器人能够实时理解自己的身体和周围环境并自主做出判断的能力。

打个比方，它正从一台单纯听命行事的机器，进化为一个能观察情况并判断“啊，现在这样做才对”的智能“代理（Agent）” [Gemini Robotics-ER 1.6 | Gemini API | 谷歌 AI 开发者文档](https://ai.google.dev/gemini-api/docs/robotics-overview)。这意味着在工厂或危险的工业现场，机器人可以在没有人类帮助的情况下，更安全、更完美地自主工作 [Gemini Robotics-ER 1.6: 现实世界的机器人智能](https://www.labellerr.com/blog/gemini-robotics-er-1-6-explained/)。

## 易于理解：机器人的“眼睛”和“大脑”

Gemini Robotics-ER 1.6 是一种 **视觉语言模型 (Vision-Language Model, VLM)** [Gemini Robotics-ER 1.6 | Gemini API | 谷歌 AI 开发者文档](https://ai.google.dev/gemini-api/docs/robotics-overview)。这意味着它能同时理解眼睛看到的图像信息和我们使用的日常语言，并将其联系起来。我们可以通过三个比喻来解释该模型的核心能力。

### 1. “在脑海中绘制地图的能力”（空间推理）
想象一下，当你在深夜漆黑的房间里去洗手间时，即使不开灯，也能凭借记忆推测家具的位置并巧妙避开。该模型通过整合来自多个摄像头的复杂视频，使机器人能立体地感知其所处的空间（多摄像头推理） [Gemini Robotics-ER 1.6: 现实世界的机器人智能](https://www.labellerr.com/blog/gemini-robotics-er-1-6-explained/)。它不仅仅是在拍照，而是深度“理解”：“那个物体在我身后，这面墙是我可以穿过的空间” [Gemini Robotics-ER 1.6: 谷歌新款机器人模型的功能解析](https://www.junia.ai/blog/gemini-robotics-er-1-6)。

### 2. “确认作业是否完成的细致性”（成功检测）
许多机器人在收到抓取物品的指令时，仅仅是执行伸出手臂的动作。即使中间物品掉了，它也会认为“我已经伸过手了，任务完成！”并进入下一步。但该模型具备 **成功检测 (Success detection)** 功能 [Gemini Robotics-ER 1.6: 通过增强的具身推理助力现实世界机器人任务](https://deepmind.google/blog/gemini-robotics-er-1-6/) [DeepMind 的 Gemini Robotics-ER 1.6 将具身 AI 推向现实世界](https://gadgetbond.com/google-deepmind-gemini-robotics-er-1-6-embodied-ai-reasoning-model/)。在完成工作后，它会自主确认“物品真的被正确移动了吗？”，如果失败了，它会重新尝试或停止操作 [Gemini Robotics-ER 1.6: 谷歌新款机器人模型的功能解析](https://www.junia.ai/blog/gemini-robotics-er-1-6)。

### 3. “以专家眼光读取仪表”（仪表读取）
工业现场有很多指针式压力表或显示油量的玻璃管（视镜）。对于普通机器人来说，这些可能只是复杂的图画，但 Gemini Robotics-ER 1.6 可以准确读出这些刻度当前的含义 [DeepMind 的 Gemini Robotics-ER 1.6 让 Spot 能够读取仪表 - WinBuzzer](https://winbuzzer.com/2026/04/16/google-deepmind-gemini-robotics-er-1-6-autonomous-industrial-inspections-xcxwbn/) [DeepMind 的 Gemini Robotics-ER 1.6 将具身 AI 推向现实世界](https://gadgetbond.com/google-deepmind-gemini-robotics-er-1-6-embodied-ai-reasoning-model/)。这水平就像是一位经验丰富的工厂管理员在亲自检查设备。

## 现状：‘Spot’变聪明了

该模型由 Laura Graesser 和 Peng Xu 等谷歌顶尖研究人员开发，目前已应用于实际机器人中并取得了惊人的成果 [Gemini Robotics-ER 1.6: 通过增强의 具身推理助力现实世界机器人任务](https://deepmind.google/blog/gemini-robotics-er-1-6/)。

特别是波士顿动力著名的机器人狗“Spot”，得益于该模型，它现在能够自主巡检工厂，读取各种仪表并精确检查设备状态 [DeepMind 的 Gemini Robotics-ER 1.6 让 Spot 能够读取仪表 - WinBuzzer](https://winbuzzer.com/2026/04/16/google-deepmind-gemini-robotics-er-1-6-autonomous-industrial-inspections-xcxwbn/)。在物理推理能力（物体指向、计数、轨迹预测等）方面，它的性能远超之前的 Gemini Robotics-ER 1.5 或高性能模型 Gemini 3.0 Flash [Gemini Robotics-ER 1.6: 助力现实世界机器人任务...](https://onmine.io/gemini-robotics-er-1-6-powering-real-world-robotics-tasks-through-enhanced-embodied-reasoning/) [Gemini Robotics: 将 AI 带入物理世界](https://arxiv.org/html/2503.20020v1)。

现在，如果你对机器人说“请检查那个红色阀门旁边的压力表”，机器人已经达到了能完美理解其含义并立即付诸行动的水平 [Gemini Robotics-ER 1.6 | Gemini API | 谷歌 AI 开发者文档](https://ai.google.dev/gemini-api/docs/robotics-overview)。

## 未来会怎样？

谷歌 DeepMind 的这次发布是一个重要的信号，表明机器人正走出实验室，走向我们真正的生活“现场”。

在不久的将来，搭载该模型的机器人将首先被派往人类极难进入的放射性设施或有毒气体泄漏现场。机器人将不再仅仅扮演传输现场画面的角色，而是能够做出“气体数值处于危险水平，将立即关闭主阀门”这类高层次的判断并完成任务 [Gemini Robotics-ER 1.6: 现实世界的机器人智能](https://www.labellerr.com/blog/gemini-robotics-er-1-6-explained/)。

此外，这些技术将成为开发更通用机器人的坚实基础。不仅是在工厂，我们有望在家庭中也更快地见到能利索地协助处理复杂家务的“真正聪明的机器人助手” [谷歌发布 Gemini Robotics 用于构建通用机器人](https://9to5google.com/2025/03/12/gemini-robotics/)。

## AI 的视角

**想象一下：** 早上起床说一句“帮我查一下冰箱里牛奶的保质期，把客厅乱放的东西归位”，机器人就会自动完成家务。如果说之前的 AI 只是在屏幕中通过文本和图像对话的“聪明秘书”，那么通过 Gemini Robotics-ER 1.6，它终于获得了“理解世界并能行动的身体”。

这种将人类语言转化为实际物理行动的惊人技术，在不久的将来，将把我们在科幻电影中梦寐以求的“与机器人共存”变为日常现实。AI 终于走出了电脑，开始与我们并肩而行。

---

## 参考资料

1. [Gemini Robotics ER 1.6: 增强的具身推理](https://deepmind.google/blog/gemini-robotics-er-1-6/)
2. [Gemini Robotics-ER 1.6 | Gemini API | 谷歌 AI 开发者文档](https://ai.google.dev/gemini-api/docs/robotics-overview)
3. [Gemini Robotics-ER 1.6 - The Keyword](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-1-6/)
4. [Gemini Robotics-ER 1.6: 现实世界的机器人智能](https://www.labellerr.com/blog/gemini-robotics-er-1-6-explained/)
5. [DeepMind 的 Gemini 1.6 为机器人带来指向点击现实... | ...](https://robohorizon.com/en-us/news/2026/04/deepminds-gemini-16-gives-robots-point-and-click-reality/)
6. [Gemini Robotics-ER 1.6: 谷歌新款机器人模型的功能解析](https://www.junia.ai/blog/gemini-robotics-er-1-6)
7. [DeepMind 的 Gemini Robotics-ER 1.6 让 Spot 能够读取仪表 - WinBuzzer](https://winbuzzer.com/2026/04/16/google-deepmind-gemini-robotics-er-1-6-autonomous-industrial-inspections-xcxwbn/)
8. [DeepMind 的 Gemini Robotics-ER 1.6 将具身 AI 推向现实世界](https://gadgetbond.com/google-deepmind-gemini-robotics-er-1-6-embodied-ai-reasoning-model/)
9. [Google 新闻 - Google DeepMind 发布 Gemini Robotics-ER...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lRcVBQMEVCSDJXV1M3RVlPOEV5Z0FQAQ?hl=en-US&gl=US&ceid=US:en)
10. [Gemini Robotics-ER 1.6: 助力现实世界机器人任务...](https://onmine.io/gemini-robotics-er-1-6-powering-real-world-robotics-tasks-through-enhanced-embodied-reasoning/)
11. [Gemini Robotics: 将 AI 带入物理世界](https://arxiv.org/html/2503.20020v1)
12. [谷歌发布 Gemini Robotics 用于构建通用机器人](https://9to5google.com/2025/03/12/gemini-robotics/)
13. [利用 Gemini Robotics-ER 1.5 构建下一代物理智能体](https://developers.googleblog.com/en/building-the-next-generation-of-physical-agents-with-gemini-robotics-er-15/)