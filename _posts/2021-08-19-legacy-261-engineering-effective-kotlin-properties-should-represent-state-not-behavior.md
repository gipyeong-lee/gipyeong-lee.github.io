---
layout: post
title: "Effective Kotlin - Properties should represent state, not behavior"
description: "코틀린의 속성은 자바의 필드와 비슷해 보입니다. 그렇지만, 서로 다른 컨셉을 갖고 있습니다. //Kotlinproperty var name:String?=null //Javafield String name=null; 같은 방식으로 사용할지라도, 코틀린의 속성은 좀 더 많은 것을 할..."
date: 2021-08-19 00:43:04 +0900
section: blog
category: engineering
lang: ko
ref: 2021-08-19-legacy-261-engineering-effective-kotlin-properties-should-represent-state-not-behavior
tags:
  - "속성"
  - "Properties"
  - "Kotlin"
  - "Effective"
  - "Computer"
  - "engineering"
---

<h3>
코틀린의 속성은 자바의 필드와 비슷해 보입니다. 그렇지만, 서로 다른 컨셉을 갖고 있습니다.
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
같은 방식으로 사용할지라도, 코틀린의 속성은 좀 더 많은 것을 할 수 있다.
</h3>
<blockquote>
<p>
property 선언에 대한 전체 구문
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
Custom Get, Set ( var )
</h4>
<pre class="cs">
<code>
var name: String? = null
    get() = field?.toUpperCase()
    set(value) { if(!value.isNullOrBlank()) { field = value }
</code>
</pre>
<h4>
Custom Get ( val )
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
필드는 커스터마이징하게 선언할 수 없습니다. 다만, 속성에 지원 필드가 필요할경우 자동으로 생성합니다. 이 지원 필드는 field 식별자를 사용하여 접근자에서 참조할 수 있습니다.
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
Different with function?
</h4>
<p>
코틀린에서의 프로퍼티는 해당 객체의
<b>
상태
</b>
를 의미한다면, 함수는 해당 객체의
<b>
행위
</b>
를 의미합니다.
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
생각해봅시다.
</h3>
<h4>
항상 속성을 이용하는 방식이 좋을까요?
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
다음의 코드를 개선을 한다면 다음처럼 개선을 할 수 있습니다.
<br>
접근할때마다 매번 연산을 하는것은 비효율 적이기 떄문이지요.
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
데이터를 보유하지 않은채, 해당 속성을 사용할 수 있다.
</h4>
<p>
어떤 연유로, date 유형을 사용하지 못하는 경우에도, 코틀린의 속성 기능을 사용해서, Date유형의 데이터를 저장하는 것이 아니라, 다른 값을 이용해서, Date 유형의 값을 사용하 수 있다. ( 직렬화등을 할 경우, millis 에 대해서만 값을 갖고 있다가, 사용할때는, Date 형태로 변환하는 형태 )
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
속성은 단순 필드가 아닌, 접근자로서도 사용할 수 있습니다.
</h4>
<pre class="reasonml">
<code>
valContext.preferences:SharedPreferences
    get() = PreferenceManager.getDefaultSharedPreferences(this)
valContext.inflater:LayoutInflater
    get() = getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
valContext.notificationManager:NotificationManager
    get() = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
</code>
</pre>
<h4>
속성기능은 만능일까요?
</h4>
<blockquote>
<p>
<b>
순환, 반복 등과 같은 특정한 로직이 들어가거나, 알고리즘적인 부분
</b>
이 주입된 속성은
<b>
올바른 사용법이 아닙니다.
</b>
</p>
</blockquote>
<pre class="kotlin">
<code>
// Don't do this !
val Tree&lt;Int&gt;.sum:Int
    get() = when (this) {
        is Leaf -&gt; value
        is Node -&gt; left.sum + right.sum
    }
</code>
</pre>
<p>
Property (속성)은 일반적으로 상태를 나타내거나, 설정하는 데에만 사용해야합니다.
<br>
속성을 사용하기보다 함수를 사용하길 권장하는 예시를 드립니다.
</p>
<ul>
<li>
O(1) 보다 복잡도가 높을 경우 ( 계산 비용이 많이 들경우 )
</li>
<li>
단순 작업 (로깅, 요소 업데이트 등) 이상의 비즈니스 로직을 담을 경우
</li>
<li>
멤버를 두 번 연속 호출시, 다른 결과가 출력될 경우.
</li>
<li>
Int.toDouble() 과 같이 관례적 표현의 중복이 생길 경우.
</li>
<li>
Getter 에서 속성의 상태를 변경할 경우.
</li>
</ul>
<h4>
참고
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
