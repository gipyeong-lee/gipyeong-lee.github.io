---
layout: post
title: "AI在Linux内核中发现了1,000个“后门”？——安全新时代"
description: "OpenAI的最新AI智能体在Linux内核中发现了948个潜在的安全漏洞。这对我们的日常生活和IT安全意味着什么？"
summary: "OpenAI的AI智能体发现了Linux内核中的948个安全漏洞，证明了AI既可以是网络安全的威胁，也可以是强大的防御工具。"
tags: [AI, 安全, Linux, OpenAI, 网络威胁]
image: 2026-11-06-OpenAI-Just-Found-Nearly-1k-Ways-to-Gain-Root-Access-in-Linux.jpg
image_alt: "人工智能标志浮现在复杂的数字代码上方，仿佛正在分析漏洞的图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这一发现表明，AI不仅是写作和绘画的工具，还具备了拆解并重组数字世界基础的能力。现在的安全已不再是人与人之间的博弈，而是AI与AI之间的较量。"
quiz:
  - question: "在本次研究中，OpenAI的AI智能体共发现了多少个Linux内核漏洞？"
    choices: ["约500个", "948个", "1200个"]
    answer: 1
    explanation: "通过OpenAI的自动化流水线，发现了948个Linux内核的特有漏洞。"
  - question: "本次研究的核心目标之一是什么？"
    choices: ["扩展Linux内核的功能", "验证攻击者能否获得系统的“Root权限（管理员权限）”", "商业软件的定价"]
    answer: 1
    explanation: "本次研究旨在验证人工智能智能体能否在发现Linux内核缺陷后，利用这些缺陷获取管理员权限——即“Root权限”。"
  - question: "研究过程中使用了什么模型？"
    choices: ["GPT-4o", "GPT-6 Astra Cyber", "Gemma 3"]
    answer: 1
    explanation: "此次安全红队演练主要围绕名为“GPT-6 Astra Cyber”的模型进行。"
lang: zh-cn
ref: 2026-11-06-OpenAI-Just-Found-Nearly-1k-Ways-to-Gain-Root-Access-in-Linux
---

想象一下，从你使用的智能手机到庞大的服务器，支撑全球数字世界的引擎——“Linux”系统，如果突然被打开了近1,000个“后门”会怎样？而且这些后门并非由人类，而是由人工智能在眨眼之间发现的。

OpenAI近期宣布，他们利用其人工智能模型在Linux内核（系统的核心部分）中发现了948个新的漏洞 [[출처 1](https://www.youtube.com/watch?v=GEJQMbxZwAc), [출처 11](https://www.howtogeek.com/openai-cyber-model-gained-linux-root-access/)]。这不仅仅是简单的错误发现，因为AI不仅能够自主寻找网络攻击路径，甚至能实时设计出利用这些路径的方法 [[출처 15](https://www.securityweek.com/ai-agents-got-root-on-linux-via-948-kernel-flaws-in-openai-research/)]。

### 为什么这很重要？ (Why It Matters)

我们每天使用的云服务、Android智能手机，甚至智能冰箱或汽车等物联网（IoT，设备间互联互通的技术）设备，大多运行在Linux基础之上。简单来说，Linux就是数字世界的“地基”。地基牢固建筑才安全，如果Linux的安全性崩溃，建立在其上的所有数字服务都将陷入危险。

如果这处地基被揭露出存在1,000处裂缝，意味着全球无数设备都可能暴露在攻击之下。据称，本次研究中发现的漏洞达到了足以让攻击者获取系统最高权限——“Root权限”的水平 [[출처 11](https://www.howtogeek.com/openai-cyber-model-gained-linux-root-access/), [출처 15](https://www.securityweek.com/ai-agents-got-root-on-linux-via-948-kernel-flaws-in-openai-research/)]。一旦获得Root权限，攻击者便可随意读取设备上的所有信息、远程控制设备，甚至破坏数据。

### 浅显易懂的解释 (The Explainer)

我们可以这样比喻：将Linux内核想象成一座巨大的城池。过去，安全专家们需要人工巡视城墙，用望远镜逐一确认是否有薄弱环节。但由于城池过于庞大，人类在物理上几乎无法找出所有缝隙。

OpenAI为了“攻破”这座城池，投入了极其聪明的“AI侦察兵”。这些侦察兵进行了每秒数千次的撞击、攀爬和寻孔训练。此次使用的模型“GPT-6 Astra Cyber”如同数千名专业黑客同时进攻一般，以极高的速度找出了缺陷 [[출처 7](https://gizmodo.com/openai-built-a-giant-fake-internet-for-its-agents-to-use-and-abuse-safely-2000830274)]。

最令人震惊的是，它不仅上报了“这里有个洞”，还能自动生成“如何通过该洞穴渗透并取代城主（获取Root权限）”的“实际攻击方法” [[출처 15](https://www.securityweek.com/ai-agents-got-root-on-linux-via-948-kernel-flaws-in-openai-research/)]。攻破一个漏洞的成本仅为1,280美元左右，相比人类的研究，这种方式挖掘安全漏洞显得更加经济高效 [[출처 15](https://www.securityweek.com/ai-agents-got-root-on-linux-via-948-kernel-flaws-in-openai-research/)]。

### 现状 (Where We Stand)

目前，这一成果是OpenAI进行的红队演练（Red-teaming，即为了寻找系统漏洞而故意进行攻击的专家团队训练）的一部分 [[출처 7](https://gizmodo.com/openai-built-a-giant-fake-internet-for-its-agents-to-use-and-abuse-safely-2000830274)]。虽然这一发现证明了AI挖掘安全漏洞的能力突飞猛进，但同时也警示人们，如果这种能力落入心怀叵测的黑客手中将会非常危险。所幸，此次发现并非为了破坏实际系统，而是在通过AI构建更安全软件的研究过程中实现的。

### 未来会怎样？ (What's Next)

未来的安全竞争将演变为“谁拥有更聪明的AI”之争。攻击者会利用AI寻找漏洞，防御者（安全专家）也会利用AI加固城墙。未来，AI不仅限于发现漏洞，还将扮演“数字盾牌”的角色，自动编写安全补丁并实时修复系统缺陷。我们这些普通用户将生活在由AI管理的更安全的数字环境中，但也必须密切关注这一过程中AI与AI之间那场隐形的较量。

---

## 参考资料

1. OpenAIFound948WaystoHackLinux.. - YouTube: https://www.youtube.com/watch?v=GEJQMbxZwAc
2. OpenAIBuilt a Giant Fake Internet for Its Agents to Use and Abuse... - Gizmodo: https://gizmodo.com/openai-built-a-giant-fake-internet-for-its-agents-to-use-and-abuse-safely-2000830274
3. OpenAI used AI to find nearly 1,000 ways for hackers to ... - How-To Geek: https://www.howtogeek.com/openai-cyber-model-gained-linux-root-access/
4. AI Agents Got Root on Linux via 948 Kernel Flaws in OpenAI ... - SecurityWeek: https://www.securityweek.com/ai-agents-got-root-on-linux-via-948-kernel-flaws-in-openai-research/