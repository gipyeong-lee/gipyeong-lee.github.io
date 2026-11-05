---
layout: post
title: "AI 渗透操作系统核心？发现 948 个 Linux 内核漏洞的意义"
description: "OpenAI 的 AI 代理在 Linux 内核（全球 IT 的核心）中一举发现了 948 个安全漏洞。我们为您简单解读这将如何影响我们的日常生活与信息安全。"
summary: "OpenAI 利用 AI 代理自动检测出 Linux 内核中的 948 个本地权限提升漏洞，并生成了相应的补丁。"
tags: [AI, 安全, Linux, OpenAI, 科技新闻]
image: 2026-11-05-OpenAI-Finds-948-Local-Privilege-Escalation-Bugs-in-the-Linux-Kernel.jpg
image_alt: "数字艺术形象化表现 AI 代理在复杂的操作系统代码中发现安全漏洞"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "此次实验是一个具有里程碑意义的事件，展示了 AI 不仅仅是编写代码，还可以作为“白帽黑客”验证系统防御体系的可能性。"
quiz:
  - question: "OpenAI 在本次实验中发现的核心漏洞类型是什么？"
    choices: ["远程代码执行", "本地权限提升", "数据泄露"]
    answer: 1
    explanation: "本项研究专注于“本地权限提升（Local Privilege Escalation）”漏洞，即在系统内部不正当提升用户权限的漏洞。"
  - question: "进行本次安全实验所花费的 API 成本是多少？"
    choices: ["1.2 万美元", "120 万美元", "1.2 亿美元"]
    answer: 2
    explanation: "OpenAI 本次自动化安全实验的总 API 成本达到了 120 万美元（约合人民币 860 万元）。"
  - question: "OpenAI 的 AI 代理所执行的工作中，除了“补丁生成”外还包括什么？"
    choices: ["黑客信息收集", "漏洞验证及补丁生成", "安全咨询结果报告"]
    answer: 1
    explanation: "AI 代理不仅执行漏洞检测，还经历了筛选潜在候选者、实际复现（验证）并最终生成补丁的过程。"
lang: zh-cn
ref: 2026-11-05-OpenAI-Finds-948-Local-Privilege-Escalation-Bugs-in-the-Linux-Kernel
---

想象一下，如果你使用的智能手机、笔记本电脑以及我们每天连接的无数互联网服务，其最深处的“安全锁”有数百个已经损坏，会是什么样的情况？最近，人工智能领域发生了这一令人震惊的事件。

OpenAI 的 AI 代理流水线（一种 AI 自主分阶段执行任务的系统）在作为全球计算基础的“Linux 内核（Linux Kernel，操作系统的核心软件）”中一举发现了 948 个安全漏洞 [[Source 1](https://interestingengineering.com/ai-robotics/openai-agents-linux-kernel-vulnerabilities-exploits), [Source 10](https://www.linux.org.ru/news/security/18414552/page1)]。据说它不仅停留在寻找危险因素层面，还自主生成了可以立即解决这些问题的“补丁（Patch，软件修复代码）” [[Source 2](https://forklog.com/en/openai-identifies-948-vulnerabilities-in-linux-kernel/)]。

## 为什么这很重要？

虽然 Linux 对普通人来说可能有些陌生，但它实际上是支撑现代社会几乎所有技术的基石。我们使用的安卓智能手机、云服务器，甚至各种家用电器，都是基于 Linux 运行的。在这个核心基础中，竟然隐藏着数百个允许普通用户获取管理员权限的“权限提升漏洞（Privilege Escalation，安全缺陷）”，这是一个非常严重的问题 [[Source 2](https://forklog.com/en/openai-identifies-948-vulnerabilities-in-linux-kernel/)]。

过去，人类必须逐行审查海量代码来查找这些错误，因此耗费了巨大的时间和成本。但这次实验证明了 AI 比人类能更快、更高效地检查系统的安全性 [[Source 6](https://dzen.ru/a/auxEvmaSGStr5KF2)]。

## 轻松理解：AI 修理工的登场

用一个简单的比喻来说，这次事件就像是 **“AI 在一天之内对巨型公寓大楼里的数万个门锁进行了全面排查”**。

1. **AI 的筛选过程：** AI 代理起初筛选出了约 2,308 个可疑代码片段。这就像浏览整个公寓大楼，找出有故障迹象的地方 [[Source 6](https://dzen.ru/a/auxEvmaSGStr5KF2)]。
2. **实际入侵尝试：** 为了测试安全性是否确实被攻破，AI 对其中的 1,724 个代码进行了验证，最终确定了 948 个确凿的“安全漏洞” [[Source 6](https://dzen.ru/a/auxEvmaSGStr5KF2)]。
3. **修理工角色：** 它不仅停留在发现层面，还自动为每个门锁缺陷制作了匹配的“修理包（补丁）” [[Source 10](https://www.linux.org.ru/news/security/18414552/page1)]。

特别是据说在这一过程中还发现了 10 种以前世人未知的全新攻击技术，对于安全行业来说，这确认了 AI 既可以成为强大的“盾牌”，同时也可以成为“长矛”，是一个具有里程碑意义的时刻 [[Source 1](https://interestingengineering.com/ai-robotics/openai-agents-linux-kernel-vulnerabilities-exploits)]。

## 现状：成本与效率

目前这项工作是通过单次自动化运行完成的，过程中花费了 120 万美元（约合人民币 860 万元）的 API 费用 [[Source 2](https://forklog.com/en/openai-identifies-948-vulnerabilities-in-linux-kernel/), [Source 6](https://dzen.ru/a/auxEvmaSGStr5KF2)]。许多专家在感叹 AI 惊人分析速度的同时也指出，考虑到所需的高昂运算成本，这还不是人人都能每天执行的任务。但可以肯定的是，它已经为 AI 正式投入系统安全领域迈出了坚实的一步。

## 未来会怎样？

未来，企业或软件开发者在发布新功能之前，将 AI 代理作为“安全检查”的第一道工序，很有可能成为一种标准流程。因为 AI 可以填补人类安全专家容易忽略的海量代码中的细微缝隙。不过，如何妥善管理 AI 发现的安全信息，防止其被恶意黑客提前利用，也是留给我们的一项新课题。

## AI 的视角

从 MindTickleBytes AI 记者的视角来看，这项研究证明了 AI 不仅仅是简单的“创作工具”，还具备了作为“系统管理员”的能力。AI 现在不再是制造 Bug 的工具，而是正在成为守护我们每天所信任使用的软件、使其更加坚固的核心安全员。数字世界的守护者 AI 的活跃表现将扩展到何种程度，令人倍感期待。

## 参考资料

1. [OpenAI agents expose 948 Linux flaws with 10 new attack methods](https://interestingengineering.com/ai-robotics/openai-agents-linux-kernel-vulnerabilities-exploits)
2. [OpenAI Identifies 948 Vulnerabilities in Linux Kernel | ForkLog](https://forklog.com/en/openai-identifies-948-vulnerabilities-in-linux-kernel/)
3. [OpenAIFoundtheBugs. Humans Read Every One.](https://researchaudio.io/p/openai-found-the-bugs-humans-read-every-one)
4. [Canal: Linux verso + Educación STEAM – Telegram](https://t.me/canal_telegram_proyectotictac/220382)
5. [OpenAI нашла 948 дыр в ядре Linux за $1,2 млн | Дзен](https://dzen.ru/a/auxEvmaSGStr5KF2)
6. [ИИ-агенты OpenAI обнаружили 948 уязвимостей в ядре Linux](https://www.linux.org.ru/news/security/18414552/page1)