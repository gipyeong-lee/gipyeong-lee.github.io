---
layout: post
title: "机器人终于能像人类一样行动了吗？谷歌 Gemini Robotics 2.5 闪亮登场"
description: "通过谷歌 DeepMind 最新机器人 AI——Gemini Robotics 2.5 在工厂一线展现的惊人灵巧度与提升后的作业速度，一探即将来临的机器人未来。"
summary: "谷歌 DeepMind 公布的 Gemini Robotics 2.5 相比前代模型，任务成功率最高提升了 100%，作业速度缩短了 30%，并在实际工厂场景中创下了 96% 的成功率记录，显著增强了机器人的实际灵巧性。"
tags: [AI, 机器人工程, 谷歌DeepMind, Gemini]
image: 2026-11-11-Gemini-Robotics-25-accelerates-real-world-general-dexterity.jpg
image_alt: "应用了谷歌 DeepMind Gemini Robotics 2.5 技术、正在执行复杂任务的仿人机器人"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Gemini Robotics 2.5 不仅仅是变得更聪明，它还证明了“具身智能”在物理世界中实际执行任务的可能性。我们离看到在身边默默协助工作的机器人同事的日子又近了一步。"
quiz:
  - question: "与前代模型相比，谷歌 Gemini Robotics 2.5 有哪些改进？"
    choices: ["提升了任务成功率并缩短了作业速度", "电池寿命延长了两倍", "设计了全新的机器人硬件"]
    answer: 0
    explanation: "Gemini Robotics 2.5 根据不同任务，成功率最高提升了 100%，处理速度也快了 20% 到 30%。"
  - question: "像 Gemini Robotics 2.5 这样的 VLA 模型通过什么来决定机器人的行为？"
    choices: ["仅分析历史数据日志", "结合摄像头输入值与指令", "仅使用用户的语音指令"]
    answer: 1
    explanation: "VLA（视觉-语言-动作）模型通过结合摄像头看到的视觉信息和给定的指令，输出机器人的动作。"
  - question: "在工厂现场，搭载 Gemini Robotics 2.5 的机器人创下了多少百分比的成功率？"
    choices: ["85%", "90%", "96%"]
    answer: 2
    explanation: "在奔驰工厂的测试中，Apptronik 的仿人机器人 Apollo 2 利用 Gemini Robotics 2.5 实现了 96% 的任务成功率。"
lang: zh-cn
ref: 2026-11-11-Gemini-Robotics-25-accelerates-real-world-general-dexterity
---

想象一下：在堆满复杂零部件的工厂工作台上，机械臂毫不犹豫地直接挑选出所需的零件，或是瞬间完成以前必须由人工完成的精细打结作业。过去，机器人更像是只会重复既定路径的“简单机器”，但现在，它们正在蜕变为能够自行分析情况并采取行动的“聪明劳动力”。

2026 年 11 月 10 日，谷歌 DeepMind 公布了将机器人智能推向新高度的“Gemini Robotics 2.5”。这是谷歌迄今为止推出的性能最强大的视觉-语言-动作（VLA, Vision-Language-Action）模型 [[参考资料 9](https://codingislove.com/gemini-robotics-2-5/), [参考资料 12](https://arxiv.org/abs/2503.20020)]。

## 为什么这很重要？

机器人不仅仅擅长重复劳动，如果它们能理解环境并展现出“灵巧性（Dexterity）”，将预示着我们的工业现场和日常生活将发生巨大变化。过去的机器人大多专注于特定工序，只要情况稍有变化，就必须由人工介入重新设定代码 [[参考资料 5](https://www.linkedin.com/posts/aslam-ahamed_artificialintelligence-ai-robotics-activity-7490016683873542144-3VmV)]。但现在，机器人通过感知环境并自行判断，能够执行更为通用的任务。

特别是在物流中心的分类工作或工厂的复杂组装线上，如果机器人能像人类一样，甚至比人类更快地执行精密作业，生产力将得到飞跃性的提升。

## 通俗易懂：拥有“眼睛”和“大脑”的机器人

打个比方，Gemini Robotics 2.5 就像是给机器人装上了“情境判断力”和“灵活的手指”。如果说以前的机器人是被蒙住眼睛、只能按既定指令移动的玩偶，那么搭载该模型的机器人则是通过摄像头（眼睛）拍下并查看周边情况，人工智能（大脑）判断视频中应该做什么，然后驱动机械臂（手）做出即时动作 [[参考资料 9](https://codingislove.com/gemini-robotics-2-5/)]。

其核心 VLA 模型的作用是将“视觉（Vision）”信息与“语言（Language）”指令相结合，转化为机器人的“动作（Action）”。这与我们阅读食谱（语言）、用眼睛确认食材状态（视觉）、然后切菜（动作）的过程非常相似。得益于此，机器人在复杂环境下也能自行寻找并执行任务 [[参考资料 10](https://deepmind.google/models/gemini-robotics/)]。

## 现状：用数字证明性能

Gemini Robotics 2.5 已经在实际现场证明了它的能力。据谷歌 DeepMind 称，与前几代机器人模型相比，该模型根据任务内容的不同，将工作成功率提高了 30% 到 100% [[参考资料 12](https://arxiv.org/abs/2503.20020)]。

令人惊讶的是速度。不仅成功率提高了，完成作业的时间也比以往快了 20% 到 30% [[参考资料 12](https://arxiv.org/abs/2503.20020)]。在梅赛德斯-奔驰工厂进行的试点运营中，Apptronik 的仿人机器人“Apollo 2”搭载 Gemini Robotics 2.5 后，创下了 96% 的惊人成功率 [[参考资料 11](https://blockchain.news/news/gemini-robotics-2-5-enhances-dexterity-safety), [参考资料 12](https://arxiv.org/abs/2503.20020)]。

## 未来将会怎样？

谷歌的目标是通过这项技术，使机器人成为在物理世界中更加通用和有用的存在。从 Gemini Robotics 2.0 模型开始，不仅能控制仿人机器人的全身，多台机器人相互协作在同一空间内工作也已成为可能 [[参考资料 10](https://deepmind.google/models/gemini-robotics/)]。

当然，这并不意味着“物理通用人工智能（Physical AGI）”已经到来。因为还有安全问题和技术难题需要解决 [[参考资料 5](https://www.linkedin.com/posts/aslam-ahamed_artificialintelligence-ai-robotics-activity-7490016683873542144-3VmV), [参考资料 12](https://arxiv.org/abs/2503.20020)]。但从技术发展的速度来看，机器人安全、精准地在我们身边替代人类工作的未来，已不再遥远。

## AI 的思考

Gemini Robotics 2.5 不仅仅是变得更聪明，它还证明了“具身智能”在物理世界中实际执行任务的可能性。我们离看到在身边默默协助工作的机器人同事的日子又近了一步。

## 参考资料

1. [Gemini Robotics 2.5 accelerates real-world general dexterity](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)
2. [Gemini— Google DeepMind | Our next era of frontier intelligence](https://deepmind.google/models/gemini/)
3. [Google Just Unveiled Gemini Robotics, and It's a Whole New Level of...](https://lilys.ai/en/notes/gemini-robotics-20251020/google-unveils-gemini-robotics-ai-humanoid)
4. [Google DeepMind's Gemini Robotics 2 boosts AI accuracy... | LinkedIn](https://www.linkedin.com/posts/aslam-ahamed_artificialintelligence-ai-robotics-activity-7490016683873542144-3VmV)
5. [Google reveals Gemini Robotics 2.0, promising improved dexterity and safety | AIBlog.com.my](https://aiblog.com.my/articles/google-reveals-gemini-robotics-20-promising-improved-dexterity-and-safety)
6. [Gemini Robotics 2 advances dexterity](https://newsletter.dotika.ai/p/gemini-robotics-2-advances-dexterity)
7. [Google DeepMind releases Gemini Robotics 2.5 for robot dexterity](https://codingislove.com/gemini-robotics-2-5/)
8. [Gemini Robotics — Google DeepMind](https://deepmind.google/models/gemini-robotics/)
9. [Gemini Robotics 2.5 Enhances Dexterity and Safety in Real ...](https://blockchain.news/news/gemini-robotics-2-5-enhances-dexterity-safety)
10. [Gemini 2.5 for robotics and embodied intelligence - Google ...](https://arxiv.org/abs/2503.20020)