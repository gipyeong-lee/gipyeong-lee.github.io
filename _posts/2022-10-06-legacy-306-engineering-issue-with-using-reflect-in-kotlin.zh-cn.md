---
layout: post
title: "Kotlin 中使用 reflect 的问题"
description: "Class kotlin.reflect.jvm.internal.calls.CallerImpl $ FieldGetter can not access a member of class 遇到了这个问题。为什么呢？我进行了研究，阅读了下文参考资料中提到的内容后理解了。以下是对文章回复的翻译。"
date: 2022-10-06 08:21:13 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2022-10-06-legacy-306-engineering-issue-with-using-reflect-in-kotlin
tags:
  - "reflect"
  - "Kotlin"
  - "Server"
  - "engineering"
translation_source_hash: f7faa6da0cacf0ee47712a10bf61c83f1964de9844336be44ee557a0125cb57f
---

<p>

<i>
Class
</i>

<i>
kotlin.reflect.jvm.internal.calls.CallerImpl
</i>
<span>
$
</span>
<i>
FieldGetter
</i>

<i>
can
</i>

<i>
not
</i>

<i>
access
</i>

<i>
a
</i>

<i>
member
</i>

<i>
of
</i>

<i>
class
</i>
</p>

<p>
遇到了这个问题。
</p>

<p>
为什么呢？我进行了研究。
</p>
<p>
阅读了下文参考资料中提到的内容后理解了。
</p>
<p>
以下是对文章回复的翻译。
</p>
<blockquote>
我理解并大体同意您的观点。但是，Kotlin 反射是在一个略有不同的模型上运行的。它旨在表现出尽可能与编译器在编译时所见一致的程序结构。您可以质疑这是否是应该追求的正确目标，但这种方法有特定的优点。例如，它使为运行时设计的系统（如 DI）能够与 Kotlin 编译器在编译时使用的等效系统保持最小差异。此外，由于核心内容在本质上与编译器核心相同，并且经过了极其彻底的测试，这使得 Kotlin 反射的实现变得更加简单和可靠。
<br>
<br>
问题在于，Java 字段以及 get/set 方法在 Kotlin 编译器中并不被视为单个属性。或者无法通过 :: 进行引用，根据 KT-8575 的说法，这是不可能的。（可以将 Java get 方法作为 foo.bar 而非 foo.getBar() 来调用，这纯粹是语法糖，不会影响编译器使用的语言或声明结构。）理论上，我们可以与编译器一起在这里分化 Java 字段/get-set 方法的表现形式，但目前我们反对这样做。
<br>
<br>
为了说明这一点，我提供一个比较实际的用例。假设您通过这种虚构的新 Kotlin 反射（其中 Java 字段 + get/set 方法被视为 KProperty）实现了一个依赖注入框架，并且该框架所使用的项目中的部分代码是用 Java 实现的。然后，您决定不使用该框架，转而选择使用加载在 Kotlin 编译器中的符号来工作的静态编译时解决方案。
<br>
<br>
使用编译器 API（虽然尚未公开，但预计会公开）将基于反射的代码转换为代码，由于反射在与编译器几乎相同的符号种类上工作，该过程相当简单。但是，随后您会发现代码生成运行失败，因为编译器对这些事物的识别方式不同。这个例子可能有点牵强，但我希望它能解释我在这里坚持表现等价性的理由。
<br>
<br>
在我看来，解决这个问题最好的方法是重新设计 Java 字段和 get/set 方法在语言和编译器中的表现方式。如果我们能让编译器认为带有 public getter 的 private Java 字段是适当的 Kotlin 属性，从而修复 KT-6653、KT-8575、KT-15620 等问题，那么正如您所要求的，这些属性也可以通过反射观察到。而且，如果该变更在语言中实现，它会自动在 Kotlin 反射中生效。
<br>
<br>
因此，比起对反射的请求，这更接近于对语言设计和编译器的请求。特别是 KT-6653 是与从 Java 代码加载属性相关的主要问题，建议您投票并关注。很抱歉篇幅较长。我理解您的困惑，但我不认为我们应该只在反射层面解决这个问题，而不是在整个语言层面。当然，这个决定并不是最终的，如果您发现了其他强有力的用例，我们可能会重新考虑是否保持与编译器 1:1 的结构是正确的做法。
</blockquote>

## 参考资料
<p>
<a href="https://youtrack.jetbrains.com/issue/KT-27928" target="_blank" rel="noopener">
https://youtrack.jetbrains.com/issue/KT-27928
</a>
</p>
<figure>
<a href="https://youtrack.jetbrains.com/issue/KT-27928" target="_blank" rel="noopener">

<div class="og-text">
<p class="og-title">
Please make it possible to access java property values through kotlin reflection : KT-27928
</p>
<p class="og-desc">
Given the following code: package my import java.time.LocalTime import kotlin.reflect.KProperty import kotlin.reflect.full.memberProperties fun main(args: ArrayᐸStringᐳ) { val time = LocalTime.parse("10:00:00") println(time.hour) val property = LocalTi
</p>
<p class="og-host">
youtrack.jetbrains.com
</p>
</div>
</a>
</figure>
<p>
<a href="https://youtrack.jetbrains.com/issue/KT-6653" target="_blank" rel="noopener">
https://youtrack.jetbrains.com/issue/KT-6653
</a>
</p>
<figure>
<a href="https://youtrack.jetbrains.com/issue/KT-6653" target="_blank" rel="noopener">

<div class="og-text">
<p class="og-title">
Kotlin properties do not override Java-style getters and setters : KT-6653
</p>
<p class="og-desc">
Kotlin properties aren't being counted as implementations for abstract methods with the same signature Example package org.marioarias.demo import org.springframework.security.core.userdetails.UserDetails import org.springframework.security.core.GrantedAuth
</p>
<p class="og-host">
youtrack.jetbrains.com
</p>
</div>
</a>
</figure>
<p>
<a href="https://youtrack.jetbrains.com/issue/KT-8575" target="_blank" rel="noopener">
https://youtrack.jetbrains.com/issue/KT-8575
</a>
</p>
<figure>
<a href="https://youtrack.jetbrains.com/issue/KT-8575" target="_blank" rel="noopener">

<div class="og-text">
<p class="og-title">
Support Java synthetic property references : KT-8575
</p>
<p class="og-desc">
May 2022 Postponed due to a lack of resources. November 2021 Planned to be Experimental in 1.7. *** public class J { private String value; public J(String value) { this.value = value; } public String getValue() { return value; } public void setValue(String
</p>
<p class="og-host">
youtrack.jetbrains.com
</p>
</div>
</a>
</figure>
<p>
<a href="https://youtrack.jetbrains.com/issue/KT-15620" target="_blank" rel="noopener">
https://youtrack.jetbrains.com/issue/KT-15620
</a>
</p>
<figure>
<a href="https://youtrack.jetbrains.com/issue/KT-15620" target="_blank" rel="noopener">

<div class="og-text">
<p class="og-title">
Implement 'expect' member property by Java getter/setter : KT-15620
</p>
<p class="og-desc">
// common.kt expect interface I { val type: Int } // jvm.kt actual typealias I = SomePlatformInterface // SomePlatformInterface.java public interface SomePlatformInterface { public int getType() { return 42; } }…
</p>
<p class="og-host">
youtrack.jetbrains.com
</p>
</div>
</a>
</figure>