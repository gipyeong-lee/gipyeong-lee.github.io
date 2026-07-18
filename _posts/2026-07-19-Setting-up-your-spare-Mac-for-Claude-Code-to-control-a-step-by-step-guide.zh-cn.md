---
layout: post
title: "我的旧 MacBook 能变身 AI 助手？用 Claude Code 远程控制 Mac 实操指南"
description: "分步指导如何利用闲置的旧 MacBook 安装 AI 助手 Claude Code，并实现远程控制。"
summary: "介绍如何将闲置 MacBook 设置为 Claude Code 专用 AI 远程设备，并通过主力办公电脑或智能手机轻松进行控制。"
tags: [AI, MacBook, Claude Code, 自动化]
image: 2026-07-19-Setting-up-your-spare-Mac-for-Claude-Code-to-control-a-step-by-step-guide.jpg
image_alt: "放在桌面上与主力办公 MacBook 连接并运行中的旧 MacBook"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "赋予旧设备新使命是可持续技术应用的精髓。希望通过本指南，你的 MacBook 能蜕变为聪明的 AI 助手。"
quiz:
  - question: "将旧 MacBook 作为 Claude Code 专用设备的主要原因之一是什么？"
    choices: ["为了提高 MacBook 的性能", "为了给 AI 代理构建一个远程且独立的运行环境", "为了延长电池寿命"]
    answer: 1
    explanation: "通过构建与主力工作环境隔离的独立设备，可以安全、高效地让 AI 执行屏幕控制和应用操作。"
  - question: "安装 Claude Code 前必须满足的条件是什么？"
    choices: ["最新款 M3 MacBook", "已订阅 Claude Pro 或激活账单的 Anthropic 账号", "独立的独立显卡"]
    answer: 1
    explanation: "使用 Claude Code 需要付费订阅 (Pro/Max) 或绑定账单的 Anthropic 账号。"
  - question: "远程控制已安装 Claude Code 的 Mac 的主要方式是什么？"
    choices: ["通过 SSH 连接并关联 Claude 应用", "随身携带 MacBook", "使用蓝牙键盘"]
    answer: 0
    explanation: "可以通过 SSH (Secure Shell，远程连接协议) 从其他设备控制，或者通过手机上的 Claude 应用关联使用。"
lang: zh-cn
ref: 2026-07-19-Setting-up-your-spare-Mac-for-Claude-code-to-control-a-step-by-step-guide
---

## 抽屉里的旧 MacBook，蜕变为 AI 助手

试想一下：清晨起床，你对手机上的 AI 说：“确认我今天的待办事项，打开指定应用整理资料。”这时，躺在抽屉角落里吃灰已久的旧 MacBook 自动唤醒屏幕，移动鼠标光标，运行应用并开始工作。这种仿佛有隐形人帮你操作电脑的魔幻场景，使用“Claude Code”工具即可变为现实。

高性能电脑不再是唯一选择。今天这篇指南将带你把闲置的 MacBook 变成“AI 专用远程设备”，让 AI 亲眼看屏幕、点击按钮并操作软件。

## 为什么这很重要？

AI 已经超越了简单的文本对话阶段，现在具备了**“电脑使用 (Computer Use)”**能力，像人类一样通过鼠标点击、键盘输入来操作软件 [出处: Claude Code 电脑使用能力](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)。

但是，如果让 AI 直接接管你的主力电脑，可能会担心隐私安全或工作干扰问题。如果把闲置的旧 MacBook 改造成一个“独立工作室”呢？不仅能安全地构建 AI 专用环境，还能让你随时随地通过手中的智能手机或主力电脑远程操控这台机器 [出处: 利用闲置 MacBook 作为 AI 远程设备](https://github.com/ykdojo/mac-claude-setup) [出处: 打造常驻 AI 控制的 Mac](https://github.com/ykdojo/claude-controls-mac)。

## 通俗解释：为 AI 装上“手”的过程

Claude Code 简单来说，就是给 AI 装上“数字鼠标和键盘”。打个比方，就是给你的旧 MacBook 装上能够由 AI 这个“大脑”指挥的“手脚”。

1. **指挥官 (AI) 与操作员 (MacBook)**：AI 下达指令（如“点击这里”），安装好的 Claude Code 会与 Mac 操作系统通信，真正地移动光标并按下按钮 [出处: AI 代理的 Mac 控制](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)。
2. **远程桥梁 (SSH)**：就像我们远程控制他人电脑一样，在你的主力设备和旧 MacBook 之间建立一条名为“SSH (Secure Shell，通过加密通信远程控制计算机的方式)”的安全通道 [出处: 通过 SSH 控制](https://github.com/ykdojo/claude-controls-mac)。

这样一来，旧 MacBook 就成了负责观看屏幕、点击和输入的“手脚”，而你则是在远程担任操纵这双手的“指挥官”。

## 安装准备

开始安装前，请准备以下物品：

* **闲置 MacBook**：旧一点也没关系，我们将把它作为远程控制的独立环境。
* **Claude 订阅**：需要拥有 Anthropic 的“Claude Pro”订阅，或已激活账单（绑定支付方式）的 Anthropic 账号 [出处: 必备资格条件](https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli)。

## 分步安装过程

安装过程主要通过终端 (Terminal，直接向计算机下达指令的文本界面) 完成 [出处: 基于终端的安装](https://www.serverman.co.uk/ai/claude/how-to-install-claude-code-on-mac/)。

1. **基础工具安装**：首先在 MacBook 上安装必要的软件工具。通常包括“Homebrew (Mac 软件包管理器)”、“Node.js (程序运行环境)”、“Git (代码版本控制工具)”等 [出处: 必备工具安装指南](https://dev.to/xujfcn/claude-code-installation-guide-for-macos-git-environment-variables-path-and-every-common-fix-4l96)。
2. **安装 Claude Code**：在终端窗口输入提供的指令即可安装 Claude Code [出处: 通过终端命令安装](https://www.kimi.com/resources/how-to-install-claude-code)。
3. **连接与配置**：安装完成后，关联你的账号。随后，为远程访问开启该设备的 SSH 设置，确保能从主力设备或手机随时连接 [出处: 远程连接设置](https://github.com/ykdojo/mac-claude-setup)。

安装过程中如遇问题，请仔细阅读终端窗口的提示。大多数情况是因为配置文件或权限问题导致的 [出处: 安装故障排除指南](https://docs.anthropic.com/en/docs/claude-code/overview)。

## 未来会如何？

完成此设置后，你就不再只是一个普通的 AI 聊天机器人用户，而是直接指挥 AI 代理的“管理员”。未来 Claude Code 将更加精进，能够自由操控更复杂的 macOS 应用。虽然目前可能以简单的点击操作为主，但不久之后，AI 就能在你的旧 MacBook 里熟练使用设计工具、代劳文档处理、通过网页冲浪整理信息，成为名副其实的秘书。

是时候让抽屉里的 MacBook 告别“废铁”身份，觉醒为智能 AI 伙伴了。

## 参考资料

1. [Setting Up Claude Code Locally with a Powerful Open-Source Model: A Step-by-Step Guide for Mac Users](https://medium.com/@luongnv89/setting-up-claude-code-locally-with-a-powerful-open-source-model-a-step-by-step-guide-for-mac-84cf9ab7302f)
2. [My Claude Code Setup Guide · GitHub](https://gist.github.com/graimon/0bf150c89d6c6844ab95866935bd4b0a)
3. [How to Set Up Claude Code on Mac (2026 Guide)](https://www.masteringai.io/guides/claude-code-setup-mac)
4. [Claude Code Installation Guide for macOS: Git, Environment Variables, Path and Every Common Fix](https://dev.to/xujfcn/claude-code-installation-guide-for-macos-git-environment-variables-path-and-every-common-fix-4l96)
5. [GitHub - ykdojo/mac-claude-setup: How to set up a spare Mac ...](https://github.com/ykdojo/mac-claude-setup)
6. [How to Install Claude Code on Mac (Step-by-Step Guide)](https://www.serverman.co.uk/ai/claude/how-to-install-claude-code-on-mac/)
7. [How to Build an AI Agent That Controls Your Mac: Claude Code Computer Use Setup Guide](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)
8. [GitHub - ykdojo/claude-controls-mac: Step-by-step guide to turning...](https://github.com/ykdojo/claude-controls-mac)
9. [How to Install And Use Claude Code - YouTube](https://www.youtube.com/watch?v=NQNrPaDPMiA)
10. [Terminal guide for new users - Claude Code Docs](https://code.claude.com/docs/en/terminal-guide)
11. [Claude Code overview - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
12. [Claude Skills Builder - Create Custom AI Skills for Claude Code](https://skills-claude.com/)
13. [Guide to use open models with Claude Code on your local device](https://unsloth.ai/docs/basics/claude-code)
14. [Claude Code CLI: Install on Mac/Windows, winget... | Inventive HQ](https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli)
15. [Install Claude Code: The Complete Guide for macOS, Windows...](https://www.morphllm.com/install-claude-code)
16. [Install Claude Code: Full Guide for Windows & Mac](https://www.kimi.com/resources/how-to-install-claude-code)
17. [Claude Code БЕСПЛАТНО через OpenRouter: настройка... - YouTube](https://www.youtube.com/watch?v=EMFMUEuNpWA)