---
layout: post
title: "AI助手可以随意使用我的办公应用吗？MCP网关的秘密"
description: "轻松了解安全连接AI Agent与外部服务的MCP网关的工作原理及最新架构。"
summary: "MCP网关是负责中介AI Agent与企业应用及数据库之间访问并保障安全与通信的核心基础设施。"
tags: [MCP, AIGateway, 安全, 人工智能, 自主Agent]
image: 2026-11-26-MCP-Gateway-How-Snap-Checks-Both-the-Person-and-the-Agent.jpg
image_alt: "表现通过安全网关安全连接AI Agent与外部应用的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI超越了简单的聊天，开始操控实际工作工具的时代已经到来。这就是为什么像出入境管理局一样的‘网关’如此必不可少。"
quiz:
  - question: "MCP网关的主要作用是什么？"
    choices: ["中介AI Agent与外部服务及MCP服务器之间的访问并管理安全", "用于开启和关闭计算机电源的硬件设备", "将智能手机电池效率提高50%以上"]
    answer: 0
    explanation: "MCP网关起到了中介作用，确保AI Agent安全访问已注册的MCP服务器（外部服务、数据库等）。"
  - question: "Docker MCP网关架构的特点是什么？"
    choices: ["将所有服务捆绑在一个巨大的单一进程中", "将各个上游MCP服务器分别在独立容器中运行，然后向客户端统一公开", "无需互联网连接，仅在本地运行"]
    answer: 1
    explanation: "Docker MCP网关采用将每个上游MCP服务器运行在独立容器中，然后向客户端公开该集合的方式。"
  - question: "Atlassian MCP服务器是如何连接AI Agent的？"
    choices: ["通过团队图谱（Teamwork Graph）在聊天窗口中直接连接Atlassian应用与工作内容", "仅专门支持邮件发送功能", "自动编译源代码"]
    answer: 0
    explanation: "Atlassian MCP服务器基于团队图谱，将浏览器和桌面AI Agent连接到Atlassian应用及工作数据。"
  - question: "Bifrost是什么角色的开源项目？"
    choices: ["同时执行高性能LLM网关、MCP网关和Agent网关的角色", "仅执行Web服务器防火墙角色的安全程序", "区块链钱包管理工具"]
    answer: 0
    explanation: "Bifrost是同时执行LLM网关、MCP网关和Agent网关功能的高性能开源网关。"
lang: zh-cn
ref: 2026-11-26-MCP-Gateway-How-Snap-Checks-Both-the-Person-and-the-Agent
---

想象一下。早上上班打开电脑，对AI助手说：“帮我查看昨天堆积的内部聊天消息，从Jira注册的Bug工单中挑出紧急的分享到Slack团队频道。”不到一秒钟，AI就连接了无数内部系统，利落地完成了工作。这确实是一个便利的世界，但脑海中突然闪过这样一丝不安：“如果AI因为我授予的权限不小心泄露了客户数据，或者执行了奇怪的指令该怎么办？”

随着人工智能（AI）超越单纯的聊天对象，直接操控我的电脑和企业应用的**自主Agent（Autonomous Agent）**时代全面开启，这个问题不再是科幻小说中的故事。而为了解决这一巨大的安全与连接问题所出现的钥匙，正是**MCP网关（Model Context Protocol Gateway）**。像Snap这样的创新企业之所以构建同时验证人和Agent的系统，原因也正在于此 [[출처 1](https://eng.snap.com/mcp-gateway)]. 今天，为了让非专业人士也能在10分钟内理解，我们将为您剖析这个复杂的科技世界。

---

## 为什么这很重要？

打个比方，过去的AI就像是一位亲切的图书馆管理员，当你向它提问时，它会组合互联网上漂浮的知识来回答你。但如今的AI Agent不再是图书馆管理员，而是进化成了亲自握着钥匙出入书库和仓库的万能经理。 

像Claude或Cursor这样的最新AI客户端可以与编码环境、浏览器、数据库以及企业协作工具自由通信 [[출처 2](https://mcp.so/)]。问题在于，AI掌握的工具越强大，“事故”的风险也就越大。被恶意Prompt注入（Prompt Injection）欺骗的AI可能会删掉整个数据库，或者访问无权限的敏感文档。简而言之，这就好比把超大卡车的方向盘交给刚拿到驾照的人一样，潜伏着相似的风险。

因此，在AI和外部工具之间需要一个充当彻底的“出入境管理局”角色的中介。这就是MCP网关。从企业安全负责人到独立开发者，对于所有想要在实际工作中引入AI的人来说，网关现在已经成为了生存的必需品，而不再是可选项。

---

## 轻松理解：什么是MCP网关？

为了理解抽象的概念，我们举一个日常生活中的例子。

> **这样比喻更容易理解：**
> 假设有一位辅佐大企业会长（用户）的天才秘书（AI Agent）。秘书非常聪明，但不能直接触碰公司金库或人事档案。会长为秘书发放了“通行证（Token及认证）”，并规定秘书在向内部仓库或外部合作方请求某事时，必须通过**安全咨询台（MCP网关）**。咨询台在仔细检查秘书带来的请求书是否真正获得了会长的许可、以及当前要做的工作是否安全之后，才会打开大门。

在这个比喻中，**安全咨询台**就是**MCP网关**。 

基本上，**MCP（Model Context Protocol）**架构是一套规定了AI应用程序如何与外部**MCP服务器**（提供工具、资源、提示词的服务器）安全收发请求的通信规则集合 [[출처 11](https://www.perplexity.ai/ko/hub/blog/mcp-architecture)]. 在这种结构中，MCP网关位于AI Agent尝试访问的已注册MCP服务器的前端，安全地中介流向外部HTTP端点或本地服务的通信 [[출처 4](https://hugs4bugs.me/how-microvm-isolation-actually-secures-your-autonomous-agents/)].

---

## 多种网关架构对比：从Docker到开源

世界上存在着各种方式的MCP网关，根据开发环境和安全需求采用了不同的架构。打个比方，这就如同从小型的社区金库到戒备森严的政府综合办公大楼一样，根据建筑物的用途，安保系统也会有所不同。

1. **Docker MCP网关**：将各个上游MCP服务器隔离运行在各自独立的Docker容器中，然后将该集合安全地统一公开给客户端的方式 [[출처 6](https://mcp.directory/blog/mcpjungle-vs-obot-vs-docker-mcp-gateway-vs-composio-2026)]. 当想要从根本上阻止服务器之间的污染时非常有用。这就像是在每个房间里单独安装了铁门和锁的自习室。
2. **基于代理的集成方式（例如 Composio）**：由服务器端直接代行（代理）工具执行的结构。它帮助开发者无需将底部的复杂联动结构直接作为原始（raw）MCP服务器公开，便能便捷地使用 [[출처 6](https://mcp.directory/blog/mcpjungle-vs-obot-vs-docker-mcp-gateway-vs-composio-2026)]. 此外，它支持像Context7这样的AI原生联动，提供了对LLM友好的结构 [[출처 7](https://composio.dev/toolkits/context7_mcp)].
3. **一体化高性能网关（例如 Bifrost）**：由Maxim等公开的开源高性能AI网关Bifrost，旨在能够在一个系统中同时执行LLM网关、MCP网关和Agent网关的功能 [[출처 10](https://github.com/maximhq/bifrost)].
4. **企业级网关（例如 Tetrate Agent Router）**：在生产规模的大型企业环境中，将AI Agent路由到所需模型、按团队结算Token费用以及调试多Agent失败案例的功能是必不可少的 [[출처 12](https://tetrate.io/)].

---

## 实际工作中的应用：内部应用、协作工具与开发环境

那么在实际业务中，MCP网关是如何被使用的呢？让我们来看看几个具有代表性的生态系统案例。

* **Atlassian MCP服务器**：帮助浏览器或桌面环境中的AI Agent连接到Jira、Confluence等Atlassian办公应用 [[출처 8](https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/)]. 所有这些连接都基于名为“团队图谱（Teamwork Graph）”的庞大关系网络顺畅运行 [[출처 8](https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/)].
* **Shopify与电商自动化**：将无代码自动化工具n8n与Shopify.dev MCP服务器结合，网店运营者只需通过对话即可轻松构建能够执行商品注册、订单管理、库存查询的强大网店AI Agent [[출처 9](https://www.youtube.com/watch?v=j2WL-av1hNI)].
* **开发者工具（GitHub、GitLab、Cursor、Windsurf）**：在开发现场，广泛应用了在浏览器工具MCP或Cursor、Windsurf等AI IDE环境中与GitHub及GitLab仓库联动，实现代码审查、问题发布、Token及Prompt设置自动化的指南 [[출처 15](https://www.youtube.com/watch?v=G25UyWfYogQ), [출처 17](https://ai-manual.ru/article/mcp-dlya-github-i-gitlab-polnyij-gajd-po-nastrojke-s-tokenami-promptami-i-konfigami-dlya-ai-instrumentov-2026/)].
* **Agent轨道与委托验证（Wever Labs Agentic Rails）**：在通过Glama平台等提供的工具中，还出现了将钱包证明（`X-Wever-Wallet-Proof`）绑定到工具路由，通过返回包含Ed25519签名收据的验证报告来严格控制Agent权限委托的系统 [[출처 5](https://glama.ai/mcp/connectors/com.weverlabs/agentic-rails/tools/wever_delegate-vetting-check)]. 此外，还共同提供了无需网页抓取（Fetch）或资金转移、仅读取调用内数据即可验证安全性的基准证据检查功能 [[출처 16](https://glama.ai/mcp/connectors/com.weverlabs/agentic-rails/tools/wever_benchmark-evidence-check)].

---

## 安全与认证：同时验证人与Agent的方法

Snap的工程博客之所以受到关注，是因为它超越了简单的技术联动，深入思考了**同时验证“人（User）”和“Agent（Agent）”这两个主体的架构（Checks Both the Person and the Agent）** [[출처 1](https://eng.snap.com/mcp-gateway)].

自主Agent发出的请求有时可能与用户的真实意图不同。当恶意攻击者操纵Agent试图执行隐藏指令时，如果没有网关，系统很难阻止这一点。打个比方，这就好比代驾司机（Agent）正在开车，但实时盘查坐在后座的真正车主（人）是否确实在指示正确的目的地，以及中间是否有怀有恶意的人插手。

因此，现代领先的MCP网关构建了以下多重防线：
1. **确认人的身份**：现在下达指令的用户是否为拥有正当权限的内部员工？
2. **设置Agent的权限限制**：当前Agent试图访问的MCP服务器和工具是否有资格执行该工作（例如：支付、修改数据库）？
3. **验证请求完整性**：传递的JSON参数和Token是否被伪造或篡改？（利用Ed25519签名等密码学收据） [[출처 5](https://glama.ai/mcp/connectors/com.weverlabs/agentic-rails/tools/wever_delegate-vetting-check)]

---

## 未来会怎样？

未来，AI Agent将渗透到我们生活的方角落角。在浏览器窗口中、在智能手机中，以及在企业庞大的云服务器基础设施中，无数的AI将相互沟通并协同工作。 

如果届时所有Agent都盲目地各行其是，数字世界将会变成无法无天的地带。为了让AI安全地握住工具并帮助人类，作为强大且灵活的出入境管理局，**MCP网关**的作用预计将会更加重大。开源网关Bifrost、基于Docker的隔离架构以及精致的Agent验证系统，未来将成为更多企业的标准基础设施 [[출처 6](https://mcp.directory/blog/mcpjungle-vs-obot-vs-docker-mcp-gateway-vs-composio-2026), [출처 10](https://github.com/maximhq/bifrost)].

---

## AI的视角

AI越聪明，我们需要的就不是“更多的自由”，而是“更坚固、更透明的安全带”。MCP网关是助力AI与人类在相互信任中协同工作的数字时代坚实盾牌。随着技术的发展，安全不应该变得越来越复杂，反而在用户无需操心的情况下，应该在看不见的地方完美运作。从这个意义上讲，网关技术的发展可以说是开启AI大众化的真正幕后功臣。

---

## 参考资料

1. [MCP Gateway: How Snap Checks Both the Person and the Agent](https://eng.snap.com/mcp-gateway)
2. [MCP Servers for Claude, Cursor & AI Agents | MCP.so](https://mcp.so/)
3. [How microVM Isolation Actually Secures your Autonomous Agents](https://hugs4bugs.me/how-microvm-isolation-actually-secures-your-autonomous-agents/)
4. [Wever Labs Agentic Rails - wever_delegate-vetting-check | Glama](https://glama.ai/mcp/connectors/com.weverlabs/agentic-rails/tools/wever_delegate-vetting-check)
5. [MCP Gateway 2026: Composio vs Docker vs MCPJungle vs Obot](https://mcp.directory/blog/mcpjungle-vs-obot-vs-docker-mcp-gateway-vs-composio-2026)
6. [Context7 MCP Integration for AI Agents | Composio](https://composio.dev/toolkits/context7_mcp)
7. [Get started with the Atlassian MCP server | Atlassian AI Gateway](https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/)
8. [This Shopify AI Agent Does EVERYTHING (n8n + MCP...) - YouTube](https://www.youtube.com/watch?v=j2WL-av1hNI)
9. [GitHub - maximhq/bifrost: Open-source, high-performance AI gateway...](https://github.com/maximhq/bifrost)
10. [MCP 架构：通过图表进行的完美技术分析](https://www.perplexity.ai/ko/hub/blog/mcp-architecture)
11. [Tetrate: The Enterprise AI Gateway Proven At Production Scale](https://tetrate.io/)
12. [Develop Faster using the browser tools MCP... - YouTube](https://www.youtube.com/watch?v=G25UyWfYogQ)
13. [Wever Labs Agentic Rails - wever_benchmark-evidence-check | Glama](https://glama.ai/mcp/connectors/com.weverlabs/agentic-rails/tools/wever_benchmark-evidence-check)
14. [MCP для GitHub и GitLab: настройка 2026 | токены... | AiManual](https://ai-manual.ru/article/mcp-dlya-github-i-gitlab-polnyij-gajd-po-nastrojke-s-tokenami-promptami-i-konfigami-dlya-ai-instrumentov-2026/)