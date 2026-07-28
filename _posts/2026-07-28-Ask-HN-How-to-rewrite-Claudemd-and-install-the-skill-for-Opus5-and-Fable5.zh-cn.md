---
layout: post
title: "我的 AI 助手变聪明了？如何正确使用 Claude Opus 5 和 Fable 5"
description: "介绍如何升级到 Anthropic 的最新 AI 模型 Claude Opus 5 和 Fable 5，以及优化现有设置的技巧。"
summary: "随着 Anthropic 新 AI 模型的推出，本文指导如何优化现有的配置文件，并通过 Claude Code 的 /doctor 功能发挥新模型 100% 的性能。"
tags: [AI, Claude, Opus5, Fable5, 生产力]
image: 2026-07-28-Ask-HN-How-to-rewrite-Claudemd-and-install-the-skill-for-Opus5-and-Fable5.jpg
image_alt: "最新 AI 模型 Claude Opus 5 和 Fable 5 的标志并排摆放。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "技术的飞跃总是要求我们随之适应。不要被工具牵着鼻子走，通过优化设置，让 AI 成为你真正的节奏领跑者。"
quiz:
  - question: "建议使用什么指令来根据最新模型调整现有的 CLAUDE.md 文件？"
    choices: ["/update", "/doctor", "/optimize"]
    answer: 1
    explanation: "使用 Claude Code 提供的 /doctor 指令，可以针对新模型环境优化技能和 CLAUDE.md 文件。"
  - question: "以下哪项最能体现 Claude Fable 5 的特点？"
    choices: ["仅适用于简单对话的模型", "专为复杂长周期项目优化的模型", "专注于图像生成的模型"]
    answer: 1
    explanation: "Claude Fable 5 是一款“神话级 (Mythos-level)”模型，特别擅长主导复杂且需要长时间投入的项目，并能自动验证结果。"
  - question: "引入 Opus 5 和 Fable 5 时，应如何处理现有资源（CLAUDE.md、技能等）？"
    choices: ["直接使用即可", "需要根据最新模型进行更新", "应该删除"]
    answer: 1
    explanation: "旧模型的设置可能无法与最新模型完美兼容，因此需要根据最新的环境进行重新设置或优化。"
lang: zh-cn
ref: 2026-07-28-Ask-HN-How-to-rewrite-Claudemd-and-install-the-skill-for-Opus5-and-Fable5
---

想象一下，你每天使用的 AI 助手突然升级到了“超级计算机”级别的智能。然而，当你像往常一样下达指令时，它的反应却不如以前聪明了。这究竟是怎么回事？

Anthropic 最近推出的最新 AI 模型 **Claude Opus 5** 和 **Fable 5** 就属于这种情况。这是因为你精心为旧模型设定的“指导方针”，与新模型的思维方式存在些许差异。这就好比让一个已经变得极其聪明的学生去做“幼儿园级别的作业”。

### 为什么要更新？

AI 技术的发展不仅仅是模型智能数值的提升。过去，我们需要一步步给 AI 下达非常具体的指令，而现在，最新模型的自主思考和自我验证能力已经强大得多。[Claude Fable 5](https://www.anthropic.com/claude/fable) 专为执行复杂、长周期的项目而设计，能带来犹如与资深研究员合作般的惊人体验([Claude Fable 5](https://miniapps.ai/claude-5-fable))。

然而，我们为旧模型编写的配置文件（`CLAUDE.md`）或自定义技能可能并不完全兼容新模型的运行方式([来源: Ask HN](https://news.mcan.sh/item/49080135))。也就是说，如果不对设置进行更新，你的助手将无法发挥 100% 的潜力，会被困在过时的方针中，无法展现出应有的性能。

### 简单理解：驯服“高级助手”

把 AI 模型的配置文件想象成你交给助手的“工作手册”。如果旧手册是为了让你擅长“处理简单琐事”，那么新手册就需要更新，以便让它具备“战略决策”的能力。

- **打个比方**：这就好比你把 10 年前给实习生用的工作手册交给了现在的部门主管。主管想要着眼于大局并自主判断，但手册里却只写着“如何泡咖啡”这种细枝末节，这显然是不高效的。
- **设置优化**：Anthropic 建议修改指导方针，以便更好地利用新模型的特性，例如回复长度控制、自主拆解任务的能力等([来源: Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5))。

### 当前情况：如何开始？

首先要做的是寻求专家的帮助。如果你正在使用 Claude Code，尝试输入 `/doctor` 指令。该指令会检查你的系统是否已针对新模型环境进行了适当设置，并自动整理你的技能和 `CLAUDE.md` 文件，使其符合最新环境的要求([来源: The new rules of context engineering](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models))。

1. **更新设置**：根据最新模型的要求，简化并优化现有的 `CLAUDE.md` 和技能文件([来源: Anthropic Releases Claude Opus 5](https://www.ghacks.net/2026/07/27/anthropic-releases-claude-opus-5-at-half-the-token-price-of-claude-fable-5/))。
2. **选择模型**：在新的 Claude Code 会话中选择模型，并根据任务的复杂程度调整 effort（努力度）级别，从而优化性能([来源: Claude code update](https://thevibefather.com/blog/claude-code-opus-5-update-effort-guide))。

### 未来会怎样？

像 Claude Fable 5 这样的模型，未来将能够理解高达 100 万 token（AI 一次性能记住的信息单位——相当于几十本书的容量）的庞大上下文，并进化到能够自主编写代码并完成验证的水平([来源: Fable5AI](https://fable5.io/))。未来将开启一个不仅限于简单编码，而是与 AI 助手共同设计你的想法，并自动发现和解决复杂错误的时代。现在，你需要做的仅仅是将这位强大助手的“手册”更新到最新版本。

### MindTickleBytes AI 记者视点
技术跑得总是比我们想象中要快。比更换工具更重要的是，我们要改变使用工具的“提问方式”。用最新的设置唤醒 AI，去解决更大的难题吧。

## 参考资料
1. [Ask HN: How to rewrite `Claude.md` and install the skill for Opus5 and Fable5](https://news.mcan.sh/item/49080135)
2. [GitHub - DizzyMii/fable-skills: Six Claude Code skills](https://github.com/DizzyMii/fable-skills)
3. [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
4. [Prompting Claude Opus 5 - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
5. [Claude Opus 5 in Claude Code: A 2026 Guide - codersera.com](https://codersera.com/blog/claude-opus-5-claude-code-guide-2026/)
6. [Claude code update — Using Claude Opus 5 in Claude Code](https://thevibefather.com/blog/claude-code-opus-5-update-effort-guide)
7. [Writing Opus 5 / Fable 5 Prompts - GitHub](https://github.com/CodingCossack/writing-opus-5-fable-5-prompts)
8. [claude-skills/fable-mode/SKILL.md](https://github.com/henriquetell/claude-skills/blob/main/fable-mode/SKILL.md)
9. [GitHub - samirinyemi/fable5-skill-library](https://github.com/samirinyemi/fable5-skill-library)
10. [Hacker News | Ask HN](https://nilaykhandelwal.com/item/49080135)
11. [Claude Opus 5 Is Powerful. Your Setup Decides How Powerful](https://emergingai.substack.com/p/claude-opus-5-is-powerful-your-setup)
12. [Karpathy's CLAUDE.md Skills File: The Complete Guide](https://agentpedia.codes/blog/karpathy-claude-code-skills-guide)
13. [Migration guide - Claude Platform Docs](https://platform.claude.com/docs/en/about-claude/models/migration-guide)
14. [Claude](https://claude.com/)
15. [Claude Fable | Anthropic](https://www.anthropic.com/claude/fable)
16. [Fable5AI — Independent Model Guide & Prompt Workspace](https://fable5.io/)
17. [Claude Opus 5 review: great at coding (but I hate talking to it)](https://www.youtube.com/watch?v=dfre9hN0HCs)
18. [GitHub - alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
19. [Claude Fable 5 · Free AI Chatbot](https://miniapps.ai/claude-5-fable)
20. [Anthropic Releases Claude Opus 5 at Half the Token Price of Claude Fable 5 - gHacks TechNews](https://www.ghacks.net/2026/07/27/anthropic-releases-claude-opus-5-at-half-the-token-price-of-claude-fable-5/)