---
layout: post
title: "AI 聊天机器人为什么只会画骑自行车的鹈鹕？剖析“多样性崩塌”现象"
description: "作为衡量大语言模型 (LLM) 性能的“骑自行车的鹈鹕”测试，为什么所有 AI 画出来的鹈鹕都如出一辙？本文带你深入浅出地了解 LLM 的“多样性崩塌”现象及其深层含义。"
summary: "在用于评估大语言模型 (LLM) 性能的“骑自行车的鹈鹕”测试中，出现了一种 AI 生成结果日益趋同的“多样性崩塌”现象。本文通过专家视角，分析了这一现象的成因及启示。"
tags: ["LLM", "人工智能", "AI", "聊天机器人", "技术", "多样性崩塌", "鹈鹕"]
image: "2026-10-15-Why-do-LLM-pelicans-look-like-this.jpg"
image_alt: "生成骑自行车鹈鹕画作的 AI 聊天机器人"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的发展速度令人惊叹，但也引发了关于技术是否能像人类一样进行多样化思考的根本性质疑。“鹈鹕测试”是一个可以窥见这一可能性的有趣指标。"
quiz:
  - question: "展示 AI 聊天机器人“多样性崩塌”现象的代表性测试是什么？"
    choices: ["生成猫咪照片", "风雨天风景画", "生成骑自行车的鹈鹕 SVG", "描述城市夜景"]
    answer: 2
    explanation: "在用于评估 LLM 性能和创造力的“骑自行车的鹈鹕” SVG 生成测试中，人们观察到了 AI 生成结果日益趋同的“多样性崩塌”现象。"
  - question: "LLM“鹈鹕测试”主要评估哪些要素？"
    choices: ["鹈鹕的颜色和大小", "自行车的品牌和型号", "可识别的鹈鹕、合格的自行车以及鹈鹕是否真的在骑车", "鹈鹕穿的衣服"]
    answer: 2
    explanation: "鹈鹕测试综合评估生成的鹈鹕是否可识别、自行车是否有车轮和车架，以及鹈鹕是否真的处于骑行状态等。"
  - question: "LLM 的“多样性崩塌”现象意味着什么？"
    choices: ["AI 变得更具创造力和不可预测性", "AI 生成的结果越来越相似，创造力下降", "AI 的学习能力下降", "AI 模型之间的性能差距变大"]
    answer: 1
    explanation: "多样性崩塌是指 LLM 生成的结果越来越相似，导致其创造力和不可预测性下降，这对 AI 的发展方向提出了重要质疑。"
lang: zh-cn
ref: "2026-10-15-Why-do-LLM-pelicans-look-like-this"
---

# AI 聊天机器人为什么只会画骑自行车的鹈鹕？剖析“多样性崩塌”现象

试想一下。你让一个高性能 AI 聊天机器人为你作画。不是普通的猫咪图或精美的风景画，而是一个有些搞怪的“骑自行车的鹈鹕”。你原本期待 AI 能用丰富多彩的画作让你大开眼界，但结果却是：所有的 AI 生成的都是外表一模一样的鹈鹕和千篇一律的自行车。仿佛所有的 AI 都是从同一个工厂流水线上下来的。

最近，人工智能领域中“鹈鹕测试”备受关注。这是一种用于评估大语言模型 (LLM) 性能的基准测试，旨在考查其指令遵循能力和创造力。然而，在“骑自行车的鹈鹕”这一测试中，AI 生成的结果日益趋同，这一事实令人震惊。专家们将其称为“LLM 多样性崩塌 (LLM diversity collapse)”。[参考资料: The Emperor Pelican Has No Clothes - arcfu.com](https://arcfu.com/post/the-emperor-pelican-has-no-clothes/) [参考资料: Why the Pelican Test Worked and Why It Is Done - LLM ...](https://braindetox.kr/en/posts/llm_benchmark_pelican_test_2026.html)

## 为什么这很重要？

随着 AI 技术深入我们的生活，AI 输出结果的多样性和创造性已成为至关重要的课题。如果 AI 总是以同样的方式思考并给出相同的结果，会发生什么呢？这意味着 AI 的创造力有限，且在面对不可预见的问题时，寻找解决方案或提出新构想的能力会大打折扣。

AI 的真正价值不仅在于快速准确地处理信息，更在于拓展人类思维、提供新视角。打个比方，这就像如果所有的厨师做任何菜都用同一种配方。烹饪的多样性和创造力将荡然无存，我们的味蕾体验也会变得极度乏味。试想一下，如果 AI 在医疗诊断、法律咨询或复杂科学研究中只给出唯一一个“最优”路径而不去探索其他可能性，那么我们可能会错失罕见病诊断或突破性科学发现的机会。

实际上，研究人员在分析了 18 个 LLM 的 1300 多万个标签后发现，“几乎所有假设都能在统计学上达到显著性”。这表明，只需稍微调整 LLM 的设置，结果就会发生巨大变化；反过来说，这也意味着根据特定设置，很容易得出极其划一的结果。[参考资料: LLMHacking: 6 Strategies to Avoid False Findings in Your Research.](https://www.linkedin.com/pulse/llm-hacking-6-strategies-avoid-false-findings-your-mikel-k-ngueajio-nogqf) LLM 只生成划一的结果，让人怀疑 AI 并非在进行真正的“理解”，而仅仅是在重复学习到的模式。

## “骑自行车的鹈鹕”有什么问题？

“骑自行车的鹈鹕”提示词旨在综合测试 LLM 的图像生成能力及复杂指令的遵循能力。[参考资料: Why the Pelican Test Worked and Why It Is Done - LLM ...](https://braindetox.kr/en/posts/llm_benchmark_pelican_test_2026.html) [参考资料: I tested the top local LLMs against ChatGPT and Claude ... - MUO](https://www.makeuseof.com/tested-the-best-local-llms-against-claude-and-chatgpt-with-one-a-pelican/) 要通过此测试，需要满足几个标准。首先，生成的图像必须能让人认出是“鹈鹕”。其次，自行车必须具备车轮和车架，最重要的是，鹈鹕必须确实处于“骑着”自行车的状态。[参考资料: I tested the top local LLMs against ChatGPT and Claude ... - MUO](https://www.makeuseof.com/tested-the-best-local-llms-against-claude-and-chatgpt-with-one-a-pelican/)

过去，针对这一提示词，不同的 LLM 会生成个性迥异的鹈鹕图。有的鹈鹕戴着头盔，有的留着胡子，自行车的种类也各不相同。这有力地证明了 LLM 在理解提示词和进行创造性实现方面的出色能力。[参考资料: Simon Willison on pelican-riding-a-bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle/)

然而，近几个月来，LLM 生成的“骑自行车的鹈鹕”图变得出奇地相似。[参考资料: The last six months in LLMs, illustrated by pelicans on bicycles](https://simonwillison.net/2025/Jun/6/six-months-in-llms/) [参考资料: The Emperor Pelican Has No Clothes - arcfu.com](https://arcfu.com/post/the-emperor-pelican-has-no-clothes/) 正如前面提到的，这就是 LLM 的“多样性崩塌”现象。

## 现状：趋同的鹈鹕们

这种划一化对 LLM 的开发和评估方式提出了根本性的质疑。有分析认为，AI 模型在“深度推理 (high reasoning)”等特定设置下可能表现更好，但这反倒可能成为损害结果多样性的因素。[参考资料: Simon Willison on llm-reasoning](https://simonwillison.net/tags/llm-reasoning/) 当模型在“深度推理”模式下运行时，可能会更倾向于针对特定提示词得出最“安全且经得起验证”的结果。最终，模型只会生成最普遍、最可预测的图像，而排除了原创性或不可预见的解释。[参考资料: 2025 in LLMs so far - ai.engineer](https://ai.engineer/talks/YpY83-kA7Bo-llm-pelican-benchmark)

这让人怀疑 AI 并非真正“理解”和“思考”，而只是在模仿学习数据中出现频率最高的模式。如果 LLM 反复呈现同样的面貌，这意味着 AI 作为激发我们想象力、开启无限可能的工具，其作用是有局限的。

## 未来将会怎样？

LLM 的“多样性崩塌”现象清晰地展示了 AI 技术发展的两面性。一方面，AI 以惊人的速度发展，正向人类智能靠近；但另一方面，结果的趋同化也对“创造力”这一人类独有的领域提出了质疑。

展望未来，AI 开发者不仅要提升性能，更应专注于研究 AI 如何生成更多元、更具创造性的结果。此外，正如“骑自行车的鹈鹕”测试所展示的那样，必须牢记 AI 的评估方式本身也会影响结果的多样性。如前所述，Bauman 等人发布的研究报告警告称，目前的评估方法可能更倾向于寻找利于得出特定结果的设置，而非衡量 AI 的真实能力。[参考资料: LLMHacking: 6 Strategies to Avoid False Findings in Your Research.](https://www.linkedin.com/pulse/llm-hacking-6-strategies-avoid-false-findings-your-mikel-k-ngueajio-nogqf)

为了使 AI 真正成为补充和扩展人类智能的工具，它必须克服划一性结果的陷阱，朝着包容更广泛创造力和不可预测性的方向发展。骑自行车的鹈鹕所呈现的划一化，正要求我们对 AI 前行的道路进行深刻反思。

## 参考资料
1. Why the Pelican Test Worked and Why It Is Done - LLM ... - [https://braindetox.kr/en/posts/llm_benchmark_pelican_test_2026.html](https://braindetox.kr/en/posts/llm_benchmark_pelican_test_2026.html)
2. The last six months in LLMs, illustrated by pelicans on bicycles - [https://simonwillison.net/2025/Jun/6/six-months-in-llms/](https://simonwillison.net/2025/Jun/6/six-months-in-llms/)
3. 2025 in LLMs so far - ai.engineer - [https://ai.engineer/talks/YpY83-kA7Bo-llm-pelican-benchmark](https://ai.engineer/talks/YpY83-kA7Bo-llm-pelican-benchmark)
4. I tested the top local LLMs against ChatGPT and Claude ... - MUO - [https://www.makeuseof.com/tested-the-best-local-llms-against-claude-and-chatgpt-with-one-a-pelican/](https://www.makeuseof.com/tested-the-best-local-llms-against-claude-and-chatgpt-with-one-a-pelican/)
5. The Emperor Pelican Has No Clothes - arcfu.com - [https://arcfu.com/post/the-emperor-pelican-has-no-clothes/](https://arcfu.com/post/the-emperor-pelican-has-no-clothes/)
6. Simon Willison on pelican-riding-a-bicycle - [https://simonwillison.net/tags/pelican-riding-a-bicycle/](https://simonwillison.net/tags/pelican-riding-a-bicycle/)
7. LLM- Detailed dive into LLM w Andrej Karpathy... - Obsidian Publish - [https://publish.obsidian.md/followtheidea/Content/AI/LLM+-+Detailed+dive+into+LLM+w+Andrej+Karpathy](https://publish.obsidian.md/followtheidea/Content/AI/LLM+-+Detailed+dive+into+LLM+w+Andrej+Karpathy)
8. LLMHacking: 6 Strategies to Avoid False Findings in Your Research. - [https://www.linkedin.com/pulse/llm-hacking-6-strategies-avoid-false-findings-your-mikel-k-ngueajio-nogqf](https://www.linkedin.com/pulse/llm-hacking-6-strategies-avoid-false-findings-your-mikel-k-ngueajio-nogqf)
9. Simon Willison on llm-reasoning - [https://simonwillison.net/tags/llm-reasoning/](https://simonwillison.net/tags/llm-reasoning/)