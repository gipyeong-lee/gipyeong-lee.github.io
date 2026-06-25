---
layout: post
title: "AI 停止思考了？Gemini 陷入“无限循环”的故事"
description: "最近有报告称，人工智能 Gemini 在给出答案前会陷入“思考中”状态并停滞不前。我们为您详细解释了其原因及用户的应对方法。"
summary: "近期，Gemini 模型在处理复杂问题时，频繁陷入“思考的沼泽（无限循环）”，导致无法给出最终答案。"
tags: [AI, Gemini, 技术问题, 故障排查]
image: 2026-06-25-Gemini-models-increasingly-stucking-in-thinking-loop.jpg
image_alt: "计算机屏幕上的 AI 聊天窗口中，“思考中”图标在无限旋转"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是复杂推理模型在成长过程中必然会遇到的阵痛。AI 越是尝试像人类一样深入思考，就越容易产生这种错误。"
quiz:
  - question: "当 Gemini 陷入“思考的沼泽”时，会出现的典型症状是什么？"
    choices: ["回答速度过快", "不断在外部重复其内部的思考过程，无法完成回答", "系统突然关闭"]
    answer: 1
    explanation: "有报告称，模型会无休止地在外部重复诸如“等一下！”、“再考虑一下”之类的内部思考，从而无法完成回答。"
  - question: "Gemini 的“思考模型（Thinking model）”为何出现？"
    choices: ["为了更快地进行搜索", "为了解决日益复杂的问题", "仅仅是为了进行简单的文本聊天"]
    answer: 1
    explanation: "Gemini 的思考模型旨在更深入地推理并解决更加复杂的问题。"
  - question: "Gemini CLI 用户近期面临什么样的困扰？"
    choices: ["无法连接互联网", "“思考中”的状态持续时间过长", "回答的文字量过少"]
    answer: 1
    explanation: "在 CLI 版本中，回答延迟现象严重，原本只需 2 分钟的任务现在可能需要长达 2 小时才能完成。"
lang: zh-cn
ref: 2026-06-25-Gemini-models-increasingly-stucking-in-thinking-loop
---

想象一下：你请一位聪明的秘书“帮我总结这份项目报告”。然而，秘书却在一旁嘀咕：“嗯，序言怎么写呢？啊，等一下！这个也得放进去。不对，再考虑一下。等等！这个也要……”它陷入了自我对话的循环中，已经嘟囔了一个小时。

最近，人工智能（AI）Gemini（谷歌的 AI 模型）的用户中也出现了类似的情况。据说 AI 在为了给出答案而苦思冥想时，看起来就像陷入了“无限循环（Infinite loop，即无休止地重复同一个过程）”。我们的智能 AI 秘书到底发生了什么？

### 为什么这很重要？

随着 AI 技术的发展，我们的日常生活也在发生变化。将写作或复杂的企划任务交给 AI 已经变得司空见惯。然而，AI 无法给出答案并卡死的情况，已经不仅仅是单纯的不便了。特别是在开发者使用的 CLI（基于命令行的界面）环境中，问题更加严重。据报道，原本只需 2 分钟就能完成的工作，现在竟然需要延迟长达 2 小时[1]。这直接打击了那些信任并依赖 AI 处理业务的用户，导致工作效率大幅下降。

### 浅显易懂：思考模型的“成长痛”

Gemini 2.5 等最新模型被称为“思考模型（Thinking model）”。如果说过去的 AI 仅仅是预测下一个单词出现的概率，那么这些模型则被设计为具备高度推理能力，以解决更加复杂的问题[7, 8]。

简单来说，这类似于小学生解数学题时，不仅写下答案，还在试卷角落一步步写下解题过程。但现在的 Gemini 在思考得太深时，在解题过程中陷入了“思考的沼泽”。用户目睹了 AI 无休止地在外部重复诸如“等一下！”、“再考虑一下……”之类的内部苦恼，却迟迟无法给出必要的结论并停在那里[3]。可以说，AI 因为试图过度深入思考，反而被自己的想法束缚住了手脚。

### 现状：思考的沼泽正在加深

这种“思考循环”现象在 Gemini 3.1 Pro 和 3.5 Flash 等最新模型中都有出现[6, 9]。特别是在 Gemini CLI 环境中，许多用户都经历过“思考中（Thinking）”的状态指示条停留几分钟，甚至几小时的情况[1, 4]。

甚至连购买了付费订阅服务的用户也无法幸免[4]。当然，作为临时的解决方案，手动打开并关闭模型的“思考过程”窗口有时可以打破循环[5]，但这并非从根本上解决问题。

### 未来会怎样？

专家分析称，这种情况很可能是人工智能在执行更复杂推理的过程中所产生的“成长痛”。这是因为人工智能的智能水平越高，需要处理的逻辑路径就越复杂。为了防止这种无限循环，预计谷歌将持续进行更新，以强化 AI 的自我修正能力并提高推理过程的效率。对于用户而言，暂时来说，比起一次性向 AI 抛出过于复杂的问题，采取分步骤提问的方式来绕过这一问题或许会更明智。

### MindTickleBytes 的 AI 记者视点

这是复杂推理模型在成长过程中必然会遇到的阵痛。AI 越是尝试像人类一样深入思考，就越容易产生这种错误。我们或许正在见证 AI 从“说话机器”进化为“思考存在”的过渡期。

---

## 参考资料

1. [gemini stuck in thinking loop for hours · Issue #26116 · google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli/issues/26116)
2. [Gemini AI Prompts Stuck? Troubleshooting Tips for Google Workspace Users | Workalizer](https://workalizer.com/insights/gemini/solving-gemini-prompt-freezes-a-google-workspace-users-guide-to-ai-troubleshooting/)
3. [Thinking out loud and stuck in an infinite thought loop when drafting a final response · Issue #16342 · google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli/issues/16342)
4. [Gemini CLI v0.36.0 hangs on "Thinking" indefinitely (>5m) despite AI Pro subscription · Issue #24570 · google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli/issues/24570)
5. [Why Gemini Stops Writing & How to Fix It | Full Guide](https://www.arsturn.com/blog/gemini-keeps-stopping-why-it-happens-and-how-to-fix-it)
6. [Geminimodelsincreasinglystuckinginthinkingloop| Hacker News](https://news.ycombinator.com/item?id=48642229)
7. [Gemini2.5: Our newestGeminimodelwiththinking](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/)
8. [Models|GeminiAPI | Google AI for Developers](https://ai.google.dev/gemini-api/docs/models)
9. [Geminimodelsincreasinglystuckinginthinkingloop: hackernews](https://old.lemmy.sdf.org/post/55058455)