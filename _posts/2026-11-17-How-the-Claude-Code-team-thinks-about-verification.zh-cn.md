---
layout: post
title: "AI完成90%的代码？Claude Code团队谈“验证”的秘密"
description: "Anthropic Claude Code团队使用AI编写和审查了90%的代码。轻松了解为什么验证比提示词更重要。"
summary: "探讨AI代理时代Claude Code团队保持代码质量的核心秘诀——“验证（Verification）”以及具体的工作方式。"
tags: [AI, ClaudeCode, 编程, 开发, Anthropic]
image: 2026-11-17-How-the-Claude-Code-team-thinks-about-verification.jpg
image_alt: "表现开发者在电脑屏幕前利用AI编程工具的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "比起单纯写好指令（提示词），让AI基于自身证据自行验证结果，才是代理时代的真正核心。"
quiz:
  - question: "在Claude Code团队中，由Claude编写和审查的代码比例大约是多少？"
    choices: ["约50%", "约90%", "约30%"]
    answer: 1
    explanation: "Claude Code团队中约90%的代码由Claude编写和审查。"
  - question: "Claude Code开发者们认为最强大的质量提升杠杆（lever）是什么？"
    choices: ["编写更精细的提示词", "让AI自行验证其工作", "限制代码长度"]
    answer: 1
    explanation: "鲍里斯·切尔尼（Boris Cherny）等开发人员一致认为，“验证（Verification）”是比提示词更强大的质量提升手段。"
  - question: "关于Claude Code团队理解复杂代码库的方式，以下表述正确的是？"
    choices: ["将整个模型记在脑海中", "需要时随时请求Claude解释特定片段以重建理解", "完全不读代码"]
    answer: 1
    explanation: "团队成员并不将整个模型记在脑海中，而是在需要时请求Claude解释特定切片，按需重建对上下文的理解。"
lang: zh-cn
ref: 2026-11-17-How-the-Claude-Code-team-thinks-about-verification
---

想象一下。清晨上班坐在电脑前，今天要完成的复杂编程任务中有90%由人工智能（AI）自动搞定。你亲自动手敲键盘编写代码的时间显著减少，迎来了仔细审查AI交付成果的日常生活。这并不是遥远未来科幻电影中的故事，而是全球知名AI企业Anthropic旗下的终端编程代理Claude Code开发团队的真实日常 [出处 1, 出处 11]。

那么，站在制造全球最强AI最前沿的开发者们，是如何稳定管理这个庞大而复杂的系统的呢？很多人单纯认为：“只要把提示词（Prompt）写得更华丽、更精致就行了。”但Claude Code团队透露的真正成功秘密完全颠覆了我们的预期。他们异口同声地表示：**“与提示词相比，验证（Verification，客观确认结果是否正确的流程）要重要得多”** [出处 3]。今天这篇文章将带大家一步步探究在人工智能主导编程的时代，他们是如何严格保持软件质量的。

---

## 为什么这很重要？

我们常想象，当AI时代来临，人类只需帅气地抛出问题便可高枕无忧。仿佛只要下达“帮我做这样一个程序”的指令，完美的成果就会瞬间诞生。但在实际业务中，尤其是构建数十万行宏大软件的现场，确认AI编写的代码是否真正正常运行、是否存在隐藏的Bug（程序缺陷或错误），才是决定整个工作成败的关键。 

如果盲目信任AI生成的代码而未经任何验证就将其应用于商业服务，导致整个系统瘫痪，会发生什么？无数客户将在瞬间遭受巨大不便，公司也将蒙受天文数字的金钱和信誉损失。因此，在AI代写代码的时代，人类与AI紧密协作，构建**“用客观证据证明结果确实正确的验证体系”**，成为决定企业生死存亡的核心要素。观察Claude Code团队如何解决这一难题，能为我们未来如何看待和使用融入日常的各种AI自主工具提供清晰的线索。

---

## 轻松理解：比提示词这一“咒语”更重要的自动阅卷机

为了便于读者理解，我们举一个日常的例子。**以提示词为中心的方法**就像去找一位名厨，嘴上长篇大论地要求“帮我做一个美味又健康的晚餐”。厨师虽然会尽力，但由于“美味健康”的标准因人而异，做出来的菜可能会偏咸或营养失衡。

相反，Claude Code团队强调的**以验证为中心的方法**就像是在菜肴旁边设立严格的“评分标准表”和“自动阅卷机”。这种方式预先制定具体的合格标准，例如“这道菜的钠浓度必须恰好在0.8%以下，烹饪时间不得超过20分钟，且必须通过烤箱温度传感器正常工作的测试”。AI根据这一标准自己烹饪，运行测试设备后，才报告菜肴已经完成。

事实上，包括Claude Code团队的鲍里斯·切尔尼（Boris Cherny）在内的主要开发人员强调：**“在Claude Code中，最强大的质量提升杠杆（lever，大幅拉升系统成果的核心支柱）是让AI自主验证其工作”** [出处 3]。 

这里还有一个更有趣的工作方式转变。Claude Code团队不向开发者逐一指示细碎的“任务（task）”，而是赋予宏观的**“目标（goal）”** [出处 2]。例如，不如下达诸如“把这个按钮的边距修改2像素并分离内部函数”这样琐碎的鼠标键盘操作指令，而是抛出“请改善这个画面的用户体验（UX），显著缩短移动端加载速度”这样宏大的目标。随后，Claude便会运转代理循环（Agent Loop，AI自主思考、执行工具并修复错误的反复自主执行过程），自主寻找所需文件，修改代码，并运行测试命令来亲自证明其成果的正确性。

另一个比喻是，处理数百万行的庞大源代码，就像试图把复杂大都市里的每一条小巷都背在脑海中一样。但Claude Code团队展现出了**“与其勉强记住整体，不如在需要时按需重建理解（rebuild understanding on demand）”**的智慧 [출처 6]。就像打开导航时只有当前经过的小巷周边被放大并清晰可见一样，他们不把整个代码装在脑子里，而是在需要修改特定部分时，实时请求Claude解释对应的代码片段以掌握上下文并推进工作 [出处 6]。

---

## 当前现状：AI编写90%的代码，以及六重防线

目前在Claude Code团队内部，惊人的是，**大约90%的代码都是由Claude编写和审查的** [出处 1, 出处 7]。人类开发者从头到尾敲击键盘逐行键入的传统开发时代已经过去，如今，扮演协调者（Orchestrator，像交响乐团指挥一样调控整体流向的角色）的角色已成为核心，负责精心调校AI编写的代码并把握方向。

那么，当AI编写了90%的代码时，系统如何能保持稳定并完美运转呢？其稳固的秘诀就在于经过周密设计的**“验证层（Verification Layer）”**。在Claude Code编写的典型代码变更历史最终提交为PR（Pull Request，开发者请求将所写代码合并到主代码库的过程）之前，必须通过多达**6个阶段的验证检查点** [出处 7]。 

这其中不仅包含开发者提交PR前经历的自我验证流程，还严丝合缝地包括每次代码变更时在服务器上自动运行的严格且必不可少的CI（Continuous Integration，持续集成，持续合并源代码变更并自动测试的系统）检查 [출처 7]。换言之，无论AI编写的代码看上去多么天衣无缝，如果无法通过这苛刻的六重自动验证关卡，就绝不可能被反映到实际服务的源代码中，这是一个极其安全的结构。

---

## 未来会怎样？

Anthropic创始人达里奥·阿莫代伊（Dario Amodei）与顶尖研究团队引领的方向以及Claude Code团队生动的洞察，未来的AI编程与代理生态系统将向以下三个核心方向进一步演进 [出处 9]：

1. **验证与自主自动化循环的高级化**：超越单纯的文本生成模型水平，AI直接运行代码、测试并自主诊断和修复错误的“代理循环”系统将成为行业的基本标准 [出处 5]。
2. **上下文极简主义（Context Minimalism）的确立**：不再一次性向AI注入大量不必要的信息而造成混乱，而是转变为挑选并精确利用关键时刻所需最少信息的最高效工作方式 [출처 5]。
3. **例行程序与自动模式（Auto Mode）的普及**：即使没有人在旁一一监督，在重复的开发循环中，AI依托坚实的安全装置（验证系统）自主工作的环境将推广至所有开发一线 [출처 5]。

归根结底，即将到来的未来开发和问题解决并不取决于“如何对AI把话说得天花乱坠”。相反，成败将取决于**“能否建立起扎实的测试与验证标准，以证明AI带回来的庞大成果是否真的值得信赖”** [出处 3]。

---

## AI视角（MindTickleBytes AI记者视角）

许多人希望AI能成为一个自动解决世上所有复杂问题的“魔盒”。但正如Anthropic Claude Code团队的生动案例所明确证明的那样，真正的生产力提升并非来自虚幻的魔法般提示词，而是源自冷酷而彻底的“验证系统”。随着AI变得越来越聪明，人类的角色正在超越单纯的程序员或监督者，进化为公正严格的“首席评审员”以及决定方向的“战略家”。这正是随着技术日趋高端，不丢失基本功与验证价值的态度变得愈发珍贵的原因。

---

## 参考资料

1. How the Claude Code team thinks about verification - https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/
2. How the Claude Code team uses Claude Code - YouTube - https://www.youtube.com/watch?v=S-sYlFiGFv8
3. Verification Beats Prompting, Boris Cherny's Top Claude Code Tip... - https://blog.vibecoder.me/verification-beats-prompting-claude-code-boris-cherny
4. Claude Code by Anthropic | AI coding agent and assistant - https://claude.com/product/claude-code
5. Claude Code's Creators Explain Agent Loops & How... | The Neuron - https://www.theneuron.ai/explainer-articles/claude-code-creators-boris-cherny-and-cat-wu-explain-how-to-use-agent-loops/
6. Critical thinking when agents do the work... | Thread Navigator - https://threadnavigator.com/thread/2117512471930167377/
7. How the Claude Code team reviews code that Claude writes - https://heybrahim.com/notes/claude-code-team-code-review.html
8. Dario Amodei: Anthropic CEO on Claude, AGI & the Future... - YouTube - https://www.youtube.com/watch?v=ugvHCXCOmm4
9. Claude (AI) - Wikipedia - https://en.wikipedia.org/wiki/Claude_(AI))
10. Claude by Anthropic | The AI for problem solvers - https://claude.com/
11. Newsroom \ Anthropic - https://www.anthropic.com/news