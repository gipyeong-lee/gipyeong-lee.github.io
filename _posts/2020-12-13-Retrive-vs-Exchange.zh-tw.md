---
layout: post
title: Webflux 中 `retrieve` 與 `exchange` 有什麼不同？
tags: [spring boot, webflux]
style: border
color: info
description: 如果您在 API 伺服器或其他地方使用 Webflux 技術棧，您應該閱讀這篇文章。
lang: zh-tw
ref: 2020-12-13-Retrive-vs-Exchange
---

## 在什麼情況下？

我當時正在使用 Spring Boot 2.x.x 版本的 Webflux。

當我在代碼中使用 WebClient 時，通常會在請求後使用 `exchange()`。因為我所使用的 API 在失敗時，仍會回傳 `200 HTTP Status` 並帶有錯誤主體（error body）。

當時我犯了一個大錯，我以為 `exchange()` 和 `retrieve()` 是相同的。

如果你也是這麼想的，那你就錯了。它們是不同的。那麼 `exchange` 和 `retrieve` 之間到底有什麼區別呢？

### 回應方式不同

根據 [官方文件](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--)：

- **WebClient.ResponseSpec `retrieve()`**
  - 當回應狀態為 **200 OK** 時的回應主體。
  - 預設情況下，4xx 和 5xx 的回應會導致 `WebClientResponseException`。若要自定義錯誤處理，請使用 `onStatus` 處理器。

- **reactor.core.publisher.Mono<ClientResponse> `exchange()`**
  - 自 Spring 5.3 起已棄用，因為可能導致記憶體和/或連線洩漏。
  - 使用 `exchange()` 時，應用程式有責任消耗（consume）任何回應內容，無論是成功、錯誤或非預期數據等情況。若不這樣做，可能會導致記憶體洩漏。
  - 請改用 `exchangeToMono(Function)` 或 `exchangeToFlux(Function)`。

- **`exchangeToMono`, `exchangeToFlux`**
  - 自 Spring 5.3 以上版本提供。
  - 自 Spring Boot 2.4.x 以上版本提供。

### 何時會發生記憶體洩漏？

當您未在代碼中使用 `ClientResponse.bodyToMono` 或 `bodyToFlux` 時。

```kotlin
.exchange()
.flatMap { clientResponse ->
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // 請求成功
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // HTTP 請求失敗。這裡會發生記憶體洩漏。
        throw Exception()
    }
}
```

在失敗的情況下，您將面臨記憶體洩漏，因為您沒有消耗（consume）回應主體。

如果您沒有消耗回應主體，您的連線將不會斷開。

接下來會發生什麼事呢？您的 HTTP 連線池（connection pool）將被已使用的執行緒填滿。當沒有更多可用執行緒時，您的請求將會失敗。

## 如何解決？

如果您使用的是 Spring Boot 2.4.x 以上的版本，請像下面這樣使用 `exchangeToMono`：

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

如果您使用的是 Spring Boot 2.4.x 以下的版本，請使用 `retrieve()`，或在拋出異常前消耗您的回應主體。

例如以下代碼：

```kotlin
clientResponse.bodyToMono<String>().defaultIfEmpty("").map {
    throw Exception()
}
```

## 結論

我認為在開始使用函式庫之前，應該養成仔細閱讀並正確使用文件的習慣。
函式庫並不會幫你處理好所有事情。

> _求知若渴，虛懷若谷 (Stay Hungry, Stay Foolish)_

## 附錄

- [Spring Boot 版本列表](https://docs.spring.io/spring-boot/docs/)
- [Spring Boot 2.3.x 依賴版本](https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions)
- [Spring Framework WebClient 文件](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--)
