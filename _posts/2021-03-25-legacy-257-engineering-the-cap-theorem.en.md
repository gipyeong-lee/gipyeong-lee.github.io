---
layout: post
title: "The CAP Theorem"
description: "What is the CAP theorem? Before we talk about the CAP theorem, we need to understand distributed systems and why they are necessary. As you know, in the mobile era, the volume of requests and data has increased exponentially..."
date: 2021-03-25 08:06:24 +0900
section: blog
category: engineering
lang: en
ref: 2021-03-25-legacy-257-engineering-the-cap-theorem
tags:
  - "cap"
  - "distributed"
  - "distributed environments"
  - "cap"
  - "Data"
  - "engineering"
translation_source_hash: c95aff1d775a791d7ad7fd6ba0e1ad2708569ebb47e6350ea707799765b07a6b
---

<h2>
What is the CAP theorem?
</h2>
<p>
Before we talk about the CAP theorem, we need to understand distributed systems and why they are necessary.
</p>
<p>
As you know, in the mobile era, the volume of requests and data has increased exponentially.
</p>
<p>
In accordance with this situation, database environments now have requirements for easy scalability and the need for data to be delivered quickly.
</p>
<p>
A distributed system environment was devised to solve these requirements.
</p>
<p>
The CAP theorem is also called Brewer’s Theorem, because it was first advanced by Professor Eric A. Brewer during a talk he gave on distributed computing in 2000.
</p>
<p>
Two years later, MIT professors Seth Gilbert and Nancy Lynch published a proof of “Brewer’s Conjecture.”
</p>
<hr>
<h3>
The CAP theorem
</h3>
<p>
Let’s take a look at the three distributed system characteristics to which the CAP theorem refers.
</p>
<h4>
Consistency
</h4>
<p>
It means that all clients see the same data at the same time.
</p>
<p>
This term can be interpreted in several ways. Please do not confuse it with ACID consistency.
</p>
<blockquote>
<p>
From a database point of view
</p>
</blockquote>
<pre class="applescript">
<code>
It means 'transaction'. The transaction is the unit of interaction in such database systems. Actually, database transactions have ACID properties.
</code>
</pre>
<blockquote>
<p>
From an atomic point of view
</p>
</blockquote>
<pre class="livecodeserver">
<code>
Single request/response operation sequence.
All clients see the same data at the same time.
</code>
</pre>
<h4>
Availability
</h4>
<p>
It means that any client making a request for data gets a response, even if one or more nodes are down.
</p>
<p>
Another way to state this—all working nodes in the distributed system return a valid response for any request, without exception.
</p>
<h4>
Partition tolerance
</h4>
<p>
A partition is a communications break within a distributed system—a lost or temporarily delayed connection between two nodes. Partition tolerance means that the cluster must continue to work despite any number of communication breakdowns between nodes in the system.
</p>
<hr>
<h3>
CAP theorem NoSQL database types
</h3>
<p>
These days, NoSQL (Not Only SQL) databases consider horizontal scale, not just vertical. They can also rapidly scale across a growing network consisting of multiple interconnected nodes.
</p>
<p>
There are several types based on these two CAP properties.
</p>
<ul>
<li>
CP Database: A CP database delivers consistency and partition tolerance at the expense of availability. When a partition occurs between any two nodes, the system must shut down the non-consistent node (i.e., make it unavailable) until the partition is resolved.
</li>
<li>
AP Database: An AP database delivers availability and partition tolerance at the expense of consistency. When a partition occurs, all nodes remain available, but those at the wrong end of a partition might return an older version of data than others. (When the partition is resolved, AP databases typically resync the nodes to repair all inconsistencies in the system.)
</li>
<li>
CA Database: A CA database delivers consistency and availability across all nodes. However, it cannot do this if there is a partition between any two nodes in the system, and therefore it cannot deliver fault tolerance. (Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of some of its components.)
</li>
</ul>
<p>
As you know, in distributed systems, partitions cannot be avoided. Therefore, a CA distributed database cannot exist. However, this doesn’t mean you can’t have a CA database for your distributed application if you need one. Many relational databases, such as <code>PostgreSQL</code>, deliver consistency and availability and can be deployed to multiple nodes using replication and sharding.
</p>
<hr>
<h3>
MongoDB and the CAP theorem (CP)
</h3>
<p>
MongoDB is a popular NoSQL database management system that stores data as BSON (binary JSON) documents. It is frequently used for big data and real-time applications running at multiple different locations. Relative to the CAP theorem, MongoDB is a CP data store—it resolves network partitions by maintaining consistency, while compromising on availability.
</p>
<p>
MongoDB is a single-master system—each replica set can have only one primary node that receives all the write operations. All other nodes in the same replica set are secondary nodes that replicate the primary node's operation log and apply it to their own data set. By default, clients also read from the primary node, but they can specify a read preference that allows them to read from secondary nodes.
</p>
<p>
<img alt="CAP" src="{{ site.baseurl }}/assets/images/blog/2020-12-17-Database-the-cap-theorem/mongodb_failover.svg">
</p>
<p>
When the primary node becomes unavailable, the secondary node with the most recent operation log will be elected as the new primary node. Once all the other secondary nodes catch up with the new master, the cluster becomes available again. As clients cannot make any write requests during this interval, the data remains consistent across the entire network.
</p>
<hr>
<h3>
Cassandra (AP)
</h3>
<p>
Apache Cassandra is an open-source NoSQL database maintained by the Apache Software Foundation. It is a wide-column database that lets you store data on a distributed network. However, unlike MongoDB, Cassandra has a masterless architecture, and as a result, it has multiple points of failure rather than a single one.
</p>
<p>
Relative to the CAP theorem, Cassandra is an AP database—it delivers availability and partition tolerance but cannot deliver consistency all the time. Because Cassandra doesn't have a master node, all nodes must be available continuously. However, Cassandra provides eventual consistency by allowing clients to write to any nodes at any time and reconciling inconsistencies as quickly as possible.
</p>
<p>
As data only becomes inconsistent in the case of a network partition and inconsistencies are quickly resolved, Cassandra offers “repair” functionality to help nodes catch up with their peers. However, constant availability results in a highly performant system that might be worth the trade-off in many cases.
</p>
<hr>
<h3>
Conclusion
</h3>
<p>
Looking at databases based on the CAP theorem in a distributed system, we can better understand the advantages of each database. Finally, I would like to express my gratitude to IBM for organizing the information on the CAP theorem, distributed processing systems, and databases.
</p>
<blockquote>
<p>
<i>
Stay Hungry, Stay Foolish
</i>
</p>
</blockquote>
<hr>
<h3>
## References
</h3>
<ul>
<li>
<a href="https://www.ibm.com/cloud/learn/cap-theorem">
IBM CAP theorem
</a>
</li>
<li>
<a href="https://en.wikipedia.org/wiki/Consistency_(database_systems)">
Consistency
</a>
</li>
<li>
<a href="https://docs.mongodb.com/manual/replication/">
MongoDB
</a>
</li>
</ul>