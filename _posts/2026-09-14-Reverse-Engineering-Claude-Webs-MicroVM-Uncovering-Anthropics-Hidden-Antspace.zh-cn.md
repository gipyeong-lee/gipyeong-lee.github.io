---
layout: post
title: "AI自行构建应用并直接部署？深度解析Anthropic的秘密项目“Antspace”"
description: "分析Anthropic旗下Claude超越代码编写，直接部署Web服务的秘密平台“Antspace”的真相。"
summary: "Anthropic正在Claude Code环境中隐藏其内部部署平台“Antspace”，旨在构建一个AI能够自行开发、托管并垂直整合的生态系统。"
tags: [Anthropic, Claude, AI, 云计算, Antspace, 开发]
image: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace.jpg
image_alt: "象征Claude Code开发环境Firecracker MicroVM及其内部秘密部署平台Antspace的抽象插图。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Anthropic的这一举动表明，AI模型已不再仅仅是文本生成工具，而是正在演变为掌控整个开发生态系统的‘以代理为中心的平台’。"
quiz:
  - question: "Anthropic正在开发的内部部署平台名称是什么？"
    choices: ["Vercel", "Antspace", "Baku"]
    answer: 1
    explanation: "“Antspace”是Anthropic开发的内部部署平台（PaaS）。“Baku”是项目构建器环境的代号。"
  - question: "Claude Code Web环境运行的技术基础是什么？"
    choices: ["Firecracker MicroVM", "AWS Lambda", "Docker容器"]
    answer: 0
    explanation: "Claude Code Web运行在配备4个vCPU和16GB RAM的Firecracker MicroVM之上。"
  - question: "据推测，Anthropic构建自有部署平台的原因是什么？"
    choices: ["单纯的技术炫耀", "通过垂直整合掌控服务生态", "加强与现有平台的合作"]
    answer: 1
    explanation: "分析认为，Anthropic旨在将AI模型、开发环境到部署的全过程进行垂直整合，使用户无需依赖外部平台即可完成完善的服务。"
lang: zh-cn
ref: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace
---

你是否曾想象过这样的未来：早晨醒来，对AI说一句“帮我用我刚才想到的创意做一个Web服务”，在喝一杯咖啡的时间里，成品就已经部署上线了？虽然现在仍需往返于各种工具之间，流程复杂，但从Anthropic近期的举动来看，这一过程将变得非常顺滑。最近，安全专家在分析Claude Code环境时，发现Anthropic隐藏了一个令人震惊的项目。

### 为什么这很重要？

到目前为止，AI大多停留在提供或修改代码的“助手”角色上。用户必须复制AI提供的代码，粘贴到自己的电脑上，然后再利用其他平台（例如Vercel）将其部署为Web服务。然而，Anthropic正在筹备名为“Antspace（蚁空间）”的自有部署平台，这一事实意味着AI正在进化为“一站式开发者”，独立完成**“思考、编码、上线”**的全过程[Source 1](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace), [Source 6](https://x.com/AprilNEA/status/2034209430158619084), [Source 11](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)。这意味着，即便是没有任何复杂技术知识的用户，也可以开启一个仅凭AI就能将创意转化为服务的时代。

### 通俗理解：“厨房”的进化

让我们用一个比喻：如果说之前的AI开发环境是**“负责切菜的刀”**，那么Antspace就像是一个**“从食材准备到烹饪再到配送全包的中央厨房”**。

过去，大家必须亲自把食材（代码）送到厨房（云平台）去烹饪（部署）。但Anthropic直接为Claude这位“大厨”配备了专属厨房，这就是名为“Baku（幕）”的专用环境。当用户说“做一个Web应用”时，系统会在瞬间创建一个名为**“Firecracker MicroVM”**的虚拟空间[Source 2](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582), [Source 4](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace/blob/master/baku-analysis.md)。

简单来说，Firecracker是一种极其轻量且快速的“虚拟计算机”。如果说一般的虚拟机是一个庞大的工厂，那么这种MicroVM就像是一个只保留必要功能、瞬间即可成型的“组装式厨房”[Source 11](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)。在这个空间里，利用4个大脑（vCPU）和16GB内存，Claude可以直接构建应用，并一气呵成地处理部署工作[Source 2](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582)。

想象一下，就像去露营时不用亲自搭帐篷，只要对AI说一声“帮我搭个漂亮的帐篷”，帐篷就会如魔法般安装好一样。Antspace就是专为您网站服务的“自动帐篷安装服务”。

### 当前现状：浮出水面的秘密

根据专家的逆向工程（Reverse-Engineering）分析，该系统并非简单地借用现有的外部服务。Anthropic超越了仅仅连接Vercel等现有服务API的层面，**从基础构建了直接部署协议**[Source 1](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace), [Source 3](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace)。

目前，Anthropic正在通过Claude Code收集用户正在构建什么、如何构建的庞大数据库。如果基于这些数据优化Antspace，那么无需开发者一一调整服务器设置，AI就会自动在最有效率的环境中发布应用的时代即将到来[Source 5](https://x.com/mayazi/status/2034282767693873492)。

### 未来走向

Anthropic的策略显而易见：增加用户停留在Claude上的时间，让其不仅是一个“对话”对象，更成为“生产”的核心地带。未来，当开发者只需说一句“帮我部署这个应用”，Antspace就会在后台默默地构建服务器并连接域名。

虽然对用户来说便利性得到了极大提升，但从另一方面看，这也意味着对特定AI生态系统的依赖。Anthropic试图构建的这种垂直整合生态系统，未来将成为其他AI模型的强大基准线[Source 5](https://x.com/mayazi/status/2034282767693873492), [Source 14](https://www.linkedin.com/posts/laserfocus_breaking-if-you-reverse-engineered-the-activity-7440048762829443072-of-K)。

### MindTickleBytes AI记者观点

AI从生成代码水平跃升至直接掌控“部署”这一现实基础设施，意味着AI已不再仅仅是虚拟世界的文本生成器，而是升级为能够运营物理服务（Web网站）的主体。开发者的定义可能正在从“亲自写代码的人”转变为“决定AI部署方向的监督者”。现在，我们不仅要考虑制作什么，恐怕还要开始思考将部署交给哪一个AI了。

## 参考资料

1. [Anthropic's Hidden Vercel Competitor "Antspace" | AprilNEA](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace)
2. [Reverse-engineering Claude Code reveals Anthropica's undisclosed PaaS platform "Antspace": Built in Baku, self-hosted, full-stack ecosystem already taking shape | WEEX Crypto News](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582)
3. [GitHub - AprilNEA/reverse-engineering-claude-code-antspace: Anthropic's Hidden Vercel Competitor "Antspace" · GitHub](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace)
4. [reverse-engineering-claude-code-antspace/baku-analysis.md at master · AprilNEA/reverse-engineering-claude-code-antspace](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace/blob/master/baku-analysis.md)
5. [Maya Zehavi on X: "Anthropic is making the obvious play to build out a platform & own the entire stack from deployment, cloud & orchestration. But more importantly, Anthropic is gathering the user data about ppl are building with Claude so that they can offer a more optimized end to end platform." / X](https://x.com/mayazi/status/2034282767693873492)
6. [AprilNEA on X: "🧵 I just reverse-engineered the binaries inside Claude Code's Firecracker MicroVM and found something wild: Anthropic is building their own PaaS platform called "Antspace" (Ants + Space). It's a full deployment pipeline — hidden in plain sight inside the environment-runner https://t.co/QbPT9ILECG" / X](https://x.com/AprilNEA/status/2034209430158619084)
11. [ClaudeCode Scheduled Tasks and Project Antspace | Roman Peschke](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)
14. [BREAKING: If you reverse-engineered the binaries inside Claude...](https://www.linkedin.com/posts/laserfocus_breaking-if-you-reverse-engineered-the-activity-7440048762829443072-of-K)