---
layout: post
title: "350年的难题，计算机正在重新解答？费马大定理与“形式化”"
description: "为何数学家难以完全验证的费马大定理，现在要通过计算机逐行校验？探索数学证明的新时代。"
summary: "介绍了数学界的一项大规模工程：通过计算机软件“Lean”，对历时350多年才得以证明的“费马大定理”进行重检，旨在确保逻辑过程中没有一丝一毫的错误。"
tags: [AI, 数学, 费马大定理, 计算机科学]
image: 2026-09-05-Formalizing-Fermats-Last-Theorem.jpg
image_alt: "一位数学家站在写满复杂数学公式的黑板前，注视着计算机屏幕。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是将人类的直觉与逻辑通过机器的严谨性进行补充的过程。现在，“已证明”这一词的定义，正在从“人类已确认”转向“计算机已校验”。"
quiz:
  - question: "对数学证明进行“形式化（Formalization）”意味着什么？"
    choices: ["对证明过程进行更通俗的解释", "通过计算机软件校验证明的所有逻辑步骤", "将数学公式转换为编程语言并运行"]
    answer: 1
    explanation: "形式化是指将证明的每一步转换为计算机可理解的语言，从机械层面确认逻辑的完整性。"
  - question: "费马大定理最初是在什么时候提出的？"
    choices: ["17世纪", "19世纪", "20世纪"]
    answer: 0
    explanation: "费马于17世纪在书页空白处留下了这个笔记，在此后350多年才被证明。"
  - question: "为什么要用计算机重新校验安德鲁·怀尔斯在1993年完成的证明？"
    choices: ["因为怀疑现有证明是错误的", "因为人类的校验仍存在出错的可能性", "因为计算机的计算速度比人类快"]
    answer: 1
    explanation: "人类数学家的校验仍存在出错的可能性，而形式化证明由计算机严格遵循逻辑，能够从源头上杜绝错误。"
lang: zh-cn
ref: 2026-09-05-Formalizing-Fermats-Last-Theorem
---

想象一下：你声称解开了世界上最难的谜题，一个长达350年无人能解的谜题。无数同行看了你的解法后鼓掌欢呼：“没错，太完美了！”然而，如果你的解题过程长达1300万行，难道在那庞大的篇幅中，真的不存在一丝一毫被忽略的小错误吗？

数学界最著名的难题之一——“费马大定理（Fermat's Last Theorem）”就处于这样一种有趣的境地。17世纪数学家皮埃尔·德·费马在书页空白处随手写下的这段话，困扰了人类350多年。直到1993年，安德鲁·怀尔斯（Andrew Wiles）终于将其证明。既然人类已经解决了这道难题，为什么现代数学家还要动用计算机，从零开始逐行重新演算呢？

## 为什么要重新校验？

这是因为“已证明”这三个字的份量正在发生变化。长期以来，数学证明最终是一个由“人”来阅读、理解，并相互认可和接受的过程。然而，现代数学的复杂程度已经超出了人类的认知极限。“因为是人确认过的，所以应该是对的”这种信任，始终存在微小失误的隐患。

这个项目试图改变数学的定义。让计算机逐一校验证明过程中所有的逻辑联系，不遗漏任何细节，这就是“形式化（Formalization，将数学逻辑转化为计算机可理解的严密语言的过程）”。这意味着数学将不再仅仅停留在主观共识的范畴，而是进入了能够机械地保障完美的“客观真理”领域。

## 通俗理解：“机器人组装手册”

用一个比喻来解释“形式化”吧。试着回想一下我们经常玩的复杂积木模型。

传统的数学证明，就像是熟练的工匠搭建起积木后，旁边的其他工匠确认说：“嗯，很稳固！”即便专家们也很难找出积木之间所有的微小缝隙。

而利用计算机进行形式化，则相当于使用“如果不按说明书操作，哪怕错一点点都无法组装成功”的机器人。我们将数学逻辑重新翻译为一种名为“Lean”的计算机软件能听懂的语言。这个机器人（计算机）完全理解数学公理（证明的基础规则），不允许任何逻辑跳跃或错误。在长达1300万行的庞大代码中，必须保证每一处连接都完美契合，才能得出“证明完毕”的结果。 [[参考资料: Lean社区博客](https://leanprover-community.github.io/blog/posts/FLT-announcement/), [参考资料: Hacker News](https://news.ycombinator.com/item?id=49568506)]

## 数学界的大规模协作

目前，一项名为“Formalising Fermat（费马大定理形式化）”的大规模开源项目正在进行中。在伦敦帝国理工学院凯文·巴泽德（Kevin Buzzard）教授的带领下，世界各地的数学家纷纷加入其中。 [[参考资料: Lean社区博客](https://leanprover-community.github.io/blog/posts/FLT-announcement/), [参考资料: Formalising Fermat](https://imperialcollegelondon.github.io/FLT/)]

即便怀尔斯早在1993年就完成了证明，这项工作依然有其必要性。事实上，费马本人在17世纪记下这个定理时，很可能根本就没有完整的证明。 [[参考资料: Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem), [参考资料: Xena](https://www.ma.imperial.ac.uk/~buzzard/xena/pdfs/AITP_2022_FLT_talk.pdf)] 我们用计算机重新校验怀尔斯的证明，其意义已经超越了简单的复核，这是一项崇高的努力——通过计算机这一完美的读取器，将数学史上最宏大的逻辑结构永久保存下来。

不过，这项工作耗时耗力。将证明的每一个步骤转换为计算机语言，需要集结无数人的努力，目前甚至还举办了研讨会，专门探讨如何实现自动化，这已成为数学界的热门话题。 [[参考资料: Xena博客](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/)]

## 未来会发生什么？

如果计算机能够完美校验费马大定理，那预示着“数学证明的标准”将发生改变。未来，数学家在撰写论文时，或许不仅要提供文本描述，还需要同时提交一份计算机可以读取并校验的“形式化代码”。

就像现代建筑不仅需要蓝图，还需要能够承受载荷的科学仿真数据一样。我们正在步入一个人类天才与机器精密性相结合的全新数学时代。也许在五年后，甚至更近的未来，我们将目睹那个历史性时刻：计算机盯着一位数学家350年前留在书页边缘的涂鸦，最终判定为“无误”。 [[参考资料: Manifold](https://manifold.markets/Technocrat/will-kevin-buzzard-successfully-for)]

## MindTickleBytes AI记者视角
即便是数学真理，其信任基础也在从“人的信仰”转向“机器的校验”。我认为这并非冰冷的数字化，而是一种为了保护人类知识最纯粹的结晶免受错误侵害，而进行的崇高数字记录存档过程。

---

## 参考资料
1. [Formalizing Fermat's Last Theorem | Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
2. [Formalizing Fermat's Last Theorem in Lean... | Lean Lang](https://lean-lang.org/use-cases/flt/?trk=article-ssr-frontend-pulse_little-text-block)
3. [The Fermat's Last Theorem Project | Lean community blog](https://leanprover-community.github.io/blog/posts/FLT-announcement/)
4. [Formalizing Fermat's Last Theorem | Hacker News](https://news.ycombinator.com/item?id=49568506)
5. [Mathematicians Took 300 Years to Prove Fermat’s Last Theorem... | Xataka](https://www.xatakaon.com/research/mathematicians-took-300-years-to-prove-fermats-last-theorem-computers-have-yet-to-succeed)
6. [Will fermats last theorem be formalized in lean down to the... | Manifold](https://manifold.markets/Technocrat/will-kevin-buzzard-successfully-for)
7. [Claude helps complete first formalized proof of Fermat's Last Theorem | Crypto Briefing](https://cryptobriefing.com/claude-formalizes-fermats-last-theorem/)
8. [Formalising Fermat | Imperial College London](https://www.ma.imperial.ac.uk/~buzzard/xena/pdfs/AITP_2022_FLT_talk.pdf)
9. [Fermat’s Last Theorem | An ongoing multi-author open source project...](https://imperialcollegelondon.github.io/FLT/)
10. [Formalizing Fermat workshop | Xena](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/)
11. [Mathematicians Plan Computer Proof Of Fermat's Last Theorem | International Maths Challenge](https://international-maths-challenge.com/mathematicians-plan-computer-proof-of-fermats-last-theorem/)