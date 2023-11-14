---
layout: post
title: "[java] Spring RestTemplate과 Feign을 이용한 서비스 간 통신"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

서비스 간 통신은 분산 시스템에서 매우 중요한 요소입니다. 이를 위해 스프링 프레임워크에서는 RestTemplate과 Feign이라는 두 가지 방법을 제공합니다. 이 블로그 포스트에서는 각각의 방법에 대해 자세히 알아보겠습니다.

## 1. RestTemplate

RestTemplate은 스프링의 HTTP 통신을 간편하게 처리하기 위한 클래스입니다. RESTful 웹 서비스에 대한 요청을 생성하고 응답을 받을 수 있습니다.

```java
RestTemplate restTemplate = new RestTemplate();
String url = "http://api.example.com/users/{id}";
Map<String, String> params = new HashMap<>();
params.put("id", "123");

UserDto user = restTemplate.getForObject(url, UserDto.class, params);
```

위의 코드에서는 RestTemplate을 사용하여 "http://api.example.com/users/{id}" URL에 GET 요청을 보내고, 응답을 UserDto 객체로 받아옵니다. URL의 `{id}` 부분은 params 맵에서 값을 가져와 대체됩니다.

RestTemplate은 다양한 HTTP 메소드와 응답 타입을 지원합니다. 또한, 요청과 응답에 대한 인터셉터를 추가하여 헤더를 설정하거나 응답을 가공할 수 있습니다.

## 2. Feign

Feign은 스프링 클라우드 프로젝트의 일부로 개발된 선언적인 HTTP 클라이언트입니다. 인터페이스를 정의하고 해당 인터페이스의 메소드를 호출함으로써 서비스 간 통신을 처리할 수 있습니다.

```java
@FeignClient(name = "user-service")
public interface UserServiceClient {

    @GetMapping("/users/{id}")
    UserDto getUserById(@PathVariable("id") String id);
}

// Feign 클라이언트 사용 예시
@Autowired
private UserServiceClient userServiceClient;

public void getUser(String id) {
    UserDto user = userServiceClient.getUserById(id);
}
```

위의 코드에서는 `@FeignClient` 어노테이션을 사용하여 UserServiceClient 인터페이스를 Feign 클라이언트로 정의합니다. `@GetMapping` 어노테이션을 사용하여 서비스의 URL과 메소드를 매핑하고, 해당 메소드를 호출하여 서비스 간 통신을 처리합니다.

Feign은 스프링 클라우드의 서비스 디스커버리와 통합되어 서비스의 위치를 자동으로 찾아주고, 로드 밸런싱을 지원합니다.

## 결론

RestTemplate과 Feign은 모두 스프링의 편리한 기능을 활용한 서비스 간 통신 방법입니다. RestTemplate은 직접적인 방법을 사용하여 HTTP 요청과 응답을 처리하는 반면, Feign은 선언적인 방법을 이용하여 클라이언트 인터페이스를 정의하고 자동으로 서비스 간 통신을 처리합니다.

어떤 방법을 선택할지는 프로젝트의 요구 사항과 복잡도에 따라 결정될 수 있습니다.