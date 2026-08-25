---
layout: post
title: "我的电脑变身AI专家？Perplexity '便携式电脑'将带来的变革"
description: "Perplexity发布的本地AI代理平台“便携式电脑”究竟是什么？为何它如此重要？为您简要解读。"
summary: "Perplexity的“便携式电脑”是一种全新的平台方式，它无需将敏感数据发送至云端，而是直接在用户的本地计算机上运行AI代理，从而兼顾了安全与性能。"
tags: [AI, Perplexity, 人工智能, 本地AI, 安全]
image: 2026-08-26-Perplexity-Portable-Computer.jpg
image_alt: "可视化展示在NVIDIA DGX Spark设备上运行的本地AI代理系统"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "减少对云端的依赖并在个性化环境中控制AI，是迈向真正代理时代必不可少的一步。"
quiz:
  - question: "Perplexity的“便携式电脑”与传统的基于云的AI最大的区别是什么？"
    choices: ["完全不需要互联网连接", "不将数据发送至云端，在本地环境处理", "订阅费用要高得多"]
    answer: 1
    explanation: "“便携式电脑”将代理运行所需的全部核心任务在用户的本地硬件上进行处理，从而增强了数据隐私性。"
  - question: "“便携式电脑”平台推荐什么样的硬件环境？"
    choices: ["普通入门级智能手机", "搭载NVIDIA DGX Spark及RTX的Linux机器", "支持Web浏览器的平板电脑"]
    answer: 1
    explanation: "为了处理高性能AI模型，利用了基于NVIDIA的DGX Spark或搭载RTX GPU的Linux系统硬件。"
  - question: "本地AI代理在执行复杂任务时如何应对？"
    choices: ["强行仅在本地处理所有任务", "仅在必要时将任务切换至基于云的尖端模型", "立即中断任务并弹出错误提示"]
    answer: 1
    explanation: "采取默认在本地处理的方式，但针对本地模型难以解决的任务，通过扩展（escalation）至基于云的高级模型功能来解决。"
lang: zh-cn
ref: 2026-08-26-Perplexity-Portable-Computer
---

想象一下。早上醒来，你对电脑里的AI说：“把昨天在公司写的会议文档和相关资料整理一下，做成一份发给团队成员的摘要报告。”过去，这些资料都需要传送到互联网那头的云服务器进行处理，但现在，这个过程只在你房间里的电脑中发生。

Perplexity最近发布的“便携式电脑（Portable Computer）”正是梦想实现这一变革的服务。它不仅是一个辅助联网搜索的AI，更开辟了一条新路径：在保护你数据安全的同时，直接在你的电脑上运行AI代理（一种能够接收用户指令、自主调用工具和模型来完成任务的AI） [[Source 1](https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai)]。

## 为什么这很重要？

此前，要使用AI，必须将敏感信息发送到谷歌或OpenAI等大型企业的云服务器上。这带来了对数据隐私和安全的担忧。此外，AI模型每次执行任务时产生的服务器使用费（Token费用）也是一大负担。

但“便携式电脑”与众不同。运行代理的核心引擎——“代理协作框架（AI Agent Harness，一种使AI代理能有机调用多种工具的框架）”、“编排器（Orchestrator，指挥任务的管理系统）”，以及底层实际进行思考的“子代理LLM（大语言模型）”，全部都在用户的本地硬件上运行 [[Source 7](https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/), [Source 8](https://x.com/perplexity_ai/status/2092268362386780270)]。换句话说，由于数据不会外泄，安全性大大提升，且针对本地任务无需额外的云端使用费 [[Source 2](https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/), [Source 3](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs)]。

## 轻松理解

把“便携式电脑”比作**“在家做饭的主厨”**如何？

如果说现有的AI服务是向远方的名店（云服务器）下单并等待料理配送，那么“便携式电脑”就像是把专业主厨（本地AI模型）请到了你家的厨房。因为无需将食材（你的个人数据）送出去，所以既新鲜又安全。

但偶尔也会需要制作非常复杂且困难的顶级大餐，对吧？那种时候，主厨会在自己解决的同时，仅针对确实需要极其高深技术的部分，暂时向外面的米其林星级大厨（基于云的顶级模型）请求协助。Perplexity的“便携式电脑”配备了“步骤级路由（Step-level routing）”系统，平时在电脑内快速处理，只有在本地模型难以解决时，才会智能地借助云端的力量 [[Source 1](https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai), [Source 5](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/)]。

在这里担任主厨角色的AI模型是“Qwen 3.8 27B”或Perplexity额外训练的“PPLX 27B”模型 [[Source 4](https://gizmodo.com/perplexity-launches-local-ai-model-that-will-run-on-your-gpu-instead-of-the-cloud-2000802883), [Source 6](https://www.computerworld.com/article/4213821/perplexitys-on-device-ai-offering-promises-data-control-and-lower-token-costs.html)]。27B（270亿参数）既足够聪明，足以处理大多数复杂的办公任务，又是能够适配NVIDIA高性能硬件“DGX Spark”或RTX GPU环境的理想尺寸 [[Source 4](https://gizmodo.com/perplexity-launches-local-ai-model-that-will-run-on-your-gpu-instead-of-the-cloud-2000802883), [Source 11](https://pc-tablet.com/perplexity-launches-portable-computer-local-ai-agent-for-private-workflows/193699/)]。

## 现状

目前，“便携式电脑”的目标用户是那些希望构建完全个性化AI工作流的人群。不过，硬件要求相当严格，必须具备搭载NVIDIA DGX Spark等高性能GPU的Linux机器环境 [[Source 2](https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/), [Source 3](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs)]。

这不仅仅是下载并运行模型那么简单。该平台作为一个完整包，不仅提供AI模型，还集成了AI执行任务所需的各种工具、应用连接功能，以及能够安全执行任务的“沙箱（安全增强的隔离执行环境）” [[Source 5](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/), [Source 7](https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/)]。

## 未来展望

能够亲手把控数据这一点，在企业级环境中尤为吸引人。以“便携式电脑”为起点，未来随着个人硬件性能的提升，更复杂的AI代理将在无需云端的情况下，在我们的桌面上忠实地履行个人秘书的职责 [[Source 9](https://techgenyz.com/perplexity-portable-computer-nvidia-dgx-spark/)]。

通过此次发布，Perplexity开启了用户可以更精细地选择AI利用方式的“本地优先（Local-first）”时代。不久的将来，你的GPU将不再仅仅是玩游戏或处理图形的组件，它即将成为最聪明的个人AI代理的“大脑”。

## AI的观点
减少对云端的依赖并在个性化环境中控制AI，是迈向真正代理时代必不可少的一步。这将把数据的控制权归还给用户，同时也为营造更加紧密且可信的人机协作环境创造了契机。

## 参考资料

1. Introducing Portable Computer - perplexity.ai: https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai
2. Portable Computer is Perplexity's new local AI agent - ZDNET: https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/
3. Perplexity partners with Nvidia to launch Portable Computer ...: https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs
4. Perplexity Launches Local AI Model That Will Run on Your GPU ...: https://gizmodo.com/perplexity-launches-local-ai-model-that-will-run-on-your-gpu-instead-of-the-cloud-2000802883
5. Perplexity and NVIDIA team up to release a local AI agent: https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/
6. Perplexity’s on-device AI offering promises data control and ...: https://www.computerworld.com/article/4213821/perplexitys-on-device-ai-offering-promises-data-control-and-lower-token-costs.html
7. Perplexity Ships Portable Computer on NVIDIA DGX Spark: Local ...: https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/
8. Perplexity on X: "Today we’re launching Portable Computer on ...: https://x.com/perplexity_ai/status/2092268362386780270
9. Perplexity Portable Computer Could Change AI Agents With ...: https://techgenyz.com/perplexity-portable-computer-nvidia-dgx-spark/
11. PerplexityLaunchesPortableComputerLocal AI Agent for Private...: https://pc-tablet.com/perplexity-launches-portable-computer-local-ai-agent-for-private-workflows/193699/