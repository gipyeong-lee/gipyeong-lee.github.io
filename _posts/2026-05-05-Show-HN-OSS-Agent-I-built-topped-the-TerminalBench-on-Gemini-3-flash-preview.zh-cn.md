---
layout: post
title: "超越巨头谷歌的‘无名AI骑士’，登上终端王座"
description: "开源AI智能体‘Dirac’打破谷歌官方纪录，夺得终端基准测试冠军的秘诀及其对未来的影响"
summary: "搭载谷歌 Gemini 3 的开源AI智能体 Dirac 在计算机专家领域——‘终端’控制测试中刷新了世界第一纪录。"
tags: [AI智能体, Gemini3, 开源, Dirac, 终端基准测试]
image: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview.jpg
image_alt: "黑色终端屏幕上方，闪烁的数字大脑正在实时解决复杂代码"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这一事件证明，公开协作的力量可能比巨头公司的垄断技术更强大。它展示了 AI 从单纯的对话伙伴向‘行动助手’进化的转折点。"
quiz:
  - question: "此次刷新世界纪录的开源AI智能体叫什么名字？"
    choices: ["Gemini CLI", "Dirac", "Junie CLI"]
    answer: 1
    explanation: "Dirac 是由 Dirac Delta Labs 的 Max Trivedi 开发的一款开源AI智能体。"
  - question: "评估 AI 终端操作能力的这项测试名称是？"
    choices: ["TerminalBench 2.0", "Gemini 测试", "Hacker News 基准测试"]
    answer: 0
    explanation: "TerminalBench 是评估 AI 在命令行界面中执行文件管理或脚本编写能力的基准。"
  - question: "Dirac 在此次测试中记录的正确率是多少？"
    choices: ["47.8%", "64.3%", "65.2%"]
    answer: 2
    explanation: "Dirac 创下了 65.2% 的成功率，大幅领先谷歌的官方纪录 (47.8%)。"
lang: zh-cn
ref: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview
---

想象一下，你突然独自被留在一个布满复杂机械装置的巨大工厂控制室。四周有成千上万个开关，屏幕上不断滚动着让人无法理解、如同密码般的代码。这里是驱动工厂一切运作的核心地带，但如果你不是一名经验极其丰富的技术人员，你甚至不敢轻易触碰任何东西。

在我们每天使用的计算机中，也存在这样一个“秘密控制室”。那就是布满黑色背景和白色文字的**终端（Terminal，通过直接输入命令来控制计算机的窗口）**。普通用户通过鼠标点击精美的图标来使用电脑，而真正的专家则通过终端这个工具直接操纵计算机的骨架，设计复杂的系统。

然而最近，在这个专家的圣域——终端领域，发生了一件令世界震惊的事情。一家由个人开发者创建的“无名开源 AI”击败了谷歌（Google）等巨头公司制作的官方 AI，成为了世界上最聪明的终端专家。这就像是一位街头小吃店的厨师在米其林三星大厨的厨艺大赛中夺冠一样，充满了反转。

## 为什么这很重要？“从只会说话的 AI 转向会行动的 AI”

到目前为止，我们遇到的 ChatGPT 或 Gemini 等 AI 主要擅长“说话”。在“写诗”、“翻译英语”、“总结长文”等请求上，它们表现得非常出色。但是，如果要交给它们一些实际工作，比如“帮我把电脑里乱七八糟的 1,000 个文件按内容整理好，并自动安装所需的程序”，它们往往表现得并不稳定。

这次引发热议的名为 **Dirac** 的 AI 智能体则完全不同。根据 [Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview) 的报道，Dirac 证明了它能够直接接入计算机最深处的终端，发出复杂指令、管理文件并自主解决问题的能力。

简单来说，这意味着 AI 已经超越了仅仅提供信息的“口才好的秘书”，进化成了能够代为管理电脑、处理复杂技术任务的**“能干的代理人（Agent）”**。特别是，夺得第一名的不是投入了数万亿资金的大型企业的付费服务，而是任何人都可以查阅设计图并免费使用的**开源（Open Source，向大众公开软件设计图即源代码）**模型，这一点让全世界的开发者感到狂热。

## 通俗理解：AI 的“驾照考试”——TerminalBench

为了衡量 AI 有多聪明，专家们会让它们参加各种“考试”。这次 Dirac 登上王座的考试是 **TerminalBench 2.0**。[Open-Source AIAgentTopsTerminalBench2.0 Leaderboard](https://aihaberleri.org/en/news/open-source-ai-agent-scores-652percent-on-terminalbench-20-in-2026-beating-gemini-and-junie-cli)

如果把这项考试做个类比，它就像是**“面向 AI 的高难度驾驶考试”**。只不过驾驶的不是汽车，而是“计算机终端”这个极其棘手和复杂的装置。考试项目包含了一些连专家都会汗流浃背的难题：[OSS Agent Tops TerminalBench with Gemini-3 - PromptZone](https://www.promptzone.com/maria_gonzalez_419fd1b8/oss-agent-tops-terminalbench-with-gemini-3-3lh2)

1.  **Shell 脚本编写 (Shell Scripting)**：按顺序编写给计算机下达的多个步骤的指令（打个比方，就像是毫无误差地写出供数万人食用的复杂菜肴的食谱）。
2.  **文件管理**：在成千上万个文件中寻找细微差别，筛选、移动和修改所需内容的精细工作。
3.  **系统设置**：根据目的完全改造计算机内部环境的高难度任务。

开发者‘umair24171’评价道：“大多数 AI 考试往往只是简单的知识问答，但 TerminalBench 是真正衡量 AI 是否能实际‘干活’的实战测试。” [Gemini-3-Flash: My aiagentbenchmarkterminalbenchWin & 3 Fixes](https://dev.to/umair24171/gemini-3-flash-my-ai-agent-benchmark-terminalbench-win-3-fixes-44eb)

## 当前局势：大卫击败歌利亚的惊人分差

这次对决的结果对整个 IT 行业产生了巨大的冲击。这就像是一个一直稳居全校第一的富家优等生，被一个自寻出路努力学习的学生以压倒性的分差击败了一样。让我们来看看实际的成绩单：

*   **Dirac**：**65.2%**（基于任何人都可以使用的开源架构） [r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/ )
*   **Junie CLI**：64.3%（原排名第一的昂贵付费商用模型）
*   **谷歌官方纪录**：**47.8%**（谷歌直接用自家模型测试的结果）

令人惊讶的是，Dirac 的得分比谷歌创下的官方纪录高出了整整 17.4 个百分点。如果换算成学校考试，谷歌得了 48 分，而 Dirac 则拿到了超过 65 分。[r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/)

这位胜利背后的隐形助推器实际上是谷歌开发的最新 AI 大脑——**Gemini-3-flash-preview** 模型。[Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview) Gemini-3 Flash 是谷歌的野心之作，旨在执行复杂编码和系统任务时，比现有模型更快、更聪明地运作。[Gemini3Flash— Google DeepMind](https://deepmind.google/models/gemini/flash/)

但关键在于，谷歌自身未能充分利用这一优秀的引擎，得分停留在 40 分左右；而开发者麦斯·特里维迪（Max Trivedi）通过对该引擎进行精细调整和优化，发挥出了世界顶级性能。而且，他是在没有任何隐瞒、公开了所有设计图的情况下做到的。[ShowHN:OSSAgentIbuilttoppedtheTerminalBenchon...](https://news.ycombinator.com/item?id=47920787)

## 未来会怎样？来到我们身边的“万能维修工” AI

Dirac 的成功清晰地展示了我们即将迎来的两个未来。

第一，**AI 将成为我们家里的“电脑万能维修工”。**想象一下，当电脑速度突然变慢或弹出原因不明的错误窗口时，不再需要支付昂贵的维修费请专家，而是对 AI 智能体说：“去终端查查这个问题的原因并修好它。” AI 在黑色屏幕中浏览数万行代码并在 1 分钟内完成维修的时代已经不远了。

第二，**“共同创造的力量”将战胜巨头企业的垄断。**虽然借用了谷歌制造的引擎，但如果全球的人们共同思考和改进利用该引擎的更好方法（智能体结构），就能产出比企业独自秘密研发更优秀成果，这一点在这次事件中得到了证实。

当然，前方仍有路要走。65.2% 的得分意味着 10 次中仍可能有 3 次出错。在终端操作中出错，可能面临删掉珍贵家庭照片或重要办公文件的风险。因此，开发者们为了确保 AI 绝不出错，正在不断研究以建立更完美的“安全装置”。

## AI 视角：MindTickleBytes AI 记者的观察

“Dirac 的胜利不仅仅是数字的对决。它证明了 AI 这一强大工具并非特定大企业的专利，而是当我们所有人的智慧和好奇心汇聚在一起时，它能发出最耀眼的光芒。现在，我们已经度过了纠结于‘该问 AI 什么’的时代，正站在真正‘智能体时代’的门槛上，开始思考‘该把电脑里的哪些难题交给 AI 处理’。”

## 参考资料
1. [ShowHN:OSSAgentIbuilttoppedtheTerminalBenchon...](https://news.ycombinator.com/item?id=47920787)
2. [Gemini-3-Flash: My aiagentbenchmarkterminalbenchWin & 3 Fixes](https://dev.to/umair24171/gemini-3-flash-my-ai-agent-benchmark-terminalbench-win-3-fixes-44eb)
3. [Open-Source AIAgentTopsTerminalBench2.0 Leaderboard](https://aihaberleri.org/en/news/open-source-ai-agent-scores-652percent-on-terminalbench-20-in-2026-beating-gemini-and-junie-cli)
4. [Gemini3Flash— Google DeepMind](https://deepmind.google/models/gemini/flash/)
5. [r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/)
6. [OSS Agent Tops TerminalBench with Gemini-3 - PromptZone](https://www.promptzone.com/maria_gonzalez_419fd1b8/oss-agent-tops-terminalbench-with-gemini-3-3lh2)
7. [Gemini 3 — Google DeepMind](https://deepmind.google/models/gemini/)
8. [Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview)

## 事实查核摘要
- 检查项：15
- 验证项：15
- 结论：通过