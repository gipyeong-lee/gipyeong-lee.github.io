---
layout: post
title: "对AI说一句“画个杯子”就能得到3D模型？开源CAD平台“CADAM”登场"
description: "无需编程或复杂的软件，使用日常语言即可进行3D设计？介绍这款仅凭文本即可创建CAD模型的开源AI工具——CADAM。"
summary: "初创公司Adam发布了开源AI CAD平台“CADAM”，用户可通过自然语言提示词生成参数化3D模型。"
tags: [AI, 3D设计, CAD, 开源, 技术趋势]
image: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD.jpg
image_alt: "显示AI在浏览器中生成3D建模设计画面的简洁界面图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion:---
layout: post
title: "对AI说“画个杯子”就能得到3D模型？开源CAD平台“CADAM”问世"
description: "无需编程或复杂的软件，日常语言也能进行3D设计？介绍这款仅凭文本即可生成CAD模型的开源AI工具——CADAM。"
summary: "初创公司Adam发布了开源AI CAD平台“CADAM”，用户可通过自然语言提示词生成参数化3D模型。"
tags: [AI, 3D设计, CAD, 开源, 技术趋势]
image: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD.jpg
image_alt: "简洁的界面，展示了在网页浏览器中由AI生成的3D建模设计画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "降低复杂CAD工具的门槛，是实现硬件设计大众化的重要钥匙。但还需持续观察AI生成的模型能否达到专业工程级别的精度。"
quiz:
  - question: "CADAM生成3D模型的方式是什么？"
    choices: ["直接生成图像", "编写OpenSCAD代码后进行3D渲染", "简单修改现有的3D文件"]
    answer: 1
    explanation: "CADAM通过文本提示词编写OpenSCAD代码，并将其渲染为3D模型。"
  - question: "使用CADAM需要什么？"
    choices: ["高配置本地CAD软件", "专业3D设计资格证书", "网页浏览器"]
    answer: 2
    explanation: "CADAM是一款基于网页的工具，无需本地安装，直接在浏览器中即可使用。"
  - question: "Adam为硬件团队提供的工具，除了CADAM还有什么？"
    choices: ["面向使用Onshape和Autodesk Fusion团队的CAD副驾驶功能", "Photoshop和Illustrator", "Excel和PowerPoint"]
    answer: 0
    explanation: "Adam不仅提供自研平台CADAM，还为使用Onshape和Autodesk Fusion的团队提供CAD副驾驶（Co-pilot）功能。"
lang: zh-cn
ref: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD
---

想象一下：你需要在桌上放一个造型独特的笔筒。在过去，你得打开复杂的专业设计软件，一寸一寸测量尺寸，鼠标点击成千上万次才能绘出线条。但如果现在，你只需对AI说一句：“帮我做一个高度为10厘米、侧面带有镂空孔的六角形笔筒”，设计就完成了，那会是怎样的一种体验？

硅谷前沿初创公司Adam (YC W25) 近期发布了一款名为“CADAM”的开源平台，旨在让这一未来图景成为现实（[来源: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)）。下面带你深入了解这项有望大幅降低硬件设计门槛的惊人技术。

## 为什么这很重要？

CAD（计算机辅助设计）作为机械设计的基石，在过去几十年里并没有发生根本性的变化。尽管每年都有新版本问世，但软件却变得愈发臃肿、复杂，对于初学者而言，其学习曲线极其陡峭（[来源: Adam (YC W25) is building an AI Co-pilot for CAD](https://www.linkedin.com/posts/y-combinator_adam-yc-w25-is-building-an-ai-co-pilot-activity-7291123133569261568-BDm1)）。

Adam瞄准的正是这一痛点。他们坚信，正如AI彻底改变了软件开发方式一样，AI也将成为机械设计领域辅助创作的核心媒介（[来源: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)）。无论是普通用户还是专业工程师，无需在本地安装沉重的软件，仅通过网页浏览器即可即时创建高质量的3D模型，这意味着设计方法论本身将迎来一次巨大的范式转变（[来源: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)）。

## 轻松理解

CADAM通常被形容为“AI版TinkerCAD”（[来源: Adam launches CADAM, an open-source text-to-CAD platform](https://www.agentic-universe.net/articles/su55qBXbEQEy849MZT-tU)）。那么，文本是如何变成立体3D模型的呢？

打个比方，这就好比你对“厨师（AI）”下单：“帮我做一份好吃的牛排”。AI并不会亲手去煎肉，而是会非常严谨地写出一份菜谱（OpenSCAD代码）（[来源: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)）。将这份菜谱放入烤箱（通过WebAssembly技术驱动的网页浏览器环境），一道可口的佳肴（3D模型）就自动完成了（[来源: GitHub - Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM)）。

这里的核心在于“通过代码生成”。这被称为“参数化设计”（通过调整数值或参数来修改模型的方式）。由于设计本身就是代码，如果你之后改变主意说：“把高度改成12厘米”，AI只需简单修改代码中的数值，即可瞬间完成模型调整（[来源: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)）。

## 当前进展

目前，CADAM已作为一个开源项目发布，任何人都可以通过网页浏览器访问并尝试使用（[来源: GitHub - Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM)）。生成的模型支持导出为STL、SCAD、DXF等格式，完全满足实际3D打印或机械加工的需求，实用性极高（[来源: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)）。

Adam成立于2025年，除了自研平台外，他们还为使用Onshape或Autodesk Fusion等专业工具的硬件团队提供“CAD副驾驶（Co-pilot）”工具（[来源: Adam | CAD Copilot for Hardware Teams](https://adam.new/)）。不过，由于目前尚处于早期阶段，在极其精密和复杂的专业设计领域，它更多是扮演提高创作速度的辅助角色，而非完全替代传统的专业工具（[来源: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)）。

## 未来展望

如果Adam愿景得以实现，即AI成为机械设计最重要的创作手段，那么我们将迎来一个“所想即所得”的时代——任何人在脑海中构思的创意，都能立刻转化为可打印的3D实物（[来源: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)）。对于创意制造者而言，这将极大地降低工具学习成本；而对于专业人士，它将承担重复性的设计工作，让人们能更专注于更有价值的创新。

## MindTickleBytes AI记者观点

降低复杂CAD工具的门槛，是实现硬件设计大众化的重要钥匙。但还需持续观察AI生成的模型能否达到实际工程级别的精度，以及如何确保所生成的结构安全性，这将是未来最大的关注点。

## 参考资料

1. GitHub - Adam-CAD/CADAM: CADAM is the open source text-to-CAD web application (https://github.com/Adam-CAD/CADAM)
2. Launch HN: Adam (YC W25) – Open-Source AI CAD | Hacker News (https://news.ycombinator.com/item?id=48572553)
3. Adam | CAD Copilot for Hardware Teams (https://adam.new/)
4. Adam: AI Powered CAD | Y Combinator (https://www.ycombinator.com/companies/adam)
5. Open-Source CAD Tools and x86 ML Extensions Advance, While AI Assistant Security Lags (https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)
6. Adam (YC W25) is building an AI Co-pilot for CAD Design... - LinkedIn (https://www.linkedin.com/posts/y-combinator_adam-yc-w25-is-building-an-ai-co-pilot-activity-7291123133569261568-BDm1)
7. Adam launches CADAM, an open-source text-to-CAD platform (https://www.agentic-universe.net/articles/su55qBXbEQEy849MZT-tU)