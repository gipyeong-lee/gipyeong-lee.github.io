---
layout: post
title: "Webflux 中 exchange 與 retrieve 的差異"
description: "在什麼情況下？我當時正在使用 Spring Boot 2.x.x 版本的 Webflux。當我在程式碼中使用 Webclient 時，我通常會在請求後使用 exchange()，因為我所使用的 API 在失敗時會回傳 200 HTTP 狀態碼並帶有錯誤訊息主體..."
date: 2021-03-25 08:00:24 +0900
section: blog
category: engineering
lang: zh-tw
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
在什麼情況下？
</h2>
<p>
我當時正在使用 Spring Boot 2.x.x 版本的 Webflux。
</p>
<p>
當我在程式碼中使用 Webclient 時，我通常會在請求後使用 <code>exchange()</code>。原因是我所使用的 API 在失敗時，會回傳 <code>200 HTTP 狀態碼</code> 並帶有錯誤訊息主體。
</p>
<p>
當時我犯了一個大錯，我以為 <code>exchange()</code> 和 <code>retrieve()</code> 是一樣的。
</p>
<p>
如果你也這麼想，那就錯了。它們是不同的。那麼 <code>exchange</code> 和 <code>retrieve</code> 之間有什麼區別呢？
</p>
<h3>
回應方式不同
</h3>
<p>
根據 <a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">官方文件</a>：
</p>
<ul>
<li>
<p>
WebClient.ResponseSpec <code>retrieve()</code>
</p>
<ul>
<li>
當回應狀態為 <strong>200 OK</strong> 時，取得回應主體 (Response body)
</li>
<li>
預設情況下，4xx 和 5xx 的回應會導致 WebClientResponseException。若要自訂錯誤處理，請使用 onStatus 處理器。
</li>
</ul>
</li>
<li>
<p>
reactor.core.publisher.Mono&lt;ClientResponse&gt; <code>exchange()</code>
</p>
<ul>
<li>
自 Spring 5.3 起，由於存在記憶體和/或連線洩漏的可能性，此方法已被標記為不建議使用
</li>
<li>
當使用 <code>exchange()</code> 時，應用程式必須負責消耗任何回應內容，無論情境為何（成功、錯誤、意外資料等）。如果不這樣做，可能會導致記憶體洩漏。
</li>
<li>
請改用 <code>exchangeToMono(Function)</code> 或 <code>exchangeToFlux(Function)</code>
</li>
</ul>
</li>
<li>
<p>
<code>exchangeToMono</code>, <code>exchangeToFlux</code>
</p>
<ul>
<li>
自 Spring >= 5.3 起提供
</li>
<li>
自 Spring Boot 版本 >= 2.4.x 起提供
</li>
</ul>
</li>
</ul>
<h3>
何時會發生記憶體洩漏
</h3>
<p>
當你在以下程式碼中沒有使用 <code>ClientResponse.bodyToMono</code> 或 <code>bodyToFlux</code> 時：
</p>
<pre>
<code class="language-kotlin">
.exchange()
.flatMap { clientResponse -&gt;
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // 請求成功
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // HTTP 請求失敗。在這裡發生了記憶體洩漏
        throw Exception()
    }
}
</code>
</pre>
<p>
在失敗的情況下，你會面臨記憶體洩漏，因為你沒有消耗回應主體。
</p>
<p>
如果你沒有消耗回應主體，那麼你的連線就不會被中斷。
</p>
<p>
現在，發生了什麼事……？你的 HTTP 連線池將會被已使用的執行緒填滿。當沒有更多可用執行緒時，你的請求將會失敗。
</p>
<h2>
如何解決？
</h2>
<p>
如果你使用的 Spring Boot 版本高於 2.4.x，請像下面這樣使用 <code>exchangeToMono</code>：
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
如果你使用的 Spring Boot 版本低於 2.4.x，請使用 <code>retrieve()</code>，或者在拋出異常之前消耗掉你的回應主體。
</p>
<p>
範例如下：
</p>
<pre>
<code class="language-kotlin">
clientResponse.bodyToMono&lt;String&gt;().defaultIfEmpty("").map {
    throw Exception()
}
</code>
</pre>
<h2>
結論
</h2>
<p>
我認為在使用函式庫之前，我應該養成正確閱讀和使用文件的習慣。
<br>
函式庫並不會自動處理所有事情。
</p>
<blockquote>
<p>
<em>
求知若飢，虛心若愚 (Stay Hungry, Stay Foolish)
</em>
</p>
</blockquote>
<h2>
參考資料
</h2>
<ul>
<li>
<a href="https://docs.spring.io/spring-boot/docs/">
Spring Boot 版本
</a>
</li>
<li>
<a href="https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions">
Spring Boot 2.3.x 依賴版本
</a>
</li>
<li>
<a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">
Spring framework webclient 文件
</a>
</li>
</ul>