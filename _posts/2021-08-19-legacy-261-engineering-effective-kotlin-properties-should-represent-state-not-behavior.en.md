---
layout: post
title: "Effective Kotlin - Properties should represent state, not behavior"
description: "Kotlin properties may look similar to Java fields, but they have different concepts. Even if you use them in the same way, Kotlin properties can do much more..."
date: 2021-08-19 00:43:04 +0900
section: blog
category: engineering
lang: en
ref: 2021-08-19-legacy-261-engineering-effective-kotlin-properties-should-represent-state-not-behavior
tags:
  - "Properties"
  - "Kotlin"
  - "Effective"
  - "Computer"
  - "engineering"
translation_source_hash: 84d4c4309cd5c051b990741049746b5e53c3d9e9bdba314b6932a365f1290fb4
---

<h3>
Kotlin properties may look similar to Java fields, but they have different concepts.
</h3>
<pre class="html xml">
<code>
// Kotlin property
var name: String? = null

// Java field
String name = null;
</code>
</pre>
<h3>
Even if you use them in the same way, Kotlin properties can do much more.
</h3>
<blockquote>
<p>
Full syntax for property declaration
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
Custom Get, Set (var)
</h4>
<pre class="cs">
<code>
var name: String? = null
    get() = field?.toUpperCase()
    set(value) { if(!value.isNullOrBlank()) { field = value } }
</code>
</pre>
<h4>
Custom Get (val)
</h4>
<pre class="dart">
<code>
val fullName: String?
    get() = "$name $surname"
</code>
</pre>
<h4>
Backing Fields
</h4>
<p>
Fields cannot be declared customly. However, Kotlin automatically generates a backing field if the property requires one. This backing field can be accessed in accessors using the `field` identifier.
</p>
<pre class="sql">
<code>
var counter = 0 // the initializer assigns the backing field directly
    set(value) {
        if (value &gt;= 0)
            field = value
            // counter = value // ERROR StackOverflow: Using actual name 'counter' would make setter recursive
    }
</code>
</pre>
<h4>
Different from functions?
</h4>
<p>
In Kotlin, if a property represents the <b>state</b> of an object, a function represents the <b>behavior</b> of that object.
</p>
<pre class="kotlin">
<code>
// property
val isEmpty: Boolean
  get() = amount == 0
</code>
</pre>
<pre class="kotlin">
<code>
// function
fun isEmpty(): Boolean {
  return amount == 0
}
</code>
</pre>
<h3>
Let's think about it.
</h3>
<h4>
Is it always better to use properties?
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
The code above can be improved as follows:
<br>
Because calculating it every time it is accessed is inefficient.
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
You can use properties without holding data.
</h4>
<p>
For some reason, even if you cannot use the `Date` type, you can use Kotlin's property features to work with `Date` values by using other values instead of storing actual `Date` type data (e.g., when serializing, you might hold only the `millis` value and convert it to `Date` format when used).
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
Properties can be used as accessors, not just as simple fields.
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
Are properties a silver bullet?
</h4>
<blockquote>
<p>
<b>
Properties that contain specific logic such as loops, recursion, or algorithmic parts
</b>
are <b>not the correct way to use them.</b>
</p>
</blockquote>
<pre class="kotlin">
<code>
// Don't do this!
val Tree&lt;Int&gt;.sum: Int
    get() = when (this) {
        is Leaf -&gt; value
        is Node -&gt; left.sum + right.sum
    }
</code>
</pre>
<p>
Properties should generally only be used to represent or set state.
<br>
Here are examples where using a function is recommended over using a property:
</p>
<ul>
<li>
When the complexity is higher than O(1) (i.e., calculation is computationally expensive)
</li>
<li>
When it contains business logic beyond simple operations (e.g., logging, updating elements)
</li>
<li>
When calling the member twice in a row produces different results
</li>
<li>
When it duplicates conventional expressions like `Int.toDouble()`
</li>
<li>
When the getter changes the state of the property
</li>
</ul>
<h4>
References
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