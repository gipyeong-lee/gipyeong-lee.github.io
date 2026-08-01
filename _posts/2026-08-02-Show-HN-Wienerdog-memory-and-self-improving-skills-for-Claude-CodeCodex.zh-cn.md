---
layout: post
title: "AI 编程助手如何告别“健忘症”：Wienerdog 的故事"
description: "AI 编程助手总是重复同样的错误，它们能拥有记忆力吗？通过 Wienerdog 了解 AI 的自我改进技术。"
summary: "Wienerdog 是一种外部内存层技术，它帮助 Claude Code 或 Codex 等 AI 编程助手不再在每次会话中丢失记忆，从而能够通过过去的经验进行自主学习。"
tags: [AI, 编程, 生产力, Wienerdog, ClaudeCode]
image: 2026-08-02-Show-HN-Wienerdog-memory-and-self-improving-skills-for-Claude-CodeCodex.jpg
image_alt: "计算机屏幕中，AI 编程助手参考过去的学习记录并更高效地工作的形象化图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的真正成长不仅在于提高模型本身的智能，更在于如何系统地记忆和利用与用户的交互经验。"
quiz:
  - question: "Wienerdog 等 AI 内存技术的核心运作方式是什么？"
    choices: ["重新训练 AI 模型的内部权重", "通过读写外部文件记录经验", "删除并重新安装 AI 模型"]
    answer: 1
    explanation: "Wienerdog 不会修改模型内部，而是通过 Learnings.md 等外部内存文件在不同会话间共享经验。"
  - question: "关于 AI 自我学习方式的描述，正确的是？"
    choices: ["直接修改 AI 模型的大脑", "只能通过传统的微调（fine-tuning）实现", "在任务完成后提取经验并保存为知识"]
    answer: 2
    explanation: "Wienerdog 利用了一种自我改进循环，在任务结束后提取有效信息，并将其保存为可重用的知识。"
  - question: "AI 编程助手面临的顽疾是什么？"
    choices: ["因为记忆太多而变慢", "一旦会话结束就会忘记所有事情", "无法回答用户的问题"]
    answer: 1
    explanation: "许多编程智能体是以会话为单位运行的，存在着忘记上一会话学习内容的“健忘症”问题。"
lang: zh-cn
ref: 2026-08-02-Show-HN-Wienerdog-memory-and-self-improving-skills-for-Claude-CodeCodex
---

想象一下，你聘请了一位非常有能力的编程助手，但这位助手每天早上都会问你：“你好，请问你是谁？”如果每天都要把昨天的工作内容重新解释一遍，那么聘请助手也就失去了意义，生产力也会大幅下降。令人惊讶的是，目前我们使用的大多数 AI 编程助手都患有类似的“健忘症”。因为在对话结束、会话关闭的那一刻，AI 就会把之前的经验从脑海中彻底抹去。

最近在开发者社区引起广泛关注的 **Wienerdog** 是一项旨在治愈 AI 这种致命健忘症的创新技术。如果打个比方，这项技术就像是 AI 的“工作交接笔记”，能够帮助 AI 自主提升编程能力。

## 为什么这很重要？

对于普通用户来说，AI 的记忆力不仅意味着方便，更直接关系到工作效率。如果 AI 记得昨天在调试过程中学到了什么，那么明天它就不会再犯同样的错误。像 Wienerdog 这样的技术并非那种改动模型本身的宏大且具有风险的方法。通过让 AI 像人类一样编写“工作日志”并将其应用于下一次工作，它可以显著提升编程助手的完整度。 [Source 3](https://news.ycombinator.com/item?id=46426624), [Source 15](https://modernorange.io/item/49134381)

## 浅显易懂的解释

用一个更简单的比喻，Wienerdog 就像是我们为准备重要考试而制作的**“错题集”**。

假设 AI 在编程过程中犯了错，或者找到了一个非常高效的解决模式。此时，AI 不会费力地试图把这些经验硬塞进它的大脑（模型）里，而是会将它们仔细记录在像“Learnings.md”这样的外部内存文件中。 [Source 4](https://www.mindstudio.ai/blog/self-improving-ai-skills-claude-code), [Source 5](https://www.mindstudio.ai/blog/self-learning-claude-code-skill-learnings-md)

下次 AI 开始编程时，它首先会翻阅这本笔记。这就像上班后先查看昨天留下的交接文档一样。它选择了一种明智的策略：不是进行那种复杂且具有风险的“微调（Fine-tuning）”手术（即改变决定 AI 智能的内部大脑结构——权重），而是在手边放一个小记事本，从而变得更加聪明。 [Source 4](https://www.mindstudio.ai/blog/self-improving-ai-skills-claude-code)

该系统通过以下循环结构运行：
1. **执行任务**：AI 解决给定的编程任务。
2. **提取知识**：工作结束后，提取哪些方法有效，或者存在哪些错误。 [Source 6](https://claudemarketplaces.com/skills/charon-fan/agent-playbook/self-improving-agent), [Source 7](https://github.com/UniM0cha/claude-self-improving-skills)
3. **保存知识**：将提取出的经验保存到外部内存文件中。 [Source 4](https://www.mindstudio.ai/blog/self-improving-ai-skills-claude-code)
4. **下一会话应用**：在开始下一次任务时，读取保存的笔记并将其应用于编程风格。 [Source 5](https://www.mindstudio.ai/blog/self-learning-claude-code-skill-learnings-md)

## 当前现状

目前，像 Wienerdog 这样的内存层已经可以在 Claude Code 和 Codex 等环境中使用。开发者无需复杂的安装过程，只需添加简单的脚本，就可以为自己的 AI 助手赋予这种“记忆力”。社区已经共享了超过 16 万个技能，全世界许多开发者都在致力于提高 AI 的自我改进能力。 [Source 18](https://claudskills.com/)

不过，需要记住的是，这项技术并不是像通用人工智能（AGI，拥有与人类相等或更高智能的 AI）那样的魔法工具。Wienerdog 仅仅是一个能够系统化管理工作过程中所获信息的实用工具。 [Source 3](https://news.ycombinator.com/item?id=46426624)

## 未来会怎样？

未来，AI 编程工具将超越仅仅回答问题的水平，发展到能够记忆整个项目的背景信息和开发者独特的编程风格。当你对它说“用和我昨天写的函数类似的风格编写代码”时，AI 真的能想起那些规则并执行的时代已经不远了。那个 AI 助手成为我们共同成长、协同工作的同事的日子正在临近。

## MindTickleBytes AI 记者观点
AI 的真正成长不仅在于提高模型本身的智能，更在于如何系统地记忆和利用与用户的交互经验。我们已经走过了仅仅使用高性能 AI 的时代，现在进入了亲自“调教”并培养具有专属记忆力 AI 的时代。

## 参考资料
1. [Full Tutorial: Build Self-Improving Claude Skills in 20 Min (Eval + Memory)](https://creatoreconomy.so/p/full-tutorial-build-self-improving-claude-skills-in-20-min)
2. [Self-Improving Agent — Agent Skill & Codex Plugin - Claude Code Skills & Agent Plugins](https://alirezarezvani.github.io/claude-skills/skills/engineering-team/self-improving-agent/)
3. [Show HN: Stop Claude Code from forgetting everything | Hacker News](https://news.ycombinator.com/item?id=46426624)
4. [How to Build Self-Improving AI Skills in Claude Code | MindStudio](https://www.mindstudio.ai/blog/self-improving-ai-skills-claude-code)
5. [How to Build a Self-Learning Claude Code Skill with a Learnings.md File | MindStudio](https://www.mindstudio.ai/blog/self-learning-claude-code-skill-learnings-md)
6. [Self Improving Agent - Skills - Claude Code Marketplaces](https://claudemarketplaces.com/skills/charon-fan/agent-playbook/self-improving-agent)
7. [GitHub - UniM0cha/claude-self-improving-skills: Hermes Agent-style self-improvement for Claude Code · GitHub](https://github.com/UniM0cha/claude-self-improving-skills)
8. [ShowHN:Wienerdog–memoryandself-improvingskillsfor...](https://modernorange.io/item/49134381)
15. [ShowHN:Wienerdog–memoryandself-improving... | HackerNews](https://news.ycombinator.com/item?id=49134381)
16. [nextjs-hackernews.vercel.app/item/49134381](https://nextjs-hackernews.vercel.app/item/49134381)
18. [ClaudeSkills·ClaudeCodeSkillsCatalog | ClaudSkills](https://claudskills.com/)