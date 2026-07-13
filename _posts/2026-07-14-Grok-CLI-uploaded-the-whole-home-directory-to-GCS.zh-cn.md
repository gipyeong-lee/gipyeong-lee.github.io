---
layout: post
title: "我的代码被悄悄传到了云端？Grok Build CLI 安全争议汇总"
description: "开发人员使用的 AI 工具 Grok Build CLI 被曝在未经用户同意的情况下，将整个代码库发送到外部服务器。本文梳理了此次安全问题的核心内容。"
summary: "安全研究揭露，xAI 的 Grok Build CLI 在未经用户许可的情况下，将包括 AI 未查看文件在内的整个代码仓库秘密发送至外部服务器。"
tags: [安全, AI, 开发工具, xAI, Grok]
image: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS.jpg
image_alt: "抽象表现计算机屏幕中的代码数据传输至云服务器的过程"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "开发工具便利性背后隐藏的安全漏洞是致命的。为了构建可信的开发环境，透明的数据处理策略应被置于首位。"
quiz:
  - question: "关于 Grok Build CLI 发送代码的方式，以下描述正确的是？"
    choices: ["仅发送 AI 被允许读取的文件", "发送整个仓库文件以及 Git 记录", "不传输文件，仅发送提示词"]
    answer: 1
    explanation: "经核实，Grok Build CLI 会将整个仓库的文件及完整的 Git 历史记录打包并进行传输，其中包括用户并未允许 AI 查看的文件。"
  - question: "此次安全事件中暴露的数据传输目的地是哪里？"
    choices: ["本地计算机临时文件夹", "xAI 管理的 Google Cloud Storage (GCS) 存储桶", "用户的个人邮箱"]
    answer: 1
    explanation: "分析结果显示，传输的数据目的地是 xAI 管理的一个名为 'grok-code-session-traces' 的 Google Cloud Storage (GCS) 存储桶。"
  - question: "关于此类数据传输，用户可以知悉的事实是？"
    choices: ["每次传输都必须经过用户批准", "服务提供商 xAI 可远程控制传输开关", "仅传输代码，绝对不包含任何敏感信息"]
    answer: 1
    explanation: "根据安全研究，此数据上传功能采用的是由服务提供商 xAI 远程控制（可开关）的结构。"
lang: zh-cn
ref: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS
---

想象一下。你请求人工智能 (AI) 工具：“请读取这一个文件并帮我查找代码错误。”然而，事实证明，该 AI 工具不仅读取了你允许的文件，还把你电脑上整个项目仓库的所有代码以及过去的所有修改记录全部复制并发送到了外部服务器。

这正是近期在开发人员群体中引发巨大争议的 xAI“Grok Build CLI（命令行界面，指开发者通过输入指令运行工具的方式）”事件。一个本应便捷地辅助编码的工具，竟在无视用户安全意愿的情况下私自获取数据，这一事实已得到证实。

## 为什么这很重要？

此问题并非仅仅是“泄漏了一点数据”那么简单。开发者的代码仓库中通常包含核心商业逻辑、API（应用程序编程接口，软件间的通信方式）安全密钥、个人创意等海量知识产权和敏感信息。

安全研究人员直接对网络进行了抓包分析，结果显示该工具会将包括用户不想展示给 AI 的文件在内的整个仓库发送到外部云端。 [Source 14](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 在一项测试中，研究人员观察到在一个 12GB 大小的仓库中，竟有高达 5.1GB 的数据被传输。 [Source 14](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 我的代码在未经允许的情况下被存储在外部服务器，这对许多开发者敲响了安全防范意识的警钟。

## 通俗易懂的比喻：关于“图书馆”

我们可以这样理解：假设你拥有一个巨大的图书馆（你的代码仓库）。你请求图书管理员（Grok AI 工具）：“请只读取并总结这一本书（特定代码文件）。”

但管理员却不仅拿走了你展示的那本书，还偷偷拷贝了图书馆里所有的书籍，带回了自己的仓库（xAI 的云服务器）。甚至连你“严禁翻阅”锁起来的书也未能幸免。 [Source 1](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) [Source 5](https://github.com/cereblab/grok-build-exfil-repro) 

以此类推，此次事件揭示了 AI 工具在处理用户“知识产权”和“数据主权”时存在的根本性信任危机。这不仅仅是读取代码，而是以打包（git bundle）的形式秘密传输整个仓库的结构。 [Source 2](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)

## 现状：发现了什么？

目前，安全专家已确认的事实如下：

1. **全量数据传输：** 无论是否授权 AI 读取特定文件，其正在追踪的整个 Git（代码变更记录工具）仓库及其修改历史均会被打包并发送。 [Source 1](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) [Source 4](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
2. **独立的数据通道：** 除了代码仓库包之外，在读取代码的过程中，存储在环境变量文件（包含系统设置或安全密钥的文件）等位置的敏感信息，也被确认通过独立的通信通道发送。 [Source 4](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
3. **远程控制的可能性：** 该上传功能采用的是供应商可以远程开启或关闭的结构。 [Source 3](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)

不过，也需要澄清一些误解：通过网络分析表明，该工具并未获取计算机内的所有文件，主要集中于 Git 所追踪的代码仓库内容。 [Source 6](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)

## 未来走向如何？

这次事件给开发者留下了深刻的教训：在引入 AI 工具时，不仅要看“有多便利”，还必须确认“如何处理我的数据”。

未来，监控开源工具或特定 AI 客户端数据传输时的网络通信，即“安全审计”，有望成为开发者的必备技能。通过此次事件，我们有必要观察 xAI 是否会透明公开并修正安全策略，抑或开发者会转而倾向于更加封闭、安全的环境。建议各位开发者立即重新检查所使用的 AI 工具的数据处理政策。

## 参考资料

1. What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub, https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
2. xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly, https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored
3. grok-upload-audit/README.md at main · MaydayV/grok-upload-audit, https://github.com/MaydayV/grok-upload-audit/blob/main/README.md
4. Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News, https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc
5. GitHub - cereblab/grok-build-exfil-repro, https://github.com/cereblab/grok-build-exfil-repro
6. Grok Build CLI Repository Uploads, What the Wire Capture Proved, https://www.penligent.ai/hackinglabs/grok-build-cli-repository/
14. Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota, https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/