---
layout: post
title: "Webflux 中 exchange 和 retrieve 的区别"
description: "在什么情况下使用？我在 Spring Boot 2.x.x 版本中使用 Webflux。在代码中使用 WebClient 时，我通常会在请求后使用 exchange()，因为我使用的 API 在失败时会返回 200 HTTP 状态码和错误主体。"
date: 2021-03-25 08:00:24 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2021-03-25-legacy-256-engineering-webflux-exchange-retrieve
tags:
  - "Exchange"
  - "memory"
  - "webflux"
  - "retrieve"
  - "Server"
  - "engineering"
translation_source_hash: 803a5b3534f43b95543032e29a1526b0004d0d1e0adfd3d035d4d845230dcb65
---

<h2>
在什么情况下使用？
</h2>
<p>
我使用的是 Spring Boot 2.x.x 版本的 Webflux。
</p>
<p>
在代码中使用 Webclient 时，我通常会在请求后使用 <code>exchange()</code>。原因是我所使用的 API 在失败时也会返回 <code>200 HTTP Status</code> 以及错误内容。
</p>
<p>
当时我犯了一个大错，以为 <code>exchange()</code> 和 <code>retrieve()</code> 是一样的。
</p>
<p>
如果你也这么想，那就错了。它们是不同的。那么 <code>exchange</code> 和 <code>retrieve</code> 到底有什么区别呢？
</p>
<h3>
响应处理不同
</h3>
<p>
根据 <a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">官方文档</a>：
</p>
<ul>
<li>
<p>
WebClient.ResponseSpec <code>retrieve()</code>
</p>
<ul>
<li>
当响应状态为 <strong>200 OK</strong> 时返回响应主体。
</li>
<li>
默认情况下，4xx 和 5xx 响应会导致 WebClientResponseException 异常。要自定义错误处理，请使用 onStatus 处理程序。
</li>
</ul>
</li>
<li>
<p>
reactor.core.publisher.Mono&lt;ClientResponse&gt; <code>exchange()</code>
</p>
<ul>
<li>
自 Spring 5.3 起，因其可能导致内存泄漏和/或连接泄漏而被标记为废弃。
</li>
<li>
使用 <code>exchange()</code> 时，应用程序有责任消费任何响应内容（无论场景是成功、错误、意外数据等）。不这样做会导致内存泄漏。
</li>
<li>
请改用 <code>exchangeToMono(Function)</code> 或 <code>exchangeToFlux(Function)</code>。
</li>
</ul>
</li>
<li>
<p>
exchangeToMono, exchangeToFlux
</p>
<ul>
<li>
自 Spring >= 5.3 起可用。
</li>
<li>
自 Spring Boot 版本 >= 2.4.x 起可用。
</li>
</ul>
</li>
</ul>
<h3>
何时会发生内存泄漏
</h3>
<p>
当你未在代码中使用 <code>ClientResponse.bodyToMono</code> 或 <code>bodyToFlux</code> 时。
</p>
<pre>
<code class="language-kotlin">
.exchange()
.flatMap { clientResponse -&gt;
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // 请求成功
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // HTTP 请求失败。此处发生了内存泄漏。
        throw Exception()
    }
}
</code>
</pre>
<p>
在失败的情况下，你会面临内存泄漏，因为你没有消费响应主体。
</p>
<p>
如果不消费响应主体，连接就不会断开。
</p>
<p>
现在，会发生什么呢……你的 HTTP 连接池会被已使用的线程填满。当没有可用线程时，你的后续请求将会失败。
</p>
<h2>
如何解决？
</h2>
<p>
如果你使用的是 Spring Boot 2.4.x 以上版本，请按如下方式使用 <code>exchangeToMono</code>：
</p>
<pre>
<code class="language-kotlin">
.exchangeToMono(response -&gt; {
    if (response.statusCode().equals(HttpStatus.OK)) {
        return response.bodyToMono(Person.class);
    }
    else if (response.statusCode().is4xxClientError()) {
        return response.bodyToMono(ErrorContainer.class);
    }
    else {
        return Mono.error(response.createException());
    }
});
</code>
</pre>
<p>
如果你的 Spring Boot 版本低于 2.4.x，请使用 <code>retrieve()</code>，或者在抛出异常前手动消费响应主体。
</p>
<p>
示例如下：
</p>
<pre>
<code class="language-kotlin">
clientResponse.bodyToMono&lt;String&gt;().defaultIfEmpty("").map {
    throw Exception()
}
</code>
</pre>
<h2>
结论
</h2>
<p>
我想，在正式使用库之前，我应该养成阅读并正确使用文档的习惯。
<br>
库并不能自动处理一切。
</p>
<blockquote>
<p>
<em>
求知若饥，虚心若愚 (Stay Hunger, Stay Foolish)
</em>
</p>
</blockquote>
<h2>
参考资料
</h2>
<ul>
<li>
<a href="https://docs.spring.io/spring-boot/docs/">
Spring Boot 版本信息
</a>
</li>
<li>
<a href="https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions">
Spring Boot 2.3.x 依赖版本
</a>
</li>
<li>
<a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">
Spring Framework WebClient 文档
</a>
</li>
</ul>