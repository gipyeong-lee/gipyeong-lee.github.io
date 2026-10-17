---
layout: post
title: "AI 编程助手 'Junie Local' 登场，直接在您的电脑上运行"
description: "了解 JetBrains 推出的全新 AI 编程助手 Junie Local，它无需云端连接，即可在您的电脑上安全地执行编程任务。"
summary: "JetBrains 发布的 'Junie Local' 是一款 AI 编程代理，它能够在开发者的设备上独立运行，无需外部服务器连接，从而确保了数据安全和离线工作环境。"
tags: [AI, 编程, JetBrains, JunieLocal, 开发工具]
image: 2026-10-18-JetBrains-Junie-Local-An-agent-you-own-not-one-you-rent.jpg
image_alt: "在电脑上离线运行的 AI 编程代理 Junie Local 的概念图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "将工具的完全控制权交还给开发者是一个非常重要的进步。一个兼顾安全性和性能的本地代理时代正在开启。"
quiz:
  - question: "Junie Local 的最大特点是什么？"
    choices: ["只能通过云服务器运行", "在我的电脑上完全离线运行", "必须订阅付费服务"]
    answer: 1
    explanation: "Junie Local 设计为无需外部服务器连接，直接在开发者的设备上运行。"
  - question: "如何从 Junie Local 切换回云端模型？"
    choices: ["需要重装 IDE", "使用 /model 命令", "必须联系 JetBrains"]
    answer: 1
    explanation: "Junie Local 可以通过 /model 命令轻松地在云端引擎和本地引擎之间进行切换。"
  - question: "使用 Junie Local 需要什么样的初始设置过程？"
    choices: ["需要复杂的环境配置", "只需下载约 20GB 数据并输入一条命令的简单过程", "需要专家的安装支持"]
    answer: 1
    explanation: "Junie Local 的设置非常简单，只需下载约 20GB 的数据并输入一条命令即可完成。"
lang: zh-cn
ref: 2026-10-18-JetBrains-Junie-Local-An-agent-you-own-not-one-you-rent
---

想象一下：在进行复杂的编码任务时，您是否曾因为源代码需要发送到外部服务器而感到不安？或者因为网络连接不稳定而无法顺畅使用 AI 工具而感到沮丧？

过去，AI 编程助手主要依赖庞大的云服务器来运行。但现在情况变了。JetBrains 推出的 'Junie Local' 开启了一个新时代，开发者可以直接在自己的设备上拥有并控制 AI 同事。

## 为什么这很重要？ (Why It Matters)

最大的变化在于“数据控制权”。以往的 AI 编程助手通常需要将用户的源代码发送到云服务器进行处理。在对安全敏感的企业环境或需要严防代码泄露的重要项目中，开发者往往不得不对使用 AI 持保留态度。

Junie Local 不受云端终端点或代币配额的限制，仅使用您电脑的资源即可运行。[来源: JetBrainsShipsJunieLocal:A27B CodingAgentThat Runs Offline](https://rits.shanghai.nyu.edu/ai/jetbrains-junie-local/) 这意味着开发者无需将代码发送到外部服务器，可以在完全离线的环境中持续工作。[来源: JetBrainsShipsJunieLocal:A27B CodingAgentThat Runs Offline](https://rits.shanghai.nyu.edu/ai/jetbrains-junie-local/) 这是一个为开发者打造的真正 '本地' 环境，既实现了安全性的最大化，又消除了外部制约。

## 易于理解的解释 (The Explainer)

'代理(Agent，指不仅能回答问题，还能自行制定计划并执行任务的智能 AI)' 这个术语可能还比较陌生。

简单打个比方，如果说现有的 AI 是 '辅助编程的家教老师'，那么代理就像是 '执行实际工作的编程实习生'。老师只有在学生提问时才会回答，而实习生只要说一句 "帮我实现这个功能"，他就会制定计划、修改文件，甚至直接完成构建和测试。[来源: Junie:JetBrains' AI CodingAgent(2026) — MCP.Directory](https://mcp.directory/blog/junie-jetbrains-coding-agent-2026)

这个能干的实习生现在直接住进了您的电脑里，这就是 Junie Local。Junie Local 基于 4 位量化的 'Qwen3.6-27B' 模型运行。[来源: JunieLocal:JetBrains' Free On-Device AI CodingAgentRuns...](https://dev.to/jamilxt/junie-local-jetbrains-free-on-device-ai-coding-agent-runs-qwen36-27b-entirely-on-your-mac-59i8) 就像我们在手机照片上应用滤镜一样，它将庞大的 AI 大脑（模型）针对您的电脑环境进行了轻量化和优化。[来源: JunieLocal: Run the AI CodingAgenton Your Mac |JetBrains](https://blog.jetbrains.com/junie/2026/08/junie-local-launch/) 因为它直接在您的电脑上运行，所以无需连接互联网，也不必每次都进行账户登录。它成了完全属于您个人的代理。[来源: JuniebyJetBrains. AI CodingAgent.](https://junie.jetbrains.com.cn/local)

## 当前状况 (Where We Stand)

目前，Junie Local 已与 JetBrains IDE（集成开发环境）完美集成。[来源: JuniebyJetBrains. AI CodingAgent.](https://junie.jetbrains.com.cn/local) 开发者只需像往常一样在熟悉的 IDE 内下达指令即可。它还具备灵活性，根据需要，可以通过 '/model' 命令随时从云端模型切换到本地代理。[来源: JuniebyJetBrains. AI CodingAgent.](https://junie.jetbrains.com.cn/local)

当然，由于是在本地运行，硬件配置必须跟得上。它主要在高性能 Mac 电脑上流畅运行，初次设置需要下载约 20GB 的数据。[来源: JunieLocal:JetBrains' Free On-Device AI CodingAgentRuns...](https://dev.to/jamilxt/junie-local-jetbrains-free-on-device-ai-coding-agent-runs-qwen36-27b-entirely-on-your-mac-59i8) [来源: JetBrains'Junienow runs entirely offline. - The New Stack](https://thenewstack.io/jetbrains-junie-local-agent/) 但为了把用户便利放在首位，它被设计成只需一条 '/local' 命令即可轻松完成设置，省去了复杂的 DIY 过程。[来源: JetBrains'Junienow runs entirely offline. - The New Stack](https://thenewstack.io/jetbrains-junie-local-agent/)

## 未来将会如何？ (What's Next)

AI 正在超越单纯的外部云服务，扩展到个人设备内运行的必要 '工具' 领域。Junie Local 为开发者提出了一个新的生态系统，让他们能够最大化发挥自身设备性能，从而更自由、更安全地进行编程。

如果未来有更多轻量化且聪明的模型针对本地环境进行优化，那么在完全无法连接互联网的飞机上，或是在网络安全性受到严格限制的区域内，得到 AI 实习生的辅助进行编程将成为日常。JetBrains 的这一举措是将 AI 技术的主导权交还给开发者的有趣而有力的一步。

## 参考资料

1. [JuniebyJetBrains. AI CodingAgent.](https://junie.jetbrains.com.cn/local)
2. [JetBrainsShipsJunieLocal:A27B CodingAgentThat Runs Offline](https://rits.shanghai.nyu.edu/ai/jetbrains-junie-local/)
3. [JunieLocal: Run the AI CodingAgenton Your Mac |JetBrains](https://blog.jetbrains.com/junie/2026/08/junie-local-launch/)
4. [JunieLocal:JetBrains' Free On-Device AI CodingAgentRuns...](https://dev.to/jamilxt/junie-local-jetbrains-free-on-device-ai-coding-agent-runs-qwen36-27b-entirely-on-your-mac-59i8)
5. [JetBrains'Junienow runs entirely offline. - The New Stack](https://thenewstack.io/jetbrains-junie-local-agent/)
6. [Junie:JetBrains' AI CodingAgent(2026) — MCP.Directory](https://mcp.directory/blog/junie-jetbrains-coding-agent-2026)