---
layout: post
title: "[java] Spring Cloud Gateway를 사용한 API 게이트웨이 구축 방법"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

API 게이트웨이는 클라이언트 요청을 받아 백엔드 마이크로서비스로 전달하는 역할을 수행하는 서버입니다. 이러한 아키텍처는 클라이언트에 대한 단일 진입점을 제공하고, 요청과 응답 전송 시 보안, 로깅, 로드 밸런싱 등 다양한 기능을 추가할 수 있습니다. 이 글에서는 Spring Cloud Gateway와 함께 API 게이트웨이를 구축하는 방법에 대해 알아보겠습니다.

## 1. Spring Boot 프로젝트 생성

먼저, Spring Boot 프로젝트를 생성해야 합니다. Maven이나 Gradle을 사용하여 Spring Initializr를 통해 간단히 프로젝트를 생성할 수 있습니다.

## 2. Spring Cloud Gateway 의존성 추가

Spring Cloud Gateway를 사용하려면 `spring-cloud-starter-gateway` 의존성을 프로젝트에 추가해야 합니다.

```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-gateway</artifactId>
    </dependency>
    ...
</dependencies>
```

## 3. API 게이트웨이 구성

`application.yml` 파일을 통해 API 게이트웨이를 구성할 수 있습니다. 다음은 예시입니다.

```yaml
server:
  port: 8080

spring:
  cloud:
    gateway:
      routes:
        - id: first-service
          uri: http://localhost:8081
          predicates:
            - Path=/first/**
        - id: second-service
          uri: http://localhost:8082
          predicates:
            - Path=/second/**
```

위의 예시에서는 `/first/**` 경로로 들어오는 요청을 `http://localhost:8081`로, `/second/**` 경로로 들어오는 요청을 `http://localhost:8082`로 전달합니다.

## 4. 필터 적용

Spring Cloud Gateway는 필터를 사용하여 요청 및 응답을 변형하거나 추가적인 작업을 수행할 수 있습니다. 예를 들어, 보안 필터를 추가하여 인증된 사용자만 특정 경로에 접근하도록 할 수 있습니다.

```java
@Component
public class AuthenticationFilter implements GatewayFilter {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        // 인증 로직 구현
    }
}
```

위의 예시는 사용자 인증을 위한 필터 구현체입니다. 이 필터를 사용하기 위해서는 `@Component` 애노테이션을 붙여 스프링의 컴포넌트로 등록해야 합니다.

## 5. 실행 및 테스트

모든 설정이 완료되었다면, 프로젝트를 실행하여 API 게이트웨이를 테스트할 수 있습니다. 웹 브라우저나 API 클라이언트를 사용하여 `http://localhost:8080/first/**` 또는 `http://localhost:8080/second/**` 경로로 요청을 보내볼 수 있습니다.

## 결론

Spring Cloud Gateway를 사용하여 API 게이트웨이를 구축하는 방법에 대해 알아보았습니다. 게이트웨이를 통해 단일 진입점을 제공하고, 다양한 기능을 추가하여 마이크로서비스 아키텍처를 유연하고 확장 가능하게 구성할 수 있습니다. 추가적으로 Spring Cloud Netflix의 Zuul과 같은 다른 API 게이트웨이도 고려해볼만 합니다. 

관련 참고 문서:
- [Spring Cloud Gateway 공식 문서](https://cloud.spring.io/spring-cloud-gateway/reference/html/)
- [Spring Initializr](https://start.spring.io/)