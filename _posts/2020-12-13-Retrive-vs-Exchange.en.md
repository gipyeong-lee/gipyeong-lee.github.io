---
layout: post
title: What is the difference between `retrieve` and `exchange` in WebFlux?
tags: [spring boot, webflux]
style: border
color: info
description: If you are using the WebFlux stack on your API server or elsewhere, you should read this post.
lang: en
ref: 2020-12-13-Retrive-vs-Exchange
---

## Under what circumstances?

I was using WebFlux with Spring Boot version 2.x.x.

When using `WebClient` in my code, I usually used `exchange()` after a request. This was because the API I was using returned a `200 HTTP Status` with an error body when it failed.

At that time, I made a big mistake: I thought `exchange()` and `retrieve()` were the same.

If you think that, you are wrong. They are different. So, what is the difference between `exchange` and `retrieve`?

### The Responses are Different

According to the [docs](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--):

- WebClient.ResponseSpec `retrieve()`
  - Returns the response body when the response status is **200 OK**.
  - By default, 4xx and 5xx responses result in a `WebClientResponseException`. To customize error handling, use `onStatus` handlers.

- reactor.core.publisher.Mono<ClientResponse> exchange()
  - Deprecated since Spring 5.3 due to the possibility of leaking memory and/or connections.
  - When using `exchange()`, it is the responsibility of the application to consume any response content regardless of the scenario (success, error, unexpected data, etc.). Not doing so can cause a memory leak.
  - Please use `exchangeToMono(Function)` or `exchangeToFlux(Function)` instead.

- exchangeToMono, exchangeToFlux
  - Available since Spring Framework >= 5.3.
  - Available since Spring Boot version >= 2.4.x.

### When does a memory leak occur?

It occurs when you do not use `ClientResponse.bodyToMono` or `bodyToFlux` in your code.

```kotlin
.exchange()
.flatMap { clientResponse ->
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // success request.
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // failed http request. In here, a memory leak occurred.
        throw Exception()
    }
}
```

In the failure case, you will face a memory leak because you didn't consume the response body.

If you do not consume the response body, your connection will not be released.

Now, what happens? Your HTTP connection pool will fill up with active threads. When there are no more threads available, your requests will fail.

## How to Solve It?

If you are using Spring Boot 2.4.x or higher, use `exchangeToMono` as shown below.

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

If you are using a version lower than Spring Boot 2.4.x, use `retrieve()` or ensure you consume the response body before throwing an exception.

For example, in the code below:

```kotlin
clientResponse.bodyToMono<String>().defaultIfEmpty("").map {
    throw Exception()
}
```

## Conclusion

I realized I should get into the habit of reading the documentation properly before using a library.
Libraries don't do everything for you.

> _Stay Hungry, Stay Foolish_

## Appendix

- [Versions of Spring Boot](https://docs.spring.io/spring-boot/docs/)
- [Spring Boot 2.3.x Dependencies](https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions)
- [Spring framework webclient docs](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--)
