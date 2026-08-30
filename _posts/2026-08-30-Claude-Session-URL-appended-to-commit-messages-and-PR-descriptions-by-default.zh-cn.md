---
layout: post
title: "我的编程记录竟然被公开了？警惕 Claude Code 的‘会话 URL’"
description: "AI 编程工具 Claude Code 会在提交记录中自动添加会话 URL，本文将探讨由此引发的隐私与机密泄露隐患及其应对方法。"
summary: "Claude Code 自动嵌入的会话 URL 存在泄露对话内容的风险，许多用户强烈要求将其更改为可选（opt-in）功能。"
tags: [AI, 编程, ClaudeCode, 安全, 隐私保护]
image: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default.jpg
image_alt: "计算机屏幕上显示的代码提交记录，旁边悬浮着危险警告图标"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "开发过程的透明度固然重要，但若将与 AI 的私密对话随代码一同发布，将构成严重的安全隐患。信息保护应置于功能便利性之上。"
quiz:
  - question: "为什么 Claude Code 在提交信息中添加的‘会话 URL’会成为问题？"
    choices: ["因为它导致代码运行缓慢", "因为它可能泄露完整的对话记录", "因为它占用了大量存储空间"]
    answer: 1
    explanation: "点击该 URL 即可查看与 AI 的完整对话内容，存在敏感信息外泄的风险。"
  - question: "之前的 'attribution.commit' 设置是否能够关闭会话 URL？"
    choices: ["是的，可以完美控制", "不能，会话 URL 不在控制范围内", "部分可以"]
    answer: 1
    explanation: "用户指出，最初即便配置了 'attribution.commit' 或 'attribution.pr'，也无法控制会话 URL 的自动插入。"
  - question: "开发者社区要求 Anthropic 采取的合理改进方向是什么？"
    choices: ["彻底删除会话 URL 功能", "将默认值更改为‘不启用（opt-in）’", "提供更长的 URL"]
    answer: 1
    explanation: "用户持续要求将默认设置改为‘加入许可（opt-in）’模式，以便仅在需要时才选择激活。"
lang: zh-cn
ref: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default
---

想象一下：今天早上，你为了一个极其机密的研发项目，与 AI 编程助手紧密协作编写代码。你还特地叮嘱过：“这部分是公司内部机密，绝对不能外泄。”然而几天后，当有人进入代码库（Repository）时，无意中点击了代码旁附带的链接，会发生什么呢？通过那个链接，你与 AI 之间的所有对话内容将瞬间展现在对方屏幕上。

近期，使用 AI 编程工具“Claude Code”的开发者们对此深感忧虑。大家指出，这项旨在提升开发效率的功能，正成为意想不到的安全漏洞通道。

### 为什么这很重要？

大多数开发者会将代码记录在 Git 等版本控制系统中。Claude Code 在编写代码后，会自动在提交（Commit，代码变更记录）信息和合并请求（PR，代码合并申请）的正文中，添加一个包含“Claude-Session”字样的 URL [Source 1, Source 5]。

从表面上看，这似乎只是标注了“此代码由 Claude Code 编写”的来源说明。但一旦点击该链接，创建代码时的**完整对话记录**就会直接暴露 [Source 5]。这其中不仅包含代码，还可能涉及保密项目的方案、安全相关的探讨，甚至公司内部的机密对话。如果该代码库是公开的，那么你的所有思考过程和开发细节也将彻底暴露在公众面前 [Source 5]。

### 形象比喻：‘草稿纸’与‘便利贴’

我们可以用一个比喻来理解这个问题：如果你编写的代码是“最终成品”，那么与 AI 的对话就是为了实现该成品而在草稿纸上留下的“所有涂鸦与思考痕迹”。

现在的 Claude Code 相当于在提交成品时，顺手把草稿纸上写的所有内容贴在便利贴上，并将其附在成品一起发布 [Source 6, Source 7]。问题的核心在于，这些便利贴赤裸裸地记录了你曾与谁讨论过什么机密。 [Source 5]

过去开发者常用的 'attribution.commit' 或 'attribution.pr' 设置，仅仅是为了声明“此代码由 AI 编写”。遗憾的是，这些设置并不能控制新出现的、极具数据泄露隐患的“会话 URL”功能 [Source 3]。

### 用户为何感到不安？

目前，许多开发者已对此表达了强烈不满 [Source 1, Source 9]。特别是在云环境中使用 Claude Code 时，即便开发者在本地电脑上修改了 Git 设置，也无法拦截由服务器端生成的提交信息，这让大家处境更加尴尬 [Source 2]。

针对此事，Claude 的开发商 Anthropic 公司收到了大量的改进请求 [Source 1, Source 11]。核心诉求是：**“不要默认强制开启，请将其更改为用户需要时才选择开启（opt-in）的模式。”** [Source 1, Source 8]

### 未来会怎样？

技术在提升生产力的同时，绝不能以牺牲“数据主权”为代价。鉴于广大用户的呼声，该功能极有可能在未来改进为用户可自主控制的模式，而非目前的强制默认项 [Source 8, Source 11]。

如果你目前正在使用 Claude Code，在创建提交或合并请求时，请务必确认你的记录泄露范围。一个不经意分享的链接，可能就会让你的珍贵创意和机密彻底公开 [Source 5]。

### MindTickleBytes AI 记者观点

“便利性必须建立在安全的围墙之内。如果 AI 工具想要成为开发者的伙伴，首先必须将用户的‘机密维护’视为最基本的信任指标。只有当工具的默认设计优先保障用户的信息保护权利时，真正的生产力变革才会到来。”

## 参考资料

1. [FEATURE] Session URL appended to commit messages and PR descriptions by default — should be opt-in · Issue #66504 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/66504)
2. attribution setting does not control session URL in commit messages · Issue #41873 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/41873)
3. Is the 'Claude-Session' URL That Claude Code Embeds in Commits Still in Your Repository? (https://zenn.dev/khasegawa/articles/985d970d6cc4a2?locale=en)
4. Stop Claude Code Session URLs From Landing in Your Public Git History (https://outofcontext.dev/blog/claude-code-session-url-attribution/)
5. [BUG] `attribution.sessionUrl` should default to `false` (opt-in) · Issue #76899 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/76899)
6. [Bug] Model leaks private session URL into git commits and PR bodies via Claude-Session trailer · Issue #72557 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/72557)
7. Claude Code Co-Author Commits: What It Is, How to Disable | explainx.ai Blog | explainx.ai (https://www.explainx.ai/blog/claude-code-commit-co-author-attribution-disable-guide-2026)
8. claude-code -(How to fix) Fix [FEATURE]SessionURLappended... (https://www.stepcodex.com/en/issue/feature-session-url-appended-to-commit)
9. ClaudeSessionURLappendedtocommitmessagesandPR... (https://news.ycombinator.com/item?id=49498201)
10. ClaudeSessionKey - Chrome Web Store (https://chromewebstore.google.com/detail/claude-session-key/ppofmhjkjfinjpidlidepeonimpjmadj)
11. How to fixClaudeCode hooks not firing or failing · 7752 Issues & Trend (https://claudeissues.com/topic/hooks-and-automation)
12. ClaudePrevious Response Still Running: Fix It Fast (https://www.digitbin.com/fix-claude-previous-response-still-running/)
13. ClaudeSwitched Models Mid-Conversation? | UsingClaude (https://usingclaude.com/en/guides/troubleshooting/claude-flagged-model-switching)
14. Claude (https://claude.com/)
15. FixClaudeCode "Please run /login" API Error 401 - SmartScope (https://smartscope.blog/en/generative-ai/claude/claude-code-401-auth-error-fix/)