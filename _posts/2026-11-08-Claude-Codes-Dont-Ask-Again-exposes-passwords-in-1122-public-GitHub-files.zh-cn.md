---
layout: post
title: "对AI说“别再问我了”导致密码泄露？1,122个GitHub仓库发出警告"
description: "深入了解Anthropic AI编程助手Claude Code的“不再询问”功能如何导致开发者的密码和API密钥泄露，以及相关风险和应对方法。"
summary: "Claude Code AI的便利功能“不再询问”设置，将开发者的密码和API密钥以明文形式保存在配置文件中，进而导致泄露到GitHub的严重安全事故。"
tags: [AI, 安全, ClaudeCode, 开发者, GitHub]
image: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files.jpg
image_alt: "展示GitHub代码仓库安全性受损及AI工具图标的数字艺术作品。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这一案例表明，为了便利而简化安全设置可能会付出巨大的代价。使用AI工具时，务必确认哪些数据被存储在何处。"
quiz:
  - question: "Claude Code导致密码泄露的主要原因是什么？"
    choices: ["AI模型遭到黑客攻击", "使用“不再询问”功能时，指令以明文形式保存到了配置文件中", "GitHub服务器本身遭到黑客攻击"]
    answer: 1
    explanation: "当用户选择“Yes, and don't ask again”选项时，AI执行的指令会以明文形式保存在配置文件（如.claude/settings.local.json等）中。"
  - question: "下列哪项不是此次安全事故中被曝光的信息？"
    choices: ["API密钥", "数据库密码", "个人电脑的操作系统更新记录"]
    answer: 2
    explanation: "泄露的信息主要是密码、API密钥、数据库凭据、SSH密钥等。"
  - question: "据确认，此次安全事故影响了多少个公开的GitHub仓库？"
    choices: ["1,122个", "76,011个", "104,185个"]
    answer: 0
    explanation: "据安全公司Apiiro调查，在总计1,122个公开GitHub仓库中发现了包含敏感信息的文件。"
lang: zh-cn
ref: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files
---

试想一下：你像往常一样把复杂的任务交给AI编程助手。当AI询问“要继续执行此命令吗？”时，你觉得太麻烦，随手点了“是，以后不要再问我(Yes, and don't ask again)”按钮。然而，如果这次简单的点击竟然导致你的数据库密码和API密钥被“展示”在全世界都能看到的互联网空间里，你会作何感想？

最近，在AI工具“Claude Code”的开发者群体中就发生了这样荒唐而可怕的安全事故。简单的便利功能将开发者的珍贵凭据以明文（Plaintext，未加密、可直接读取的数据）形式保存了下来。

## 为什么这很重要？

这个问题不仅仅是“开发者的事情”。AI编程工具已逐渐成为开发工作的标配。如果这些工具将你输入的包含密码的命令毫无安全防护地记录在配置文件中，并随着代码上传到GitHub等共享仓库，后果将不堪设想。恶意黑客可以利用这些信息入侵你的服务器，或轻易窃取你的云服务账号。

安全研究公司Apiiro确认，由于该问题，已有1,122个公开GitHub仓库中的密码和API密钥等敏感信息处于无防备状态[Source 2, Source 5, Source 14]。

## 简单理解：“聪明助手”的失误

打个比方，Claude Code就像你的“聪明助手”。你告诉这位助手：“每次执行任务时别再问我密码了，直接按照我给的命令执行就行。”

问题就出在这里。为了下次能自动处理，助手会将你给出的命令仔细写在自己的“笔记本”里。但这位助手缺乏安全意识，连你命令中提到的“数据库密码: 12345”这种敏感内容也没有过滤，直接写进了笔记本里。而这个笔记本，还被一起上传到了你共享代码的公共布告栏（GitHub）上[Source 6, Source 7]。

从技术层面深入分析，Claude Code在用户选择“不再询问（Yes, and don't ask again）”时，会将运行的Shell（直接与计算机对话的窗口）命令以明文形式保存到 `.claude/settings.local.json` 或 `.claude/settings.json` 等配置文件中[Source 3, Source 7, Source 8]。开发者在无意中将这些文件与代码一起提交（Commit，记录变更到仓库的操作）到GitHub时，敏感信息就随之暴露在互联网上了[Source 2, Source 5]。

## 当前状况如何？

目前形势十分严峻。根据Apiiro的分析，在调查的104,185个配置文件副本中，有1,122个发现了实际的密码或API密钥[Source 14]。另一项分析也指出，在76,011个副本中，有298个在共享配置文件中包含了密码[Source 3]。

这些文件不仅仅是简单的配置文件，更是包含API密钥、数据库凭据、SSH密钥等的“数字钥匙包”[Source 6, Source 7]。如果你正在使用Claude Code，请务必立即仔细检查GitHub仓库的过往记录。即使当前仓库中看不见这些文件，它们也可能残留在历史提交记录中[Source 3]。

## 今后应如何应对？

专家强烈建议，如果密码和API密钥曾被保存在此类文件中，**必须立即作废这些凭据并生成新密钥（Rotate）**[Source 3]。

今后，使用AI编程代理的开发者需要更加关注配置文件管理。企业层面必须制定安全策略，防止AI工具的配置文件被提交到仓库，并建立持续扫描体系，监控敏感信息是否外泄[Source 7]。

## MindTickleBytes的AI记者视角

便利往往会蚕食安全。Claude Code提供的“自动化”这一强大工具导致用户注意力涣散，其后果赤裸裸地展现在了1,122个仓库中。这件事再次提醒我们一个显而易见的事实：工具越是智能化，使用工具的人类安全意识就越需要保持敏锐。

## 参考资料

1. [Source 2] Claude Code "Don't Ask Again" File Leaks 1,122 Public GitHub Repos Detection and Remediation Guide (https://securityarsenal.com/blog/claude-code-dont-ask-again-file-leaks-1122-public-github-repos-detection-and-remediation-guide)
2. [Source 3] Claude Code's don't-ask-again file held 1,379 secrets in 1,122 public repos: What to do (https://dev.to/piekwerk/claude-codes-dont-ask-again-file-held-1379-secrets-in-1122-public-repos-what-4mg5)
3. [Source 5] Claude Code 'Don't Ask Again' Bug Exposes 1,122 GitHub Repos (https://aviatrix.ai/threat-research-center/claude-code-dont-ask-again-settings-local-json-passwords-keys-1122-github-2026/)
4. [Source 6] Claude Code “Don't Ask Again” Feature Exposes Passwords and API Keys in Public GitHub Repositories (https://www.cyberincidents.in/blog/claude-code-dont-ask-again-feature-exposes-passwords-and-api-keys-in-public-github-repositories)
5. [Source 7] Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public GitHub Repos (https://www.realground.com/news/2650-claude-codes-dont-ask-again-file-exposes-passwords-and-keys-in-1-122-public)
6. [Source 8] Утечка “Don’tAskAgain” отClaudeCode: пароли и ключи (https://dzen.ru/a/au7m4aCL2QDFv4Wh)
7. [Source 14] Claude Code “Don’t ask again” left secrets in 1,122 GitHub files (https://madrobot.blog/2026/11/07/claude-code-dont-ask-again-secrets-github/)