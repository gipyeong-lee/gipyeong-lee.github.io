---
layout: post
title: "Spring WebFlux - (1) Mono 與 Flux"
description: "Spring 說明了創建 WebFlux 的原因如下。由於這是主觀解釋，建議直接閱讀原文。若有翻譯錯誤或需要補充的內容，請留言告知。(_ _) Why was Spring WebFlux created? 為什麼會出現 Spring Web..."
date: 2020-02-11 12:37:01 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2020-02-11-legacy-226-engineering-spring-webflux-1-mono-flux
tags:
  - "Server"
  - "engineering"
translation_source_hash: 33b3629e8d8ffc461c3ad27335eb2211c7ad6cff76fed609fd83321dbb876295
---

<p>
Spring 說明了創建 WebFlux 的原因如下。
</p>
<p>
由於這是主觀解釋，建議直接閱讀原文。
</p>
<p>
若有翻譯錯誤或需要補充的內容，請留言告知。(_ _)
</p>

<blockquote>
Why was Spring WebFlux created?
<br>
<b>
為什麼會出現 Spring WebFlux？
</b>
<br>
<br>
Part of the answer is the need for a non-blocking web stack to handle concurrency with a small number of threads and scale with fewer hardware resources. Servlet 3.1 did provide an API for non-blocking I/O. However, using it leads away from the rest of the Servlet API, where contracts are synchronous (Filter, Servlet) or blocking (getParameter, getPart). This was the motivation for a new common API to serve as a foundation across any non-blocking runtime. That is important because of servers (such as Netty) that are well-established in the async, non-blocking space.
<br>
<b>
首先，為了以少量執行緒（threads）處理併發性，並以更少的硬體資源進行擴展，我們需要一個非阻塞（non-blocking）的 Web 堆疊。雖然 Servlet 3.1 確實提供了用於非阻塞 I/O 的 API，但使用它會讓我們遠離其餘的 Servlet API，因為它們的合約（contracts）大多是同步的（如 Filter、Servlet）或阻塞的（如 getParameter、getPart）。這正是推動開發一套能在任何非阻塞執行環境下作為基礎的全新通用 API 的動機。這一點非常重要，因為它影響了在非同步、非阻塞領域中已成熟運作的伺服器（例如 Netty）。
</b>
<br>
<br>
The other part of the answer is functional programming. Much as the addition of annotations in Java 5 created opportunities (such as annotated REST controllers or unit tests), the addition of lambda expressions in Java 8 created opportunities for functional APIs in Java. This is a boon for non-blocking applications and continuation-style APIs (as popularized by CompletableFuture and ReactiveX) that allow declarative composition of asynchronous logic. At the programming-model level, Java 8 enabled Spring WebFlux to offer functional web endpoints alongside annotated controllers.
<br>
<b>
另一個原因則是函數式程式設計（functional programming）。正如 Java 5 中引入註解（annotations）創造了許多機會（例如帶註解的 REST 控制器或單元測試），Java 8 中引入 Lambda 表達式也為 Java 中的函數式 API 創造了機會。這對於非阻塞應用程式以及非同步邏輯的宣告式組合（declarative composition）來說是一大福音（如 CompletableFuture 和 ReactiveX 所推廣的延續風格 API）。在程式設計模型層面上，Java 8 讓 Spring WebFlux 能夠在提供帶註解控制器的同時，也提供函數式的 Web 端點。
</b>
</blockquote>
<p>
此外，為了讓大家更好地理解 Reactive 的概念，我在下方進行了整理。
</p>
<p>
Spring 中對 Reactive 的定義如下。
</p>

<blockquote>
We touched on “non-blocking” and “functional” but what does reactive mean?
<br>
<b>
我們已經討論了「非阻塞」和「函數式」，那麼 Reactive 是什麼意思呢？
</b>
<br>
<br>
The term, “reactive,” refers to programming models that are built around reacting to change — network components reacting to I/O events, UI controllers reacting to mouse events, and others. In that sense, non-blocking is reactive, because, instead of being blocked, we are now in the mode of reacting to notifications as operations complete or data becomes available.
<br>
<b>
「Reactive（響應式）」一詞是指圍繞著「對變化作出反應」所構建的程式設計模型——例如網路組件對 I/O 事件作出反應、UI 控制器對滑鼠事件作出反應等。從這個意義上說，非阻塞就是一種響應式，因為我們現在不再處於被阻塞的狀態，而是進入了當操作完成或數據可用時，根據通知作出反應的模式。
</b>
<br>
<br>
There is also another important mechanism that we on the Spring team associate with “reactive” and that is non-blocking back pressure. In synchronous, imperative code, blocking calls serve as a natural form of back pressure that forces the caller to wait. In non-blocking code, it becomes important to control the rate of events so that a fast producer does not overwhelm its destination.
<br>
<b>
Spring 團隊還將另一個重要的機制與「響應式」聯繫起來，那就是非阻塞背壓（non-blocking back pressure）。在同步的指令式程式碼中，阻塞式呼叫作為一種自然的背壓形式，強制呼叫者等待。而在非阻塞程式碼中，控制事件的速度變得非常重要，這樣快速的生產者（producer）才不會讓目的地（consumer）不堪負荷。
</b>
<br>
<br>
<br>
Reactive Streams is a small spec (also adopted in Java 9) that defines the interaction between asynchronous components with back pressure. For example a data repository (acting as Publisher) can produce data that an HTTP server (acting as Subscriber) can then write to the response. The main purpose of Reactive Streams is to let the subscriber to control how quickly or how slowly the publisher produces data.
<br>
<b>
Reactive Streams 是一項小型規範（也被 Java 9 採用），定義了具有背壓功能的非同步組件之間的互動。例如，數據儲存庫（作為 Publisher）可以產生數據，隨後由 HTTP 伺服器（作為 Subscriber）寫入回應中。Reactive Streams 的主要目的是讓訂閱者（subscriber）能夠控制發佈者（publisher）產生數據的快慢。
</b>
</blockquote>
<p>
我想整理一下在使用過程中學習的 API。
</p>
<p>
在 WebFlux 開發過程中，我們經常會使用 Mono 和 Flux 對象，並使用 flatmap、zipWith 等 API，我將在這裡一一整理。
</p>
<p>
本文件中使用的所有資料來源如下：
<a href="projectreactor.io" target="_blank" rel="noopener">
projectreactor.io
</a>
</p>
<figure class="og-loading">
載入中...
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
這是 Mono 的時間軸，時間從左向右流動。
<br>
<br>
</b>
<span>
This is the optional item emitted by the Mono
<br>
</span>
<b>
<span>
這是 Mono 發出的選填項目。
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
這條垂直線表示 Mono 已成功完成。
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
這些虛線和這個方框表示正在對 Mono 應用轉換（transformation）。
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
這個 Mono 是轉換後的結果。
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
如果由於某種原因 Mono 異常終止並出現錯誤，垂直線將被 X 取代。
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