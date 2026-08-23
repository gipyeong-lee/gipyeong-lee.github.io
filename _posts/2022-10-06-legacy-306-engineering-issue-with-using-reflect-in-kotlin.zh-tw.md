---
layout: post
title: "在 Kotlin 中使用 reflect 的問題"
description: "Class kotlin.reflect.jvm.internal.calls.CallerImpl $ FieldGetter can not access a member of class 面臨了這樣的問題。我進行了研究，閱讀了下方參考資料中的文章後理解了原因..."
date: 2022-10-06 08:21:13 +0900
section: blog
category: engineering
lang: zh-tw
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
面臨了這樣的問題。
</p>

<p>
為什麼呢？我進行了研究。
</p>
<p>
閱讀了下方參考資料中提及的文章後，便理解了。
</p>
<p>
我將下方文章的回答翻譯如下。
</p>
<blockquote>
我理解您的觀點，且大多同意。但 Kotlin 反射（Reflection）運作在略有不同的模型上。它呈現的程式結構與編譯器在編譯時所見的結構盡可能相似。雖然有人會質疑這是否是正確的目標，但這種方法確實有其優勢。例如，它能確保為執行時期設計的系統（如 DI）與 Kotlin 編譯器在編譯時期使用的等效系統保持最小的差異。此外，由於核心本質上與編譯器的核心相同且經過極其徹底的測試，這使得 Kotlin 反射的實現更容易且更穩定。
<br>
<br>
問題在於，Java 欄位（field）及 get/set 方法在 Kotlin 編譯器中並不被視為單一屬性。或者無法透過 :: 來參考，根據 KT-8575 這是不可能的。（事實上，可以透過 foo.bar 而非 foo.getBar() 來呼叫 Java get-method，這純粹是語法糖，並不影響編譯器使用的語言或宣告結構。）理論上，我們可以從編譯器分支出 Java 欄位/get-set 方法的表示方式，但目前我們反對這樣做。
<br>
<br>
為了說明，我舉一個實際的使用案例。假設您透過這個虛構的新 Kotlin 反射（其中 Java 欄位 + get/set-method 被視為 KProperty）實現了一個依賴注入框架，並且該框架所使用的專案中，部分程式碼是以 Java 實現的。然後，您決定不使用該框架，轉而採用基於編譯器載入符號（symbol）的靜態編譯時間解決方案。
<br>
<br>
您可以使用編譯器 API（雖然尚未公開，但未來將會公開）將基於反射的程式碼轉換為程式碼，因為反射作用於與編譯器幾乎相同的符號，過程相當簡單。然而，當您執行程式碼生成時，會發現 Java 類別的提供中斷了，因為編譯器對這些內容的識別方式不同。這個例子可能有點牽強，但我希望它能解釋我為何主張表示法的等效性。
<br>
<br>
在我看來，解決此問題的最佳方法是重新設計 Java 欄位和 get/set 方法在語言和編譯器中的顯示方式。如果能讓編譯器認為擁有 public getter 的 private Java 欄位是適當的 Kotlin 屬性，那麼我們就可以修正 KT-6653、KT-8575、KT-15620 等問題，並且也可以透過反射來觀察這些屬性。此外，一旦該變更在語言中實現，Kotlin 反射也會自動支援。
<br>
<br>
因此，比起針對反射，這更像是對語言設計和編譯器的請求。特別是 KT-6653 是涉及從 Java 程式碼載入屬性的主要問題，因此建議進行投票並關注。抱歉文章有點長。我理解您的困惑，但不認為我們應該只在反射中解決這個問題，而不是在整個語言層面上。當然，這個決定並非絕對，如果發現其他強大的使用案例，我們會重新考慮是否將結構與編譯器保持 1:1 是正確的做法。
</blockquote>

## 參考資料

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