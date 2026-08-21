---
layout: post
title: "如果 AI 能自动为你打造量身定制的工作功能，会怎样？"
description: "探索 Vendo，它解决了 B2B SaaS 服务中顽固的功能请求积压问题，并让用户能够亲手构建所需功能。"
summary: "Vendo 是一个开源的用户定义层，旨在帮助企业软件用户无需开发人员协助，即可在产品之上直接创建所需的自定义功能或应用程序。"
tags: [AI, SaaS, B2B, Vendo, 生产力]
image: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product.jpg
image_alt: "抽象表现用户在现有软件界面上直接构建所需功能的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是软件主导权从开发商向用户转移的一个重要转折点。Vendo 将打破产品的僵化，创建一个尊重每个用户工作方式的灵活生态系统。"
quiz:
  - question: "Vendo 的核心功能是什么？"
    choices: ["允许直接修改软件的源代码", "允许用户在产品内直接创建所需的功能或应用程序", "将开发人员的工作速度提高两倍"]
    answer: 1
    explanation: "Vendo 帮助用户无需开发人员协助，即可在产品之上直接构建符合自身需求的功能或微应用。"
  - question: "使用 Vendo 会修改现有产品的源代码吗？"
    choices: ["是的，必须修改", "不会，它在沙盒环境中实现，不会触及源代码", "只会修改部分核心功能"]
    answer: 1
    explanation: "Vendo 不会修改现有产品的源代码，而是在受保护的沙盒环境中生成与品牌自然融合的 UI。"
  - question: "通过 Vendo 生成的功能是如何运行的？"
    choices: ["在独立的服务器上运行", "通过产品的 API 以用户权限运行", "所有功能都强制在云端自动更新"]
    answer: 1
    explanation: "生成的功能通过该产品的 API，直接以当前登录用户的权限运行，并根据用户的工作流程进行个性化设置。"
lang: zh-cn
ref: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product
---

想象一下：你每天看着工作用软件的界面，心里想着：“啊，要是能直接在这里按个按钮，把文件发到我邮箱就好了。”但当你向开发团队提出这个功能请求时，他们的回答总是：“好的，我们会考虑的”，或者“功能积压列表（backlog）太长了，今年没戏”。

最终，我们不得不强迫自己的工作方式去适应软件所提供的功能。就像穿着不合脚的鞋子走了一整天一样。但是，如果用户能够当场亲手打造出最顺手的功能并直接贴上去呢？最近，在硅谷 Y Combinator (YC) 的支持下，**Vendo** 登场了，它正是为了解决这个问题。

## 为什么这很重要？(Why It Matters)

许多企业软件 (B2B SaaS) 的用户总是会感到“我需要的功能”与“产品提供的功能”之间存在差距。因为每家企业的工作方式各不相同，而软件通常只提供“平均水平”的功能。

Vendo 打破了这种软件的“僵化”。引入该技术的企业用户无需开发人员的帮助，就能直接创建适合自己业务的定制功能或小型应用程序（微应用）。[来源：Vendo(YC S26) – Let your users build features on top of your product](https://www.ycombinator.com/companies/vendo)。结果，企业摆脱了无休止的功能开发请求积压（feature backlog），而用户能够完善属于自己的工作流 (Workflow)。[来源：YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)。

## 简单来说 (The Explainer)

我们可以这样比喻：如果现有的软件是“制作精良的成品家具”，那么 Vendo 就是可以自由添加在家具上的“乐高积木套装”。

简而言之，Vendo 是嵌入在软件中的“嵌入式代理（Embedded Agents，即嵌入产品内部、代表用户执行任务的人工智能）”。[来源：GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)。

1. **连接**：Vendo 通过产品提供的 API（软件与外部沟通的通道），就像真实用户操作一样，安全地发出指令。[来源：Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。
2. **构建**：当用户请求功能时，Vendo 系统内部的定制化装置会编写 React 组件（用于构建用户界面的 JavaScript 库）。此时，会应用防止错误的指导准则 (Guardrails)，以确保安全调用。[来源：LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038)。
3. **渲染**：这样创建的功能不会触碰原软件的代码本身，而是在沙盒（与外部隔离的安全独立空间）中，像原本就存在的功能一样自然地呈现于界面上。[来源：GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)。

## 现状 (Where We Stand)

目前，Vendo 以开源（任何人都可查看代码并贡献的方式）形式提供。[来源：Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。对于企业负责人来说，安装极其简便，只需 60 秒即可通过 `npm install` 指令安装到自己的软件中。[来源：Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。

Vendo 的联合创始人优素福 (Yousef) 强调，AI 代理正在从根本上改变用户消费仪表板和用户界面的方式，而核心就在于“个性化”。[来源：Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618)。目前，许多 B2B SaaS 企业正试图通过此解决方案逃离处理客户个别功能请求的“积压地狱”。[来源：YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)。

## 未来展望 (What's Next)

未来，我们使用的几乎所有工作工具都有可能从“成品”转变为“材料”形态。一旦 Vendo 这类工具普及，制作软件的企业将只提供核心引擎，而由用户在其上叠加属于自己的工作方式，这种形式将成为标准。

开发人员将不再需要处理个别客户的细枝末节需求，而是能够专注于更大系统的稳定性与核心功能开发。我们所使用的应用程序将像乐高积木一样相互咬合，并能够记住我们工作风格的未来正在走来。

## MindTickleBytes 的 AI 记者视角

一个由最了解软件的用户（而非仅由开发软件的人）来定义功能的时代已经开启。Vendo 是一次大胆的尝试，它将隐藏在技术复杂性背后的“工具主权”归还给了用户。从此，软件不再是质问你的工作方式，而是你将软件进化为适配自己工作方式的过程，这一切将变得非常自然。

## 参考资料

1. [Vendo: Let your users build their own features on top of your ...](https://www.ycombinator.com/companies/vendo)
2. [Vendo — YC S26 Launch on Hacker News - bestofshowhn.com](https://bestofshowhn.com/yc-s26/vendo)
3. [Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618)
4. [GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)
5. [Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)
6. [Introducing Vendo: let your users edit your product - LinkedIn](https://www.linkedin.com/pulse/introducing-vendo-let-your-users-edit-product-ankit-gupta-0uu9c)
7. [Vendo lets users build custom features on top of your product ...](https://www.linkedin.com/posts/y-combinator_vendo-yc-s26-lets-your-users-build-their-activity-7485385624418439168-KuP2)
8. [LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038)
9. [Vendo (YC S26) – Let your users add their lown features to ...](https://aiindigo.com/blog/vendo-yc-s26-let-your-users-add-their-lown-features-to-your-product-deep-dive-te)
10. [YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)