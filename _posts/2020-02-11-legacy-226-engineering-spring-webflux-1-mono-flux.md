---
layout: post
title: "Spring WebFlux - (1) Mono와 Flux"
description: "Spring 에서 WebFlux 를 생성한 이유를 다음과 같다고 얘기합니다. 주관적인 해석이므로, 원문을 직접 해석하시길 추천드립니다. 잘못 해석된부분이나, 추가할 내용이 있다면 댓글 부탁드립니다. (_ _) Why was Spring WebFlux created? 왜 스프링 웹플..."
date: 2020-02-11 12:37:01 +0900
section: blog
category: engineering
lang: ko
ref: 2020-02-11-legacy-226-engineering-spring-webflux-1-mono-flux
tags:
  - "Server"
  - "engineering"
---

<p>
Spring 에서 WebFlux 를 생성한 이유를 다음과 같다고 얘기합니다.
</p>
<p>
주관적인 해석이므로, 원문을 직접 해석하시길 추천드립니다.
</p>
<p>
잘못 해석된부분이나, 추가할 내용이 있다면 댓글 부탁드립니다. (_ _)
</p>

<blockquote>
Why was Spring WebFlux created?
<br>
<b>
왜 스프링 웹플럭스가 생겼나?
</b>
<br>
<br>
Part of the answer is the need for a non-blocking web stack to handle concurrency with a small number of threads and scale with fewer hardware resources. Servlet 3.1 did provide an API for non-blocking I/O. However, using it leads away from the rest of the Servlet API, where contracts are synchronous (Filter, Servlet) or blocking (getParameter, getPart). This was the motivation for a new common API to serve as a foundation across any non-blocking runtime. That is important because of servers (such as Netty) that are well-established in the async, non-blocking space.
<br>
<b>
먼저 적은 수의 스레드로 동시성을 처리하고 더 적은 하드웨어 리소스로 확장하기 위해 non-blocking 웹 스택이 필요했습니다. 그러나 이를 사용하면 동기식 메커니즘인 Filter, Servlet 과 getParameter,getPart 와 같은 blocking API 등으로 인해 Servlet API 에서 멀어지게되는데 이는 새로운 공통 API가 모든 non-blocking 런타임에서 기초 역할을 하도록 하는 계기가 되었습니다. 이 부분은 중요한데 async, non-blocking 공간에서 잘 확립된 서버(ex.Netty)에 영향을 주기 때문입니다.
</b>
<br>
<br>
The other part of the answer is functional programming. Much as the addition of annotations in Java 5 created opportunities (such as annotated REST controllers or unit tests), the addition of lambda expressions in Java 8 created opportunities for functional APIs in Java. This is a boon for non-blocking applications and continuation-style APIs (as popularized by CompletableFuture and ReactiveX) that allow declarative composition of asynchronous logic. At the programming-model level, Java 8 enabled Spring WebFlux to offer functional web endpoints alongside annotated controllers.
<br>
<b>
또 다른 하나는 기능적 프로그래밍입니다.  Webflux는 async 로직을 선언적으로 구성할 수 있는 non-blocking 앱 및 연속 스타일 API ( CompletableFuture,ReactiveX 에서 유명해진) 에 도움이됩니다. 프로그래밍 모델 수준에서 Java 8 을 통해 Spring WebFlux 는 주석이 달린 컨트롤러와 함께 기능적인 웹 앤드포인트를 제공할 수 있었습니다.
</b>
</blockquote>
<p>
더불어 Reactive 에 대한 개념을 알면 좋을 것 같아서 아래 정리해봅니다.
</p>
<p>
Spring 에서의 Reactive 의 정의는 다음과 같습니다.
</p>

<blockquote>
We touched on “non-blocking” and “functional” but what does reactive mean?
<br>
<b>
우리는 non-blocking 과 functional 에 대해 언급하였지만, reactive 는 어떤 의미일까?
</b>
<br>
<br>
The term, “reactive,” refers to programming models that are built around reacting to change — network components reacting to I/O events, UI controllers reacting to mouse events, and others. In that sense, non-blocking is reactive, because, instead of being blocked, we are now in the mode of reacting to notifications as operations complete or data becomes available.
<br>
<b>
우선 "반응성" 라는 용어는 I/O 이벤트에 반응하는 네트워크 구성 요소, 마우스 이벤트 등에 반응하는 UI 컨트롤러 등의 변화에 대응하여 구축된 프로그래밍 모델을 말합니다. 이러한 의미에서, 비 차단은 반응 적입니다. 왜냐하면 우리는 이제 막히지 않고, 작업이 완료되거나 데이터를 사용할 수 있게 되면서 알림이 오면 반응하는 상황에 있습니다.
</b>
<br>
<br>
There is also another important mechanism that we on the Spring team associate with “reactive” and that is non-blocking back pressure. In synchronous, imperative code, blocking calls serve as a natural form of back pressure that forces the caller to wait. In non-blocking code, it becomes important to control the rate of events so that a fast producer does not overwhelm its destination.
<br>
<b>
스프링팀의 또 다른 중요메커니즘은 "반응성"과 관련이 있으며 non-blocking 역압입니다. 동기식, 명령형 코드에서 차단 호출은 발신자가 대기하게하는 자연적인 배압의 역할을합니다. 비 차단 코드에서는 producer 가 consumer 를 압도하지 않도록 이벤트 속도를 제어하는 것이 중요합니다.
</b>
<br>
<br>
<br>
Reactive Streams is a small spec (also adopted in Java 9) that defines the interaction between asynchronous components with back pressure. For example a data repository (acting as Publisher) can produce data that an HTTP server (acting as Subscriber) can then write to the response. The main purpose of Reactive Streams is to let the subscriber to control how quickly or how slowly the publisher produces data.
<br>
<b>
리액티브 스트림은 역압을 갖는 비동기 구성 요소 간의 상호 작용을 정희하는 사양입니다. 예를 들어, 데이터 저장소 ( 게시자 역할 ) 는 HTTP 서버( 가입자) 가 응답에 쓸 수 있는 데이터를 생성할 수 있습니다. ReactiveStreams 의 주요 목적은 구독자가 게시자의 데이터를 얼마나 빨리 또는 느리게 생성하는지 제어 할 수 있도록 하는 것입니다.
</b>
</blockquote>
<p>
사용하면서 공부하는 api 를 정리하고 싶었습니다.
</p>
<p>
이 글에서는 WebFlux 를 하다보면, Mono, Flux 객체를 사용하여 flatmap, zipWith 등등 api 를 사용하게 되는데 이를 하나씩 정리합니다.
</p>
<p>
본 글에서 사용되는 모든 자료의 출처는 이곳입니다 :
<a href="projectreactor.io" target="_blank" rel="noopener">
projectreactor.io
</a>
</p>
<figure class="og-loading">
불러오는 중입니다...
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
이것은 모노 타임이 왼쪽에서 오른쪽으로 흐르는 타임 라인입니다
<br>
<br>
</b>
<span>
This is the optional item emitted by the Mono
<br>
</span>
<b>
<span>
모노에서 방출되는 옵션 품목입니다
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
이 세로선은 모노가 성공적으로 완료되었음을 나타냅니다.
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
점선과 상자는 변형이 모노에 적용되고 있음을 나타냅니다
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
이 모노는 변형의 결과입니다
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
어떤 이유로 Mono가 비정상적으로 종료되고 오류가 발생하면 수직선이 X로 바뀝니다.
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
