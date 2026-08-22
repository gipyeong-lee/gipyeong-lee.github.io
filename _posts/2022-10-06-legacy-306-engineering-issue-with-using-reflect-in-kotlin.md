---
layout: post
title: "Issue with using reflect in kotlin"
description: "Class kotlin.reflect.jvm.internal.calls.CallerImpl $ FieldGetter can not access a member of class 다음의 이슈에 직면하였다. 왜일까 Research 를 하였고. 아래 Reference 에 명시한 글을 읽고..."
date: 2022-10-06 08:21:13 +0900
section: blog
category: engineering
lang: ko
ref: 2022-10-06-legacy-306-engineering-issue-with-using-reflect-in-kotlin
tags:
  - "reflect"
  - "Kotlin"
  - "Server"
  - "engineering"
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
다음의 이슈에 직면하였다.
</p>

<p>
왜일까 Research 를 하였고.
</p>
<p>
아래 Reference 에 명시한 글을 읽고 나니 이해가 되었다.
</p>
<p>
아래 글의 답변을 번역해두었다.
</p>
<blockquote>
나는 당신의 요점을보고 대부분 동의합니다. 그러나 Kotlin 리플렉션은 약간 다른 모델에서 작동합니다. 컴파일 타임에 컴파일러가 볼 수 있는 것과 최대한 유사한 프로그램 구조를 나타냅니다. 이것이 추구해야 할 올바른 목표라는 점에 대해 이의를 제기할 수 있지만 이 접근 방식에는 특정 이점이 있습니다. 예를 들어 런타임용으로 설계된 시스템(예: DI)이 컴파일 타임에 Kotlin 컴파일러가 사용하는 동등한 시스템과 최소한의 차이로 일치하도록 합니다. 또한 코어가 기본적으로 컴파일러의 코어와 동일하고 매우 철저하게 테스트되기 때문에 Kotlin 리플렉션의 구현을 보다 쉽고 안정적으로 만듭니다.
<br>
<br>
문제는 Java 필드 및 get/set 메서드가 Kotlin 컴파일러에서 단일 속성으로 간주되지 않는다는 것입니다. 또는 ::를 통해 참조할 수 있으며, 이는 KT-8575에 따라 불가능합니다. (자바 get-method를 foo.getBar() 대신 foo.bar로 호출할 수 있다는 사실은 순전히 구문상의 설탕이며 컴파일러가 사용하는 언어나 선언 구조에 영향을 미치지 않습니다.) 이론적으로 우리는 컴파일러와 함께 여기에서 Java 필드/get-set 메서드의 표현을 분기할 수 있지만 지금 당장은 반대합니다.
<br>
<br>
설명하기 위해 다소 실제 사용 사례를 제공하겠습니다. 이 가상의 새로운 Kotlin 리플렉션(여기서 Java 필드 + get/set-method는 KProperty로 간주됨)을 통해 종속성 주입 프레임워크를 구현했으며 이 프레임워크가 사용되는 프로젝트의 일부 코드는 Java로 구현되었음을 고려하십시오. 그런 다음 Kotlin 컴파일러에서 로드한 기호를 사용하여 작동하는 정적 컴파일 시간 기반 솔루션을 위해 이 프레임워크를 사용하지 않기로 결정합니다.
<br>
<br>
컴파일러 API(아직 공개되지는 않았지만 공개될 예정임)를 사용하여 리플렉션 기반 코드를 코드로 변환하고 리플렉션이 컴파일러와 거의 동일한 종류의 기호에서 작동하기 때문에 프로세스가 상당히 간단합니다. 그러나 그런 다음 코드 생성을 실행하고 컴파일러가 이러한 것을 다르게 인식하기 때문에 Java 클래스의 제공이 중단되었음을 알게 됩니다. 이 예는 약간 인위적이지만 내가 여기에서 표현의 동등성을 주장하는 이유를 설명하기를 바랍니다.
<br>
<br>
내 생각에 이 문제를 해결하는 가장 좋은 방법은 Java 필드와 get/set 메서드가 언어와 컴파일러에서 표시되는 방식을 다시 디자인하는 것입니다. 컴파일러가 public getter가 있는 private Java 필드가 적절한 Kotlin 속성이라고 믿게 만들어 KT-6653, KT-8575, KT-15620 등을 수정할 수 있다면 리플렉션을 통해 요청한 대로 이러한 속성을 관찰할 수 있습니다. 또한. 그러나 해당 변경 사항이 언어에서 구현되면 Kotlin 리플렉션에서 자동으로 작동합니다.
<br>
<br>
따라서 리플렉션보다 언어 설계 및 컴파일러에 대한 요청에 가깝습니다. 특히, KT-6653은 Java 코드에서 속성을 로드하는 것과 관련된 주요 문제이므로 투표하고 시청하는 것이 좋습니다. 다소 긴 글 죄송합니다. 나는 당신의 혼란을 이해하지만 우리가 전체 언어가 아니라 반영에서만 이 문제를 해결해야 한다고 생각하지 않습니다. 물론 이 결정이 완전히 최종적인 것은 아니며 다른 강력한 사용 사례를 찾은 경우 컴파일러와 구조를 1:1로 유지하는 것이 올바른 일이라고 재고할 수 있습니다.
</blockquote>

<p>
참고자료
</p>
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
