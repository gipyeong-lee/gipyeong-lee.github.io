---
title: what's different between `retrieve` and `exchange` in Webflux?
tags: [spring boot, webflux]
style: border
color: light
description: If you using webflux stack on your api server or else. you should read this post.
---

## Under what circumstances?

I was using webflux with spring boot version 2.x.x

When i was using Webclient in my codes. I was usually using `exchange()` after request. cause, api what i used. when failed. it response `200 HTTP Status` with error body.

At that time i had a big mistake. that I thought `exchange()` and `retrieve()` is same.

If you think like that. you are wrong. they are different. then what is different `exchange` and `retrieve`?

### Response is Different

According to [docs](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.RequestHeadersSpec.html#retrieve--)

- WebClient.ResponseSpec `retrieve()`
  - Response body when response status is **200 ok**
  - By default, 4xx and 5xx responses result in a WebClientResponseException. To customize error handling, use onStatus handlers.

- reactor.core.publisher.Mono<ClientResponse> exchange()
  - since Spring 5.3 due to the possibility to leak memory and/or connections
  - when using exchange(), it is the responsibility of the application to consume any response content regardless of the scenario (success, error, unexpected data, etc). Not doing so can cause a memory leak.
  - please, use exchangeToMono(Function), exchangeToFlux(Function)

- exchangeToMono, exchangeToFlux
  - since spring >= 5.3 available.
  - since spring boot version >= 2.4.x available.

### When occur memory leak.

When you didn't using `ClientResponse.bodyToMono,bodyToFlux` under codes.

```kotlin
.exchange()
.flatMap { clientResponse ->
    if (clientResponse.statusCode() === HttpStatus.OK) {
        // success request.
        clientResponse.bodyToMono(CLASS::class.java)
    }
    else {
        // failed http request. in here memory leak occured.
        throw Exception()
    }
}
```

In fail case you will be faced on memory leak. cause you didn't consume your response body.

If you didn't consume your response body, than your connection would not be disconnected.

Now, what happened..? your http connect pool will be fulled by used thread. When there are no more threads available, your request will be failed.

## How to Solved?

If you using upper version of spring boot 2.4.x than using `exchangeToMono` like below.

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

If you under verion of spring boot 2.4.x than using `retrieve()` or consume your response body before throw exception.

For excample below codes.

```kotlin
clientResponse.bodyToMono<String>().defaultIfEmpty("").map {
    throw Exception()
}
```

## Conclusion

I thought I should get into the habit of reading and using the document properly before using the library.
Libraries don't do everything.

## Appendix

- [Versions of Spring Boot](https://docs.spring.io/spring-boot/docs/)
- [Spring Boot 2.3.x Dependencies](https://docs.spring.io/spring-boot/docs/2.3.x/reference/html/appendix-dependency-versions.html#dependency-versions)

> _Stay Hunger, Stay Foolish_
