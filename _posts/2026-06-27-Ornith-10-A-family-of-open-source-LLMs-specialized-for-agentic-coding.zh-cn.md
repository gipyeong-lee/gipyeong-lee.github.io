---
layout: post
title: "AI 自己编写“测试题”？编码代理的新进化：Ornith-1.0"
description: "Deep Reinforce 推出的开源编码 AI 'Ornith-1.0' 能够自主构建编码环境并解决问题。写给普通人的通俗解读。"
summary: "Ornith-1.0 是一款最新的开源编码 AI 模型，具备自主设计测试环境（脚手架）并进行学习的能力。"
tags: [AI, 编码, 开源, 技术趋势]
image: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding.jpg
image_alt: "Ornith-1.0 标志与复杂编码逻辑自主重构的数字图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这种不局限于人类设定的框架，而是由 AI 自行确立试错标准的自主学习方式，将使编码代理的水平迈上一个新台阶。"
quiz:
  - question: "Ornith-1.0 模型与以往编码 AI 相比，最大的特征是什么？"
    choices: ["提升互联网搜索速度", "自主构建用于解决问题的测试环境（脚手架）", "增加图像生成功能"]
    answer: 1
    explanation: "Ornith-1.0 不仅能通过强化学习解决编码问题，还能自行设计用于验证该问题的环境（脚手架）。"
  - question: "Ornith-1.0 模型是以什么许可证发布的？"
    choices: ["私有独占许可证", "GPL 许可证", "MIT 许可证"]
    answer: 2
    explanation: "Ornith-1.0 以 MIT 许可证发布，无论科研还是商业用途均可自由使用。"
  - question: "Ornith-1.0 模型基于哪些现有模型进行训练？"
    choices: ["Gemma 4 与 Qwen 3.5", "GPT-4o", "Llama 3"]
    answer: 0
    explanation: "Ornith-1.0 是基于现有的强大模型 Gemma 4 和 Qwen 3.5 进行追加训练（后训练）得到的。"
lang: zh-cn
ref: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding
---

想象一下。你请了一位能干的开发人员帮忙修复复杂的软件漏洞。如果这位开发人员不仅修复了代码，还为了确认漏洞是否真正被修复，顺手构建了所需的所有测试工具和环境，那会是什么感觉？简直就像魔法一样。

最近，人工智能研究所 Deep Reinforce 发布了一款全新的 AI 模型家族——**Ornith-1.0**，它就展现了这种令人惊叹的能力。虽然市面上已经有很多编码 AI，但 Ornith-1.0 展现了更高维度的进化：像经验丰富的工程师一样，它能自行设计解决问题的“舞台”。

## 为什么这很重要？

到目前为止，大多数编码 AI 仅局限于在人类预设的规则范围内寻找答案。然而，现实世界的编码并没有标准答案。识别问题所在、构建验证问题的测试环境、修复后再次确认，这一系列复杂过程缺一不可。[出处: Ornith1.0: SelfLearningLLM forCoding| by Mehul Gupta | Medium](https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc)

像 Ornith-1.0 这样的“代理型编码模型”，使 AI 不仅仅停留在预测下一个单词的水平，而是能够自主执行软件工程的全过程。此外，这些模型以开源方式发布，让全球开发人员无论企业规模大小，都能将前沿技术引入到自己的服务中。[出处: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

## 通俗理解：“会自己搭厨房的厨师”

Ornith-1.0 的核心在于**“自主构建测试环境（Self-Scaffolding）”**。

让我们打个比方。假设我们要雇佣一位厨师。如果现有的 AI 是只会照着菜谱做菜的机器人，那么 Ornith-1.0 就像是在做菜前先检查厨房设备。如果煤气灶不够用，它就自己安装炉灶；如果没有检查食材新鲜度的工具，它就自己制造工具，然后再开始做菜。

这里所说的“脚手架（Scaffold）”，是一种用于验证代码是否正常运行的测试蓝图。现有的模型依赖于人类预先构建好的测试环境，而 Ornith-1.0 通过**强化学习（Reinforcement Learning，通过在试错中获得奖励来学习的方式）**，能够同时优化问题解决方案及其验证平台。[出处: Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854) [出处: Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)

## 性能如何？

Deep Reinforce 发布了多种模型，以满足不同用户的需求。从轻量、快速的 9B（90 亿参数）模型，到规模庞大的 397B（3970 亿参数）“专家混合（MoE，将多个小模型高效组合的方式）”模型，选择空间非常广阔。[出处: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

性能也同样令人瞩目。在衡量实际编码问题解决能力的著名测试基准“SWE-Bench Verified”中，它获得了 82.4 分的高分。这在现有开源模型中无疑是最高水平。[出处: Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854) [出处: Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)

## 未来图景

Ornith-1.0 的出现预示着开源 AI 生态系统将发生巨变。依赖大型科技公司垄断模型的时代即将过去，一个任何人都能亲自构建并改进强大编码工具的时代已经开启。[出处: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

未来，AI 将不仅仅是辅助编写代码，而是进化为指挥整个软件开发项目的“自主工程师”。开发人员将能够专注于更具创造性和架构性的思考，而重复枯燥的验证工作则由 AI 代理代劳，这一未来，随着 Ornith-1.0 的到来已经迈出了第一步。[出处: DeepReinforce Releases Ornith-1.0 for Self-Scaffolding Coding Agents, TechGig](https://techgig.com/news/software-devops/deepreinforce-releases-ornith-1-0-for-self-scaffolding-coding-agents/132008000)

## 参考资料

1. [Ornith1.0—Open-SourceAgenticCodingModels](https://www.ornith.site/)
2. [Ornith1.0: SelfLearningLLM forCoding| by Mehul Gupta | Medium](https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc)
3. [IntroducingOrnith1.0-AgenticCodingLLMs - YouTube](https://www.youtube.com/watch?v=uD4-uy0GmHE)
4. [Ornith-1.0-adeepreinforce-ai Collection](https://huggingface.co/collections/deepreinforce-ai/ornith-10)
5. [IntroducingOrnith1.0-open-source- Art of Smart](https://www.artofsm.art/t/introducing-ornith-1-0/20592)
6. [DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)
7. [DeepReinforce releasesopen-sourceOrnith-1.0codingmodels...](https://digg.com/tech/f2u02pzq)
8. [deepreinforce-ai/Ornith-1.0-9B-GGUF · Hugging Face](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)
9. [Ornith-1.0: Self-ScaffoldingLLMsforAgenticCoding](https://deep-reinforce.com/ornith_1_0.html)
1---
layout: post
title: "AI 自己编写“考题”？编程智能体的新进化：Ornith-1.0"
description: "Deep Reinforce 推出的开源编程 AI“Ornith-1.0”能够自行构建编程环境并解决问题。适合普通读者的科普解读。"
summary: "Ornith-1.0 是一款具备自主设计及学习测试环境（脚手架）能力的最新开源编程 AI 模型。"
tags: [AI, 编程, 开源, 技术趋势]
image: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding.jpg
image_alt: "Ornith-1.0 Logo 与自动重构复杂编程逻辑的数字图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "不拘泥于人类预设的框架，由 AI 自行确立试错标准的主动式学习方法，将使编程智能体的能力提升至全新高度。"
quiz:
  - question: "Ornith-1.0 模型区别于以往编程 AI 的最大特点是什么？"
    choices: ["提升了互联网搜索速度", "能够自行构建用于解决问题的测试环境（脚手架）", "增加了图像生成功能"]
    answer: 1
    explanation: "Ornith-1.0 不仅能通过强化学习解决编程问题，还能自行设计用于验证这些问题的环境（脚手架）。"
  - question: "Ornith-1.0 模型以何种许可证发布？"
    choices: ["私有商业许可证", "GPL 许可证", "MIT 许可证"]
    answer: 2
    explanation: "Ornith-1.0 以 MIT 许可证发布，无论研究还是商业用途均可自由使用。"
  - question: "Ornith-1.0 模型基于哪些现有模型进行了训练？"
    choices: ["Gemma 4 和 Qwen 3.5", "GPT-4o", "Llama 3"]
    answer: 0
    explanation: "Ornith-1.0 是基于现有的强大模型 Gemma 4 和 Qwen 3.5 进行追加训练（后训练）的。"
lang: zh-CN
ref: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding
---

想象一下：你请一位优秀的开发人员修复复杂的软件 Bug。这位开发人员不仅修复了代码，为了确认 Bug 是否真正被修复，还顺手把所需的测试工具和环境全部搭建好了。这听起来是不是像变魔术一样？

最近，AI 研究机构 Deep Reinforce 公布了其全新的 AI 模型家族——**Ornith-1.0**，它就展现了这种惊人的能力。过去编程 AI 虽然多，但 Ornith-1.0 的进化维度在于它像资深工程师一样，能自行设计解决问题的“舞台”。

## 这为什么重要？

以往大多数编程 AI 只能在人类设定的规则内寻找答案。然而，现实世界的编程并没有唯一的“标准答案”。如何识别问题所在、构建验证问题的测试环境、修正后再次确认，这些复杂的流程缺一不可。[出处: Ornith1.0: SelfLearningLLM forCoding| by Mehul Gupta | Medium](https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc)

像 Ornith-1.0 这样的“智能体编程模型”，让 AI 不仅仅停留在预测下一个词的水平，而是能自主完成软件工程的全过程。更重要的是，这些模型以开源形式发布，让全球开发者无论企业规模大小，都能将前沿技术引入到自己的服务中。[出处: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

## 轻松理解：会“自己造厨房”的厨师

Ornith-1.0 的核心在于**“自主测试环境（Self-Scaffolding）”**。

打个比方，假设我们要招聘一名厨师。如果现有的 AI 是只能看食谱做菜的机器人，那么 Ornith-1.0 在做菜前会先检查厨房设备。如果燃气灶不足，它会自己安装炉头；如果没有检查食材新鲜度的工具，它会直接造出一个工具，然后再开始做菜。

所谓的“脚手架（Scaffold）”，就是用于验证代码是否正常运行的一套测试蓝图。现有模型依赖于人类预先建立的测试环境，而 Ornith-1.0 则通过**强化学习（Reinforcement Learning，一种通过答对获得奖励、在试错中不断学习的方法）**，同时优化问题解决方案与验证结果的舞台。[出处: Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854) [出处: Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)

## 进展如何？

Deep Reinforce 公布了多种模型，以便用户根据自身环境进行选择。从轻量快速的 9B（90 亿参数）模型，到规模宏大、采用“专家混合（MoE，将多个小模型高效组合的方式）”的 397B（3970 亿参数）模型，选择非常丰富。[出处: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

性能表现也令人惊叹。在著名的编程能力测试平台“SWE-Bench Verified”上，它创下了 82.4 分的高分，在现有开源模型中独占鳌头。[出处: Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854) [出处: Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)

## 未来景象

Ornith-1.0 的登场预示着开源 AI 生态将迎来巨变。依赖巨头垄断模型的时代已经过去，一个任何人都能自行构建并改进强大编程工具的时代已经开启。[出处: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

未来，AI 将不仅仅是辅助写代码，而是发展成为指挥整个软件开发项目的“自主型工程师”。开发者可以专注于更有创造力和设计感的思考，而重复枯燥的验证工作将由 AI 智能体来完成——Ornith-1.0 正是迈向这一未来的第一步。[出处: DeepReinforce Releases Ornith-1.0 for Self-Scaffolding Coding Agents, TechGig](https://techgig.com/news/software-devops/deepreinforce-releases-ornith-1-0-for-self-scaffolding-coding-agents/132008000)

## 参考资料

1. [Ornith1.0—Open-SourceAgenticCodingModels](https://www.ornith.site/)
2. [Ornith1.0: SelfLearningLLM forCoding| by Mehul Gupta | Medium](https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc)
3. [IntroducingOrnith1.0-AgenticCodingLLMs - YouTube](https://www.youtube.com/watch?v=uD4-uy0GmHE)
4. [Ornith-1.0-adeepreinforce-ai Collection](https://huggingface.co/collections/deepreinforce-ai/ornith-10)
5. [IntroducingOrnith1.0-open-source- Art of Smart](https://www.artofsm.art/t/introducing-ornith-1-0/20592)
6. [DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)
7. [DeepReinforce releasesopen-sourceOrnith-1.0codingmodels...](https://digg.com/tech/f2u02pzq)
8. [deepreinforce-ai/Ornith-1.0-9B-GGUF · Hugging Face](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)
9. [Ornith-1.0: Self-ScaffoldingLLMsforAgenticCoding](https://deep-reinforce.com/ornith_1_0.html)
10. [DeepReinforceOpenSourcesOrnith-1.0CodingModels - Open...](https://www.opensourceforu.com/2026/06/deepreinforce-open-sources-ornith-1-0-coding-models/)
11. [LLM Explorer: AI Agent andOpen-SourceLanguage Model Directory](https://llm-explorer.com/)
12. [Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854)
13. [Saidul on X: "Open-source AI just raised the bar for coding agents..."](https://x.com/saidul_dev/status/2070154993240608844)
14. [🚨 AI News | TestingCatalog on X: "DeepReinforce has released Ornith-1.0..."](https://x.com/testingcatalog/status/2070153054679179400)
15. [Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)
16. [DeepReinforce Releases Ornith-1.0 for Self-Scaffolding Coding Agents, TechGig](https://techgig.com/news/software-devops/deepreinforce-releases-ornith-1-0-for-self-scaffolding-coding-agents/132008000)
17. [0xMarioNawfal on X: "DeepReinforce just launched Ornith-1.0..."](https://x.com/RoundtableSpace/status/2070211260898275530)
18. [deepreinforce-ai/Ornith-1.0-9B · Hugging Face](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)