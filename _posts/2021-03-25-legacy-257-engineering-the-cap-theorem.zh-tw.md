---
layout: post
title: "CAP 定理"
description: "什麼是 CAP 定理？在探討 CAP 定理之前，我們需要先了解分散式系統及其原因。眾所周知，在行動世代，請求與數據量呈現指數級增長..."
date: 2021-03-25 08:06:24 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2021-03-25-legacy-257-engineering-the-cap-theorem
tags:
  - "cap"
  - "分散式"
  - "分散式環境"
  - "캡"
  - "資料"
  - "工程"
translation_source_hash: c95aff1d775a791d7ad7fd6ba0e1ad2708569ebb47e6350ea707799765b07a6b
---

<h2>
什麼是 CAP 定理？
</h2>
<p>
在探討 CAP 定理之前，我們需要先了解分散式系統及其原因。
</p>
<p>
眾所周知，在行動世代，請求與數據量呈現指數級增長。
</p>
<p>
基於這種情況，在資料庫環境中，也出現了易於擴展且需快速傳遞數據的需求。
</p>
<p>
分散式系統環境正是為了滿足這些需求而設計的。
</p>
<p>
CAP 定理又稱為布魯爾定理（Brewer's Theorem），因為它是由 Eric A. Brewer 教授於 2000 年在一次關於分散式計算的演講中首次提出的。
</p>
<p>
兩年後，麻省理工學院（MIT）的 Seth Gilbert 和 Nancy Lynch 教授發表了「布魯爾猜想」的證明。
</p>
<hr>
<h3>
CAP 定理
</h3>
<p>
讓我們來看看 CAP 定理所指的分散式系統的三個特性。
</p>
<h4>
一致性 (Consistency)
</h4>
<p>
意指所有客戶端在同一時間看到相同的數據。
</p>
<p>
這個詞有多種含義，請勿將其與 ACID 中的一致性混淆。
</p>
<blockquote>
<p>
從資料庫的角度來看
</p>
</blockquote>
<pre class="applescript">
<code>
意指「交易」（Transaction）。交易是此類資料庫系統中的互動單位。實際上，資料庫交易具有 ACID 屬性。
</code>
</pre>
<blockquote>
<p>
從原子性的角度來看
</p>
</blockquote>
<pre class="livecodeserver">
<code>
單一請求/回應的操作序列。
所有客戶端在同一時間看到相同的數據。
</code>
</pre>
<h4>
可用性 (Availability)
</h4>
<p>
意指任何客戶端對數據發出的請求都能得到回應，即使有一個或多個節點故障。
</p>
<p>
另一種說法是：分散式系統中所有正常運作的節點都必須對任何請求返回有效的回應，無一例外。
</p>
<h4>
分區容錯性 (Partition tolerance)
</h4>
<p>
分區（Partition）是指分散式系統內的通訊中斷，即兩個節點之間的連線遺失或暫時延遲。分區容錯性意味著即使系統節點之間發生任何數量的通訊中斷，叢集仍必須持續運作。
</p>
<hr>
<h3>
CAP 定理與 NoSQL 資料庫類型
</h3>
<p>
現今的 NoSQL（非關聯式）資料庫考慮的不僅是垂直擴展，還有水平擴展。此外，它們還能在由多個互連節點組成的日益增長的網路中快速擴展。
</p>
<p>
根據兩個 CAP 特性，有幾種不同的類型。
</p>
<ul>
<li>
CP 資料庫：CP 資料庫以犧牲可用性為代價，提供一致性和分區容錯性。當任何兩個節點之間發生分區時，系統必須關閉不一致的節點（即使其不可用），直到分區解決為止。
</li>
<li>
AP 資料庫：AP 資料庫以犧牲一致性為代價，提供可用性和分區容錯性。當發生分區時，所有節點保持可用狀態，但處於分區錯誤端的節點可能會返回比其他節點更舊的數據版本。（當分區解決後，AP 資料庫通常會重新同步節點以修復系統中的所有不一致。）
</li>
<li>
CA 資料庫：CA 資料庫在所有節點間提供一致性和可用性。然而，如果系統中任何兩個節點之間發生分區，它就無法做到這一點，因此無法提供容錯能力。（容錯能力是指系統在某些元件發生故障時仍能持續正常運作的屬性。）
</li>
</ul>
<p>
如您所知，在分散式系統中，分區是無法避免的。因此，CA 分散式資料庫並不存在。但這並不意味著如果您的分散式應用程式需要，您就不能擁有 CA 資料庫。許多關聯式資料庫，例如 <code>PostgreSQL</code>，透過複製（Replication）與分片（Sharding）部署到多個節點，即可提供一致性和可用性。
</p>
<hr>
<h3>
MongoDB 與 CAP 定理 (CP)
</h3>
<p>
MongoDB 是一種流行的 NoSQL 資料庫管理系統，它以 BSON（二進位 JSON）文件格式儲存數據。它經常被用於在多個不同地點執行的大數據和即時應用程式中。就 CAP 定理而言，MongoDB 是一個 CP 資料儲存庫——它透過維持一致性來解決網路分區問題，同時犧牲了可用性。
</p>
<p>
MongoDB 是一個單主（Single-master）系統——每個複本集（Replica Set）只能有一個主節點（Primary Node）接收所有的寫入操作。同一複本集中的所有其他節點都是輔助節點（Secondary Nodes），它們會複製主節點的操作日誌並將其應用到自己的數據集中。預設情況下，客戶端也從主節點讀取數據，但也可以指定讀取偏好（Read Preference），允許從輔助節點讀取。
</p>
<p>
<img alt="CAP" src="{{ site.baseurl }}/assets/images/blog/2020-12-17-Database-the-cap-theorem/mongodb_failover.svg">
</p>
<p>
當主節點變得不可用時，擁有最新操作日誌的輔助節點將被選為新的主節點。一旦所有其他輔助節點趕上新的主節點，叢集就會再次變得可用。由於在此期間客戶端無法進行任何寫入請求，數據在整個網路中保持一致。
</p>
<hr>
<h3>
Cassandra (AP)
</h3>
<p>
Apache Cassandra 是一個由 Apache 軟體基金會維護的開源 NoSQL 資料庫。它是一個寬欄位（Wide-column）資料庫，允許您在分散式網路上儲存數據。然而，與 MongoDB 不同的是，Cassandra 採用無主（Masterless）架構，因此它擁有多個故障點，而非單一故障點。
</p>
<p>
就 CAP 定理而言，Cassandra 是一個 AP 資料庫——它提供可用性和分區容錯性，但無法始終提供一致性。由於 Cassandra 沒有主節點，所有節點必須持續保持可用。然而，Cassandra 透過允許客戶端在任何時間向任何節點寫入數據，並儘快協調不一致性，從而提供最終一致性（Eventual Consistency）。
</p>
<p>
由於數據僅在網路分區的情況下才會變得不一致，且不一致會被迅速解決，Cassandra 提供了「修復」（Repair）功能來幫助節點跟上其對等節點。然而，持續的可用性會帶來高性能系統，在許多情況下，這可能是值得權衡的。
</p>
<hr>
<h3>
結論
</h3>
<p>
透過在分散式系統中檢視基於 CAP 理論的資料庫，我們能更好地理解每個資料庫的優勢。最後，我要感謝 IBM 對 CAP 理論、分散式處理系統和資料庫的整理。
</p>
<blockquote>
<p>
<i>
求知若飢，虛心若愚 (Stay Hungry, Stay Foolish)
</i>
</p>
</blockquote>
<hr>
<h3>
參考資料
</h3>
<ul>
<li>
<a href="https://www.ibm.com/cloud/learn/cap-theorem">
IBM CAP 定理
</a>
</li>
<li>
<a href="https://en.wikipedia.org/wiki/Consistency_(database_systems)">
一致性
</a>
</li>
<li>
<a href="https://docs.mongodb.com/manual/replication/">
MongoDB
</a>
</li>
</ul>