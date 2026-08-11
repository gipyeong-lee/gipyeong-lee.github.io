---
layout: post
title: "AI像人一样说话会更聪明吗？“拟人化”的陷阱"
description: "为什么要求AI“像人一样说话”反而可能降低其性能？让我们从专家的视角一探究竟。"
summary: "试图让AI看起来像人，会混淆用户的预期与AI的本质目的，反而可能导致性能下降。"
tags: [AI, LLM, 技术分析, 人工智能伦理]
image: 2026-08-11-Humanising-LLM-Outputs-Is-Dumb.jpg
image_alt: "人与机器人在对坐交谈的抽象数字插画"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI不是拥有人类情感的朋友，而是高效的信息处理工具。相比执着于人类式的“模仿”，更明智的做法是专注于成果的准确性和实际价值。"
quiz:
  - question: "要求AI通过诸如“我有ADHD”等策略表现得像人，这种做法隐含了什么风险？"
    choices: ["无限提高AI的处理速度", "混淆用户的预期与AI的本质目的", "自动提升AI的智能水平"]
    answer: 1
    explanation: "专家指出，这种拟人化尝试在用户的预期与AI的实际通信策略之间产生了脱节，是一种错误的路径。"
  - question: "要求AI给出过于简洁的回答时，可能会出现什么潜在问题？"
    choices: ["AI的记忆力会被重置", "AI会变得更聪明", "限制了作为AI思考过程的Token，反而可能使其变笨"]
    answer: 2
    explanation: "在LLM中，Token被用作思考单位。强行要求过于简洁会限制这种“思考空间”，反而可能导致回答质量下降。"
  - question: "评估AI成果时，最重要的因素是什么？"
    choices: ["是否使用了人类化的语气", "AI的性能及与用户需求的匹配度", "回答是否足够有趣"]
    answer: 1
    explanation: "专家强调，评估的核心不在于语气的拟人化，而在于AI能多有效地处理信息，并给出用户所期望的准确答案。"
lang: zh-cn
ref: 2026-08-11-Humanising-LLM-Outputs-Is-Dumb
---

想象一下。你让公司里最聪明的实习生写一份报告，结果这位实习生突然说：“我其实患有ADHD（注意缺陷多动障碍），能用易于理解的简单技术英语（ASD-STE100，航空业所用的限制性词汇英语）跟我沟通吗？”虽然我们可以理解实习生的个人情况，但工作的核心终究在于他写出的报告是否准确清晰。

最近，许多人工智能（AI）用户都在费尽心思让AI变得像“人”一样。在提示词（Prompt）中加入“我有ADHD”、“请使用非常拟人的语气”等条件正变得非常流行。然而，专家警告称，这种尝试可能是一种“错误的抽象”，会损害AI的本质能力。[出处 1](https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb), [出处 3](https://devtalk.com/t/humanising-llm-outputs-is-dumb/248727)

## 这为什么重要？

随着AI技术的飞速发展，我们逐渐将AI视为对话伙伴而非工具。但如果AI为了表现出“人味儿”而牺牲了原本的数据处理效率，那么在关键时刻，它可能会提供错误信息或无法解决复杂问题。将AI仅仅当作情感慰藉，还是将其作为强大的思考工具，这一问题要求我们从根本上改变看待技术的方式。[出处 4](https://cybermediacreations.com/humanising-llm-outputs-is-dumb/), [出处 5](https://avaoroi.com/general/humanising-llm-outputs-is-dumb/)

## 简单易懂：别拿走AI的“草稿纸”

我们把AI写文章的过程比作“烹饪”。基于Transformer（一种识别句子中词语间关系的AI结构）的大语言模型（LLM）就像是一位利用海量食材（数据）寻找最佳食谱的厨师。

用户向AI下单“你就是个人类”，这相当于强迫一位优秀的厨师不去烹饪，而是去表演“模仿人类”。由于把精力都放在了表演上，它发挥出本职水平——即调好味道、确认食材新鲜度——的机会就减少了。

此外，要求回答过于简短也需要警惕。在LLM中，“Token”（AI用于拆解语言以进行思考的单位）就是一种思考单位。就像做数学题时需要足够的演算步骤才能算出正确答案一样，如果强迫AI过于简洁，无异于夺走了它进行充分思考的“草稿纸空间”，从而导致模型做出更愚蠢的判断。[出处 12](https://news.ycombinator.com/item?id=47647907)

## 现状

目前，AI行业正将“评估（Evaluation）”作为核心课题，即衡量AI回答的准确性以及与用户意图的匹配度。由于AI的回答具有概率性，同一个问题每次的结果可能都不同，因此持续且一致的性能评估至关重要。[出处 6](https://cohere.com/llmu/evaluating-llm-outputs), [出处 9](https://www.databricks.com/blog/best-practices-and-methods-llm-evaluation)

尽管许多人为了获得人类化的语气而给AI设定特定的人格（Persona），但专家担心这种“拟人化”反而会干扰对AI效率和准确性的评估。我们应该正视一个事实：不是AI想看起来像人，而是我们正在为了强加一层人类化的外壳，而损害AI的效率。[出处 4](https://cybermediacreations.com/humanising-llm-outputs-is-dumb/)

## 未来趋势

未来，比起给AI披上情感人格，建立精密的验证系统来确认AI结论是否基于事实、是否存在逻辑谬误将变得更加重要。例如，在医疗或法律等要求绝对准确的领域，AI的设计将不再是模仿人类语气，而是通过一步步验证逻辑链条来输出答案。[出处 13](https://www.linkedin.com/pulse/evaluating-llm-outputs-how-know-when-ai-right-fix-vivekraj-deg2c)

我们应当从将AI视为人类替身的幻觉中醒来。尽管AI有时表现得甚至不如家猫聪明，但我们必须记住，当它与人类协作时，它是能够发挥惊人效率的优秀“思考工具”。[出处 8](https://towardsdatascience.com/llms-are-dumber-than-a-house-cat-81e7b3d63190/)

## MindTickleBytes AI记者视角

技术的进步往往让我们在对AI的“人类式温情”期望与AI能展现的“机械式精密”之间感到纠结。但请记住，就像你不会向薪资计算器或导航仪询问人生感悟一样，AI也只有在不丢失其本质性能与精密性的前提下，才能最大限度地帮助我们的生活。比起被外壳所迷惑，现在是时候专注于AI答案中名为“准确性”的核心内核了。

## 参考资料

1. [HumanisingLLMOutputsisDumb — Kuber Mehta](https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb)
2. [HumanisingLLMOutputsIsDumb | Hacker News](https://news.ycombinator.com/item?id=49243474)
3. [HumanisingLLMOutputsisDumb | Devtalk](https://devtalk.com/t/humanising-llm-outputs-is-dumb/248727)
4. [HumanisingLLMOutputsIsDumb - Cyber Media Creations](https://cybermediacreations.com/humanising-llm-outputs-is-dumb/)
5. [HumanisingLLMOutputsIsDumb - Avaoroi](https://avaoroi.com/general/humanising-llm-outputs-is-dumb/)
6. [EvaluatingOutputs](https://cohere.com/llmu/evaluating-llm-outputs)
7. [Who Validates the Validators? AligningLLM-Assisted Evaluation of...](https://blog.athina.ai/who-validates-the-validators-aligning-llm-assisted-evaluation-of-llm-outputs-with-human-preferences)
8. [LLMs Are Dumber Than a House Cat | Towards Data Science](https://towardsdatascience.com/llms-are-dumber-than-a-house-cat-81e7b3d63190/)
9. [Best Practices and Methods for LLM Evaluation | Databricks Blog](https://www.databricks.com/blog/best-practices-and-methods-llm-evaluation)
10. [My LLM's outputs got 200% better with this simple trick.](https://makingaieasy.substack.com/p/my-llms-outputs-got-200-better-with)
12. [Oh boy. Someone didn't get the memo that for LLMs, *tokens are units of thinking... | Hacker News](https://news.ycombinator.com/item?id=47647907)
13. [EvaluatingLLMOutputs: How to Know When AI is "Right" and How to...](https://www.linkedin.com/pulse/evaluating-llm-outputs-how-know-when-ai-right-fix-vivekraj-deg2c)