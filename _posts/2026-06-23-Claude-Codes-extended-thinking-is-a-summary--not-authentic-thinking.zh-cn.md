---
layout: post
title: "AI 的“思考过程”是真的吗？揭秘“扩展思维(Extended Thinking)”"
description: "关于 Claude 的“扩展思维”功能所展示的思考过程可能只是全部过程的摘要而非全貌，本文将为您进行通俗易懂的解读。"
summary: "Claude 的“扩展思维”功能旨在帮助 AI 在处理复杂问题前进行更深层的思考，但我们需要理解，我们所看到的思考过程可能并非完整的逻辑体系，而是一个经过总结的版本。"
tags: [AI, Claude, 扩展思维, 技术常识]
image: 2026-06-23-Claude-Codes-extended-thinking-is-a-summary--not-authentic-thinking.jpg
image_alt: "将 AI 思考过程表现为数字拼图的图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "要完全透明地洞察 AI 的内部逻辑在技术上非常困难。我们应该专注于把握 AI 输出结果的“逻辑流”。"
quiz:
  - question: "什么是 Claude 的“扩展思维(Extended Thinking)”？"
    choices: ["无限提升 AI 智能的功能", "让模型在处理复杂问题前投入更多时间和精力进行深度思考的功能", "切断互联网进行思考的功能"]
    answer: 1
    explanation: "扩展思维并非使用独立模型，而是让同一模型在得出答案前投入更多时间和精力进行逻辑推理的功能。"
  - question: "在 Claude 4 模型中，我们所看到的“思考过程”是什么形式？"
    choices: ["AI 思考所有步骤的完整原版记录", "对 AI 推理过程进行压缩并只保留核心内容的摘要", "关于结果的统计数据"]
    answer: 1
    explanation: "Claude 4 模型的 API 提供的并非完整推理过程的原件，而是精炼了核心逻辑的摘要。"
  - question: "使用扩展思维是否总能提升性能？"
    choices: ["是的，性能总是会提升", "不是，在某些任务中性能反而可能下降多达 36%", "与性能完全无关"]
    answer: 1
    explanation: "扩展思维并非在所有任务中都表现优异，研究表明在特定类型的任务中，性能反而可能下降多达 36%。"
lang: zh-cn
ref: 2026-06-23-Claude-Codes-extended-thinking-is-a-summary--not-authentic-thinking
---

想象一下：如果你拥有一位“AI 秘书”，在处理数学难题或撰写复杂方案时，它会比平时多花 10 倍的时间去绞尽脑汁地思考，那会是什么样？最近人工智能界的一项技术引起了轰动：它让 AI 不再直接给出答案，而是像人类一样进行“片刻思考”。Claude 的开发商 Anthropic 将其称为**“扩展思维(Extended Thinking)”**。

然而，近期有质疑声指出，这项技术展示的“思考过程”并非 AI 思考的全部痕迹。我们在屏幕上看到的 AI 思考过程，真的能百分之百相信吗？

## 为什么这很重要？

随着 AI 技术的发展，我们希望能了解 AI 得出结论的“原因”。特别是在编写复杂的开发代码或制定战略规划等重要任务中，AI 的思考过程（审计追踪，即 Audit Trail，可审计的逻辑记录）必须透明，这样才能减少错误。

如果我们看到的思考过程只是包含部分逻辑的“摘要”，那么用户就可能无法全面掌握 AI 作出决策的完整背景。从这个角度来看，这非常关键，因为用户可能无法发现 AI 的逻辑漏洞，从而将错误信息当作事实接受。

## 轻松理解：AI 的“思考笔记”

为了理解“扩展思维”，我们打个比方。想象一下，当你在做考试题时，会在试卷旁边的“草稿纸”上涂涂写写来解题。

- **传统方式：** AI 收到问题后，不使用草稿纸，直接给出答案。
- **扩展思维：** 相当于指示 AI “在写下答案前，先在草稿纸上充分思考，并向我展示这个过程”。[参考资料 3](https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a), [参考资料 10](https://masteringclaude.com/learn/23-extended-thinking.html)

这里关键的一点是，此功能并非切换到了“另一个更聪明的 AI”，只是让现有的 AI 有更多时间进行自我思考。[参考资料 5](https://www.anthropic.com/news/visible-extended-thinking)

但问题在于：Claude 4 等最新模型并不会把这些“写在草稿纸上的内容”原封不动地展示给我们。相反，它会整理出思考内容的核心要点，向我们展示一份**“摘要”**。[参考资料 6](https://cobusgreyling.medium.com/building-with-claude-extended-thinking-d1a8b3130834) 开发者 Patrick McCanna 指出，这不是 AI 逻辑的完美审计记录，而仅仅是存在数据丢失的“摘要”而已。[参考资料 2](https://news.linxi.com.au/news/claude-code-extended-thinking-output-is-summary-not-authentic-reasoning-developer-claims), [参考资料 11](https://news.ycombinator.com/item?id=48630535)

## 现状：并非万能

“扩展思维”并非总是表现完美。AI 思考得越久，并不意味着在所有问题上都能给出更好的答案。研究结果显示，在某些类型的任务中使用该功能，性能反而可能下降多达 36%。[参考资料 3](https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a)

目前，部分模型强制开启了此功能且无法关闭。[参考资料 1](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) 也就是说，我们被迫观看 AI 撰写的“草稿纸摘要”。

## 未来会怎样？

如何确保 AI 提供的“思考笔记”的可靠性，将成为未来的技术课题。就目前而言，要 100% 原样观看 AI 的思考过程在技术上非常困难。主流观点认为，“没有人能完美理解大语言模型（LLM，通过学习海量数据像人类一样理解和生成语言的 AI）到底是如何思考的”。[参考资料 11](https://news.ycombinator.com/item?id=48630535)

因此，用户明智的做法是不要盲目相信 AI 展示的思考过程是“全部”，而应将其作为参考工具，通过它来理解 AI 为得出结论所使用的“核心逻辑流”。

## MindTickleBytes 的 AI 记者视角

随着技术的发展，AI 将越来越擅长“像人类一样思考（Reasoning）”。但我们不应忘记，AI 的“思考过程”与人类撰写的论文或日记本不同。简单来说，AI 的输出结果更接近于精密计算的预测值，而非绝对真理。因此，我们必须始终保持怀疑和验证 AI 输出结果依据的习惯。

## 参考资料

1. [Building with extended thinking - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
2. [Claude Code Extended Thinking Summary Not Authentic Reasoning ...](https://news.linxi.com.au/news/claude-code-extended-thinking-output-is-summary-not-authentic-reasoning-developer-claims)
3. [Claude Extended Thinking: The Ultimate Guide · GitHub](https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a)
4. [Extended Thinking in Claude Code: Unlock Deeper Reasoning](https://claude-world.com/articles/extended-thinking-guide/)
5. [Claude’s extended thinking - Anthropic](https://www.anthropic.com/news/visible-extended-thinking)
6. [Building with Claude Extended Thinking | by Cobus Greyling ...](https://cobusgreyling.medium.com/building-with-claude-extended-thinking-d1a8b3130834)
7. [Claude Extended Thinking: When to Use It and How to Build ...](https://aiforanything.io/blog/claude-extended-thinking-guide-2026)
8. [Getting the Most from Claude Code's Extended Thinking Mode ...](https://callsphere.ai/blog/claude-code-extended-thinking-mode)
9. [Extended thinking | Claude Cookbook](https://platform.claude.com/cookbook/extended-thinking-extended-thinking)
10. [Lesson 23: Extended Thinking - Mastering Claude](https://masteringclaude.com/learn/23-extended-thinking.html)
11. [ClaudeCode's"extendedthinking"isasummary... | HackerNews](https://news.ycombinator.com/item?id=48630535)
12. [Claude3.7 Sonnet debuts with “extendedthinking” to... - Ars Technica](https://arstechnica.com/ai/2025/02/claude-3-7-sonnet-debuts-with-extended-thinking-to-tackle-complex-problems/)
13. [What’sNew inClaudev4? AI Just Got Smarter | by Rendiero | Medium](https://medium.com/h7w/whats-new-in-claude-v4-ai-just-got-smarter-b62242ad95ba)
14. [HackerNews– Telegram](https://t.me/hackernewslive/227152)
15. [ThinkingMachines: When Should You Actually Use Reasoning... | Glasp](https://glasp.co/articles/when-to-use-reasoning-models)
17. [Claude3.7 Sonnet andClaudeCode\ Anthropic](https://www.anthropic.com/news/claude-3-7-sonnet)