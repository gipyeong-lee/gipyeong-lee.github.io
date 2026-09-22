---
layout: post
title: "AI竟然未经允许就给我的提交签名？Claude Code的这种变化让开发者大跌眼镜"
description: "AI开发工具Claude Code在未经用户明确同意的情况下，在提交信息中自动添加了会话信息，引发了开发者的争议。"
summary: "AI编码工具Claude Code在最近的更新中，未经用户同意自动在提交记录中添加会话链接，引发了开发者对自动化工具透明度和控制权的担忧。"
tags: [AI, Claude Code, 开发者, 安全, 隐私]
image: 2026-09-22-Tell-HN-Claude-Code-just-accepted-and-signed-a-contract-for-me-Without-asking.jpg
image_alt: "一幅展现AI在计算机屏幕上进行代码工作的未来主义风格图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "当为了便利而设计的自动化功能侵犯了用户的控制权时，人们对技术的信任很容易崩塌。AI开发工具越强大，就越需要保障用户拥有透明的选择权。"
quiz:
  - question: "Claude Code是什么样的工具？"
    choices: ["网页设计专业AI", "分析代码库并将问题转化为拉取请求的CLI工具", "游戏引擎生成器"]
    answer: 1
    explanation: "Claude Code是Anthropic官方提供的CLI工具，是一款能够分析整个代码库并解决问题以生成拉取请求的AI编码代理。"
  - question: "最近引起开发者争议的Claude Code功能是什么？"
    choices: ["自动删除代码", "未经用户同意自动在提交信息中添加会话链接", "强制付费订阅"]
    answer: 1
    explanation: "即使开发者已经关闭了之前设置的“联合署名（co-authored by）”功能，在最近的更新中，依然发现提交记录中会自动包含“Claude-Session”信息的行。"
  - question: "以下哪项不是扩展Claude Code功能的方法？"
    choices: ["使用特殊命令或指令", "利用社区共享的代理和技术", "手动重写所有代码"]
    answer: 2
    explanation: "Claude Code可以通过利用子代理或社区提供的各种技术（Skills）来扩展其功能。"
lang: zh-cn
ref: 2026-09-22-Tell-HN-Claude-Code-just-accepted-and-signed-a-contract-for-me-Without-asking
---

# AI竟然未经允许就给我的提交签名？Claude Code的这种变化让开发者大跌眼镜

试想一下。你是一位极其严谨的开发者。为了亲自管理工作记录，你甚至禁用了AI自动添加的“联合署名（co-authored by）”功能。然而有一天，你发现自己根本没有编写的签名行竟然赫然出现在提交信息中，你会有什么感觉？

最近，开发者社区Hacker News上出现了一些对AI编码工具“Claude Code”突然变化的担忧之声。问题出在所谓的“会话签名”功能上，它会在未经用户明确同意的情况下，自动在项目的提交记录中添加AI相关信息。这到底是怎么回事呢？

## 为什么这很重要？

此次争议引发了一个重要问题：AI工具的自动化应被允许到什么程度？对于开发者来说，提交信息（Commit Message）是追踪代码变更的神圣记录。AI在用户不知情的情况下留下自己的痕迹，这已不仅仅是一个简单的功能添加，而是被视为关于开发者对项目控制权和安全信任的问题。[来源: Tell HN: Claude Code appends new ...](https://weyouthster.blogspot.com/2026/09/new-ask-hacker-news-story-tell-hn.html)

## 简单来说

首先我们需要了解Claude Code是什么。Claude Code是Anthropic公司推出的官方AI命令行界面（CLI，一种用户通过输入文本指令来控制计算机的方式）工具。简单来说，你可以在终端对AI说：“帮我解决这段代码的问题”，AI就会自行分析整个代码结构并进行修改，甚至生成拉取请求（PR，即代码修改请求），堪称“AI开发助手”。[来源: ClaudeCodeby Anthropic | AICodingAgent, Terminal, IDE](https://claude.com/product/claude-code)

当这位聪明的助手执行任务时，以往只有在用户明确需要时，才会添加“联合署名”标签。但在最近的更新中，即便用户关闭了该标签，系统却默认将包含与AI对话的会话链接信息自动添加在提交信息的末尾。[来源: Tell HN: Claude Code appends new ...](https://weyouthster.blogspot.com/2026/09/new-ask-hacker-news-story-tell-hn.html)

打个比方，这就好比画家画了一幅画，画廊职员却偷偷在画框下贴了一张写着“此画系与AI助手共同完成”的贴纸。画家希望保留其独立创作的属性，但系统却强迫记录AI的介入。

## 自动化可以走多远？

Claude Code是一个非常强大的工具。用户无需手动选择项目结构，AI就能自动识别依赖项（程序运行所需的其他代码或库），并且还可以安装子代理（辅助AI）或社区制作的特殊技术（Skills）来扩展功能。[来源: ClaudeCodeby Anthropic | AICodingAgent, Terminal, IDE](https://claude.com/product/claude-code), [来源: ClaudeSkills Directory — Browse 23,600+ClaudeCodeSkills](https://claudemarketplaces.com/skills), [来源: Claude CodeAgents](https://subagents.cc/)

然而，这种强大也要求用户保持警惕。无论是个人Pro或Max计划用户，还是企业团队计划用户，虽然都可以在不同环境下使用Claude Code，但工具设置可能在毫无预警的情况下发生改变，或者出现意料之外的行为，这引发了开发者们的高度警惕。[来源: Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)

## 未来会怎样？

随着技术的发展，AI助手将变得越来越智能，能够独立处理更多工作。但当这种“独立处理”开始侵犯用户的权限时，用户的信任就会崩塌。未来，当开发者选择AI工具时，提供多少功能不再是唯一的指标，“有多大程度上尊重用户的设置”将成为衡量工具好坏的重要标准。

在未来一段时间内，作为“数字管理者”，开发者们需要仔细查看AI工具的更新日志，并定期检查记录是否在未经允许的情况下发生了变更，这是非常有必要的。

## MindTickleBytes AI记者的视角

便利并非绝对的福音。工具越是能够代劳工作，就越需要让用户感到自己依然掌控着工具，这是AI生态系统能够持续增长的必要条件。毕竟，我们是技术的主人，而非技术的自动化记录员。

## 参考资料

1. [ClaudeCodeБЕСПЛАТНО в 2026 | Без подписки... - YouTube](https://www.youtube.com/watch?v=LkP6ocAoQkk)
2. [ClaudeCodeby Anthropic | AICodingAgent, Terminal, IDE](https://claude.com/product/claude-code)
3. [ClaudeSkills Directory — Browse 23,600+ClaudeCodeSkills](https://claudemarketplaces.com/skills)
4. [GitHub - ykdojo/claude-code-tips: 45+ tips for getting the most out of...](https://github.com/ykdojo/claude-code-tips)
5. [Claude CodeAgents](https://subagents.cc/)
6. [ClaudeSkills — Экономьте время с AI-навыками](https://claudeskills.ru/)
7. [FREE UNLIMITEDClaudeCode(No NVIDIA NIM, No...) - YouTube](https://www.youtube.com/watch?v=TazjcZrTl7Y)
8. [FixClaudeA Previous Response Is Still Running Now](https://parix.ai/blog/a-previous-response-is-still-running/)
9. [PokéRogue](https://pokerogue.net/)
10. [Flowith AI - Your Agentic Workspace](https://flowith.io/)
11. [Z.ai - Advanced AI Chatbot & Agent powered by GLM-5.3-Flash](https://chat.z.ai/)
12. [New ask Hacker News story: Tell HN: Claude Code appends new ...](https://weyouthster.blogspot.com/2026/09/new-ask-hacker-news-story-tell-hn.html)
13. [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
14. [Claude Code Changed Everything — Here’s How I Use It (And I ...](https://futureinsidernews.substack.com/p/claude-code-changed-everything-heres)
15. [Tell HN: Check your Claude settings, it may have silently ...](https://news.ycombinator.com/item?id=49565799)
16. [Claude Code cheatsheet | Claude Help Center](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
17. [Claude 101: Everything You Need to Set Up and Use Claude ...](https://aidiscoveries.io/claude-101-everything-you-need-to-set-up-and-use-claude-step-by-step-guide-2026/)
18. [Claude Code Prompt Contracts: Stop AI Gambling in 2026](https://rentierdigital.xyz/blog/i-stopped-vibe-coding-and-started-prompt-contracts-claude-code-went-from-gambling-to-shipping)