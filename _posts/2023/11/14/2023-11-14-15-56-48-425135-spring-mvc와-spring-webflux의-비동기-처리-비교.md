---
layout: post
title: "[java] Spring MVC와 Spring WebFlux의 비동기 처리 비교"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

Spring 프레임워크는 Java로 웹 애플리케이션을 개발하는 데 널리 사용되는 프레임워크입니다. Spring MVC는 전통적인 동기 방식으로 웹 요청을 처리하는 데 사용되며, Spring WebFlux는 비동기 방식으로 웹 요청을 처리하는 데 사용됩니다.

## 1. Spring MVC

Spring MVC는 멀티스레드를 사용하여 동기적으로 클라이언트 요청을 처리합니다. 이는 기본적으로 Servlet 기반의 웹 애플리케이션에 적합한 방식입니다. Spring MVC는 `@RequestMapping` 어노테이션을 사용하여 요청을 처리하는 메서드를 정의하며, 각 요청은 별도의 스레드에서 처리됩니다.

```java
@RestController
public class MyController {

    @RequestMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```

Spring MVC는 스레드를 블로킹하지 않고 리소스를 효율적으로 사용하기 위해 비동기 서블릿을 지원합니다. 하지만, I/O 연산이 많은 애플리케이션에서는 처리량과 확장성에 제한이 있을 수 있습니다.

## 2. Spring WebFlux

Spring WebFlux는 비동기적인 넌블로킹 방식으로 웹 요청을 처리합니다. 이는 기본적으로 Reactive Streams API를 지원하며, Non-Blocking I/O 모델을 사용하여 요청-응답 사이클을 처리합니다. Spring WebFlux는 `@RestController` 어노테이션을 사용하여 요청을 처리하는 메서드를 정의합니다.

```java
@RestController
public class MyController {

    @GetMapping("/hello")
    public Mono<String> hello() {
        return Mono.just("Hello, World!");
    }
}
```

Spring WebFlux는 Reactor 프로젝트의 Mono나 Flux와 같은 리액티브 타입을 사용하여 비동기 방식으로 작업을 수행합니다. 이를 통해 많은 자원을 효율적으로 관리하고 높은 처리량과 확장성을 달성할 수 있습니다.

## 3. 비동기 처리 비교

Spring MVC와 Spring WebFlux는 각각 동기적인 방식과 비동기적인 방식으로 웹 요청을 처리합니다. 비동기 처리는 I/O 연산이 많은 애플리케이션에서 효과적이며, 더 적은 자원으로 높은 처리량을 달성할 수 있습니다. 반면, 동기 처리는 작업 순서와 상태에 더 중점을 둡니다.

아래는 Spring MVC와 Spring WebFlux의 비동기 처리 방식 비교입니다.

|  | Spring MVC | Spring WebFlux |
|---|---|---|
| 동작 방식 | 멀티스레드, 블로킹 | 넌블로킹, 비동기 |
| 사용 가능한 리액티브 타입 | 지원하지 않음 | Mono, Flux 등 |
| 웹 서버 | Tomcat, Jetty 등 | Netty, Undertow 등 |
| 기타 특징 | 표준 Servlet 기반 | 리액티브 스트림 API 지원 |

## 4. 결론

Spring MVC는 전통적인 동기적인 방식으로 웹 요청을 처리하는 데 사용되며, 기존의 Servlet 기반 애플리케이션을 쉽게 개발할 수 있습니다. 반면, Spring WebFlux는 비동기적인 넌블로킹 방식으로 웹 요청을 처리하는 데 사용되며, 높은 처리량과 확장성을 요구하는 애플리케이션에 적합합니다.

비동기 처리 방식을 선택할 때는 애플리케이션의 요구 사항과 성능 목표를 고려해야 합니다. Spring MVC는 기본적인 개발 방법을 제공하며, Spring WebFlux는 리액티브 프로그래밍 모델을 지원합니다.