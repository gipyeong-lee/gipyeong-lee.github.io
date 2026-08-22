---
layout: post
title: "我的 AI 突然变笨了？Claude Code 的隐藏实验故事"
description: "你是否曾感到 AI 模型性能突然下降？通过 Anthropic 在 Claude Code 中进行的“努力程度”调整及用户的不佳体验，我们来探讨 AI 透明度问题。"
summary: "为了削减成本和提高响应速度，Anthropic 秘密调低了 Claude Code 的默认推理强度，在用户对质量下降的抱怨声中，最终恢复了设置。"
tags: [AI, Anthropic, ClaudeCode, 人工智能, 技术伦理]
image: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code.jpg
image_alt: "Claude Code 界面及表示推理过程的图形元素"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企业在进行技术优化时，应透明公开变更原因，以维护与用户的信任。实验性功能应当始终优先保障用户的选择权。"
quiz:
  - question: "Anthropic 下调 Claude Code 默认推理水平的主要原因是什么？"
    choices: ["增强模型安全性", "削减成本并提高响应速度", "为了学习更多数据"]
    answer: 1
    explanation: "Anthropic 为了响应用户关于 Token 消耗过多的反馈，试图提高响应速度并降低 Token 消耗。"
  - question: "在 Claude Code 中，“努力程度 (effort level)”越高，会发生什么？"
    choices: ["响应速度更快", "思维深度更深，更擅长解决复杂问题", "产生的费用必然更高"]
    answer: 1
    explanation: "努力程度与思维深度相关，能够提升解决复杂问题的能力。"
  - question: "Anthropic 是如何解决近期发生的质量下降问题的？"
    choices: ["向用户收取更高费用", "于 4 月 7 日恢复到之前的水平", "完全更换了 AI 模型"]
    answer: 1
    explanation: "Anthropic 承认该措施是一个错误的权衡，并于 2026 年 4 月 7 日将设置恢复至原本较高的推理水平。"
lang: zh-cn
ref: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code
---

想象一下，你有一位每天都在协助你工作的聪明 AI 助手。如果这位直到昨天还能轻松解决复杂编程问题的助手，今天早上突然开始只给出极其简单的回答，或者遗漏了关键上下文，你会有多惊慌？最近，人工智能公司 Anthropic 的开发工具“Claude Code”的用户群体中，就发生了这样的事情。

### 为什么这很重要？

这起事件对将 AI 作为专业工具的用户来说是一个巨大的打击。这不仅仅是模型变慢的问题，而是用户的 AI “大脑运行方式”在不知情的情况下被强制改变，导致工作效率直接受损。这向我们揭示了一个重要事实：我们每天使用的 AI 服务，可能随时会因为企业的内部政策而发生性能波动，且事先没有任何预警。

### 易懂解释：什么是 AI 的“努力程度”？

Claude Code 有一个功能，叫做**“努力程度 (Effort Level，即决定 AI 为解决问题而进行深度思考程度的设置)”**。

简单来说，这个努力程度就像学生答题时投入的精力。“低努力”水平相当于粗略扫一眼题目就匆忙写下答案，“高努力”水平则意味着逐字细读、审题并进行深入思考。 [来源: Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)

打个比方，这就好比一位资深厨师一直在精心烹饪，却突然为了节省食材费和时间而改为快餐式烹饪。作为消费者，自然能感觉到口味的差异。

2026 年 2 月至 3 月期间，Anthropic 在没有任何通知的情况下，将 Claude Code 的默认努力程度从“高”下调至“中”。 [来源: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/) Anthropic 相关人士解释称，这是为了响应用户关于 Token（AI 语言单位）消耗过多的反馈，旨在改善响应速度并削减成本。 [来源: Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)

然而结果是惨痛的。这次调整导致 AI 的思考深度大幅削减了 73%，正在进行复杂编程工作的用户明显感知到了性能的急剧下滑。 [来源: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)

### 当前现状：连番更新带来的混乱

调查显示，性能下降的原因是三次重大更新叠加所致。 [来源: Anthropic Claude Code Quality Drop](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026) 特别是在 3 月份，针对部分用户进行了 A/B 测试（随机展示不同方案以比较效果），在此过程中出现了诸如将代码计划限制在 40 行以内、或删除必要上下文信息等问题，招致了用户的强烈反弹。 [来源: Anthropic A/B Tested Claude Code Plan Mode](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)

最终，Anthropic 承认其决策是一个“错误的权衡”，并于 4 月 7 日将设置恢复到了之前的水平。 [来源: Why Is Claude Code Slow?](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)

### 未来会怎样？

这次事件为 AI 工具的透明度敲响了警钟。专家认为，提供专业 AI 工具的企业在应用实验性变更时，必须征得用户同意，或至少提前发布公告。 [来源: Mike Ramos Criticizes Anthropic](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code) 未来，用户将更强烈地要求拥有能够自行选择和调节 AI 模型“努力程度”的环境。

## MindTickleBytes 的 AI 记者视角

AI 的性能不仅是冷冰冰的数字，更直接关系到用户的信任。此次以“技术优化”之名进行的“悄然变更”引发了如此巨大的生产力损失，充分说明了 AI 企业为何必须将透明沟通放在首位。随着越来越多的用户将 AI 作为核心工作工具，这种政策透明度将与技术实力一样，成为衡量企业竞争力的关键指标。

## 参考资料

1. [Claude Code's Thinking Depth Dropped 73% — Anthropic Admits](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)
2. [Anthropic appears to be A/B testing reduced effort levels in Claude Code](https://zeli.app/zh/story/49401549)
3. [Anthropic Claude Code Quality Drop: What Actually Happened](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026)
4. [Claude Code's Feb–Mar 2026 Updates Quietly Broke Complex Engineering](https://dev.to/shuicici/claude-codes-feb-mar-2026-updates-quietly-broke-complex-engineering-heres-the-technical-5b4h)
5. [Anthropic A/B Tested Claude Code Plan Mode Without Telling Users](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)
6. [An update on recent Claude Code quality reports \ Anthropic](https://www.anthropic.com/engineering/april-23-postmortem)
7. [Mike Ramos Criticizes Anthropic for Undisclosed A/B Test](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code)
8. [Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
9. [Why Is Claude Code Slow? Official Causes and Developer Fixes](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)
10. [Anthropic admits it dumbed down Claude with 'upgrades'](https://www.theregister.com/software/2026/04/24/anthropic-admits-it-dumbed-down-claude-with-upgrades/5228105)
11. [Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)
12. [Mystery solved: Anthropic reveals changes to Claude's harnesses](https://venturebeat.com/technology/mystery-solved-anthropic-reveals-changes-to-claudes-harnesses-and-operating-instructions-likely-caused-degradation)
13. [Anthropic is facing a wave of user backlash over reports of performance issues](https://finance.yahoo.com/sectors/technology/articles/anthropic-facing-wave-user-backlash-091348318.html)
14. [Anthropic explains Claude Code’s recent performance](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?ref=biztoc.com)