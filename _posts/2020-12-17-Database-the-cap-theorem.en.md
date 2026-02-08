---
layout: post
title: "Database - Part1 : The CAP Theorem"
tags: [Database, CAP]
style: border
color: success
description: Understanding why we need NoSQL.
lang: en
ref: 2020-12-17-Database-the-cap-theorem
---

![CAP](/assets/images/blog/2020-12-17-Database-the-cap-theorem/cap.png){: width="60%"}

## What is the CAP theorem?

Before discussing the CAP theorem, we need to understand distributed systems and why they are necessary.

As we know, in the mobile era, the volume of requests and data has increased exponentially.

To address this situation, database environments require systems that are easily scalable and capable of delivering data quickly.

Distributed system environments were devised to meet these requirements.

The CAP theorem is also known as Brewer’s Theorem, as it was first introduced by Professor Eric A. Brewer during a talk on distributed computing in 2000.

Two years later, MIT professors Seth Gilbert and Nancy Lynch published a proof of “Brewer’s Conjecture.”

---

### The CAP theorem

Let’s examine the three characteristics of distributed systems referred to in the CAP theorem.

#### Consistency

This means that all clients see the same data at the same time.

This term can be interpreted in several ways. Please do not confuse it with consistency in ACID.

> From a database point of view

```txt
It refers to a `transaction`. A transaction is a unit of interaction in a database system. In fact, database transactions have ACID properties.
```

> From an atomic point of view

```txt
Single request/response operation sequence.
All clients see the same data at the same time.
```

#### Availability

This means that any client making a request for data receives a response, even if one or more nodes are down.

Stated another way: all working nodes in the distributed system return a valid response for any request, without exception.

#### Partition tolerance

A partition is a communications break within a distributed system—a lost or temporarily delayed connection between two nodes. Partition tolerance means that the cluster must continue to work despite any number of communication breakdowns between nodes in the system.

---

### CAP theorem NoSQL database types

Nowadays, NoSQL (Not Only SQL) databases consider horizontal scaling, not just vertical. They can rapidly scale across a growing network consisting of multiple interconnected nodes.

There are several types based on the two CAP properties.

- CP Database: A CP database delivers consistency and partition tolerance at the expense of availability. When a partition occurs between any two nodes, the system must shut down the non-consistent node (i.e., make it unavailable) until the partition is resolved.
  
- AP Database: An AP database delivers availability and partition tolerance at the expense of consistency. When a partition occurs, all nodes remain available, but those on the wrong side of a partition might return an older version of data than others. (When the partition is resolved, AP databases typically resync the nodes to repair all inconsistencies in the system.)

- CA Database: A CA database delivers consistency and availability across all nodes. However, it cannot do this if there is a partition between any two nodes in the system, and therefore cannot deliver fault tolerance. (Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of some of its components.)

As we know, in a distributed system, partitions cannot be avoided. Therefore, a distributed CA database cannot exist. However, this doesn’t mean you can’t have a CA database for your distributed application if you need one. Many relational databases, such as `PostgreSQL`, deliver consistency and availability and can be deployed to multiple nodes using replication and sharding.

---

### MongoDB and the CAP theorem ( CP )

MongoDB is a popular NoSQL database management system that stores data as BSON (binary JSON) documents. It is frequently used for big data and real-time applications running in multiple locations. Relative to the CAP theorem, MongoDB is a CP data store—it resolves network partitions by maintaining consistency while compromising on availability.

MongoDB is a single-master system—each replica set can have only one primary node that receives all write operations. All other nodes in the same replica set are secondary nodes that replicate the primary node's operation log and apply it to their own data set. By default, clients read from the primary node, but they can also specify a read preference that allows them to read from secondary nodes.

![CAP](/assets/images/blog/2020-12-17-Database-the-cap-theorem/mongodb_failover.svg)

When the primary node becomes unavailable, the secondary node with the most recent operation log will be elected as the new primary node. Once all other secondary nodes catch up with the new master, the cluster becomes available again. Since clients cannot make any write requests during this interval, the data remains consistent across the entire network.

---

### Cassandra ( AP )

Apache Cassandra is an open-source NoSQL database maintained by the Apache Software Foundation. It is a wide-column database that allows you to store data on a distributed network. However, unlike MongoDB, Cassandra has a masterless architecture, and as a result, it has multiple points of failure rather than a single one.

Relative to the CAP theorem, Cassandra is an AP database—it delivers availability and partition tolerance but cannot guarantee consistency at all times. Because Cassandra does not have a master node, all nodes must be continuously available. However, Cassandra provides eventual consistency by allowing clients to write to any node at any time and reconciling inconsistencies as quickly as possible.

Since data only becomes inconsistent in the case of a network partition and inconsistencies are quickly resolved, Cassandra offers “repair” functionality to help nodes catch up with their peers. However, constant availability results in a highly performant system that may be worth the trade-off in many cases.

---

### Conclusion

By looking at databases based on the CAP theorem in distributed systems, we can better understand the advantages of each database. Finally, I would like to express my gratitude to IBM for organizing the information on the CAP theorem, distributed processing systems, and databases.

> _Stay Hungry, Stay Foolish_

---

### Appendix

- [IBM CAP theorem](https://www.ibm.com/cloud/learn/cap-theorem)
- [Consistency](https://en.wikipedia.org/wiki/Consistency_(database_systems))
- [MongoDB](https://docs.mongodb.com/manual/replication/)
