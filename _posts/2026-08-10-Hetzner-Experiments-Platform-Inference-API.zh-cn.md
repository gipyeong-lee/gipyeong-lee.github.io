---
layout: post
title: "我的电脑能自己跑AI？Hetzner（赫兹纳）的新AI实验究竟是什么？"
description: "欧洲知名数据中心企业Hetzner公布了一项实验性AI推理API服务，本文将为您解析其特点与潜力。"
summary: "深入了解Hetzner利用数据中心基础设施免费提供的实验性OpenAI兼容AI推理API服务。"
tags: [AI, Hetzner, 基础设施, 推理API]
image: 2026-08-10-Hetzner-Experiments-Platform-Inference-API.jpg
image_alt: "象征Hetzner数据中心与AI技术的现代图形图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Hetzner的举动预示着AI基础设施市场可能出现强有力的“高性价比”竞争者。如果该服务能从实验阶段走向正式运营，将为开发者提供重要的选择。"
quiz:
  - question: "Hetzner全新AI推理API的特点是什么？"
    choices: ["每月收取固定订阅费", "采用兼容OpenAI标准SDK的API模式", "必须手动下载模型"]
    answer: 1
    explanation: "Hetzner的推理API旨在兼容OpenAI的标准SDK及REST API，因此可以直接使用现有工具。"
  - question: "目前Hetzner推理API服务的状态如何？"
    choices: ["正式商业服务", "任何人均可付费使用", "属于实验阶段，不提供服务保证(SLA)"]
    answer: 2
    explanation: "该服务目前处于实验阶段，是一个没有计费或服务质量保证（SLA）的实验性平台。"
  - question: "如何使用Hetzner推理API服务？"
    choices: ["在Hetzner实验平台仪表盘生成API Token", "通过电话咨询", "必须安装特定软件"]
    answer: 0
    explanation: "用户需访问Hetzner实验平台（Experiments dashboard）自行生成API Token即可使用服务。"
lang: zh-cn
ref: 2026-08-10-Hetzner-Experiments-Platform-Inference-API
---

想象一下，如果你平时使用的那些人工智能（AI）服务，实际上就像巨大工厂里的零件一样在运作，会是什么样？当我们向“ChatGPT”这类AI提问时，某个地方的数据中心会接收请求，进行复杂的计算，然后再将答案发送回来。最近，欧洲知名数据中心企业Hetzner（赫兹纳）开启了一项“实验”，预示着这一过程即将迎来新的变化。这究竟是怎么回事呢？

### 这为什么重要？

对于日常使用AI的用户来说，这可能算不上什么剧烈变动。但对于开发者和初创企业从业者而言，这可是个大好消息。Hetzner目前正在[免费提供实验性的AI推理API（Inference API）](https://docs.hetzner.com/general/company-and-policy/experiments/inference/)，这就像是免费分发了一个“工具箱”，让任何人都能轻松地为自己的服务加入AI功能。

“API”这个词可能听起来有些陌生。简单来说，就像我们用手机点外卖时，外卖APP充当了餐厅与我们之间的桥梁一样，API是一项能让开发者轻松调用AI技术的“桥梁”技术。

特别是对于刚刚起步的初创公司来说，能够按需付费、高效运维AI模型的环境至关重要。[Hetzner的推理服务有望为这类企业开辟低成本利用高性能模型的新路径](https://devsandlogics.com/blog/hetzner-is-working-on-llm-inference)。

### 简单理解：如何借用AI的“学习成果”

“推理（Inference）”这个词听起来深奥吗？打个比方，如果说人工智能把浩瀚图书馆里的书全部背下来的过程叫“学习”，那么当我们提问时，它根据这些知识找到答案的过程就叫“推理”。

Hetzner利用其在欧洲的数据中心基础设施，开始代为处理这一“推理”过程。[用户只需在Hetzner实验平台（Experiments dashboard）申请API Token](https://emit-solution.com/en/blog/hetzner-ai-inference-api)，就能以非常熟悉的方式将AI模型连接到自己的程序中，就像使用OpenAI的服务一样。[因为它完全支持标准的OpenAI SDK和通用的网络通信协议（REST API）](https://emit-solution.com/en/blog/hetzner-ai-inference-api)。

就像在手机修图软件里选择滤镜一样，用户只需将Hetzner准备的高性能模型（如“Qwen3.6-35B”）简单应用到自己的服务中即可。无需复杂安装，就能为自己的APP聘请一位专家级的AI助手。

### 现状：仍处于“实验室”阶段

不过需要注意的是，Hetzner明确表示该服务[目前处于实验状态](https://docs.hetzner.com/general/company-and-policy/experiments/inference/)。

- **无正式定价政策：** 目前虽然免费提供，但[尚不清楚何时会收费，或是未来是否会转为正式服务](https://sliplane.io/blog/hetzner-inference)。
- **缺乏服务质量保证（SLA）：** 由于目前没有企业可放心依赖的“服务质量保证（SLA）”，直接应用于核心业务系统仍存在风险。SLA是一种承诺服务不会中断并稳定运行的协议，而目前这只是一个没有任何束缚的自由实验阶段。[目前提供的模型也仅限于一种（Qwen3.6-35B-A3B-FP8）](https://aitodaybrief.com/en/news/tools-and-releases/hetzner-launches-free-experimental-openai-compatible-llm-inference-api)。

即便如此，其性能也令人惊叹。[非官方测量数据显示，从发送问题到输出第一个字符仅需约0.15秒（153ms），生成速度高达每秒224个单词](https://mindpattern.ai/s/2026-07-24-hetzner-is-quietly-testing-free-openai-compatible-inference)。这得益于Hetzner直接运营数据中心所带来的基础设施效率。

### 未来走向如何？

Hetzner正通过这项服务[测试市场需求，以及其数据中心处理AI任务的稳定性](https://emit-solution.com/en/blog/hetzner-hosted-openclaw-experiment)。

如果Hetzner未来能成功完成实验，增加更多模型或将其正式商业化，那么许多曾因高昂成本而苦恼的开发者将能更自由地利用AI技术。更值得关注的是，作为一家重视数据主权的欧洲企业，Hetzner提供了一个既能自主管理数据、又能使用强大AI功能的替代方案。

### MindTickleBytes AI记者观点

比起技术本身，Hetzner的这次尝试在“基础设施民主化”层面显得更加有趣。这释放出一个信号：原本由IT巨头垄断的AI处理能力，正开始被运营高效数据中心的传统基础设施企业所共享。这或许会带来一种变革，就像比起大型电力公司，家门口的电工找到了让家里电器运转得更高效的方法一样。

## 参考资料

1. [HetznerInference: the new AIAPIserving... | EMIT Solution](https://emit-solution.com/en/blog/hetzner-ai-inference-api)
2. [HetznerLaunches FreeExperimentalOpenAI-Compatible LLM... | AITodayBrief](https://aitodaybrief.com/en/news/tools-and-releases/hetzner-launches-free-experimental-openai-compatible-llm-inference-api)
3. [[Feature]: Hi Teknium/Nous, please add support forHetznerAI... | GitHub Issues](https://github.com/NousResearch/hermes-agent/issues/73423)
4. [The frontier labs are building a productHetznerwill sell like bandwidth | LinkedIn](https://www.linkedin.com/pulse/frontier-labs-building-product-hetzner-sell-like-bandwidth-ben-luong-1mjtc)
5. [Hetzner Inference: First Look | Sliplane Blog](https://sliplane.io/blog/hetzner-inference)
6. [Hetzner now hosts OpenClaw: free AI assistant instances as an experiment | EMIT Solution](https://emit-solution.com/en/blog/hetzner-hosted-openclaw-experiment)
7. [Hetzner Enters LLM Inference: What It Means for SaaS Builders in 2026 | Devs & Logics Blog](https://devsandlogics.com/blog/hetzner-is-working-on-llm-inference)
8. [Inference API - Hetzner Docs](https://docs.hetzner.com/general/company-and-policy/experiments/inference/)
9. [Experiments Platform - Overview - Hetzner Docs](https://docs.hetzner.com/general/company-and-policy/experiments/experiments-platform/)
10. [Hetzner is quietly testing free OpenAI-compatible inference. | MindPattern AI](https://mindpattern.ai/s/2026-07-24-hetzner-is-quietly-testing-free-openai-compatible-inference)
11. [Hetzner Tests LLM Inference with Qwen on Its Own ... | Zeli App](https://zeli.app/en/story/49033087)
12. [Hetzner Inference: First Look | Jonas Scholz - LinkedIn](https://www.linkedin.com/posts/jonas-scholz-490274163_hetzner-inference-first-look-activity-7486346679424593922-htYe)
13. [Hetzner testet LLM-Inference-API mit Qwen3-Modell und 262K ... | Lumeric](https://www.lumeric.app/post/02b73ec9-f9f8-4572-aa06-e79935340a86)