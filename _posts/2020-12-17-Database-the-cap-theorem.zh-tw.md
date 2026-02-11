---
layout: post
title: "資料庫 - 第 1 部分：CAP 定理"
tags: [Database, CAP]
style: border
color: success
description: 思考為什麼我們需要 NoSQL。
lang: zh-tw
ref: 2020-12-17-Database-the-cap-theorem
---

![CAP](/assets/images/blog/2020-12-17-Database-the-cap-theorem/cap.png){: width="60%"}

## 什麼是 CAP 定理？

在討論 CAP 定理之前，我們需要了解什麼是分散式系統以及為什麼需要它。

如你所知，在行動裝置時代，請求量和數據量呈指數級增長。

為了因應這種情況，資料庫環境也產生了易於擴充且必須快速傳輸數據的需求。

分散式系統環境便是為了解決這些需求而設計的。

CAP 定理也稱為布魯爾定理（Brewer’s Theorem），因為它最初是由 Eric A. Brewer 教授在 2000 年的一次關於分散式運算的演講中提出的。

兩年後，麻省理工學院（MIT）的教授 Seth Gilbert 和 Nancy Lynch 發表了「布魯爾猜想」（Brewer’s Conjecture）的證明。

---

### CAP 定理

讓我們來看看 CAP 定理所指的三個分散式系統特性。

#### 一致性 (Consistency)

這意味著所有用戶端在同一時間都能看到相同的數據。

這個詞可以有多種解釋，請不要與 ACID 中的一致性混淆。

> 從資料庫的角度來看

```txt
它代表「事務」（Transaction）。事務是資料庫系統中交互的單位。事實上，在資料庫中，事務具有 ACID 屬性。
```

> 從原子性（Atomic）的角度來看

```txt
單個請求/回應操作序列。
所有用戶端在同一時間都能看到相同的數據。
```

#### 可用性 (Availability)

這意味著任何發出數據請求的用戶端都能得到回應，即使一個或多個節點發生故障。

另一種說法是——分散式系統中所有運作中的節點都會為任何請求返回有效的回應，絕無例外。

#### 分割容錯性 (Partition tolerance)

網路分割（Partition）是指分散式系統內的通訊中斷——即兩個節點之間的連線遺失或暫時延遲。分割容錯性意味著儘管系統中的節點之間發生任何數量的通訊故障，叢集仍必須繼續運作。

---

### CAP 定理與 NoSQL 資料庫類型

現今的 NoSQL（非關聯式）資料庫不僅考慮垂直擴充（Vertical scale），還考慮水平擴充（Horizontal scale）。此外，它們可以在由多個互連節點組成的日益增長的網路中快速擴充。

根據兩項 CAP 屬性的組合，可以分為幾種類型：

- **CP 資料庫**：CP 資料庫提供一致性和分割容錯性，但以犧牲可用性為代價。當任何兩個節點之間發生分割時，系統必須關閉不一致的節點（即使其不可用），直到分割問題解決。
  
- **AP 資料庫**：AP 資料庫提供可用性和分割容錯性，但以犧牲一致性為代價。當發生分割時，所有節點保持可用，但位於分割錯誤端的節點可能會返回比其他節點更舊的數據版本。（當分割解決後，AP 資料庫通常會重新同步節點以修復系統中所有不一致之處）

- **CA 資料庫**：CA 資料庫在所有節點上提供一致性和可用性。然而，如果系統中任何兩個節點之間存在分割，它就無法做到這一點，因此無法提供容錯性。（容錯性是指使系統在某些組件發生故障時仍能正常運行的屬性。）

如你所知，在分散式系統中，網路分割是無法避免的。因此，純粹的 CA 分散式資料庫是不存在的。但是，這並不意味著如果你需要的話，就不能為你的分散式應用程式配備 CA 資料庫。許多關聯式資料庫（如 `PostgreSQL`）提供了一致性和可用性，並且可以透過複製（Replication）以及分片（Sharding）部署到多個節點。

---

### MongoDB 與 CAP 定理 (CP)

MongoDB 是一個受歡迎的 NoSQL 資料庫管理系統，它將數據存儲為 BSON（二進位 JSON）文件。它常用於在多個不同地點運行的巨量資料和即時應用程式。相對於 CAP 定理，MongoDB 是一個 CP 數據存儲——它通過維護一致性來解決網路分割問題，同時在可用性上做出妥協。

MongoDB 是一個單主機（Single-master）系統——每個副本集（Replica set）只能有一個主節點（Primary node）接收所有寫入操作。同一副本集中的所有其他節點都是從節點（Secondary nodes），它們複製主節點的操作日誌並應用於自己的數據集。預設情況下，用戶端也從主節點讀取，但他們也可以指定讀取偏好，允許從從節點讀取。

![CAP](/assets/images/blog/2020-12-17-Database-the-cap-theorem/mongodb_failover.svg)

當主節點變得不可用時，擁有最新操作日誌的從節點將被選為新的主節點。一旦所有其他從節點趕上新主節點的進度，叢集就會再次變得可用。由於用戶端在此間隔期間無法發出任何寫入請求，因此數據在整個網路中保持一致。

---

### Cassandra (AP)

Apache Cassandra 是由 Apache 軟體基金會維護的開源 NoSQL 資料庫。它是一個寬列資料庫（Wide-column database），允許你在分散式網路上存儲數據。然而，與 MongoDB 不同，Cassandra 採用無主架構（Masterless architecture），因此它有多個故障點，而不是單一故障點。

相對於 CAP 定理，Cassandra 是一個 AP 資料庫——它提供可用性和分割容錯性，但無法始終提供一致性。因為 Cassandra 沒有主節點，所有節點必須持續可用。然而，Cassandra 通過允許用戶端隨時向任何節點寫入，並儘快調解不一致之處，來提供最終一致性（Eventual consistency）。

由於數據僅在網路分割的情況下才會變得不一致，且不一致之處會被迅速解決，Cassandra 提供了「修復」（Repair）功能來幫助節點趕上其同儕節點。然而，持續的可用性造就了一個高效能的系統，在許多情況下，這種權衡是值得的。

---

### 結論

通過 CAP 定理來觀察分散式系統中的資料庫，我們可以更好地理解每種資料庫的優勢。最後，我要感謝 IBM 對 CAP 定理、分散式處理系統和資料庫所做的整理。

> _求知若渴，大智若愚 (Stay Hungry, Stay Foolish)_

---

### 附錄

- [IBM CAP 定理](https://www.ibm.com/cloud/learn/cap-theorem)
- [一致性 (Consistency)](https://en.wikipedia.org/wiki/Consistency_(database_systems))
- [MongoDB](https://docs.mongodb.com/manual/replication/)
