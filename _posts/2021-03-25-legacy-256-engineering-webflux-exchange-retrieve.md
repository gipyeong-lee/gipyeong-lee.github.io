---
layout: post
title: "Webflux exchange 와 retrieve 의 차이"
description: "Under what circumstances? I was using webflux with spring boot version 2.x.x When i was using Webclient in my codes. I was usually using exchange() after req..."
date: 2021-03-25 08:00:24 +0900
section: blog
category: engineering
lang: ko
ref: 2021-03-25-legacy-256-engineering-webflux-exchange-retrieve
tags:
  - "Exchange"
  - "memory"
  - "webflux"
  - "retrieve"
  - "Server"
  - "engineering"
---

<h2>
Under what circumstances?
</h2>
<p>
I was using webflux with spring boot version 2.x.x
</p>
<p>
When i was using Webclient in my codes. I was usually using
<code>
exchange()
</code>
after request. cause, api what i used. when failed. it response
<code>
200 HTTP Status
</code>
with error body.
</p>
<p>
At that time i had a big mistake. that I thought
<code>
exchange()
</code>
and
<code>
retrieve()
</code>
is same.
</p>
<p>
If you think like that. you are wrong. they are different. then what is different
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
Response is Different
</h3>
<p>
According to
<a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">
docs
</a>
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
Response body when response status is
<strong>
200 ok
</strong>
</li>
<li>
By default, 4xx and 5xx responses result in a WebClientResponseException. To customize error handling, use onStatus handlers.
</li>
</ul>
</li>
<li>
<p>
reactor.core.publisher.Mono
<clientresponse>
exchange()
</p>
<ul>
<li>
since Spring 5.3 due to the possibility to leak memory and/or connections
</li>
<li>
when using exchange(), it is the responsibility of the application to consume any response content regardless of the scenario (success, error, unexpected data, etc). Not doing so can cause a memory leak.
</li>
<li>
please, use exchangeToMono(Function), exchangeToFlux(Function)
</li>
</ul>
</li>
<li>
<p>
exchangeToMono, exchangeToFlux
</p>
<ul>
<li>
since spring &gt;= 5.3 available.
</li>
<li>
since spring boot version &gt;= 2.4.x available.
</li>
</ul>
</li>
</ul>
<h3>
When occur memory leak.
</h3>
<p>
When you didn't using
<code>
ClientResponse.bodyToMono,bodyToFlux
</code>
under codes.
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
In fail case you will be faced on memory leak. cause you didn't consume your response body.
</p>
<p>
If you didn't consume your response body, than your connection would not be disconnected.
</p>
<p>
Now, what happened..? your http connect pool will be fulled by used thread. When there are no more threads available, your request will be failed.
</p>
<h2>
How to Solved?
</h2>
<p>
If you using upper version of spring boot 2.4.x than using
<code>
exchangeToMono
</code>
like below.
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
If you under verion of spring boot 2.4.x than using
<code>
retrieve()
</code>
or consume your response body before throw exception.
</p>
<p>
For excample below codes.
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
I thought I should get into the habit of reading and using the document properly before using the library.
<br>
Libraries don't do everything.
</p>
<blockquote>
<p>
<em>
Stay Hunger, Stay Foolish
</em>
</p>
</blockquote>
<h2>
Appendix
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
