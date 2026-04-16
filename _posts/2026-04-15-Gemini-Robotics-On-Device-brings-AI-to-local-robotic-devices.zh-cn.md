---
layout: post
title: "Wi-Fi断了机器人也能叠衣服？谷歌公开“机器人专用人工智能”的秘密"
description: "通过谷歌 DeepMind 发布的“Gemini Robotics On-Device”技术，了解无需互联网连接即可自主判断并精细动作的机器人未来。"
summary: "谷歌 DeepMind 公开了“Gemini Robotics On-Device”，该技术直接在机器人硬件上运行，无需云端连接即可执行精细任务。"
tags: [机器人学, 人工智能, 谷歌 DeepMind, 端侧 AI, Gemini]
image: 2026-04-15-Gemini-Robotics-On-Device-brings-AI-to-local-robotic-devices.jpg
image_alt: "两只机器人手臂精细地拉开包的拉链或折叠衣服等协助家务劳动的未来主义场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "完全降低互联网依赖性的端侧机器人 AI 的出现，将成为机器人走出受控实验室、进入我们日常客厅和厨房的决定性转折点。这项兼顾安全与速度的技术极有可能成为未来家务机器人的标准。"
quiz:
  - question: "Gemini Robotics On-Device 最显著的特征是什么？"
    choices: ["降低机器人价格", "无需互联网连接，在机器人内部直接运行 AI", "将机器人的电池寿命延长 2 倍"]
    answer: 1
    explanation: "该模型的核心在于无需云端或互联网连接，AI 即可在机器人设备本身本地运行。"
  - question: "该 AI 模型为机器人提供了哪些具体能力？"
    choices: ["超高速行驶能力", "拉开拉链或叠衣服等精细动作", "飞行功能"]
    answer: 1
    explanation: "Gemini Robotics On-Device 旨在执行需要高水平技巧的任务，如拉开拉链、叠衣服等。"
  - question: "该模型主要针对哪种类型的机器人进行了优化？"
    choices: ["带轮子的配送机器人", "拥有双臂的机器人 (bi-arm robots)", "吸尘器形状的机器人"]
    answer: 1
    explanation: "该模型特别针对使用双臂的机器人 (bi-arm robots) 进行了优化。"
lang: zh-cn
ref: 2026-04-15-Gemini-Robotics-On-Device-brings-AI-to-local-robotic-devices
---

如果你在家里用过扫地机器人，可能经历过这种令人沮丧的情况：只要 Wi-Fi 连接稍微不稳定，机器人就会突然停在原地“发呆”，或者即使下达了清扫指令，它也要等好半天才慢吞吞地开始动作。

为什么到目前为止，这些“聪明”的机器人还是如此依赖互联网呢？打个比方，机器人的身体虽然在你家里，但它庞大的大脑——人工智能（AI）却生活在互联网另一端遥远的巨型计算机服务器（云端）中。机器人每当看到眼前的一只袜子并进行判断时，都必须向地球另一端的服务器询问：“我现在看到的是什么？”“下一步该怎么动？”然后等待回答。

但现在，机器人无需互联网这条“生命线”就能自主思考并立即做出反应的时代正在开启。谷歌 DeepMind（Google DeepMind）发布的突破性技术——**“Gemini Robotics On-Device”**正是这一变革的主角 [[Gemini Robotics On-Device 为本地机器人设备带来 AI](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)]。

## 为什么这对我们的生活很重要？

想象一下，在你家的地下室或野营地等互联网信号不佳的地方，你对机器人说：“帮我打开这个包。”如果机器人只是不断重复“正在检查连接状态...”，那该多让人尴尬？

Gemini Robotics On-Device 是一项直接在机器人体内植入非常聪明的“微型大脑”的技术 [[谷歌推出可在机器人本地运行的新 Gemini 模型](https://techcrunch.com/2025/06/24/google-rolls-out-new-gemini-model-that-can-run-on-robots locally/)]。这项技术将改变我们未来的原因主要有三点：

1. **眨眼间的反应速度**：由于无需向外部发送信号，反应速度快如闪电（低延迟，low-latency）。当机器人快要拿不住东西时，它可以实时进行微调，例如立即增加手部力量 [[Gemini Robotics On-Device 为本地机器人设备带来 AI](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)]。
2. **严密的隐私保护**：机器人拍摄的家里角角落落的视频数据无需发送到外部服务器。所有判断都在设备内部完成，从而极大地缓解了隐私泄露的担忧 [[新谷歌 AI 让机器人在没有云的情况下更智能 - 福克斯新闻](https://www.foxnews.com/tech/new-google-ai-makes-robots-smarter-without-cloud)]。
3. **随处可用**：即使在互联网中断的灾难现场或偏远地区，机器人也能像连接了城市高速互联网一样智能地工作 [[Gemini Robotics On-Device 为本地机器人设备带来 AI](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)]。

## 轻松理解：机器人的“观察、理解与行动”大脑

这种新型 AI 在专业术语中被称为**视觉-语言-行动模型（VLA，Vision-Language-Action model）** [[Gemini Robotics On-Device 模型卡](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)]。听起来可能有点复杂，但其实它和我们在日常生活中处理物品的过程是一样的。

*   **视觉 (Vision)**：通过机器人的眼睛（摄像头）“观察”眼前凌乱的衣物。
*   **语言 (Language)**：当人说“帮我把这件衬衫叠好”时，“理解”其意图。
*   **行动 (Action)**：基于理解的内容，“决定”机器人手臂关节转动多少度、以什么速度移动。

这项技术是基于谷歌的移动端人工智能“Gemma”并针对机器人进行了优化 [[Gemini Robotics On-Device 模型卡](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)]。简单来说，它不是请来一位读过图书馆万卷书的天才学者，而是让机器人兜里揣着一份“核心摘要笔记”，同时又培养出一位实战能力无与伦比的“资深现场专家”。

令人惊讶的是，据谷歌称，这个“微型大脑”模型表现出的智能水平与使用庞大云端系统时几乎旗鼓相当 [[谷歌揭秘 Gemini Robotics：机器人端侧 AI 的未来](https://www.analyticsinsight.net/news/google-unveils-gemini-robotics-the-future-of-on-device-ai-for-robots)]。可谓是身材变小但实力依旧的“小巨人”。

## 现状：拉开拉链的精细触感

到目前为止，机器人最难完成的任务之一就是处理“柔软的物体”。搬运坚硬的箱子可以通过数学公式计算，但折叠软塌塌的衣服或捏住小包的拉链头并拉开，则需要像人一样细腻的感觉（灵巧性，dexterity）。

Gemini Robotics On-Device 特别针对**双臂机器人 (bi-arm robots)**进行了设计，使其能像人一样精细地工作 [[Gemini Robotics On-Device 为本地机器人设备带来 AI](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)]。在实际演示中，搭载该 AI 的机器人出色地完成了以下高难度任务 [[Gemini Robotics On-Device 为本地机器人设备带来 AI](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)]：

*   准确找到包上的小拉链头并顺滑地拉开
*   将凌乱的衣物整齐地叠好
*   听取人类自然的语音指令，并快速应对初次遇到的突发状况

谷歌 DeepMind 希望通过该模型，让机器人超越工厂里只会重复单一工作的机器，转变为在我们客厅里能轻松处理万种家务的“通用家务助手” [[DeepMind 的 Gemini Robotics On-Device 为本地机器人设备带来先进 AI...](https://roboticsandautomationnews.com/2025/06/26/google-deepmind-launches-new-vision-language-action-model-to-put-ai-directly-into-local-robotic-devices/92669/)]。

## 未来的机器人世界会是什么样子？

当然，这并不意味着从明天起搭载该技术的机器人就能帮你叠好所有的衣服。目前，谷歌仅向少数选定的合作伙伴和测试者公开该模型，以验证其安全性 [[Gemini Robotics On-Device 模型卡](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)]。

但专家们确信，这次发布将成为彻底改变机器人产业格局的“游戏规则改变者” [[Gemini Robotics On-Device：谷歌为本地机器人带来 AI](https://insighttechtalk.com/tech-news/gemini-robotics-on-device-google-ai-local-robots/)]。因为现在已经有了一套标准，即使不投入昂贵的服务器运营成本，也能以极低的功耗让机器人变得智能。

在不远的将来，如果“无需互联网连接的机器人助手”上市，其核心跳动的必将是这项 Gemini Robotics On-Device 技术。机器人不再依附于互联网，而是独立地陪伴在我们身边的世界，比想象中更近。

---

### MindTickleBytes AI 记者的视角
人工智能切断了名为云端的“脐带”，开始在设备内部自我生存，这意味着机器人正在成为真正意义上的独立存在。现在，机器人不再是那个盯着服务器响应而呆立不动的机器。它们已经准备好成为可靠的伙伴，能即时听懂我们的语言，动作迅捷，并代替我们处理日常琐事。

## 参考资料
1. [Gemini Robotics On-Device 为本地机器人设备带来 AI](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)
2. [DeepMind 的 Gemini Robotics On-Device 为本地机器人设备带来先进 AI...](https://roboticsandautomationnews.com/2025/06/26/google-deepmind-launches-new-vision-language-action-model-to-put-ai-directly-into-local-robotic-devices/92669/)
3. [谷歌推出可在机器人本地运行的新 Gemini 模型](https://techcrunch.com/2025/06/24/google-rolls-out-new-gemini-model-that-can-run-on-robots-locally/)
4. [Gemini Robotics On-Device 模型卡](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)
5. [Gemini Robotics On-Device 为本地机器人设备带来 AI (AiPulseLab)](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)
6. [Gemini Robotics On-Device：谷歌为本地机器人带来 AI](https://insighttechtalk.com/tech-news/gemini-robotics-on-device-google-ai-local-robots/)
7. [谷歌揭秘 Gemini Robotics：机器人端侧 AI 的未来](https://www.analyticsinsight.net/news/google-unveils-gemini-robotics-the-future-of-on-device-ai-for-robots)
8. [新谷歌 AI 让机器人在没有云的情况下更智能 - 福克斯新闻](https://www.foxnews.com/tech/new-google-ai-makes-robots-smarter-without-cloud)
9. [DeepMind 发布新一代机器人 AI 模型：Gemini Robotics On-Device](https://www.aibase.com/news/19215)
10. [AI 机器人：谷歌 DeepMind 的端侧模型 | AI 杂志](https://aimagazine.com/news/google-launches-offline-gemini-ai-model-for-robots)

## 事实核查摘要
- 核查项：19
- 已确认：19
- 结论：通过 (PASS)