---
layout: post
title: Webflux 中 `retrieve` 和 `exchange` 有什么区别？
tags: [spring boot, webflux]
style: border
color: info
description: 如果您在 API 服务器或其他地方使用 Webflux 技术栈，您应该阅读这篇文章。
lang: zh-cn
ref: 2020-12-13-Retrive-vs-Exchange
---

## 在什么情况下？

我当时正在使用 Spring Boot 2.x.x 版本的 Webflux。

当我在代码中使用 WebClient 时，我通常在请求后使用 `exchange()`。因为我使用的 API 在失败时也会返回 `200 HTTP Status` 并在 Body 中包含错误信息。

当时我犯了一个大错，我以为 `exchange()` 和 `retrieve()` 是一样的。

如果你也这么想，那就错了。它们是不同的。那么 `exchange` 和 `retrieve` 到底有什么区别呢？

### 响应方式不同

根据 [文档](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--)：

- **WebClient.ResponseSpec `retrieve()`**
  - 当响应状态为 **200 OK** 时的响应体。
  - 默认情况下，4xx 和 5xx 响应会导致 `WebClientResponseException`。如需自定义错误处理，请使用 `onStatus` 处理器。

- **reactor.core.publisher.Mono<ClientResponse> `exchange()`**
  - 自 Spring 5.3 起，由于可能导致内存和/或连接泄漏而被弃用。
  - 使用 `exchange()` 时，应用程序有责任在任何情况下（成功、错误、意外数据等）消费响应内容。如果不这样做，可能会导致内存泄漏。
  - 请使用 `exchangeToMono(Function)` 或 `exchangeToFlux(Function)`。

- **`exchangeToMono`, `exchangeToFlux`**
  - 自 Spring 5.3 起可用。
  - 自 Spring Boot 2.4.x 起可用。

### 何时会发生内存泄漏？

当你在代码中没有使用 `ClientResponse.bodyToMono` 或 `bodyToFlux` 时。

```kotlin
.exchange()
.flatMap { clientResponse ->
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // 请求成功
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // HTTP 请求失败。此处会发生内存泄漏。
        throw Exception()
    }
}
```

在失败的情况下，你会面临内存泄漏，因为你没有消费响应体。

如果你不消费响应体，连接就无法释放并断开。

接下来会发生什么？你的 HTTP 连接池将被占用的线程填满。当没有更多可用线程时，你的请求将会失败。

## 如何解决？

如果你使用的是 Spring Boot 2.4.x 或更高版本，请按如下方式使用 `exchangeToMono`：

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

如果你使用的是 Spring Boot 2.4.x 之前的版本，请使用 `retrieve()`，或者在抛出异常之前消费响应体。

例如以下代码：

```kotlin
clientResponse.bodyToMono<String>().defaultIfEmpty("").map {
    throw Exception()
}
```

## 结论

我觉得在开始使用一个库之前，应该养成仔细阅读文档并正确使用的习惯。库并不能包办一切。

> _Stay Hungry, Stay Foolish_

## 附录

- [Spring Boot 版本列表](https://docs.spring.io/spring-boot/docs/)
- [Spring Boot 2.3.x 依赖项](https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions)
- [Spring Framework WebClient 文档](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--)
