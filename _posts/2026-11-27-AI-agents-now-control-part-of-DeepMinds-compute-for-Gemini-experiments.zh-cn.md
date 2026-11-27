---
layout: post
title: "AI自主实验时代：谷歌DeepMind将部分Gemini计算资源交由AI代理掌管"
description: "谷歌DeepMind已将部分计算资源控制权转交给AI代理，用于开发下一代Gemini模型。本文探讨AI自主进行科学实验的时代意义及其安全防范措施。"
summary: "谷歌DeepMind为下一代Gemini模型实验，将部分自主计算资源委托给了AI代理。不过, 完全的自我迭代仍显遥远, 且为便于人类监督, DeepMind保留了不奖励内部思维链的安全防范机制。"
tags: [AI, 谷歌DeepMind, Gemini, AI代理, 技术动态]
image: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments.jpg
image_alt: "一幅表现AI系统在实验室电脑屏幕前自主分析计算数据的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI自主设计并执行实验, 是从工具向同伴的巨大转变。只要保持透明思维链验证这一安全防范措施, 科学发现的速度将超越想象。"
quiz:
  - question: "谷歌DeepMind交给了AI代理什么权限？"
    choices: ["公司人事招聘权限", "用于下一代Gemini实验的部分计算资源", "谷歌搜索引擎源代码修改权限"]
    answer: 1
    explanation: "谷歌DeepMind允许AI代理自主控制部分计算预算（compute budget）, 用于下一代Gemini模型的开发实验。"
  - question: "在AI训练过程中, DeepMind故意不给予奖励的是什么？"
    choices: ["代码编写速度", "内部思维链（Chain of Thought）", "服务器电量消耗"]
    answer: 1
    explanation: "DeepMind在训练中故意不奖励AI的内部思维链（Chain of Thought）, 使AI意图以未经修改的自然语言保留, 以便人类在执行前进行审查。"
  - question: "DeepMind研究副总裁科赖·卡夫库奥格卢（Koray Kavukcuoglu）强调的当前AI状态是什么？"
    choices: ["递归自我改进（Recursive Self-Improvement）仍遥遥无期", "AI已经完全取代了人类研究员", "不需要人类介入的自主研究时代已经开启"]
    answer: 0
    explanation: "研究副总裁科赖·卡夫库奥格卢强调, 尽管AI开始控制实验计算, 但实现无限自我升级的递归自我改进（RSI）阶段仍是遥远的未来。"
lang: zh-cn
ref: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments
---

想象一下, 您是一家庞大研究机构的总负责人, 在夜里将实验室超级计算机的部分使用权限交给了人工智能助手。当您早晨上班时, 却发现该人工智能不仅提出了连人类研究员都未曾想到的新颖假设, 还通过整夜数千次的虚拟实验, 将具有实际意义的成果整洁地整理好了。听起来像是小说里的故事吗？然而, 在谷歌DeepMind的实验室里, 类似的事情正在切实发生。

## AI亲手掌握实验室钥匙

近日, 谷歌DeepMind为下一代Gemini（谷歌核心的大型语言模型系列, 能够同时理解文本、图像、音频等多种形态的数据 [来源：维基百科](https://en.wikipedia.org/wiki/Gemini_(language_model))）模型的实验, 允许**AI代理（AI Agent, 指能够自主判断并执行目标的自主型人工智能程序）**自主控制实验室的核心资源——部分计算预算（compute budget）([AI agents now control part of DeepMind's compute for Gemini experiments](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/))。 

这一消息由谷歌DeepMind研究副总裁（VP of Research）兼Gemini开发负责人科赖·卡夫库奥格卢（Koray Kavukcuoglu）在官方播客《Google DeepMind: The Podcast》第35期中首次披露, 从而公之于世([DeepMind Agents Control Part of Gemini Training Compute](https://explainx.ai/blog/google-deepmind-gemini-agents-training-compute-koray-kavukcuoglu-november-2026))。从单纯回答问题的水平跃升为直接策划实验、分配计算的主体, 这一转变吸引了整个科技界的目光。

---

## 为什么这很重要？

这则新闻对于我们普通人的日常生活意味着什么？其核心在于**“研究与技术发展的速度开始脱离人类的时间表”**。 

过去, 在开发新的AI模型或发掘新材料时, 人类科学家必须亲自提出假设、在计算机中输入指令并等待结果。这个过程充满了耗费大量时间和资金的枯燥重复工作。然而, 当AI代理直接掌控计算资源并主导实验时, 人类发现新知识和创新技术的速度将会快到超乎想象。

事实上, 谷歌DeepMind通过此类自主代理系统（如Co-Scientist系统）已经取得了巨大的成果。从新材料合成到医疗AI架构的自主开发, 已经在多个科学领域成功导出了经实验验证的成果([Google Deepmind's AI Co-Scientist now plans experiments, runs ...](https://the-decoder.com/google-deepminds-ai-co-scientist-now-plans-experiments-runs-lab-equipment-and-writes-scientific-papers/)).甚至有AI代理在人类研究员的监督下, 以比传统方式快高达1,600倍的速度发现了旧版RSA加密算法漏洞的技术([Google DeepMind finds 1,600x faster way to expose encryption flaws](https://interestingengineering.com/ai-robotics/google-deepmind-agents-expose-older-encryption-flaws)). 

也就是说, 此举意味着这些实验性成功不仅限于单次事件, 而是已深度融入谷歌核心AI模型Gemini整个开发流程的标准化运营方式中。

---

## 通俗易懂的比喻：就像给“超级实习生”发了公司信用卡

为了方便大家理解这个复杂的局面, 我们举一个日常的例子。 

假设您招了一位能力极强但还不是正式员工的“超级实习生”。在此之前, 这位实习生只负责前辈交办的简单文档处理或资料搜集工作。但公司负责人做出了决定, 赋予了该实习生权限：**“我给你公司信用卡的部分额度, 你可以根据自己认为的需求, 在夜里尽情开展市场调查项目。”**

实习生（AI代理）在给定的预算（计算资源）范围内, 自主决定要了解的主题, 通宵运行计算机分析数据后, 在早晨提交报告。这正是DeepMind此次在Gemini实验中所尝试的事情。

然而, 这里产生了一个重要疑问：“当实习生开始自主行使权限时, 它会不会脱离控制, 随心所欲地暴走呢？”

DeepMind的研究人员准确洞察到了这一点, 并准备了一道非常独特的安全防范措施。他们决定在训练过程中, 刻意不奖励人工智能内部思考的过程, 即**“思维链（Chain of Thought, 指AI在得出答案前在脑海中进行分步推理的内部思考流程）”**([AI agents now control part of Deepmind's compute for Gemini experiments ...](https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but)). 

这是什么意思呢？简单来说, 就是将AI为什么要做这种实验的**内部意图与动机以未经筛选的自然语言（人类可读语言）原封不动、透明地保留下来**, 以便人类管理者在其实施行动前进行彻底的审查([AI agents now control part of Deepmind's compute for Gemini experiments ...](https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but)).这并非把脑海遮得严严实实, 而是创造了一扇能够透明窥探实习生内心想法的玻璃窗。

---

## 当前现状：进展到了哪里, 局限又在哪里？

媒体常常以“AI正在像终结者一样自我修复并不断进化”的标题进行刺激性报道。然而, 一线的呼声却要冷静且现实得多。

谷歌DeepMind副总裁科赖·卡夫库奥格卢在播客采访中承认, 此举是实验室内部重大战略转变（strategic shift）的一部分, 但也划清了界限：科幻电影中常见的**“递归自我改进（Recursive Self-Improvement, 即AI通过不断修改代码使自己无限变聪明的循环）”**目前仍然路途遥远([AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement remains distant](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)).

也就是说,当前的AI代理充其量只是在人类设计的框架与安全装置内, 利用指定的计算预算“代行”实验。这并不意味着它处于自主设定目标并彻底改造自身架构的阶段。AI已进化为极其强大的“实验助手”和“编排者”, 但最终的指挥棒依然紧握在人类研究员的手中。

---

## 未来将如何发展？

通过这次发布, 我们可以一窥AI发展下一阶段的面貌。 

超越了单纯擅长写作、绘画的生成式AI时代, 我们正快速步入**直接进行科学发现与技术开发的“代理式AI（Agentic AI）”时代**。谷歌DeepMind的最终目标是构建一套涵盖全科学领域的统一通用算法([DeepMind's Gemini Experiments Now Orchestrated by AI Agents](https://best-ai.org/ai-news/deepminds-gemini-experiments-now-orchestrated-by-ai-agents-5o695i)).

未来我们需要关注的是：AI代理在受控的计算资源中能够产出多精细的假设, 以及在此过程中与人类合作的治理机制（Governance, 管理体系）能否得到安全维护。随着技术的不断精细化, DeepMind旨在透明化监控人工智能“内部思维链”的哲学理念, 预计将成为全球AI行业重要的标准安全指南。

---

## 参考资料

1. The Decoder, *AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement remains distant*, https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/
2. AI Weekly, *DeepMind Agents Now Run Part of Gemini Experiment Compute*, https://aiweekly.co/alerts/deepmind-agents-now-run-part-of-gemini-experiment-compute
3. TopAI Tools, *AI agents now control part of Deepmind's compute for Gemini experiments, but*, https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but
4. ExplainX AI, *DeepMind Agents Control Part of Gemini Training Compute — Koray Kavukcuoglu*, https://explainx.ai/blog/google-deepmind-gemini-agents-training-compute-koray-kavukcuoglu-november-2026
5. Emergent SH, *DeepMind AI Agents Now Control Gemini Experiment Compute*, https://emergent.sh/news/deepmind-ai-agents-now-control-gemini
6. Best AI, *DeepMind's Gemini Experiments Now Orchestrated by AI Agents*, https://best-ai.org/ai-news/deepminds-gemini-experiments-now-orchestrated-by-ai-agents-5o695i
7. AI Future, *AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement*, https://aifuture.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but-recu-21077
8. The Decoder, *Google Deepmind's AI Co-Scientist now plans experiments, runs lab equipment and writes scientific papers*, https://the-decoder.com/google-deepminds-ai-co-scientist-now-plans-experiments-runs-lab-equipment-and-writes-scientific-papers/
9. Wikipedia, *Gemini (language model)*, https://en.wikipedia.org/wiki/Gemini_(language_model)
10. Interesting Engineering, *Google DeepMind finds 1,600x faster way to expose encryption flaws*, https://interestingengineering.com/ai-robotics/google-deepmind-agents-expose-older-encryption-flaws