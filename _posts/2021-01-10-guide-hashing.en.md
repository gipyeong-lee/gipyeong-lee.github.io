---
layout: post
title: "Database - Part 5: Consistent Hashing"
style: border
color: info
description: What is consistent hashing? Before understanding this, first, hashing can be understood as `chopping and mixing`. A Hash Map is a data structure that maps data to an index. It can be said to be the most efficient as O(1). It is generally stored as key-value pairs.
lang: en
ref: 2021-01-10-guide-hashing
---

### Overview

What is consistent hashing?
Before understanding this, first, hashing can be understood as `chopping and mixing`. A Hash Map is a data structure that maps data to an index. It can be said to be the most efficient as O(1). It is generally stored as key-value pairs.

Let's just talk about hashing to this extent and talk about distributed hashing.

#### Distributed Hashing

Let's assume we have the hash table below. Now we will store this data in a distributed data store.

| KEY     | HASH       | HASH mod `3` |
|---------|------------|--------------|
| "john"  | 1633428562 | 2            |
| "bill"  | 7594634739 | 0            |
| "jane"  | 5000799124 | 1            |
| "steve" | 9787173343 | 0            |
| "kate"  | 3421657995 | 2            |

If we divide and store it on three servers, it is organized as follows.
They have indices of A:0, B:1, C:2 respectively.

| A       | B      | C      |
|---------|--------|--------|
| "bill"  | "jane" | "john" |
| "steve" |        | "kate" |

Imagine a situation where one piece of equipment suddenly breaks down while using it well like this. If we assume server C goes down, data will be allocated to the hash table and servers again as follows.

| KEY     | HASH       | HASH mod `2` |
|---------|------------|--------------|
| "john"  | 1633428562 | 0            |
| "bill"  | 7594634739 | 1            |
| "jane"  | 5000799124 | 0            |
| "steve" | 9787173343 | 1            |
| "kate"  | 3421657995 | 1            |

Now, data will be stored in the two storages A:0, B:1 as follows.

| A      | B       |
|--------|---------|
| "john" | "bill"  |
| "jane" | "steve" |
| "kate" |         |

If this happens, the location of all keys that existed in C will change. At this time, a re-hashing task from the original data is required, which puts a load on the original server. And in the meantime, the data requested by the client is lost.

The hashing technique that came out to solve this is Consistent Hashing.

### Consistent Hashing

![image](/assets/images/blog/2021-01-10-hashing/hashing.png){: width="60%"}

The image above is everything I will talk about this time.
Let's assume we are hashing according to the image above.

| KEY     | HASH       | ANGLE (DEG) |
|---------|------------|-------------|
| "john"  | 1633428562 | 58.7        |
| "C"     | 2269549488 | 81.7        |
| "kate"  | 3421657995 | 123.1       |
| "jane"  | 5000799124 | 180         |
| "A"     | 5572014557 | 200.5       |
| "bill"  | 7594634739 | 273.4       |
| "B"     | 8077113361 | 290.7       |
| "steve" | 787173343  | 352.3       |

Place the servers in the hashing table as well.

Here, there is one rule for finding the server where each key is located.

**The nearest server when rotating counter-clockwise is the storage where the key is located.**

Summarizing the storage where the keys are stored based on the criteria mentioned above, it is as follows.

| KEY     | HASH       | ANGLE (DEG) | LABEL | SERVER |
|---------|------------|-------------|-------|--------|
| "john"  | 1632929716 | 58.7        | "C"   | C      |
| "kate"  | 3421831276 | 123.1       | "A"   | A      |
| "jane"  | 5000648311 | 180         | "A"   | A      |
| "bill"  | 7594873884 | 273.4       | "B"   | B      |
| "steve" | 9786437450 | 352.3       | "C"   | C      |

So what on earth is the advantage of this technique?

Now let's imagine, suppose equipment C is removed. Existing techniques required all keys to be rehashed.

**Right here, through this technique, we can see that only the keys allocated to equipment C need rehashing.**

This is because the keys looking at servers A and B are already looking at the nearest locations A and B. Even if C disappears, there are no changes to those keys. Only the keys allocated to server C need rehashing.

Conversely, even if equipment is added, only K/N (number of keys / number of equipment) rehashing is required, not rehashing for all keys.

For example, when there are 3 keys and 2 pieces of equipment. If we think about one piece of equipment entering between them. If we assume it is designed so that keys enter the equipment evenly, rehashing may occur for 3/3 = 1 key, which can eventually show a balanced appearance where one key is stored per piece of equipment.

Consistent Hashing has a problem. It is key skew. How can we mitigate this?

### Ketama Consistent Hashing

![image](/assets/images/blog/2021-01-10-hashing/hashing2.png){: width="60%"}

First, the easiest way is to split the server into multiple tokens and place them on the Consistent Hashing Circle.
This is the Ketama Consistent Hashing technique. Disperse server A from A0 to A10 so that key distribution is as uniform as possible.

### Thoughts

- Ultimately, rehashing is an unavoidable problem. I think designing and creating it so that rehashing occurs minimally is a requirement for distributed processing.

### Example Project ( I simply implemented the above theory )

- [Reduster](https://github.com/gipyeong-lee/reduster)

### Appendix

- [Constant Hashing](https://www.toptal.com/big-data/consistent-hashing)
- [hashing, ketama](https://codeascraft.com/2017/11/30/how-etsy-caches)
