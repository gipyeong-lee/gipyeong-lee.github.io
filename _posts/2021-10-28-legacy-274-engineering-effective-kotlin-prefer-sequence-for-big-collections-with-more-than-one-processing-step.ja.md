---
layout: post
title: "Effective Kotlin - 複数の処理ステップがある大きなコレクションにはSequenceを推奨"
description: "要約 Eager evaluation（先行評価）とLazy evaluation（遅延評価） 順序は重要です listOfのようなIterableな構造の結果とsequenceOfの結果は異なります。 sequenceOf(1,2,3) .filter { print(\"F..."
date: 2021-10-28 12:40:30 +0900
section: blog
category: engineering
lang: ja
ref: 2021-10-28-legacy-274-engineering-effective-kotlin-prefer-sequence-for-big-collections-with-more-than-one-processing-step
tags:
  - "Computer"
  - "engineering"
translation_source_hash: 4169f25082ca263494ba918717ac85cb5431779b94f38fa33cd5e6139bd28fa5
---

<h1>
要約
</h1>
<p>
<span>
Eager evaluation（先行評価） vs
<span>
Lazy evaluation（遅延評価）
</span>
</span>
</p>
<h2>
順序は重要です
</h2>
<p>
listOfのようなIterableな構造の結果とsequenceOfの結果は異なります。
</p>
<pre class="dart">
<code>
sequenceOf(1,2,3)
    .filter { print("F$it, "); it % 2 == 1 }
    .map { print("M$it, "); it * 2 }
    .forEach { print("E$it,")}

// 出力: F1, M1, E2, F2, F3, M3, E6,

listOf(1,2,3)
       .filter { print("F$it, "); it % 2 == 1 }
       .map { print("M$it, "); it * 2 }
       .forEach { print("E$it, ") }

// 出力: F1, F2, F3, M1, M3, E2, E6,
</code>
</pre>
<p>
<a href="https://pl.kotl.in/fi1wJyWPw" target="_blank" rel="noopener">
コードテスト
</a>
</p>
<h2>
Sequenceは最小限の操作のみを行います
</h2>
<p>
必要な最小限の作業を行います。
</p>
<pre class="armasm">
<code>
(1..10).asSequence()
   .filter { print("F$it, "); it % 2 == 1 }
   .map { print("M$it, "); it * 2 }
   .find { it &gt; 5 }
// 出力: F1, M1, F2, F3, M3,

(1..10)
   .filter { print("F$it, "); it % 2 == 1 }
   .map { print("M$it, "); it * 2 }
   .find { it &gt; 5 }
// 出力: F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, M1, M3, M5, M7, M9,
</code>
</pre>
<p>
<a href="https://pl.kotl.in/Ckjd2eyoY" target="_blank" rel="noopener">
コードテスト
</a>
</p>
<h2>
Sequenceは無限になり得ます
</h2>
<p>
Sequenceは無限の要素を持つことができます。
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
// 永久に実行され続けます
</code>
</pre>
<p>
<a href="https://pl.kotl.in/l9tWJyaT2" target="_blank" rel="noopener">
コードテスト
</a>
</p>
<h2>
Sequenceは各処理ステップでコレクションを作成しません
</h2>
<pre class="angelscript">
<code>
numbers
   .filter { it % 10 == 0 } // ここでコレクションを1つ作成
   .map { it * 2 } // ここでコレクションを1つ作成
   .sum()
// 合計で、内部的に2つのコレクションが作成されます
numbers
   .asSequence()
   .filter { it % 10 == 0 }
   .map { it * 2 }
   .sum()
// コレクションは作成されません
</code>
</pre>
<h2>
Sequenceが高速にならない場合は？
</h2>
<p>
現時点では、sorted関数が唯一の例外的なケースだと言われています。
<br>
<b>
無限の
</b>
Sequenceに対してsortedを処理すると、無限ループに陥る可能性があるため注意してください。
</p>
<pre class="yaml">
<code>
generateSequence(0) { it + 1 }.take(10).sorted().toList()
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
generateSequence(0) { it + 1 }.sorted().take(10).toList()
// 無限時間。終了しません。
</code>
</pre>
<h2>
結論
</h2>
<p>
巨大なコレクションを扱い、1つ以上の処理ステップがある場合は、Sequenceを使用して処理すべきです。
</p>