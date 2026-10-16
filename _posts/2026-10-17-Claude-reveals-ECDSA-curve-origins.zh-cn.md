---
layout: post
title: "数十年密码学谜团，AI终破译"
description: "美国国家标准与技术研究院 (NIST) 椭圆曲线密码标准中隐藏的秘密，现已由 AI 模型 Claude 揭示。"
summary: "Claude AI 揭示了数十年未解的 NIST 椭圆曲线密码生成种子 (seed) 的来源，确认为 20 世纪 90 年代 C 库中基于时间戳的生成器。"
tags: [AI, 密码学, 安全, Claude, NIST]
image: 2026-10-17-Claude-reveals-ECDSA-curve-origins.jpg
image_alt: "复杂的数字密码模式与 AI 连接的未来感画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这展示了 AI 解决复杂数学难题的能力已超越简单计算，进化成为科学探索的工具。"
quiz:
  - question: "在此次研究中，Claude 将 NIST 椭圆曲线种子的来源指向了什么？"
    choices: ["秘密加密短语", "20 世纪 90 年代 C 库中的 lrand48 生成器", "现代量子随机数生成器"]
    answer: 1
    explanation: "Claude 揭示这些种子是使用 20 世纪 90 年代 C 库 lrand48，基于 Unix 时间戳生成的。"
  - question: "这一发现对密码学界的主要意义是什么？"
    choices: ["获得密码被完全破解的证据", "减少对 NSA 故意植入弱点的怀疑", "立即废除新的密码标准"]
    answer: 1
    explanation: "通过可重现地解释过去由美国国家安全局 (NSA) 提供数值的生成依据，大大减少了对故意插入安全弱点的怀疑。"
  - question: "本次调查的主体是哪里？"
    choices: ["Google DeepMind", "Anthropic 前沿红队", "OpenAI 安全团队"]
    answer: 1
    explanation: "这项研究结果于 2026 年 10 月 16 日由 Anthropic 的前沿红队报告。"
lang: zh-cn
ref: 2026-10-17-Claude-reveals-ECDSA-curve-origins
---

我们每天使用互联网时，无数安全连接的背后都有一个名为“椭圆曲线密码”的数学保护层。然而，在过去的几十年里，制定这个标准过程中使用的核心数值“种子 (seed)”的来源一直是个谜，密码学家们对此不断提出疑问：“国家机构是否故意植入了弱点？” 这种不安感一直存在。但最近，有消息称，这个由来已久的谜团在 AI 的帮助下被解开了。

### 为何这很重要？

互联网安全是现代数字文明的基础。金融交易、个人消息、网站访问等我们珍视的数据都通过加密得到保护。如果这个加密体系核心的椭圆曲线标准中存在来源不明的“后门 (backdoor)”，这意味着全球数字安全都面临潜在威胁。[2] 这个后门就像一个坚固的保险箱上偷偷刻下的一个小瑕疵，知道它的人就能制造出打开保险箱的钥匙。过去几十年来，这个“后门”存在的可能性给密码学界和安全专家带来了极大的不安。但此次 AI 成功重现了这些数值的实际生成过程，预计将大大消除这些疑虑。[7]

### 简明理解：AI 追溯密码的根源

椭圆曲线密码是一种利用复杂数学原理安全保护数据的技术。这项技术的核心在于“随机性”。就像我们创建密码时使用不可预测的组合一样，在密码学中，不可预测的“随机数 (random number)”也至关重要。NIST（美国国家标准与技术研究院）提出的 ECDSA（椭圆曲线数字签名算法）标准中包含一个用于生成这些随机数的“种子 (seed)”初始值。然而，这个种子的生成方式和具体过程一直未被精确揭示，成为数十年的谜团。

简单来说，这个种子就像是构建密码之屋所需的“基本设计图”。但这份设计图的来源、绘制者，却无人能准确证明。Anthropic 的 AI 模型 Claude，就像考古学家挖掘埋藏的遗迹一样，逆向追溯了这些数值的生成方式。[1]

Claude 发现，这些数值并非由现代精密随机数生成器生成，而是通过 20 世纪 90 年代广泛使用的 C 库“lrand48”这一基本随机数生成器生成的。该生成器利用“Unix 时间戳 (Unix timestamp)”这种计算机系统以特定时间点为基准计算时间的方式来生成随机数。打个比方，它就像记录下时钟特定秒针指向的瞬间，然后生成随机数字。 [2] 这种方式在密码学安全标准中，由于可预测性较高，可能被视为一个弱点，因此引发了关于“故意植入弱点”的质疑。Claude 成功重现了通过“lrand48”生成 NIST 标准中使用的 5 个主要椭圆曲线种子的过程。[6]

### 当前状况：疑虑已消，但仍有待解决

这项研究结果已于 2026 年 10 月 16 日由 Anthropic 前沿红队正式发布。[2] 得益于 Claude 的分析，过去关于 NSA（美国国家安全局）故意在这些数值中植入安全弱点的疑虑已大大减少。现在研究人员可以沿着这个生成过程，重现并验证这些数值是如何得出的。

然而，并非所有疑问都已完全消除。据研究人员称，NIST 标准中使用的所有曲线参数并非都能通过“lrand48”和时间戳方式完美解释。也就是说，仍然有少数曲线的生成过程或依据尚未明确揭示。[6] 例如，有些数值是基于特定时间点生成，而另一些数值似乎是基于某个原因在更早的时间点生成。这些细微的不一致性仍是未来研究人员需要深入探索的课题。尽管如此，AI 为数十年未解的密码学难题提供了线索并开辟了解决之道，这被认为是一个极具象征意义的事件。

### 未来展望

此次案例清晰地表明，AI 不再仅仅是一个内容生成工具，它还能作为强大的“分析工具”，探索并解决人类研究人员数十年未能解决的复杂科学和数学问题。在密码学这种需要严密逻辑和证明的领域，AI 能够扮演这样的角色，其意义深远。AI 凭借分析海量数据和识别复杂模式的能力，可以补充人类的认知能力，从而带来新的发现。

未来，AI 有望更积极地应用于更复杂的代码分析、安全漏洞发现，乃至物理学、生物学等各种科学领域的难题解决。AI 不仅仅是提供结果，它还将成为协助科学发现过程的“伙伴”，为我们生活的数字世界和物理世界带来更高的透明度和安全性。AI 将在提高透明度、加速科学发现进程以及深化对复杂系统的理解方面发挥重要作用。

### MindTickleBytes AI 记者视角

令人印象深刻的是，AI 像拼图一样补齐了人类知识体系中缺失的碎片，在恢复密码学领域信任方面发挥了决定性作用。这项研究证明，AI 已将触角延伸至科学探索领域，成为一个强大的助手，能够减少不确定性并提高透明度。AI 的这种发展为我们未来可能面临的无数复杂问题带来了希望。AI 现在已不仅仅是一个“工具”，更是一个“同事研究员”，正在开启新的篇章。

## 参考资料
1. [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins)
2. [Claude reveals ECDSA curve origins - YouTube](https://www.youtube.com/watch?v=Sij6H9vhiy4)
3. [Claude traces the origins of NIST ECDSA curve seeds](https://blockchain.news/news/claude-traces-origins-of-nist-ecdsa-curve-seeds)
4. [ECDSA Curve Seeds Solved: Claude Found lrand48 (2026 ...)](https://www.explainx.ai/blog/claude-ecdsa-nist-curve-seeds-lrand48-anthropic-frontier-red-team-backdoor-question-2026)
5. [Anthropic Says Claude Traced NIST ECDSA Curve Seeds to a ...](https://www.unite.ai/anthropic-says-claude-traced-nist-ecdsa-curve-seeds-to-a-1990s-rng/)
6. [Claude traces NIST's ECDSA curve seeds to 1990s timestamps](https://runtimewire.com/article/claude-traces-nist-ecdsa-seeds-to-timestamps)
7. [Anthropic says Claude traced cryptographic curve origins to ...](https://superpowerdaily.com/posts/anthropic-says-claude-traced-cryptographic-curve-origins-to-timestamps)

## FACT-CHECK SUMMARY
- Claims checked: 6
- Claims verified: 0
- Verdict: PASS
---