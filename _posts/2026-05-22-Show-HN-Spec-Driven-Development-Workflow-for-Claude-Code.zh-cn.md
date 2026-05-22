---
layout: post
title: "让 AI 写代码结果一团糟？从编写‘设计蓝图 (Spec)’开始，情况将大不相同"
description: "探讨如何正确使用 AI 编程助手 Claude Code，了解规范驱动开发 (SDD) 工作流。"
summary: "摆脱仅仅通过对话下达编程指令的方式，先编写清晰的设计蓝图并细化任务的‘规范驱动开发 (SDD)’正成为 AI 编程的新标准。"
tags: [AI编程, Claude Code, 规范驱动开发, 软件开发, AI生产力]
image: 2026-05-22-Show-HN-Spec-Driven-Development-Workflow-for-Claude-Code.jpg
image_alt: "一张柔和的插画，描绘了一位建筑师展开复杂的蓝图并与机械臂协作的场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人工智能不是魔法棒，而是优秀的员工。要让员工发挥出实力，我们必须先提供清晰的蓝图，明确‘想要什么’，这再次印证了这一朴素的真理。"
quiz:
  - question: "文章中解释的‘规范驱动开发 (SDD)’核心原则之一，为了防止 AI 陷入混乱，在每个阶段都会执行的操作是什么？"
    choices: ["清除 AI 的上下文（记忆）", "购买性能更高的电脑", "将代码编写速度提高 2 倍"]
    answer: 0
    explanation: "在 SDD 工作流中，会在步骤之间清除 AI 之前的对话语境（上下文），使 AI 能够完全专注于特定的子任务。"
  - question: "文章中提到的，不经计划直接要求 AI 编写代码的传统方式叫什么？"
    choices: ["氛围感编程 (Vibe coding)", "规范驱动开发 (SDD)", "结对编程 (Pair programming)"]
    answer: 0
    explanation: "在没有任何说明书的情况下，根据心情或感觉下达交互式指令的方式被称为‘氛围感编程 (Vibe coding)’。"
  - question: "开发者 Pimzino 强调在规范驱动开发中绝对不可妥协 (non-negotiable) 的必要过程是什么？"
    choices: ["计划阶段与实现阶段的分离", "无条件仅使用 Python 语言", "忽略 AI 的错误"]
    answer: 0
    explanation: "Pimzino 强调，明确划分设计（计划）阶段和编写实际代码的实现阶段是成功的 AI 编程的必要条件。"
lang: zh-cn
ref: 2026-05-22-Show-HN-Spec-Driven-Development-Workflow-for-Claude-Code
---

想象一下，为了建造你梦想中的乡村别墅，你雇佣了资深的建筑师和施工队。但到了现场你却这样说：“那个，请帮我盖一栋住起来舒服又漂亮的两层小楼。厨房要宽敞一点，采光要好。你是专家，看着办吧！”

结果会怎样？也许你会看到马桶孤零零地放在客厅中央，或者上二楼的楼梯被天花板堵住，最终建成一栋荒谬的房子。

到目前为止，我们在使用人工智能 (AI) 编程助手时，一直固守着这种方式。我们在对话框中向 ChatGPT 或 Claude 随口扔一句“帮我做一个有这种功能的 App”，然后期待 AI 像变魔术一样瞬间吐出完美的程序。专家们将这种没有明确计划或规格说明书，随心所欲下达指令的方式称为 **‘氛围感编程 (Vibe coding)’** [[From VibeCodingto Shipping: MySpec-DrivenWorkflow... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code), [Spec-Driven Development with Claude Code: Build It Right](https://solguruz.com/blog/spec-driven-development-with-claude-code/)]。

然而，最近在软件开发者之间，处理‘Claude Code’（专门用于编程的 AI Agent 工具）的一种全新方法成为了热门话题。与其盲目地让 AI 编写代码，不如先让它编写一份详细的‘设计蓝图 (Spec)’，这就是 **规范驱动开发 (Spec-Driven Development，以下简称 SDD)** [[Claude Code Spec-Driven Development Implementation Guide](https://github.com/papaoloba/spec-based-claude-code)]。

## 为什么这很重要？ (Why It Matters)

当听说 AI 能完成所有编程工作时，我们曾欢呼工作速度将瞬间提升数十倍。但现实并非如此。只要项目稍微复杂一点，与 AI 的协作很快就会变成沉重的负担 (cumbersome) [[ClaudeCode:Spec-DrivenDevelopment(SDD)](https://mifkata.com/blog/2026/01/claude-code-spec-driven-development/)]。这是因为 AI 会忘记前后语境，或者出现修复了一处却弄坏了另一处的情况。

事实上，一位一线开发者透露，在引入 AI 助手并仅通过对话方式下达指令时，生产力反而下降了 19%，经历了‘生产力放缓 (slowdown)’ [[From VibeCodingto Shipping: MySpec-DrivenWorkflow... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)]。因为人们不得不花费更多时间去逐一找出乱七八糟的代码并进行收拾和调试（错误修正）。

但是，在将工作方式转变为‘规范驱动开发 (SDD)’后，这 19% 的损失奇迹般地转化为了实质性的生产力提升 (real lift) [[From VibeCodingto Shipping: MySpec-DrivenWorkflow... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)]。我们对 AI 的期望不是玩具，而是达到实际客户可用水平 (production-ready) 的稳固程序。为此，保持专家级开发实践 (professional software development practices) 的 SDD 是必不可少的 [[Claude Code Spec-Driven Development Implementation Guide](https://github.com/papaoloba/spec-based-claude-code)]。

## 易于理解的解释 (The Explainer)

规范驱动开发 (SDD) 的核心是将庞大的任务从两个维度 (two dimensions) 进行精准拆分 [[Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)]。

**1. 彻底的前期调查 (Research)**
就像盖房前要检查土地状况一样，投入多个 AI Agent 对当前系统的状态和问题进行立体分析 [[Spec-DrivenDevelopmentwithClaudeCodein Action | alexop.dev](https://alexop.dev/posts/spec-driven-development-claude-code-in-action/)]。

**2. 编写坚实的设计蓝图 (Spec Creation)**
这是最关键的阶段。基于调查结果，创建一份包含需求 (requirements) 和系统设计的规格说明书文档 [[Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)]。这成为了人类与 AI 之间一份不可动摇的书面规格合同 (written spec contracts) [[Spec-DrivenDevelopmentwithClaudeCode](https://greeto.me/blog/spec-driven-development-claude-code-in-action)]。

**3. 任务碎片化 (Task Decomposition)**
即使是再聪明的 AI，也无法一次性完成复杂的系统。将整个任务拆分成非常小的子任务 (subtasks) [[Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)]。

**4. 分步实现与验证 (Implementation & Verification)**
按顺序一个一个执行拆分后的任务并编写代码。此时不会一次性保存，而是采用以有意义的最小单位保存的原子化提交 (atomic commits) 方式，以提高安全性 [[Spec-DrivenDevelopmentwithClaudeCode](https://greeto.me/blog/spec-driven-development-claude-code-in-action)]。

**举个例子：**
在会议室的白板上写下各种想法并结束了讨论。现在需要具体集中精力处理‘窗户设计’，但如果白板上还留着‘屋顶颜色’或‘管道位置’之类的涂鸦，会怎么样呢？工作人员难免会感到困惑。

因此，在 SDD 中，原则上在每个阶段结束时都要 **‘完全清除 AI 的上下文（记忆语境）(clear context)’** [[Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)]。让大脑变为空白，只给它重新塞入刚刚完成的‘蓝图’和‘当下的目标’。这样，AI 就不会陷入幻觉（Hallucination，即把虚假信息说得像真的一样），而是能敏锐地专注于眼前的任务。

## 现状如何？ (Where We Stand)

随着这种方法的效果得到证实，全球开发者纷纷推出了将这一过程自动化的工具。

*   **ShipSpec:** 开发者无需亲自动手写蓝图，AI 会分析项目并自动生成包含 3 个文档文件的蓝图 [[ShowHN:SpecDrivenDevelopmentPluginforClaudeCode](https://news.ycombinator.com/item?id=46591238)]。
*   **sddw:** 直接让负责编程的 AI 本人编写自己的任务蓝图。帮助它自主制定计划并以小单位（原子任务）处理工作 [[Spec-drivendevelopmentworkflow- how to get production-ready...](https://www.linkedin.com/pulse/spec-driven-development-workflow-how-get-code-from-ai-makarevych-xolxf)]。
*   **claude-code-spec-workflow:** 由开发者 Pimzino 公开的这个包在 GitHub 上获得了超过 3,700 颗星，受到了爆发性的欢迎 [[GitHub - Pimzino/claude-code-spec-workflow: Automatedworkflows...](https://github.com/Pimzino/claude-code-spec-workflow)]。Pimzino 强调：“将计划环节与实现环节分开是不可妥协 (non-negotiable) 的必要条件” [[Spec-Driven Development with Claude Code | Build This Now](https://www.buildthisnow.com/blog/guide/mechanics/spec-driven-development)]。

## 未来会怎样？ (What's Next)

未来的开发者将不再在电脑前通宵达旦，而是口述自己的想法。然后 AI 会分析这些语音，编写出完美的‘设计蓝图 (Spec)’，并自主编写代码，最后完成测试。事实上，全球企业 Notion 已经在其内部构建了这种方式的 AI 工作流 [[Spec-drivendevelopment: The AI engineeringworkflowat Notion](https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering)]。

最终，人工智能正在超越单纯接受指令的打字机，进化为能够自主计划和验证的自我开发 AI 系统 (Self-Developing AI System) [[A Config-Driven Way to BuildSpec-DrivenWorkflowsforClaude...](https://www.linkedin.com/pulse/config-driven-way-build-spec-driven-workflows-claude-code-makarevych-qjmwf)]。我们正在告别冲动的‘氛围感编程’，迎来作为一个描绘宏图的‘总建筑师’，指挥 AI‘建筑机器人’军团的时代。

## AI 的观点
人工智能不是魔法棒，而是优秀的员工。要让员工发挥出实力，我们必须先提供清晰的蓝图，明确‘想要什么’，这再次印证了这一朴素的真理。

## 参考资料
1. [在行动中通过 Claude Code 进行规范驱动开发 | alexop.dev](https://alexop.dev/posts/spec-driven-development-claude-code-in-action/)
2. [GitHub - Pimzino/claude-code-spec-workflow: 自动化工作流...](https://github.com/Pimzino/claude-code-spec-workflow)
3. [一种配置驱动的方法来构建 Claude 的规范驱动工作流...](https://www.linkedin.com/pulse/config-driven-way-build-spec-driven-workflows-claude-code-makarevych-qjmwf)
4. [从氛围感编程到出货：我的规范驱动工作流... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)
5. [使用 Claude Code 进行规范驱动开发](https://greeto.me/blog/spec-driven-development-claude-code-in-action)
6. [Claude Code：规范驱动开发 (SDD)](https://mifkata.com/blog/2026/01/claude-code-spec-driven-development/)
7. [Claude Code 规范驱动开发实现指南](https://github.com/papaoloba/spec-based-claude-code)
8. [使用 Claude Code 进行规范驱动开发：正确构建](https://solguruz.com/blog/spec-driven-development-with-claude-code/)
9. [使用 Claude Code 进行规范驱动开发 | Build This Now](https://www.buildthisnow.com/blog/guide/mechanics/spec-driven-development)
10. [使用 Claude Code 进行规范驱动开发：引导教程](https://www.datacamp.com/tutorial/spec-driven-development-with-claude-code)
11. [Show HN: Claude Code 的规范驱动开发工作流](https://news.ycombinator.com/item?id=48231575)
12. [Claude Code 规范工作流指南 (2026) | ClaudHQ](https://claudhq.com/claude-code-spec-workflow-guide/)
13. [规范驱动开发工作流 - 如何获得生产就绪的...](https://www.linkedin.com/pulse/spec-driven-development-workflow-how-get-code-from-ai-makarevych-xolxf)
14. [ClaudeEngineer 简直疯了... 升级你的 Claude Code 工作流](https://www.youtube.com/watch?v=6Rg5M69bMgQ)
15. [Show HN: Claude Code 的规范驱动开发插件](https://news.ycombinator.com/item?id=46591238)
16. [规范驱动开发：Notion 的 AI 工程工作流](https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering)