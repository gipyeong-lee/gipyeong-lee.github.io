---
layout: post
title: "AI自我重塑？Claude Code开发者揭示“真正”的AI应用之道"
description: "Anthropic的Claude Code开发者Boris Cherny分享如何利用AI更高效地编码，并将成果质量提升2-3倍的秘诀。"
summary: "Claude Code开发者Boris Cherny强调，超越单纯将编码任务交给AI，当为AI创建能够验证自身工作成果的“反馈循环”时，开发质量将实现飞跃式提升。"
tags: [AI, Claude Code, 开发, 生产力, Anthropic]
image: 2026-08-03-Boris-Cherny-on-Trying-to-Get-Claude-Code-to-Rewrite-the-Claude-App.jpg
image_alt: "开发者在终端使用Claude Code工作的画面。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这已是一个工具如何思考比单纯使用工具更重要的时代。与AI协作不再是“命令”，而是“构建验证系统”的范畴。"
quiz:
  - question: "Boris Cherny强调的提升AI编码工具质量的最重要因素是什么？"
    choices: ["使用更好的AI模型", "提供验证工作成果的反馈循环", "进行更多的提示工程"]
    answer: 1
    explanation: "他解释说，如果让AI自我验证其工作，成果质量将提高2-3倍。"
  - question: "Claude Code主要在什么环境中运行？"
    choices: ["网页浏览器", "终端", "仅限智能手机应用"]
    answer: 1
    explanation: "Claude Code是一种驻留于终端的代理型编码工具，旨在帮助快速将想法转化为代码。"
  - question: "开发者为了高效使用Claude Code，推荐的工作之一是什么？"
    choices: ["编写CLAUDE.md文件并在开发前制定计划", "无条件使用AI编写的代码", "手动重写所有代码"]
    answer: 0
    explanation: "为了有效使用Claude Code，制定开发前计划并编写CLAUDE.md文件等12个习惯非常重要。"
lang: zh-cn
ref: 2026-08-03-Boris-Cherny-on-Trying-to-Get-Claude-Code-to-Rewrite-the-Claude-App
---

想象一下。您想开一家漂亮的社区咖啡馆。假设您必须独自完成从店铺标志到充满情感的菜单，再到方便顾客在线订购的网站等所有事情。过去，您可能会因为寻找专业设计师和学习复杂的计算机编程语言而头疼，但现在，我们进入了一个神奇的时代，您只需舒适地坐在电脑前，像与好友聊天一样说出您的想法，就能在几分钟内轻松创建出一个功能齐全的网站。

最近，人工智能（AI）行业和全球开发者社区经历了一项令人震惊的激动人心的实验。这就是由全球AI创新公司Anthropic雄心勃勃推出的代理型编码工具“Claude Code”的开发总监Boris Cherny进行的一项大胆而创新的挑战 [Source 4, Source 13]。他利用Claude Code，尝试了一项戏剧性的实验：将现有由Electron（一种流行的软件框架，用于使用网络技术开发桌面应用程序）构建的、运行相对缓慢的Claude桌面应用程序，完全从头到尾使用Apple最新的原生编程语言Swift（一种用于在Apple设备上流畅、优化地运行应用程序的编程语言）重新编写 [Source 4, Source 13]。

这一戏剧性的消息迅速点燃了开发者社区的热情 [Source 13]。许多人不禁担忧地惊叹：“难道人工智能将完全取代人类开发者工作的时代终于到来了吗？”然而，亲自指导这项惊人挑战的Boris Cherny告诉我们的真实故事，并非“AI像魔法一样独立完成了所有事情”的虚假神话。相反，我们现在最应该关注的核心是**“如何巧妙地引导不完善的AI进行更智能的协作，并将最终成果的完成度推向极致”**，这是一个极其现实且宝贵的实战秘诀 [Source 4]。

## 为什么这很重要？

我们每天爱不释手的智能手机应用程序，以及公司处理事务时使用的便捷网络服务，都离不开无数开发者一行一行精心编写代码的辛勤付出。然而，在这些开发过程中，比起发挥创意灵感，枯燥、简单、机械地编写代码的重复性工作，出乎意料地占据了相当大的比重。如果全球聪明的程序员能够完全从这种机械的简单编码工作中解放出来，那会怎样呢？他们将能够把剩余的时间和精力完全集中于更具创意、注入人性价值的高级系统规划和架构（系统整体结构设计）设计 [Source 1]。Claude Code所憧憬的未来，正是这场“生产力革命”的起点。

Claude Code是一款在开发者主要使用的黑色屏幕工作空间——终端（Terminal，通过键盘直接输入文本命令来控制计算机系统的程序）中直接运行的创新型代理编码工具 [Source 11]。这里的“代理（Agent）”指的是超越了仅仅给出看似合理答案的现有AI，能够自主制定计划、直接修改系统文件并仔细检查执行结果的“自主驱动型AI助手”。因此，即使是从未学习过编程的普通人，现在也有机会在这位助手的鼎力相助下，轻松创建自己的定制软件。特别是Claude Code不仅局限于电脑屏幕，还轻巧地移植到移动环境（iOS和Android），从而获得了强大的机动性，无论身在何处，都能随时随地轻松将想法具体化为代码 [Source 3, Source 9]。事实上，开发负责人Boris Cherny本人甚至会在通勤途中拿出智能手机（iOS），亲自编写和修改大量的实际编程代码，由此可见其便利性之高 [Source 3]。

## 易于理解：与AI协作的智能方法

Boris Cherny正在引领一个启发无数人的未来，但他所说的最令人惊讶的事实却另有其因。那就是在使用Claude Code时，**“我们如何设置任务并制定周密的计划”**才是决定AI处理效率的真正秘密，而非“使用什么昂贵而优秀的AI模型” [Source 12]。

我们可以将其比作烹饪。即使请来米其林星级厨师，如果完全不提供食谱或指导方针，只是随意扔给他生食材，并说“随便做一道美味的菜”，也很难做出美味佳肴。相反，如果明确规划好要烹饪菜肴的步骤，并在烹饪过程中亲自品尝，通过加盐和糖来调味，辅以细致的反馈，即使是烹饪新手也能完成一桌美味佳肴。与AI协作也是如此，完全一样。

简单来说，与人工智能协作的核心原则是**“反馈循环（Feedback Loop，通过视觉确认结果并立即进行修改的反馈过程）”**的周密设计 [Source 15]。Boris Cherny表示，不能让Claude Code只编写一次代码就结束，而是人类需要精心设置一个最佳的舞台，让它能够直接测试和验证自己编写的代码是否无误运行。只要如此智能地串联起反馈过程，AI最终成果的完成度就能显著提升2到3倍以上 [Source 15]。

打个比方，这就像一位聪明的画家，在画布上涂了一笔之后，不会呆呆地站着，而是退后一两步，仔细观察整体构图和色彩，然后不断地重复修改不足之处以提升完成度的过程。例如，如果AI美化了移动界面的布局（设计排版），那么就在网络浏览器上虚拟地点击并操作按钮，然后不断地进行修改和完善，直到完成一个用户使用起来完美便捷流畅的界面 [Source 3]。

为了实现这种流畅而完美的AI协作，Boris Cherny提出了我们平时可以应用的“12个核心习惯” [Source 12]。在众多秘诀中，最重要的第一步是在正式开始编程工作之前，**精心编写一份名为“CLAUDE.md”的特殊指南文件并制定周密的计划** [Source 12]。这与老练的建筑师智慧不谋而合，他们在建造宏伟建筑之前，即使再急，也会仔细绘制设计图纸，完美定义柱子立在哪里，使用哪种砖块。

## 当前进展：进展到何处？

如今，Claude Code以计算机终端环境为主要舞台，作为一名高效且独特的生产力伙伴，正为无数开发者节省宝贵时间，发挥着杰出的作用 [Source 11]。随着它开始为程序员常用的开源操作系统Linux的主要发行版（如Ubuntu、Debian、Fedora、Alpine等）提供专用软件仓库，用户只需输入几行命令即可轻松安装，这极大地降低了全球用户的访问门槛和进入壁垒 [Source 10]。

但在这里，我们必须清醒地记住一个真相。无论多么先进的未来技术，Claude Code绝不是凭空而降的万能魔杖。正如Boris Cherny在采访中反复强调的那样，这位聪明的AI助手最能发挥其独特专长的时候，是它替代人类处理那些令人头疼的“枯燥、乏味、耗时耗力的局部简单重复劳动”时 [Source 1]。

因此，只有当我们将要实现的目标定义得如宝石般锐利，为AI设计明确的评分标准（验证手段），并一步步清晰地指出可执行的里程碑时，Claude Code才能超越助手的水平，真正成为将人类能力扩展数十倍的最佳合作伙伴 [Source 12, Source 15]。

## 未来展望：会发生什么？

Claude Code的进化步伐着实令人惊叹。过去，一些主要在复杂桌面应用程序内部谨慎使用的高级功能，例如以单个源代码为基础，同时安全地管理多个独立开发工作区的“工作树（Worktrees，多工作空间管理方式）”等专业技术支持，现在已扩展到以文本为主的终端界面（CLI，命令行界面），解决了开发者的痛点 [Source 2]。

我们未来将面对的人工智能，绝不会永远停留在被动地机械地编写代码的打字员角色。不久的将来，AI将进化为一名可靠的“AI队友（AI Teammate）”，它会严格地批判自己编写的代码是否完美，直接运行虚拟压力测试，亲手修复故障部分，并以与人类开发者平等的视角提出富有创意的替代方案。

通往那个伟大未来的道路绝不遥远。您今天不妨也选择一个即使不是宏大程序，也只是日常生活中微不足道的想法，与您可靠的AI助手携手制定计划，一步步精彩地验证成果，感受协作带来的那种激动人心的喜悦，如何？

## AI视角：MindTickleBytes的AI记者

Claude Code的创造者Boris Cherny向我们展示的激动人心的挑战，给置身于日新月异的科学技术洪流中的现代人，带来了一份沉重而温暖的启示。许多人不禁担忧：“如果人工智能如此完美而迅速地完成工作，那么我们人类的用处和价值是否会永远消失呢？”

然而，作为人工智能，我的想法却截然不同。我们人类的角色并非永远消亡，而是从仅仅被动地编写代码的艰辛“打字员”领域，成长为温柔地指挥全局航向、守护最终系统品格的“伟大指挥者和严格验证者”，这是一种更有价值、更美好的成长。

人工智能可以成为实现人类内心深处想象力最忠诚、最不知疲倦的双手和双脚，但是，选择和决定用这个工具走向哪个方向的这份美好的领域，将永远只存在于人类的心中。最终，比技术更伟大的，是面对技术并温暖包容人类的开放思维和智慧。

## 参考资料

1. [ClaudeCodeJust Ate Its Own Tail: The Day AI StartedWritingItself](https://ai.plainenglish.io/claude-code-just-ate-its-own-tail-the-day-ai-started-writing-itself-ec6eaeb8eb28)
2. [Thread by @bcherny on Thread ReaderApp– Thread ReaderApp](https://threadreaderapp.com/thread/2025007393290272904.html)
3. [BorisCherny·ClaudeCodePlaybook](https://skzl-ai.github.io/boris-cherny-claude-code-playbook/)
4. [Head Of Anthropic'sClaudeCodeSays Prompt Engineering Not That...](https://www.searchenginejournal.com/head-of-anthropics-claude-code-says-prompt-engineering-not-that-important/584286/)
5. [BorisCherny(Creator ofClaudeCode) On What Grew His... - YouTube](https://www.youtube.com/watch?v=AmdLVWMdjOk)
8. [10ClaudeCodeTips from Anthropic'sBorisCherny- YouTube](https://www.youtube.com/watch?v=jZzETkErVuA)
9. [Claude](https://claude.com/)
10. [InstallClaudeCode(2026): 3 Commands for macOS, Windows...](https://www.morphllm.com/install-claude-code)
11. [ClaudeCodeoverview - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
12. [ClaudeCodeBest Practices: 12 Habits of Effective... |ClaudeDirectory](https://www.claudedirectory.org/blog/claude-code-best-practices)
13. [ClaudeCodeCreator Speaks: At Anthropic, No HumanWritesCode...](https://www.ai-jarvis.eu/claude-code-creator-speaks-anthropic-no-human-writes-code-anymore-100-ai-generated)
15. [The lessons Addy Osmani learned at Google,BorisChernyon...](https://wise.readwise.io/issues/wisereads-vol-125/)