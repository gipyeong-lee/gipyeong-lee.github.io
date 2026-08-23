---
layout: post
title: "Spring WebFlux - (1) Mono and Flux"
description: "Spring explains why they created WebFlux as follows. As this is a subjective interpretation, I recommend interpreting the original text directly. If there are any misinterpretations or additional content, please leave a comment. (_ _) Why was Spring WebFlux created?"
date: 2020-02-11 12:37:01 +0900
section: blog
category: engineering
lang: en
ref: 2020-02-11-legacy-226-engineering-spring-webflux-1-mono-flux
tags:
  - "Server"
  - "engineering"
translation_source_hash: 33b3629e8d8ffc461c3ad27335eb2211c7ad6cff76fed609fd83321dbb876295
---

<p>
Spring explains the reason for creating WebFlux as follows.
</p>
<p>
Since this is a subjective interpretation, I recommend reading the original text yourself.
</p>
<p>
If there are any parts that have been misinterpreted or if you have anything to add, please leave a comment. (_ _)
</p>

<blockquote>
Why was Spring WebFlux created?
<br>
<br>
Part of the answer is the need for a non-blocking web stack to handle concurrency with a small number of threads and scale with fewer hardware resources. Servlet 3.1 did provide an API for non-blocking I/O. However, using it leads away from the rest of the Servlet API, where contracts are synchronous (Filter, Servlet) or blocking (getParameter, getPart). This was the motivation for a new common API to serve as a foundation across any non-blocking runtime. That is important because of servers (such as Netty) that are well-established in the async, non-blocking space.
<br>
<br>
The other part of the answer is functional programming. Much as the addition of annotations in Java 5 created opportunities (such as annotated REST controllers or unit tests), the addition of lambda expressions in Java 8 created opportunities for functional APIs in Java. This is a boon for non-blocking applications and continuation-style APIs (as popularized by CompletableFuture and ReactiveX) that allow declarative composition of asynchronous logic. At the programming-model level, Java 8 enabled Spring WebFlux to offer functional web endpoints alongside annotated controllers.
</blockquote>
<p>
Additionally, I thought it would be good to understand the concept of Reactive, so I have summarized it below.
</p>
<p>
The definition of Reactive in Spring is as follows:
</p>

<blockquote>
We touched on “non-blocking” and “functional” but what does reactive mean?
<br>
<br>
The term, “reactive,” refers to programming models that are built around reacting to change — network components reacting to I/O events, UI controllers reacting to mouse events, and others. In that sense, non-blocking is reactive, because, instead of being blocked, we are now in the mode of reacting to notifications as operations complete or data becomes available.
<br>
<br>
There is also another important mechanism that we on the Spring team associate with “reactive” and that is non-blocking back pressure. In synchronous, imperative code, blocking calls serve as a natural form of back pressure that forces the caller to wait. In non-blocking code, it becomes important to control the rate of events so that a fast producer does not overwhelm its destination.
<br>
<br>
<br>
Reactive Streams is a small spec (also adopted in Java 9) that defines the interaction between asynchronous components with back pressure. For example a data repository (acting as Publisher) can produce data that an HTTP server (acting as Subscriber) can then write to the response. The main purpose of Reactive Streams is to let the subscriber to control how quickly or how slowly the publisher produces data.
</blockquote>
<p>
I wanted to organize the APIs I am studying while using them.
</p>
<p>
In this article, I will explain the APIs such as flatmap, zipWith, etc., that you inevitably use when working with WebFlux, utilizing Mono and Flux objects, one by one.
</p>
<p>
The source of all materials used in this article is here:
<a href="projectreactor.io" target="_blank" rel="noopener">
projectreactor.io
</a>
</p>
<figure class="og-loading">
Loading...
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
<br>
<span>
This is the optional item emitted by the Mono
</span>
<br>
<br>
<span>
This vertical line indicates that the mono has completed successfully
</span>
<br>
<br>
<span>
These dotted lines and this box indicate that a transformation is being applied to the mono
</span>
<br>
<br>
<span>
This Mono is the result of the transformation
</span>
<br>
<br>
<span>
If for some reason the Mono terminates abnormally, with an error, the vertical line is replaced by an X
</span>
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