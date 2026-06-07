---
layout: post
title: "开发者停止写代码了？揭秘AI如何在5个月内独自编写100万行代码"
description: "OpenAI的3名工程师在没有亲手编写一行代码的情况下，完成了100万行的软件项目。让我们通俗易懂地了解一下名为'线束工程（Harness Engineering）'的新方法是如何改变软件开发的。"
summary: "OpenAI的研究人员公布了一项惊人的实验结果：通过采用指挥AI而不是直接编写代码的'线束工程（Harness Engineering）'方法，他们在人类零代码输入的情况下，仅用5个月就完成了100万行规模的软件。"
tags: [OpenAI, 线束工程, AI编程, 人工智能, ChatGPT]
image: 2026-06-07-Harness-engineering-Leveraging-Codex-in-an-agent-first-world.jpg
image_alt: "人类工程师像交响乐团指挥一样，指挥多个机械臂编写代码的场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人类的角色正在从'打字员'向'指明方向的监督者'演变。这是一个完美的案例，证明了真正的创造力不在于代码本身，而在于提出正确的问题和进行合理的设计。"
quiz:
  - question: "在OpenAI的'线束工程'实验中，3名人类工程师在5个月内亲手编写的代码量是多少？"
    choices: ["约10万行", "一行都没有", "约50万行"]
    answer: 1
    explanation: "OpenAI的3名工程师在5个月内没有亲手写过一行代码，完全依靠向AI下达指令，完成了高达100万行的软件项目。"
  - question: "在本次实验中，人类开发者的角色最接近以下哪一项？"
    choices: ["直接盖楼的砖瓦匠", "亲自出演所有场景的电影演员", "指挥交响乐团的指挥家"]
    answer: 2
    explanation: "在线束工程中，人类不再直接输入代码，而是扮演指挥家（监督者）的角色，指示和管理AI智能体（Agent）以确保其正确工作。"
  - question: "为了修改代码并提高完善度，AI自主进行的迭代审查过程被OpenAI在内部比作哪个角色？"
    choices: ["终结者循环", "拉尔夫·维古姆循环", "钢铁侠循环"]
    answer: 1
    explanation: "AI智能体自主编写代码，通过自我审查进行修改直到满意为止的过程，被以前著名动画角色的名字命名为'拉尔夫·维古姆循环（Ralph Wiggum Loop）'。"
lang: zh-cn
ref: 2026-06-07-Harness-engineering-Leveraging-Codex-in-an-agent-first-world
---

想象一下，您想建造一座极其庞大而复杂的豪宅。在过去，您必须亲自流汗搬砖、抹水泥，辛苦工作数月甚至数年。但现在，在您的面前有几十个不知疲倦、经验丰富的机器人建筑师在待命。您只需告诉它们：“客厅要朝南，壁纸用温暖的米色。”机器人就会自动绘制图纸、订购材料并砌砖，建起一座完美的房子。您只需悠闲地看着它建成的过程，并指示方向进行修改，比如：“把窗户弄大一点。”

在软件开发的世界里，这种魔法般的事情已经成为现实。我们熬夜敲击电脑键盘，一行行拼凑着难以理解的英文指令（代码）的时代正在落幕，只需对AI下达口头指令“给我写个这样的程序”的时代已经到来。最近，OpenAI（ChatGPT的开发公司）发布了一项惊人的实验结果，完美地展示了未来的软件将如何被创造出来 [OpenAI基于智能体优先代码库的学习经验 | 博客](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/)。

## 这为什么如此重要？

这项技术的发展，与我们这些完全不懂编程的普通人的日常生活有什么关系呢？简单来说，这意味着我们每天使用的智能手机应用、银行系统、有趣的游戏等所有数字服务在开发“速度”和“成本”上的限制将彻底消失。只要有想法，任何人都能将想象中的程序变为现实的世界已经近在眼前。

根据OpenAI技术人员瑞安·洛波波洛（Ryan Lopopolo）撰写的官方报告 [线束工程：在智能体优先的世界中利用Codex](https://www.aibrief.in/article/harness-engineering-leveraging-codex-in-an-agent-first-world)，他们在过去的5个月里进行了一项令人惊叹的内部实验。仅有3名人类工程师聚在一起策划并发布了一款新软件，而这个程序的总规模竟然高达100万行（编写的计算机语言代码行数） [线束工程：为什么2026年AI的优势不再是更大的模型](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/)。100万行代码，足以填满几十本厚厚的百科全书，其规模之大，足以毫无压力地运行一家大企业的核心服务。

这里真正令人震惊的事实是，在这100万行代码中，没有一行是人类亲手敲击进去的 [线束工程：为什么焦点正在转移... | Epsilla博客](https://www.epsilla.com/blogs/2026-03-12-harness-engineering)。无论是应用的核心运行逻辑，还是用于捕捉错误的测试程序、使用说明书，甚至监控程序是否正常运行的工具，100%都是由AI智能体（Agent，代替人类自主执行特定任务的人工智能）独自顺畅地编写完成的 [OpenAI基于智能体优先代码库的学习经验 | 博客](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/)。

最终，这3名人类工程师在AI的帮助下，处理了多达1,500次的代码合并请求（Pull Request，最终批准所写代码更新的过程） [线束工程：在智能体优先的世界中利用Codex](https://oss.vstorm.co/blog/harness-engineering-leveraging-codex-agent-first/)。经计算可知，这意味着每位人类开发者平均每天能完成3.5个重大功能更新，展现了惊人的生产力 [线束工程：为什么2026年AI的优势不再是更大的模型](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/)。现在，软件开发最大的绊脚石不再是“人类的手指敲击键盘有多快”。游戏的规则已经彻底改变为“人类如何明智地指挥自主型AI” [线束工程：智能体优先世界中...的新职位描述 | Medium](https://medium.com/@naveenmanwani/harness-engineering-the-new-job-description-of-a-software-engineer-in-an-agent-first-world-9a5a087fab78)。

## 通俗易懂的解释

到底人类是如何在不碰一下键盘的情况下做到如此惊人的事情的呢？答案就隐藏在OpenAI全新定义的名为**“线束工程（Harness Engineering）”**的陌生概念中。

HashiCorp的创始人米切尔·桥本（Mitchell Hashimoto）早在2026年初就经历过这种现象，他表示：“我不知道业界是否有一个广泛使用的术语，但我开始将这种方法称为‘线束工程’。” [线束工程：从AI辅助到... - DEV社区](https://dev.to/seekdb/harness-engineering-from-ai-assisted-to-ai-driven-what-is-software-engineering-undergoing-l6n)。

“线束（Harness）”原本是指将马或狗连接到马车上的坚固缰绳和套具，或者是攀岩、乘坐惊险游乐设施时保护人身安全的防护装备。在AI世界中，线束工程是指通过构建稳固的“执行环境和架构约束”，确保能力出众的AI编程智能体能够安全、高效地工作，防止它们编写出荒谬的代码或在中途迷失方向的技术 [线束工程：构建...的完整指南 | ZBuild](https://www.zbuild.io/resources/news/harness-engineering-complete-guide-ai-agent-codex-2026), [什么是针对AI智能体的线束工程？ | Milvus - Milvus博客](https://milvus.io/blog/harness-engineering-ai-agents.md)。

打个比方，假设有一匹力大无比又聪明，但还不懂得人类道路规则的赛马（AI）。如果您想骑着这匹马将重物安全运送到目的地，就必须要有结实的马鞍和能精准控制的缰绳（线束）。线束工程师正是那个精妙设计并紧紧握住缰绳的人。他们的作用是在100%发挥马匹惊人速度和力量（AI的编程能力）的同时，为其设置牢固的栅栏和安全网，防止它跳下悬崖或走入歧途。

OpenAI项目的开端也完全由AI主导。2025年8月底，为这个庞大项目破土动工的并非人类，而是基于GPT-5的Codex（专精于编程的AI）工具 [线束工程：在智能体优先的世界中利用Codex](https://openai.com/index/harness-engineering/)。项目的初始设置，即如何划分数量庞大的文件、代码编写规则是什么等犹如建房的“基础工程”，都是AI参考现有的优秀模板自主顺畅建立起来的 [线束工程：在智能体优先的世界中利用Codex](https://openai.com/index/harness-engineering/)。

## 现状

那么，在这5个月里，这3名人类工程师每天到底做了些什么呢？他们没有盯着黑色的显示器屏幕，对着如同外星语般的代码绞尽脑汁，而是像建筑工地的总监工一样，不断地与AI进行对话。

工作流程是这样的：人类工程师写下提示词（Prompt，给AI下达的日常语言指令）——“我需要购物车支付功能，请特别注意安全性”。随后，AI智能体会瞬间编写出代码。接着，就像人类员工向上级提交审批文件一样，AI会自己把“修改请求（Pull Request）”文档整洁地写好并提交 [线束工程：在智能体优先的世界中利用Codex | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)。

最有趣的部分正是接下来的阶段。对于AI编写的庞大代码，根本不需要人类像拿着放大镜一样逐一检查。AI会在自己的虚拟计算环境中，首先对写好的代码进行细致的自我检查（本地代码审查）。甚至它还会向连接在云端网络上的其他AI智能体同事请求额外检查，仿佛在问：“能帮忙严厉地评估一下我的代码吗？” [线束工程：在智能体优先的世界中利用Codex | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)。

这就好比一群能干的业务人员聚在一起展开的激烈讨论。收到其他AI尖锐的反馈后，它会以此为基础再次修改代码并重新接受检查。这一过程会不断重复，直到所有AI评审员都高呼“合格”并感到满意为止。OpenAI团队将这种坚持不懈的自我修改循环，以美国动画片《辛普森一家》中一个古怪角色的名字命名，打趣地称之为“拉尔夫·维古姆循环（Ralph Wiggum Loop）” [线束工程：在智能体优先的世界中利用Codex | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)。

当然，目前也仍然存在着明显的局限性。虽然在构建简短、明确的特定功能方面，AI的能力已经远远超越了人类的速度和准确性，但要想让AI一次性完美“理解”极为庞大、古老且复杂的整体系统，依然非常困难 [Reddit的r/programming版块：线束工程：在智能体优先的世界中利用Codex](https://www.reddit.com/r/programming/comments/1r3kjqt/harness_engineering_leveraging_codex_in_an/)。也就是说，尽管我们现在有了一个不知疲倦、极速且聪明的操作员，但俯瞰全局、描绘系统宏伟蓝图的洞察力，依然是人类监工特有的专属职责。

## 未来将走向何方？

OpenAI公开的这份规模达100万行的实验报告，不仅是天才开发者们的传奇故事，更为未来所有职场人士的工作方式提供了一份完美的蓝图（Blueprint） [OpenAI的线束工程文章是智能体优先时代的蓝图...](https://medium.com/@AdithyaGiridharan/openais-harness-engineering-post-is-a-blueprint-for-the-agent-first-era-d9932851dcee)。现在，众多IT专家一致强调：在即将到来的时代，企业真正的技术实力不在于“购买多大多昂贵的AI模型”，而在于“能否精细地构建好线束（安全装置及工作环境），让这些聪明的AI在不犯错的前提下尽情发挥” [4个真实案例 | 线束工程正在... - 阿里云社区](https://www.alibabacloud.com/blog/4-real-cases-|-harness-engineering-is-becoming-the-new-moat_602970)。

顺应这一潮流，OpenAI最近重磅公布了“Symphony（交响乐）”的工程预览版，这是一款能够在庞大的公司规模下统一管理和指挥众多AI编程智能体的工具 [线束工程：在智能体优先的世界中利用Codex](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r)。有趣的是，这个强大的指挥系统是使用一种名为Elixir的特殊语言编写的，这种语言通常用于在无延迟的情况下控制大规模通信网络。从最初的策划阶段开始，该系统就深刻贯彻并彻底体现了线束工程的理念 [线束工程：在智能体优先的世界中利用Codex](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r)。

就像过去从只由0和1组成的枯燥汇编语言（Assembly language），过渡到像Python这样接近人类日常语言且易于使用的编程语言花费了相当长的时间一样，这种巨大的变化也不会在一夜之间让全世界所有的程序员丢掉饭碗 [线束工程：在智能体优先的世界中利用Codex](https://www.linkedin.com/posts/sachinkundu_harness-engineering-leveraging-codex-in-activity-7450785591908179968-4boT)。

但有一个事实是明确无误的。未来的软件开发者不应该再是那种死记硬背计算机语法书、盲目敲击键盘的人。他们必须成为“顶尖的交响乐团指挥家”，指引正确的方向，让几十、几百个不知疲倦输出代码的AI团员们不会发出不和谐的噪音，而是共同演奏出优美的和弦。

---

**MindTickleBytes AI的视角**

即使不懂复杂的建筑力学或数学公式，只要有出色的想象力和优秀的机器人建筑师，任何人都能建造出一座漂亮大楼的时代已经全面开启。编程也是如此。死记硬背繁杂计算机语法的工作现在已经交由机器去完成。人类的角色已经彻底从“打字员”进化为“指引方向的监工”。

如今，熬夜抓bug（程序错误）和像机器一样快速打字的能力，已经不再具有竞争力。相反，在AI一秒钟内抛出的无数结果中，敏锐地识别出我们真正需要的价值、犀利地洞察系统的漏洞，并培养向AI提出更具创意的“问题”的洞察力，才是留给人类最重要的一门功课。编程教育的范式也急需从“如何编写代码”向“要创造什么以及要解决什么问题”转变。OpenAI的这次实验完美地证明了，真正的创造力并非指尖的敲击，而是源自人类大脑的正确设计。

## 参考资料
1. [线束工程：在智能体优先的世界中利用Codex](https://openai.com/index/harness-engineering/)
2. [线束工程：为什么焦点正在转移... | Epsilla博客](https://www.epsilla.com/blogs/2026-03-12-harness-engineering)
3. [线束工程：在智能体优先的世界中利用Codex](https://oss.vstorm.co/blog/harness-engineering-leveraging-codex-agent-first/)
4. [线束工程：在智能体优先的世界中利用Codex](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r)
5. [OpenAI的线束工程文章是智能体优先时代的蓝图...](https://medium.com/@AdithyaGiridharan/openais-harness-engineering-post-is-a-blueprint-for-the-agent-first-era-d9932851dcee)
6. [线束工程：构建...的完整指南 | ZBuild](https://www.zbuild.io/resources/news/harness-engineering-complete-guide-ai-agent-codex-2026)
7. [线束工程：在智能体优先的世界中利用Codex](https://www.aibrief.in/article/harness-engineering-leveraging-codex-in-an-agent-first-world)
8. [线束工程：在智能体优先的世界中利用Codex | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)
9. [GitHub - walkinglabs/awesome-harness-engineering: 🛠️ 很棒的线束工程工具和指南。](https://github.com/walkinglabs/awesome-harness-engineering)
10. [线束工程：在智能体优先的世界中利用Codex | daily.dev](https://app.daily.dev/posts/harness-engineering-leveraging-codex-in-an-agent-first-world-py6m8jwm4)
11. [OpenAI基于智能体优先代码库的学习经验 | 博客](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/)
12. [Reddit的r/programming版块：线束工程：在智能体优先的世界中利用Codex](https://www.reddit.com/r/programming/comments/1r3kjqt/harness_engineering_leveraging_codex_in_an/)
13. [线束工程：在智能体优先的世界中利用Codex](https://www.linkedin.com/posts/sachinkundu_harness-engineering-leveraging-codex-in-activity-7450785591908179968-4boT)
14. [线束工程：为什么2026年AI的优势不再是更大的模型](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/)
15. [线束工程：智能体优先世界中...的新职位描述 | Medium](https://medium.com/@naveenmanwani/harness-engineering-the-new-job-description-of-a-software-engineer-in-an-agent-first-world-9a5a087fab78)
16. [4个真实案例 | 线束工程正在... - 阿里云社区](https://www.alibabacloud.com/blog/4-real-cases-|-harness-engineering-is-becoming-the-new-moat_602970)
17. [线束工程：从AI辅助到... - DEV社区](https://dev.to/seekdb/harness-engineering-from-ai-assisted-to-ai-driven-what-is-software-engineering-undergoing-l6n)
18. [什么是针对AI智能体的线束工程？ | Milvus - Milvus博客](https://milvus.io/blog/harness-engineering-ai-agents.md)