---
layout: post
title: "Webflux exchange と retrieve の違い"
description: "どのような状況で？私は Spring Boot 2.x.x バージョンで Webflux を使用していました。コード内で Webclient を使用する際、通常はリクエストの後に exchange() を使用していました。なぜなら、使用していた API が失敗した際に 200 HTTP ステータスとエラーボディを返していたからです..."
date: 2021-03-25 08:00:24 +0900
section: blog
category: engineering
lang: ja
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
どのような状況で？
</h2>
<p>
私は Spring Boot 2.x.x バージョンで Webflux を使用していました。
</p>
<p>
コード内で Webclient を使用する際、通常はリクエストの後に <code>exchange()</code> を使用していました。なぜなら、使用していた API が失敗した際に <code>200 HTTP ステータス</code> とエラーボディを返していたからです。
</p>
<p>
当時、私は大きな勘違いをしていました。<code>exchange()</code> と <code>retrieve()</code> が同じものだと思い込んでいたのです。
</p>
<p>
もしあなたもそう思っているなら、それは間違いです。両者は異なります。では、<code>exchange</code> と <code>retrieve</code> にはどのような違いがあるのでしょうか？
</p>
<h3>
レスポンスが異なる
</h3>
<p>
<a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">
公式ドキュメント
</a>
によると：
</p>
<ul>
<li>
<p>
WebClient.ResponseSpec <code>retrieve()</code>
</p>
<ul>
<li>
レスポンスステータスが <strong>200 OK</strong> の場合のレスポンスボディ
</li>
<li>
デフォルトでは、4xx および 5xx のレスポンスは WebClientResponseException を発生させます。エラーハンドリングをカスタマイズするには、onStatus ハンドラを使用してください。
</li>
</ul>
</li>
<li>
<p>
reactor.core.publisher.Mono&lt;ClientResponse&gt; <code>exchange()</code>
</p>
<ul>
<li>
Spring 5.3 以降、メモリリークや接続リークの可能性があるため非推奨。
</li>
<li>
exchange() を使用する場合、成功、エラー、予期せぬデータなど、どのようなシナリオであってもレスポンスコンテンツを消費するのはアプリケーション側の責任となります。消費しない場合、メモリリークの原因となります。
</li>
<li>
<code>exchangeToMono(Function)</code>、<code>exchangeToFlux(Function)</code> を使用してください。
</li>
</ul>
</li>
<li>
<p>
exchangeToMono, exchangeToFlux
</p>
<ul>
<li>
Spring >= 5.3 以降で利用可能。
</li>
<li>
Spring Boot バージョン >= 2.4.x 以降で利用可能。
</li>
</ul>
</li>
</ul>
<h3>
メモリリークが発生するケース
</h3>
<p>
以下のように <code>ClientResponse.bodyToMono</code> や <code>bodyToFlux</code> を使用しなかった場合です。
</p>
<pre>
<code class="language-kotlin">
.exchange()
.flatMap { clientResponse -&gt;
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // リクエスト成功
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // HTTP リクエスト失敗。ここでメモリリークが発生します。
        throw Exception()
    }
}
</code>
</pre>
<p>
失敗した場合、レスポンスボディを消費していないためメモリリークに直面することになります。
</p>
<p>
レスポンスボディを消費しないと、コネクションが切断されません。
</p>
<p>
さて、どうなるでしょうか？ HTTP コネクションプールが使用中のスレッドで一杯になります。利用可能なスレッドがなくなると、リクエストは失敗します。
</p>
<h2>
解決策は？
</h2>
<p>
Spring Boot 2.4.x 以上のバージョンを使用している場合は、以下のように <code>exchangeToMono</code> を使用します。
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
Spring Boot 2.4.x 未満のバージョンを使用している場合は、<code>retrieve()</code> を使用するか、例外を投げる前にレスポンスボディを消費してください。
</p>
<p>
以下はそのコード例です。
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
ライブラリを使う前に、ドキュメントを正しく読み、活用する習慣を身につけるべきだと痛感しました。
<br>
ライブラリは全てをよしなに解決してくれるわけではありません。
</p>
<blockquote>
<p>
<em>
Stay Hunger, Stay Foolish（ハングリーであれ、愚かであれ）
</em>
</p>
</blockquote>
<h2>
参考資料
</h2>
<ul>
<li>
<a href="https://docs.spring.io/spring-boot/docs/">
Spring Boot のバージョン
</a>
</li>
<li>
<a href="https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions">
Spring Boot 2.3.x の依存関係
</a>
</li>
<li>
<a href="https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--">
Spring framework webclient ドキュメント
</a>
</li>
</ul>