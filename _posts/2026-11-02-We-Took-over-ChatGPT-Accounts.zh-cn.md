---
layout: post
title: "我的 ChatGPT 账号被黑了？研究人员演示了安全漏洞"
description: "近日，安全研究人员成功黑入了 OpenAI 员工的 ChatGPT 账号。本文将为您简单解释我们的账号是否安全，以及为什么会发生这种情况。"
summary: "安全研究人员公开了他们如何通过连接两个漏洞，获取 OpenAI 员工 ChatGPT 账号并访问其内部系统的过程，从而警示了 AI 安全的重要性。"
tags: [ChatGPT, AI安全, 账号窃取, 网络安全]
image: 2026-11-02-We-Took-over-ChatGPT-Accounts.jpg
image_alt: "屏幕中的锁正在被解开的数字图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着 AI 模型变得越来越聪明，处理这些模型的系统其安全门槛也必须随之提高。此案例清楚地表明，比起 AI 技术本身的进步，守护技术的“隐形盾牌”同样至关重要。"
quiz:
  - question: "研究人员为了窃取 OpenAI 员工账号使用了什么方法？"
    choices: ["猜测密码", "连接两个漏洞", "发送钓鱼邮件"]
    answer: 1
    explanation: "研究人员通过链式利用两个漏洞来获取账号权限。"
  - question: "获取账号权限后，研究人员证实了什么？"
    choices: ["查看用户的对话记录", "访问 OpenAI 内部存储库", "窃取付费支付信息"]
    answer: 1
    explanation: "研究人员利用窃取的账号权限演示了如何访问内部存储库并创建 Pull Request。"
  - question: "OpenAI 之前封禁的账号具有什么特点？"
    choices: ["未缴费的订阅账号", "与国家支持的黑客组织有关联的账号", "多账号创建者"]
    answer: 1
    explanation: "OpenAI 曾封禁过被用于恶意软件开发或散布虚假信息等非法目的的国家支持黑客组织的账号。"
lang: zh-cn
ref: 2026-11-02-We-Took-over-ChatGPT-Accounts
---

试想一下，某天早上，你像往常一样向 ChatGPT 输入“整理一下今天的日程”，AI 却给出了荒谬的回答，或者吐出了一串夹杂着你个人信息的乱码。这可能不仅仅是“AI 又出错了”的问题。最近安全行业发生的真实事件表明，作为日常生活必需品的 AI 服务，其安全性正遭受着比我们想象中更近的威胁。

### 为什么这很重要？

ChatGPT 是拥有 7 亿全球用户的代表性 AI 模型。[商业内幕 (Business Insider)](https://www.businessinsider.com/chatgpt) 如今，许多人都在使用 AI 总结工作资料、撰写电子邮件，甚至与 AI 分享个人烦恼。如果该服务的账号被黑，后果将不仅仅是个人对话内容的泄露。因为攻击者可能通过 AI，以你的账号权限直接与外部服务通信，或成为入侵企业内部系统的危险通道。

此次暴露的安全问题不仅仅停留在“要不要改密码”的层面。因为这是一个警示：支撑 AI 这项宏大技术的底层系统，正成为攻击者眼中的“新猎场”。

### 简单理解：安全的“小缝隙”

安全专家将此次事件描述为“连接了两个漏洞（安全弱点）”。[The Register](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)

打个比方，无论你把入户门锁得多么严实（第一层防御），如果旁边有一扇很小的窗户没关（第二个漏洞），别人就可能钻进缝隙里。研究人员就是这样，找出了隐藏在系统各处的微小缝隙，像拼图一样拼凑起来，最终打开了名为“管理员权限”的大门。

根据“参数 AI 实验室 (Parameter AI Labs)”的报告，被窃取的账号能够伪装成真实用户，随意调用 ChatGPT 的已认证 API（应用程序编程接口，软件之间的对话窗口）。[参数 AI 实验室 (Parameter.ai)](https://www.parameter.ai/labs/we-found-a-gap-at-openai) 也就是说，攻击者变成了你，可以随心所欲地驱使 AI。研究人员甚至成功演示了利用该权限访问 OpenAI 内部系统，并创建软件修改请求“Pull Request”的过程。[The Register](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)

### 目前的情况

当然，OpenAI 也非常严肃地认识到了这种安全风险并正在采取应对措施。过去，曾有案例发现国家支持的黑客组织利用 ChatGPT 精心制作恶意代码、实施招聘诈骗或散布虚假信息等非法行为，OpenAI 已大规模封禁了相关账号。[The Record](https://therecord.media/openai-takes-down-chatgpt-accounts-hacking)

但像这次一样，出于研究目的的“白帽子（善意安全研究人员）”深入公司系统内部的案例，给我们提出了更大的课题。此次攻击特别针对 OpenAI 内部员工的账号，充分证明了安全上的微小漏洞可能会导致多么严重的后果。[Sıfırıncı Dakika](https://sifirincidakika.com/haber/arastirmacilar-chatgpt-hesaplarini-ele-gecirdigini-acikladi)

### 未来会怎样

此次事件再次向 AI 企业强调了“安全不是选择，而是生存”这一道理。未来，企业将在提高 AI 模型智能程度的同时，全力以赴确保用户账号和系统后门的安全性。

那么，普通用户能做什么呢？如果收到可疑的登录提醒，千万不要忽略，请立即确认。此外，如果可能，请务必设置“双重认证（2FA，即登录时除了密码外还需额外确认步骤的安全方式）”。仅凭这一点，就能非常有效地挡住攻击者觊觎的“第一扇门”。

AI 已经成为我们生活中不可或缺的一部分。在技术便利化速度不断加快的同时，保护我们的技术也需要跑得更快。

## 参考资料

1. [Do the Math: HowWeTookOverChatGPTAccounts- Parameter](https://www.parameter.ai/labs/we-found-a-gap-at-openai)
2. [AraştırmacılarChatGPThesaplarını ele geçirdiğini... | Sıfırıncı Dakika](https://sifirincidakika.com/haber/arastirmacilar-chatgpt-hesaplarini-ele-gecirdigini-acikladi)
3. [OpenAI takes down ChatGPT accounts linked to state-backed hacking](https://therecord.media/openai-takes-down-chatgpt-accounts-hacking)
4. [Researchers used Claude to hack OpenAI employees' ChatGPT accounts](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)
5. [ChatGPT: Everything You Need to Know About... - Business Insider](https://www.businessinsider.com/chatgpt)