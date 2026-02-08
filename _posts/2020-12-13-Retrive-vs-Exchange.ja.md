---
layout: post
title: Webfluxの `retrieve` と `exchange` の違いとは？
tags: [spring boot, webflux]
style: border
color: info
description: APIサーバーなどでWebfluxスタックを使用しているなら、この記事を読むべきです。
lang: ja
ref: 2020-12-13-Retrive-vs-Exchange
---

## どのような状況だったのか？

私はSpring Boot 2.x.xバージョンでWebfluxを使用していました。

コード内でWebClientを使用する際、リクエスト後に `exchange()` をよく使っていました。なぜなら、私が使用していたAPIは、失敗時にもエラー本文とともに `200 HTTP Status` を返していたからです。

当時、私は大きな勘違いをしていました。`exchange()` と `retrieve()` は同じものだと思っていたのです。

もしあなたもそう思っているなら、それは間違いです。これらは別物です。では、`exchange` と `retrieve` は何が違うのでしょうか？

### レスポンスの違い

[ドキュメント](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--)によると：

- WebClient.ResponseSpec `retrieve()`
  - レスポンスステータスが **200 ok** の場合のレスポンス本文を取得します。
  - デフォルトでは、4xxおよび5xxのレスポンスは `WebClientResponseException` になります。エラーハンドリングをカスタマイズするには、`onStatus` ハンドラを使用します。

- reactor.core.publisher.Mono<ClientResponse> exchange()
  - Spring 5.3以降、メモリや接続のリークが発生する可能性があるため（注意が必要です）。
  - `exchange()` を使用する場合、シナリオ（成功、エラー、予期しないデータなど）に関わらず、**レスポンスコンテンツを消費するのはアプリケーションの責任です**。そうしないと、メモリリークが発生する可能性があります。
  - `exchangeToMono(Function)`、`exchangeToFlux(Function)` を使用してください。

- exchangeToMono, exchangeToFlux
  - Spring Framework >= 5.3 以降で利用可能。
  - Spring Boot version >= 2.4.x 以降で利用可能。

### いつメモリリークが発生するのか

以下のコードのように、`ClientResponse.bodyToMono` や `bodyToFlux` を使用しなかった場合です。

```kotlin
.exchange()
.flatMap { clientResponse ->
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // 成功したリクエスト
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // 失敗したhttpリクエスト。ここでメモリリークが発生します。
        throw Exception()
    }
}
```

失敗したケースでは、メモリリークに直面することになります。なぜなら、レスポンス本文を消費しなかったからです。

レスポンス本文を消費しないと、接続は切断されません。

その結果、何が起こるでしょうか...？ HTTP接続プールが使用中のスレッドで一杯になります。利用可能なスレッドがなくなると、リクエストは失敗するようになります。

## 解決方法は？

Spring Boot 2.4.x以上のバージョンを使用している場合は、以下のように `exchangeToMono` を使用します。

```kotlin
.exchangeToMono(response -> {
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
```

Spring Boot 2.4.x未満のバージョンの場合は、`retrieve()` を使用するか、例外をスローする前にレスポンス本文を消費してください。

例えば以下のコードのようにします。

```kotlin
clientResponse.bodyToMono<String>().defaultIfEmpty("").map {
    throw Exception()
}
```

## 結論

ライブラリを使用する前に、ドキュメントを適切に読んで使用する習慣を身につけるべきだと思いました。
ライブラリがすべてやってくれるわけではありません。

> _Stay Hunger, Stay Foolish_

## 付録

- [Spring Bootのバージョン](https://docs.spring.io/spring-boot/docs/)
- [Spring Boot 2.3.xの依存関係](https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions)
- [Spring framework webclient ドキュメント](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--)
