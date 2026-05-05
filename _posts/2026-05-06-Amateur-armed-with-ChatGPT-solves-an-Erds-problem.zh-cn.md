---
layout: post
title: "非数学专业23岁青年，用ChatGPT破解60年数学难题？"
description: "介绍23岁业余爱好者利亚姆·普莱斯（Liam Price）利用GPT-5.4 Pro解决困扰数学界60年的埃尔德什猜想的惊人事件。"
summary: "一名未受过专业数学训练的23岁青年利用ChatGPT在短短80分钟内解决了60年未解的数学难题，并得到了菲尔兹奖得主陶哲轩（Terence Tao）的验证。"
tags: [ChatGPT, AI数学, 埃尔德什猜想, 利亚姆·普莱斯, 人工智能, 数学难题]
image: 2026-05-06-Amateur-armed-with-ChatGPT-solves-an-Erds-problem.jpg
image_alt: "一名青年坐在电脑前与ChatGPT对话，注视着复杂的数学公式"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这一事件表明，AI已不仅仅是简单的信息检索工具，而是进化为能够发现人类直觉无法触及的新逻辑路径的‘智能伙伴’。"
quiz:
  - question: "这次解决60年数学难题的主角姓名和年龄是多少？"
    choices: ["陶哲轩，40岁", "利亚姆·普莱斯，23岁", "保罗·埃尔德什，23岁"]
    answer: 1
    explanation: "23岁的业余数学爱好者利亚姆·普莱斯是这次发现的主角。"
  - question: "解决该问题使用的是哪款AI模型？"
    choices: ["GPT-4", "GPT-5.4 Pro", "Claude 3"]
    answer: 1
    explanation: "利亚姆·普莱斯通过订阅ChatGPT Pro使用了GPT-5.4 Pro模型。"
  - question: "菲尔兹奖得主陶哲轩对AI的解决方法有何评价？"
    choices: ["与传统方法完全相同", "之前的研究者从第一步起就走错了方向", "逻辑错误太多"]
    answer: 1
    explanation: "陶哲轩高度评价了AI的新方法，称之前的所有研究者从第一步起就走错了方向。"
lang: zh-cn
ref: 2026-05-06-Amateur-armed-with-ChatGPT-solves-an-Erds-problem
---

2026年4月的一个平凡的周一下午。居住在英国的23岁青年利亚姆·普莱斯（Liam Price）正坐在电脑前，像往常一样与ChatGPT交流。他从未接受过专业的数学教育，也不是拥有博士学位的研究员 [来源 3](https://byteiota.com/amateur-solves-60-year-erdos-problem-with-chatgpt/)。然而，他那天下午出于好奇做出的一个决定，却引发了一个彻底改变数学史的巨大成果。

他向ChatGPT提出的问题是困扰全球天才数学家长达60年之久、最终未能破解的难题。结果令人难以置信。ChatGPT仅用80分钟就给出了完善的逻辑证明，这一结果被誉为“数学界诺贝尔奖”的菲尔兹奖得主陶哲轩（Terence Tao）正式确认其为“正确” [来源 3](https://byteiota.com/amateur-solves-60-year-erdos-problem-with-chatgpt/), [来源 6](https://eu.36kr.com/en/p/3784815604817154)。

究竟这种如魔法般的事情是如何发生的？MindTickleBytes将为您通俗易懂地解读这位业余爱好者与人工智能携手创造的惊人事件的全过程。

## 这为什么很重要？

迄今为止，数学的最前沿一直是只有接受过高度训练的少数专家才能涉足的圣地。为了破解积压数十年的难题，阅读数千篇相关论文、将复杂的公式在脑海中铭记数年是必经的痛苦过程。

然而，这一事件象征着那座坚固的堡垒正在倒塌。随着像ChatGPT这样的大语言模型（LLM）的出现，即使不懂直接操作复杂的数学工具，只要懂得向人工智能提出正确问题，任何人都可以为扩展人类知识边界做出贡献 [来源 2](https://best-ai.org/ai-news/amateur-armed-with-chatgpt-solves-a-60-year-old-erds-problem), [来源 5](https://www.aitoolcrunch.com/blog/chatgpt-solves-erdos-problem/)。

专家们将其称为“非专业人士数学发现的新路径” [来源 2](https://best-ai.org/ai-news/amateur-armed-with-chatgpt-solves-a-60-year-old-erds-problem)。**简单来说**，现在是一个任何人都可以将AI作为超级计算机助手，仅凭“想法”和“提问”就能震惊世界的时代。

## 轻松理解：“禁止倍数俱乐部”与AI的捷径

这次解决的问题是20世纪最伟大的数学家之一保罗·埃尔德什（Paul Erdős）留下的关于“原始集（Primitive sets）”的猜想 [来源 7](https://www.indiatoday.in/education-today/news/story/liam-price-solves-60-year-old-erdos-math-puzzle-with-chatgpt-2903168-2026-05-01), [来源 12](https://www.weaving.news/news/019dc7a1-8ddd-7770-81d2-d328b83864f0)。虽然名字听起来很难，但原理出奇地简单。

### 什么是原始集？
为了理解这个概念，我们可以想象一个**“禁止倍数俱乐部”**。俱乐部的规则非常明确：
> “俱乐部成员中的任何数字都不能是其他成员的倍数。”

例如，如果成员中有 `2`，那么像 `4, 6, 8, 10` 这样的数字绝对不能加入。如果 `3, 5, 7` 是成员，因为它们彼此都不是对方的倍数，所以可以和平共处。数学家将遵守这种规则的数字集合称为“原始集”。保罗·埃尔德什对这些数字集所具有的独特性质提出了一个非常刁钻的问题，答案在60年里一直是一个谜 [来源 2](https://best-ai.org/ai-news/amateur-armed-with-chatgpt-solves-a-60-year-old-erds-problem), [来源 4](https://tech.yahoo.com/ai/chatgpt/articles/amateur-armed-chatgpt-vibe-maths-123000665.html)。

### AI是如何解决的？
利亚姆·普莱斯使用了最新的AI模型GPT-5.4 Pro输入了这个问题 [来源 3](https://byteiota.com/amateur-solves-60-year-erdos-problem-with-chatgpt/)。他甚至不知道这个问题是多么著名的难题，只是发送了一个类似“请证明这个问题的对错”的一次性请求（提示词） [来源 3](https://byteiota.com/amateur-solves-60-year-erdos-problem-with-chatgpt/), [来源 9](https://news.ycombinator.com/item?id=47903126)。

ChatGPT在约80分钟的时间里通过自我构建逻辑的推理（Reasoning）过程，得出了完善的证明 [来源 3](https://byteiota.com/amateur-solves-60-year-erdos-problem-with-chatgpt/), [来源 11](https://www.msn.com/en-us/news/other/chatgpt-credited-with-solving-60-year-old-erdős-math-problem/gm-GM45F355EF)。**打个比方**：到目前为止，所有的数学家为了在茂密的森林中寻找出路，都只是拨开脚下的草丛前行。而AI则是升起无人机俯瞰整个森林，然后找到了一条没人想到的、完全不同方向的捷径。陶哲轩教授感叹道：“之前的所有研究者从第一步起就走错了方向”，对AI的创新方法表示赞赏 [来源 6](https://eu.36kr.com/en/p/3784815604817154)。

## 现状：“氛围数学（Vibe Maths）”的诞生

此事报道后，西方媒体开始将其称为**“氛围数学（Vibe Maths）”** [来源 1](https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/), [来源 4](https://tech.yahoo.com/ai/chatgpt/articles/amateur-armed-chatgpt-vibe-maths-123000665.html)。这是一个幽默的名称，意指比起严谨的公式，这种方式更多是通过与AI交流来传递“感觉（Vibe）”和“方向感”来解决问题的。

目前的情况总结如下：
1. **验证完成**：世界著名数学家陶哲轩确认AI的解法在逻辑上没有缺陷 [来源 3](https://byteiota.com/amateur-solves-60-year-erdos-problem-with-chatgpt/), [来源 6](https://eu.36kr.com/en/p/3784815604817154)。
2. **论文撰写**：AI负责核心想法和逻辑展开，而将其整理成学术格式并进行最终验证则由人类专家负责 [来源 7](https://www.indiatoday.in/education-today/news/story/liam-price-solves-60-year-old-erdos-math-puzzle-with-chatgpt-2903168-2026-05-01)。
3. **新的可能性**：全球数学界正以半期待半担忧的心态关注这种方法是否也能应用于其他数学难题 [来源 12](https://www.weaving.news/news/019dc7a1-8ddd-7770-81d2-d328b83864f0)。

## 未来会怎样？

利亚姆·普莱斯的案例不会只是一个偶然的插曲。因为已经有很多业余爱好者开始利用ChatGPT挑战各种难题，掀起了“埃尔德什热潮（AI-for-Erdős craze）” [来源 1](https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/)。

我们不久后将目睹以下变化：
- **人人都能成为数学家的世界**：复杂的计算和证明过程由AI承担，人类将专注于思考“应该提出什么样有价值的问题” [来源 13](https://timesofindia.indiatimes.com/technology/tech-news/ai-helps-solve-a-60-year-old-erds-math-puzzle-that-stumped-generations-of-mathematicians/articleshow/130678333.cms)。
- **学科边界瓦解**：不仅在数学领域，物理、化学等基础科学的所有领域，业余爱好者与AI的协作都可能创造出新的突破 [来源 5](https://www.aitoolcrunch.com/blog/chatgpt-solves-erdos-problem/)。
- **AI推理能力的进化**：正如在GPT-5.4 Pro模型中所看到的，超越单纯预测下一个词的水平，能够执行高度逻辑推理的模型将成为科学研究不可或缺的伙伴 [来源 10](https://www.buildfastwithai.com/blogs/gpt-5-4-solved-a-60-year-math-problem-what-happened/)。

**想象一下**：在你随口提出的一个问题中，人工智能找到了解开百年科学之谜的线索。正如利亚姆·普莱斯所证明的那样，下一次数学史的主角可能就是你。

---

### AI的视角
**MindTickleBytes AI记者的观点：**
如果说过去的数学天才们是孤独地用纸和笔挖掘宇宙的奥秘，那么现在则是所有掌握“提问”这把钥匙的人都能接近那些奥秘的时代。这一事件表明，AI并不是要取代人类的智能，而是成为了一种能够无限放大人类“好奇心”破坏力的强大放大器。我们向AI提出的问题越好，人类的知识版图扩展得就越快。

---

## 参考资料
1. [业余爱好者利用ChatGPT“氛围数学”解决了一个60年的难题 ...](https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/)
2. [业余爱好者利用ChatGPT解决了60年前的埃尔德什猜想](https://best-ai.org/ai-news/amateur-armed-with-chatgpt-solves-a-60-year-old-erds-problem)
3. [业余爱好者利用ChatGPT解决埃尔德什60年难题 | byteiota](https://byteiota.com/amateur-solves-60-year-erdos-problem-with-chatgpt/)
4. [业余爱好者利用ChatGPT“氛围数学”解决了一个60年的难题](https://tech.yahoo.com/ai/chatgpt/articles/amateur-armed-chatgpt-vibe-maths-123000665.html)
5. [业余数学家利用ChatGPT解决埃尔德什60年难题](https://www.aitoolcrunch.com/blog/chatgpt-solves-erdos-problem/)
6. [23岁业余爱好者利用ChatGPT解决60年数学难题 ...](https://eu.36kr.com/en/p/3784815604817154)
7. [业余爱好者利用ChatGPT解决专家无法破解的60年数学难题 ...](https://www.indiatoday.in/education-today/news/story/liam-price-solves-60-year-old-erdos-math-puzzle-with-chatgpt-2903168-2026-05-01)
8. [业余爱好者利用ChatGPT解决埃尔德什难题 | Hacker News](https://news.ycombinator.com/item?id=47903126)
9. [GPT-5.4 解决了一个60年的数学难题：发生了什么](https://www.buildfastwithai.com/blogs/gpt-5-4-solved-a-60-year-math-problem-what-happened)
10. [AI辅助证明可能破解了60年前的埃尔德什猜想](https://www.msn.com/en-us/news/other/chatgpt-credited-with-solving-60-year-old-erdős-math-problem/gm-GM45F355EF)
11. [业余爱好者利用ChatGPT解决埃尔德什难题](https://www.weaving.news/news/019dc7a1-8ddd-7770-81d2-d328b83864f0)
12. [AI助力解决困扰数代数学家的60年埃尔德什数学谜题 ...](https://timesofindia.indiatimes.com/technology/tech-news/ai-helps-solve-a-60-year-old-erds-math-puzzle-that-stumped-generations-of-mathematicians/articleshow/130678333.cms)