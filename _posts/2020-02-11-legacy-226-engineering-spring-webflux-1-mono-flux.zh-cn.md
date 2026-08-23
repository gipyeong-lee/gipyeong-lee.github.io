---
layout: post
title: "Spring WebFlux - (1) Mono 和 Flux"
description: "Spring 团队说明了创建 WebFlux 的原因。由于这是主观解读，建议阅读原文。如果有翻译错误或需要补充的内容，欢迎在评论区指出。(_ _) Why was Spring WebFlux created? 为什么会出现 Spring WebFlux..."
date: 2020-02-11 12:37:01 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2020-02-11-legacy-226-engineering-spring-webflux-1-mono-flux
tags:
  - "Server"
  - "engineering"
translation_source_hash: 33b3629e8d8ffc461c3ad27335eb2211c7ad6cff76fed609fd83321dbb876295
---

<p>
Spring 团队说明了创建 WebFlux 的原因。
</p>
<p>
由于这是主观解读，建议阅读原文。
</p>
<p>
如果有翻译错误或需要补充的内容，欢迎在评论区指出。(_ _)
</p>

<blockquote>
Why was Spring WebFlux created?
<br>
<b>
为什么会出现 Spring WebFlux？
</b>
<br>
<br>
Part of the answer is the need for a non-blocking web stack to handle concurrency with a small number of threads and scale with fewer hardware resources. Servlet 3.1 did provide an API for non-blocking I/O. However, using it leads away from the rest of the Servlet API, where contracts are synchronous (Filter, Servlet) or blocking (getParameter, getPart). This was the motivation for a new common API to serve as a foundation across any non-blocking runtime. That is important because of servers (such as Netty) that are well-established in the async, non-blocking space.
<br>
<b>
首先，需要一个非阻塞（non-blocking）的 Web 栈，以便用少量的线程处理并发，并以更少的硬件资源进行扩展。虽然 Servlet 3.1 提供了非阻塞 I/O 的 API，但使用它会背离其余的 Servlet API，因为那些 API 的契约是同步的（Filter, Servlet）或阻塞的（getParameter, getPart）。这促使我们需要一个新的通用 API，作为任何非阻塞运行时环境的基础。这一点很重要，因为它会影响在异步、非阻塞领域中已经成熟的服务器（如 Netty）。
</b>
<br>
<br>
The other part of the answer is functional programming. Much as the addition of annotations in Java 5 created opportunities (such as annotated REST controllers or unit tests), the addition of lambda expressions in Java 8 created opportunities for functional APIs in Java. This is a boon for non-blocking applications and continuation-style APIs (as popularized by CompletableFuture and ReactiveX) that allow declarative composition of asynchronous logic. At the programming-model level, Java 8 enabled Spring WebFlux to offer functional web endpoints alongside annotated controllers.
<br>
<b>
另一个原因是函数式编程。正如 Java 5 中添加注解创造了机遇（如注解 REST 控制器或单元测试）一样，Java 8 中 Lambda 表达式的加入也为 Java 中的函数式 API 创造了机会。这对非阻塞应用程序和连续式 API（如 CompletableFuture 和 ReactiveX 所推广的那样）来说是一大福音，它们允许以声明式方式组合异步逻辑。在编程模型层面，Java 8 使 Spring WebFlux 能够提供函数式 Web 端点，并与注解控制器共存。
</b>
</blockquote>
<p>
此外，我认为了解 Reactive 的概念会很有帮助，整理如下。
</p>
<p>
Spring 对 Reactive 的定义如下：
</p>

<blockquote>
We touched on “non-blocking” and “functional” but what does reactive mean?
<br>
<b>
我们提到了“非阻塞”和“函数式”，但“响应式”（reactive）是什么意思呢？
</b>
<br>
<br>
The term, “reactive,” refers to programming models that are built around reacting to change — network components reacting to I/O events, UI controllers reacting to mouse events, and others. In that sense, non-blocking is reactive, because, instead of being blocked, we are now in the mode of reacting to notifications as operations complete or data becomes available.
<br>
<b>
“响应式”一词是指围绕对变化做出反应而构建的编程模型——例如网络组件对 I/O 事件做出反应，UI 控制器对鼠标事件做出反应等。从这个意义上讲，非阻塞就是响应式的，因为我们不再处于阻塞状态，而是处于当操作完成或数据可用时，对通知做出反应的状态。
</b>
<br>
<br>
There is also another important mechanism that we on the Spring team associate with “reactive” and that is non-blocking back pressure. In synchronous, imperative code, blocking calls serve as a natural form of back pressure that forces the caller to wait. In non-blocking code, it becomes important to control the rate of events so that a fast producer does not overwhelm its destination.
<br>
<b>
Spring 团队认为与“响应式”相关的另一个重要机制是非阻塞背压（back pressure）。在同步的命令式代码中，阻塞调用是一种自然的背压形式，强制调用者等待。而在非阻塞代码中，控制事件速率变得非常重要，以防止快速的生产者（producer）压垮其目的地。
</b>
<br>
<br>
<br>
Reactive Streams is a small spec (also adopted in Java 9) that defines the interaction between asynchronous components with back pressure. For example a data repository (acting as Publisher) can produce data that an HTTP server (acting as Subscriber) can then write to the response. The main purpose of Reactive Streams is to let the subscriber to control how quickly or how slowly the publisher produces data.
<br>
<b>
Reactive Streams 是一项小型规范（也被 Java 9 采用），它定义了具有背压功能的异步组件之间的交互。例如，数据存储库（作为 Publisher/发布者）可以生成数据，HTTP 服务器（作为 Subscriber/订阅者）随后将其写入响应。Reactive Streams 的主要目的是让订阅者控制发布者生成数据的快慢。
</b>
</blockquote>
<p>
我想整理一下在使用过程中学习的 API。
</p>
<p>
在 WebFlux 中，我们经常会用到 Mono 和 Flux 对象，并使用 flatmap、zipWith 等 API，我将把它们逐一整理出来。
</p>
<p>
本文中使用的所有资料来源均在此处：
<a href="projectreactor.io" target="_blank" rel="noopener">
projectreactor.io
</a>
</p>
<figure class="og-loading">
正在加载中...
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
这是 Mono 时间从左向右流动的线性时间轴
<br>
<br>
</b>
<span>
This is the optional item emitted by the Mono
<br>
</span>
<b>
<span>
这是 Mono 发出的可选数据项
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
这条垂直线表示 Mono 已成功完成
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
这些虚线和方框表示正在对 Mono 应用转换
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
此 Mono 是转换的结果
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
如果由于某种原因 Mono 异常终止并发生错误，垂直线将被 X 代替
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

## 参考资料