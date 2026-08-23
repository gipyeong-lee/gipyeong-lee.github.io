---
layout: post
title: "Kotlinでreflectを使用する際の課題"
description: "Class kotlin.reflect.jvm.internal.calls.CallerImpl $ FieldGetter can not access a member of class という問題に直面しました。なぜか調査したところ、以下の参考資料に記載された内容で理解できました..."
date: 2022-10-06 08:21:13 +0900
section: blog
category: engineering
lang: ja
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
次のような問題に直面しました。
</p>

<p>
なぜだろうと思い調査したところ、
</p>
<p>
以下の参考資料で明示されている内容を読み、納得がいきました。
</p>
<p>
参考資料内にある回答を翻訳しました。
</p>
<blockquote>
ご指摘の点は理解でき、そのほとんどに同意します。しかし、Kotlinのリフレクションは少し異なるモデルで動作します。コンパイル時にコンパイラから見えるものと可能な限り近いプログラム構造を表現することを目的としています。これが目指すべき正しい目標であるかという点については議論の余地があるかもしれませんが、このアプローチには特定の利点があります。例えば、実行時用に設計されたシステム（例：DI）が、コンパイル時にKotlinコンパイラが使用する同等のシステムと最小限の差異で一致するようにします。また、Kotlinリフレクションのコアは基本的にコンパイラのコアと同一であり、非常に徹底的にテストされているため、実装をより簡単かつ安定したものにできます。
<br>
<br>
問題は、Javaのフィールドやget/setメソッドが、Kotlinコンパイラにおいて単一のプロパティとしてみなされないことです。また、::を通じて参照することもできません。これはKT-8575に従って不可能です。（Javaのgetメソッドをfoo.getBar()の代わりにfoo.barのように呼び出せるという事実は純粋なシンタックスシュガーであり、言語やコンパイラが使用する宣言構造には影響しません。）理論的には、コンパイラとは別にJavaのフィールドやget-setメソッドの表現を分岐させることも可能ですが、現時点では反対です。
<br>
<br>
説明のために、多少実践的なユースケースを挙げます。この仮想的な新しいKotlinリフレクション（ここではJavaのフィールドとget/setメソッドがKPropertyとみなされる）を使用して依存関係注入フレームワークを実装したとします。そして、このフレームワークが使用されるプロジェクトの一部コードがJavaで実装されていると仮定してください。その後、Kotlinコンパイラで読み込んだシンボルを使用して動作する、静的なコンパイル時ベースのソリューションのために、このフレームワークを使用しないことにします。
<br>
<br>
コンパイラAPI（まだ公開されていませんが、今後公開予定です）を使用してリフレクションベースのコードをコードに変換しますが、リフレクションがコンパイラとほぼ同じ種類のシンボルで動作するため、そのプロセスはかなり単純です。しかし、その後コード生成を実行すると、コンパイラがそれらを異なって認識するため、Javaクラスの提供が機能しなくなったことに気づきます。この例は少し作り話ですが、私がここで表現の同等性を主張する理由を説明できれば幸いです。
<br>
<br>
私の考えでは、この問題を解決する最良の方法は、Javaのフィールドとget/setメソッドが言語やコンパイラで表現される方法を再設計することです。もしコンパイラが「public getterを持つprivateなJavaフィールドは適切なKotlinプロパティである」と判断するようにすれば、KT-6653、KT-8575、KT-15620などを修正でき、リフレクションを通じても要求通りにそれらのプロパティを観測できるようになります。また、その変更が言語側で実装されれば、Kotlinリフレクションでも自動的に機能します。
<br>
<br>
したがって、これはリフレクションというよりは言語設計やコンパイラに対する要望に近いものです。特にKT-6653は、Javaコードからプロパティを読み込む際に関係する主要な問題なので、投票やウォッチをすることをおすすめします。長文になり申し訳ありません。ご混乱は理解できますが、言語全体ではなくリフレクションのみでこの問題を解決すべきだとは考えていません。もちろん、この決定が完全に最終的なものではなく、他に強力なユースケースが見つかれば、コンパイラとの構造を1:1で維持することが正しいことなのか再考するかもしれません。
</blockquote>

<p>
## 参考資料
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
Kotlinリフレクションを通じてJavaプロパティ値にアクセスできるようにしてください : KT-27928
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
KotlinプロパティがJavaスタイルのgetter/setterをオーバーライドしない : KT-6653
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
Java合成プロパティの参照をサポート : KT-8575
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
Javaのgetter/setterによる 'expect' メンバープロパティの実装 : KT-15620
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