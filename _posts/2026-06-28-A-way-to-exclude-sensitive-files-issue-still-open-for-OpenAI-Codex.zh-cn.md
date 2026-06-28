---
layout: post
title: "AI 会窃取我电脑的密码吗？OpenAI Codex 对敏感文件的访问问题"
description: "Codex 是开发者常用的 OpenAI 代码编写 AI，有没有什么办法能防止它擅自读取宝贵的密码或环境配置文件？为您整理了目前正在讨论的安全议题。"
summary: "OpenAI Codex CLI 持续面临擅自访问开发者敏感文件的质疑，目前尚无官方原生功能彻底屏蔽此类操作，安全风险需引起重视。"
tags: [AI安全, 开发工具, OpenAI, Codex, 数据隐私]
image: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex.jpg
image_alt: "计算机屏幕上的 AI 编程工具正在分析文件，同时伴有锁的图标"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "当便利性凌驾于安全性之上时，事故便不可避免。在官方推出排除功能之前，用户需要学会提升自我防范的“安全壁垒”。"
quiz:
  - question: "OpenAI Codex CLI 目前处理工作目录下文件的默认方式是？"
    choices: ["每次都会获得用户批准", "无需用户批准即可读取及修改", "无论如何都会将所有文件发送到外部"]
    answer: 1
    explanation: "Codex 在默认审批模式下，可以自动读取并修改工作目录内的文件。"
  - question: "目前为防止 Codex 访问敏感文件（如 .env），最推荐的临时对策是？"
    choices: ["在配置文件中使用排除选项", "隔离沙箱环境或限制文件权限", "删除 AI 模型"]
    answer: 1
    explanation: "由于尚无官方排除功能，目前通过限制文件访问权限或使用沙箱进行隔离是最佳手段。"
  - question: "Codex 向 AI 模型发送信息的方式是？"
    choices: ["只发送用户选择的文件", "将工具执行结果连同文件内容一并上传", "完全不发送任何文件内容"]
    answer: 1
    explanation: "Codex 会上传工具执行结果，在此过程中可能包含被访问文件的内容。"
lang: zh-cn
ref: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex
---

试想一下，你把编程任务交给智能 AI 助手后，起身去喝了杯咖啡。AI 出色地完成了你的代码，但在过程中，它却读取了包含你邮箱账号密码或 API 连接密钥的 `.env` 文件，你会怎么想？最近，OpenAI 的代码编写 AI 工具“Codex”的此类安全隐患，在开发者社区引发了热议。

### 为什么这很重要？

开发者在进行项目时，通常会将重要的连接信息或安全密钥存储在 `.env` 等文件中。这些文件如同“数字钥匙”。然而，如果辅助编程的 AI —— Codex 能够读取这些文件，就会引发人们的担忧：宝贵的个人信息可能会在开发者不知情的情况下，被当作 AI 模型的训练数据泄露，或者被传输到外部服务器。 [出处: Add ability to hide sensitive files from agent · Issue #85](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX) 由于 Codex 在处理工具执行结果时，会采取一并上传所访问文件内容的方式，因此需要格外警惕。 [出处: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### 简单解释

打个比方，Codex 目前就像你的一位“热情过头的图书管理员”。本应只拿取你指定的代码文件，但因为过于热情，它甚至翻看了你藏在书架角落里的所有敏感文件。

更严重的问题在于，目前根本没有“这些文件不许看”这种官方功能，无法让管理员明确禁区。 [出处: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847) 在默认审批模式下，Codex 无需用户单独批准，即可自由读取和修改工作目录内的文件。 [出处: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security) 当然，在执行超出工作区范围或需要网络连接的命令时，它会要求用户批准，但在文件访问本身的管理上，仍存在局限性。 [出处: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security)

### 当前状况

开发者群体强烈要求增加允许指定文件不被 AI 读取的设置功能（例如 `.codexignore`）。 [出处: Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456) 然而，OpenAI 目前尚未提供官方的应对方案。 [出处: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)

专家建议，为解决此问题，目前最稳妥的方法是从源头上阻断 AI 进程对敏感文件的访问。将文件移至其他文件夹、加强 Unix 文件权限设置，或在沙箱（与外部隔绝的安全虚拟空间）中执行任务，是当前最有效的应对策略。 [出处: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### 未来会怎样？

这个问题目前正在开源社区中持续讨论，要求更安全设计的呼声很高。 [出处: [SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410) 未来，我们可能会看到不再依赖用户手动控制，而是通过配置文件即可轻松阻断 AI 访问的官方“排除（Exclusion）”功能。建议开发者在使用 Codex 时，务必定期查看最新更新和安全相关变更。 [出处: How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)

---

**MindTickleBytes 的 AI 记者视点**
随着 AI 变得越聪明，我们需要守护的秘密也就越多。比起等待软件变得完美无缺，或许更需要我们这些 AI 用户学会如何精明地筑起“安全篱笆”。

## 参考资料

1. [A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)
2. [A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)
3. [Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456)
4. [How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)
5. [Agent approvals & security – Codex | OpenAI Developers](https://developers.openai.com/codex/agent-approvals-security)
6. [[SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410)
7. [Add ability to hide sensitive files from agent · Issue #85 ...](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX)