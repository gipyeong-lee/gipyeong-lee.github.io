---
layout: post
title: "AI寻找软件“漏洞”？安斯罗普（Anthropic）安全追踪器揭秘"
description: "深入了解安斯罗普的安全程序，探讨AI如何自动发现并管理软件安全漏洞及其影响力。"
summary: "安斯罗普正利用其AI模型系统地自动发现全球软件中的安全漏洞，并通知开发人员以引导其进行修补。"
tags: [AI, 安全, 安斯罗普, 软件, 技术]
image: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities.jpg
image_alt: "屏幕上显示着象征计算机代码和安全性的数字图形图像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI化身防御者率先发现漏洞固然是好事，但修补速度远落后于漏洞发现速度，这是我们必须解决的新难题。"
quiz:
  - question: "安斯罗普在发现安全漏洞后首先会做什么？"
    choices: ["向互联网公开漏洞", "私下通知软件维护者", "立即编写攻击代码"]
    answer: 1
    explanation: "安斯罗普遵循“协同漏洞披露（CVD）”政策，将发现的漏洞私下传达给软件维护者，给予他们在公开披露前进行修复的时间。"
  - question: "截至2026年10月，安斯罗普发现的漏洞候选者中，实际公开的漏洞有多少个？"
    choices: ["6,157个", "29,439个", "516个"]
    answer: 0
    explanation: "根据安斯罗普的仪表盘，在29,439个候选者中，有6,157个漏洞被公开，其中516个在顶级项目中得到了修补。"
  - question: "安斯罗普的安全程序面临的现实挑战是什么？"
    choices: ["AI完全无法发现漏洞", "实际修补速度滞后于漏洞发现速度", "所有漏洞都立即被利用"]
    answer: 1
    explanation: "在已发现的漏洞中，已修复的比例约为8.4%，面对AI发现漏洞的庞大数量，实际开发人员的修补速度跟不上，这是现实挑战。"
lang: zh-cn
ref: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities
---

想象一下，在你使用的智能手机或网页浏览器中住着一位“安全侦探”。这位侦探不眠不休，整天巡视着软件的各个角落，寻找黑客可能入侵的细小“漏洞”。

最近，人工智能公司安斯罗普（Anthropic）因运营着这样一个安全程序而备受瞩目。AI不再仅仅是写文章或画图，它已站在保护我们日常使用程序安全的最前线。

### 为什么这很重要？

我们每天的生活都依赖于无数软件。我们用浏览器购物，通过操作系统（OS）处理工作。如果这些程序存在安全漏洞会怎样？黑客可以利用这些空隙窃取个人信息或使系统瘫痪。

以往，寻找这些漏洞是人工安全专家的职责。然而，软件太庞大、太复杂，人工寻找所有漏洞存在局限性。安斯罗普的方法正在改变这一格局。他们试图通过AI更快速、更高效地发现漏洞，在攻击者动坏心思之前先筑起防线。这不仅关乎个人隐私保护，更直接关系到我们所信赖的整个数字生态系统的安全性 [[参考资料 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)]。

### 浅显易懂：“安全侦探”AI的工作方式

安斯罗普利用名为“克劳德（Claude）”的AI模型及其内部研究模型，分析全球的开源及闭源软件 [[参考资料 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude), [参考资料 6](https://red.anthropic.com/2026/cvd/about/)]。

简单来说，传统的安全检查就像人拿着放大镜在整栋楼里巡视寻找裂缝，而安斯罗普的AI则是在完美掌握建筑图纸后，动用数千个摄像头在瞬间找出结构缺陷。

特别是名为“克劳德·神话（Claude Mythos）”的模型，它不仅能自动发现漏洞，还具备生成如何实施攻击的代码的能力 [[参考资料 7](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html), [参考资料 8](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)]。这就像医生不仅诊断疾病，还通过模拟病菌如何侵入身体，从而研制出完美的预防疫苗。

### 现状：成千上万的漏洞与缓慢的修补

那么，目前发现了多少漏洞呢？截至2026年10月2日，根据安斯罗普的仪表盘，他们审查了约29,439个漏洞候选者，并正式公开了其中的6,157个 [[参考资料 5](https://vulnerabilities.ai/ledger)]。

但这里有一个既引人关注又令人担忧的点：在已发现的漏洞中，实际由开发人员完成修补的比例约为8.4%（516个） [[参考资料 5](https://vulnerabilities.ai/ledger)]。AI正在以惊人的速度发现问题，但人类修复问题的速度却跟不上。

此外，尽管发现了如此多的漏洞，但幸运的是，其中只有不到0.5%被黑客实际利用 [[参考资料 16](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)]。然而，鉴于已有案例报告称AI被用于无需人工干预、自动发现漏洞并实施攻击，情况仍不容乐观 [[参考资料 19](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)]。

### 未来趋势

安斯罗普不会立即在互联网上散布发现的漏洞。相反，根据“协同漏洞披露（Coordinated Vulnerability Disclosure, CVD）”政策，他们会私下通知相关软件的维护者，并给予修改时间 [[参考资料 6](https://red.anthropic.com/2026/cvd/about/)]。

未来，AI发现的漏洞数量将呈指数级增长，软件开发环境也随之需要变革。极有可能从人工逐一修补AI发现的问题，转向AI发现问题并自动生成、应用修补程序的“自动化防御体系”。

我们现在生活的时代，已不仅是担心AI攻击计算机，而是通过AI构建更安全的软件环境。为了了解未来的技术进步如何进一步保障我们的数字生活安全，值得关注安斯罗普的仪表盘。

---
**MindTickleBytes的AI记者视角：**
技术总是一体两面。安斯罗普的AI担当安全哨兵是巨大的进步，但漏洞发现速度远超修补速度的现状，要求软件行业进行前所未有的竞速。安全已不再是人所为的“艺术”，而成了AI与人类必须共同破解的无止境的马拉松。

## 参考资料

1. [Tracking Anthropic-discovered vulnerabilities](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)
2. [Discovering and exploiting vulnerabilities in critical, real ...](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)
3. [Anthropic's coordinated vulnerability disclosure dashboard](https://red.anthropic.com/2026/cvd/)
4. [Coordinated vulnerability disclosure for Claude-discovered ...](https://www.anthropic.com/coordinated-vulnerability-disclosure)
5. [Ledger — Tracking the AI Vulnerability-Discovery Programs](https://vulnerabilities.ai/ledger)
6. [About this dashboard - red.anthropic.com](https://red.anthropic.com/2026/cvd/about/)
7. [Claude Mythos Security Vulnerabilities: What We Know in 2026](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html)
8. [How Anthropic Claude Mythos is reshaping the vulnerability ...](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)
9. [Research \Anthropic](https://www.anthropic.com/research)
10. [A Cheeky Pint withAnthropicCEO Dario Amodei - YouTube](https://www.youtube.com/watch?v=GcqQ1ebBqkc)
11. [Secret Claudetrackershocks users afterAnthropic’s anti-surveillance...](https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/)
13. [AnthropicStatus. Check ifAnthropicis down or having... | StatusGator](https://statusgator.com/services/anthropic)
16. [Anthropic-linked CVEs pile up, attackers mostly shrug](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)
19. [Full report: Disrupting the first reported AI-orchestrated ...](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)