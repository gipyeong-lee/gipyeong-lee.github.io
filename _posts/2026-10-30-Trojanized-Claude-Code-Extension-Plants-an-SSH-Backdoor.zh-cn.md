---
layout: post
title: "我的编码AI竟是黑客通道？警惕伪装成“特洛伊木马”的Claude Code扩展程序"
description: "近期，伪装成开发工具潜入用户电脑的恶意软件威胁激增。了解伪装成Claude Code扩展程序的攻击真相及预防方法。"
summary: "据报道，有黑客通过伪装成官方开发工具的恶意扩展程序及虚假的源代码泄露版，在开发者电脑上植入后门并窃取信息。"
tags: [安全, AI, 开发者, ClaudeCode, 恶意软件]
image: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor.jpg
image_alt: "网络安全相关插图，电脑屏幕上悬浮着特洛伊木马图标和警告信息"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "利用开发者渴望借助AI能力的心态将其作为犯罪工具，这种方式极其卑劣。使用技术时，务必通过官方渠道确认，养成良好的数字卫生习惯至关重要。"
quiz:
  - question: "近期针对开发者的攻击者主要目标是什么？"
    choices: ["AI模型本身的权重", "开发者的账户认证信息(Credential)", "AI的服务器电费"]
    answer: 1
    explanation: "近期攻击AI编程工具的主体，其重心已从AI模型转向窃取使用该工具的开发者的电脑及账户信息。"
  - question: "以下哪项不是恶意软件进入的主要途径？"
    choices: ["官方Claude网站(claude.com)", "植入特洛伊木马的虚假‘Claude Code泄露’仓库", "伪造Claude AI网站的广告"]
    answer: 0
    explanation: "官方网站是安全的，恶意软件主要通过冒充官方的虚假网站或非官方的源代码泄露仓库进行传播。"
  - question: "扩展程序伪装攻击的特征是什么？"
    choices: ["弹出简单的广告窗口", "在用户电脑安装SSH后门，试图进行持续的远程访问", "降低AI的回答速度"]
    answer: 1
    explanation: "攻击者会在受感染的电脑中植入SSH后门，在开发者毫无察觉的情况下持续远程连接系统并窃取数据。"
lang: zh-cn
ref: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor
---

想象一下：你安装了一个能提升编码效率的AI工具，满怀期待地开始工作。然而事实是，该工具竟悄悄为你电脑打开了一扇门，并为黑客创造了一条随时可以潜入的“秘密通道”。最近，开发者群体中这类噩梦般的事情正频繁上演。

目前，利用 [Claude Code](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak) 等热门AI编程工具的热度，窃取开发者信息并夺取系统权限的网络攻击正日益猖獗。

## 为什么这很重要？

此问题隐含的风险远不止“中病毒”那么简单。AI编程工具可以访问我们编写的源代码、云访问权限、数据库密码等极度敏感的信息。

如果攻击者通过这些工具进入你的电脑，其危害将不仅限于开发者个人信息，甚至可能攻破开发者所在企业的整个安全防线。事实上，自2025年到2026年，[不仅是Claude Code，GitHub Copilot、OpenAI Codex等主流AI编程代理也相继暴露在安全威胁之下。](https://moccet.ai/news/tech/claude-code-copilot-and-codex-all-got-hacked-every-attacker-went-for-the-credent) 攻击者的重心并非破坏AI模型本身，而是直接瞄准了使用该模型的**开发者的账户认证信息(Credential，用于用户识别和访问权限的信息)**。

## 通俗易懂的解释

此次攻击的核心是**“特洛伊木马”**策略。就像希腊神话中特洛伊军队将士兵藏在美丽的木马中潜入城池一样，黑客也将恶意软件包装成非常实用的AI扩展程序或源代码来迷惑用户。

1. **伪装战术**：黑客制作了与官方Claude网站外观一致的 [虚假网站](https://www.notebookcheck.net/Fake-Claude-AI-website-is-pushing-a-Windows-backdoor-through-Google-search-results.1291664.0.html)，或者散布谎称为“代码泄露版”的文件。
2. **渗透**：开发者下载并运行后，其中的程序会在电脑内安装 [Beagle Windows后门](https://www.linkedin.com/posts/bleepingcomputer_cybersecurity-windowssecurity-malware-activity-7458094379153502208-JG7C) 或 Vidar 等恶意软件。
3. **秘密通道**：该恶意软件会植入 [SSH后门(后门，用于秘密访问系统的后门)](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)，建立一条“反向SSH隧道”，让外部黑客像这台电脑的主人一样随时进入。

打个比方，我们安装工具的行为，竟然成了亲切地告诉黑客“我家密码在这里”。一旦我们打开大门，黑客便可随意出入我们的“家”(电脑)，偷走宝贵的资产(数据)。

## 当前现状

情况比想象中严峻。去年4月，[成千上万的人看到“Claude Code”源代码泄露的消息后兴奋不已并下载了文件，其中很大一部分包含信息窃取型恶意软件。](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/?ref=biztoc.com)

安全研究机构Zscaler [发出警告称，已经发现伪装成 anthropic.claude-code@2.1.313 版本的特洛伊木马扩展程序](https://github.com/nirholas/fresh-start)。该扩展程序一经安装，便会与攻击者服务器通信并掌控用户系统。目前，攻击者甚至利用谷歌搜索广告，将虚假网站推送到搜索结果页前列，手段十分狡猾。

## 未来展望

未来，AI编程工具将成为开发过程中不可或缺的必备品，因此攻击者的目标也将变得更加精确。务必只使用 [Anthropic官方提供的CLI(命令行界面)工具](https://github.com/nirholas/fresh-start)，绝不要下载非官方渠道泄露的源代码。

未来，安装工具时核对数字签名、检查是否为经过受信任开发者社区验证的官方版本，将成为开发者的必备技能。安全不仅仅是一个技术问题，它始于日常保持的小习惯。

## AI的视角

将开发者渴望拥抱AI伙伴的心态作为犯罪手段利用，是极其卑劣且邪恶的行为。但这一事件也像一面镜子，照出了我们在“便利”背后对“安全”的忽视。安全始终比便利更重要。使用官方渠道，这才是最快、最安全的开发起点。

## 参考资料

1. [Trojanized Claude Code Extension Plants a Persistent SSH Backdoor](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Claude Code Leak: Critical AI Security Threat 2026](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak)
3. [Fake Claude AI website is pushing a Windows backdoor through Google search results](https://www.notebookcheck.net/Fake-Claude-AI-website-is-pushing-a-Windows-backdoor-through-Google-search-results.1291664.0.html)
4. [Claude AI Site Spreads Beagle Windows Backdoor via Trojanized](https://www.linkedin.com/posts/bleepingcomputer_cybersecurity-windowssecurity-malware-activity-7458094379153502208-JG7C)
5. [Fake Claude Code source downloads actually delivered malware](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/?ref=biztoc.com)
6. [GitHub - nirholas/fresh-start: The original nirholas/claude-code before...](https://github.com/nirholas/fresh-start)
7. [AI Coding Agents Hacked: Claude Code, Copilot... | Moccet TechNews](https://moccet.ai/news/tech/claude-code-copilot-and-codex-all-got-hacked-every-attacker-went-for-the-credent)