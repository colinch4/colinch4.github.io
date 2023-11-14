---
layout: post
title: "[java] Spring WebClient를 사용한 비동기 RESTful API 호출 방법"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

Spring WebClient는 Spring 5부터 도입된 비동기 HTTP 클라이언트입니다. WebClient는 기존의 RestTemplate보다 더 유연하고 효율적인 방식으로 RESTful API를 호출할 수 있습니다. 이번 블로그 포스트에서는 Spring WebClient를 사용하여 비동기 방식으로 RESTful API를 호출하는 방법에 대해 알아보겠습니다.

## WebClient 의존성 추가하기
WebClient를 사용하기 위해서는 먼저 해당 의존성을 프로젝트에 추가해야 합니다. Maven 기준으로는 다음과 같이 의존성을 추가할 수 있습니다.
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-webflux</artifactId>
</dependency>
```

## WebClient 빈 설정하기
WebClient를 사용하기 위해서는 빈으로 등록해야 합니다. 이를 위해서는 `WebClient.Builder`를 사용합니다. 
```java
@Configuration
public class WebClientConfig {

    @Bean
    public WebClient webClient() {
        return WebClient.builder().build();
    }
}
```

## 비동기 API 호출하기
WebClient를 이용하여 비동기 방식으로 RESTful API를 호출할 수 있습니다. 예를 들어, `GET` 메소드를 사용하여 JSON 형식의 데이터를 조회하는 요청을 보내는 코드는 다음과 같습니다.
```java
@Autowired
private WebClient webClient;

public Mono<ResponseEntity<String>> getData() {
    return webClient.get()
            .uri("https://api.example.com/data")
            .header("Authorization", "Bearer {token}")
            .exchangeToMono(response -> {
                if (response.statusCode().is2xxSuccessful()) {
                    return response.bodyToMono(String.class);
                } else {
                    return response.createException().flatMap(Mono::error);
                }
            })
            .map(data -> ResponseEntity.ok().body(data));
}
```
위의 코드에서는 `exchangeToMono` 메소드를 사용하여 비동기로 API를 호출하고, 응답을 처리합니다. 응답이 성공인 경우 `bodyToMono` 메소드를 사용하여 데이터를 Mono 형태로 받아옵니다. 응답이 실패인 경우 `createException` 메소드를 사용하여 예외를 생성하고, 이를 처리합니다.

## 비동기 API 호출 결과 받기
비동기 API 호출의 결과는 Mono 또는 Flux 형태로 받아올 수 있습니다. Mono는 0 또는 1개의 결과를 받아올 때 사용하고, Flux는 여러 개의 결과를 받아올 때 사용합니다. 이를 이용하여 비동기 API 호출의 결과를 처리할 수 있습니다.

```java
public void handleApiCall() {
    Mono<ResponseEntity<String>> responseMono = getData();
    responseMono.subscribe(responseEntity -> {
        if (responseEntity.getStatusCode().is2xxSuccessful()) {
            String data = responseEntity.getBody();
            // 데이터 처리 로직
        } else {
            // 에러 처리 로직
        }
    });
}
```

위의 코드에서는 `subscribe` 메소드를 사용하여 Mono의 결과를 처리합니다. 응답이 성공인 경우 `getStatusCode` 메소드를 사용하여 상태 코드를 확인하고, `getBody` 메소드를 사용하여 데이터를 받아옵니다. 이후 데이터 처리 또는 에러 처리 로직을 구현할 수 있습니다.

## 결론
Spring WebClient를 사용하여 비동기 방식으로 RESTful API를 호출하는 방법에 대해 알아보았습니다. WebClient는 기존의 RestTemplate보다 더 유연하고 효율적인 방식으로 API를 호출할 수 있으며, Reactor에서 제공하는 Mono와 Flux와 함께 사용하면 비동기 API 호출을 보다 효과적으로 처리할 수 있습니다.

---

**참고 자료:**
- [Spring WebClient Reference Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html#webflux-client)
- [Baeldung - Introduction to Spring WebClient](https://www.baeldung.com/spring-5-webclient)