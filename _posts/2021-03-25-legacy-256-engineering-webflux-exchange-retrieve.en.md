---
layout: post
title: "The difference between Webflux exchange and retrieve"
description: "Under what circumstances? I was using webflux with spring boot version 2.x.x When i was using Webclient in my codes. I was usually using exchange() after req..."
date: 2021-03-25 08:00:24 +0900
section: blog
category: engineering
lang: en
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
Under what circumstances?
</h2>
<p>
I was using WebFlux with Spring Boot version 2.x.x.
</p>
<p>
When I was using WebClient in my code, I usually used
<code>
exchange()
</code>
after the request because of the API I was using; when it failed, it responded with a 
<code>
200 HTTP Status
</code>
along with an error body.
</p>
<p>
At that time, I made a big mistake by thinking that
<code>
exchange()
</code>
and
<code>
retrieve()
</code>
were the same.
</p>
<p>
If you think that, you are wrong. They are different. Then what is the difference between
<code>
exchange
</code>
and
<code>
retrieve
</code>
?
</p>
<h3>
The response is different
</h3>
<p>
According to the <a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">
docs
</a>:
</p>
<ul>
<li>
<p>
WebClient.ResponseSpec
<code>
retrieve()
</code>
</p>
<ul>
<li>
Provides the response body when the response status is 
<strong>
200 OK
</strong>.
</li>
<li>
By default, 4xx and 5xx responses result in a WebClientResponseException. To customize error handling, use onStatus handlers.
</li>
</ul>
</li>
<li>
<p>
reactor.core.publisher.Mono&lt;ClientResponse&gt; 
<code>
exchange()
</code>
</p>
<ul>
<li>
Deprecated since Spring 5.3 due to the possibility of leaking memory and/or connections.
</li>
<li>
When using exchange(), it is the responsibility of the application to consume any response content regardless of the scenario (success, error, unexpected data, etc.). Not doing so can cause a memory leak.
</li>
<li>
Please use exchangeToMono(Function) or exchangeToFlux(Function) instead.
</li>
</ul>
</li>
<li>
<p>
exchangeToMono, exchangeToFlux
</p>
<ul>
<li>
Available since Spring &gt;= 5.3.
</li>
<li>
Available since Spring Boot version &gt;= 2.4.x.
</li>
</ul>
</li>
</ul>
<h3>
When do memory leaks occur?
</h3>
<p>
They occur when you do not use 
<code>
ClientResponse.bodyToMono
</code>
 or 
<code>
bodyToFlux
</code>
 in your code, like this:
</p>
<pre>
<code class="language-kotlin">
.exchange()
.flatMap { clientResponse -&gt;
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // success request.
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // failed http request. in here memory leak occured.
        throw Exception()
    }
}
</code>
</pre>
<p>
In the failure case, you will face a memory leak because you didn't consume the response body.
</p>
<p>
If you don't consume your response body, the connection won't be disconnected.
</p>
<p>
Now, what happens? Your HTTP connection pool will be filled with used threads. When there are no more threads available, your request will fail.
</p>
<h2>
How to solve it?
</h2>
<p>
If you are using a Spring Boot version higher than 2.4.x, use 
<code>
exchangeToMono
</code>
 as shown below:
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
If you are using a version of Spring Boot earlier than 2.4.x, use 
<code>
retrieve()
</code>
 or consume your response body before throwing an exception.
</p>
<p>
For example, see the code below:
</p>
<pre>
<code class="language-kotlin">
clientResponse.bodyToMono&lt;String&gt;().defaultIfEmpty("").map {
    throw Exception()
}
</code>
</pre>
<h2>
Conclusion
</h2>
<p>
I thought I should get into the habit of reading and using the documentation properly before using a library.
<br>
Libraries don't do everything.
</p>
<blockquote>
<p>
<em>
Stay Hungry, Stay Foolish
</em>
</p>
</blockquote>
<h2>
参考资料
</h2>
<ul>
<li>
<a href="https://docs.spring.io/spring-boot/docs/">
Versions of Spring Boot
</a>
</li>
<li>
<a href="https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions">
Spring Boot 2.3.x Dependencies
</a>
</li>
<li>
<a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">
Spring framework webclient docs
</a>
</li>
</ul>