---
layout: post
title: "我的编程工具被黑了？回顾 Claude Code 扩展程序事件"
description: "本文回顾了最近 Cursor 编辑器中发生的 Claude Code 扩展程序被篡改事件的始末，并探讨了如何保护系统安全。"
summary: "10 月 29 日，部署在 Cursor 编辑器市场中的一个被篡改的 Claude Code 扩展程序尝试安装 SSH 后门，但被迅速拦截。"
tags: [安全, AI, Cursor, ClaudeCode, 问题]
image: 2026-11-02-Postmortem-on-Claude-Code-Cursor-extension-hack.jpg
image_alt: "电脑屏幕上出现安全警告弹窗，蓝色的编程工具图标变成了红色"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "编程工具的便捷背后承载着巨大的供应链安全责任。这次事件提醒我们，我们所使用的 AI 工具也需要像常规软件一样进行严格的验证。"
quiz:
  - question: "最近发生的 Cursor 扩展程序篡改事件的主要目的是什么？"
    choices: ["窃取 AI 模型训练数据", "安装 SSH 后门", "收集用户支付信息"]
    answer: 1
    explanation: "该被篡改的扩展程序试图通过安装 SSH 后门来获取对用户系统的访问权限。"
  - question: "在该事件中，被篡改的扩展程序在市场上曝光了多久？"
    choices: ["数月", "仅几个小时", "一周"]
    answer: 1
    explanation: "该篡改版本在 Cursor 市场上仅发布了几个小时就得到了处理。"
  - question: "为了防止软件供应链攻击，用户应注意什么？"
    choices: ["让所有扩展程序自动更新", "避免安装来源不明的扩展程序", "删除编程工具"]
    answer: 1
    explanation: "安装来源不明或不可信的扩展程序会增加安全风险，因此务必保持警惕。"
lang: zh-cn
ref: 2026-11-02-Postmortem-on-Claude-Code-Cursor-extension-hack
---

想象一下：你像往常一样打开基于 AI 的代码编辑器“Cursor”，准备在下班前做最后的代码收尾。系统提示你常用的 AI 工具扩展程序有更新。你毫无怀疑地点下了更新按钮。但就在那一刻，如果你电脑深处被打开了一条未经授权的秘密通道，会怎样？

10 月 29 日，许多开发者使用的 AI 工具“Claude Code”扩展程序中就发生了这样的事。今天，我们就来聊聊这个潜入我们日常生活的 AI 工具安全问题，以及它带给我们的启示。

### 为什么这很重要？

AI 编码助手现已成为开发者不可或缺的“助手”。但是，如果这个助手心怀不轨，为你打开了系统的后门，后果会如何？这次事件并非简单的 Bug，而是展示了所谓的“供应链攻击”（Supply-chain attack，即在软件制作或分发过程中植入恶意代码的攻击）的危险性。

我们使用的许多扩展程序往往在不知不觉中拥有了访问整个计算机系统的权限。像这次一样，一个受信赖的扩展程序被篡改，普通用户很难察觉。这不仅仅是几行代码被修改的问题，它意味着我们的整台计算机都有可能暴露给外部攻击者。

### 简单理解：“假更新”的木马

用一个非常简单的比喻来解释这次事件：假设你每天早上都会阅读投递到家里的“报纸”。但有一天，送报员在真报纸中间精心插入了一份“虚假号外”。当你展开那份假号外时，触发了某个装置，把你的入户门密码发送给了黑客。

[Claude Code 扩展程序（anthropic.claude-code，版本 2.1.313 及 2.1.312）](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/) 正是这份“虚假号外”。攻击者伪装成官方扩展程序，植入了一个在正常程序运行前先行工作的“加载器”（Loader，一种加载程序的特殊代码）。

该加载器试图暗中与攻击者的服务器通信，旨在开启所谓的“后门”（Backdoor，即绕过系统安全设置私下接入的秘密通道）。在此过程中，确认了其试图安装 **SSH 后门**（远程访问通道），以便攻击者远程控制用户的计算机。[来源：微软安全博客](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)

简单来说，黑客试图在你电脑里的私人空间偷偷开一扇后门。

### 当前状况：迅速行动的“数字消防员”

幸运的是，这次事件没有造成大规模的损失。因为 Cursor 在发现该篡改扩展程序后迅速采取了行动。带有恶意代码的假程序在市场上仅存在了[短短几个小时就被移除](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)。

然而，正如[俄罗斯主流 IT 媒体](https://www.comss.ru/page.php?id=22662)对此事的报道，大量开发者使用的 AI 编码环境成为攻击目标，这一事实足以引起我们的警觉。[通过 YouTube 公开的分析视频](https://www.youtube.com/watch?v=ipJbxVMODhE)也详细解释了攻击者如何精心植入加载器，并试图通过反向隧道进行通信的缜密过程。这就像是用极精湛的技术试图突破一栋高级公寓的安防系统。

### 未来会怎样？

通过这次事件，开发者们认识到在使用 AI 工具时，不能只图“便利”，还要重视“验证”的重要性。未来，即使是通过官方渠道分发的软件，也需要对安全更新或变更事项保持高度敏感。

此外，企业未来将加强安全体系，不仅是简单的“安装”扩展程序，还将更严密地监控它们拥有什么权限，以及访问系统的哪些区域。我们也应该养成避免安装来源不明的扩展程序的习惯，如果有可疑更新，请务必立即查阅社区或官方渠道。就像走在路上，绝对不会毫无戒心地喝下陌生人给的饮料一样。

### MindTickleBytes AI 记者的视角

技术的进步总是带来便利，但其背后必然伴随着安全阴影。这次 Claude Code 事件给习惯了便利的我们上了一课：安全的数字环境并非免费的午餐，需要我们时刻审视与警惕。在我们享受便捷的同时，安全就像时刻流动的生命体，一旦关注和戒备松懈，攻击随时可能卷土重来。

## 参考资料

1. [Inside a malicious Claude Code branded extension and its persistent SSH backdoor](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)
2. [Claude Code Copies in Cursor's Marketplace Hid an SSH... - YouTube](https://www.youtube.com/watch?v=ipJbxVMODhE)
3. [Бэкдор в Claude Code для Cursor: почему удаления плагина недостаточно](https://www.comss.ru/page.php?id=22662)