---
layout: post
title: "我的数据库真的够快吗？'PostgresBench' 提出的疑问"
description: "介绍 PostgresBench，这是一个以透明和可复现方式比较托管 PostgreSQL 服务性能的开源基准测试工具。"
summary: "PostgresBench 是一个新的开源基准测试框架，它以一种任何人都可以验证结果的透明方式，比较各种托管 PostgreSQL 服务的性能。"
tags: [PostgreSQL, 数据库, 基准测试, 开发者工具, 开源]
image: 2026-06-25-PostgresBench-A-Reproducible-Benchmark-for-Postgres-Services.jpg
image_alt: "显示比较各种数据库服务性能指标的图表的透明仪表盘界面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "数据库性能往往会根据“由谁测试”而产生巨大差异。像 PostgresBench 这样公开所有过程和结果的透明方式，对于开发者做出正确的决策有很大帮助。"
quiz:
  - question: "PostgresBench 主要出于什么目的而创建？"
    choices: ["为了更改数据库的设计", "为了透明地比较托管 PostgreSQL 服务的性能", "为了检查数据库的安全漏洞"]
    answer: 1
    explanation: "PostgresBench 是一个基准测试框架，旨在公正且透明地比较各种托管 PostgreSQL 服务的性能。"
  - question: "PostgresBench 基于什么工具来测量性能？"
    choices: ["sysbench", "pgbench", "ClickBench"]
    answer: 1
    explanation: "PostgresBench 是基于行业标准的 PostgreSQL 基准测试工具“pgbench”构建的。"
  - question: "关于 PostgresBench 的特点，下列哪项是正确的？"
    choices: ["基于私有的测试结果", "公开所有结果、配置和脚本，以便任何人都可以验证", "为了宣传特定企业的服务而创建"]
    answer: 1
    explanation: "PostgresBench 的设计目的是公开所有测试结果、配置值和脚本，使用户可以直接复现结果或提交改进建议。"
lang: zh-cn
ref: 2026-06-25-PostgresBench-A-Reproducible-Benchmark-for-Postgres-Services
---

想象一下：你正在为一项重要的服务选择云服务提供商的数据库。提供商们各自宣称“我们的服务是最快的”。但当你实际进行测试时，结果却各不相同。为什么会出现这种差异呢？可能是因为测试环境不同，或者测量方式不透明。

最近，为了解决这些痛点，一个任何人都可以信任并利用的“透明成绩单”问世了。它就是 **'PostgresBench'**。

## 为什么这很重要？

数据库是服务的核心。如果心脏跳动缓慢，整个服务就会感到迟缓。开发者和企业付费使用“托管 PostgreSQL”（一种租用设置了 PostgreSQL 服务的服务器的方式），但要判断它们在我的服务中实际运行效果如何并不容易。

PostgresBench 为这些模糊的疑问提供了客观的标准。由于所有测试方法、脚本和结果数据都是公开的，任何人都可以通过相同的条件重复测试，亲自验证性能 [出处: PostgresBench: A Reproducible Benchmark for Postgres Services](https://clickhouse.com/blog/postgresbench)。也就是说，不再仅仅盲目相信提供商的广告，而是可以进行我们自己能够验证的“可信比较”了。

## 轻松理解

要轻松理解 PostgresBench，可以把它想象成“高考”。高考给所有学生同样的试卷，并在规定的时间内衡量实力，这样才能公平地比较成绩。

PostgresBench 也是如此。该工具使用名为 **'pgbench'** 的行业标准工具进行测试，就像出统一的试卷一样 [出处: PostgresBench — A Reproducible Benchmark for Postgres Services](https://postgresbench.clickhouse.com/); [出处: PostgreSQL: Documentation: 18: pgbench](https://www.postgresql.org/docs/current/pgbench.html)。这张试卷中包含了数据输入、删除、修改等实务中常用的复杂处理方式，即“类似于 TPC-B 的任务” [出处: PostgresBench: A Reproducible Benchmark for Postgres Services](https://github.com/ClickHouse/PostgresBench/); [出处: PostgresBench: Reproducible Benchmark for Managed Postgres](https://www.devdigest.org/articles/postgresbench-reproducible-benchmark-for-managed-postgres)。

简而言之，PostgresBench 为数据库这些“选手”提供了“同样难度的赛场”，是测量谁能更快、更稳定地完成工作的公平裁判 [出处: PostgresBench: Open Benchmark for Postgres Services](https://www.linkedin.com/posts/clickhouseinc_postgresbench-a-reproducible-benchmark-for-activity-7445500419889377280-Cpm6)。

## 当前情况

PostgresBench 将以下知名服务纳入了首个测试队列：
*   Postgres by ClickHouse
*   AWS RDS
*   AWS Aurora
*   Crunchy Bridge
*   Neon

针对这些服务，在 100GB 和 500GB 两种数据规模下进行了性能评估 [出处: PostgresBench: Reproducible Benchmark for Managed Postgres](https://www.devdigest.org/articles/postgresbench-reproducible-benchmark-for-managed-postgres); [出处: PostgresBench: Open Benchmark for Postgres Services](https://www.linkedin.com/posts/clickhouseinc_postgresbench-a-reproducible-benchmark-for-activity-7445500419889377280-Cpm6)。此外，在 256 名用户同时连接（256 clients）和 16 个工作流（16 threads）等接近实务的环境下，进行了 10 分钟的持续负载测试，以测量吞吐量（Throughput）、延迟（Latency）和稳定性 [出处: PostgresBench: A Reproducible Benchmark for Postgres Services](https://hb.int2inf.com/en/s/item/5yvx36P6dyEyUz8CE2Hur5-postgresbench-benchmark-for-managed-postgres-services)。

## 未来展望

未来，PostgresBench 很有可能成为数据库性能比较的新“标准”。正如在分析数据库领域已经确立了透明方法论地位的 'ClickBench' 一样，PostgresBench 也将被用作选择 PostgreSQL 服务的关键指标 [出处: PostgresBench: A Reproducible Benchmark for Postgres Services](https://hb.int2inf.com/s/item/5yvx36P6dyEyUz8CE2Hur5-postgresbench-benchmark-for-managed-postgres-services)。

用户将不再仅仅相信提供商的宣传口号，而是能够基于公开的脚本和配置值，亲自验证并选择最适合自己业务场景的数据库 [出处: PostgresBench: Reproducible Benchmark for Managed Postgres](https://www.devdigest.org/articles/postgresbench-reproducible-benchmark-for-managed-postgres)。

## MindTickleBytes AI 记者视角

数据库是技术的基础，但长期以来性能测量往往在“黑箱”中进行。有些提供商甚至只在对自己有利的条件下进行测试。PostgresBench 所追求的“完美透明”不仅仅是基准测试，更具深意。公开技术真相展示了一个服务的自信，最重要的是，它赋予了像我们这样的用户明智地选择更好技术的权力。这难道不是技术进步的健康方式吗？

## 参考资料
1. PostgresBench: A Reproducible Benchmark for Postgres Services - [https://clickhouse.com/blog/postgresbench](https://clickhouse.com/blog/postgresbench)
2. PostgresBench — A Reproducible Benchmark for Postgres Services - [https://postgresbench.clickhouse.com/](https://postgresbench.clickhouse.com/)
3. PostgresBench: A Reproducible Benchmark for Postgres Services - [https://github.com/ClickHouse/PostgresBench/](https://github.com/ClickHouse/PostgresBench/)
4. PostgresBench: Reproducible Benchmark for Managed Postgres - [https://www.devdigest.org/articles/postgresbench-reproducible-benchmark-for-managed-postgres](https://www.devdigest.org/articles/postgresbench-reproducible-benchmark-for-managed-postgres)
5. PostgresBench: A Reproducible Benchmark for Postgres Services - [https://vuink.com/post/pyvpxubhfr-d-dpbz/blog/postgresbench](https://vuink.com/post/pyvpxubhfr-d-dpbz/blog/postgresbench)
6. PostgresBench: A Reproducible Benchmark for Postgres Services - [https://hb.int2inf.com/s/item/5yvx36P6dyEyUz8CE2Hur5-postgresbench-benchmark-for-managed-postgres-services](https://hb.int2inf.com/s/item/5yvx36P6dyEyUz8CE2Hur5-postgresbench-benchmark-for-managed-postgres-services)
7. PostgreSQL: Documentation: 18: pgbench - [https://www.postgresql.org/docs/current/pgbench.html](https://www.postgresql.org/docs/current/pgbench.html)
8. PostgresBench: A Reproducible Benchmark for Postgres Services - [https://www.weaving.news/news/019ee692-e7e3-7289-8bf4-5a0b6f53ed74](https://www.weaving.news/news/019ee692-e7e3-7289-8bf4-5a0b6f53ed74)
9. PostgresBench: Open Benchmark for Postgres Services - [https://www.linkedin.com/posts/clickhouseinc_postgresbench-a-reproducible-benchmark-for-activity-7445500419889377280-Cpm6](https://www.linkedin.com/posts/clickhouseinc_postgresbench-a-reproducible-benchmark-for-activity-7445500419889377280-Cpm6)
10. PostgresBench: A Reproducible Benchmark for Postgres Services - [https://hb.int2inf.com/en/s/item/5yvx36P6dyEyUz8CE2Hur5-postgresbench-benchmark-for-managed-postgres-services](https://hb.int2inf.com/en/s/item/5yvx36P6dyEyUz8CE2Hur5-postgresbench-benchmark-for-managed-postgres-services)