---
layout: post
title: "Spring WebFlux - (1) MonoとFlux"
description: "SpringがWebFluxを作成した理由は、以下の通りだと説明されています。あくまで主観的な解釈ですので、原文を直接解釈されることをお勧めします。誤訳や追加すべき内容があれば、コメントをお願いします。 (_ _) Why was Spring WebFlux created? なぜSpring WebFluxができたのか..."
date: 2020-02-11 12:37:01 +0900
section: blog
category: engineering
lang: ja
ref: 2020-02-11-legacy-226-engineering-spring-webflux-1-mono-flux
tags:
  - "Server"
  - "engineering"
translation_source_hash: 33b3629e8d8ffc461c3ad27335eb2211c7ad6cff76fed609fd83321dbb876295
---

<p>
SpringがWebFluxを作成した理由は、以下の通りだと説明されています。
</p>
<p>
あくまで主観的な解釈ですので、原文を直接解釈されることをお勧めします。
</p>
<p>
誤訳や追加すべき内容があれば、コメントをお願いします。 (_ _)
</p>

<blockquote>
Why was Spring WebFlux created?
<br>
<b>
なぜSpring WebFluxができたのか？
</b>
<br>
<br>
Part of the answer is the need for a non-blocking web stack to handle concurrency with a small number of threads and scale with fewer hardware resources. Servlet 3.1 did provide an API for non-blocking I/O. However, using it leads away from the rest of the Servlet API, where contracts are synchronous (Filter, Servlet) or blocking (getParameter, getPart). This was the motivation for a new common API to serve as a foundation across any non-blocking runtime. That is important because of servers (such as Netty) that are well-established in the async, non-blocking space.
<br>
<b>
まず、少数のスレッドで並行性を処理し、より少ないハードウェアリソースでスケールするためのノンブロッキングWebスタックが必要でした。Servlet 3.1はノンブロッキングI/O用のAPIを提供しましたが、それを使用すると、コントラクトが同期（Filter、Servlet）またはブロッキング（getParameter、getPart）である残りのServlet APIから離れてしまいます。これが、あらゆるノンブロッキングランタイムの基盤となる新しい共通APIを求める動機となりました。この点は、非同期・ノンブロッキングの分野で十分に確立されたサーバー（例：Netty）に影響を与えるため重要です。
</b>
<br>
<br>
The other part of the answer is functional programming. Much as the addition of annotations in Java 5 created opportunities (such as annotated REST controllers or unit tests), the addition of lambda expressions in Java 8 created opportunities for functional APIs in Java. This is a boon for non-blocking applications and continuation-style APIs (as popularized by CompletableFuture and ReactiveX) that allow declarative composition of asynchronous logic. At the programming-model level, Java 8 enabled Spring WebFlux to offer functional web endpoints alongside annotated controllers.
<br>
<b>
もう一つの理由は関数型プログラミングです。Java 5でのアノテーションの追加が（アノテーション付きのRESTコントローラーやユニットテストのような）機会を生み出したのと同様に、Java 8でのラムダ式の追加は、Javaにおける関数型APIの機会を生み出しました。これは、非同期ロジックの宣言的な構成を可能にするノンブロッキングアプリケーションや継続スタイルAPI（CompletableFutureやReactiveXによって普及）にとって恩恵となります。プログラミングモデルのレベルでは、Java 8により、Spring WebFluxはアノテーション付きのコントローラーと並んで関数型のWebエンドポイントを提供できるようになりました。
</b>
</blockquote>
<p>
さらに、Reactiveの概念を知っておくと良いと思いますので、以下にまとめます。
</p>
<p>
SpringにおけるReactiveの定義は以下の通りです。
</p>

<blockquote>
We touched on “non-blocking” and “functional” but what does reactive mean?
<br>
<b>
「ノンブロッキング」と「関数型」については触れましたが、Reactive（リアクティブ）とは何を意味するのでしょうか？
</b>
<br>
<br>
The term, “reactive,” refers to programming models that are built around reacting to change — network components reacting to I/O events, UI controllers reacting to mouse events, and others. In that sense, non-blocking is reactive, because, instead of being blocked, we are now in the mode of reacting to notifications as operations complete or data becomes available.
<br>
<b>
「リアクティブ」という用語は、変化に反応するように構築されたプログラミングモデルを指します。たとえば、I/Oイベントに反応するネットワークコンポーネントや、マウスイベントに反応するUIコントローラーなどです。その意味で、ノンブロッキングはリアクティブです。なぜなら、ブロックされる代わりに、操作が完了したりデータが利用可能になったりした際の通知に反応するモードになっているからです。
</b>
<br>
<br>
There is also another important mechanism that we on the Spring team associate with “reactive” and that is non-blocking back pressure. In synchronous, imperative code, blocking calls serve as a natural form of back pressure that forces the caller to wait. In non-blocking code, it becomes important to control the rate of events so that a fast producer does not overwhelm its destination.
<br>
<b>
Springチームが「リアクティブ」と関連付けているもう一つの重要なメカニズムは、ノンブロッキングの背圧（Back Pressure）です。同期的な命令型コードでは、ブロック呼び出しが発信者を待機させる自然な形の背圧として機能します。ノンブロッキングコードでは、高速なプロデューサーが宛先を圧倒しないように、イベントの発生率を制御することが重要になります。
</b>
<br>
<br>
<br>
Reactive Streams is a small spec (also adopted in Java 9) that defines the interaction between asynchronous components with back pressure. For example a data repository (acting as Publisher) can produce data that an HTTP server (acting as Subscriber) can then write to the response. The main purpose of Reactive Streams is to let the subscriber to control how quickly or how slowly the publisher produces data.
<br>
<b>
Reactive Streamsは（Java 9でも採用されている）小さな仕様で、背圧を伴う非同期コンポーネント間の相互作用を定義するものです。たとえば、データリポジトリ（Publisherとして機能）は、HTTPサーバー（Subscriberとして機能）がレスポンスに書き込めるデータを生成できます。Reactive Streamsの主な目的は、SubscriberがPublisherのデータ生成速度を制御できるようにすることです。
</b>
</blockquote>
<p>
使用しながら学ぶAPIを整理したいと考えました。
</p>
<p>
この記事では、WebFluxを使用する際にMonoやFluxオブジェクトを使ってflatmapやzipWithといったAPIを使用することになるため、それらを一つずつ整理していきます。
</p>
<p>
本記事で使用するすべての資料の出典はこちらです：
<a href="projectreactor.io" target="_blank" rel="noopener">
projectreactor.io
</a>
</p>
<figure class="og-loading">
読み込み中です...
</figure>
<hr>
<h4>
Mono
</h4>
<p>
public abstract class
<span>
Mono&lt;T&gt;
</span>
extends
<a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true">
Object
</a>
implements
<a href="https://projectreactor.io/docs/core/release/api/reactor/core/CorePublisher.html">
CorePublisher
</a>
&lt;T&gt;
</p>


<blockquote>
This is the timeline of the Mono Time flows from left to right
<br>
<b>
これはMonoのタイムラインで、時間が左から右へ流れます
<br>
<br>
</b>
<span>
This is the optional item emitted by the Mono
<br>
</span>
<b>
<span>
これはMonoから放出されるオプションのアイテムです
<br>
<span>
<br>
</span>
</span>
</b>
<span>
<span>
This vertical line indicates that the mono has completed successfully
</span>
</span>
<b>
<span>
<span>
<br>
この垂直線は、Monoが正常に完了したことを示します
<br>
<br>
</span>
</span>
</b>
<span>
<span>
<span>
These dotted lines and this box indicate that a transformation is being applied to the mono
</span>
</span>
</span>
<b>
<span>
<span>
<span>
<br>
これらの点線とボックスは、Monoに対して変換が適用されていることを示します
<br>
<br>
</span>
</span>
</span>
</b>
<span>
<span>
<span>
<span>
This Mono is the result of the transformation
</span>
</span>
</span>
</span>
<b>
<span>
<span>
<span>
<span>
<br>
このMonoは変換の結果です
<br>
<br>
</span>
</span>
</span>
</span>
</b>
<span>
<span>
<span>
<span>
<span>
If for some reason the Mono terminates abnormally, with an error, the vertical line is replaced by an X
<br>
</span>
</span>
</span>
</span>
</span>
<b>
<span>
<span>
<span>
<span>
<span>
何らかの理由でMonoが異常終了し、エラーが発生した場合、垂直線はXに置き換わります
</span>
</span>
</span>
</span>
<br>
</span>
</b>
</blockquote>

<h4>
Flux
</h4>
<p>
public abstract class
<span>
Flux&lt;T&gt;
</span>
extends
<a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true">
Object
</a>
implements
<a href="https://projectreactor.io/docs/core/release/api/reactor/core/CorePublisher.html">
CorePublisher
</a>
&lt;T&gt;
</p>