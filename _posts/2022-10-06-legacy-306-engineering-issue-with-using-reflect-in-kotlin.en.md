---
layout: post
title: "Issue with using reflect in kotlin"
description: "Class kotlin.reflect.jvm.internal.calls.CallerImpl $ FieldGetter can not access a member of class I encountered the following issue. Why? I did some research. After reading the post mentioned in the Reference below, I understood it. I have translated the answer from the post below."
date: 2022-10-06 08:21:13 +0900
section: blog
category: engineering
lang: en
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
I encountered the following issue.
</p>

<p>
Why? I did some research.
</p>
<p>
After reading the post mentioned in the Reference below, I understood it.
</p>
<p>
I have translated the answer from the post below.
</p>
<blockquote>
I see your point and largely agree. However, Kotlin reflection works on a slightly different model. It represents the program structure as closely as possible to what the compiler sees at compile-time. One could argue whether this is the right goal to pursue, but there are specific benefits to this approach. For example, it ensures that systems designed for runtime (e.g., DI) align with the equivalent systems used by the Kotlin compiler at compile-time with minimal discrepancy. It also makes the implementation of Kotlin reflection easier and more reliable because the core is fundamentally the same as the compiler's core and is very thoroughly tested.
<br>
<br>
The issue is that Java fields and get/set methods are not considered a single property by the Kotlin compiler, or cannot be referenced via ::, which is impossible according to KT-8575. (The fact that you can call a Java get-method as foo.bar instead of foo.getBar() is purely syntactic sugar and does not affect the language or declaration structure used by the compiler.) Theoretically, we could branch the representation of Java fields/get-set methods here with the compiler, but we are against it for now.
<br>
<br>
To explain, I will provide a somewhat practical use case. Consider that you have implemented a dependency injection framework via this hypothetical new Kotlin reflection (where Java field + get/set-method is considered a KProperty), and some code in the project where this framework is used is implemented in Java. Then you decide not to use this framework in favor of a static compile-time based solution that works using symbols loaded from the Kotlin compiler.
<br>
<br>
The process is fairly simple because you convert reflection-based code into code using the Compiler API (not public yet, but will be) and because reflection works on almost the same kind of symbols as the compiler. However, you then run code generation and find that the provision of Java classes is broken because the compiler perceives these things differently. This example is slightly contrived, but I hope it explains why I am arguing for representational equivalence here.
<br>
<br>
In my opinion, the best way to solve this problem is to redesign how Java fields and get/set methods are represented in the language and compiler. If we can make the compiler believe that a private Java field with a public getter is a proper Kotlin property, we can fix KT-6653, KT-8575, KT-15620, etc., and also observe these properties via reflection as requested. Also, once those changes are implemented in the language, they will automatically work in Kotlin reflection.
<br>
<br>
Therefore, this is more of a request for language design and the compiler than for reflection. Specifically, KT-6653 is a major issue related to loading properties from Java code, so I recommend voting and watching it. Sorry for the rather long post. I understand your confusion, but I don't think we should fix this only in reflection, not in the whole language. Of course, this decision is not completely final, and if we find other strong use cases, we can reconsider whether keeping the structure 1:1 with the compiler is the right thing to do.
</blockquote>

## References

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