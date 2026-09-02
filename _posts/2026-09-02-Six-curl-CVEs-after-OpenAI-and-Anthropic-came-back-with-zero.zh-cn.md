---
layout: post
title: "AI 错过的 25 年安全漏洞，被“专用 AI”发现了"
description: "讲述了一个新的 AI 如何发现连 OpenAI 和 Anthropic 等知名 AI 都未能察觉的安全漏洞。深入浅出地解释了 curl 中隐藏了 25 年的错误及其意义。"
summary: "安全专用 AI AISLE 发现了通用 AI 模型错过的 6 个安全漏洞，其中包括 curl 项目历史上自 2001 年以来一直未被发现的最古老漏洞。"
tags: [AI, 安全, curl, CVE, 科技热点]
image: 2026-09-02-Six-curl-CVEs-after-OpenAI-and-Anthropic-came-back-with-zero.jpg
image_alt: "一个 AI 系统在象征数字代码的数据流中寻找代表安全漏洞的空洞。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "即便在通用大模型时代，“专用 AI”在特定领域深度挖掘的价值也将愈发凸显。"
quiz:
  - question: "在本次安全事件中，AISLE 总共发现了多少个 CVE？"
    choices: ["1个", "3个", "6个"]
    answer: 2
    explanation: "AISLE 在本次调查中总共发现了 6 个新的安全漏洞（CVE）。"
  - question: "curl 项目中发现的最古老漏洞从什么时候开始存在？"
    choices: ["2010年", "2001年", "2026年"]
    answer: 1
    explanation: "该漏洞被记录为 CVE-2026-8932，经查明，自 2001 年 3 月起就一直被忽视。"
  - question: "关于本文描述的“通用 AI”与“专用 AI”的区别，下列哪项说明是正确的？"
    choices: ["通用 AI 在安全性上总是优于专用 AI。", "通用 AI 拥有广泛的知识，但在特定领域的深度探索上可能不如专业工具。", "通用 AI 已不再进行开发。"]
    answer: 1
    explanation: "虽然 OpenAI 或 Anthropic 的模型非常强大，但像 AISLE 这样专注于安全分析的系统可以在特定领域展现出更卓越的成果。"
lang: zh-cn
ref: 2026-09-02-Six-curl-CVEs-after-OpenAI-and-Anthropic-came-back-with-zero
---

## 寻找 25 年安全漏洞的“安全侦探”AI

试想一下：你 25 年来每天早上都仔细锁好房门出门，结果却发现门锁背面的螺丝从一开始就根本没拧紧。你会是什么心情？既会感到后怕，或许也会因为 25 年来竟然平安无事而感到一丝庆幸吧。

最近，全球开发者都在使用的数据传输工具“curl”（一种通过多种协议安全传输数据的工具）就发生了这样的事情。更令人震惊的是，发现这个深层“安全漏洞”的并不是人类，而是一个专门针对安全领域进行训练的“专用 AI 系统”。特别是，该系统发现了 6 个连 OpenAI 或 Anthropic 等巨头开发的知名“通用 AI”模型都未能察觉的致命漏洞。

### 这为什么重要？

“curl”这个名字对普通人来说可能有些陌生，但事实上，你每天都在使用它。无论是我们常用的智能手机 App、笔记本电脑的软件更新，还是各种 IoT（物联网）设备在传输数据时，内部都在使用 curl 或相关技术 libcurl（用于让程序具备 curl 功能的库）[Source 3]。

这意味着，该工具存在的安全漏洞可能导致我们日常使用的数十亿台设备面临黑客攻击的风险。此次由安全专用 AI 平台 AISLE 发现的问题中，甚至包含了认证绕过（即无需通过安全验证即可非法入侵）等致命 Bug，险些成为数据泄露的通道 [Source 5]。

### 简而言之：“全能选手”与“专家”的区别

这一结果展现了 AI 世界有趣的一面。OpenAI 或 Anthropic 的模型是掌握世间所有知识的“全能选手”。无论是写作、编程还是翻译外语，它们都应付自如。然而，此次 curl 安全调查则需要像“精密宝石加工”一样深入且狭窄的专业知识。

打个比方，通用 AI 就像从高空快速俯瞰广袤森林的无人机。它在把握森林整体地貌方面表现出色，却很难发现隐藏在森林地面落叶下的小昆虫（安全漏洞）。相反，像 AISLE 这样拿着放大镜和镊子仔细搜寻地面的昆虫学家，能够找到无人机忽略的细小生物 [Source 1, Source 6]。实际上，在这次案例中，通用 AI 模型要么只找到了 1 个，要么毫无建树，而 AISLE 却发现了 6 个漏洞，展现了压倒性的差距 [Source 6]。

### 现状：curl 历史上最古老的漏洞

在 AISLE 发现的漏洞中，有一个编号为“CVE-2026-8932”的问题 [Source 3, Source 5]。这个 Bug 从 2001 年 3 月起就一直存在。在漫长的 25 年里，无数专业开发者审视并使用过这些代码，却始终没有人察觉到其中隐藏的细微逻辑错误 [Source 5, Source 7]。

得益于此，curl 在此次安全补丁更新中总共记录了 18 个 CVE（公开的安全漏洞列表）[Source 3, Source 6]。这将成为 curl 项目历史上规模最大的安全改进工作之一 [Source 5]。

### 未来将会怎样？

这一事件将彻底改变我们看待 AI 的视角。未来，竞争的重心将不再仅仅是打造“更聪明的 AI”，而是打造“在特定领域钻研得更精深的 AI”[Source 1]。

未来，不仅是在安全领域，在医学、法律、半导体设计等极其具体和专业的领域，拥有比人类更锐利双眼的“专家 AI”将层出不穷。我们日常使用的软件也将受到这些专家 AI 的持续监测，变得比以往更加安全。不过，对于我们所使用的 AI 具备何种能力，以及该模型“忽略”了什么，人类仍需保持警惕并时刻关注。

---

## MindTickleBytes 的 AI 记者视角

当 OpenAI 或 Anthropic 在通用大模型性能竞争中争奇斗艳时，在无形之处解决安全问题的专用 AI 的成长令人惊叹。如今，AI 不再仅仅是“输出创意结果的工具”，更进化成了能够找出我们 25 年来未曾察觉的代码缝隙的“数字守卫者”。

## 参考资料

1. [AISLE Discovered Six curl CVEs After OpenAI and Anthropic Found Zero](https://aisle.com/blog/aisle-discovered-six-curl-cves-after-openai-and-anthropic-found-zero)
2. [AISLE Discovers 6 CVEs in curl, Including Oldest Issue Ever Reported](https://aisle.com/blog/aisle-discovers-6-new-cves-in-curl-including-the-oldest-security-issue-ever-reported)
3. [Aisle Discovers 6 New CVEs in Curl, Including the Oldest Issue Ever Reported](https://news.chathome.org/news/aisle-discovers-6-new-cves-in-curl-including-the-oldest-issue-ever-reported-T7C6scli?locale=en)
5. [Curl Fixes a 25-Year-Old Bug in Its Largest CVE Release Yet](https://securityaffairs.com/194220/security/curl-fixes-a-25-year-old-bug-in-its-largest-cve-release-yet.html)
6. [AISLE Discovers 6 New CVEs in curl, Including the Oldest Issue Ever Reported](https://vuink.com/post/nvfyr-d-dpbz/blog/aisle-discovers-6-new-cves-in-curl-including-the-oldest-issue-ever-reported)
7. [Curl's 6 New CVEs Hit AI Toolchains - PromptZone](https://www.promptzone.com/xiu_lynch/curls-6-new-cves-hit-ai-toolchains-37ni)