---
layout: post
title: "Effective Kotlin - 处理大型集合时，若有多个处理步骤，请优先使用 Sequence"
description: "总结：即时求值 (Eager evaluation) 与 延迟求值 (Lazy evaluation) 的区别。顺序很重要，listOf 等 iterable 结构的结果与 sequenceOf 的结果不同。sequenceOf(1,2,3) .filter { print(\"F..."
date: 2021-10-28 12:40:30 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2021-10-28-legacy-274-engineering-effective-kotlin-prefer-sequence-for-big-collections-with-more-than-one-processing-step
tags:
  - "Computer"
  - "engineering"
translation_source_hash: 4169f25082ca263494ba918717ac85cb5431779b94f38fa33cd5e6139bd28fa5
---

<h1>
总结
</h1>
<p>
<span>
即时求值 (Eager evaluation) 与
<span>
延迟求值 (Lazy evaluation)
</span>
</span>
</p>
<h2>
顺序很重要
</h2>
<p>
像 listOf 这样的 iterable 结构的结果与 sequenceOf 的结果值是不同的。
</p>
<pre class="dart">
<code>
sequenceOf(1,2,3)
    .filter { print("F$it, "); it % 2 == 1 }
    .map { print("M$it, "); it * 2 }
    .forEach { print("E$it,")}

// 打印：F1, M1, E2, F2, F3, M3, E6,

listOf(1,2,3)
       .filter { print("F$it, "); it % 2 == 1 }
       .map { print("M$it, "); it * 2 }
       .forEach { print("E$it, ") }

// 打印：F1, F2, F3, M1, M3, E2, E6,
</code>
</pre>
<p>
<a href="https://pl.kotl.in/fi1wJyWPw" target="_blank" rel="noopener">
代码测试
</a>
</p>
<h2>
Sequence 执行最少的操作
</h2>
<p>
执行最少的工作。
</p>
<pre class="armasm">
<code>
(1..10).asSequence()
   .filter { print("F$it, "); it % 2 == 1 }
   .map { print("M$it, "); it * 2 }
   .find { it &gt; 5 }
// 打印：F1, M1, F2, F3, M3,

(1..10)
   .filter { print("F$it, "); it % 2 == 1 }
   .map { print("M$it, "); it * 2 }
   .find { it &gt; 5 }
// 打印：F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, M1, M3, M5, M7, M9,
</code>
</pre>
<p>
<a href="https://pl.kotl.in/Ckjd2eyoY" target="_blank" rel="noopener">
代码测试
</a>
</p>
<h2>
Sequence 可以是无限的
</h2>
<p>
Sequence 可以是无限的。
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
// 无限运行
</code>
</pre>
<p>
<a href="https://pl.kotl.in/l9tWJyaT2" target="_blank" rel="noopener">
代码测试
</a>
</p>
<h2>
Sequence 不会在每个处理步骤中创建集合
</h2>
<pre class="angelscript">
<code>
numbers
   .filter { it % 10 == 0 } // 这里创建了 1 个集合
   .map { it * 2 } // 这里创建了 1 个集合
   .sum()
// 总共在后台创建了 2 个集合
numbers
   .asSequence()
   .filter { it % 10 == 0 }
   .map { it * 2 }
   .sum()
// 没有创建集合
</code>
</pre>
<h2>
Sequence 什么时候不一定更快？
</h2>
<p>
据说目前为止 sorted 函数是唯一的特例。
<br>
<b>
注意
</b>
：如果对 <b>无限的</b> Sequence 进行 sorted 处理，可能会陷入死循环。
</p>
<pre class="yaml">
<code>
generateSequence(0) { it + 1 }.take(10).sorted().toList()
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
generateSequence(0) { it + 1 }.sorted().take(10).toList()
// 无限耗时。不会返回结果。
</code>
</pre>
<h2>
结论
</h2>
<p>
当处理巨大的集合，且包含一个以上的处理步骤时，应该使用 Sequence 来进行处理。
</p>