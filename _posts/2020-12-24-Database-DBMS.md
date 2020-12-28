---
title: "Database - Part2 : DBMS"
tags: [Database, DBMS, RDBMS, DB, ACID]
style: border
color: info
description: Let's check what is DBMS
---

## What is DBMS

> A database is an organized collection of data, generally stored and accessed electronically from a computer system. Where databases are more complex they are often developed using formal design and modeling technique.
The database management system (DBMS) is the software that interacts with end users, applications, and the database itself to capture and analyze the data. The DBMS software additionally encompasses the core facilities provided to administer the database.

### Definition

Connolly and Begg define database management system (DBMS) as a "software system that enables users to define, create, maintain and control access to the database

The core functionality is the storage, retrieval and update of data

Basically DBMS support below functions.

- Data storage, retrieval and update
- User accessible catalog or data dictionary describing the metadata
- Support for transactions and concurrency
- Facilities for recovering the database should it become damaged
- Support for authorization of access and update of data
- Access support from remote locations
- Enforcing constraints to ensure data in the database abides by certain rules

---

## RDBMS

Relational Database (Relational Database, Cultural Language: Relational Data Base, Relational Data Base, RDB) is a computer information database with a very simple principle in which a simple relationship between keys and values is tabulated. It is a digital database based on the data relational model proposed by Edgar F. Curd in 1970.

### Architecture

![Architecture](/assets/images/blog/2020-12-24-Database-DBMS/img1.png){: width="60%"}

#### Query Cache

> ##### This is extremely useful in high-read, low-write environments.
>
> ##### Queries are examined in a case-sensitive manner
>
> `SELECT * FROM t` !=  `select * from t`
>
> ##### Comments are also considered and can make the queries differ
>
> `/* retry */SELECT * FROM t` != `/* retry2 */SELECT * FROM t`
>
> ##### limitation
>
> The query cache needs to be disabled in order to use OQGRAPH.
>
> The query cache is not used by the Spider storage engine (amongst others).
>
> The query cache also needs to be disabled for MariaDB Galera cluster versions prior to "5.5.40-galera", "10.0.14-galera" and "10.1.2".

#### Query Optimizer

> The query optimizer is essentially a piece of software that “models” the way in which the database relational engine works. Using the query processor tree and the statistics it has about the data, and applying the model, it works out what it thinks will be the optimal way to execute the query – that is, it generates an execution plan.
>
> ##### cost based
>
> ```It decides if the data can be accessed through indexes, what types of joins to use and much more. The decisions made by the optimizer are based on what it calculates to be the cost of a given execution plan, in terms of the required CPU processing and I/O, and how fast it will execute```
>
> ##### trivial plan
>
> ```A single table with no indexes and with no aggregates or calculations within the query – then rather than spend time trying to calculate the absolute optimal plan, the optimizer will simply apply a single```
>
> Once the optimizer arrives at an execution plan, the actual plan is created and stored in a memory space known as the `plan cache` - unless an identical plan already exists in the cache
> As the optimizer generates potential plans, it compares them to previously generated plans in the cache. If it finds a match, it will use that plan

#### Query Execution Plan

There are two distinct types of execution plan. First, there is the plan that represents the output from the optimizer. This is known as an Estimated execution plan. The operators, or steps, within the plan will be labeled as logical, because they’re representative of the optimizer’s view of the plan.

Next is the plan that represents the output from the actual query execution. This type of plan is known, funnily enough, as the Actual execution plan. It shows what actually happened when the query executed.

### Transaction

In order for the database management system (DBMS) to operate efficiently and accurately, it must have ACID transactions.

### Index

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
> ClusteredIndex is same structure with secondary index. secondary index have cluster key.
> It means, if clustered index, secondary index changed. than you need to change address of data record

1. search index_first_name for getting record address
2. get result using by record address.

> #### InnoDB
>
> All of secondary index store primary key index. so, you don't necessary to change address of data record when secondary index changed.

1. search index_first_namea and get primary key value.
2. get record address using by primary key.
3. get result using by record address.

---

## ACID

- Atomicity
  - Atomicity guarantees that each transaction is treated as a single "unit".
- Consistency
  - Any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers, and any combination thereof. if some transaction ignore above rules, that transaction should be canceled.
- Isolation
  - Transactions are often executed concurrently (e.g., multiple transactions reading and writing to a table at the same time). Isolation ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially. Isolation is the main goal of concurrency control
- Durability
  - Once a transaction has been committed, it will remain committed even in the case of a system failure (e.g., power outage or crash).

## Conclusion

Understand about DBMS's transaction based on ACID.
Might be next time my post about normalization of RDBMS.
The normalization of RDBMS is a process to maintain integrity.

> _Stay Hunger, Stay Foolish_

## Appendix

- [wikipedia](https://en.wikipedia.org/wiki/Database#Database_management_system)
- [query](https://www.red-gate.com/simple-talk/sql/performance/execution-plan-basics/)
- [SQL w3school](https://www.w3schools.com/sql/trysql.asp?filename=trysql_op_in)