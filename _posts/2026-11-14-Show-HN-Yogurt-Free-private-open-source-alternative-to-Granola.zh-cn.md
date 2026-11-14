---
layout: post
title: "告别每次会议都会闯入的监视者机器人！保护隐私的开源会议笔记应用“酸奶(Yogurt)”"
description: "介绍 Yogurt，一款免费、保护隐私的开源会议笔记应用，无需偷偷潜入 Zoom、Google Meet 或 Teams 会议的机器人，即可在您的电脑上安全运行。"
summary: "作为传统 AI 会议记录服务的替代方案（告别每次会议都有陌生机器人出席、让人心生顾虑的现象），开源桌面应用“酸奶（Yogurt）”正备受瞩目，它能在您的电脑本地安全地将语音转换为文字并进行总结。"
tags: [Yogurt, Granola, AI会议记录, 开源, 隐私保护, 端侧AI]
image: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola.jpg
image_alt: "象征 Yogurt 应用界面及会议笔记在本地安全处理的插图，置于电脑屏幕前"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "带着隐私与开源哲学强势切入由云服务主导的会议笔记市场的 Yogurt，将为开发者和注重隐私的用户带来一个令人欣喜的转折点。"
quiz:
  - question: "与其他许多会议录音工具相比，Yogurt（酸奶）最核心的不同特征是什么？"
    choices: ["AI 机器人不直接参与会议，而是在本地后台进行录音", "必须进行付费订阅才能导出文字记录", "如果没有网络连接则完全无法运行"]
    answer: 0
    explanation: "Yogurt 不会以机器人身份进入 Zoom、Google Meet 或 Teams 等会议，而是直接在你的电脑后台录制声音，从而保护隐私。"
  - question: "在 Yogurt 应用中生成的会议录音和总结保存在哪里？"
    choices: ["开发商的云服务器", "用户的电脑内部", "开源公共数据库"]
    answer: 1
    explanation: "Yogurt 旨在确保所有会议录音、文字转写（Transcript）和总结均不会泄露到电脑外部，仅保留在本地设备上。"
  - question: "Yogurt 是采用哪种许可证发布的开源项目？"
    choices: ["GPL v3", "MIT 许可证", "商业专有许可证"]
    answer: 1
    explanation: "Yogurt 是由 Eric 开发的、基于 MIT 许可证的自由开放的开源桌面应用程序。"
lang: zh-cn
ref: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola
---

想象一下：一场重要的内部会议或客户会议刚要开始，屏幕角落里却赫然出现了一个名字陌生的“AI 机器人（Bot）”。参会者莫名感到一阵紧张，挥之不去的是一种隐隐的不安：“这段对话会不会被原封不下地保密存储在某个云服务器上，以后被用来做广告定向投放或模型训练？”

我们日常使用的许多 AI 会议辅助工具在带来便利的同时，却会将我们宝贵的对话内容传输到外部云端，有时甚至强行要求付费订阅。特别是最近人气颇高的 Granola 等服务虽然也很优秀，但它们将完整导出功能限制在付费方案中，或者在数据加密管理方面存在种种限制 [Source 13]。打个比方，这就像你在写日记时，旁边总有个陌生人在偷看并审查内容一样憋屈。

为了从根本上解决这种憋屈感，一个全新的开源项目诞生了——这就是 **Yogurt（酸奶）**。通过 Hacker News 的 Show HN 走进大众视野的 Yogurt 是一款免费的开源会议笔记应用，它不需要将机器人引入 Zoom、Google Meet 或 Teams 等视频会议中，而只在你的电脑本地安全运行 [Source 1, Source 8]。

---

## 为什么这很重要？

对于现代职场人士、自由职业者和远程工作者来说，会议占据了一天中的很大一部分。记录并总结会议内容的 AI 工具现已成为必需品，但其背后总是伴随着“侵犯隐私”的标签。你所分享的敏感商业构思、个人对话或公司机密信息被存储在第三方云服务器上，无异于一颗随时可能引爆的安全事故定时炸弹。

Yogurt 从根本上解决了这个问题。基于**“我的会议记录只能存在于我的电脑中”**这一哲学，它被设计为会议录音文件、文字转写以及 AI 总结绝不会外泄到外部服务器 [Source 1]。开发者 Eric 注意到，利用体积小巧且功能强大的端侧（On-device）AI 模型，无需依赖昂贵的付费云服务，就能将硬件性能发挥到极致，从而制作出绝佳的会议笔记 [Source 1]。

此外，它作为完全开源（MIT 许可证）的项目公开，代码可被透明地验证，任何人都可以无需担心订阅费而自由下载和使用 [Source 1, Source 8]。对于对成本敏感的个人用户或需要严密安全的企业环境而言，这都是一个巨大的吸引力。用户再也不必支付高昂的月订阅费并受到功能限制了。

---

## 轻松理解：Yogurt 是如何工作的？

简单来说，Yogurt 就像是**“在你电脑里默默工作的私人助理”**。 

传统的会议录音机器人就像是猛然推开会议室大门、大喊“大家好，开始录音了”并令参会者感到紧张的外部观察员；而 Yogurt 则像是一个精密的录音机，静静地坐在会议室角落，只在你的笔记本上悄悄留下记录。 

Yogurt 的工作流程如下：

1. **无机器人的后台录音**：当开始 Zoom、Google Meet 或 Teams 会议时，Yogurt 不会以机器人账号进入会议室 [Source 1, Source 2]。相反，它会在后台检测用户的电脑音频系统并静默录音。其他人甚至无法察觉你正在运行会议记录应用。
2. **实时文字转写与总结**：会议进行期间，对话内容会实时转换为文字（Transcript）并显示在屏幕上 [Source 2]。会议结束后，端侧 AI 模型会立即总结核心内容，并将会议决定的行动计划（Action Items）、各参会者的待办事项以及个人笔记整洁地归纳好 [Source 2, Source 8]。
3. **本地数据存储**：生成的所有数据都不会传输到外部云端，而是安全地保存在用户的硬盘上 [Source 1]。 
4. **本地 MCP 服务器连接**：如果你想让性能更强大的前沿 AI 模型（例如 Anthropic 的 Claude、OpenAI 等）分析会议笔记，可以通过 Yogurt 提供的本地 MCP（Model Context Protocol）服务器由用户自行选择并连接 [Source 1]。完全无需依赖充当中介的付费云服务 [Source 1]。

这就像拍照时没有盲目上传到云端，而是保存在智能手机的默认相册中，仅在需要时分享到自己想要的地方一样。技术的控制权完全回归到了用户手中，而不是服务提供商。

---

## 现状：进展如何，有哪些功能？

Yogurt 是一款支持 Windows、Mac 和 Linux 的跨平台桌面应用 [Source 1, Source 5]。从开发初期开始，它就在 UI 交互、动画和硬件性能优化上下足了功夫，从而提供流畅且迅捷的用户体验 [Source 1]。

在最近发布的 v0.3.6 版本中，新增了自动更新及版本检查设置功能，甚至还加入了在 macOS 环境下安装后自动卸载（Eject）磁盘镜像（DMG）的贴心便利功能 [Source 11]。它展现出了极高的成熟度：无需创建账号---
layout: post
title: "告别每次开会都进来的监视者机器人！保护隐私的开源会议笔记应用“酸奶（Yogurt）”"
description: "向您介绍无需 Zoom、Google Meet、Teams 会议中偷偷潜入的机器人，在本地电脑安全运行的免费开源会议笔记应用——酸奶（Yogurt）。"
summary: "作为传统 AI 会议记录服务的替代方案，它不再让陌生机器人出席会议并引发拘束感，而是在本地电脑中安全地将语音转为文字并进行摘要。开源桌面应用“酸奶（Yogurt）”正备受瞩目。"
tags: [Yogurt, Granola, AI会议记录, 开源, 隐私保护, 端侧AI]
image: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola.jpg
image_alt: "放置在电脑屏幕前的酸奶（Yogurt）应用界面，具象化展示了会议笔记在本地安全处理的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "以隐私和开源精神为武器杀入由云服务主导的会议笔记市场的酸奶（Yogurt），将成为开发者和注重隐私用户的福音与转折点。"
quiz:
  - question: "酸奶（Yogurt）与其他许多会议录音工具最大的不同之处是什么？"
    choices: ["AI 机器人不直接参与会议，而是在本地后台进行录音", "只有订阅付费版才能导出转录文本", "如果没有网络连接则完全无法运行"]
    answer: 0
    explanation: "酸奶不会作为机器人加入 Zoom、Google Meet、Teams 等会议，而是在你的电脑后台直接录制声音，从而保护隐私。"
  - question: "酸奶应用中生成的会议录音和摘要保存在哪里？"
    choices: ["开发商的云服务器", "用户自己的电脑内部", "开源公共数据库"]
    answer: 1
    explanation: "酸奶旨在确保所有会议录音、文本转换（转录）和摘要都不会泄露到电脑外部，仅保留在本地设备上。"
  - question: "酸奶是以什么许可证分发的开源项目？"
    choices: ["GPL v3", "MIT 许可证", "商业专有许可证"]
    answer: 1
    explanation: "酸奶是由 Eric 开发的基于 MIT 许可证的自由且开放的开源桌面应用程序。"
lang: ko
ref: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola
---

想象一下。当你正要开始一场重要的内部会议或客户洽谈时，屏幕角落里突然出现了一个顶着陌生名字的“AI 机器人（Bot）”。与会者们心中难免会感到一丝紧张，心里总觉得犯嘀咕：“这段对话会不会原封不动地存放在某个云服务器上，以后被拿去当作广告定向投放或模型训练？”

我们日常使用的许多 AI 会议辅助工具虽然带来了便利，但其背后总是伴随着“侵犯隐私”的标签。我们分享的敏感商业创意、私人对话或公司机密信息被存储在第三方云服务器上，就像一颗不知何时会引爆的安全定时炸弹。

为了从根本上解决这种困扰，一个新鲜的开源项目应运而生。它就是——**酸奶（Yogurt）**。通过 Hacker News 的 Show HN 为世人所知的酸奶，是一款无需将机器人引入 Zoom、Google Meet、Teams 等视频会议，就能在本地电脑中安全运行的免费开源会议笔记应用 [Source 1, Source 8]。

---

## 为什么这很重要？

对于现代职场人士、自由职业者和远程工作者来说，会议占据了日常的大部分时间。能够记录和总结会议内容的 AI 工具现在已成为标配，但其背后往往附带着“隐私侵犯”的隐患。

酸奶从根本上解决了这个问题。秉持着**“我的会议记录只能存在我的电脑里”**的哲学，它在设计上确保了会议录音文件、文字转录本以及 AI 摘要内容绝不会有哪怕一次泄露到外部服务器 [Source 1]。开发者 Eric 注意到，利用变得小巧而强大的端侧（On-device）AI 模型，无需经过昂贵的付费云服务，就能够将硬件性能发挥到极致，从而制作出优秀的会议笔记 [Source 1]。

此外，它完全以开源（MIT 许可证）形式公开，代码可被透明审查，任何人都可以无需担心订阅费而自由下载使用 [Source 1, Source 8]。这对于注重成本的个人用户以及对安全性要求极高的企业环境来说，都具有巨大的吸引力。大家再也不用支付昂贵的月费却还要处处受限了。

---

## 轻松理解：酸奶是如何工作的？

简单来说，酸奶就像是**“一个在你电脑里默默工作的私人助理”**。

如果说传统的会议录音机器人是那种大摇大摆闯进会议室、大喊一声“大家好，我开始记录了”并让与会者感到紧张的外部旁听者，那么酸奶就像是一个安静地坐在会议室角落里、只在自己的笔记本上沙沙记录的精密录音机。

酸奶的工作流程可以按步骤概括为：

1. **无机器人的后台录音**：当开始 Zoom、Google Meet 或 Teams 会议时，酸奶不会以机器人账号进入会议室 [Source 1, Source 2]。相反，它会在后台侦测用户的电脑音频系统并静默录音。其他人甚至不知道你是否正在运行会议记录应用。
2. **实时转录与摘要**：在会议进行的同时，屏幕上会实时显示转录出的文本内容 [Source 2]。会议结束后，端侧 AI 模型会立即总结核心内容，并精简整理出会议决定的行动项（Action Items）、各参与者的待办事项以及个人笔记 [Source 2, Source 8]。
3. **本地数据存储**：生成的所有数据都不会传输到外部云，而是安全地保存在用户的硬盘中 [Source 1]。
4. **本地 MCP 服务器集成**：如果你想让拥有更强性能的前沿 AI 模型（如 Anthropic 的 Claude、OpenAI 等）来分析会议笔记，可以通过酸奶提供的本地 MCP（Model Context Protocol）服务器由用户自主选择连接 [Source 1]。完全无需依赖充当中间桥梁的付费云服务 [Source 1]。

这就好比拍照时不是盲目上传到云端，而是保存在智能手机的默认相册中，仅在需要时才分享到你想去的地方。技术的主导权重新回到了用户手中，而不是服务提供商。

---

## 现状：进展到什么地步了，有哪些功能？

酸奶作为一款跨平台桌面应用开发，支持 Windows、Mac 和 Linux [Source 1, Source 5]。从开发初期开始，它就在 UI 交互、动画和硬件性能优化上下足了功夫，提供流畅且快速的用户体验 [Source 1]。

在最近发布的 v0.3.6 版本中，新增了自动更新和版本检查设置功能，甚至还加入了在 macOS 环境下安装后自动卸载（Eject）磁盘镜像（DMG）的贴心便利功能 [Source 11]。它展现出了极高的完成度：无需创建账号或经历繁琐的连接过程，就能直接与日历同步并导入会议日程 [Source 1]。

在开源社区和科技博主之间，它作为 Granola 的优秀开源替代品（Open-Source Granola Alternative）广为流传，正在注重隐私的实干家和开发者之间迅速扩散 [Source 1, Source 9]。特别是在付费订阅模型大行其道的 SaaS 市场中，它既免费又提供强大的本地中心化功能，成为了巨大的差异化优势 [Source 1, Source 9]。

---

## 未来会怎样？

未来，AI 会议记录市场很有可能会分化为“以云端为中心的集中式服务”和“以本机为中心的隐私型端侧服务”。随着小型开源 AI 模型性能的飞跃式发展，用户已经完全不需要通过庞大的服务器，就能在个人笔记本或 PC 上获得高质量的摘要和问答（Chat with your meetings）体验 [Source 1]。

未来用户在存储会议记录时，首先会追问的一定是：“这些会议内容被传输到哪里去了？”像酸奶这样的项目，为开发者自由扩展功能、用户完全掌控自己的数据树立了标准。

或许不久的将来，那种开完会后怀着忐忑的心情请机器人退场的场景，将彻底被在电脑本地安全快速整理会议记录的全新方式所取代。

---

## AI 的视角：为什么值得关注？

以隐私和开源精神为武器杀入由云服务主导的会议笔记市场的酸奶，将成为开发者和注重隐私用户的福音与转折点。它堪称一个模范案例，向对集中式 SaaS 生态感到疲惫的用户展示了端侧本地 AI 与开源的结合能迸发出多么强大的替代力量。

---

## 参考资料

1. [Show HN: Yogurt – Free, private, open-source alternative to Granola](https://github.com/FrigadeHQ/yogurt) [Source 1]
2. [Yogurt: Free, private, open-source alternative to Granola](https://www.producthunt.com/products/yogurt) [Source 2]
3. [5 Best Open Source Granola Alternatives in 2026](https://openalternative.co/alternatives/granola) [Source 4]
4. [Best 10 Granola Alternatives & Competitors [2026] | Jamie](https://www.meetjamie.ai/blog/granola-alternatives) [Source 5]
5. [Free open-source alternatives to Granola | Maigentools](https://www.maigentools.com/alternatives/granola) [Source 6]
6. [Show HN: Yogurt – Free, private, open-source alternative...](https://daily.dev/posts/show-hn-yogurt-free-private-open-source-alternative-to-granola-w8zhburxd) [Source 8]
7. [Yogurt Growth Play: Free + Open Source Beats a Paid Leader ...](https://www.figuringoutwithai.com/growth/yogurt-free-open-source-granola-alternative-growth-play-2026) [Source 9]
8. [Yogurt AI: Granola的免费开源替代品，保护隐私的AI会议...](https://dev-hub.dev/news/8348) [Source 10]
9. [Yogurt AI: Free, Private, Open-Source Meeting Notes | AI/TLDR](https://ai-tldr.dev/tools/yogurt/) [Source 11]
10. [9 Best Granola AI Alternatives in 2026 (Compared & Reviewed)](https://www.getvoibe.com/resources/granola-alternatives/) [Source 13]