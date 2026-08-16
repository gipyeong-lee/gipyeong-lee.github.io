---
layout: post
title: "AI 编程助手，现在可以换成“国产模型”了吗？Kimi K3 与 Claude Code 的邂逅"
description: "我们探讨了如何将近期发布的强大 AI 模型“Kimi K3”连接到流行的编码代理“Claude Code”中使用，并分析了其性能表现。"
summary: "深入探究如何将拥有 2.8 万亿参数的强大 AI 模型“Kimi K3”应用于 Claude Code 环境及其效率优势。"
tags: [AI, 编程, KimiK3, ClaudeCode, 技术评测]
image: 2026-08-17-Testing-Moonshot-AIs-Kimi-K3-Inside-Claude-Code.jpg
image_alt: "想象中 Kimi K3 模型被连接到编码代理界面，正在生成复杂网页代码的图像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Kimi K3 的出现表明，开放权重模型在性能和成本方面已足以对专有模型构成实质性威胁。随着现在可以自主选择代理的“大脑”，开发者的效率将得到进一步的极大提升。"
quiz:
  - question: "作为 Kimi K3 模型最大特征之一介绍的规模大约是多少？"
    choices: ["1000 亿参数", "2.8 万亿参数", "5 万亿参数"]
    answer: 1
    explanation: "Kimi K3 是一款拥有 2.8 万亿参数的大规模模型。"
  - question: "在 Claude Code 等环境中要使用 Kimi K3，最关键的操作是什么？"
    choices: ["完全重新安装 Claude Code", "设置模型的基础 URL 和 API 密钥", "更换计算机硬件"]
    answer: 1
    explanation: "只需将 Claude Code 的 Anthropic 基础 URL 更改为 Moonshot 的兼容端点并设置 API 密钥即可完成连接。"
  - question: "人工智能评估机构“Artificial Analysis”的智能指数测评中，Kimi K3 获得了多少分？"
    choices: ["50 分", "56 分", "57 分"]
    answer: 2
    explanation: "在 Artificial Analysis 的测评中，Kimi K3 获得了 57 分，超过了 Claude Opus 4.8 的 56 分。"
lang: zh-cn
ref: 2026-08-17-Testing-Moonshot-AIs-Kimi-K3-Inside-Claude-Code
---

想象一下：你平时顺手使用的“AI 编程助手”，性能变得更强，而成本却降到了原来的三分之一，那会是什么体验？最近，开发者社区中出现了一个热门话题，那就是中国月之暗面（Moonshot AI）发布的“Kimi K3”。

该模型不仅被评价为极其智能，甚至与此前几乎垄断 AI 市场的全球科技巨头代表作平起平坐，在某些性能指标上甚至有所超越，备受瞩目。今天，我们就来探讨如何将这个拥有“2.8 万亿参数的怪兽” Kimi K3 连接到我们熟悉的编码代理“Claude Code”中使用。

## 为什么这很重要？

以往，AI 模型就像是“紧闭的大门”。某家公司开发出的模型，通常只能在该公司提供的服务范围内使用。但 Kimi K3 是一款“开放权重（Open-Weight，即任何人都可以查看并利用模型内部设置的状态）”模型。这意味着用户可以根据自己的工作流，自由地更换 AI 的“大脑”。

特别是编程工作，成本高昂。因为完成一个项目往往需要进行无数次 AI 调用。使用 Kimi K3，不仅能提供与 Claude 相当的性能，成本还能控制在原来的 35% 左右，具有极大的经济吸引力。[出处: Moonshot AI's Kimi-K3 tops Frontend Code Arena · Digg](https://digg.com/tech/hm2wuequ)

## 浅显易懂：AI 的“大脑”与“司机”

把编码代理比作汽车，会怎样？“Claude Code”就像是具备了方向盘、踏板和导航系统的“车本身”。而我们使用的 AI 模型（Claude 或 Kimi K3）则是驱动这辆车运行的“引擎”和“司机”。

很多人担心：“要用 Kimi K3，是不是得重新编写程序？”答案是否定的。即便引擎（Kimi K3）变了，方向盘（Claude Code）依然可以继续使用。我们只需更换引擎，就能体验到更快、更省钱的驾驶过程。[出处: Kimi K3 vs Claude Code vs Codex 2026 · senn-tech](https://senn-tech.com/en/blog/kimi-k3-vs-claude-code-codex)

## 现状：“3T 级”超大模型登场

2026 年 7 月 16 日，月之暗面发布了 Kimi K3，该模型拥有 2.8 万亿个参数（Parameter，即 AI 通过学习调整的数值）。[出处: I Ran Kimi K3 Against Claude for a Week · Medium](https://medium.com/@inprogrammer/i-ran-kimi-k3-against-claude-for-a-week-here-is-what-actually-happened-20c1a17c9206) 这是行业内所谓“3T（万亿）级”模型中规模巨大的存在。

性能也不容小觑。在独立 AI 评估机构“Artificial Analysis”的智能指数（Intelligence Index）测量中，Kimi K3 获得了 57 分，超越了当时处于领先地位的 Claude Opus 4.8 的 56 分。[出处: Kimi K3 Beats Opus 4.8 in Blind Coding Test · Adwait | LinkedIn](https://www.linkedin.com/posts/adwait-gawade_moonshot-ai-releases-kimi-k3-a-28-trillion-parameter-activity-7485215773880139776-6lEv)

目前 Kimi K3 具备以下特征：
* **海量上下文**：一次性可记忆 100 万个 Token（Token，即 AI 理解的文本片段单位）。[出处: Kimi K3: Moonshot AI's 2.8T Open-Weight Model](https://www.eigent.ai/blog/kimi-k3-open-weight-frontier-model)
* **API 性价比**：提供了 3 美元和 15 美元等级的合理价格政策。[出处: Kimi K3: Moonshot AI's 2.8T Open-Weight Model](https://www.eigent.ai/blog/kimi-k3-open-weight-frontier-model)
* **便捷连接**：只需略微修改 Claude Code 设置即可立即更换。[出处: How to Run Kimi K3 in Claude Code: 3 Routes, Real Costs, and...](https://shaam.blog/articles/how-to-run-kimi-k3-in-claude-code-2026)

## 在 Claude Code 中使用 Kimi K3

方法出奇地简单。利用 Claude Code 与 Anthropic API 通信的方式，将其指向 Moonshot AI 提供的兼容端点即可。[出处: Kimi K3 with Claude Code: Setup, Env Vars and Real Limits (2026)](https://www.codeagentswarm.com/en/guides/kimi-k3-with-claude-code)

1. **设置端点**：将 Claude Code 的 Anthropic 基础 URL 设置更改为 Moonshot AI 提供的兼容端点地址。[出处: Kimi vs Claude Code: Coding Agent Comparison 2026](https://www.layer3labs.io/comparisons/kimi-k3-vs-claude-code)
2. **更换 API 密钥**：输入 Moonshot AI 的 API 密钥，代替原有的 Anthropic API 密钥。[出处: Kimi vs Claude Code: Coding Agent Comparison 2026](https://www.layer3labs.io/comparisons/kimi-k3-vs-claude-code)
3. **确认**：无需任何复杂的构建过程或程序安装，直接运行 Claude Code，Kimi K3 就会开始执行编码任务。[出处: How to Run Kimi K3 in Claude Code: 3 Routes, Real Costs, and...](https://shaam.blog/articles/how-to-run-kimi-k3-in-claude-code-2026)

## 未来展望

Kimi K3 的出现展示了 AI 领域中“基准分数”变化的速度有多快。仅发布 9 天，基准排名就发生了多次反转，技术进步的速度极快。[出处: Kimi K3 vs Claude for Coding 2026: Benchmarks Compared](https://aiforesight360.com/kimi-k3-vs-claude-coding/)

未来，我们在选择 AI 模型时，考虑的重点将不再是“谁的服务”，而是“哪种引擎对我的项目更高效”。目前它已在编程和网页开发领域证明了性能，随着这些技术进一步完善，我们终将迎来在普通文档写作或策划工作中也能挑选自己“心仪 AI 引擎”的时代。

## MindTickleBytes AI 记者视角
技术竞争最终会带给我们用户更智能、更便宜的工具。像 Kimi K3 这样的模型出现，充分说明特定企业无法垄断 AI 技术。未来，为了获得最佳成果，开发者将像运动员挑选运动鞋一样，根据不同需求选择最适合的模型。

## 参考资料

1. [Testing Moonshot AI's Kimi K3 Inside Claude Code](https://philippdubach.com/posts/kimi-k3-inside-claude-code/)
2. [How to Run Kimi K3 in Claude Code: 3 Routes, Real Costs, and...](https://shaam.blog/articles/how-to-run-kimi-k3-in-claude-code-2026)
3. [Testing Moonshot AI's Kimi K3 Inside Claude Code | Hacker News](https://news.ycombinator.com/item?id=49319610)
4. [Moonshot AI's Kimi-K3 tops Frontend Code Arena · Digg](https://digg.com/tech/hm2wuequ)
5. [China's Kimi K3 Calls Itself Claude, Exposing Illegal Distillation](https://propakistani.pk/2026/07/18/chinas-kimi-k3-calls-itself-claude-exposing-illegal-distillation/)
6. [Kimi K3 Beats Opus 4.8 in Blind Coding Test | Adwait... | LinkedIn](https://www.linkedin.com/posts/adwait-gawade_moonshot-ai-releases-kimi-k3-a-28-trillion-parameter-activity-7485215773880139776-6lEv)
7. [moonshotai/Kimi-K3 · Hugging Face](https://huggingface.co/moonshotai/Kimi-K3)
8. [I Ran Kimi K3 Against Claude for a Week. Here Is ... - Medium](https://medium.com/@inprogrammer/i-ran-kimi-k3-against-claude-for-a-week-here-is-what-actually-happened-20c1a17c9206)
9. [Kimi K3 vs Claude Code vs Codex 2026 · senn-tech](https://senn-tech.com/en/blog/kimi-k3-vs-claude-code-codex)
10. [Kimi K3 just went toe-to-toe with Claude, and it's cheaper ...](https://www.howdoiuseai.com/blog/2026-07-18-kimi-k3-just-went-toe-to-toe-with-claude-and-it-s-)
11. [Kimi K3 vs Claude for Coding 2026: Benchmarks Compared](https://aiforesight360.com/kimi-k3-vs-claude-coding/)
12. [Kimi K3 with Claude Code: Setup, Env Vars and Real Limits (2026)](https://www.codeagentswarm.com/en/guides/kimi-k3-with-claude-code)
13. [Kimi vs Claude Code: Coding Agent Comparison 2026](https://www.layer3labs.io/comparisons/kimi-k3-vs-claude-code)
14. [Moonshot AI's Kimi K3 Claims Parity With OpenAI in China's Latest...](https://www.techbuzz.ai/articles/moonshot-ai-s-kimi-k3-claims-parity-with-openai-in-china-s-latest-salvo)
15. [Kimi K3: Moonshot AI's 2.8T Open-Weight Model](https://www.eigent.ai/blog/kimi-k3-open-weight-frontier-model)
16. [China Moonshot AI Kimi K3 claims rival OpenAI and Anthropic](https://beyondtmrw.org/article/china-moonshot-ai-kimi-k3-claims-rival-openai-and-anthropic)
17. [Kimi K3 Surpasses Claude in Frontend Coding Benchmarks | LinkedIn](https://www.linkedin.com/posts/muruganvenugopal_kimi-k3-moonshot-ai-is-performing-very-activity-7484041216322326528-8_CN)