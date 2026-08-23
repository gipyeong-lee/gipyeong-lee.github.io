---
layout: post
title: "Effective Kotlin - 屬性應代表狀態，而非行為"
description: "Kotlin 的屬性看起來與 Java 的欄位相似。然而，它們擁有不同的概念。即使以相同的方式使用，Kotlin 的屬性也能實現更多功能..."
date: 2021-08-19 00:43:04 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2021-08-19-legacy-261-engineering-effective-kotlin-properties-should-represent-state-not-behavior
tags:
  - "屬性"
  - "Properties"
  - "Kotlin"
  - "Effective"
  - "Computer"
  - "engineering"
translation_source_hash: 84d4c4309cd5c051b990741049746b5e53c3d9e9bdba314b6932a365f1290fb4
---

<h3>
Kotlin 的屬性看起來與 Java 的欄位相似。然而，它們擁有不同的概念。
</h3>
<pre class="html xml">
<code>
//Kotlin property
var name:String?=null

//Java field
String name=null;
</code>
</pre>
<h3>
即使以相同的方式使用，Kotlin 的屬性也能實現更多功能。
</h3>
<blockquote>
<p>
屬性宣告的完整語法
</p>
</blockquote>
<pre class="fsharp">
<code>
var &lt;propertyName&gt;[: &lt;PropertyType&gt;] [= &lt;property_initializer&gt;]
    [&lt;getter&gt;]
    [&lt;setter&gt;]
</code>
</pre>
<h4>
自定義 Get, Set ( var )
</h4>
<pre class="cs">
<code>
var name: String? = null
    get() = field?.toUpperCase()
    set(value) { if(!value.isNullOrBlank()) { field = value }
</code>
</pre>
<h4>
自定義 Get ( val )
</h4>
<pre class="dart">
<code>
val fullName: String?
    get() = "$name $surname"
</code>
</pre>
<h4>
後備欄位 (Backing Fields)
</h4>
<p>
欄位無法自定義宣告。不過，當屬性需要後備欄位時，系統會自動建立。此後備欄位可以在存取器中透過 <code>field</code> 識別字進行參照。
</p>
<pre class="sql">
<code>
var counter = 0 // 初始化器直接賦值給後備欄位
    set(value) {
        if (value &gt;= 0)
            field = value
            // counter = value // 錯誤 StackOverflow：使用實際名稱 'counter' 會導致 setter 遞迴呼叫
    }
</code>
</pre>
<h4>
與函數有何不同？
</h4>
<p>
在 Kotlin 中，屬性代表該物件的<b>狀態</b>，而函數則代表該物件的<b>行為</b>。
</p>
<pre class="kotlin">
<code>
// 屬性
val isEmpty: Boolean
  get() = amount == 0
</code>
</pre>
<pre class="kotlin">
<code>
// 函數
fun isEmpty(): Boolean {
  return amount == 0
}
</code>
</pre>
<h3>
讓我們思考一下。
</h3>
<h4>
總是使用屬性的方式比較好嗎？
</h4>
<pre class="angelscript">
<code>
class FruitBucket(
    val price: Int,
    val discount: Int,
    var amount: Int
) {
  val isEmpty: Boolean
    get() = amount == 0
  val salePrice: Int
    get() = price - discount
}
</code>
</pre>
<p>
若要改善上述程式碼，可以修改如下：<br>
因為每次存取時都進行計算是沒有效率的。
</p>
<pre class="angelscript">
<code>
class FruitBucket(
    val price: Int,
    val discount: Int,
    var amount: Int
) {
  val isEmpty: Boolean
    get() = amount == 0
  val salePrice: Int = price - discount
}
</code>
</pre>
<h4>
可以在不持有資料的情況下使用該屬性。
</h4>
<p>
基於某些原因，即便無法使用 <code>Date</code> 型別，也可以利用 Kotlin 的屬性功能，不直接儲存 <code>Date</code> 型別的資料，而是利用其他數值來使用 <code>Date</code> 型別的值。（例如在進行序列化等操作時，僅持有 <code>millis</code> 的值，使用時再轉換為 <code>Date</code> 型別的形式）
</p>
<pre class="pgsql">
<code>
var date: Date
    get() = Date(millis)
    set(value) {
        millis = value.time
    }
</code>
</pre>
<h4>
屬性不僅是單純的欄位，也可以作為存取器使用。
</h4>
<pre class="reasonml">
<code>
val Context.preferences:SharedPreferences
    get() = PreferenceManager.getDefaultSharedPreferences(this)
val Context.inflater:LayoutInflater
    get() = getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
val Context.notificationManager:NotificationManager
    get() = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
</code>
</pre>
<h4>
屬性功能是萬能的嗎？
</h4>
<blockquote>
<p>
<b>
包含迴圈、重複等特定邏輯，或是注入演算法部分
</b>
的屬性，<b>並非正確的使用方式。</b>
</p>
</blockquote>
<pre class="kotlin">
<code>
// 不要這樣做！
val Tree&lt;Int&gt;.sum:Int
    get() = when (this) {
        is Leaf -&gt; value
        is Node -&gt; left.sum + right.sum
    }
</code>
</pre>
<p>
屬性 (Property) 通常應該僅用於表示狀態或進行設定。<br>
以下提供建議使用函數而非屬性的情況：
</p>
<ul>
<li>
複雜度高於 O(1) 的情況（計算成本較高時）
</li>
<li>
包含除了簡單操作（如記錄日誌、更新元素等）以外的業務邏輯時
</li>
<li>
連續兩次呼叫成員卻輸出不同結果時
</li>
<li>
會產生類似 <code>Int.toDouble()</code> 這種慣例表達式的重複時
</li>
<li>
在 Getter 中變更屬性狀態時
</li>
</ul>
<h4>
參考資料
</h4>
<ul>
<li>
<a href="https://kotlinlang.org/docs/properties.html#backing-fields">
https://kotlinlang.org/docs/properties.html#backing-fields
</a>
</li>
<li>
Effective Kotlin
</li>
</ul>