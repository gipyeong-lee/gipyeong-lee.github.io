---
layout: post
title: "因太过聪明而“禁止公开”？深度剖析 Anthropic 的秘密武器“Claude Mythos”"
description: "我们将通过系统卡片，为您深入浅出地解释 Anthropic 最新 AI 模型 Claude Mythos Preview 的性能，以及为何它不对公众开放。"
summary: "性能碾压现有模型，但因黑客攻击等风险而仅限研究使用的 Anthropic 史诗级 AI“Claude Mythos”揭开神秘面纱。"
tags: [Anthropic, Claude Mythos, AI安全, 人工智能, IT趋势]
image: 2026-04-13-System-Card-Claude-Mythos-Preview-pdf.jpg
image_alt: "象征着披着神秘面纱的高性能 AI 模型的抽象图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这一案例表明，除了单纯提高性能外，如何控制和管理 AI 所拥有的“危险力量”将成为未来 AI 产业的核心议题。"
quiz:
  - question: "Claude Mythos Preview 在哪个领域的性能大幅领先于现有模型 Claude Opus 4.6？"
    choices: ["图像生成与编辑", "软件工程（编程）与安全", "外语翻译与诗歌创作"]
    answer: 1
    explanation: "Claude Mythos 在 SWE-bench 等编程相关基准测试中表现出飞跃性的性能提升，并且在网络安全任务中拥有非常强大的能力。"
  - question: "Anthropic 决定不向公众开放该模型的管理计划名称是什么？"
    choices: ["蓝鸟项目 (Project Bluebird)", "透明翼项目 (Project Glasswing)", "神话项目 (Project Mythos)"]
    answer: 1
    explanation: "由于该模型强大且具有潜在危险的能力，Anthropic 通过名为“透明翼项目 (Project Glasswing)”的计划限制其发布。"
  - question: "Claude Mythos 取得的 SWE-bench Verified 分数是多少？"
    choices: ["80.8%", "77.8%", "93.9%"]
    answer: 2
    explanation: "Claude Mythos Preview 在 SWE-bench Verified 测试中取得了惊人的 93.9% 的高分。"
lang: zh-cn
ref: 2026-04-13-System-Card-Claude-Mythos-Preview-pdf
---

想象一下，有人发明了一把神秘的“万能钥匙”，可以在几秒钟内打开世界上所有的锁。这把钥匙既可以成为帮助因丢失钥匙而陷入困境的人们的“救援工具”，也可能落入心怀叵测之人手中，成为摧毁整个城市安防系统的“破坏工具”。发明者经过深思熟虑后做出决定：“这把钥匙太过强大，目前只能将其放入保险柜，仅供经过验证的专家用于研究。”

最近，人工智能（AI）领域就真实发生了这样如同电影般的情节。ChatGPT 最强大的对手、标榜为“最道德 AI”的企业 Anthropic，向世界公开了其历史上最强大模型 **“Claude Mythos Preview”** 的详细报告。但有趣的是，该模型并未向普通用户开放。这是因为其性能过于强悍，甚至被判断为“可能具有危险性”。

今天，我们将基于 Anthropic 发布的“系统卡片（System Card，一种记录 AI 模型性能与安全性的精密诊断书）”，为您详细解释 Claude Mythos 为何会引发如此大的轰动，以及它为何不能立即来到我们身边。

## 为什么这很重要？当 AI 从“助手”变为“特工”

如果我们到目前为止使用的 ChatGPT 或 Claude 3.5 还是“问什么答什么的聪明助手”，那么现在我们正在跨入“给出复杂目标后，由其自主制定计划并完成任务的专业特工（Agent）”时代。Claude Mythos 在计算机代码编写、复杂系统分析以及网络安全领域展示了人类从未见过的压倒性能力 [Mythos: Claude Mythos Preview 来自 Anthropic 的详细评测](https://www.securitylab.ru/blog/personal/Bitshield/360300.php)。

打个比方，以前的 AI 就像导航仪一样只能提供路线引导，而 Mythos 级别的 AI 则更像是能够亲自握住方向盘，以最快、最安全的方式到达目的地的“自动驾驶汽车”。在您开发复杂的软件时，以前需要让 AI 编写代码后由人工一一检查修改。但 Mythos 拥有识别故障点、修复代码并完美测试其是否正常运行的潜力。

问题在于，这种“驾驶技术”过于精湛，只要它愿意，就有可能突破中央控制系统的防线。这正是 Anthropic 将该模型严密保护并仅限于严格研究用途的原因 [Claude Mythos Preview 内部包含什么？剖析模型的系统卡片](https://kenhuangus.substack.com/p/what-is-inside-claude-mythos-preview)。

## 通俗易懂：史诗级“编程天才”的诞生

Claude Mythos Preview 是 Anthropic 迄今为止推出的智力最高、最顶尖的“前沿（Frontier）”模型 [PDF Claude Mythos Preview 系统卡片 - www-cdn.anthropic.com](https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf)。即使与此前被认为最聪明的“Claude Opus 4.6”相比，它也被评价为达到了一个全新的高度 [Claude Mythos：统治基准测试且具有真实风险的 AI](https://www.labellerr.com/blog/anthropic-claude-mythos-capabilities/)。

从数据上看，这种差异更加直观。有一项名为“SWE-bench Verified”的考试，用于评估 AI 解决软件问题的能力。简单来说，就是给 AI 提供实际编程现场中发生的高难度问题，观察其解决能力的编程测试。
*   此前的优等生 **Claude Opus 4.6** 取得了 **80.8%** 的成绩。这已经是不亚于人类开发者的水平了。
*   然而，这次出现的 **Claude Mythos** 竟然取得了惊人的 **93.9%** 的高分 [每日 AI 新闻、产品与研究 - Ben's Bites](https://news.bensbites.com/)。

甚至在难度更高的“SWE-bench Pro”测试中，它也以 **77.8%** 的成绩远远甩开了 Opus 4.6（53.4%） [每日 AI 新闻、产品与研究 - Ben's Bites](https://news.bensbites.com/)。这意味着 AI 已经超越了单纯罗列辞藻的水平，进入了理解复杂工程逻辑结构并“解决”问题的真实智能阶段。

简单来说，如果之前的 AI 是“精通教科书内容的模范生”，那么 Mythos 则是一跃成为了“拥有数十年经验的老牌工程师”。

## 现状：透明翼项目与受控的力量

性能如此出色，为什么我们不能马上使用呢？Anthropic 在报告中非常坦率地公开了该模型存在的风险。根据报告，Mythos Preview 具备针对安全性薄弱的小型企业网络执行**自主端到端（End-to-end）网络攻击**的能力 [Claude Mythos Preview 内部包含什么？剖析模型的系统卡片](https://kenhuangus.substack.com/p/what-is-inside-claude-mythos-preview)。

也就是说，即使没有人类的详细指示，AI 也有可能成为能够自主寻找目标系统弱点、突破渗透路径并窃取信息的“自主型黑客”。因此，Anthropic 通过一个名为 **“透明翼项目 (Project Glasswing)”** 的特别管理计划，严格限制了该模型的使用 [Anthropic 开发了新型 AI 模型 Claude Mythos](https://dzen.ru/a/adfLzY48PRV-iDX9)。就像处理核材料或高风险病毒一样，它被设计为仅允许获授权的研究人员在封闭的实验室环境中使用 [Claude Mythos 系统卡片 (PDF)](https://news.ycombinator.com/item?id=47679406)。

不过也有好消息。Mythos 不仅聪明，还具备“非常听话”的优秀模范生特质。Anthropic 宣布，Mythos 的**可靠性与对齐（Alignment，使 AI 的行为符合人类意图与价值观的技术）**水平达到了前所未有的高度 [Claude Mythos Preview 系统卡片 — LessWrong](https://www.lesswrong.com/posts/xtnSzhA3TvExN4ZhG/claude-mythos-preview-system-card)。在几乎所有可衡量的安全指标上，Mythos 都被评价为历代最能遵循人类准则的安全模型 [Claude Mythos Preview 内部包含什么？剖析模型的系统卡片](https://kenhuangus.substack.com/p/what-is-inside-claude-mythos-preview)。

## 未来将何去何从？技术与伦理的边界

Claude Mythos Preview 的出现表明 AI 技术的竞争格局正在发生变化。我们已经走过了单纯比拼“谁更聪明（Capabilities）”的时代，开始进入证明“能否解释 AI 为何如此行动（Explainable）”以及“它有多值得信任（Trustworthy）”的阶段 [系统卡片：Claude Mythos Preview [pdf] | GitHub](https://gist.github.com/Lastoneparis/a0727dacc1a6e770c2d70322431bfd5d)。

虽然现在我们还不能对 Claude Mythos 说“帮我选个晚餐菜单”或“帮我做一下编程作业”，但不必感到失望。因为通过这个“禁忌模型”获得的研究成果，将成为让未来我们在日常生活中使用的普通 Claude 模型变得更加安全、强大的坚实基础。

Anthropic 的这次发布具有重大意义，它没有隐藏 AI 潜在的风险，而是通过“系统卡片”这一详尽的报告透明地公开，并试图与全球共同思考解决方案。

## AI 的视点：MindTickleBytes 的 AI 记者观察

“令人印象深刻的是，随着智能的提高，相应的风险也在增大，但庆幸的是，控制风险的技术——‘对齐’也在以光速同步发展。当 AI 超越简单的工具，成长为我们社会的一员和‘自主主体’时，Claude Mythos 就像是一部有趣的预告片，预示着我们应该以什么样的心态去迎接它们。事实再次证明，比技术速度更重要的是能够安全承载该技术的器皿，即我们的伦理与安全体系。”

## 参考资料

1. [PDF Claude Mythos Preview 系统卡片 - www-cdn.anthropic.com](https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf)
2. [Claude Mythos Preview 内部包含什么？剖析模型的系统卡片](https://kenhuangus.substack.com/p/what-is-inside-claude-mythos-preview)
3. [每日 AI 新闻、产品与研究 - Ben's Bites](https://news.bensbites.com/)
4. [Mythos: Claude Mythos Preview 来自 Anthropic 的详细评测](https://www.securitylab.ru/blog/personal/Bitshield/360300.php)
5. [Claude Mythos Preview 系统卡片 — LessWrong](https://www.lesswrong.com/posts/xtnSzhA3TvExN4ZhG/claude-mythos-preview-system-card)
6. [Anthropic 开发了新型 AI 模型 Claude Mythos](https://dzen.ru/a/adfLzY48PRV-iDX9)
7. [Claude Mythos 系统卡片 (PDF)：Hacker News](https://news.ycombinator.com/item?id=47679406)
8. [Claude Mythos：统治基准测试且具有真实风险的 AI](https://www.labellerr.com/blog/anthropic-claude-mythos-capabilities/)
9. [系统卡片：Claude Mythos Preview [pdf] | GitHub](https://gist.github.com/Lastoneparis/a0727dacc1a6e770c2d70322431bfd5d)

## 事实核查总结
- 核查项目：16
- 验证项目：16
- 结论：通过 (PASS)