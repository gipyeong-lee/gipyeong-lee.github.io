---
layout: post
title: "AI 知道汽车和飞机的共同点吗？像人类一样看“世界”的 AI 诞生了"
description: "介绍让 AI 超越单纯辨别物体、像人类一样理解世界的新研究。带您了解 Google DeepMind 的世界模型以及韩国研究团队的创新技术。"
summary: "通过向在物体识别方面是天才、但在抽象概念方面表现欠佳的 AI 教导“人类视觉”，开启了构建更智能、更安全的人工智能之旅。"
tags: [人工智能, DeepMind, 世界模型, 机器学习, 技术趋势]
image: 2026-05-03-Teaching-AI-to-see-the-world-more-like-we-do.jpg
image_alt: "通过机器人的眼睛观察到的世界像人类大脑神经网络一样连接在一起，展现出把握复杂物体间关系的状态"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "如果 AI 学会了人类的常识，我们将不再需要担心 AI 的“荒唐错误”。比起数据量，植入“类人思维方式”才是通往真正智能的必经之路。"
quiz:
  - question: "目前的 AI 系统在辨别数百种车型时，会忽略什么？"
    choices: ["汽车的准确发动机功率", "汽车和飞机都是金属制交通工具这一共同点", "汽车轮胎的品牌名称"]
    answer: 1
    explanation: "根据 Google DeepMind 的说法，AI 虽然擅长识别单个物体，但在把握“金属制的大型交通工具”等抽象共同点或关系方面存在困难。"
  - question: "AI 为了理解周围环境如何运作而进行的“大脑模拟”称为什么？"
    choices: ["虚拟现实 (Virtual Reality)", "图像处理 (Image Processing)", "世界模型 (World Models)"]
    answer: 2
    explanation: "世界模型是指 AI 在内部表达并模拟环境运行原理的系统。"
  - question: "由韩国延世大学研究团队参与开发，协助计算机像人类大脑一样处理图像的技术是？"
    choices: ["Lp-卷积 (Lp-Convolution)", "数据标注 (Data Annotation)", "科学游戏 (Scientific Game)"]
    answer: 0
    explanation: "Lp-卷积是一项让计算机能更像人类大脑一样处理图像的突破性技术。"
lang: zh-cn
ref: 2026-05-03-Teaching-AI-to-see-the-world-more-like-we-do
---

各位，请想象一下。你面前有一个最新型的人工智能 (AI)。这个 AI 堪称“汽车博主”，能在短短一秒钟内辨认出世界上存在的数百种汽车品牌和型号。然而，当你问这个聪明的 AI “汽车和飞机有什么相似之处？”时，它却答不上来，或者满口胡言。对于我们人类来说再自然不过的常识——“它们都是金属制的大型交通工具”，对这个 AI 来说竟然是世界上最难的问题。[教 AI 像我们一样看世界 - deepmind.google](https://deepmind.google/blog/teaching-ai-to-see-the-world-more-like-we-do/)

这就是当今 AI 面临的一道巨大的墙，即所谓的**“认知差距 (Perception Gap)”**。[教 AI 通过人类的眼睛看世界：弥补认知差距...](https://joshuaberkowitz.us/blog/news-1/teaching-ai-to-see-the-world-through-human-eyes-bridging-the-perception-gap-1784) 简单来说，AI 就像是一个能背下数万本书的背诵天才，但却完全不知道书中的内容与我们的生活有什么关系。表面上看起来它比人类聪明得多，但观察世界的方式却与我们截然不同，因此偶尔会犯下令人啼笑皆非的错误。然而，最近全球的科学家们为了缩小这一差距，开始教导 AI “人类的眼睛”和“人类的常识”。

## 为什么这很重要？ (Why It Matters)

你可能会问：“AI 只要能准确辨认汽车型号就行了，知道它和飞机相似有那么重要吗？”但这个问题不仅仅是回答智力竞赛题的水平，它直接关系到我们每天使用的 AI 的**安全性**。

目前的 AI 虽然非常聪明，但同时也有一个致命的弱点：不可预测性。[世界模型：目前 AI 领域最重要的 10 件事 | MIT 技术评论](https://www.technologyreview.com/2026/04/21/1135650/world-models-ai-artificial-intelligence/) 虽然其识别物体和分类模式的能力超越了人类，但它无法理解其中蕴含的深刻关系或抽象概念。[教 AI 通过人类的眼睛看世界：弥补认知差距...](https://joshuaberkowitz.us/blog/news-1/teaching-ai-to-see-the-world-through-human-eyes-bridging-the-perception-gap-1784)

举个例子。假设一辆自动驾驶汽车在道路上遇到了一个“空纸箱”。人类司机会做出常识性的判断：“那是轻飘飘的纸，直接开过去也很安全”或者“不知道里面装了什么，还是避开吧”。但如果 AI 仅仅将其识别为“方形数据模式”，当出现从未见过的箱子形态时，它可能无法区分那是岩石还是纸张，从而导致事故风险。

因此，将 AI 与人类知识体系相匹配的“对齐 (Aligning)”工作，是让 AI 在任何情况下都能保持稳健 (Robustness)，并使其能自如适应从未教过的全新情况 (Generalize) 的核心钥匙。[教 AI 像人类一样看世界 —— Google DeepMind](https://aifuturethinkers.com/teaching-ai-to-see-the-world-more-like-humans-do-google-deepmind/)

## 易于理解：教导 AI “常识”的三种方法

科学家们为了给 AI 移植人类的视觉系统，主要采用了三种创新的策略。

### 1. 在大脑中运行“模拟”：世界模型 (World Models)
当你早上醒来，即使闭着眼睛也能生动地想象出厕所在哪里，或者打开玄关门后会展现出什么样的走廊。这是因为我们大脑中存有世界如何运作的“地图”或“运行原理”。

赋予 AI 这种想象力的正是**“世界模型 (World Models)”**。[世界模型：教 AI 像人类一样思考 - LinkedIn](https://www.linkedin.com/pulse/world-models-teaching-ai-think-like-humans-abhishek-banerjee-wakhe) 这意味着 AI 不再像拍照一样单纯存储周围环境，而是构建一个能够自我预测环境将如何变化的内部系统。[世界模型：教 AI 像人类一样思考 - LinkedIn](https://www.linkedin.com/pulse/world-models-teaching-ai-think-like-humans-abhishek-banerjee-wakhe) 这样它就具备了提前在大脑中进行模拟的能力：“如果我推这个杯子，它会掉到地上摔碎吧？”

### 2. 复制大脑的过滤器：Lp-卷积 (Lp-Convolution)
我们的大脑拥有一种非常高效的过滤器，能从海量的视觉信息中精准筛选出重要的信息。最近，延世大学、基础科学研究所 (IBS) 以及德国马克斯·普朗克研究所的联合研究团队推出了一项名为**“Lp-卷积 (Lp-Convolution)”**的技术，协助计算机能够更像人类大脑一样处理图像。[AI 地平线：教计算机像人类一样观察世界](https://theticker.org/16359/science/ai-horizons-teaching-computers-to-view-the-world-like-humans-do/)

比喻来说，这就像是给 AI 戴上了一副人类在观察世界时所使用的“特殊眼镜”。戴上这副眼镜后，AI 也能在处理信息时优先考虑人类认为重要的物体轮廓或立体感，从而实现更自然的识别。

### 3. 通过游戏学习认知：布朗大学的研究
美国布朗大学 (Brown University) 的研究人员正在以一种非常有趣的方式教育 AI。那就是通过“游戏”来教导它如何像人类一样感知。[研究人员正在教 AI 像人类一样观察 —— MSN](https://www.msn.com/en-us/news/technology/researchers-are-teaching-ai-to-see-more-like-humans/ar-AA1H2LFn) 就像小孩通过玩积木学习世界的物理定律一样，AI 也在虚拟世界的游戏中触摸并移动各种物体，积累与人类相似的视觉逻辑。[训练 AI 像人类一样观察 —— 美国国家科学基金会](https://www.nsf.gov/news/training-ai-see-more-humans)

## 现状 (Where We Stand)

就在此时此刻，Google DeepMind 正在加速研究，并在国际学术期刊《自然 (Nature)》上发表了深度研究结果，分析了 AI 与人类在组织视觉信息方式上的差异。[教 AI 像人类一样看世界 —— Google DeepMind](https://aifuturethinkers.com/teaching-ai-to-see-the-world-more-like-humans-do-google-deepmind/)

但坦诚地说，路还很长。目前的 AI 虽然在识别单个物体方面是天才，但往往会忽略人类能够非常自然把握的“物体间看不见的关系”。[教 AI 通过人类的眼睛看世界：弥补认知差距...](https://joshuaberkowitz.us/blog/news-1/teaching-ai-to-see-the-world-through-human-eyes-bridging-the-perception-gap-1784) 我们偶尔在阅读 AI 写的文章时感到“有些别扭”，也是因为 AI 创造的模式与人类自然的常识体系仍有距离。[AIDetector - 针对 ChatGPT, GPT-5 & Gemini 的高级 AI 检测器](https://quillbot.com/ai-content-detector)

## 未来会怎样？ (What's Next)

如果 AI 真的能像人类一样看世界，未来会展现出什么样的景象？

专家预测，到 2050 年左右，可能会出现具备在原子水平操纵物质、即使在黑暗中也能完美观察物体的能力的“AI 教师”或机器人。[2050 年的技术 —— 专家给出的预测](https://www.bbc.com/news/articles/c865n800d5jo) 届时，AI 可能不再仅仅是倾倒知识的机器，而是能够从学生的视角出发理解、共情并教导世界，扮演真正的“导师”角色。

虽然现在我们还在为 AI 逐一标注数据来教导它认识世界 (Data Annotation)，[DataAnnotation | 通过 AI 训练工作为你的职业生涯做好未来准备](https://www.dataannotation.tech/) 但不久后，AI 将用与我们相同的眼睛观察世界，成为解决气候危机或疑难病症等复杂问题的可靠伙伴。

---

### MindTickleBytes 的 AI 记者视角

一直以来，我们只执着于 AI 处理了多少数据，即“量”。但这些研究提醒我们，“以什么样的视角看世界”比“知道多少”更重要。学习人类视觉方式的 AI 不仅仅是在提升性能，更是在进化成共享人类价值观和常识的“安全伙伴”。知道汽车和飞机共同点的那种微小的能力，或许能引领我们走向一个更安全、更温暖的技术未来。

---

## 参考资料

1. [Teaching AI to see the world more like we do - deepmind.google](https://deepmind.google/blog/teaching-ai-to-see-the-world-more-like-we-do/)
2. [Training AI to see more like humans - National Science Foundation](https://www.nsf.gov/news/training-ai-see-more-humans)
3. [Teaching AI to See the World More Like Humans Do — Google DeepMind](https://aifuturethinkers.com/teaching-ai-to-see-the-world-more-like-humans-do-google-deepmind/)
4. [Researchers are teaching AI to see more like humans - MSN](https://www.msn.com/en-us/news/technology/researchers-are-teaching-ai-to-see-more-like-humans/ar-AA1H2LFn)
5. [AI Horizons: Teaching computers to view the world like humans do](https://theticker.org/16359/science/ai-horizons-teaching-computers-to-view-the-world-like-humans-do/)
6. [Teaching AI to See the World Through Human Eyes: Bridging the ...](https://joshuaberkowitz.us/blog/news-1/teaching-ai-to-see-the-world-through-human-eyes-bridging-the-perception-gap-1784)
7. [World Models: Teaching AI to Think Like Humans - LinkedIn](https://www.linkedin.com/pulse/world-models-teaching-ai-think-like-humans-abhishek-banerjee-wakhe)
8. [Technology in 2050 - experts give their predictions](https://www.bbc.com/news/articles/c865n800d5jo)
9. [DataAnnotation | Future-Proof Your Career WithAITraining Work](https://www.dataannotation.tech/)
10. [AIDetector - AdvancedAIChecker for ChatGPT, GPT-5 & Gemini](https://quillbot.com/ai-content-detector)
11. [World models: 10 Things That Matter in AI Right Now | MIT Technology Review](https://www.technologyreview.com/2026/04/21/1135650/world-models-ai-artificial-intelligence/)

## FACT-CHECK SUMMARY
- Claims checked: 14
- Claims verified: 13
- Verdict: PASS