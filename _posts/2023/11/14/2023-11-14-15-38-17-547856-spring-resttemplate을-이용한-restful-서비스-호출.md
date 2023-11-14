---
layout: post
title: "[java] Spring RestTemplate을 이용한 RESTful 서비스 호출"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

Spring RestTemplate은 Spring 프레임워크에서 제공하는 HTTP 클라이언트 라이브러리로, RESTful 서비스를 호출하는데 매우 편리한 기능을 제공합니다. 이 글에서는 RestTemplate을 사용하여 RESTful 서비스를 호출하는 방법에 대해 알아보겠습니다.

## 의존성 추가하기

먼저, Maven이나 Gradle을 사용하여 프로젝트에 Spring RestTemplate의 의존성을 추가해야 합니다.

Maven:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

Gradle:

```
implementation 'org.springframework.boot:spring-boot-starter-web'
```

## RestTemplate 사용하기

RestTemplate은 HTTP 요청을 보내고 응답을 받는데 사용됩니다. 주요 메소드는 다음과 같습니다.

- `getForObject(url, responseType)`: GET 요청을 보내고 응답을 객체로 받습니다.
- `postForEntity(url, request, responseType)`: POST 요청을 보내고 응답을 ResponseEntity로 받습니다.
- `put(url, request)`: PUT 요청을 보냅니다.
- `delete(url)`: DELETE 요청을 보냅니다.

### GET 요청 보내기

```java
RestTemplate restTemplate = new RestTemplate();
String url = "http://example.com/api/users/{id}";

User user = restTemplate.getForObject(url, User.class, 1);
System.out.println(user.getName()); // 사용자의 이름 출력
```

### POST 요청 보내기

```java
RestTemplate restTemplate = new RestTemplate();
String url = "http://example.com/api/users";

User newUser = new User("John Doe");

ResponseEntity<User> response = restTemplate.postForEntity(url, newUser, User.class);
if (response.getStatusCode() == HttpStatus.CREATED) {
    User createdUser = response.getBody();
    System.out.println(createdUser.getId()); // 생성된 사용자의 ID 출력
}
```

## 요청 매개변수 수정하기

URL에 포함되는 매개변수를 동적으로 설정하려면, `getForObject` 메소드의 세 번째 매개변수에 `UriVariables`를 사용하면 됩니다.

```java
RestTemplate restTemplate = new RestTemplate();
String url = "http://example.com/api/users/{id}";

Map<String, String> params = new HashMap<>();
params.put("id", "1");

User user = restTemplate.getForObject(url, User.class, params);
System.out.println(user.getName()); // 사용자의 이름 출력
```

## 응답을 커스터마이즈하기

RestTemplate은 기본적으로 JSON 형식의 응답을 처리할 수 있습니다. 하지만, 다른 형식의 응답을 처리해야 할 때는 커스터마이즈해야 합니다. 예를 들어, XML 형식의 응답을 처리하려면 Jackson 외에 추가적인 라이브러리가 필요합니다.

Maven:

```xml
<dependency>
    <groupId>com.fasterxml.jackson.dataformat</groupId>
    <artifactId>jackson-dataformat-xml</artifactId>
</dependency>
```

Gradle:

```
implementation 'com.fasterxml.jackson.dataformat:jackson-dataformat-xml'
```

RestTemplate을 생성할 때, 커스터마이즈된 `HttpMessageConverter`를 추가해야 합니다.

```java
RestTemplate restTemplate = new RestTemplate();

MappingJackson2XmlHttpMessageConverter xmlConverter = new MappingJackson2XmlHttpMessageConverter();
xmlConverter.setSupportedMediaTypes(Collections.singletonList(MediaType.APPLICATION_XML));

restTemplate.getMessageConverters().add(xmlConverter);
```

이제 RestTemplate을 사용하여 XML 형식의 응답을 처리할 수 있습니다.

## 결론

Spring RestTemplate을 사용하여 RESTful 서비스를 호출하는 방법을 알아보았습니다. RestTemplate은 다양한 HTTP 메소드를 지원하며, 요청과 응답을 커스터마이즈할 수 있는 기능을 제공합니다. 좀 더 복잡한 상황에서는 WebClient를 고려해볼 수도 있습니다. Spring에서 제공하는 HTTP 클라이언트 라이브러리 중에서 선택해 사용하는 것이 중요합니다.

참고 자료:
- [Spring RestTemplate 공식 문서](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/client/RestTemplate.html)
- [Spring RestTemplate Guide](https://spring.io/guides/gs/consuming-rest/)