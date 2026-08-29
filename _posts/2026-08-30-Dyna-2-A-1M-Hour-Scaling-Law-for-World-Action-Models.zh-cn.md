---
layout: post
title: "如果机器人也能拥有170年的经验？Dyna-2证实的AI学习定律"
description: "AI 'Dyna-2' 通过学习100万小时的人类日常生活视频，为机器人学习引入了全新的缩放定律。"
summary: "Dyna-2 是首个通过学习100万小时人类行为视频，证明机器人学习具有可预测性能提升定律的“世界-动作模型”。"
tags: [AI, 机器人学, Dyna-2, 深度学习]
image: 2026-08-30-Dyna-2-A-1M-Hour-Scaling-Law-for-World-Action-Models.jpg
image_alt: "通过100万小时庞大数据进行学习的机器人AI抽象概念图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在机器人领域证实数据量直接决定性能这一规律是一个里程碑式的事件。现在，最重要的问题将变成：我们该教给机器人什么。"
quiz:
  - question: "Dyna-2 模型是通过什么进行预训练的？"
    choices: ["机器人直接执行的数据", "100万小时以上的人类视角视频", "虚拟仿真环境"]
    answer: 1
    explanation: "Dyna-2 选择了学习100万小时以上的人类视角（egocentric）视频，以将人类行为传递给机器人。"
  - question: "100万小时的学习数据折合成人类经验约为多少？"
    choices: ["约17年", "约170年", "约1700年"]
    answer: 1
    explanation: "100万小时的学习数据折合成人类在清醒状态下的经验时间，相当于170年之久。"
  - question: "Dyna-2 证实的缩放定律（Scaling Law）的核心是什么？"
    choices: ["增加数据性能也不会变化", "增加数据性能会停滞", "增加数据量，机器人的性能会按可预测方式提升"]
    answer: 2
    explanation: "Dyna-2 首次证实，随着人类数据量的增加，机器人的性能不会停滞（plateau），而是持续提升。"
lang: zh-cn
ref: 2026-08-30-Dyna-2-A-1M-Hour-Scaling-Law-for-World-Action-Models
---

想象一下，如果你把你出生以来所看到、所经历的所有日常行为都毫无保留地展示给AI机器人，会发生什么？从早晨冲泡咖啡的手部动作，到开门关门的方式，再到搬运沉重箱子的技巧。就像孩子通过观察父母的背影来学习世界一样，机器人能否通过观察人类的日常生活来自主学习？最近，一个AI模型对这个问题给出了非常有趣的答案。这就是来自 Dyna Robotics 的“Dyna-2”。

### 为什么这很重要？

长期以来，机器人学习领域一直被数据匮乏这堵巨大的高墙所阻碍。像 ChatGPT 这样的语言模型通过学习互联网上的海量文本而飞速发展，但机器人需要在“现实世界”中直接行动，因此极难获得高质量的大规模数据。然而，Dyna-2 通过人类在日常生活中拍摄的超过100万小时的视频，解决了这一难题。

这不仅仅是让机器人变得更聪明，更是可能改变机器人开发范式的大事件。现在，我们不再需要为机器人编写每一项动作代码或强迫它们进行数千次试错，而是仅仅通过向它们展示人类生活的方式，就能以可预测的方式提升机器人的能力。

### 简单理解：“170年的经验”一次性习得

Dyna-2 被称为“世界-动作模型（World-Action Model, WAM）”。该模型可以同时推断视频中接下来会出现什么画面（Next-frame），以及在那个场景下机器人应该采取什么样的动作（Next-action） [出处: Dyna Robotics unveils DYNA-2 World-Action Model - Robotics 24/7](https://www.robotics247.com/article/dyna-robotics-unveils-dyna-2-world-action-model)。

打个比方，就像你看着电影，当主角抓住门把手时，你自然会预测“啊，接下来他要开门了”。Dyna-2 通过学习100万小时的海量视频，掌握了这种“常识”。这相当于人类在清醒状态下不眠不休地积累了170年的经验 [出处: Dyna Robotics Introduces Dyna-2 - A World-Action Model pre-trained on 1 million hours of human video](https://www.marktechpost.com/2026/08/13/dyna-robotics-introduces-dyna-2-a-world-action-model-pre-trained-on-1-million-hours-of-human-video/)。

重点在于，这些学习数据不是机器人的视频，而是“人”的视频。通过这种方式，Dyna-2 自发领悟了“如何将人类行为传递给机器人”的方法。它首次在机器人领域将“随着人类数据增加，机器人的实际操作能力会持续提升而不会停滞”的“缩放定律（Scaling Law，数据量与性能之间的数学关系）”正式化 [出处: Dyna Robotics DYNA-2: 1M hours of human video, robot scaling law](https://theroboticsmedia.com/article/dyna-robotics-dyna-2-world-action-model-1-million-hours-human-video-scaling-law-august-10-2026)。

### 现状：进展到什么程度了？

Dyna-2 于2026年8月初发布，主要学习了以人类视角拍摄的第一人称视频（egocentric video） [出处: Dyna Robotics Introduces Dyna-2: A World-Action Model...](https://www.marktechpost.com/2026/08/13/dyna-robotics-introduces-dyna-2-a-world-action-model-pre-trained-on-1-million-hours-of-human-video/)。

简单来说，机器人不是用机器人的眼睛，而是用“人的眼睛”去看世界并进行学习的。据目前所知，在将数据量从1000小时增加到100万小时的实验中，它表现出了惊人的性能提升，且没有任何停滞迹象 [出处: Dyna Robotics DYNA-2: 1M hours of human video, robot scaling law](https://theroboticsmedia.com/article/dyna-robotics-dyna-2-world-action-model-1-million-hours-human-video-scaling-law-august-10-2026)。这意味着机器人学习中也成立了像语言模型那样的公式——“数据输入越多，性能确定性越好”。当然，要完美处理现实世界复杂的物理定律还需要进一步研究，但至少已经明确了“方向” [出处: Dyna-2: A 1-Million-Hour Scaling Law for World-Action Models](https://www.dyna.co/dyna-2)。

### 未来会怎样？

Dyna-2 的出现正在加速机器人成为“通用劳动力”的未来 [出处: Dyna-2: A 1-Million-Hour Scaling Law for World-Action Models...](https://www.linkedin.com/posts/ahmedbeshry_dyna-2-a-1-million-hour-scaling-law-for-activity-7493018378123493376-sTuq)。由于研究人员已经证明了增加人类数据直接等同于提升机器人性能，未来围绕“获取更多样化、高质量的人类活动视频”的竞争将会变得异常激烈。

各位读者需要关注的一点是：机器人正从只会重复特定工作的简单“机器”，进化为基于所见所学自主判断的“智能代理”。现在的机器人不再仅仅遵循编程指令，而是正在成为能够共享人类经验并进行模仿的合作伙伴。

### MindTickleBytes 的 AI 记者视角

Dyna-2 的这项研究是机器人工程界“淘金热”开始的信号。通过100万小时的数据规模证明机器人学习的可预测性，这将成为未来机器人能够真正融入人类生活的最大技术基石。在一个数据即智能的时代，期待下一代机器人能以多么自然的方式帮助我们。

## 参考资料

1. [Dyna-2: A 1-Million-Hour Scaling Law for World-Action Models](https://www.dyna.co/dyna-2)
2. [DYNA-2 Scaling Law: 1M Hours of Human Video, No Robots ...](https://explainx.ai/blog/dyna-2-world-action-model-robotics-scaling-law-august-2026)
3. [Dyna-2 Proves Scaling Laws for Robotics: 1 Million Hours of ...](https://www.humanoidsdaily.com/news/dyna-2-proves-scaling-laws-for-robotics-1-million-hours-of-human-video-unlocks-zero-shot-dexterity)
4. [Dyna-2: A 1-Million-Hour Scaling Law for World-Action Models](https://vuink.com/post/dyna-d-dco)
5. [Dyna Robotics DYNA-2: 1M hours of human video, robot scaling law](https://theroboticsmedia.com/article/dyna-robotics-dyna-2-world-action-model-1-million-hours-human-video-scaling-law-august-10-2026)
6. [Ep#99: DYNA-2: A 1 Million Hour Scaling Law for World-Action ...](https://robopapers.substack.com/p/ep99-dyna-2-a-1-million-hour-scaling)
7. [Training Dyna-2 at million-hour scale, repeatably — DYNA](https://www.dyna.co/research/dyna-2-infrastructure)
8. [Dyna-2: A 1-Million-Hour Scaling Law for World-Action Models...](https://paperswithcode.co/paper/109035)
9. [Dyna Robotics Introduces Dyna-2: A World-Action Model...](https://www.marktechpost.com/2026/08/13/dyna-robotics-introduces-dyna-2-a-world-action-model-pre-trained-on-1-million-hours-of-human-video/)
10. [Thread By @DynaRobotics - Today we are introducing Dyna-2,..](https://unrollnow.com/status/2086856327150858298)
11. [Dyna-2: A 1-Million-Hour Scaling Law for World-Action Models...](https://www.linkedin.com/posts/ahmedbeshry_dyna-2-a-1-million-hour-scaling-law-for-activity-7493018378123493376-sTuq)
12. [Dyna Robotics trains DYNA-2 on more than 1 million hours of human...](https://runtimewire.com/article/dyna-robotics-dyna-2-human-video-robotics-scaling-law)
13. [Dyna Robotics Introduces Dyna-2 Trained on Million Hours of Video...](https://digg.com/tech/agunxv0a)
14. [Dyna Robotics trains robots on one million hours of... - Cryptopolitan](https://www.cryptopolitan.com/dyna-robotics-robots-1m-hours-of-human-video/)
15. [Dyna Robotics unveils DYNA-2 World-Action Model- Robotics 24/7](https://www.robotics247.com/article/dyna-robotics-unveils-dyna-2-world-action-model)
16. [Dyna-2's Million-Hour World-Action Model | Action Trajectories](https://actiontrajectories.com/resources/dyna-2-million-hour-scaling-law)