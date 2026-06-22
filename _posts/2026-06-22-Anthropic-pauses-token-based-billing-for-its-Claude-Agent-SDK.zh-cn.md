---
layout: post
title: "AI 定价突然变更？Anthropic 为何在开发者抵制下叫停"
description: "近日，AI 公司 Anthropic 暂停了原计划引入的全新基于 Token 的定价方案。我们将为您深入浅出地解析开发者为何抵制，以及这对我们有何深远影响。"
summary: "由于开发者的强烈抵制，Anthropic 已暂停为 Claude Agent SDK 引入高额的基于 Token 的定价方案。"
tags: [AI, Anthropic, Claude, 定价, 技术议题]
image: 2026-06-22-Anthropic-pauses-token-based-billing-for-its-Claude-Agent-SDK.jpg
image_alt: "Anthropic Logo 置于交错的复杂文档与代码背景之上"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企业追求创新固然重要，但若创新导致用户难以承受的成本压力，便会丧失信任。此次叫停决定表明，AI 服务若要实现普及，必须以“可持续的经济性”为基础。"
quiz:
  - question: "Anthropic 计划引入并随后叫停的定价模式是什么？"
    choices: ["订阅制无限使用", "基于 Token 的按量付费", "观看广告免费使用"]
    answer: 1
    explanation: "Anthropic 原计划将 Agent SDK 的使用量从现有订阅服务中剥离，转向基于 Token 的按量付费计费体系。"
  - question: "此次定价变动最让开发者担忧的是什么？"
    choices: ["服务速度下降", "费用突然飙升", "数据安全问题"]
    answer: 1
    explanation: "开发者担心，原本在订阅费用内包含的大规模 Agent 任务将改为单独计费，从而导致成本大幅增加。"
  - question: "Anthropic 给开发者发送的公告核心内容是什么？"
    choices: ["定价方案全面废除", "维持现有政策", "确认涨价两倍"]
    answer: 1
    explanation: "Anthropic 通过发给客户的电子邮件明确表示：“目前没有任何改变（Nothing changes for now）”，从而叫停了该政策。"
lang: zh-cn
ref: 2026-06-22-Anthropic-pauses-token-based-billing-for-its-Claude-Agent-SDK
---

想象一下：你正在订阅一款按月支付固定费用的流媒体服务，享受着无限看权限。突然，公司宣布：“从现在起，每看一部电影都要按分钟加收费用。”你会作何感想？对于习惯每天看电影的用户来说，这不仅是困惑，更会引发愤怒。

最近，人工智能领域就发生了类似事件。知名 AI 公司 Anthropic 曾宣布要改变其开发工具“Claude Agent SDK”（帮助 AI 自主思考并执行任务的工具）的计费体系，但仅在实施前夕便紧急叫停。 [Source 2](https://www.devdigest.org/articles/anthropic-pauses-token-based-billing-for-claude-agent-sdk), [Source 6](https://www.aichatdaily.com/ai-business/anthropic-pauses-token-based-billing-change-claude-agent-sdk)

### 为何此事至关重要？

这一事件表明，AI 技术的发展不仅局限于“变得更聪明”，在人们如何“付费与使用”的经济层面，也正处于一个重要的转折点。 [Source 4](https://www.weexplaintech.com/2026/06/anthropic-pauses-token-based-billing.html) 

开发者利用 AI 构建执行复杂自动化任务的应用。如果计费模式骤变，运营成本可能会瞬间翻倍。这绝不仅仅是开发者的烦恼。运营成本上涨，最终会以服务涨价或功能缩水的形式转嫁给使用这些 AI 应用的普通用户。 [Source 1](https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-claude-agent-sdk), [Source 10](https://www.newsbreak.com/news/4714926599628-anthropic-pauses-token-based-billing-for-its-claude-agent-sdk)

### 通俗理解：从“自助餐”变为“按盘计费”？

简单来说，Anthropic 的方案是将“自助餐模式”改为“按盘计费模式”。

原本开发者支付固定月费即可获得一定量的 AI 使用额度。但在 5 月 13 日，Anthropic 宣布从 6 月 15 日起将“Claude Agent SDK”的使用量从现有订阅福利中移除。 [Source 7](https://www.winzheng.com/en/article/anthropic-pauses-claude-agent-sdk-token-billing) 

类比来看，原本的订阅费成了“入场费”，而 AI 实际执行任务的量将按“Token”（AI 处理数据的单位，类似于句子的碎片）额外收费。 [Source 7](https://www.winzheng.com/en/article/anthropic-pauses-claude-agent-sdk-token-billing), [Source 8](https://letsdatascience.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-1cff2071) 用户甚至可能需要额外购买 20 美元到 200 美元不等的点数。 [Source 8](https://letsdatascience.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-1cff2071)

### 当前现状

该计划原定于 6 月 15 日生效。 [Source 4](https://www.weexplaintech.com/2026/06/anthropic-pauses-token-based-billing.html), [Source 6](https://www.aichatdaily.com/ai-business/anthropic-pauses-token-based-billing-change-claude-agent-sdk) 然而消息一出，开发者抵制声浪不断。尤其是那些利用 AI 处理大量自动化任务的“重度用户”，担心自己的运营成本会飙升到无法承受的程度。 [Source 2](https://www.devdigest.org/articles/anthropic-pauses-token-based-billing-for-claude-agent-sdk), [Source 9](https://www.coreiten.com/en/article/anthropic-abruptly-halts-claude-agent-sdk-billing-hike-after-developer-backlash)

最终，Anthropic 在生效当日紧急叫停了该计划。 [Source 13](https://www.bitsminds.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-2026) 公司在给客户的邮件中简洁地表示：“目前没有任何改变（Nothing changes for now）”。 [Source 13](https://www.bitsminds.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-2026) 目前，原有的订阅模式和使用限制保持不变。 [Source 12](https://www.msn.com/en-us/news/other/anthropic-pauses-claude-agent-sdk-billing-overhaul/gm-GM25B5B0AE)

### 未来会怎样？

此次叫停证明了 Anthropic 无法忽视开发者的声音。但这并不意味着定价改革会永远消失。随着 AI 服务规模扩大及模型性能提升，企业确实需要寻找更高效、更具可持续性的盈利模式。 [Source 4](https://www.weexplaintech.com/2026/06/anthropic-pauses-token-based-billing.html) 

未来，我们将密切关注 Anthropic 如何与开发者沟通，以制定更合理且可预测的定价体系。随着 AI 深入日常生活，其使用成本也应保持透明、合理，唯有如此，才能真正加速技术的普及进程。

## 参考资料

1. [Anthropic “pauses” token-based billing for its Claude Agent SDK](https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk/)
2. [Anthropic Pauses Token-Based Billing for Claude Agent SDK](https://www.devdigest.org/articles/anthropic-pauses-token-based-billing-for-claude-agent-sdk)
3. [Anthropic “pauses” token-based billing for its Claude Agent SDK](https://vuink.com/post/nefgrpuavpn-d-dpbz/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk)
4. [Anthropic Pauses Token-Based Billing - weexplaintech.com](https://www.weexplaintech.com/2026/06/anthropic-pauses-token-based-billing.html)
5. [Anthropic "pauses" token-based billing for its Claude Agent SDK](https://article.wn.com/view/2026/06/17/Anthropic_pauses_tokenbased_billing_for_its_Claude_Agent_SDK/)
6. [Anthropic pauses token-based billing change for Claude Agent SDK](https://www.aichatdaily.com/ai-business/anthropic-pauses-token-based-billing-change-claude-agent-sdk)
7. [Anthropic Pauses Claude Agent SDK Token Billing Change Amid ...](https://www.winzheng.com/en/article/anthropic-pauses-claude-agent-sdk-token-billing)
8. [Anthropic Pauses Claude Agent SDK Billing Overhaul](https://letsdatascience.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-1cff2071)
9. [Anthropic Pauses Claude Agent SDK Billing Changes for Developers](https://www.coreiten.com/en/article/anthropic-abruptly-halts-claude-agent-sdk-billing-hike-after-developer-backlash)
10. [Anthropic "pauses" token-based billing for its Claude Agent SDK](https://www.newsbreak.com/news/4714926599628-anthropic-pauses-token-based-billing-for-its-claude-agent-sdk)
12. [Anthropic Pauses Claude Agent SDK Billing Overhaul - MSN](https://www.msn.com/en-us/news/other/anthropic-pauses-claude-agent-sdk-billing-overhaul/gm-GM25B5B0AE)
13. [Anthropic Backs Off Its Claude Agent SDK Billing Overhaul on ...](https://www.bitsminds.com/news/anthropic-pauses-claude-agent-sdk-billing-overhaul-2026)