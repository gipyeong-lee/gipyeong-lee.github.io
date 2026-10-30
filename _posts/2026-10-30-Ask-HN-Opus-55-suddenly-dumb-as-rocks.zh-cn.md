---
layout: post
title: "AI 突然变笨了？Claude 3.5 新模型背后的真相"
description: "针对最新 AI 模型 Claude Opus 5.5 发布后被质疑性能下降的分析及其技术背景"
summary: "尽管 Claude Opus 5.5 发布后引发了部分用户关于性能下降的争议，但这很可能是 AI 新的通信方式与现有程序设计逻辑发生冲突所致。"
tags: [AI, Claude, Anthropic, 人工智能, 科技]
image: 2026-10-30-Ask-HN-Opus-55-suddenly-dumb-as-rocks.jpg
image_alt: "计算机屏幕上的 AI 标志与陷入思考的人影"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这看起来是新技术引入时产生的暂时性使用差距。模型本身的智能水平并未下降，而是 AI 与人类沟通的方式发生了变化，从而引发了混乱。"
quiz:
  - question: "Claude Opus 5.5 模型发布后，部分用户抱怨其“工作半途停止”的主要原因是什么？"
    choices: ["模型本身变得比以前更笨了", "新的通信方式与现有应用程序逻辑不匹配", "为了降低服务器成本而故意降低了性能"]
    answer: 1
    explanation: "由于模型被设计为比以前更频繁地通报进度，导致现有程序将此信号误认为是错误或作业结束。"
  - question: "与前代模型（Opus 5）相比，Claude Opus 5.5 的改进之处是什么？"
    choices: ["智能水平提升了 10 倍", "运行速度提升 30%，成本降低 40%", "引入了全新的图像编辑功能"]
    answer: 1
    explanation: "与前代模型相比，Opus 5.5 的运行速度快了 30%，成本降低了 40%。"
  - question: "当模型中断工作时，开发人员建议用户采取什么行动？"
    choices: ["立即卸载并重装模型", "输入“继续 (Continue)”等补充指令", "初始化模型设置"]
    answer: 1
    explanation: "模型中途停止可能是一种“通信”过程，通过输入继续指令，可以促使工作继续进行。"
lang: zh-cn
ref: 2026-10-30-Ask-HN-Opus-55-suddenly-dumb-as-rocks
---

想象一下：你那个平日里极其聪明、连复杂的编程难题都能迎刃而解的 AI 助手，某天突然在工作时停了下来，或者开始给出比平时更简短、更敷衍的回答。这就好像你那位曾被视为天才的朋友突然失忆了一样。

最近，在黑客新闻 (Hacker News) 和各类社交媒体上，Anthropic 于 2026 年 9 月 22 日发布的最新模型“Claude Opus 5.5”引发了类似的投诉浪潮。[参考资料 1](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/50238759), [参考资料 10](https://abz.global/technology/has-claude-opus-55-actually-been-nerfed-what-the-last-three-days-show), [参考资料 11](https://braindetox.kr/posts/claude_opus_5_5_release_2026.html)

## 为什么这个争议很重要？

AI 现在不仅是玩具，更是业务的核心工具。关于性能下降的争议可能只是心理作用，但实际使用的 AI 行为发生变化，确实会直接影响工作效率。关于回复变短或不遵循指令的报道显示，随着 AI 深入我们的生活，用户对模型一致性和可靠性的关注度变得异常敏感。[参考资料 10](https://abz.global/technology/has-claude-opus-55-actually-been-nerfed-what-the-last-three-days-show)

## 变得更聪明了，为什么看起来反而变笨了？

专家认为，Opus 5.5 的“新性格”是原因之一。

简而言之，如果说之前的 AI 模型在收到问题后只会给出标准答案，是一个“沉默的考生”，那么 Opus 5.5 则变成了一位“热心的课外辅导老师”，它在解题时会不断地说：“我现在正在进行第一步”，“现在切换到第二步”。[参考资料 3](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/), [参考资料 12](https://www.htx.com/news/opus-55-ditches-work-halfway-official-reveal-your-program-cl-Ph5pWWRy/)

由于模型在设计上更具通信导向性 (more communicative)，它开始将中间过程视为“进度更新 (progress updates)”来报告。问题出在这里：那些利用 AI 的现有程序（应用程序）在设计时，预期的是 AI 不吭声直接给出结果。当 AI 突然开始絮叨，程序就会误以为这是任务结束信号或感到混乱。也就是说，并不是 AI 变笨了，而是 AI 的沟通方式改变导致了与现有程序逻辑的“不匹配 (mismatch)”。[参考资料 12](https://www.htx.com/news/opus-55-ditches-work-halfway-official-reveal-your-program-cl-Ph5pWWRy/)

## 是否真的性能下降了？

当然，并非所有的不满都源于这种沟通方式的差异。查看实际测试员的反馈或基准测试追踪数据，确实存在一些关于回复变短或编程结果不如以前精确的反馈。[参考资料 10](https://abz.global/technology/has-claude-opus-55-actually-been-nerfed-what-the-last-three-days-show)

但从技术指标来看，Opus 5.5 确实非常强大。与前代 Opus 5 相比，其运行速度提高了 30%，每个 Token 的使用成本降低了 40%。专家评估认为，在处理复杂推理或编程任务时，该模型依然是市场上最强大的工具之一。[参考资料 5](https://hi-tech.mail.ru/news/156106-anthropic-vypustila-claude-opus-5-5/), [参考资料 11](https://braindetox.kr/posts/claude_opus_5_5_release_2026.html)

## 我们该如何应对？

Anthropic 似乎意识到了这次争议是由技术变革引起的暂时性现象。开发者社区现在正在分享实用的“使用技巧”，即当 AI 中途停止工作时，只需输入“继续 (Continue)”，它就能继续完成工作。[参考资料 12](https://www.htx.com/news/opus-55-ditches-work-halfway-official-reveal-your-program-cl-Ph5pWWRy/)

随着 AI 模型本身的进化，我们也需要逐步调整使用 AI 的方式（提示词的编写方式）。Anthropic 通过 Claude 官方博客建议，可以在 `CLAUDE.md` 等配置文件中预先明示“提问时和持续进行工作时的规则”，以防止 AI 自行中断工作。[参考资料 3](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)

## AI 的视角

当聪明的 AI 看起来突然变得笨拙时，我们首先要审视的不是技术的倒退，而是“沟通语言的变化”。人机之间的语言交流此刻正在进化，有时这种变化的速度甚至超过了我们所使用工具的发展速度。最终，如果我们能学会更好地理解和驯服 AI，Opus 5.5 将会成为比以往任何时候都更加高效的助手。

## 参考资料

1. [VueHN2.0 | HasOpus5.5gottendumberfor anyone else in the last...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/50238759)
2. [ClaudeOpus5.5- API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/anthropic/claude-opus-5.5)
3. [Getting the most out ofOpus5.5in Claude and... / claude.dev Blog](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)
4. [ClaudeOpus5.5· Бесплатный чат-бот ИИ](https://miniapps.ai/ru/claude-opus-5-5)
5. [ClaudeOpus5.5: характеристики, цена, отличия отOpus5и Fable...](https://hi-tech.mail.ru/news/156106-anthropic-vypustila-claude-opus-5-5/)
6. [Питер Янг собрал свой аттракцион сOpus5.5: 30... - vibecoding.ru](https://vibecoding.ru/news/2026/09/23/opus-55-virtual-ride)
7. [A Week After Launch, Paying Users Say Opus 5.5 Got Worse ...](https://admix.software/blog/claude-opus-5-5-nerf-reports)
8. [Opus 5.5 may be getting quietly worse · 58 HN comments | Zeli](https://zeli.app/story/49901736)
9. [Why Opus 5 Feels Worse: RLVR Theory Explained (2026 ...](https://www.explainx.ai/blog/why-claude-opus-5-feels-worse-to-work-with-august-2026)
10. [Has Claude Opus 5.5 Actually Been Nerfed? What the Last Three ...](https://abz.global/technology/has-claude-opus-55-actually-been-nerfed-what-the-last-three-days-show)
11. [Claude Opus 5.5 출시 — 토큰 가격 인하와 벤치마크 지표로 본 성능 ...](https://braindetox.kr/posts/claude_opus_5_5_release_2026.html)
12. [Opus 5.5 Ditches Work Halfway? Official Reveal: Your Program ...](https://www.htx.com/news/opus-55-ditches-work-halfway-official-reveal-your-program-cl-Ph5pWWRy/)
13. [Claude's Game Recompilation Capabilities May Have Been Nerfed](https://kotaku.com/claudes-reverse-engineering-capabilities-used-to-recompile-games-may-have-been-quietly-nerfed-2000749320)