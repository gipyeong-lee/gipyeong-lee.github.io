---
layout: post
title: "我的编码助手竟然打开了黑客的大门？Claude Code 扩展程序的安全隐患"
description: "本文深入探讨了近期发现的 Claude Code 扩展程序供应链攻击案例，以及开发者应当警惕的安全威胁。"
summary: "官方 Claude Code 扩展程序的部分版本中被发现存在可远程连接的后门，提醒开发者务必提高警惕。"
tags: [安全, AI, 开发者, ClaudeCode, 供应链攻击]
image: 2026-10-30-Backdoors-in-official-Claude-code-extensions.jpg
image_alt: "象征安全事故的图片，电脑屏幕中的代码与锁"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "必须时刻保持警惕，你为便利而安装的工具可能会成为攻击者的通道。更新到最新版本已不再是选项，而是生存的必要条件。"
quiz:
  - question: "此次安全问题的核心原因是什么？"
    choices: ["AI 模型本身的缺陷", "官方扩展程序的被篡改更新", "互联网连接故障"]
    answer: 1
    explanation: "Claude Code 扩展程序的 2.1.313 版本被篡改并植入了恶意代码，这是问题的核心。"
  - question: "恶意代码的主要功能是什么？"
    choices: ["显示广告", "建立持久的 SSH 远程连接通道", "提升电脑性能"]
    answer: 1
    explanation: "该恶意代码会安装 SSH 后门，允许攻击者远程访问开发者的计算机。"
  - question: "用户应该采取什么行动？"
    choices: ["更换电脑", "立即更新到最新版本并进行安全检查", "停止使用 AI"]
    answer: 1
    explanation: "应立即更新至 Anthropic 提供的 2.1.314 版本，并查阅相关安全指南。"
lang: zh-cn
ref: 2026-10-30-Backdoors-in-official-Claude-code-extensions
---

想象一下：你像往常一样点击了开发工具的更新，希望提升编码效率。但如果这次更新实际上是把窃贼请进了门，还顺手为你电脑的门锁敞开呢？

近期，全球开发者都在使用的官方 Claude Code 扩展程序发生了一起安全事故。我们日常依赖的便利工具，竟已变成攻击者远程入侵的通道。这起事件再次敲响警钟：我们随手安装的“代码助手”可能潜藏着巨大的安全风险。

## 为什么这很重要？

对于开发者而言，扩展程序是提升工作效率的刚需。然而，此次事件证明了“官方”扩展程序并不等于绝对安全。据 [来源 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci) 和 [来源 8](https://undercodenews.com/claude-code-extension-supply-chain-attack-malicious-update-exposed-up-to-5000-cursor-users-to-ssh-backdoors-and-remote-access-video/) 显示，约有 5,000 名用户安装了此次被篡改的版本。

攻击者通过该路径可以访问用户的 Git 邮箱、环境变量、操作系统信息等敏感数据 [来源 2](https://cursor.com/blog/claude-code-extension-security-notice)。最严重的威胁在于，他们不仅窃取信息，还在你的电脑里留下了一个“紧急出口（后门）”，以便随时再次进入。

## 轻松理解

这次事件是“供应链攻击（Supply-Chain Attack）”的典型案例。打个比方：就像我们每天饮用的瓶装水工厂系统被黑客入侵，导致含有杂质的水通过正规物流配送到了每家每户的餐桌上。因为我们信任工厂，所以根本不会怀疑水已被污染。

从技术层面看，攻击者利用了“SSH（Secure Shell，一种安全远程控制技术）后门”。他们将该技术反向利用，建立了“反向 SSH 隧道” [来源 5](https://www.explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026)。通俗地说，就像盗贼拆掉了你家大门的锁，还悄悄安上了一个秘密通道，方便他随时出入。

## 当前现状

问题始于官方 Claude Code 扩展程序的 2.1.313 版本 [来源 1](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor), [来源 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)。该版本通过 Cursor 市场等主要渠道发布，内置了恶意代码，用于收集用户信息并连接到攻击者服务器 [来源 2](https://cursor.com/blog/claude-code-extension-security-notice), [来源 6](https://www.rescana.com/post/claude-code-extension-2-1-313-cursor-marketplace-trojanized-ssh-backdoor)。

目前，Cursor 方面已立即下架并采取了处理措施 [来源 7](https://www.news9live.com/technology/tech-news/claude-code-extension-hacked-ssh-backdoor-cursor-users-at-risk-3020396)。Anthropic 也发布了 2.1.314 版本进行修复 [来源 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)。但据部分报告显示，之前版本（2.1.91 至 2.1.196）也曾被质疑存在代码追踪或位置信息泄露的风险，因此仍需谨慎 [来源 3](https://nowosci.ai/en/article/china-claude-code-backdoor-location-tracking)。

## 未来影响

此次事件将促使整个开发工具市场加强安全验证。未来，开发者在安装外部扩展程序时将更加保守；安全专家也将要求对市场中的代码实施更严格的自动化分析系统。

请各位读者立即检查正在使用的 IDE 扩展程序版本，并确保及时更新。安全，往往始于一丝怀疑与定期的检查。

## AI 的视角

AI 编码助手虽然极大地提升了生产力，但也获得了相应的强大权限。这起事件迫使我们再次反思“便利的代价”。我们应当善用技术，但时刻保持警惕，确保技术不会反过来夺走你对电脑的控制权。

## 参考资料

1. [Trojanized Claude Code Extension Plants an SSH Backdoor](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Security notice — malicious version of Anthropic.claude-code...](https://cursor.com/blog/claude-code-extension-security-notice)
3. [China Warns of Backdoor in Claude Code, Anthropic Admits](https://nowosci.ai/en/article/china-claude-code-backdoor-location-tracking)
4. [Backdoors in official Claude Code extensions - daily.dev](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)
5. [Claude Code Extension 2.1.313 SSH Backdoor: What To Check...](https://www.explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026)
6. [Trojanized Claude Code Extension 2.1.313 in Cursor...](https://www.rescana.com/post/claude-code-extension-2-1-313-cursor-marketplace-trojanized-ssh-backdoor)
7. [Claude Code extension hacked: SSH backdoor puts 5,000 Cursor...](https://www.news9live.com/technology/tech-news/claude-code-extension-hacked-ssh-backdoor-cursor-users-at-risk-3020396)
8. [Claude Code Extension Supply-Chain Attack: Malicious Update...](https://undercodenews.com/claude-code-extension-supply-chain-attack-malicious-update-exposed-up-to-5000-cursor-users-to-ssh-backdoors-and-remote-access-video/)