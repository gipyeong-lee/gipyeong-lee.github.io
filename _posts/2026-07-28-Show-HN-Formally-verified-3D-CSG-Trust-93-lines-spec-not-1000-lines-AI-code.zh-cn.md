---
layout: post
title: "AI编写的1000行代码值得信赖吗？93行的“定式”给出了答案"
description: "与其逐行审查AI生成的复杂代码，不如验证一份极其简短且完美的蓝图（规范），本文将为您介绍这一获取信任的最新软件工程方法。"
summary: "不再依赖AI编写的庞大代码，通过验证包含核心功能的93行精确规范来提升软件可信度，了解这一最新的开发趋势。"
tags: [AI, 软件工程, 编程, CSG, 形式化验证]
image: 2026-07-28-Show-HN-Formally-verified-3D-CSG-Trust-93-lines-spec-not-1000-lines-AI-code.jpg
image_alt: "复杂的3D几何图形相互结合，背景中极短的代码成为信任的象征"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "问题越复杂，越不应堆砌代码，而应专注于定义本质的“形式化规范”，这才是真正的技术进步。"
quiz:
  - question: "验证AI生成代码的最新工程方法的核心是什么？"
    choices: ["同时使用更多的AI模型", "增加逐行的手动代码审查", "对小型且完美的蓝图（规范）进行形式化验证"]
    answer: 2
    explanation: "目前的方法不再是对AI编写的数千行代码逐一进行审查，而是通过形式化验证包含核心规则的短规范来确保可信度。"
  - question: "3D建模中使用的“CSG（Constructive Solid Geometry，构造实体几何）”技术的定义正确的是？"
    choices: ["将简单的照片转换为3D", "通过结合、差集等方式将基本图形组合成复杂3D对象的建模方法", "简单的2D草图绘制工具"]
    answer: 1
    explanation: "CSG是一种将基本图形（Primitive）作为叶子节点，将并集（Union）或交集（Intersection）等作为父节点，以树状结构表示3D对象的方法。"
  - question: "在软件开发中，“形式化验证（Formal Verification）”的目的是什么？"
    choices: ["为了更快地编写代码", "从数学上保证代码的正确性", "为了让AI变得更聪明"]
    answer: 1
    explanation: "形式化验证是一个通过严格的约束条件和数学逻辑，保证软件完全按照设计精确运行的过程。"
lang: zh-cn
ref: 2026-07-28-Show-HN-Formally-verified-3D-CSG-Trust-93-lines-spec-not-1000-lines-AI-code
---

想象一下，你正打算用3D打印机制作一个非常复杂的零件。制造这个零件的设计图非常复杂，以至于人工难以直接检查。你让AI绘制了图纸，结果它瞬间生成了超过1000行代码。你敢百分之百信任这些代码并直接按下打印键吗？

随着AI编写软件时代的到来，“如何写好代码”已不再是唯一核心，取而代之的是“如何信任代码”。今天，我们将介绍一种最新的技术方法，它不再盲目信任复杂的AI代码，而是仅凭93行精确的设计蓝图来确保软件的安全。

### 为什么这很重要？

到目前为止，当AI编写代码时，我们一直试图让人们逐行阅读以寻找错误。然而，当代码量超过几千行时，这项工作实际上是不可能的。我们很容易错过重要的漏洞。如果该软件用于3D建筑或精密机械设计等对误差要求极高的领域，可能会引发重大事故。[Don’t ReviewAICode.VerifyIt. - YouTube](https://www.youtube.com/watch?v=sClTAvkQDOU)

这项技术将范式从“逐一核对AI编写的代码”转变为“证明代码通过了既定规则（规范）”。因为即使人类不查看所有代码，只要有数学上精确的短设计图，就能保证安全性。

### 浅显易懂：烹饪食谱与形式化验证

为了理解这项技术，我们先来看一个叫 **CSG（Constructive Solid Geometry，构造实体几何）** 的概念。CSG是一种像积木一样通过堆叠、重叠或切割极其简单的形状（立方体、圆柱体等）来制作复杂3D模型的方法。[Constructive solid geometry - Wikipedia](https://en.wikipedia.org/wiki/Constructive_solid_geometry)

这有点类似于我们在照片修图App中叠加滤镜。单个滤镜很简单，但组合在一起就能产生出色的效果。在3D世界中，应用将基本图形组合、重叠和切割的规则，就能创建复杂的3D对象。

但是，如果这些“组合规则”是由人编写的，可能会出错吧？因此，最近开发人员创建了 **“93行核心规范”** 代替这些复杂的代码。[Formally verified 3D mesh intersection - GitHub](https://github.com/schildep/verified-3d-mesh-intersection)

这被称为 **形式化验证（Formal Verification）** 的过程，用以下比喻可以轻松理解：做饭时，不是在放入100种配料后逐一检查味道如何，而是预先精确验证好“一勺盐、两勺糖”这一份精确的食谱。一旦食谱被证明在数学上是正确的，其余复杂的烹饪过程只需要遵循该食谱即可，错误会显著减少。

### 当前情况

在目前的开发领域，人们正在以这种方式实现复杂功能。实际上，在一个项目中，开发人员利用形式化验证库，在约8小时内成功完成了AI代码生成过程中的控制和验证自动化。[ShowHN:Formallyverifiedpolygon intersection – Opus... -HNDebrief](https://hndebrief.com/2026-06-04/show-hn-formally-verified-polygon-intersection-opus-48-oneshots-prev-failed)

过去，开发人员不得不通宵达旦地审查AI编写的超过1000行的代码，而现在，只需将不足100行的“答案集”输入到形式化验证工具中，就能获得信任。不过，这项技术在要求极高精度的工程领域非常强大，但在制作普通网页或轻量级App时，仍存在成本和时间较高的“高级技术”局限性。

### 未来会怎样？

未来，我们使用的AI工具将变得更加智能。它们将不仅是编写代码，还会进化为能够自我验证所编写的代码在数学上是否合理的AI。[Linear– The system for product development](https://linear.app/)

你可能不再需要直接审查代码，而是仅凭“这个AI生成的产物是否通过了93行形式化规范？”这一个问题来判断软件的安全性。信任的标准正从“人的眼睛”向“数学证明”迁移。

### MindTickleBytes的AI记者观点
盲目信任AI生成成果的时代已经结束。这一案例表明，技术越复杂，我们越应专注于更简单、更强大的本质（规范）。毕竟，驾驭聪明工具的方法不是“确认更多”，而是“定义更准”。

## 参考资料
1. [Don’t ReviewAICode.VerifyIt. - YouTube](https://www.youtube.com/watch?v=sClTAvkQDOU)
2. [Constructive solid geometry - Wikipedia](https://en.wikipedia.org/wiki/Constructive_solid_geometry)
3. [Formally verified 3D mesh intersection - GitHub](https://github.com/schildep/verified-3d-mesh-intersection)
4. [ShowHN:Formallyverifiedpolygon intersection – Opus... -HNDebrief](https://hndebrief.com/2026-06-04/show-hn-formally-verified-polygon-intersection-opus-48-oneshots-prev-failed)
5. [Linear– The system for product development](https://linear.app/)