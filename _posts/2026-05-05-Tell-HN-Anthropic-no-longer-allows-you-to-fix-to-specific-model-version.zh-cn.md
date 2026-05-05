---
layout: post
title: "昨天的 AI 和今天的 AI 不一样？Anthropic 取消“版本固定”功能的原因"
description: "为您深入浅出地解释 Anthropic 停止 Claude AI 模型版本固定功能的消息，以及由此引发的用户和开发者担忧。"
summary: "随着全球 AI 企业 Anthropic 移除固定使用特定版本模型的功能，人们对 AI 性能一致性的担忧日益增加。"
tags: [AI, Anthropic, Claude, 技术趋势, 开发者]
image: 2026-05-05-Tell-HN-Anthropic-no-longer-allows-you-to-fix-to-specific-model-version.jpg
image_alt: "一张抽象表达计算机屏幕上的 AI 模型代码发生微妙变化，导致用户感到困惑的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "强迫用户使用“最新性能”对企业而言虽然高效，但在视信任为生命的专业服务领域，这可能会成为毒药。"
quiz:
  - question: "据报道，Anthropic 最近移除的功能是什么？"
    choices: ["AI 的韩语回答功能", "将模型固定在特定时间点的功能", "付费订阅服务"]
    answer: 1
    explanation: "Anthropic 移除了允许开发者选择并固定（Pin）特定旧版本 AI 模型的功能。"
  - question: "Anthropic 的模型分类方式与竞争对手 OpenAI 有何不同？"
    choices: ["Anthropic 提供按日期排列的快照", "Anthropic 使用基于等级（Tier）的名称", "Anthropic 仅使用数字表示版本"]
    answer: 1
    explanation: "OpenAI 使用带日期的快照方式，而 Anthropic 使用类似“Claude 3.5 Sonnet”的以等级为核心的名称。"
  - question: "最近一些开发者经历的“无声降级”现象是什么？"
    choices: ["订阅费自动结算的现象", "旧模型在后台运行而非最新模型的现象", "AI 回答速度变快的现象"]
    answer: 1
    explanation: "有报告称，尽管请求了最新模型（如 Sonnet 4.6），系统却偷偷连接到了旧模型（如 Sonnet 4.5）。"
lang: zh-cn
ref: 2026-05-05-Tell-HN-Anthropic-no-longer-allows-you-to-fix-to-specific-model-version
---

## “昨天还是天才，今天怎么变这样？”

想象一下，你有一位非常精干、有能力的秘书。每天早上，他都会准时为你端来咖啡，并按你喜欢的风格汇总报告。然而有一天，这位秘书突然宣布他“学会了更高效的方式”，改为你端来绿茶，并擅自更改了报告格式。虽然秘书坚称“这是最新、最好的方式”，但你需要的不是“最新”，而是“一如既往的一致性”。

现在，AI 行业的巨头之一 **Anthropic** 正深陷类似的争议之中。这家开发了 ChatGPT 强力竞争对手“Claude”的公司，最近实际上取消了开发者固定（Pin）使用 AI 模型特定版本的功能。 [TellHN：Anthropic 不再允许固定特定模型版本...](https://news.ycombinator.com/item?id=47775389)

你可能会想：“最新版本不是更好吗？”但对于从事专业工作的人来说，这个消息相当令他们恐惧。为什么这么多聪明的开发者对此决定感到困惑？MindTickleBytes 将为你深入剖析其中的原因。

---

## 为什么这很重要？ (Why It Matters)

我们使用的 AI 并非一旦制成就永远不变的成品。为了提升性能和安全性，开发商每天都在更新 AI 的大脑。但在技术领域，“更新”并不总等同于“正确答案”。

**1. 不可预测性 (Unpredictability)**
假设有一家公司运营着利用 AI 审核复杂法律文件的服务。如果昨天还能完美识别特定条款的 AI，在今天突如其来的“更新”后开始遗漏该条款，会发生什么？服务的公信力将瞬间崩塌。打个比方，这就像你每天驾驶的汽车，刹车灵敏度在你睡醒后就会莫名其妙地发生变化。

**2. 成本与效率的不匹配**
最新模型通常更聪明，但计算量也更大，因此费用更贵。有些用户可能会认为：“我不需要太复杂的功能，我只想继续使用虽然适度聪明但价格便宜的去年版本。”如果厂商强制用户只能使用最新型，用户可能不得不支付不必要的额外费用。

**3. 保持工作精度**
在总结论文或编写精密代码的任务中，AI 是一种“工具”。就像木匠希望一直使用顺手的锤子一样，专家们往往坚持使用经过他们验证的特定日期的 AI 版本。Anthropic 的这次决定无异于在宣布：“我们给你什么，你就用什么，我们会自行决定帮你换成最好的。” [TellHN：Anthropic 不再允许固定特定模型版本...](http://hnforyou.com/ask)

---

## 深入浅出：“快照”与“菜单”的区别 (The Explainer)

管理 AI 模型的方式主要分为两种。为了便于理解，我们再次使用餐厅的例子。

### 1. OpenAI 方式：“原汁原味的日期快照”
OpenAI（ChatGPT 的制造者）会在模型名称后附带日期。例如 `gpt-4-0613`。 [今日 AI 更新（2026 年 5 月）——最新 AI 模型发布](https://llm-stats.com/llm-updates) 这种方式被称为 **快照（Snapshot，就像拍照一样保存特定时间点的状态）**。它的意思是：“我们把 2023 年 6 月 13 日版本的 AI 冷冻保存了，如果一年后你还需要，拿出来用还是那个味道。”用户有权选择自己想要的特定时点的 AI。

### 2. Anthropic 方式：“厨师精选，等级（Tier）系统”
相比之下，Anthropic 使用类似“Claude 3.5 Sonnet”这样以等级为主的名称。 [今日 AI 更新（2026 年 5 月）——最新 AI 模型发布](https://llm-stats.com/llm-updates) 这就像餐厅里的“高级套餐”菜单。虽然菜单名字一直没变，但如果厨师（Anthropic）认为“今天的食材这个更好”，他就会随意更换菜单构成（AI 的详细性能）。

问题在于，最近 Anthropic 在 API（程序间沟通的渠道）管理界面中去掉了明确选择特定日期版本的功能。 [TellHN：Anthropic 不再允许固定特定模型版本...](https://news.ycombinator.com/item?id=47775389) 现在，开发者只能祈祷 Anthropic 在后台进行的模型更换确实是一种“改进”，然后被动接受。

---

## 现状：“无声降级”的恐惧

这种政策变化已经引发了实际事故。最近，开发者社区中出现了大量荒唐的 Bug 报告。有案例发现，用户明明设置了使用最新模型“Sonnet 4.6”，系统却无视设置，偷偷将其连接到了性能较低的旧模型“Sonnet 4.5”。 [[BUG] Vertex/Bedrock 子代理被静默降级为旧模型 (Sonnet 4.5, Opus 4.1) · Issue #30815 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/30815)

这被称为 **静默降级（Silent Downgrade）**。用户相信自己支付了高昂费用在使用最新的 AI，但实际上却是旧版 AI 在提供回答。

Anthropic 的应对方式也引发了争议。当收到关于模型间对话协议“模型上下文协议（MCP）”中出现问题的举报时，Anthropic 方面给出了冰冷的回答：**“这并非设计缺陷，而是符合预期（Works as designed）。”** [Anthropic 的模型上下文协议如何实现简单的远程执行 | Hackaday](https://hackaday.com/2026/04/24/how-anthropics-model-context-protocol-allows-for-easy-remote-execution/)

此外，今年 4 月，Anthropic 还曾在付费服务“Claude Code”中突然限制用户使用第三方工具（如 OpenClaw 等）。 [编码代理内部机制，Anthropic 禁止第三方使用 Claude Code...](https://tldr.tech/dev/2026-04-06) 虽然该措施后来被撤回，但用户心中“Anthropic 只想过度控制我们”的不满正在积聚。 [Anthropic - OpenClaw](https://docs.openclaw.ai/providers/anthropic)

---

## 未来会如何？ (What's Next)

Anthropic 的这种做法既是一种“技术自信”，也是一场危险的“豪赌”。他们似乎在担保自己的 AI 更新非常完美，绝不会出现性能突然下降（Regression，回归现象）。事实上，最近公开的“Claude Mythos”模型确实展示了压倒性的性能，备受期待。 [Anthropic 在不告知的情况下静默降低了思考能力... | IBTimes UK](https://www.ibtimes.co.uk/concerns-rise-anthropic-ai-silent-performance-drop-1791504)

然而，用户的焦虑短期内恐难平息。我们需要关注的变化如下：

*   **智能的黑箱化**：确认我所使用的 AI 真实身份的方法正逐渐消失。即使在使用“装作很聪明的旧模型”，用户也无从得知。
*   **成本的不透明性**：随着模型自动更新，用户可能在不知不觉中面临计费体系变动的风险。 [编码代理内部机制，Anthropic 禁止第三方使用 Claude Code...](https://tldr.tech/dev/2026-04-06)
*   **用户流失的可能性**：视一致性和可靠性为生命的企业，很有可能会转向能够明确固定版本的 OpenAI 或谷歌（Gemini）。

---

## AI 视角：MindTickleBytes AI 记者点评

Anthropic 的决定似乎是在追求一种“用户无需逐一检查引擎的完美自动驾驶汽车”。虽然剥夺了你打开引擎盖查看的权利，但作为交换，它承诺始终提供最佳的驾驶体验。然而，当驾驶员无法检查引擎，而车又突然停下时，谁来承担责任呢？

随着 AI 逐渐成为我们社会的必备基础设施，与单纯追求“更高分数”的性能同等重要的，是用户能够控制的“信任”和“可预测性”。全球都在关注 Anthropic 将如何平衡这两者。

---

## 参考资料

1. [TellHN：Anthropic 不再允许固定特定模型版本...](https://news.ycombinator.com/item?id=47775389)
2. [TellHN：Anthropic 不再允许固定特定模型版本...](http://hnforyou.com/ask)
3. [今日 AI 更新（2026 年 5 月）——最新 AI 模型发布](https://llm-stats.com/llm-updates)
4. [模型 API | anthropics/anthropic-sdk-python | DeepWiki](https://deepwiki.com/anthropics/anthropic-sdk-python/5.4-models-api)
5. [[BUG] Vertex/Bedrock 子代理被静默降级为旧模型 (Sonnet 4.5, Opus 4.1) · Issue #30815 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/30815)
6. [Anthropic 的模型上下文协议如何实现简单的远程执行 | Hackaday](https://hackaday.com/2026/04/24/how-anthropics-model-context-protocol-allows-for-easy-remote-execution/)
7. [编码代理内部机制，Anthropic 禁止第三方使用 Claude Code...](https://tldr.tech/dev/2026-04-06)
8. [Anthropic - OpenClaw](https://docs.openclaw.ai/providers/anthropic)
9. [Anthropic 在不告知的情况下静默降低了思考能力... | IBTimes UK](https://www.ibtimes.co.uk/concerns-rise-anthropic-ai-silent-performance-drop-1791504)

## 事实核查摘要
- 待核实声明：14
- 已核实声明：14
- 结论：通过 (PASS)