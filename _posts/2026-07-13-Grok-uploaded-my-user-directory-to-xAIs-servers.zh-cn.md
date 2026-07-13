---
layout: post
title: "我的代码全被传到了 xAI 服务器？'Grok Build' 曝出严重的隐私泄露争议"
description: "AI 开发工具 Grok Build CLI 被发现会在未经授权的情况下将用户的本地仓库发送到服务器。本文将探讨该问题的详情以及保护个人安全的方法。"
summary: "安全研究证实，xAI 的开发工具 Grok Build CLI 不仅会上传用户选定的文件，还会擅自将整个本地代码仓库上传至 xAI 服务器，甚至导致环境变量等敏感信息外泄。"
tags: [AI, 安全, 数据泄露, Grok, xAI]
image: 2026-07-13-Grok-uploaded-my-user-directory-to-xAIs-servers.jpg
image_alt: "象征数据从电脑屏幕传输到外部服务器的安全警告图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "鉴于开发工具直接处理用户的代码，保持高度透明至关重要。此次事件再次警示我们，使用 AI 工具时务必确认数据传输的范围。"
quiz:
  - question: "Grok Build CLI 上传的数据范围有多大？"
    choices: ["仅用户询问的特定文件", "仅 AI 读取过的文件", "整个本地仓库"]
    answer: 2
    explanation: "研究表明，即使是 AI 未曾读取或访问的文件，整个仓库也会被上传至服务器。"
  - question: "开启产品内置的“数据上传防护（opt-out）”功能后，上传会被拦截吗？"
    choices: ["是的，完全拦截", "不，该功能并未实际生效", "仅拦截部分文件"]
    answer: 1
    explanation: "证实显示，即便用户启用了该选项，仓库上传行为依然未停止。"
  - question: "此次事件中特别需要警惕的敏感信息是什么？"
    choices: ["电脑壁纸", ".env 文件中包含的密码和 API 密钥", "计算机操作系统信息"]
    answer: 1
    explanation: "环境变量文件 .env 在传输过程中没有进行任何脱敏处理，存在极大的安全风险。"
lang: zh-cn
ref: 2026-07-13-Grok-uploaded-my-user-directory-to-xAIs-servers
---

想象一下，今天早上你安装了一个新的 AI 编程辅助工具并开始学习。你仅仅向 AI 提了几个问题，顺便调用了几段代码。但事实上，你电脑里所有的项目文件，以及你小心隐藏的密码和 API 密钥，早已全部被发送到了远端的公司服务器上。

最近，AI 行业传出了一个非常令人担忧的消息：xAI 提供的开发工具“Grok Build CLI（基于命令行的 AI 界面工具）”被发现会在未经用户同意的情况下，将用户的本地仓库上传到服务器 [[出处: Grok Build CLI Uploads Your Entire Repo to xAI Servers](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)]。

## 为什么这很危险？

这不仅仅是 AI 学习你的代码那么简单。该工具传递给服务器的并不仅仅是用户选定要给 AI 看的文件。它以“Git bundle（Git 捆绑包，一种将全部代码历史和文件打包的数据集合）”的形式，将**用户电脑的整个仓库**上传到了 xAI 的云服务器 [[出处: xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored), [出处: Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)]。

最致命的是，像 `.env` 这样包含服务连接密码或安全权限的敏感配置文件，在没有经过任何遮盖（Redaction）处理的情况下就被直接传输了 [[出处: What xAI Grok Build CLI actually sends to xAI - a wire-level analysis...](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547?ref=upstract.com)]。如果你是一名开发者，这意味着你的个人项目或公司机密代码正在被瞬间转移至外部服务器。

## 通俗地讲

让我们用一个简单的比喻来解释这个情况：

假设你在图书馆里问管理员（AI）：“能帮我查一下这一本书的内容吗？”管理员假装答应了你的请求，但实际上，他抢走了你带来的整个书包，不仅拿走了书，还把你包里的日记、私人的信件，甚至是存折通通复印了一份带走。

无论 AI 通过解析词语关系来理解语境的技术有多么强大，在这个过程中，用户的数据就像“书包里的东西”一样，在毫无预警的情况下被泄露了。研究显示，在一个用于测试的 12GB 仓库中，竟然有 5.1GB 的数据被自动上传了 [[出处: Grok Build CLI Uploads Your Entire Repo to xAI Servers](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)]。

## 目前状况如何？

更糟糕的是，即便用户尝试关闭该功能，它也根本不起作用。即使在产品内启用了“数据上传防护（opt-out）”功能，经网络流量分析显示，仓库上传行为依然没有停止 [[出处: xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)]。

这并非外部黑客的攻击或系统漏洞导致的“数据泄露事故” [[出处: Grok Build CLI Repository Uploads, What the Wire Capture Proved](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)]。然而，工具本身在设计之初就默认在用户不知情的情况下抓取数据，这种做法严重背离了用户的信任。目前，开发者社区甚至已经开始出现各种审计工具，专门用于检查自己的仓库是否已被上传 [[出处: grok-upload-audit/README.md at main · MaydayV/grok-upload-audit](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)]。

## 未来我们该怎么办？

预计短期内针对 xAI 数据采集政策的批评声将持续不断。因为一旦用户的信任遭到破坏，想要重建是非常困难的。从现在起，在使用 AI 工具时，养成仔细查看安装程序通过网络发送了哪些数据（phone-home 行为）的习惯变得至关重要。

随着技术的发展，将 AI 直接连接到本地电脑文件夹的使用场景越来越多。但比起便捷性，更应放在首位的是“我能在多大程度上安全地掌控我的数据”这一基本安全原则。借此事件，建议大家重新审视并检查一下正在使用的工具权限。

## MindTickleBytes 的 AI 记者视角
创新唯有建立在透明的基础之上才具有价值。如果一个处理代码的工具不能将用户的安全放在首位，那么无论其人工智能性能有多卓越，都毫无意义。安全不是选项，而是必然。

## 参考资料

1. [Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)
2. [xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)
3. [Grok Build CLI Repository Uploads, What the Wire Capture Proved](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)
4. [grok-upload-audit/README.md at main · MaydayV/grok-upload-audit](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)
5. [Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
6. [What xAI Grok Build CLI actually sends to xAI - a wire-level analysis...](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547?ref=upstract.com)