---
layout: post
title: "AI 像团队成员一样工作？揭秘 Y Combinator 公布的“QM”"
description: "带您了解创业孵化器 Y Combinator 公布的多人 AI 代理底座（Agent Harness）——“QM”。"
summary: "Y Combinator 公布的开源 AI 代理底座“QM”是一个允许整个团队与 AI 代理协作的系统，旨在协助处理整理邮件、管理代码仓库等实际工作。"
tags: [AI, 代理, 生产力, YCombinator, QM]
image: 2026-08-01-qm-Multiplayer-agent-harness-for-work.jpg
image_alt: "象征多位 AI 代理在多样化的工作环境中与团队成员协作的数字插画"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "如果 AI 模型是大脑，那么底座就是帮助大脑处理实际工作的“手脚”。QM 是将这些“手脚”以团队为单位进行连接的重要进展。"
quiz:
  - question: "QM 的设计初衷是什么？"
    choices: ["辅助个人游戏娱乐", "自动化和管理团队协作任务", "自主开发 AI 模型"]
    answer: 1
    explanation: "QM 是 Y Combinator 内部使用的工具，旨在通过与代理协作，处理工程、会计、法务等企业各类工作。"
  - question: "什么是代理底座（Agent Harness）？"
    choices: ["AI 模型大脑的代称", "使 AI 模型能够执行实际任务的软件外壳", "计算机的物理硬件部件"]
    answer: 1
    explanation: "底座是包裹在 AI 模型周围的软件，它将仅仅会预测文本的 AI 转化为能够完成实际工作的劳动者。"
  - question: "关于 QM 安全机制的描述，正确的是？"
    choices: ["没有安全保护，任何人都可以访问所有数据", "作为代理使用用户的权限，所有操作均会被审计", "只有管理员可以执行所有任务"]
    answer: 1
    explanation: "QM 代理使用下达指令的用户凭据和权限进行工作，由于所有操作记录均会被留存，因此在安全方面可以得到妥善管理。"
lang: zh-cn
ref: 2026-08-01-qm-Multiplayer-agent-harness-for-work
---

想象一下：早上醒来打开邮箱时，昨晚收到的数十封咨询邮件已经被按重要性分类完毕，甚至连简单的回复草稿都写好了，这会是什么感觉？或者在团队项目进行中，你在 Slack 上随口说一句“把上次会议记录里的任务项同步到代码仓库”，实际的编程工作就开始了，那又会怎样？

在此之前，AI 一直是我们询问问题时提供答案的智能对话伙伴。然而，时代正在发生转变，AI 将不再仅仅是说话，而是作为团队的一员去执行实际的“工作”。最近，被誉为创业摇篮的 Y Combinator (YC) 将其内部使用的 AI 协作系统“QM”开源，进一步加速了这一未来的到来。[来源: Y Combinator on X](https://x.com/ycombinator/status/2083243960684908768?lang=en), [来源: QM — Open-Source Agent Harness from YC](https://qm.ycombinator.com/index.html)

### 为什么这很重要？

到目前为止，我们接触到的许多 AI 工具都专注于提高“个人”的生产力。但实际业务通常是以“团队”为单位运作的。有些任务需要会计团队的授权，有些则需要工程团队的代码支持。

QM 将这种团队协作环境与 AI 结合在了一起。它不仅让 AI 扮演个人助理的角色，更让整个企业在一个巨大的“多人”环境中与 AI 代理并肩工作。[来源: YC QM Agent Harness: A Collaborative AI Shift](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/yc-qm-agent-harness-a-collaborative-ai-shift), [来源: QM: Multiplayer AI Agent Harness for Startups and Slack](https://aitoolly.com/ai-news/article/2026-08-01-qm-a-new-multiplayer-ai-agent-harness-for-collaborative-startup-workflows-in-slack-and-web) YC 的相关人士纷纷表示，通过这个工具，即便只有很少的人手，也能像军队一样高效地工作。[来源: eve on X](https://x.com/eve_bouff/status/2083251012673094031?lang=en)

### 易于理解：AI 的“专用工作服”

“代理底座（Agent Harness）”这个词可能比较陌生。简单来说，如果把 AI 模型比作“大脑”，那么底座就是让大脑能够与世界交互并完成实际工作所需的“专用工作服”。

代理底座是包裹在 AI 模型周围的软件。[来源: What Is an Agent Harness? Model vs Agent(2026) | Taskade AI](https://www.taskade.com/wiki/ai-agents/agent-harness) 它赋予原本仅停留在文本预测水平的 AI 制定任务计划、读取和编写文件以及使用外部工具的权限。

打个比方，这就好比一个非常聪明的大学生（AI 模型）虽然会阅读文件，但因为没有公司内网账号或审批表单（底座），什么活也干不了。底座就是赋予这个学生账号、工作手册和审批印章。QM 是为了让整个团队能够共享这套工作服而设计的“多人型底座”。[来源: QM — Open-Source Agent Harness from YC](https://qm.ycombinator.com/index.html), [来源: Agentharness: что это, компоненты и примеры (2026)](https://matveev.tech/agent-harness-chto-takoe/)

### 当前现状与特点

QM 的设计非常细致，能够直接应用于企业的实际业务现场。

*   **个人与团队的平衡**：在实现个人定制化设置的同时，也能维护整个团队共享的工作环境。[来源: YC QM Agent Harness: A Collaborative AI Shift](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/yc-qm-agent-harness-a-collaborative-ai-shift)
*   **安全与审计（Audit）**：这是最关键的部分。AI 代理代为使用指令下达者的凭据（账号、权限等）。此外，AI 执行的所有任务都会记录在案，能够透明地管理谁做了什么，因此在安全方面非常稳妥。[来源: GitHub - yc-software/qm](https://github.com/yc-software/qm)
*   **灵活性**：可以通过 Slack 或 Web 界面直接对话下达工作指令，管理者可以根据组织的需求设置使用哪种模型以及安全级别等。[来源: YC QM Agent Harness: A Collaborative AI Shift](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/yc-qm-agent-harness-a-collaborative-ai-shift), [来源: QM — Open-Source Agent Harness from YC](https://qm.ycombinator.com/index.html)

### 未来展望

QM 已作为开源项目发布，并采用了 MIT 许可。这意味着全球的开发者都可以在 YC 开发的系统基础上，根据各自的情况进行定制和进一步优化。[来源: Y Combinator on X](https://x.com/ycombinator/status/2083243960684908768?lang=en) 预计未来，它与企业所使用的各种协作工具的整合将会迅速增加。

如今，AI 正在从一个“有问题就回答”的存在，演变成能够亲自执行任务并与团队成员协作的“数字化同事”。或许不久之后，你们团队也会迎来像 QM 这样的数字化同事。

## 参考资料

1. [GitHub - yc-software/qm: Multi-player agent harness for work · GitHub](https://github.com/yc-software/qm)
2. [What Is an Agent Harness? Model vs Agent(2026) | Taskade AI](https://www.taskade.com/wiki/ai-agents/agent-harness)
3. [Agentharness: что это, компоненты и примеры (2026)](https://matveev.tech/agent-harness-chto-takoe/)
4. [Y Combinator on X](https://x.com/ycombinator/status/2083243960684908768?lang=en)
5. [YC QM Agent Harness: A Collaborative AI Shift | StartupHub.ai](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/yc-qm-agent-harness-a-collaborative-ai-shift)
6. [QM — Open-Source Agent Harness from YC](https://qm.ycombinator.com/)
7. [eve on X](https://x.com/eve_bouff/status/2083251012673094031?lang=en)
8. [QM — Open-Source Agent Harness from YC](https://qm.ycombinator.com/index.html)
9. [QM: Multiplayer AI Agent Harness for Startups and Slack](https://aitoolly.com/ai-news/article/2026-08-01-qm-a-new-multiplayer-ai-agent-harness-for-collaborative-startup-workflows-in-slack-and-web)
10. [QM: A Multiplayer Agent Harness Built for Secure Team Workflows](https://ideaverse.ai/blog/qm-a-multiplayer-agent-harness-built-for-secure-team-workflows-ms9g60tq)