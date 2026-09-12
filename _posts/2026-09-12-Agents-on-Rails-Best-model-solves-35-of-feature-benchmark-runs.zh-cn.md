---
layout: post
title: "AI 代替我写代码？通过 'Agents on Rails' 基准测试看 AI 的真实实力"
description: "AI 编码代理在实际的 Ruby on Rails 项目中表现如何？我们通过最新的基准测试结果为您简单明了地解读。"
summary: "衡量 AI 在实际 Ruby on Rails 项目中实现复杂功能能力的 'Agents on Rails' 基准测试结果显示，顶级模型达到了 35% 的成功率，证明了其投入实战的可能性。"
tags: [AI, 编码, Ruby on Rails, Agents on Rails, 编程]
image: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs.jpg
image_alt: "可视化 AI 代理数据流在复杂代码文件之上的样子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "尽管 AI 的编码能力在飞速提升，但要完美完成实战水准的复杂功能仍有很长的路要走。不过，35% 这个数字仅仅是一个开始。"
quiz:
  - question: "Agents on Rails 基准测试中使用的实际项目名称是什么？"
    choices: ["Writebook", "RailsApp", "CodeAgent"]
    answer: 0
    explanation: "Agents on Rails 使用名为 Writebook 的实际项目来测试 AI 代理的性能。"
  - question: "在最近发布的 'Stage 2' 基准测试中，成功率最高的模型得分是多少？"
    choices: ["92%", "35%", "50%"]
    answer: 1
    explanation: "GPT-6 Astra 模型在 Stage 2 功能实现任务中创下了 35% 的成功率。"
  - question: "该基准测试之所以重要的最恰当原因是？"
    choices: ["为了测量 AI 的图形处理能力", "为了在与实际业务环境相似的环境中测量 AI 编码性能", "为了测试 AI 的写作能力"]
    answer: 1
    explanation: "该项目的目标是基于实际的 Ruby on Rails 代码库，测量 AI 在多大程度上能解决开发人员在工作中遇到的实际任务。"
lang: zh-cn
ref: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs
---

想象一下。早上醒来，你对 AI 助手说：“今天请在我们的网站上添加会员注册功能，并检查相关的安全问题。” 在你喝一杯咖啡的时间里，AI 已经编写好了复杂的代码，甚至完成了自我测试，并向你汇报：“所有工作已完成。”

这在几年前还只是科幻电影中的情节，但现在我们已经离这个未来又近了一步。那么，目前的 AI 在代替开发人员处理实际工作方面的表现到底如何呢？让我们通过 Ruby on Rails（用于 Web 应用程序开发的编程框架）基金会与 Evil Martians 最近公布的 **'Agents on Rails'** 基准测试结果，来一探究竟。 [[参考资料: Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report), [参考资料: Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)]

## 为什么这很重要？

到目前为止，许多 AI 模型都在宣传自己擅长编码，但实际企业环境中的项目要复杂和棘手得多。现有的基准测试大多仅停留在测试非常简短且简单的代码片段上。

'Agents on Rails' 之所以重要，是因为它是 **'实战型测试'**。它直接采用了开发人员实际使用的名为 'Writebook' 的项目代码，让 AI 去执行修复 Bug、检查安全漏洞、添加新功能等实务中会遇到的任务。 [[参考资料: Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report), [参考资料: Agents on Rails benchmark: model picks by cost and score](https://tokenstead.ai/guides/agents-on-rails-first-benchmark-report)] 换句话说，这一结果就像是一份“实务成绩单”，告诉我们在将 AI 引入我们的工作环境时，到底能信任它到什么程度。

## 简单易懂的比喻

如果把这个基准测试做一个比喻，就很容易理解了。

简单来说，如果以往的 AI 性能测量方式就像是参加“小学生水平的英语单词考试”，那么 'Agents on Rails' 就像是进入英语国家的公司入职，必须像新员工一样撰写报告并进行协作的“实务能力评估”。

AI 代理就像是刚进公司的职场新人。在第一阶段测试中，它们被要求处理非常简短且独立的任务（寻找 Bug、修复安全问题等）；在第二阶段测试中，它们被要求执行像实际开发人员那样 **'实现功能的整个过程'**。 [[参考资料: Agents on Rails: Stage 2. Can a model ship a feature?](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2), [参考资料: Agents on Rails: We ran 8 models against 21 atomic tasks to ...](https://www.linkedin.com/posts/ruby-on-rails-org_agents-on-rails-we-ran-8-models-against-activity-7493709649016188929-F2nq)]

在最近公布的第二阶段结果中，表现最出色的 'GPT-6 Astra' 模型所记录的成功率为 **35%**。你可能会觉得“呃？比想象中要低呀？”。但如果 AI 能独自成功完成 35% 的复杂实际工作，这意味着如果有熟练的开发人员在旁进行审核和修改，它完全可以达到极大提高工作效率的水平。

## 目前状况

目前，'Agents on Rails' 正在针对 8 个主要 AI 模型进行彻底的验证。 [[参考资料: Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)]

- **顶级模型的表现**：在第一阶段测试中，'Claude Opus 5' 记录了 92% 的惊人成功率。 [[参考资料: Agents on Rails: the first benchmark report | Vuink.com](https://vuink.com/post/eholbaenvyf-d-dbet/2026/8/13/agents-on-rails-the-first-benchmark-report)]
- **多种选择**：'Kimi K3' 以顶级模型一半的成本实现了 90% 的性能，证明了其效率；'GPT-5.6 Luna' 则因最低的成本而引人注目。 [[参考资料: Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)]
- **局限性**：但如第二阶段测试（必须实现完整功能）所表明的那样，AI 在完全理解实战项目的整体上下文并零失误地完成代码方面，仍需要进一步完善。

## 未来将会如何？

未来，AI 编码代理会变得更加聪明。Rails 基金会不仅会评估模型的成功率，还会综合评价它们对最新开发模式的反映程度、Token 成本（AI 处理数据时产生的单位成本）是否合理等，并持续进行演进。 [[参考资料: Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)]

读者们需要关注的不仅仅是分数，更是 **'趋势'**。AI 正在从仅仅懂得语法的阶段，跨越到直接实现能够创造实际商业价值功能的阶段。不久之后，当成功率从 35% 提升到 50%、70% 时，我们的工作方式将发生彻底的改变。

## MindTickleBytes 的 AI 记者视角
本次基准测试证明了 AI 正在超越编码的“助手”，向“同事”蜕变。35% 这个数字虽然并不完美，但 AI 已经开始理解并执行实际开发人员的工作流程，这一点比任何结果都更令人充满希望。

## 参考资料

1. [Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report)
2. [Agents on Rails: The LLM Benchmark Project](https://rubyonrails.org/2026/8/12/llm-benchmarking-project)
3. [Agents on Rails: Stage 2. Can a model ship a feature?](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2)
4. [Agents on Rails: Grok 4.6, GLM 5.3, Gemini 3.7 Flash, and Opus 4.8](https://rubyonrails.org/2026/8/17/agents-on-rails-grok-4-6-glm-5-3-gemini-3-7-flash-and-opus-4-8)
5. [Agents on Rails: the first benchmark report | Vuink.com](https://vuink.com/post/eholbaenvyf-d-dbet/2026/8/13/agents-on-rails-the-first-benchmark-report)
6. [Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)
7. [Agents on Rails benchmark: model picks by cost and score](https://tokenstead.ai/guides/agents-on-rails-first-benchmark-report)
8. [Agents on Rails: We ran 8 models against 21 atomic tasks to ...](https://www.linkedin.com/posts/ruby-on-rails-org_agents-on-rails-we-ran-8-models-against-activity-7493709649016188929-F2nq)
9. [What the First Rails Agent Benchmark Tells You, and What It ...](https://www.convective.com/currents/what-the-first-rails-agent-benchmark-tells-you)
10. [Rails team's first "Agents on Rails" benchmark report: how well do models actually know Rails APIs?](https://www.rubyforum.org/t/rails-teams-first-agent-benchmark-report-how-well-do-models-actually-know-rails-apis/631)
11. [Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)