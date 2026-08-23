---
layout: post
title: "Effective Kotlin - プロパティは動作ではなく状態を表すべき"
description: "KotlinのプロパティはJavaのフィールドと似て見えますが、異なる概念を持っています。//Kotlinproperty var name:String?=null //Javafield String name=null; 同じ方法で使用するように見えても、Kotlinのプロパティはより多くのことができます..."
date: 2021-08-19 00:43:04 +0900
section: blog
category: engineering
lang: ja
ref: 2021-08-19-legacy-261-engineering-effective-kotlin-properties-should-represent-state-not-behavior
tags:
  - "プロパティ"
  - "Properties"
  - "Kotlin"
  - "Effective"
  - "Computer"
  - "engineering"
translation_source_hash: 84d4c4309cd5c051b990741049746b5e53c3d9e9bdba314b6932a365f1290fb4
---

<h3>
KotlinのプロパティはJavaのフィールドと似て見えますが、異なる概念を持っています。
</h3>
<pre class="html xml">
<code>
//Kotlinproperty
var name:String?=null

//Javafield
String name=null;
</code>
</pre>
<h3>
同じ方法で使用するように見えても、Kotlinのプロパティはより多くのことができます。
</h3>
<blockquote>
<p>
プロパティ宣言の完全な構文
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
カスタムGet、Set ( var )
</h4>
<pre class="cs">
<code>
var name: String? = null
    get() = field?.toUpperCase()
    set(value) { if(!value.isNullOrBlank()) { field = value }
</code>
</pre>
<h4>
カスタムGet ( val )
</h4>
<pre class="dart">
<code>
val fullName: String?
    get() = "$name $surname"
</code>
</pre>
<h4>
バッキングフィールド
</h4>
<p>
フィールドをカスタマイズして宣言することはできません。ただし、プロパティにバッキングフィールドが必要な場合、自動的に生成されます。このバッキングフィールドは、アクセサ内で field 識別子を使用して参照できます。
</p>
<pre class="sql">
<code>
var counter = 0 // 初期化子はバッキングフィールドを直接割り当てます
    set(value) {
        if (value &gt;= 0)
            field = value
            // counter = value // エラー StackOverflow: 実際の名前 'counter' を使用するとセッターが再帰的になります
    }
</code>
</pre>
<h4>
関数との違いは？
</h4>
<p>
Kotlinでのプロパティはそのオブジェクトの<b>状態</b>を意味するのに対し、関数はそのオブジェクトの<b>動作</b>を意味します。
</p>
<pre class="kotlin">
<code>
// プロパティ
val isEmpty: Boolean
  get() = amount == 0
</code>
</pre>
<pre class="kotlin">
<code>
// 関数
fun isEmpty(): Boolean {
  return amount == 0
}
</code>
</pre>
<h3>
考えてみましょう。
</h3>
<h4>
常にプロパティを利用するほうが良いでしょうか？
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
上記のコードを改善する場合、次のようになります。<br>
アクセスするたびに毎回演算を行うのは非効率的だからです。
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
データを保持せずにそのプロパティを使用できます。
</h4>
<p>
何らかの理由でDate型を直接使用できない場合でも、Kotlinのプロパティ機能を使用して、Date型のデータを保存するのではなく、他の値を利用してDate型の値を使用できます。（シリアル化などを行う場合、millisの値だけを保持しておき、使用時にDate形式に変換する形態）
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
プロパティは単純なフィールドではなく、アクセサとしても使用できます。
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
プロパティ機能は万能でしょうか？
</h4>
<blockquote>
<p>
<b>
ループ、繰り返しなどの特定のロジックが含まれている、またはアルゴリズム的な部分
</b>
が注入されたプロパティは<b>正しい使用法ではありません。</b>
</p>
</blockquote>
<pre class="kotlin">
<code>
// このようなことはしないでください！
val Tree&lt;Int&gt;.sum:Int
    get() = when (this) {
        is Leaf -&gt; value
        is Node -&gt; left.sum + right.sum
    }
</code>
</pre>
<p>
プロパティは通常、状態を表したり設定したりするためにのみ使用する必要があります。<br>
プロパティを使用するよりも関数を使用することを推奨する例を挙げます。
</p>
<ul>
<li>
O(1) よりも計算量が大きい場合（計算コストが高い場合）
</li>
<li>
単純作業（ログ出力、要素の更新など）以上のビジネスロジックが含まれる場合
</li>
<li>
メンバーを2回連続で呼び出した際に、異なる結果が出力される場合
</li>
<li>
Int.toDouble() のように慣用的な表現の重複が生じる場合
</li>
<li>
Getter内でプロパティの状態を変更する場合
</li>
</ul>
<h4>
参考資料
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