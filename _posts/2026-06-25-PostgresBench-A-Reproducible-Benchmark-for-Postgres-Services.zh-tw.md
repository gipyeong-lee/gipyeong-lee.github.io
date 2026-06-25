---
layout: post
title: "我的數據庫真的夠快嗎？「PostgresBench」拋出的提問"
description: "介紹 PostgresBench，這是一個以透明且可重現的方式比較託管式 PostgreSQL 服務性能的開源基準測試工具。"
summary: "PostgresBench 是一個新的開源基準測試框架，以每個人都能驗證結果的透明方式，比較各種託管式 PostgreSQL 服務的性能。"
tags: [PostgreSQL, 數據庫, 基準測試, 開發者工具, 開源]
image: 2026-06-25-PostgresBench-A-Reproducible-Benchmark-for-Postgres-Services.jpg
image_alt: "比較不同數據庫服務性能指標的圖表出現在透明儀表板畫面上"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "數據庫性能經常會因為「誰進行了測試」而產生巨大結果差異。像 PostgresBench 這樣公開所有過程與結果的透明方式，對於開發者做出正確的技術決策將有莫大幫助。"
quiz:
  - question: "PostgresBench 的主要製作目的是什麼？"
    choices: ["為了變更數據庫的設計", "為了透明地比較託管式 PostgreSQL 服務的性能", "為了檢查數據庫的安全漏洞"]
    answer: 1
    explanation: "PostgresBench 是為公平且透明地比較各種託管式 PostgreSQL 服務性能而設計的開源基準測試框架。"
  - question: "PostgresBench 基於什麼工具來測量性能？"
    choices: ["sysbench", "pgbench", "ClickBench"]
    answer: 1
    explanation: "PostgresBench 是基於業界標準 PostgreSQL 基準測試工具「pgbench」所建構。"
  - question: "關於 PostgresBench 的特徵，下列何者正確？"
    choices: ["基於非公開的測試結果", "公開所有結果、設定與腳本，任何人都能驗證", "僅為宣傳特定企業的服務而製作"]
    answer: 1
    explanation: "PostgresBench 設計為公開所有測試結果、設定值與腳本，讓使用者可以直接重現結果或提交改進建議。"
lang: zh-tw
ref: 2026-06-25-PostgresBench-A-Reproducible-Benchmark-for-Postgres-Services
---

想像一下。您正在為重要的服務挑選雲端服務供應商的數據庫。供應商們各個都聲稱「我們的服務最快」。然而，實際測試時結果卻各不相同。為什麼會有這種差異？也許是因為測試環境不同，或者測量方式不夠透明。

最近，為了化解這種渴求，一個每個人都能信任並參考的「透明成績單」出現了。那就是 **「PostgresBench」**。

## 為什麼這很重要？

數據庫是服務的心臟。如果心臟跳動緩慢，整個服務就會變得遲鈍。開發者與企業支付費用使用「託管式 PostgreSQL（一種租用已設定好 PostgreSQL 服務的伺服器之方式）」服務，但要判斷它們在我的服務中實際表現如何並不容易。

PostgresBench 為這些模糊的疑問提供了客觀的標準。由於所有的測試方法、腳本以及結果數據都是公開的，任何人都可以用相同的條件反覆測試並親自確認性能 [出處: PostgresBench: A Reproducible Benchmark for Postgres Services](https://clickhouse.com/blog/postgresbench)。換句話說，不再只是盲目相信廠商的廣告，而是成為了我們可以親自驗證的「可信比較」。

## 輕鬆理解

要輕鬆理解 PostgresBench，試著想像「大考」。考試會給所有學生一樣的考卷，並在規定的時間內測量實力。這樣才能公平地比較分數。

PostgresBench 也是如此。這個工具使用稱為 **「pgbench」** 的業界標準工具，就像發放共同考卷一樣進行測試 [出處: PostgresBench — A Reproducible Benchmark for Postgres Services](https://postgresbench.clickhouse.com/); [出處: PostgreSQL: Documentation: 18: pgbench](https://www.postgresql.org/docs/current/pgbench.html)。這份考卷中包含了數據輸入、刪除、修改等實務上經常使用的複雜處理方式，即「類似 TPC-B 的作業」[出處: PostgresBench: A Reproducible Benchmark for Postgres Services](https://github.com/ClickHouse/PostgresBench/); [出處: PostgresBench: Reproducible Benchmark for Managed Postgres](https://www.devdigest.org/articles/postgresbench-reproducible-benchmark-for-managed-postgres)。

簡單來說，PostgresBench 為數據庫這些「選手」們提供了「同樣難度的運動場」，是測量誰能更快速、更穩定處理工作的公平裁判 [出處: PostgresBench: Open Benchmark for Postgres Services](https://www.linkedin.com/posts/clickhouseinc_postgresbench-a-reproducible-benchmark-for-activity-7445500419889377280-Cpm6)。

## 現況

PostgresBench 將以下知名服務包含在第一波測試隊列（測試對象群組）中：
*   Postgres by ClickHouse
*   AWS RDS
*   AWS Aurora
*   Crunchy Bridge
*   Neon

這些服務在 100GB 和 500GB 兩種數據大小下進行了性能評估 [出處: PostgresBench: Reproducible Benchmark for Managed Postgres](https://www.devdigest.org/articles/postgresbench-reproducible-benchmark-for-managed-postgres); [出處: PostgresBench: Open Benchmark for Postgres Services](https://www.linkedin.com/posts/clickhouseinc_postgresbench-a-reproducible-benchmark-for-activity-7445500419889377280-Cpm6)。此外，在 256 名使用者同時連線（256 clients）及 16 個工作流程（16 threads）等接近實務的環境下，持續施加 10 分鐘的負載，以測量吞吐量（Throughput）、延遲（Latency）及穩定性 [出處: PostgresBench: A Reproducible Benchmark for Postgres Services](https://hb.int2inf.com/en/s/item/5yvx36P6dyEyUz8CE2Hur5-postgresbench-benchmark-for-managed-postgres-services)。

## 未來發展

未來，PostgresBench 極有可能成為數據庫性能比較的新「標準」。就像在分析型數據庫領域中，已成為透明方法論代名詞的「ClickBench」一樣，PostgresBench 也將成為選擇 PostgreSQL 服務的核心指標 [出處: PostgresBench: A Reproducible Benchmark for Postgres Services](https://hb.int2inf.com/s/item/5yvx36P6dyEyUz8CE2Hur5-postgresbench-benchmark-for-managed-postgres-services)。

使用者將不再只是相信廠商的宣傳文案，而是能基於公開的腳本與設定值，自行驗證並選擇最適合自身業務場景的最佳數據庫 [出處: PostgresBench: Reproducible Benchmark for Managed Postgres](https://www.devdigest.org/articles/postgresbench-reproducible-benchmark-for-managed-postgres)。

## MindTickleBytes 的 AI 記者觀點

數據庫是技術的根基，但過去性能測量往往是在「黑箱」中進行。有些廠商甚至只在對自己有利的條件下進行測試。PostgresBench 所追求的「完全透明」不僅僅是基準測試，更具有深層意義。公開技術真相展現了對該服務的自信，最重要的是，它賦予了像我們這樣的用戶智慧選擇更好技術的力量。這難道不是技術發展的健康方式嗎？

## 參考資料
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