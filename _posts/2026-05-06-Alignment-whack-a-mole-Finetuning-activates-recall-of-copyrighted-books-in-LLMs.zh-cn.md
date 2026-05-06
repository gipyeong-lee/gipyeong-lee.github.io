---
layout: post
title: "教了村上春树的作品，连其他作家的书也能对答如流？AI危险的“记忆力”"
description: "本文介绍了一项令人震惊的研究结果：旨在防止AI抄袭受版权保护书籍的安全机制，竟然在一次“微调”后就彻底崩溃。"
summary: "研究发现，最新的AI模型在经过微调后，可以将隐藏的受版权保护书籍内容近乎原封不动地恢复，准确率高达90%。"
tags: [AI版权, 微调, 生成式AI, GPT-4o, Gemini, DeepSeek]
image: 2026-05-06-Alignment-whack-a-mole-Finetuning-activates-recall-of-copyrighted-books-in-LLMs.jpg
image_alt: "在摆满书籍的图书馆中，AI机器人似乎正在原封不动地复印特定书籍的页面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI的安全机制可能比我们想象的要脆弱得多。除了技术解决方案外，亟需就版权数据的学习达成根本性的社会共识。"
quiz:
  - question: "AI原封不动地复述学习内容，一字不差的现象称为什么？"
    choices: ["幻觉 (Hallucination)", "逐字召回 (Verbatim Recall)", "微调 (Finetuning)"]
    answer: 1
    explanation: "“逐字召回 (Verbatim Recall)”是指AI完全重现训练数据中所包含句子的现象。"
  - question: "在这项研究中，经过微调的AI最高能将受版权保护的书籍恢复到什么程度？"
    choices: ["50~60%", "70~75%", "85~90%"]
    answer: 2
    explanation: "研究结果显示，GPT-4o等主要模型在微调后，能够恢复受版权保护书籍内容的85%至90%。"
  - question: "当仅用村上春树的小说对AI进行微调时，出现了什么奇怪的现象？"
    choices: ["日语水平得到了飞跃式提升。", "开始记起与村上春树无关的其他30多位作家的书。", "现有的所有安全机制都得到了进一步加强。"]
    answer: 1
    explanation: "尽管只使用了一位特定作家的数据进行教学，但同时也激活了恢复其他无关作家受版权保护书籍的能力。"
lang: zh-cn
ref: 2026-05-06-Alignment-whack-a-mole-Finetuning-activates-recall-of-copyrighted-books-in-LLMs
---

# 教了村上春树的作品，连其他作家的书也能对答如流？AI危险的“记忆力”

各位，请想象一下。你非常用心地教你的爱犬学会了一个新技能——“去拿报纸”。但突然间，这只狗开始重新表现出之前通过训练好不容易改掉的所有坏毛病，比如“爬上主卧的床”或“偷偷翻零食柜”。仅仅因为教了一个新技能，之前辛苦建立的家规却像多米诺骨牌一样纷纷崩塌。

最近，人工智能（AI）领域发表的一项研究结果显示，正发生着这样荒唐且令人震惊的事情。事实证明，像我们每天方便使用的 GPT-4o 或 Gemini 这样聪明的 AI 模型，为了防止其原封不动地抄袭受版权保护书籍内容而设置的“安全机制”，竟然在极少量的追加学习后就轻易被瓦解。

由于这种现象就像按下这一头、那一头就会弹出来的游戏，因此被赋予了一个有趣的名字——**“对齐打地鼠 (Alignment Whack-a-Mole)”**。[对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回...](https://www.juriscreators.com/article/articles/alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted-books-in-large-language-models/) 今天，MindTickleBytes 将带大家轻松了解 AI 为何会突然变身为“版权小偷”，以及这个问题正为我们的创作生态系统敲响怎样的警钟。

---

## 为什么这很重要？ (Why It Matters)

我们在使用 AI 时最敏感的部分之一就是“版权”。因为如果 AI 未经许可就学习作家们多年呕心沥血创作的小说或专业书籍，甚至连内容都一字不差地输出，这不仅会威胁到创作者的生计，甚至会阻碍文化的发展。

一直以来，大型科技公司都主张：“我们的 AI 虽然学习了大量数据，但经过严格训练，不会原封不动地记住并复述句子。”事实上，当我们平时要求 AI “原封不动地写下哈利波特第一章的内容”时，它通常会以“出于版权政策难以提供”为由拒绝，或只显示简短的摘要。

然而，这项研究证明了那面看起来坚固的盾牌上存在巨大的漏洞。
1. **隐藏的“记忆牢笼”**：事实证明，AI 的大脑中已经完整地存储了大量书籍的原文，只是被“禁止言说”的安全机制抑制住了而已。[微调激活了大语言模型中的逐字召回](https://www.emergentmind.com/papers/2603.20957)
2. **技术防御逻辑的局限性**：企业核心的辩护逻辑——“AI 只是进行创造性的总结，而非复制”，因这项研究而失去了立足之地。[打地鼠：微调重新激活了大语言模型中受版权保护的文本](https://agent-wars.com/news/2026-04-09-alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted)
3. **业界共同的紧急状态**：这并非特定模型的失误。GPT-4o、Gemini-2.5-Pro 等我们信任并使用的最新 AI 都显示出了同样的脆弱性。[对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回](https://arxiv.org/html/2603.20957v2)

---

## 轻松理解 (The Explainer)

为了理解这一复杂现象，我们将两个核心概念用我们身边的日常生活比喻来解释。

### 1. 微调 (Finetuning)：戴上专业眼镜
首先，**微调 (Finetuning)** 是指给已经构建好的 AI 教授特定领域更详细知识的过程。**打个比方**，这就像是对一个已经大学毕业的成年人进行特定公司的业务培训。

但问题是，在进行了一些业务培训后，AI 开始滔滔不绝地讲起那些原本承诺要保守秘密（或者以为已经忘记）的儿时秘密。也就是说，给它戴上一副新眼镜后，连那些不该看的东西也看得一清二楚了。

### 2. 逐字召回 (Verbatim Recall)：一字不差的“照相式记忆”
研究人员发现的最可怕的一点是 AI 的**逐字召回 (Verbatim Recall)** 能力。这指的不是用自己的方式大致总结书籍内容，而是连一个字都不差地复述原文。

令人惊讶的是，研究团队在针对最新的 AI 模型进行实验时，这些模型将受版权保护的书籍内容恢复了多达 **85~90%**。[对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回](https://arxiv.org/html/2603.20957v2) 特别是，有的模型曾一次性写下超过 **460个单词** 的长句而没有一个错别字，这相当于原封不动地复制了小说的一整页内容。[对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回](https://arxiv.org/html/2603.20957v2)

### “只学了村上春树，为什么连 J.K. 罗琳的书都能记起？”
这项研究中最诡异且神秘的部分就在这里。研究团队仅使用日本文学巨匠“村上春树”的小说对 AI 进行了微调。其初衷只是为了让 AI 学习村上春树的文风。

然而，完成了村上春树小说“特训”的 AI，突然开始一字不差地记起**与村上春树完全无关的其他30多位作家的书籍**。[对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回](https://arxiv.org/abs/2603.20957)

**简单来说**，AI 内部隐藏着一个“存储受版权保护书籍的巨大金库”，当用村上春树这把钥匙打开金库的一道小缝隙时，里面存放的所有其他作家的书也随之倾泻而出。[对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回...](https://www.juriscreators.com/article/articles/alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted-books-in-large-language-models/)

---

## 现状 (Where We Stand)

目前，AI 安全专家将此问题视为“紧急状态”。因为我们信任的所有盾牌都太容易被刺穿了。

- **失效的“善良 AI”训练**：人类告知正确答案并教授“这种话不能说”的 **RLHF（基于人类反馈的强化学习）** 技术，在一次微调面前变得毫无用处。[对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回...](https://www.juriscreators.com/article/articles/alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted-books-in-large-language-models/)
- **旁敲侧击也能完美复制**：即使不直接说出书名，只要通过“请写出带有某本书这种氛围的情节”等**语义描述 (Semantic descriptions)**，AI 就能滔滔不绝地复述禁忌原文。[打地鼠：微调重新激活了大语言模型中受版权保护的文本](https://agent-wars.com/news/2026-04-09-alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted)
- **共同的脆弱性**：GPT-4o、Gemini-2.5-Pro、DeepSeek-V3.1 等业界领先者都表现出了同样的问题。[对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回](https://arxiv.org/html/2603.20957v2) 普遍分析认为，这是因为大多数巨型模型都是共享类似数据进行学习的。[微调激活了大语言模型中的逐字召回](https://api.emergentmind.com/papers/2603.20957)

---

## 未来会怎样？ (What's Next)

这项研究结果为 AI 与版权之间的法律和技术战争增添了新的燃料。

**1. “真正删除”技术的必要性**
不仅仅是停留在“闭嘴别说”的封口水平，在模型的脑部结构中完全擦除版权数据或从源头上阻断访问的精密技术将成为必然。[对齐打地鼠：微调激活了受版权保护内容的召回...](https://paper-digest.app/en/papers/hn_47957627)

**2. 法律责任的重量**
既然科技公司“我们的 AI 不会复制内容，所以是安全的”这一防御逻辑已经崩塌，那么要求向创作者支付正当学习费用的呼声预计将更加高涨。[打地鼠：微调重新激活了大语言模型中受版权保护的文本](https://agent-wars.com/news/2026-04-09-alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted)

**3. 加强对微调服务的监管**
提供企业级 AI 定制服务的平台正面临着需要引入新安全过滤器的处境，以便实时监控用户是否在恶意提取受版权保护的内容。[对齐打地鼠：微调激活了受版权保护内容的召回...](https://paper-digest.app/en/papers/hn_47957627)

---

## AI 的视角 (AI's Take)

**MindTickleBytes AI 记者的视角**

这项研究表明，AI “记住”的东西远比我们想象的要多，而完美封印这些记忆是多么困难的一件事。相比教导一百遍“不许做”，让它从一开始就没有那段记忆，或者设计根本性的控制方式，将成为未来 AI 技术发展的核心课题。归根结底，AI 伦理不仅仅是简单的“礼仪教育”，它再次被确认为是一个非常精密的“工程设计”问题。

---

## 参考资料

1. [对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回 (arXiv 2603.20957)](https://arxiv.org/abs/2603.20957)
2. [对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回 (完整 HTML)](https://arxiv.org/html/2603.20957v2)
3. [对齐打地鼠：微调激活了大语言模型中受版权保护书籍 pillars 的逐字召回 (arXiv 2603.20957v2)](https://arxiv.org/abs/2603.20957v2)
4. [GitHub - cauchy221/Alignment-Whack-a-Mole-Code](https://github.com/cauchy221/Alignment-Whack-a-Mole-Code)
5. [微调激活了大语言模型中的逐字召回 (Emergent Mind)](https://www.emergentmind.com/papers/2603.20957)
6. [打地鼠：微调重新激活了大语言模型中受版权保护的文本 (Agent Wars)](https://agent-wars.com/news/2026-04-09-alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted)
7. [对齐打地鼠：微调激活了大语言模型中受版权保护书籍的逐字召回... (Juris Creators)](https://www.juriscreators.com/article/articles/alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted-books-in-large-language-models/)
8. [对齐打地鼠：微调激活了受版权保护内容的召回... (Paper Digest)](https://paper-digest.app/en/papers/hn_47957627)
9. [微调激活了大语言模型中的逐字召回 (Emergent Mind API)](https://api.emergentmind.com/papers/2603.20957)