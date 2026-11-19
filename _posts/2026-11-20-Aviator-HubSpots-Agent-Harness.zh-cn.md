---
layout: post
title: "AI 助手太多让你感到混乱？HubSpot 给出的答案：Agent 框架 'Aviator'"
description: "在这个企业级 AI 助手井喷、管理难度剧增的时代，我们探讨 HubSpot 推出的 Agent 框架 'Aviator' 与集中式控制中心 'AgentHub' 如何重塑业务自动化的格局。"
summary: "通过 HubSpot 为解决碎片化 AI 助手管理问题而推出的 AgentHub 与 Agent 框架 'Aviator'，了解拥有 250 多万用户的商业 AI 平台的演进过程。"
tags: [HubSpot, AgentHub, Aviator, AI Agents, CRM]
image: 2026-11-20-Aviator-HubSpots-Agent-Harness.jpg
image_alt: "表现各种办公用 AI 助手在一个中央控制中心有机连接并协作的仪表盘画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "告别众多独立 AI 工具散乱各方的过去，如今将它们统一成一个有机系统的‘框架（Harness）’时代已经开启。HubSpot 的 Aviator 和 AgentHub 展示了企业级 AI 成为真正实务合作伙伴所必需的基础设施。"
quiz:
  - question: "为了解决碎片化 AI 助手的问题，HubSpot 推出的全新集中式平台的名称是什么？"
    choices: ["AgentHub", "Aviator Harness", "Breeze Customer"]
    answer: 0
    explanation: "HubSpot 构建了集中式控制中心 AgentHub，以解决 Agent 分散和碎片化的问题。"
  - question: "HubSpot 的 AI 助手平台记录的用户规模大约是多少？"
    choices: ["50多万人以上", "100多万人以上", "250多万人以上"]
    answer: 2
    explanation: "HubSpot 基于创始人的 Agentic AI 平台用户数已突破 250 万。"
  - question: "使用 AgentBuilder 需要哪种 HubSpot 订阅计划？"
    choices: ["免费版（Free）或入门版（Starter）计划", "专业版（Professional）或企业版（Enterprise）计划", "任何计划均可免费使用"]
    answer: 1
    explanation: "AgentBuilder 无法在免费或入门版计划中使用，需要专业版或企业版计划。"
lang: zh-cn
ref: 2026-11-20-Aviator-HubSpots-Agent-Harness
---

想象一下。假设你是一名在公司里负责策划营销活动、挖掘销售线索以及回复客户咨询的忙碌实务人员。为了提高工作效率，你引入了编写邮件用 AI、客户接待用 AI、数据分析用 AI 等多种人工智能工具。本以为会很方便，但实际操作时却发现各个人工智能之间无法沟通、各自为政，反而导致人类管理者不得不四处奔走进行协调的奇特现象发生。

当今许多企业所面临的现实正是如此。虽然单个 AI 的功能很出色，但它们无法与企业的核心客户关系管理（CRM）数据有机结合，处于碎片化状态。为了解决这一问题，客户关系管理（CRM）领域的巨头 HubSpot 给出了答案。这就是 Agent 管理的中央控制中心 [AgentHub](https://www.hubspot.com/products/artificial-intelligence) 以及蕴含工程学创新的 Agent 框架——[Aviator: HubSpot's Agent Harness](https://hubspot.engineering/blog/aviator-hubspots-agent-harness/) [Source 1, Source 2, Source 3]。

在本文中，我们将用浅显易懂的方式探讨 HubSpot 是如何将众多的 AI Agent 编织成一个井然有序的生态系统的，以及这对于我们的日常生活和商业有何意义。

---

## 为什么这很重要？

人们通常一提到 AI，就会想到在屏幕上弹出一个聊天窗口并提问的场景。然而，企业环境下的 AI 正在超越单纯的回答问题，向着能够自主判断和行动的“Agent”形态演进。

问题在于，企业在营销、销售、服务等各个部门引入了不同的 AI 工具。行业内将此称为**“Agent 碎片化（Agent Fragmentation）”** [Source 3]。打个比方，这就好比家里每个家电都有各自的遥控器，开电视要找 A 遥控器，开空调要找 B 遥控器一样令人头疼。当需要管理的 AI 增加到数十个时，管理成本不仅会上升，整体生产力反而会下降。

HubSpot 的 AgentHub 和 Agent 框架 Aviator 正是为了终结这种混乱的尝试 [Source 1, Source 3]。它提供了一个绝无仅有的巨大“控制塔”，能够在一个地方监控所有 AI Agent、评估绩效、开启尚未激活的助手功能，并直接构建自定义 Agent [Source 2]。在商业生态系统中，这意味着 AI 不再是碎片化的玩具，而是蜕变为有机协作的真正团队成员。

---

## 轻松理解：什么是“Agent 框架（Agent Harness）”与“AgentHub”？

为了直观地理解这些抽象概念，我们可以举几个生活中的比喻。

### 1. AgentHub：有多位专业助手工作的“综合中央办公室”
简而言之，**AgentHub**（以前称为 Breeze Agents 的系统）是公司内存在的大量 AI 助手聚集的**“综合中央办公室”** [Source 2, Source 3]。
- 进入这个办公室，可以一眼看出当前哪个助手在努力工作（激活状态）、每个助手取得了多么优异的成绩（性能检查） [Source 2]。
- 如果有尚未被部署到工作岗位的新助手，只需点击一下即可将其唤醒并立即投入实务 [Source 2]。
- 甚至可以亲自制作符合企业需求的专属**“自定义 Agent”** [Source 2]。

### 2. Agent 框架 (Aviator)：约束助手手脚的“安全装置与控制手柄”
那么，技术上将这些 Agent 紧密结合在一起的结构——**Agent 框架（Agent Harness）**，即**“Aviator”**究竟是什么呢 [Source 1]？
登山或降落伞中用于安全固定人体并控制装备的绳索或皮带被称为“Harness（安全带/框架）”。在人工智能领域，框架是指**支撑多个 AI Agent 处理复杂工具、维持内存并在安全调度的同时执行流程的框架**。

简单来说，Aviator 就像是一个坚固的“安全带和操纵杆”，能够防止 AI Agent 暴走，安全参考客户的 CRM 数据（客户咨询记录、购买历史等），并坚定不移地协助其准确执行营销、销售和服务工作。

---

## 现状：250 万用户选择的 Agentic AI 平台

目前，HubSpot 的 Agentic AI 生态系统正处于爆发式增长中。基于 HubSpot 创始人的 Agentic AI 平台已经**突破 250 万用户**，赢得了全球企业的广泛支持 [Source 17]。

现场实际运行的主要功能如下：

1. **客户 Agent（Customer Agents）**：全方位支持营销、销售和服务团队。超越简单的回复，处理实时客户互动，实现随着时间推移不断自主学习和优化的智能自动化 [Source 18]。
2. **AI 销售潜在客户开发 Agent（AI Prospecting Agent）**：销售团队的必备工具，与 CRM 数据直接联动，识别符合资格的优质潜在客户（Lead），编写定制化邮件，并自动管理后续跟进（Follow-up） [Source 8]。
3. **AgentBuilder 与 BuilderPack**：为企业用户提供轻松构建属于自己的定制化 Agent 的环境。特别是通过 HubSpot 的 OAuth，只需安装一次，无需复杂的 API 密钥设置或单独的作业设置，就可以立即运行 Agent [Source 4, Source 5]。不过，使用 AgentBuilder 需要 HubSpot 专业版（Professional）或企业版（Enterprise）计划 [Source 4]。

如上所述，AgentHub 以公开测试版（Public Beta）的形式提供，旨在根据各企业的角色（Hub roles）彻底管理治理和权限 [Source 5]。

---

## 未来会怎样？

未来的商业软件市场将彻底从“功能中心”重组为**“Agent 中心”**。过去，人们必须亲自点击软件按钮、寻找菜单并输入数据；而现在，在 AgentHub 这一中央控制塔的统领下，AI Agent 正开启自动分析客户数据、发送营销邮件、受理服务投诉的新时代。

特别是通过工程博客公开的“Aviator: HubSpot's Agent Harness”等技术框架的出现 [Source 1]，不仅超越了外表华丽的聊天工具，更为深度结合企业内部系统的高性能 AI Agent 奠定了更加稳定、无错误运行的基础。

我们需要关注的并不是 AI 有多聪明的单一模型性能。**众多的 AI Agent 如何与我们的业务数据（CRM）相结合，像一个团队一样有机地协同工作**，这一真正的竞争力时代已经来到了我们的眼前 [Source 2]。

---

## MindTickleBytes 的 AI 记者视角

> 在无数 AI 工具涌现、反而让工作现场变得更加复杂的“数字疲劳”时代，HubSpot 的 AgentHub 与 Aviator 框架正在整理工具的乱局，开启真正的协同调控时代。AI 不再是孤芳自赏的天才，而是作为连接企业所有部门与数据的坚实团队成员深深扎根。

---

## 参考资料

1. [Aviator: HubSpot's Agent Harness](https://hubspot.engineering/blog/aviator-hubspots-agent-harness/)
2. [Run, Build, and Manage Your AI Agents | AgentHub](https://www.hubspot.com/products/artificial-intelligence)
3. [Обзор HubSpot AgentHub (2026) - YouTube](https://www.youtube.com/watch?v=s1ldahJ1Zko)
4. [BuilderPack · AI actions for HubSpot AgentBuilder](https://www.builderpack.com/)
5. [HubSpot AgentHub: Access, Builder, Governance | Flowith](https://flowith.io/tools/hubspot-agent-hub/)
6. [Agent de prospection IA pour les équipes commerciales | HubSpot](https://www.hubspot.fr/products/sales/ai-prospecting-agent)
7. [HubSpot Founder’s Agentic AI Platform Surges Past 2,500,000 Users | CX Today](https://www.cxtoday.com/crm/hubspot-founders-agentic-ai-platform-surges-past-2500000-users/)
8. [Agentic AI: HubSpot Customer Agents & Custom GPTs](https://www.kunocreative.com/blog/agentic-ai-hubspot-agents-custom-gpts)