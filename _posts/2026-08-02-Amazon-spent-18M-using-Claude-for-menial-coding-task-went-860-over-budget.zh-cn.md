---
layout: post
title: "AI 맡긴 '단순 반복 업무'로 24억 원 날린 사연, 왜일까?"
description: "通过亚马逊在使用AI Claude的内部项目中超支860%，浪费180万美元的事件，探讨AI引入中隐藏的成本及管理的重要性。"
summary: "亚马逊在利用AI Claude进行简单业务自动化的项目中，在5个月内支出了超过预算860%的180万美元（约合24亿韩元），且未能推出该项目。"
tags: [AI, 技术, 亚马逊, 成本, 自动化]
image: 2026-08-02-Amazon-spent-18M-using-Claude-for-menial-coding-task-went-860-over-budget.jpg
image_alt: "办公桌上堆积的文件和旁边放着的绘有人工智能标志的智能手机。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "此次事件表明，如果AI模型的“基于Token收费”结构设计得不够高效，可能会造成巨大的财务漏洞。建立成本追踪体系与引入技术同样至关重要。"
quiz:
  - question: "亚马逊在此次事件中为AI自动化项目投入的成本是多少？"
    choices: ["18万美元", "180万美元", "860万美元"]
    answer: 1
    explanation: "亚马逊在失败的Claude AI项目中总共支出了180万美元。"
  - question: "此次AI项目超支了多少预算？"
    choices: ["500%", "860%", "1,800%"]
    answer: 1
    explanation: "该项目支出超过了最初设定预算的860%。"
  - question: "亚马逊在本项目中的一大管理失误是什么？"
    choices: ["AI模型选择错误", "5个月内未能察觉预算超支", "开发人员不足"]
    answer: 1
    explanation: "亚马逊在长达5个月的时间里完全没有察觉到预算超支的情况。"
lang: zh-cn
ref: 2026-08-02-Amazon-spent-18M-using-Claude-for-menial-coding-task-went-860-over-budget
---

想象一下。你以为雇佣了一名聪明的实习生，可以帮你处理办公室角落里琐碎的文件整理工作。然而，5个月后当你确认时，却发现这位实习生不仅没有整理文件，反而把整个办公室的办公用品预算超支了8倍，而且本该完成的工作一件也没做完。如果是你，会有什么感受？

最近，全球最大的电子商务企业亚马逊就发生了类似荒唐的事情。这是一起试图利用人工智能（AI）提高工作效率，却反过来造成巨大财务亏损的事件。

### 这为何重要？

此次事件不仅是“大企业失误”的花边新闻，更清楚地展现了我们应该如何看待和引入AI。许多企业和个人期待引入AI就能无条件降低成本，但此次案例警告我们：“缺乏管理的AI反而可能成为无法控制的成本怪兽。”

现代AI模型以“Token（令牌）”为单位计算成本。Token可以简单理解为AI读取和理解数据时使用的最小单位。这就像打开水龙头用水一样，根据使用量付费；如果管理疏忽，一个小失误就可能导致天文数字般的成本。

### 浅显易懂的解释

为什么会发生这种情况呢？此次项目是亚马逊内部试图利用名为“Claude Sonnet”的AI模型，实现匹配商品数据与作者信息的“简单重复工作”自动化 [[参考资料 1](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics), [参考资料 11](https://www.gadgetreview.com/an-amazon-internal-project-used-claude-sonnet-to-match-book-authors-and-accidentally-burned-1-8-million)]。

打个比方，就像我们本想打车去5分钟路程的便利店，结果司机走错了路，绕着地球开了5个月，还不停地跳表。AI在不断燃烧“Token”作为燃料执行任务，但系统却没有停止，持续产生费用 [[参考资料 11](https://www.gadgetreview.com/an-amazon-internal-project-used-claude-sonnet-to-match-book-authors-and-accidentally-burned-1-8-million)]。最终，这个“实习生AI”连像样的成果都没拿出来，项目甚至都没能发布 [[参考资料 4](https://betanews.com/article/amazon-claude-ai-cost-overrun/), [参考资料 8](https://www.ghacks.net/2026/07/31/leaked-amazon-documents-detail-1-8-million-overrun-on-a-single-claude-ai-task-missed-for-five-months)]。

### 现状

内部文件显示，亚马逊因该项目支出的费用高达180万美元，约合24亿韩元 [[参考资料 1](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics), [参考资料 9](https://theoutpost.ai/news-story/amazon-s-1-8-million-claude-blunder-exposes-hidden-costs-of-ai-deployments-across-tech-giants-29193/)]。这一金额比最初计划的预算足足超出了860% [[参考资料 6](https://cybernews.com/ai-news/amazon-spending-ai-claude-cost/), [参考资料 7](https://aiweekly.co/alerts/amazon-engineers-flag-18m-claude-bill-860-over-budget)]。

更令人震惊的是，亚马逊在长达5个月的时间里完全没有察觉到这次严重的预算浪费 [[参考资料 4](https://betanews.com/article/amazon-claude-ai-cost-overrun/), [参考资料 10](https://www.linkedin.com/posts/vasiliy-radostev-063947_leaked-amazon-documents-detail-18-million-activity-7489089129792696320-fRDT)]。这暗示了巨型企业内部的AI管理体系存在巨大漏洞 [[参考资料 11](https://www.gadgetreview.com/an-amazon-internal-project-used-claude-sonnet-to-match-book-authors-and-accidentally-burned-1-8-million)]。

### 未来走向

此次案例给许多企业留下了重要教训：在引入AI时，“成本监控”应先行于“技术成果” [[参考资料 12](https://news.ycombinator.com/item?id=49115075)]。预计未来许多企业将针对AI项目引入更严格的实时成本追踪系统。现在，“AI使用得有多好”固然重要，但“AI使用费管理得有多聪明”也将成为企业的核心竞争力。

### MindTickleBytes的AI记者视角

此次事件不仅仅是亚马逊浪费金钱的案例，更是象征着AI便利性背后隐藏的“付费陷阱”。企业在引入AI时，必须首先准备好能够监控“谁、在何时、何地、使用了多少Token”的智能管理系统。因为即便技术如同魔法一般，若无法妥善管理，随时都可能成为掏空我们腰包的麻烦。

## 参考资料

1. [亚马逊因使用Claude进行琐碎编码任务意外支出180万美元，预算超支860% — 在亚马逊内部AI使用指标中发现了“灾难性昂贵”的编码失误 | Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics)
2. [Reddit上的r/technology：亚马逊因使用Claude进行琐碎编码任务意外支出180万美元，预算超支860% — 在亚马逊内部AI使用指标中发现了“灾难性昂贵”的编码失误](https://www.reddit.com/r/technology/comments/1vay198/amazon_accidentally_spent_18_million_using_claude/)
3. [亚马逊因使用Claude进行琐碎编码任务意外支出180万美元，超支860% — '灾难性...](https://finance.yahoo.com/technology/ai/articles/amazon-accidentally-spent-1-8-160825610.html)
4. [亚马逊180万美元的Claude AI部署超支860%](https://betanews.com/article/amazon-claude-ai-cost-overrun/)
5. [亚马逊在失败的Claude AI Token上意外支出180万美元 | Cybernews](https://cybernews.com/ai-news/amazon-spending-ai-claude-cost/)
6. [亚马逊工程师标记180万美元Claude账单，超预算860% | AI Weekly](https://aiweekly.co/alerts/amazon-engineers-flag-18m-claude-bill-860-over-budget)
7. [泄露的亚马逊文件详细说明了单个Claude AI任务超支180万美元，且持续五个月未被发现 - gHacks Tech News](https://www.ghacks.net/2026/07/31/leaked-amazon-documents-detail-1-8-million-overrun-on-a-single-claude-ai-task-missed-for-five-months/)
8. [在单个Claude部署上花费800万美元，超预算860%。](https://theoutpost.ai/news-story/amazon-s-1-8-million-claude-blunder-exposes-hidden-costs-of-ai-deployments-across-tech-giants-29193/)
9. [泄露的亚马逊文件详细说明了单个...超支180万美元](https://www.linkedin.com/posts/vasiliy-radostev-063947_leaked-amazon-documents-detail-18-million-activity-7489089129792696320-fRDT)
10. [亚马逊内部项目使用Claude Sonnet... - Gadget Review](https://www.gadgetreview.com/an-amazon-internal-project-used-claude-sonnet-to-match-book-authors-and-accidentally-burned-1-8-million)
11. [亚马逊因使用Claude进行琐碎编码任务意外支出180万美元...](https://news.ycombinator.com/item?id=49115075)