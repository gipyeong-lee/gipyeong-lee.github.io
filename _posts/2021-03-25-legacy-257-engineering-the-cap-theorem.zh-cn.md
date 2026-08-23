---
layout: post
title: "CAP 定理"
description: "什么是 CAP 定理？在谈论 CAP 定理之前，我们需要先了解什么是分布式系统及其原因。如你所知，在移动互联网时代，请求量和数据量呈指数级增长..."
date: 2021-03-25 08:06:24 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2021-03-25-legacy-257-engineering-the-cap-theorem
tags:
  - "cap"
  - "distributed"
  - "分布式环境"
  - "cap"
  - "Data"
  - "engineering"
translation_source_hash: c95aff1d775a791d7ad7fd6ba0e1ad2708569ebb47e6350ea707799765b07a6b
---

<h2>
什么是 CAP 定理？
</h2>
<p>
在谈论 CAP 定理之前，我们需要先了解什么是分布式系统及其原因。
</p>
<p>
如你所知，在移动互联网时代，请求量和数据量呈指数级增长。
</p>
<p>
与此相适应，数据库环境也要求能够轻松扩展并快速交付数据。
</p>
<p>
为了解决这些需求，分布式系统环境应运而生。
</p>
<p>
CAP 定理也被称为布鲁尔定理（Brewer’s Theorem），因为它是由 Eric A. Brewer 教授在 2000 年的一次关于分布式计算的演讲中首次提出的。
</p>
<p>
两年后，麻省理工学院的 Seth Gilbert 和 Nancy Lynch 教授发表了对“布鲁尔猜想”的证明。
</p>
<hr>
<h3>
CAP 定理
</h3>
<p>
让我们来看看 CAP 定理所指的分布式系统的三个特性。
</p>
<h4>
一致性（Consistency）
</h4>
<p>
这意味着所有客户端在同一时间看到相同的数据。
</p>
<p>
这个词有多种解释，请不要与 ACID 中的一致性混淆。
</p>
<blockquote>
<p>
从数据库角度来看
</p>
</blockquote>
<pre class="applescript">
<code>
指“事务”。事务是此类数据库系统中的交互单元。实际上，在数据库中，事务具有 ACID 属性。
</code>
</pre>
<blockquote>
<p>
从原子性角度来看
</p>
</blockquote>
<pre class="livecodeserver">
<code>
单个请求/响应操作序列。
所有客户端在同一时间看到相同的数据。
</code>
</pre>
<h4>
可用性（Availability）
</h4>
<p>
这意味着任何对数据发起请求的客户端都能得到响应，即使是一个或多个节点宕机的情况下。
</p>
<p>
另一种表述方式是——分布式系统中的所有工作节点对任何请求都无一例外地返回有效响应。
</p>
<h4>
分区容错性（Partition tolerance）
</h4>
<p>
分区是指分布式系统内的通信中断——即两个节点之间丢失或延迟的连接。分区容错性意味着集群必须在系统内任意数量的节点间通信故障的情况下继续工作。
</p>
<hr>
<h3>
CAP 定理与 NoSQL 数据库类型
</h3>
<p>
如今，NoSQL（非关系型）数据库不仅考虑垂直扩展，还考虑水平扩展。此外，它们可以在由多个互连节点组成的不断增长的网络中快速扩展。
</p>
<p>
根据两个 CAP 属性的结合，有几种不同的类型：
</p>
<ul>
<li>
CP 数据库：CP 数据库以牺牲可用性为代价，提供一致性和分区容错性。当任意两个节点之间发生分区时，系统必须关闭不一致的节点（即使其不可用），直到分区问题得到解决。
</li>
<li>
AP 数据库：AP 数据库以牺牲一致性为代价，提供可用性和分区容错性。当发生分区时，所有节点保持可用，但位于分区错误一端的节点可能会返回比其他节点更旧的数据。（当分区问题解决后，AP 数据库通常会同步节点，修复系统中的所有不一致。）
</li>
<li>
CA 数据库：CA 数据库在所有节点间提供一致性和可用性。然而，如果系统内任意两个节点之间存在分区，它就无法做到这一点，因此无法提供容错能力。（容错能力是指系统在某些组件发生故障时仍能正常运行的属性。）
</li>
</ul>
<p>
如你所知，在分布式系统中，分区是无法避免的。因此，CA 分布式数据库是不存在的。但是，这并不意味着如果你的分布式应用需要，你就无法使用 CA 数据库。许多关系型数据库，如 <code>PostgreSQL</code>，通过复制（replication）和分片（sharding）部署到多个节点，可以实现一致性和可用性。
</p>
<hr>
<h3>
MongoDB 与 CAP 定理 (CP)
</h3>
<p>
MongoDB 是一种流行的 NoSQL 数据库管理系统，它以 BSON（二进制 JSON）文档形式存储数据。它经常被用于在大数据和多个不同地点运行的实时应用中。就 CAP 定理而言，MongoDB 是一个 CP 数据存储——它通过保持一致性来解决网络分区问题，同时在可用性上做出妥协。
</p>
<p>
MongoDB 是一个单主（single-master）系统——每个副本集（replica set）只能有一个主节点（primary node）来接收所有的写操作。同一副本集中的所有其他节点都是从节点（secondary nodes），它们复制主节点的操作日志并将其应用到自己的数据集上。默认情况下，客户端也从主节点读取数据，但也可以指定读取首选项以允许从从节点读取。
</p>
<p>
<img alt="CAP" src="{{ site.baseurl }}/assets/images/blog/2020-12-17-Database-the-cap-theorem/mongodb_failover.svg">
</p>
<p>
当主节点变得不可用时，拥有最新操作日志的从节点将被选为新的主节点。一旦所有其他从节点追上新的主节点，集群就会再次变为可用。由于客户端在此期间无法进行任何写请求，因此整个网络中的数据保持一致。
</p>
<hr>
<h3>
Cassandra (AP)
</h3>
<p>
Apache Cassandra 是由 Apache 软件基金会维护的开源 NoSQL 数据库。它是一个宽列存储数据库（wide-column database），允许你在分布式网络上存储数据。然而，与 MongoDB 不同的是，Cassandra 具有无主架构（masterless architecture），因此它拥有多个故障点，而不是单个故障点。
</p>
<p>
就 CAP 定理而言，Cassandra 是一个 AP 数据库——它提供可用性和分区容错性，但无法始终提供一致性。由于 Cassandra 没有主节点，所有节点必须持续可用。不过，Cassandra 通过允许客户端在任何时间向任何节点写入数据，并尽可能快地协调不一致，从而提供最终一致性（eventual consistency）。
</p>
<p>
由于数据仅在网络分区的情况下才会不一致，并且不一致很快就会得到解决，Cassandra 提供了“修复”功能来帮助节点追上其对等节点。然而，持续的可用性带来了一个高性能的系统，这在许多情况下可能值得进行这种权衡。
</p>
<hr>
<h3>
结论
</h3>
<p>
通过观察分布式系统中基于 CAP 理论的数据库，我们可以更好地理解每个数据库的优势。最后，我要感谢 IBM 对 CAP 理论、分布式处理系统和数据库所做的梳理。
</p>
<blockquote>
<p>
<i>
Stay Hungry, Stay Foolish（求知若饥，虚心若愚）
</i>
</p>
</blockquote>
<hr>
<h3>
参考资料
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