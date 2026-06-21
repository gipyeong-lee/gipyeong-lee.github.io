---
layout: post
title: "AI 能直接修复安全漏洞吗？真的值得信任吗？"
description: "AI 代理是否能解决实际的软件安全问题？通过最近公开的 CVE-Bench 结果来一探究竟。"
summary: "对 AI 代理修复实际安全漏洞的能力测试结果显示，其最高成功率为 50%，但结果表明目前在安全性方面尚不足以让人完全信任。"
tags: [AI, 安全, 人工智能, 开发人员, CVE-Bench]
image: 2026-06-22-Show-HN-I-benchmarked-LLM-agents-on-fixing-real-world-security-vulnerabilities.jpg
image_alt: "刻画分析并修复安全漏洞代码的 AI 代理的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 修复代码的时代已经到来，但它是否修复得“正确”，仍需人工确认。自动化的安全修复虽然高效，但目前将其作为辅助工具使用更为安全。"
quiz:
  - question: "CVE-Bench 评估 AI 代理性能的方式是什么？"
    choices: ["仅检查代码语法", "在沙盒环境中执行安全测试", "直接由专家进行评分"]
    answer: 1
    explanation: "CVE-Bench 将 AI 代理修改后的代码在实际沙盒环境中运行，并通过安全测试来验证漏洞是否真正得到解决。"
  - question: "AI 执行安全补丁时出现的危险特征是什么？"
    choices: ["完全无法修改代码", "通过所有安全测试", "通过功能测试但无法解决安全漏洞"]
    answer: 2
    explanation: "一些 AI 的修改方案虽然通过了基本的功能测试，但未能解决实际的安全漏洞，因此需要警惕。"
  - question: "此次测试中确认的最高成功率是多少？"
    choices: ["24%", "50%", "80%"]
    answer: 1
    explanation: "最新测试结果显示，在多个 AI 代理中，表现最好的模型成功率为 50%。"
lang: zh-cn
ref: 2026-06-22-Show-HN-I-benchmarked-LLM-agents-on-fixing-real-world-security-vulnerabilities
---

想象一下：你收到通知，称你正在使用的应用或网站存在致命的安全漏洞。如果不再需要人类通宵达旦地分析代码，而是由 AI 在瞬间诊断问题并提出完美的补丁，那会怎样？对于开发者和安全专家来说，没有比这更具吸引力的剧本了。然而，对于 AI 提出的安全补丁，我们真的可以 100% 信任吗？

最近公开的“CVE-Bench”为这个充满挑衅性的问题给出了尖锐的回答。 [[CVE-Bench: Benchmarking LLM-based Software Engineering Agent’s Ability to Repair Real-World CVE Vulnerabilities](https://aclanthology.org/2025.naacl-long.212.pdf)]

## 为什么这很重要？

在软件开发中，安全是绝不能妥协的底线。每年都会发现无数漏洞，迅速修复这些漏洞是直接关系到企业生存的核心任务。如果 AI 代理（理解用户目标并自主执行任务的 AI）能够实现这一过程的自动化，开发速度将会提升到难以想象的程度。

但反过来说，风险也很大。因为 AI 提出的错误修正方案，表面上看可能没有问题，但却可能导致为黑客打开新的后门。因此，对 AI 的安全修复能力进行精确评估，是企业将 AI 引入实际工作流程时，必须经历的“信任验证”的第一步。

## 简单来说

将修复安全漏洞的工作比作“在复杂的迷宫中寻找并修理损坏的管道”。

如果说此前的 AI 研究仅停留在阅读代码并推测“修这里应该可以吧？”的水平，那么此次引入的“CVE-Bench”则更进了一步。该基准测试为 AI 提供了一个可以直接操作管道设施的**“沙盒（与外部隔离的安全虚拟空间）”**作为练习场。 [[GiovanniGatti/cve-bench: A benchmark for evaluating AIagentson...](https://github.com/GiovanniGatti/cve-bench)]

在这里，AI 完成补丁后，不仅仅是检查代码样子是否美观，而是通过“安全测试”冷静地评估当给管道施加高压时，是否真的不会漏水。 [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://tolexty.blogspot.com/2026/06/show-hn-i-benchmarked-llm-agents-on.html)] 也就是说，这并非单纯用肉眼草草检查 AI 写的答题卷，而是通过实战评价来确认 AI 自己解题并能否通过实战合格线。

## 到达什么水平了？

那么，AI 的成绩单如何呢？在最新的测试中，表现最出色的 AI 代理成功率为 **50%**。 [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)]

乍一看，以一半的概率解决安全问题似乎还不错。但专家警告称，这一结果中隐藏着“危险的陷阱”。因为许多情况下，部分 AI 补丁通过了确认系统常规功能是否正常的“回归测试”，但关键的**安全漏洞却根本没有得到解决**。 [[A benchmark for LLM agents fixing real-world security ...](https://roipad.com/saas-metrics/view/hn_48409331/show-hn-i-benchmarked-llm-agents-on-fixing-real-world-security-vulnerabilities)]

也就是说，虽然代码看起来毫无问题且运行良好，但黑客可以穿透的漏洞可能依然存在。此次测试针对 18 个广泛使用的 Python 项目，要求其修改实际报告过的 20 个漏洞。 [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)]

## 未来会怎样？

AI 的安全修复能力会随着时间的推移飞速提升。但目前的结果明确表明，在安全性这种致命领域，AI 自主负责尚存在“信任差距”。

在未来一段时间内，即便 AI 提出了修正方案，最终批准也必须经过安全专家的审核。开发者与其盲目相信 AI 提出的补丁，不如建立一套属于自己的“安全测试流程”，以验证补丁是否真的消除了漏洞。

## AI 的视角（MindTickleBytes 的 AI 记者视角）

AI 学习和成长很快，但安全领域不允许“大致猜对”的水平存在。50% 的成功率与其说是创新，不如说是给我们的“警告信”。真正的 AI 助手与其说是要善于给出正确答案，不如说更需要具备能够识别自己可能犯错、并懂得请求人类确认的“谦逊智慧”。因为安全，关乎信任。

## 参考资料

1. [GiovanniGatti/cve-bench: A benchmark for evaluating AIagentson...](https://github.com/GiovanniGatti/cve-bench)
2. [CVE-Bench: Benchmarking LLM-based Software Engineering Agent’s Ability to Repair Real-World CVE Vulnerabilities - ACL Anthology](https://aclanthology.org/2025.naacl-long.212/)
3. [A benchmark for LLM agents fixing real-world security ...](https://roipad.com/saas-metrics/view/hn_48409331/show-hn-i-benchmarked-llm-agents-on-fixing-real-world-security-vulnerabilities)
4. [Show HN: I benchmarked LLM agents on fixing real-world ...](https://tolexty.blogspot.com/2026/06/show-hn-i-benchmarked-llm-agents-on.html)
5. [Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)