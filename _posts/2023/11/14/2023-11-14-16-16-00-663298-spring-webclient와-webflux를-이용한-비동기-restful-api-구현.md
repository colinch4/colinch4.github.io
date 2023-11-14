---
layout: post
title: "[java] Spring WebClient와 WebFlux를 이용한 비동기 RESTful API 구현"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

## 소개
Spring WebClient와 WebFlux는 Spring Framework에서 비동기적으로 RESTful API를 구현하는데 사용되는 강력한 도구들입니다. WebClient는 클라이언트 측 HTTP 통신을 처리하는데 사용되며, WebFlux는 서버 측 비동기 엔드포인트를 처리하는데 사용됩니다. 이들을 함께 사용하여 효율적이고 확장 가능한 비동기 웹 애플리케이션을 구현할 수 있습니다.

## WebClient 소개
WebClient는 Spring 5에서 도입된 새로운 HTTP 클라이언트 라이브러리입니다. 기존의 RestTemplate과 달리 비동기적인 방식으로 요청을 처리하며, 리액티브 프로그래밍 모델을 지원합니다. WebClient를 사용하면 더 빠르고 효율적인 웹 애플리케이션을 구현할 수 있습니다.

WebClient를 사용하기 위해 먼저 Maven 또는 Gradle을 사용하여 의존성을 추가해야 합니다. 다음은 Maven을 사용하는 예입니다:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-webflux</artifactId>
</dependency>
```

## WebFlux 소개
WebFlux는 Spring Framework 5에서 도입된 비동기 웹 개발 기능입니다. 이를 사용하면 서버 측에서 비동기 엔드포인트를 쉽게 구현할 수 있습니다. WebFlux는 Netty, Undertow, Tomcat과 같은 다양한 서버를 지원하여 선택할 수 있으며, 리액티브 프로그래밍 모델을 따릅니다.

## 비동기 RESTful API 구현 예제
다음은 Spring WebClient와 WebFlux를 사용하여 비동기 RESTful API를 구현하는 예제입니다.

```java
@RestController
public class UserController {
    
    private final WebClient webClient;
    
    public UserController(WebClient.Builder webClientBuilder) {
        this.webClient = webClientBuilder.baseUrl("https://api.example.com").build();
    }
    
    @GetMapping("/users/{id}")
    public Mono<User> getUser(@PathVariable String id) {
        return webClient.get()
                .uri("/users/{id}", id)
                .retrieve()
                .bodyToMono(User.class);
    }
    
    @PostMapping("/users")
    public Mono<User> createUser(@RequestBody User user) {
        return webClient.post()
                .uri("/users")
                .body(Mono.just(user), User.class)
                .retrieve()
                .bodyToMono(User.class);
    }
    
    // 기타 엔드포인트 및 비즈니스 로직...
}
```

위 예제에서는 UserController 클래스에서 WebClient를 사용하여 간단한 GET 및 POST 요청을 처리하고 있습니다. WebClient의 메소드 체인을 사용하여 요청을 구성하고, retrieve() 및 bodyToMono() 메소드를 사용하여 응답을 처리합니다.

## 결론
Spring WebClient와 WebFlux를 사용하여 비동기 RESTful API를 구현하는 방법에 대해 알아보았습니다. WebClient는 클라이언트 측 HTTP 통신에 사용되며, WebFlux는 서버 측 비동기 엔드포인트를 처리하는 데 사용됩니다. 이들을 함께 사용하여 효율적이고 확장 가능한 비동기 웹 애플리케이션을 구현할 수 있습니다.

더 자세한 내용은 Spring 공식 문서를 참조하시기 바랍니다.

- WebClient: [https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html#webflux-client](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html#webflux-client)
- WebFlux: [https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html#webflux](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html#webflux)