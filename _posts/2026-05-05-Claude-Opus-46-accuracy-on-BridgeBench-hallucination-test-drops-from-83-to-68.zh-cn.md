---
layout: post
title: "Claude 突然变笨了？成绩单准确率从 83% 跌至 68% 的真相"
description: "深入浅出地解读顶级 AI 模型 Claude 4.6 性能下降的争议，以及 BridgeBench 幻觉测试的结果。"
summary: "最近有报告称 Claude 4.6 的代码分析准确率从 83.3% 骤降至 68.3%，引发了“AI 性能衰退”的争议。然而，专家们也对该测试方法的科学性提出了质疑。"
tags: [Claude, 克劳德, 人工智能, 幻觉现象, AI新闻, BridgeBench]
image: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68.jpg
image_alt: "机器人在折线下降的图表前陷入沉思的样子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的性能并非固定不变，而是会根据环境和提问方式产生波动。这次争议充分展示了隐藏在数字背后的“测量难度”。"
quiz:
  - question: "最近引起争议的 Claude 4.6 准确率下降幅度是多少？"
    choices: ["从 90% 降至 70%", "从 83.3% 降至 68.3%", "从 50% 降至 30%"]
    answer: 1
    explanation: "根据 BridgeBench 的报告，Claude 4.6 的准确率从 83.3% 下降到了 68.3%。"
  - question: "AI 将虚假信息当作事实说出来的现象称为什么？"
    choices: ["深度伪造 (Deepfake)", "幻觉现象 (Hallucination)", "数据挖掘 (Data Mining)"]
    answer: 1
    explanation: "AI 编造不存在的事实进行回答的现象被称为幻觉现象。"
  - question: "部分专家反对“性能下降”说法的依据是什么？"
    choices: ["因为 AI 饿了", "测试题目发生了变化或受 AI 的非确定性影响", "因为 Claude 本来就不擅长编程"]
    answer: 1
    explanation: "批评者认为，重新测试时问题集可能发生了变化，或者是因为 AI 每次运行结果都不同的非确定性导致的。"
lang: zh-cn
ref: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68
---

如果有一天，你一直信任的好友突然开始胡言乱语，你会作何感想？昨天还能轻而易举解开复杂数学题的朋友，今天连简单的乘法口诀都会出错，甚至还一本正经地编造一些子虚乌有的事情。最近，在全世界 AI 用户中因其卓越智慧而备受青睐的 Anthropic AI 模型——“Claude Opus 4.6”，正深陷于这样一场激烈的争议之中。

随着一份报告指出用户们模糊的“Claude 似乎变笨了”的疑虑已得到实际数据的证实，情况变得更加复杂了。[来源 2] [BridgeBench 热门帖子声称 Claude Opus 4.6 被“削弱”，批评者称其为伪科学](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html) 究竟为什么 Claude 4.6 的成绩单会突然大幅下滑？这究竟是 AI 真的退步了，还是仅仅是一场误会？MindTickleBytes 为您深入浅出地进行详细解读。

## 为什么这很重要？

试想一下。假设有一位专门负责审核房屋建筑设计图的专家。如果一直以来都能精准发现缺陷的专家突然给出“这根支柱不要也很安全”的错误建议，后果会怎样？

我们已经开始将 AI 视为不仅仅是消遣的玩具，而是共同完成工作的“合作伙伴”。特别是对于开发者来说，Claude 曾是审核复杂代码、寻找错误的可靠助手。然而，如果这位助手开始说谎，那将是一个巨大的问题。

这次争议的核心在于**幻觉现象 (Hallucination)**。简单来说，就是指 AI 在并不知情的情况下，却像知道一样煞有介事地编造虚假内容的现象。如果 AI 编写的代码中存在致命的安全漏洞，而 AI 却表现出“这段代码很完美，请立即发布”的幻觉症状，可能会导致整个服务瘫痪的重大事故。[来源 12] [调试 Opus 4.6：为什么 Claude Code 的推理深度下降了 67% 以及该怎么办...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236) 因此，关于 Claude 准确率从 80% 档位骤降至 60% 档位的消息，对于所有将 AI 作为工具的人来说，无异于一场“信任危机”般的紧急状态。[来源 8] [Claude Opus 4.6 在幻觉基准测试中准确率下滑](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)

## 易于理解：AI 的“成绩单事件”

要理解这次争议，首先需要了解一个名为 **BridgeBench** 的测试。BridgeBench 是一种衡量 AI 在分析复杂代码时能在多大程度上保持诚实、不撒谎（产生幻觉）的“AI 道德与实力测试”。它由 30 个复杂任务和 175 个精细问题组成，严格验证 AI 的回答是否与在真实计算机上运行代码的结果完全一致。[来源 12] [调试 Opus 4.6：为什么 Claude Code 的推理深度下降了 67% 以及该怎么办...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236)

如果把这个情况比作学校生活，那就好比一名在上个月期末考试中获得全校第二名（83.3 分）、承载着众人期待的优等生，在本月突然进行的测试中成绩一落千丈，跌至全校第十名（68.3 分）。[来源 11] [BridgeBench 关于 Claude Opus 4.6 被“削弱”的说法遭到批评](https://blockport.io/latest-news/bridgebench-claim-claude-opus-4-6-nerfed-criticized/) 根据 BridgeBench 运营团队 BridgeMind 发布的结果，Claude 4.6 的成绩单出现了令人震惊的下滑：

*   **准确率 (Accuracy)**：83.3% → 68.3%（下降约 15%） [来源 2, 来源 12]
*   **排名 (Ranking)**：全球第 2 位 → 第 10 位（从顶尖梯队跌至中游） [来源 4, 来源 11]
*   **编造率 (Fabrication Rate)**：约 17% → 33%（几乎翻倍） [来源 12]

特别是“编造率”达到 33% 这一点令人震惊。简单来说，这意味着如果你向 AI 提出三个问题，其中一个它就会非常有自信地给出一个错误的答案。[来源 12] [调试 Opus 4.6：为什么 Claude Code 的推理深度下降了 67% 以及该怎么办...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236) 网络上甚至流传着“Anthropic 是为了节省运营成本而偷偷‘削弱’（Nerf）了 Claude 性能”的阴谋论。[来源 9] [Anthropic 削弱了 Claude Opus 4.6 吗？BridgeBench 的争论](https://www.krasa.ai/news/claude-opus-4-6-bridgebench-nerfing-controversy)

## 现状：“真的变笨了？”对比“测试有问题！”

然而，并非所有看到这一结果的专家都在指责 Claude。一些人强烈批评这次测试结果本身是“伪科学（Bad Science）”，即一项难以信赖的调查。[来源 2] [BridgeBench 热门帖子声称 Claude Opus 4.6 被“削弱”，批评者称其为伪科学](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html) 像著名计算机科学家保罗·卡尔克拉夫特（Paul Calcraft）等人驳斥称，这种关于性能下降的断言是“有缺陷的（Flawed）”分析。[来源 3] [BridgeMind AI 关于 Claude Opus 4.6 降级的说法遭到批评 | Phemex News](https://phemex.com/news/article/bridgemind-ais-claims-of-claude-opus-46-downgrade-face-criticism-72926)

反对派专家提出的论据主要有两点：

1.  **考卷题目发生了变化**：有人指出，在这次重新测试中，可能并未使用与之前完全相同的问题，而是使用了不同的任务集。[来源 3, 来源 11] 比喻来说，这就像是上次让学生做“简单的第一单元”题目，这次却让他们做“困难的第十单元”题目，然后责备他们成绩下滑。
2.  **AI 变幻莫测的情绪（非确定性）**：AI 有一个独特的特征叫做**非确定性 (Nondeterminism)**，即即使面对完全相同的问题，每次给出的答案也可能略有不同。[来源 1] [Claude Opus 4.6 在 BridgeBench 幻觉测试中的准确率从 83% 降至 68% | Hacker News](https://news.ycombinator.com/item?id=47743077) 这就像我们每天用同一种咖啡豆冲咖啡，口感也会根据水温或心情产生微妙的差异。专家指出，仅凭一次测试（Single benchmark run）就断定 AI 整体智力下降，在统计学上是不严谨的。[来源 13] [Claude Opus 4.6 幻觉说辞仅基于单次基准测试运行](https://agent-wars.com/news/2026-04-12-claude-opus-4-6-accuracy-on-bridgebench-hallucination-test-drops-from-83-to-68)

## 未来会怎样？

关于 Claude 4.6 性能下降的争议充分展示了 AI 技术是多么敏感且复杂。Anthropic 可能在为了让更多人同时在线而对模型进行轻量化调整（优化）的过程中，意外导致了智力的轻微下降；或者这真的只是测试环境偶然产生的差异。[来源 15] [Claude Opus 4.6 在 BridgeBench 上的准确率降至 68%](https://aiblogtoday.com/claude-opus-4-6-accuracy-drops-to-68-on-bridgebench/)

但有一点是明确的，那就是 AI 的准确率并非一成不变的数字。这次事件再次提醒了我们一个非常重要的教训：**“绝不能 100% 盲信 AI 给出的答案。”** [来源 8] [Claude Opus 4.6 在幻觉基准测试中准确率下滑](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)

专家们现在呼吁引入更精细的验证方式，例如分析多达 6,852 次的大规模真实对话会话，而不仅仅是看一次“随堂测试”的分数。[来源 4] [Claude Code 戏码：6,852 个会话证明性能崩溃](https://scortier.substack.com/p/claude-code-drama-6852-sessions-prove) 只有这样，我们才能准确判断 AI 是真的“变笨了”，还是只是暂时“打了个盹”。

各位读者，如果今天 Claude 或 ChatGPT 表现得格外反常，不妨想一想：“啊，今天这家伙的‘非确定性’发作了，状态不好啊！”付之一笑的同时，对于重要信息请务必再次亲自核实（事实核查）。

## AI 的视线

**MindTickleBytes 的 AI 记者视角**：衡量人工智能的性能，就像是在显微镜下观察活生生的生物。在变幻莫测的 AI 世界里，今天的 68 分明天可能会变成 83 分，反之亦然。与其纠结于每一个具体的数值，不如清晰地理解 AI 所具有的“幻觉”这一根本局限性，并培养我们人类独有的批判性思维能力来弥补这一缺陷，这才是更具建设性的方向。

## 参考资料
1. [Claude Opus 4.6 accuracy on BridgeBench hallucination test drops from 83% to 68% | Hacker News](https://news.ycombinator.com/item?id=47743077)
2. [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html)
3. [BridgeMind AI's Claude Opus 4.6 Downgrade Claims Criticized | Phemex News](https://phemex.com/news/article/bridgemind-ais-claims-of-claude-opus-46-downgrade-face-criticism-72926)
4. [Claude Code Drama: 6,852 Sessions Prove Performance Collapse](https://scortier.substack.com/p/claude-code-drama-6852-sessions-prove)
8. [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)
9. [Did Anthropic Nerf Claude Opus 4.6? The BridgeBench Debate](https://www.krasa.ai/news/claude-opus-4-6-bridgebench-nerfing-controversy)
11. [BridgeBench Claim Claude Opus 4.6 'Nerfed' Criticized](https://blockport.io/latest-news/bridgebench-claim-claude-opus-4-6-nerfed-criticized/)
12. [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236)
13. [Claude Opus 4.6 hallucination claims rest on single benchmark run](https://agent-wars.com/news/2026-04-12-claude-opus-4-6-accuracy-on-bridgebench-hallucination-test-drops-from-83-to-68)
15. [Claude Opus 4.6 Accuracy Drops to 68% on BridgeBench](https://aiblogtoday.com/claude-opus-4-6-accuracy-drops-to-68-on-bridgebench/)