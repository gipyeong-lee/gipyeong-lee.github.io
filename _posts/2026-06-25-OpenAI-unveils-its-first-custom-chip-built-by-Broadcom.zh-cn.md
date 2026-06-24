---
layout: post
title: "AI自行设计的芯片——“Jalapeño”：它有何不同？"
description: "OpenAI与博通（Broadcom）携手开发的首款定制AI芯片“Jalapeño”（墨西哥辣椒）的意义及其对日常生活的影响，本文将为您做通俗易懂的解读。"
summary: "OpenAI发布了专为大语言模型（LLM）推理打造的自研芯片“Jalapeño”。相较于传统GPU，其成本效率提高了50%，有望加速AI服务的普及。"
tags: [AI, OpenAI, 半导体, Jalapeño, 技术趋势]
image: 2026-06-25-OpenAI-unveils-its-first-custom-chip-built-by-Broadcom.jpg
image_alt: "OpenAI与博通共同开发的AI定制芯片Jalapeño的概念图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "摆脱通用GPU，转向为特定工作负载优化的ASIC（专用集成电路）是AI基础设施发展的必然趋势。Jalapeño将变革AI的成本结构，成为代理（Agent）时代全面开启的信号弹。"
quiz:
  - question: "OpenAI此次发布的定制芯片“Jalapeño”的主要目标是什么？"
    choices: ["加速普通个人电脑", "大语言模型（LLM）推理", "游戏图像处理"]
    answer: 1
    explanation: "Jalapeño旨在优化ChatGPT等LLM的推理（Inference）任务。"
  - question: "OpenAI通过自行设计芯片可以获得的主要经济优势是什么？"
    choices: ["电力消耗降低90%", "相较于现有GPU降低50%的成本", "开发周期缩短10年"]
    answer: 1
    explanation: "据称，Jalapeño相较于通用GPU可降低50%的运行成本。"
  - question: "Jalapeño开发过程中的独特之处是什么？"
    choices: ["OpenAI直接运营工厂", "利用OpenAI自身模型加速了开发速度", "重新使用了博通的现有芯片"]
    answer: 1
    explanation: "OpenAI利用了其自有的AI模型来加速芯片的开发过程。"
lang: zh-cn
ref: 2026-06-25-OpenAI-unveils-its-first-custom-chip-built-by-Broadcom
---

想象一下：我们每天使用的ChatGPT，回答问题时比现在更快、更便宜，而且更聪明。到目前为止，AI为了处理海量数据，一直依赖于通用图形处理器（GPU，即处理电脑图像和数据的核心部件）。这就像是用一口大锅做遍全世界的所有菜肴。但现在，OpenAI决定改变这种“烹饪方式”，即通过自研的AI芯片——“Jalapeño”（墨西哥辣椒）。 [OpenAI unveils its first custom chip, built by Broadcom](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)

OpenAI与半导体设计企业博通（Broadcom）于24日共同发布了首款定制AI处理器“Jalapeño”。 [OpenAI unveils its first custom chip, built by Broadcom](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) 这不仅意味着研发出更快的芯片，更是一次试图从根本上重组AI服务运营模式的尝试。 [OpenAI and Broadcom unveil LLM-optimized inference chip](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)

## 这为什么重要？

对于普通用户来说，最能切身感受到的变化是“AI服务的性价比”。目前运行AI的成本是天文数字。业界推测，构建一个1吉瓦（GW）规模的大型数据中心（运行AI的巨型计算机仓库）耗资约500亿美元（约合人民币3600亿元），其中约350亿美元用于购买芯片。 [OpenAI and Broadcom announce first custom AI chip, in strike at nvidia](https://finance.yahoo.com/technology/article/openai-and-broadcom-announce-first-custom-ai-chip-in-strike-at-nvidia-140518150.html?fr=sycsrp_catchall)

如果运行我们所用AI应用的成本降低，企业就能以更低的价格提供服务，AI也将更深入地渗透到日常生活的方方面面。Jalapeño相较于现有的通用GPU，具备将成本降低50%的能力。 [OpenAI Unveils Jalapeño — Its First AI Chip, Built With Broadcom](https://fourweekmba.com/openai-jalapeno-first-ai-chip-broadcom-inference/) 随着成本降低，那些目前仅存在于想象中的复杂AI代理（Agent）服务，也能更容易地来到我们身边。 [OpenAI Unveils Jalapeño, Its First Custom AI Chip Built With Broadcom](https://www.digitalcitizen.life/openai-unveils-jalapeno-its-first-custom-ai-chip-built-with-broadcom/)

简单打个比方，如果说通用GPU是一位能驾驶包括汽车、摩托车、卡车甚至轮船在内所有交通工具的“万能司机”，那么Jalapeño就是一列只负责以最高效率运输“数据货物”的“专用高速列车”。得益于此，AI的运作将变得更加经济高效。

## 深入浅出：为何需要“专用芯片”？

要理解Jalapeño，首先需要知道“通用芯片”与“定制芯片”的区别。

通用GPU就像是一位“模范生”，必须同时精通数学、科学、语言和美术。虽然每一门都表现不俗，但难以在特定任务上做到极致。而Jalapeño则是只求“大语言模型推理（LLM Inference，即已训练好的AI给出答案的过程）”这一门科目拿满分的“专家”。 [OpenAI unveils first custom AI inference chip, Jalapeño, with Broadcom — and its development was sped-up with OpenAI's own models](https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models)

值得一提的是，OpenAI是从零开始设计这款芯片的。 [OpenAI Unveils Jalapeño, Its First Custom AI Chip Built With Broadcom](https://www.digitalcitizen.life/openai-unveils-jalapeno-its-first-custom-ai-chip-built-with-broadcom/) 有趣的是，OpenAI在设计这款芯片时，利用了自家的AI模型，从而大幅缩短了开发周期。 [OpenAI unveils first custom AI inference chip, Jalapeño, with Broadcom — and its development was sped-up with OpenAI's own models](https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models) 这意味着AI开始通过自身的力量去设计让它变得更聪明的芯片，开启了一种惊人的良性循环。

## 当前现状

目前的Jalapeño不仅仅是一颗芯片。博通与Celestica正在开展合作，将该芯片整合到实际数据中心的服务器机架（Rack）和网络系统中。 [OpenAI, Broadcom unveil first AI inference chip](https://www.constellationr.com/insights/news/openai-broadcom-unveil-first-ai-inference-chip)

该芯片未来将成为驱动ChatGPT、Codex（代码编写AI）、OpenAI API以及未来AI代理的核心引擎。 [OpenAI Unveils Jalapeño, Its First Custom AI Chip Built With Broadcom](https://www.digitalcitizen.life/openai-unveils-jalapeno-its-first-custom-ai-chip-built-with-broadcom/) OpenAI与博通早在约18个月前就开始了相关合作，预计从明年年底开始正式部署。 [OpenAI and Broadcom announce first custom AI chip, in strike at nvidia](https://finance.yahoo.com/technology/article/openai-and-broadcom-announce-first-custom-ai-chip-in-strike-at-nvidia-140518150.html?fr=sycsrp_catchall)

## 未来发展展望

Jalapeño的出现表明，大型AI企业正在降低对通用硬件的依赖，并不断加强“垂直整合（从半导体设计到服务运营全程自管）”。

读者朋友们需要关注的核心点是：这款芯片应用于大型数据中心的速度有多快。如果明年Jalapeño开始大规模部署，AI服务的响应速度将进一步加快，我们使用AI时感受到的成本压力也将显著降低。AI技术从少数人的高端科技转化为日常生活必备工具，并以更低廉的价格落地，这一过程正是Jalapeño带来的未来。

## 参考资料

1. [OpenAI and Broadcom unveil LLM-optimized inference chip](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)
2. [OpenAI unveils its first custom chip, built by Broadcom](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)
3. [OpenAI unveils first chip as part of Broadcom deal in effort](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)
4. [OpenAI just announced its first custom chip to help ChatGPT](https://www.cnn.com/2026/06/24/tech/openai-broadcom-jalapeno-ai-chip)
5. [OpenAI Unveils Jalapeño, Its First Custom AI Chip Built With](https://www.digitalcitizen.life/openai-unveils-jalapeno-its-first-custom-ai-chip-built-with-broadcom/)
6. [OpenAI Unveils Jalapeño — Its First AI Chip, Built With](https://fourweekmba.com/openai-jalapeno-first-ai-chip-broadcom-inference/)
7. [OpenAI, Broadcom unveil first AI inference chip | Constellation Research](https://www.constellationr.com/insights/news/openai-broadcom-unveil-first-ai-inference-chip)
8. [OpenAI Reveals Its First AI Chip: Jalapeño - Gadget Review](https://www.gadgetreview.com/openai-reveals-its-first-ai-chip-jalapeno)
9. [OpenAI unveils first custom AI inference chip, Jalapeño, with Broadcom — and its development was sped-up with OpenAI's own models | VentureBeat](https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models)
10. [OpenAI unveils its first custom chip, built by Broadcom](https://www.winzheng.com/en/article/openai-custom-chip-broadcom-jalapeno)
11. [OpenAI and Broadcom announce first custom AI chip, in strike at nvidia](https://finance.yahoo.com/technology/article/openai-and-broadcom-announce-first-custom-ai-chip-in-strike-at-nvidia-140518150.html?fr=sycsrp_catchall)
12. [OpenAI, Broadcom join forces on AI chips | Cybernews](https://cybernews.com/ai-news/openai-broadcom-build-first-ai-processor-chip-deal/)
13. [OpenAI partners with Broadcom custom AI chips alongside](https://www.cnbc.com/2025/10/13/openai-partners-with-broadcom-custom-ai-chips-alongside-nvidia-amd.html)