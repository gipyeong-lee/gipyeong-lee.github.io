---
layout: post
title: "数据库 - 第二部分：DBMS"
tags: [Database, DBMS, RDBMS, DB, ACID]
style: border
color: info
description: 让我们来看看什么是 DBMS
lang: zh-cn
ref: 2020-12-24-Database-DBMS
---

## 什么是 DBMS

> 数据库是一个有组织的数据集合，通常以电子方式从计算机系统中存储和访问。当数据库较为复杂时，通常使用正式的设计和建模技术进行开发。
数据库管理系统 (DBMS) 是与最终用户、应用程序和数据库本身交互以捕获和分析数据的软件。此外，DBMS 软件还包含为管理数据库提供的核心设施。

### 定义

Connolly 和 Begg 将数据库管理系统 (DBMS) 定义为“使用户能够定义、创建、维护和控制对数据库访问的软件系统”。

其核心功能是数据的存储、检索和更新。

基本上，DBMS 支持以下功能：

- 数据的存储、检索和更新
- 描述元数据的用户可访问目录或数据字典
- 支持事务和并发
- 在数据库损坏时提供恢复设施
- 支持对数据访问和更新的授权
- 支持远程位置访问
- 强制执行约束以确保数据库中的数据遵守某些规则

---

## RDBMS

关系数据库（Relational Database，缩写为 RDB）是一种原理非常简单的计算机信息数据库，其中键与值之间的简单关系被制成表格。它是基于 Edgar F. Codd 在 1970 年提出的数据关系模型的数字数据库。

### 架构

![架构](/assets/images/blog/2020-12-24-Database-DBMS/img1.png){: width="60%"}

#### 查询缓存 (Query Cache)

> ##### 这在多读少写的环境中非常有用。
>
> ##### 查询是以区分大小写的方式进行检查的
>
> `SELECT * FROM t` !=  `select * from t`
>
> ##### 注释也会被考虑在内，并可能使查询产生差异
>
> `/* retry */SELECT * FROM t` != `/* retry2 */SELECT * FROM t`
>
> ##### 限制
>
> 为了使用 OQGRAPH，需要禁用查询缓存。
>
> Spider 存储引擎（以及其他一些引擎）不使用查询缓存。
>
> 对于 "5.5.40-galera"、"10.0.14-galera" 和 "10.1.2" 之前的 MariaDB Galera 集群版本，也需要禁用查询缓存。

#### 查询优化器 (Query Optimizer)

> 查询优化器本质上是一个对数据库关系引擎工作方式进行“建模”的软件。利用查询处理器树和它拥有的关于数据的统计信息，并应用该模型，它会计算出它认为执行查询的最佳方式——也就是说，它会生成一个执行计划。
>
> ##### 基于成本 (Cost Based)
>
> ```它决定是否可以通过索引访问数据、使用哪种类型的连接等等。优化器做出的决策基于它计算出的给定执行计划的成本，包括所需的 CPU 处理和 I/O，以及它的执行速度。```
>
> ##### 平凡计划 (Trivial Plan)
>
> ```对于一个没有索引、查询中没有聚合或计算的单表——优化器不会花时间尝试计算绝对最佳计划，而是简单地应用一个单一的计划。```
>
> 一旦优化器得出执行计划，实际计划就会被创建并存储在称为 `计划缓存 (plan cache)` 的内存空间中——除非缓存中已经存在相同的计划。
> 当优化器生成潜在计划时，它会将其与缓存中先前生成的计划进行比较。如果找到匹配项，它将使用该计划。

#### 查询执行计划 (Query Execution Plan)

有两种不同类型的执行计划。首先是代表优化器输出的计划，这被称为“估计执行计划 (Estimated execution plan)”。计划中的操作符或步骤将被标记为逻辑操作符，因为它们代表了优化器对计划的视图。

接下来是代表实际查询执行输出的计划。这种类型的计划被称为“实际执行计划 (Actual execution plan)”。它显示了查询执行时实际发生的情况。

### 事务 (Transaction)

为了使数据库管理系统 (DBMS) 高效且准确地运行，它必须具备 ACID 事务。

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
> 聚簇索引 (ClusteredIndex) 与辅助索引具有相同的结构。辅助索引包含集群键。
> 这意味着，如果聚簇索引或辅助索引发生更改，则需要更改数据记录的地址。

1. 搜索 `index_first_name` 以获取记录地址。
2. 使用记录地址获取结果。

> #### InnoDB
>
> 所有的辅助索引都存储主键索引。因此，当辅助索引更改时，不需要更改数据记录的地址。

1. 搜索 `index_first_name` 并获取主键值。
2. 使用主键获取记录地址。
3. 使用记录地址获取结果。

---

## ACID

- **原子性 (Atomicity)**
  - 原子性保证每个事务都被视为一个单一的“单元”。
- **一致性 (Consistency)**
  - 写入数据库的任何数据都必须根据所有定义的规则（包括约束、级联、触发器及其任何组合）有效。如果某些事务忽略了上述规则，则该事务应被取消。
- **隔离性 (Isolation)**
  - 事务通常是并发执行的（例如，多个事务同时对一个表进行读取和写入）。隔离性确保事务的并发执行使数据库处于与按顺序执行事务时所获得的相同状态。隔离性是并发控制的主要目标。
- **持久性 (Durability)**
  - 一旦事务被提交，即使在系统故障（例如停电或崩溃）的情况下，它也将保持提交状态。

## 结论

了解基于 ACID 的 DBMS 事务。
下次我的帖子可能是关于 RDBMS 的规范化。
RDBMS 的规范化是一个维护完整性的过程。

> _Stay Hungry, Stay Foolish_

## 附录

- [维基百科 (Wikipedia)](https://en.wikipedia.org/wiki/Database#Database_management_system)
- [查询 (Query)](https://www.red-gate.com/simple-talk/sql/performance/execution-plan-basics/)
- [SQL w3school](https://www.w3schools.com/sql/trysql.asp?filename=trysql_op_in)
