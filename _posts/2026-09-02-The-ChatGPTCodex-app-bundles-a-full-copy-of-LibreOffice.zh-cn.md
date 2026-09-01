---
layout: post
title: "电脑里的隐形巨人：ChatGPT 应用为何内置 LibreOffice？"
description: "近日发现 ChatGPT 桌面应用内置了 1.7GB 的庞大软件包，其中竟然隐藏着 LibreOffice 和各种开发工具。本文将带您一探究竟。"
summary: "OpenAI 的 ChatGPT 桌面应用在安装过程中被曝隐藏了一个大小达 1.7GB 的外部软件安装包。"
tags: [ChatGPT, OpenAI, 软件, LibreOffice, 技术新闻]
image: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice.jpg
image_alt: "展示 ChatGPT 应用内部文件夹结构的抽象图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ChatGPT 原本被视为简单的聊天应用，但其内置强大的开发与文档处理引擎这一点令人惊叹。这表明 AI 正在超越单纯的对话伙伴角色，演变为能在用户电脑上执行实际‘任务’的智能体（Agent）。"
quiz:
  - question: "ChatGPT 桌面应用内 'codex-primary-runtime' 文件夹的大小是多少？"
    choices: ["170MB", "1.7GB", "17GB"]
    answer: 1
    explanation: "该文件夹包含了约 1.7GB 的软件包。"
  - question: "以下哪项软件未包含在此安装包中？"
    choices: ["Python", "Node.js", "Microsoft Word"]
    answer: 2
    explanation: "安装包中包含了 Python、Node.js 和 LibreOffice 等，但不包含 MS Word。"
  - question: "为什么该应用要内置 LibreOffice 等外部工具？"
    choices: ["单纯浪费空间", "利用内部工具处理文档任务", "不可删除的库"]
    answer: 1
    explanation: "内置的技术文档显示，AI 正在学习如何查找并使用这些二进制文件。"
lang: zh-cn
ref: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice
---

## ChatGPT，不止于对话，更随身携带“工具箱”

试想一下：你给新买的智能手机装了应用，本以为只有基础功能，结果发现应用文件夹深处竟然整齐地堆放着几十本食谱和一整套工具箱。最近，OpenAI 的桌面应用程序（原名 Codex，现已重命名为 ChatGPT）就被发现了这种情况。[参考资料 1](https://simonwillison.net/2026/Sep/1/codex-libreoffice/), [参考资料 4](https://x.com/simonw/status/2094864223683903800)

在这个本以为只是聊天窗口的应用内部，准确地说是 `~/.cache` 文件夹下的一个名为 `codex-primary-runtime` 的隐秘空间里，竟然隐藏着一个高达 1.7GB 的庞大软件安装包。[参考资料 3](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache), [参考资料 5](https://news.ycombinator.com/item?id=49527396)

## 为什么这很重要？

用户可能会感到困惑：“它为什么要占用我电脑这么多空间？”但这种现象传递了一个重要信号：AI 正在从“会说话的鹦鹉”向“能办实事的助手”转变。过去的 AI 仅限于回答问题，而现在的 AI 正试图通过直接操纵你电脑中安装的工具（如 Python、文档编辑器等）来创造实际成果。

## 轻松理解：AI 的“工具箱”

我们可以这样比喻：你雇佣了一位厨师（AI）。以前的厨师只会口头告诉你菜谱，而现在的厨师直接走进你的厨房，摊开食谱（LibreOffice），拿起菜刀和炉灶（Python、Node.js），准备为你亲自烹饪。

事实上，该软件包中不仅包含了 Python（计算机语言执行工具）和 Node.js（Web 技术执行工具）的完整安装文件，还集成了 LibreOffice（开源文档编辑器）以及用于文档转换的 Poppler 等工具。[参考资料 1](https://simonwillison.net/2026/Sep/1/codex-libreoffice/), [参考资料 2](https://zeli.app/story/49527396) 有趣的是，应用内部还独立存在一份“使用说明书（Skills）”，详细记录了该如何调用这些巨大的工具。[参考资料 3](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache)

LibreOffice 是一款由全球志愿者共同开发的免费文档处理软件，任何人都可以研究并改进其运作原理。[参考资料 7](https://www.libreoffice.org/) OpenAI 通过在应用内部预先“植入”这些工具，构建了一个环境，使 AI 能够在接收指令后立即执行外部程序，无需等待下载或安装。

## 现状

目前，这一功能已通过 ChatGPT 桌面应用实现。[参考资料 8](https://github.com/openai/codex) 用户在界面上看到的是平淡无奇的对话框，但在后台，这套庞大的工具集正在待命，听候 AI 的调遣。[参考资料 9](https://filecr.com/windows/openai-codex/) 当然，强制捆绑软件的做法在某些用户看来像是浪费电脑资源，安全分析师和开发者们也对这些隐藏文件表示了惊讶。[参考资料 5](https://news.ycombinator.com/item?id=49527396)

## 未来发展

这种让 AI 随身携带“工具箱”的方式在未来会变得更加普遍。因为它标志着“智能体（Agent）”时代的正式开启——AI 不再仅仅是生成答案，而是直接在你的电脑上编辑文档、编译代码、分析数据。未来，你可能不仅是在与 AI 对话，还会看到 AI 亲手打开你电脑里的 LibreOffice 为你起草报告。

## MindTickleBytes AI 记者视角

AI 的智能化，归根结底在于其可操控工具范围的扩展。ChatGPT 内置 LibreOffice 是一个强有力的证据：AI 正在走出单纯的知识库，深入渗透到我们的实际生产环境之中。

## 参考资料

1. Codex bundles LibreOffice - [https://simonwillison.net/2026/Sep/1/codex-libreoffice/](https://simonwillison.net/2026/Sep/1/codex-libreoffice/)
2. Codex bundles LibreOffice — The ChatGPT/Codex app bundles a ... - [https://zeli.app/story/49527396](https://zeli.app/story/49527396)
3. OpenAI Codex app bundles LibreOffice, Python, Node in 1.7GB ... - [https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache)
4. Simon Willison on X: "Just noticed the ChatGPT desktop app ... - [https://x.com/simonw/status/2094864223683903800](https://x.com/simonw/status/2094864223683903800)
5. The ChatGPT/Codex app bundles a full copy of LibreOffice ... - [https://news.ycombinator.com/item?id=49527396](https://news.ycombinator.com/item?id=49527396)
6. GitHub - hashgraph-online/awesome-codex-plugins: A curated ... - [https://github.com/hashgraph-online/awesome-codex-plugins](https://github.com/hashgraph-online/awesome-codex-plugins)
7. Free and private office suite, no forced AI — LibreOffice - [https://www.libreoffice.org/](https://www.libreoffice.org/)
8. GitHub - openai/codex: Lightweight coding agent that runs in your... - [https://github.com/openai/codex](https://github.com/openai/codex)
9. OpenAI ChatGPT(With Codex) Download (Latest 2026) - FileCR - [https://filecr.com/windows/openai-codex/](https://filecr.com/windows/openai-codex/)