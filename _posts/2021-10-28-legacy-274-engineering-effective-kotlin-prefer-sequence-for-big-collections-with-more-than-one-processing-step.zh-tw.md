---
layout: post
title: "Effective Kotlin - 針對具有多個處理步驟的大型集合，優先使用 Sequence"
description: "摘要 立即求值（Eager evaluation）與延遲求值（Lazy evaluation）。順序很重要。像 listOf 這類 iterable 結構的結果，與 sequenceOf 的結果值是不一樣的。sequenceOf(1,2,3) .filter { print(\"F..."
date: 2021-10-28 12:40:30 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2021-10-28-legacy-274-engineering-effective-kotlin-prefer-sequence-for-big-collections-with-more-than-one-processing-step
tags:
  - "Computer"
  - "engineering"
translation_source_hash: 4169f25082ca263494ba918717ac85cb5431779b94f38fa33cd5e6139bd28fa5
---

<h1>
摘要
</h1>
<p>
<span>
立即求值（Eager evaluation）與
<span>
延遲求值（Lazy evaluation）
</span>
</span>
</p>
<h2>
順序很重要
</h2>
<p>
像 listOf 這類 iterable 結構的結果，與 sequenceOf 的結果值是不一樣的。
</p>
<pre class="dart">
<code>
sequenceOf(1,2,3)
    .filter { print("F$it, "); it % 2 == 1 }
    .map { print("M$it, "); it * 2 }
    .forEach { print("E$it,")}

// 輸出：F1, M1, E2, F2, F3, M3, E6,

listOf(1,2,3)
       .filter { print("F$it, "); it % 2 == 1 }
       .map { print("M$it, "); it * 2 }
       .forEach { print("E$it, ") }

// 輸出：F1, F2, F3, M1, M3, E2, E6,
</code>
</pre>
<p>
<a href="https://pl.kotl.in/fi1wJyWPw" target="_blank" rel="noopener">
程式碼測試
</a>
</p>
<h2>
Sequences 執行最少量的運算
</h2>
<p>
執行最少量的作業。
</p>
<pre class="armasm">
<code>
(1..10).asSequence()
   .filter { print("F$it, "); it % 2 == 1 }
   .map { print("M$it, "); it * 2 }
   .find { it &gt; 5 }
// 輸出：F1, M1, F2, F3, M3,

(1..10)
   .filter { print("F$it, "); it % 2 == 1 }
   .map { print("M$it, "); it * 2 }
   .find { it &gt; 5 }
// 輸出：F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, M1, M3, M5, M7, M9,
</code>
</pre>
<p>
<a href="https://pl.kotl.in/Ckjd2eyoY" target="_blank" rel="noopener">
程式碼測試
</a>
</p>
<h2>
Sequences 可以是無限的
</h2>
<p>
Sequence 可以是無限的。
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
// 無限執行
</code>
</pre>
<p>
<a href="https://pl.kotl.in/l9tWJyaT2" target="_blank" rel="noopener">
程式碼測試
</a>
</p>
<h2>
Sequences 不會在每個處理步驟建立集合
</h2>
<pre class="angelscript">
<code>
numbers
   .filter { it % 10 == 0 } // 此處產生 1 個集合
   .map { it * 2 } // 此處產生 1 個集合
   .sum()
// 底層總共建立了 2 個集合
numbers
   .asSequence()
   .filter { it % 10 == 0 }
   .map { it * 2 }
   .sum()
// 未建立任何集合
</code>
</pre>
<h2>
Sequence 何時不比集合快？
</h2>
<p>
據說目前為止 sorted 函式是唯一的例外情況。
<br>
<b>
注意：
</b>
若對 <b>無限</b> 的 Sequence 進行 sorted 處理，可能會導致陷入無限迴圈，請務必小心。
</p>
<pre class="yaml">
<code>
generateSequence(0) { it + 1 }.take(10).sorted().toList()
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
generateSequence(0) { it + 1 }.sorted().take(10).toList()
// 無限時間。不會返回結果。
</code>
</pre>
<h2>
結論
</h2>
<p>
處理巨大集合且包含一個以上的處理步驟時，應使用 Sequence 來進行操作。
</p>