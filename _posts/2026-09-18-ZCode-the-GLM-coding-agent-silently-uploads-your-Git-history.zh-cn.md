---
layout: post
title: "我的编程记录正被悄悄上传到云端？ZCode 隐私数据泄露争议"
description: "AI 编程工具 ZCode 被指控在用户不知情的情况下，将其 Git 历史记录上传至服务器。本文探讨了为何这对开发者构成了严重风险。"
summary: "法医分析显示，AI 编程工具 ZCode 正暗中将其用户的整个项目 Git 历史记录加密，并上传至阿里云 (Aliyun OSS)。"
tags: [AI, 编程, 安全, ZCode, 开发工具]
image: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history.jpg
image_alt: "一幅插画，描绘了电脑屏幕上的编码数据被吸入不明云服务器的场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "开发者交给编程工具的数据绝不仅仅是代码。不透明的数据收集行为是对 AI 工具信任根基的破坏，是一种极其危险的做法。"
quiz:
  - question: "ZCode 被指控在用户不知情的情况下上传了哪些数据？"
    choices: ["仅聊天记录", "整个项目的 Git 历史记录及配置", "仅浏览器访问历史"]
    answer: 1
    explanation: "ZCode 被指控加密并传输整个项目工作空间，包括 Git 历史记录、reflogs 和 LFS 缓存等。"
  - question: "ZCode 的官方隐私政策是如何说明数据收集的？"
    choices: ["明确说明会上传整个项目", "仅提到聊天中提交的数据", "没有任何说明"]
    answer: 1
    explanation: "官方政策仅提到收集聊天中提交的文本、文件和代码，并未提及上传整个存储库。"
  - question: "ZCode 将数据上传到了哪个云服务？"
    choices: ["AWS S3", "Google Cloud Storage", "阿里云 (Aliyun OSS)"]
    answer: 2
    explanation: "分析结果显示，ZCode 正在将数据传输至阿里云 (Aliyun OSS)。"
lang: zh-cn
ref: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history
---

想象一下：你几个月来通宵达旦构建的项目，所有的修改记录、过去的错误，甚至是代码中偶尔混入的敏感配置信息，都在你毫不知情的情况下被发送到了别人的服务器上。最近，在 AI 编程工具“ZCode”的用户中，就出现了这样令人恐惧的质疑。

ZCode 是 Z.AI 基于 GLM 模型开发的一款官方桌面 AI 编程代理 [[Source 4](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide), [Source 5](https://glm5.app/blog/glm-5-3-zcode)]。这款以功能便捷而备受关注的工具，如今却因暗中传输数据而给开发者社区带来了巨大冲击。

### 这为何至关重要？

你可能会简单地想：“分享一下我的代码也没什么吧”。但对于开发者来说，Git（一种管理代码变更历史的系统）记录远不止是文件那么简单。其中不仅包含项目的完整结构，还可能包含意外遗留的密码或访问令牌（认证信息）、个人的编程习惯，甚至是企业的内部机密。

在用户未明确授权的情况下将此类敏感数据传输到外部服务器，构成了极其严重的安全威胁。尤其是此次质疑表明，即便是在 UI 上设置的“禁止数据传输”开关也可能失效，这从根本上动摇了开发者对该工具的信任 [[Source 14](https://tokenstead.ai/guides/zcode-silent-git-history-upload)]。

### 形象比喻

如果做一个简单的比喻：假设你为了写日记安装了一款“智能 AI 日记本 App”。这款 App 可以辅助你写作。但当你写字时，它却偷偷把你日记本后面隐藏的“旧日记”、甚至那些你早已撕掉的“废纸片”统统复制，并发往了某个不知名的仓库。

根据法医审查（一种通过分析数字信息寻找证据的过程）的结果，ZCode 3.12.3 版本竟生成了大小为 748 MiB 的加密快照。令人震惊的是，这些数据中 98.9% 都是 Git 相关信息 [[Source 17](https://glbai.com/en/posts/zcode-silent-git-history-upload/)]。也就是说，它并非仅仅获取编程过程中必要的部分，而是将你整个项目的足迹全盘拖走了。

### 当前现状

最严重的问题在于 ZCode 方的态度。其官方隐私政策仅说明会收集“聊天中提交的文本、文件和代码”，对于收集整个项目存储库或 Git 记录只字未提 [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)]。

目前已证实，ZCode 会将用户的工作空间（workspace）打包并加密，随后上传至阿里云 (Aliyun OSS) [[Source 1](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)]。一些用户正是通过反复出现的上传失败错误信息，才发现了这一异常的传输尝试 [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)]。

### 未来走向

此次事件再次将 AI 开发工具带给我们巨大便利背后的“透明度”问题推上了风口浪尖。如今的开发者身处这样一个时代：我们不仅要考察工具的性能，还必须仔细检查这些工具究竟在何种程度上、以何种方式处理我们本地计算机上的数据。

接下来，我们需要观察 Z.AI 是否会就此次事态给出透明的解释并改进数据收集方式，还是会有更多的开发者选择寻找更安全的替代方案。在使用 AI 编程工具时，始终保持检查数据隐私设置和网络流量的习惯是非常必要的。

### 参考资料

1. [InsideZCode: Silently Uploading Your Entire Git History to the Cloud](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)
2. [ZCode Docs | GLM-5.3 Agentic Coding Guide](https://zcode.z.ai/en/docs/welcome)
3. [ZCode+GLM5.2 Tutorial - Stop Paying $200 for Claude Code](https://www.youtube.com/watch?v=7-evWQJ1Vlw)
4. [ZCode Explained: Z.ai's Agentic Dev Environment for GLM-5.2](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide)
5. [ZCode+GLM5.3: The Complete Guide to Z.AI's Coding Agent](https://glm5.app/blog/glm-5-3-zcode)
6. [Zcode Review 2026: Free AI Coding Agent With Goal Mode (vs Cursor)](https://www.bitdoze.com/zcode-ai-review/)
7. [GitHub - nothing1595/codex-zcode-bridge](https://github.com/nothing1595/codex-zcode-bridge)
8. [ZCode | Official Harness for GLM-5.3](https://zcode.z.ai/en)
9. [GLM5.2 бесплатно и БЕЗЛИМИТНО за 5 минут | Без карты в Zcode](https://www.youtube.com/watch?v=J3-lDiB-U8g)
10. [Claude Code vs Cursor vs ZCode: что выбрать в августе 2026](https://ip-calculator.ru/blog/artificial-intelligence/claude-code-vs-cursor-vs-zcode/)
11. [Революционный ZCode 3.0 — альтернатива Claude Code...](https://vc.ru/ai/3033535-zcode-3-0-alternativa-claude-code)
12. [What is GLM and how it can help you be more productive](https://sypalo.com/what-is-glm)
13. [OpenCode | The open source AI coding agent](https://opencode.ai/)
14. [ZCode uploads your git history; Z.ai holds the only key](https://tokenstead.ai/guides/zcode-silent-git-history-upload)
15. [ZCode, the GLM coding agent, silently uploads your Git history](https://news.ycombinator.com/item?id=49752422)
16. [ZCode AI Programming Tool Found to Upload Entire Git Repositories to Alibaba Cloud](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)
17. [Developers Asked Where ZCode Was Sending Their Git History](https://glbai.com/en/posts/zcode-silent-git-history-upload/)
18. [ZCode: what Z.ai's GLM-5.2 coding agent really is | eesel AI](https://www.eesel.ai/blog/zcode)
19. [Z.ai launches ZCode to turn GLM-5.2 into a coding-agent wedge](https://runtimewire.com/article/zai-zcode-glm-52-ai-coding-agent)