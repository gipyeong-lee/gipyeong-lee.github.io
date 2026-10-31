---
layout: post
title: "AI 减缓了软件开发速度？PostgreSQL 19 发布延期背后的异常情况"
description: "AI 代码审查发现的漏洞多于人类开发人员，导致 PostgreSQL 19 发布延期并大幅削减核心功能。"
summary: "由于 AI 辅助代码审查发现的缺陷远超预期，PostgreSQL 开发团队为确保质量，决定推迟发布并缩减功能规模。"
tags: [PostgreSQL, AI, LLM, 软件开发, 数据库]
image: 2026-10-31-PostgreSQL-19-Running-Behind-Schedule-Due-to-AILLM-Burden.jpg
image_alt: "电脑屏幕上排列着复杂的代码，一道象征人工智能的亮光扫过。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "与 AI 将提高开发效率的预期相反，这一案例生动地展示了 AI 如何通过提高质量标准，在开发流程中创造出新的瓶颈。"
quiz:
  - question: "PostgreSQL 19 发布延期的主要原因是什么？"
    choices: ["人类开发人员短缺", "处理 AI 代码审查发现的大量漏洞负担沉重", "服务器基础设施问题"]
    answer: 1
    explanation: "基于 AI 的代码审查发现了比以往更多的缺陷，为了解决这些问题并保持质量，发布日期被迫延期。"
  - question: "此次 PostgreSQL 19 发布中被搁置的功能规模有多大？"
    choices: ["1~2 个", "8~10 个", "50 个以上"]
    answer: 1
    explanation: "大约 8 到 10 个主要功能被从 PostgreSQL 19 中剔除，并推迟到下一个版本 v20。"
  - question: "PostgreSQL 提交者 Peter Eisentraut 是如何描述当前情况的？"
    choices: ["AI 编写的代码太多", "基于 LLM 的代码审查发现漏洞的速度超过了人类修复的速度", "AI 代替了所有开发工作"]
    answer: 1
    explanation: "Peter Eisentraut 指出，基于 LLM 的代码审查正在以快于人类修正速度的频率发现漏洞。"
lang: zh-cn
ref: 2026-10-31-PostgreSQL-19-Running-Behind-Schedule-Due-to-AILLM-Burden
---

想象一下，你正在构建一个每天被数万名用户信赖的“数字金库”——数据库系统。通常情况下，每年秋天你都会推出一个功能丰富的新版本。但这次情况不同了。随着聪明的“AI 审查员”加入，开发人员以前未曾注意到的细微缝隙（漏洞）被大量挖掘出来。最终，开发团队决定推迟发布，并被迫放弃了原本雄心勃勃准备的功能，留待后续版本实现。

这就是深受全球开发者信赖的数据库系统——PostgreSQL 的遭遇。此次 PostgreSQL 19 发布延期事件，揭示了 AI 与软件开发碰撞时产生的一种既引人入胜又令人痛苦的现象。

## 为什么这很重要？

在软件开发中，漏洞与代码形影不离。但如果发现漏洞的速度远超人类修复的速度，会发生什么呢？此次事件不仅是一个“发布延期”的消息，它更预示着 **AI 时代的软件质量标准正在发生根本性的转变**。[参考资料 16](https://www.securitylab.ru/news/578886.php)

过去，由于是人类手动审查代码，除非是极严重的错误，否则一些小问题往往会被忽略。但现在，随着 AI 对开发全过程进行细致监控，开发团队必须通过比以往更严格的审核。这对于我们所使用的众多数字服务的稳定性来说是个好消息，意味着可靠性将得到大幅提升；但同时，这对开发人员而言，也变成了一项沉重的负担。[参考资料 8](https://www.phoronix.com/news/PostgreSQL-19-Late)

## 深入浅出

让我们用一个简单的比喻来解释“代码审查”过程。想象你完成了一个精美的拼图。过去，你的朋友可能只是扫一眼说：“嘿，那块拼图好像不太对劲。”而现在，就如同 **AI 这台“超能力显微镜”** 对整幅拼图进行了扫描，甚至能找出 0.1 毫米的误差。[参考资料 9](https://digitalbourgeois.tistory.com/3844)

在此次 PostgreSQL 开发过程中，基于 LLM（大语言模型）的 AI 代码审查工具抛出了超过 40 份详细的缺陷报告。[参考资料 11](https://tech-insider.org/postgresql-19-delayed-ai-review-bugs-2026/) AI 工作得如此勤勉而精准，以至于人类开发人员根本没有足够的时间来修复所有问题。

简单来说，这就像来了一位极其严格的 AI 老师，因为作业检查得太细致，导致全班进度跟不上了。最终，PostgreSQL 提交者 Peter Eisentraut 指出：“AI 发现代码缺陷的速度，已经超过了人类修复它们的速度。”[参考资料 10](https://www.thinkfacility.com/blog/postgresql-19-delayed-llm-code-review-reverts/) 为了在截止日期前完成任务，开发团队最终决定 **忍痛割爱，删减了 8 到 10 个主要功能，并将发布日期推迟至 11 月 19 日**。[参考资料 12](https://www.metirai.com/blog/postgresql-19-delayed-llm-code-review-reverted-features-2026), [参考资料 13](https://www.explainx.ai/blog/postgres-19-delayed-ai-code-review-bugs-reverted-features-2026)

## 当前进展

原定于 9 月至 10 月间发布的 PostgreSQL 19，目前正以 11 月 19 日公开发布为目标进行最后的冲刺。[参考资料 5](https://t.me/canal_telegram_proyectotictac/218818), [参考资料 14](https://ai-manual.ru/article/postgresql-19-perenesli-na-19-noyabrya-chto-sluchilos-s-relizom-i-pri-chyom-tut-llm-revyu-koda/) 在此次被搁置的功能中，包含了许多备受期待的关键特性，例如“属性图查询（SQL/PGQ）”，这令不少等待该功能的开发者感到遗憾。[参考资料 2](https://www.youtube.com/watch?v=0KsJ7UUezgw), [参考资料 12](https://www.metirai.com/blog/postgresql-19-delayed-llm-code-review-reverted-features-2026)

这一变化不仅影响了数据库社区，还波及了数千家已经制定好数据库迁移时间表的企业。[参考资料 15](https://dzen.guru/news/reliz-postgresql-19-perenesli-na-19-noyabrya-revyu-s-pomoshchyu-llm-vskryло-desy) 尽管如此，PostgreSQL 开发团队将“质量”置于首位的理念，通过此次事件再次得到了印证。[参考资料 6](https://neon.com/blog/postgres-19-is-late-and-its-ais-fault)

## 未来展望

此次推迟的功能预计将在下一个版本 PostgreSQL 20 中亮相。有趣的是，就在几个月前，开发者们还预测 PostgreSQL 20 将专注于漏洞修复而不会引入新功能。[参考资料 4](https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471) 但由于此次事件，业界对 v20 的期待与关注度显著提升。

我们曾期待 AI 能帮助我们更快地“构建”软件，但现实却是 AI 正在更细致地“验证”我们所构建的软件，从而给开发周期带来了意想不到的变化。未来的软件开发生态系统将获得更高的稳定性，但这也意味着开发人员将面临新的挑战——即如何处理好 AI 提出的每一项“家庭作业”。

### MindTickleBytes AI 记者观察

AI 锲而不舍地寻找人类错误的模样，就像有数百名严厉的老练开发者在后台待命。那些人类可能会忽略的小问题，在 AI 面前无所遁形。如果能平稳度过这个转型期，我们所处的数字世界将会比以往任何时候都更加坚固与安全。对于开发者来说，这虽然是段艰苦的时光，但我们不妨将其视为为了交付更高质量技术成果所必须经历的“成长痛”。

## 参考资料

1. [PostgreSQL: Release Notes](https://www.postgresql.org/docs/release/19.0/)
2. [Why PostgreSQL 19 Pulled Major Features at the Finish Line - YouTube](https://www.youtube.com/watch?v=0KsJ7UUezgw)
3. [Postgres 19 delayed after AI reviewers find more bugs than humans...](https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471)
4. [Canal: Linuxverso + Educación STEAM – Telegram](https://t.me/canal_telegram_proyectotictac/218818)
5. [Postgres 19 is late, and it's AI's fault - Neon](https://neon.com/blog/postgres-19-is-late-and-its-ais-fault)
6. [Заглядывая в будущее: Postgres 19. REPACK, SQL/PGQ... / Хабр](https://habr.com/ru/companies/haulmont/articles/1061338/)
7. [PostgreSQL 19 Running Behind Schedule Due To AI/LLM Burden](https://www.phoronix.com/news/PostgreSQL-19-Late)
8. [PostgreSQL 19 출시 지연과 기능 보류: AI 코드 리뷰가 바꾼 소프트웨...](https://digitalbourgeois.tistory.com/3844)
9. [PostgreSQL 19 loses 8 to 10 features, and a developer points ...](https://www.thinkfacility.com/blog/postgresql-19-delayed-llm-code-review-reverts/)
10. [PostgreSQL 19 Delayed: AI Review Finds 40 Bugs [2026]](https://tech-insider.org/postgresql-19-delayed-ai-review-bugs-2026/)
11. [PostgreSQL 19 Slips to November After LLM-Assisted Review ...](https://www.metirai.com/blog/postgresql-19-delayed-llm-code-review-reverted-features-2026)
12. [Postgres 19 Delayed to Nov 19: AI Review Caused 8-10 Reverts ...](https://www.explainx.ai/blog/postgres-19-delayed-ai-code-review-bugs-reverted-features-2026)
13. [PostgreSQL 19 перенесли на 19 ноября: что случилось... | AiManual](https://ai-manual.ru/article/postgresql-19-perenesli-na-19-noyabrya-chto-sluchilos-s-relizom-i-pri-chyom-tut-llm-revyu-koda/)
14. [Релиз PostgreSQL 19 перенесли на 19 ноября: ревью с помощью...](https://dzen.guru/news/reliz-postgresql-19-perenesli-na-19-noyabrya-revyu-s-pomoshchyu-llm-vskryло-desy)
15. [PostgreSQL 19 не выдержал новой планки качества.](https://www.securitylab.ru/news/578886.php)
16. [PostgreSQL 19: Часть 1 или Коммитфест 2025-07 / Хабр](https://habr.com/ru/companies/postgrespro/articles/984580/)