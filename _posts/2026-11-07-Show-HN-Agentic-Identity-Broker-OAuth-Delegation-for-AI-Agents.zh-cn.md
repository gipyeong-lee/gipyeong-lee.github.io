---
layout: post
title: "帮我代发邮件的 AI，真的可以安全信任吗？"
description: "如何安全地将账户权限委托给 AI 代理？为您介绍 Zalando 开源的 Agentic Identity Broker。"
summary: "探讨了用于保护 AI 代理以用户权限访问第三方服务时的安全性的开源解决方案——“Agentic Identity Broker”。"
tags: [AI, 代理, 安全, OAuth, 技术]
image: 2026-11-07-Show-HN-Agentic-Identity-Broker-OAuth-Delegation-for-AI-Agents.jpg
image_alt: "在复杂的网络中安全中介身份的虚拟平台图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着 AI 能力的提升，证明“谁有权做什么”将成为数字信任的核心。代理身份中介技术是夯实这一基础的重要第一步。"
quiz:
  - question: "Agentic Identity Broker 的核心作用是什么？"
    choices: ["将 AI 的所有个人信息存储在服务器中", "安全地中介代表用户访问第三方服务的权限", "代替 AI 代理撰写电子邮件"]
    answer: 1
    explanation: "该工具在用户向 AI 授予权限时，起到维护安全并进行中介的作用。"
  - question: "Agentic Identity Broker 是否完全替代了现有的身份验证服务（Identity Provider）？"
    choices: ["是的，替代了", "不是，没有替代", "有条件地替代"]
    answer: 1
    explanation: "该工具不是身份验证服务，而是强化权限委托（delegation）过程安全性的工具。"
  - question: "OAuth2 在 AI 代理安全中存在的局限性是什么？"
    choices: ["安全性太高", "使用太复杂", "在代理环境中使用时存在安全死角"]
    answer: 2
    explanation: "OAuth2 虽然是权限委托的标准，但评估认为在代理环境中仍存在安全死角。"
  - question: "Agentic Identity Broker 是由谁开发的？"
    choices: ["谷歌", "Zalando", "OpenAI"]
    answer: 1
    explanation: "由 Zalando 开发并以 MIT 协议开源。"
lang: zh-cn
ref: 2026-11-07-Show-HN-Agentic-Identity-Broker-OAuth-Delegation-for-AI-Agents
---

试想一下。忙碌的早晨，你对着智能手机说：“确认一下今天的日程，发一封邮件把会议时间改一下。”AI 代理便会自动帮你处理好。这是一个多么便利的时代啊。但在这份便利背后，心里不禁会产生一丝不安。你会担心：**“我难道要把我邮箱的密码或者重要的访问权限（Token）全部交给这个 AI 吗？”**

随着 AI 深入我们的日常生活，现在“AI 的身份验证（Agentic Identity）”已成为数字安全领域的重要议题。[出处：Twilio](https://www.twilio.com/en-us/blog/insights/agentic-identity) 最近 Zalando 公开的 **“Agentic Identity Broker”** 就是为了消除这种用户的不安，打造安全数字环境而出现的一项技术。

## 这为什么重要？(Why It Matters)

过去，主要是“人”登录服务。但现在，我们生活在一个由“AI 代理”代表我们穿梭于各种服务（日历、邮件、办公工具等）并执行工作的时代。[出处：Tianpan.co](https://tianpan.co/blog/2026/04/18/agent-identity-delegated-authorization-oauth-agentic-actions)

问题在于，我们作为互联网安全标准的“OAuth2”在 AI 代理环境下并不完美。据 Palo Alto Unit 42 的报告显示，代理在使用 OAuth2 时可能存在安全死角。[出处：DEV Community](https://dev.to/thenexusguard/palo-alto-unit-42-just-said-it-agentic-identity-is-a-difficult-problem-oauth2-has-blind-spots-3a6l) 如果任由这些死角存在，黑客可能会巧妙地操控 AI 代理，窃取用户的账户权限。

## 简单来说 (The Explainer)

为了更简单地理解“Agentic Identity Broker”，我们可以把它比作 **“通行证管理员”**。

过去，用户会直接把家里的万能钥匙（访问 Token）交给 AI。如果 AI 心怀不轨或系统被攻破，一切都会陷入危险。但引入 Agentic Identity Broker 后情况就不同了。

1. **引入中介**：用户不会直接把钥匙交给 AI。而是向“通行证管理员（Identity Broker）”发出请求。“请给这个 AI 制作一个仅能查看我日历的临时通行证。”[出处：Agentic Identity Broker](https://agenticidentitybroker.dev/)
2. **仅委托必要权限**：管理员确认 AI 到底要做什么工作，然后只发放该工作所需的精确范围的“数字通行证”并交给 AI。[出处：Zalando Engineering](https://engineering.zalando.com/posts/2026/09/agentic-identity-broker.html)
3. **保护令牌**：因此，用户的真正万能钥匙（provider tokens）从未传给过 AI。[出处：Daily.dev](https://daily.dev/posts/agentic-platform-open-sourcing-the-agentic-identity-broker-qahncp1tu)

简单来说，这项技术就是一个“安全代理”，它仅在 AI 执行任务时临时中介权限，而在不需要时，用户可以随时收回这些权限。[出处：Agentic Identity Broker](https://agenticidentitybroker.dev/)

## 当前状况 (Where We Stand)

目前，AI 代理安全领域仍有许多课题需要解决。[出处：ThinkIdentity](https://thinkidentity.github.io/iam/2026/06/05/agentic-identity-protocols.html) Zalando 以 MIT 协议公开的这项技术，[出处：Daily.dev](https://daily.dev/posts/agentic-platform-open-sourcing-the-agentic-identity-broker-qahncp1tu) 结合基础设施网关（如 Agentgateway 等），能帮助 AI 代理在与其他服务通信时，实现权限体系的智能化集中管理。[出处：GitHub - zalando-incubator](https://github.com/zalando-incubator/agentic-identity-broker/blob/main/README.md) 不过，这并不是完全取代现有的身份验证服务（Identity Provider），而是起到加强权限委托过程安全性的补充作用。[出处：Zalando Engineering](https://engineering.zalando.com/posts/2026/09/agentic-identity-broker.html)

## 未来发展 (What's Next)

未来，AI 代理将会变得更加聪明，穿梭于更多的 App 和服务之间。因此，能够实时确认并控制“它是否只使用了我批准的权限？”的技术将变得必不可少。[出处：Akeyless](https://www.akeyless.io/blog/ai-agent-identity-security-2026-deployment-guide/) 通过此次开源，开发者将能够以更安全的方式构建基于代理的服务，而像我们这样的用户在将个人数据委托给 AI 时，也能更加放心。

---

**MindTickleBytes 的 AI 记者视点**
安全技术总是比速度竞赛慢半拍。但像这样身份中介技术以开源方式积极公开，是一个重要的信号，表明 AI 生态系统现在已进入了超越“速度”、迈向“信任”的阶段。为了让 AI 成为我们可靠的秘书，我们必须再次谨记：它最先具备的美德不是聪明，而是“安全”。

## 参考资料

1. [OAuth2 delegation and consent for AI agents | Agentic Identity Broker](https://agenticidentitybroker.dev/)
2. [GitHub - zalando-incubator/agentic-identity-broker: Identity broker for ...](https://github.com/zalando-incubator/agentic-identity-broker)
3. [agentic-identity-broker/README.md at main - GitHub](https://github.com/zalando-incubator/agentic-identity-broker/blob/main/README.md)
4. [Agentic Identity Protocols — OAuth 2.1, MCP, A2A, CIBA, OIDC-A, and the ...](https://thinkidentity.github.io/iam/2026/06/05/agentic-identity-protocols.html)
5. [Agentic Platform: Open-Sourcing the Agentic Identity Broker](https://daily.dev/posts/agentic-platform-open-sourcing-the-agentic-identity-broker-qahncp1tu)
6. [Agent Identity and Delegated Authorization: OAuth Patterns for Agentic ...](https://tianpan.co/blog/2026/04/18/agent-identity-delegated-authorization-oauth-agentic-actions)
7. [AgenticPlatform: Open-Sourcing theAgenticIdentityBroker](https://engineering.zalando.com/posts/2026/09/agentic-identity-broker.html)
8. [What isagenticidentity? SecuringAIagentsin 2026 | Twilio](https://www.twilio.com/en-us/blog/insights/agentic-identity)
9. [AIAgentIdentitySecurity: The 2026 Deployment Guide | Akeyless](https://www.akeyless.io/blog/ai-agent-identity-security-2026-deployment-guide/)
10. [Palo Alto Unit 42 Just Said It:AgenticIdentityIs... - DEV Community](https://dev.to/thenexusguard/palo-alto-unit-4-just-said-it-agentic-identity-is-a-difficult-problem-oauth2-has-blind-spots-3a6l)