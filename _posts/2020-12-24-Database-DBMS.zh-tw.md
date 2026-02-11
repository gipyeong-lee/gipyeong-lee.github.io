---
layout: post
title: "資料庫 - 第二部分：DBMS"
tags: [Database, DBMS, RDBMS, DB, ACID]
style: border
color: info
description: 讓我們來了解什麼是 DBMS
lang: zh-tw
ref: 2020-12-24-Database-DBMS
---

## 什麼是 DBMS

> 資料庫是經過整理的資料集合，通常以電子方式儲存並從電腦系統存取。當資料庫變得更複雜時，通常會使用正式的設計和建模技術來開發。
資料庫管理系統 (DBMS) 是與終端用戶、應用程式和資料庫本身互動，以擷取和分析資料的軟體。DBMS 軟體還包含用於管理資料庫的核心設施。

### 定義

Connolly 和 Begg 將資料庫管理系統 (DBMS) 定義為「讓使用者能夠定義、建立、維護和控制對資料庫存取的軟體系統」。

其核心功能是資料的儲存、檢索和更新。

基本上，DBMS 支援以下功能：

- 資料的儲存、檢索和更新
- 使用者可存取的目錄或描述詮釋資料 (metadata) 的資料字典
- 支援交易 (transactions) 和並行處理 (concurrency)
- 在資料庫損毀時提供修復資料庫的設施
- 支援資料存取與更新的授權
- 支援來自遠端位置的存取
- 強制執行約束 (constraints)，以確保資料庫中的資料遵守特定規則

---

## RDBMS

關聯式資料庫 (Relational Database，簡稱 RDB) 是一種電腦資訊資料庫，其原理非常簡單，將鍵 (key) 與值 (value) 之間的簡單關係製成表格。它是基於 Edgar F. Codd 於 1970 年提出的資料關聯模型而建立的數位資料庫。

### 架構

![Architecture](/assets/images/blog/2020-12-24-Database-DBMS/img1.png){: width="60%"}

#### 查詢快取 (Query Cache)

> ##### 這在「高讀取、低寫入」的環境中非常有用。
>
> ##### 查詢會以區分大小寫的方式進行檢查
>
> `SELECT * FROM t` !=  `select * from t`
>
> ##### 註解也會被考慮在內，並可能導致查詢被視為不同
>
> `/* retry */SELECT * FROM t` != `/* retry2 */SELECT * FROM t`
>
> ##### 限制
>
> 為了使用 OQGRAPH，需要停用查詢快取。
>
> Spider 儲存引擎（以及其他引擎）不使用查詢快取。
>
> 對於 "5.5.40-galera"、"10.0.14-galera" 和 "10.1.2" 之前的 MariaDB Galera 叢集版本，也需要停用查詢快取。

#### 查詢最佳化器 (Query Optimizer)

> 查詢最佳化器本質上是一段軟體，用於「模擬」資料庫關聯引擎的運作方式。它利用查詢處理器樹以及關於資料的統計資訊，並套用模型，計算出它認為執行查詢的最佳方式——也就是說，它會產生一個執行計畫。
>
> ##### 基於成本 (cost based)
>
> ```它決定是否可以透過索引存取資料、使用哪種類型的連接 (join) 等等。最佳化器所做的決定是基於它計算出的給定執行計畫的成本，包括所需的 CPU 處理和 I/O，以及執行的速度。```
>
> ##### 簡單計畫 (trivial plan)
>
> ```對於一個沒有索引、且查詢中沒有聚合或計算的單一表格——與其花時間計算絕對的最佳計畫，最佳化器會簡單地套用一個單一的計畫。```
>
> 一旦最佳化器得出執行計畫，實際計畫就會被建立並儲存在稱為「計畫快取」(plan cache) 的記憶體空間中——除非快取中已存在相同的計畫。
> 當最佳化器產生潛在計畫時，它會將其與快取中先前產生的計畫進行比較。如果發現匹配，它將使用該計畫。

#### 查詢執行計畫 (Query Execution Plan)

執行計畫有兩種不同的類型。首先是代表最佳化器輸出的計畫，這被稱為「估計執行計畫」(Estimated execution plan)。計畫中的操作員或步驟將被標記為邏輯操作，因為它們代表了最佳化器對計畫的視角。

接下來是代表實際查詢執行輸出的計畫。這種類型的計畫被稱為「實際執行計畫」(Actual execution plan)。它顯示了查詢執行時實際發生的情況。

### 交易 (Transaction)

為了讓資料庫管理系統 (DBMS) 高效且準確地運作，它必須具備 ACID 交易特性。

### 索引 (Index)

```sql
CREATE TABLE students (
    id INT NOT NULL,
    first_name VARCHAR(16) NOT NULL,
    PRIMARY KEY (id),
    INDEX index_first_name (first_name)
);

SELECT * FROM students WHERE first_name = 'GiPyeong';
```

> #### MyISAM
>
> 聚集索引 (Clustered Index) 與輔助索引 (secondary index) 具有相同的結構。輔助索引包含聚集鍵。
> 這意味著，如果聚集索引變更，輔助索引也會隨之變更。那麼你就需要更改資料記錄的位址。

1. 搜尋 index_first_name 以獲取記錄位址。
2. 使用記錄位址獲取結果。

> #### InnoDB
>
> 所有的輔助索引都會儲存主鍵索引。因此，當輔助索引變更時，不需要更改資料記錄的位址。

1. 搜尋 index_first_name 並獲取主鍵值。
2. 使用主鍵獲取記錄位址。
3. 使用記錄位址獲取結果。

---

## ACID

- 原子性 (Atomicity)
  - 原子性保證每個交易都被視為一個單一的「單位」。
- 一致性 (Consistency)
  - 寫入資料庫的任何資料都必須根據所有定義的規則（包括約束、級聯、觸發器及其任何組合）是有效的。如果某些交易忽略上述規則，則該交易應被取消。
- 隔離性 (Isolation)
  - 交易通常是並行執行的（例如，多個交易同時對一個表進行讀取和寫入）。隔離性確保交易的並行執行使資料庫處於與順序執行交易時相同的狀態。隔離性是並行控制的主要目標。
- 持久性 (Durability)
  - 一旦交易被提交，即使在系統故障（例如斷電或當機）的情況下，它仍將保持提交狀態。

## 結論

了解基於 ACID 的 DBMS 交易。
下次我的貼文可能會關於 RDBMS 的正規化。
RDBMS 的正規化是維護完整性的過程。

> _Stay Hunger, Stay Foolish_

## 附錄

- [維基百科](https://en.wikipedia.org/wiki/Database#Database_management_system)
- [查詢](https://www.red-gate.com/simple-talk/sql/performance/execution-plan-basics/)
- [SQL w3school](https://www.w3schools.com/sql/trysql.asp?filename=trysql_op_in)
