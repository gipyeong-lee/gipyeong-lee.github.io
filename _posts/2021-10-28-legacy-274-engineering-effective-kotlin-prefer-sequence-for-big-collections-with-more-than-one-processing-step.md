---
layout: post
title: "Effective Kotlin - Prefer Sequence for big collections with more than one processing step"
description: "Summary Eager evaluation vs Lazy evaluation Order is important listOf 와 같은 iterable 형태의 구조의 결과와 sequenceOf 의 결과 값은 다릅니다. sequenceOf(1,2,3) .filter { print(\"F..."
date: 2021-10-28 12:40:30 +0900
section: blog
category: engineering
lang: ko
ref: 2021-10-28-legacy-274-engineering-effective-kotlin-prefer-sequence-for-big-collections-with-more-than-one-processing-step
tags:
  - "Computer"
  - "engineering"
---

<h1>
Summary
</h1>
<p>
<span>
Eager evaluation vs
<span>
Lazy evaluation
</span>
</span>
</p>
<h2>
Order is important
</h2>
<p>
listOf 와 같은 iterable 형태의 구조의 결과와 sequenceOf 의 결과 값은 다릅니다.
</p>
<pre class="dart">
<code>
sequenceOf(1,2,3)
    .filter { print("F$it, "); it % 2 == 1 }
    .map { print("M$it, "); it * 2 }
    .forEach { print("E$it,")}

// Prints: F1, M1, E2, F2, F3, M3, E6,

listOf(1,2,3)
       .filter { print("F$it, "); it % 2 == 1 }
       .map { print("M$it, "); it * 2 }
       .forEach { print("E$it, ") }

// Prints: F1, F2, F3, M1, M3, E2, E6,
</code>
</pre>
<p>
<a href="https://pl.kotl.in/fi1wJyWPw" target="_blank" rel="noopener">
Code Test
</a>
</p>
<h2>
Sequences do the minimal number of operations
</h2>
<p>
최소한의 작업을 수행합니다.
</p>
<pre class="armasm">
<code>
(1..10).asSequence()
   .filter { print("F$it, "); it % 2 == 1 }
   .map { print("M$it, "); it * 2 }
   .find { it &gt; 5 }
// Prints: F1, M1, F2, F3, M3,

(1..10)
   .filter { print("F$it, "); it % 2 == 1 }
   .map { print("M$it, "); it * 2 }
   .find { it &gt; 5 }
// Prints: F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, M1, M3, M5, M7, M9,
</code>
</pre>
<p>
<a href="https://pl.kotl.in/Ckjd2eyoY" target="_blank" rel="noopener">
Code Test
</a>
</p>
<h2>
Sequences can be infinite
</h2>
<p>
Sequence 는 무한할 수 있습니다.
</p>
<pre class="yaml">
<code>
val fibonacci = sequence {
   yield(1)
   var current = 1
   var prev = 1
   while (true) {
       yield(current)
       val temp = prev
       prev = current
       current += temp
   }
}
print(fibonacci.take(10).toList())
// [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

print(fibonacci.toList())
// Runs forever
</code>
</pre>
<p>
<a href="https://pl.kotl.in/l9tWJyaT2" target="_blank" rel="noopener">
Code Test
</a>
</p>
<h2>
Sequences do not create collections at every processing step
</h2>
<pre class="angelscript">
<code>
numbers
   .filter { it % 10 == 0 } // 1 collection here
   .map { it * 2 } // 1 collection here
   .sum()
// In total, 2 collections created under the hood
numbers
   .asSequence()
   .filter { it % 10 == 0 }
   .map { it * 2 }
   .sum()
// No collections created
</code>
</pre>
<h2>
When aren't sequences faster ?
</h2>
<p>
현재까지는 sorted 함수가 유일한 케이스라고 합니다.
<br>
<b>
무한한
</b>
Sequence 에 대해 sorted 를 처리할 경우, 무한루프에 빠질 수 있으니 주의하세요.
</p>
<pre class="yaml">
<code>
generateSequence(0) { it + 1 }.take(10).sorted().toList()
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
generateSequence(0) { it + 1 }.sorted().take(10).toList()
// Infinite time. Does not return.
</code>
</pre>
<h2>
Conclusion
</h2>
<p>
거대한 컬렉션을 다루고,하나 이상의 프로세싱을 할 경우 Sequence 를 사용해서 다루어야 한다.
</p>
