---
layout: post
title: "Effective Kotlin - 属性应代表状态，而非行为"
description: "Kotlin 的属性看起来与 Java 的字段相似，但它们有着不同的概念。//Kotlinproperty var name:String?=null //Javafield String name=null; 即使使用方式相同，Kotlin 的属性也能做更多的事情..."
date: 2021-08-19 00:43:04 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2021-08-19-legacy-261-engineering-effective-kotlin-properties-should-represent-state-not-behavior
tags:
  - "属性"
  - "Properties"
  - "Kotlin"
  - "Effective"
  - "计算机"
  - "工程"
translation_source_hash: 84d4c4309cd5c051b990741049746b5e53c3d9e9bdba314b6932a365f1290fb4
---

<h3>
Kotlin 的属性看起来与 Java 的字段相似，但它们有着不同的概念。
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
即使使用方式相同，Kotlin 的属性也能做更多的事情。
</h3>
<blockquote>
<p>
属性声明的完整语法
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
自定义 Get, Set ( var )
</h4>
<pre class="cs">
<code>
var name: String? = null
    get() = field?.toUpperCase()
    set(value) { if(!value.isNullOrBlank()) { field = value }
</code>
</pre>
<h4>
自定义 Get ( val )
</h4>
<pre class="dart">
<code>
val fullName: String?
    get() = "$name $surname"
</code>
</pre>
<h4>
幕后字段 (Backing Fields)
</h4>
<p>
字段无法自定义声明。但是，如果属性需要幕后字段，系统会自动生成。在访问器中，可以通过 field 标识符来引用该幕后字段。
</p>
<pre class="sql">
<code>
var counter = 0 // 初始化程序直接赋值给幕后字段
    set(value) {
        if (value &gt;= 0)
            field = value
            // counter = value // 错误：堆栈溢出（StackOverflow），使用实际名称 'counter' 会使 setter 递归调用
    }
</code>
</pre>
<h4>
与函数有何不同？
</h4>
<p>
Kotlin 中的属性表示的是对象的
<b>
状态
</b>
，而函数则表示对象的
<b>
行为
</b>
。
</p>
<pre class="kotlin">
<code>
// 属性
val isEmpty: Boolean
  get() = amount == 0
</code>
</pre>
<pre class="kotlin">
<code>
// 函数
fun isEmpty(): Boolean {
  return amount == 0
}
</code>
</pre>
<h3>
让我们思考一下。
</h3>
<h4>
始终使用属性的方式更好吗？
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
若要改进上述代码，可以将其修改为如下形式。
<br>
因为每次访问时都进行计算是非常低效的。
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
可以在不持有数据的情况下使用该属性。
</h4>
<p>
由于某些原因，即使无法直接使用 Date 类型，也可以利用 Kotlin 的属性功能，不存储 Date 类型的数据，而是利用其他值来使用 Date 类型的值（例如在序列化时，只持有 millis 值，使用时转换为 Date 形式）。
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
属性不仅是简单的字段，还可以用作访问器。
</h4>
<pre class="reasonml">
<code>
val Context.preferences: SharedPreferences
    get() = PreferenceManager.getDefaultSharedPreferences(this)
val Context.inflater: LayoutInflater
    get() = getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
val Context.notificationManager: NotificationManager
    get() = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
</code>
</pre>
<h4>
属性功能是万能的吗？
</h4>
<blockquote>
<p>
<b>
包含循环、递归等特定逻辑或算法部分的
</b>
属性
<b>
并非正确的用法。
</b>
</p>
</blockquote>
<pre class="kotlin">
<code>
// 不要这样做！
val Tree&lt;Int&gt;.sum: Int
    get() = when (this) {
        is Leaf -&gt; value
        is Node -&gt; left.sum + right.sum
    }
</code>
</pre>
<p>
属性（Property）通常仅应用于表示或设置状态。
<br>
以下是建议优先使用函数而非属性的示例：
</p>
<ul>
<li>
复杂度高于 O(1) 的情况（计算成本较高时）
</li>
<li>
包含简单操作（如日志记录、元素更新等）之外的业务逻辑时
</li>
<li>
连续两次调用成员产生不同结果时
</li>
<li>
如 Int.toDouble() 这样产生重复的习惯表达时
</li>
<li>
在 Getter 中修改属性状态时
</li>
</ul>
<h4>
参考资料
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