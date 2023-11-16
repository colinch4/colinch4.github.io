---
layout: post
title: "[java] TestContainers와 REST API 테스트 작성하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

## 목차
- [TestContainers 소개](#testcontainers-소개)
- [REST API 테스트 작성 방법](#rest-api-테스트-작성-방법)

## TestContainers 소개
TestContainers는 자바 환경에서 도커 컨테이너를 사용하여 테스트 환경을 구축할 수 있는 도구입니다. 테스트를 실행하는 동안 실제 환경과 최대한 비슷한 환경을 제공하므로 더 안정적이고 신뢰성 있는 테스트를 작성할 수 있습니다.

TestContainers는 다양한 데이터베이스, 메시지 브로커, 웹 서버 등의 도커 이미지를 제공하며, 이를 사용하여 테스트 시나리오를 구축할 수 있습니다. 이를 통해 통합 테스트, 시스템 테스트, 종단 간 테스트 등을 쉽게 작성할 수 있습니다.

## REST API 테스트 작성 방법
### 1. 의존성 추가
우선 프로젝트의 의존성에 TestContainers 관련 모듈을 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 종속성을 추가합니다:

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.16.0</version>
    <scope>test</scope>
</dependency>
```

### 2. 도커 컨테이너 설정
테스트 클래스의 `@BeforeAll` 또는 `@BeforeEach` 메서드에서 TestContainers를 초기화하고 도커 컨테이너를 설정합니다. 예를 들어, PostgreSQL 데이터베이스를 사용하는 경우 다음과 같이 설정할 수 있습니다:

```java
import org.junit.jupiter.api.BeforeAll;
import org.testcontainers.containers.PostgreSQLContainer;

public class MyIntegrationTest {

    public static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:latest");

    @BeforeAll
    public static void setUp() {
        postgres.start();
        System.setProperty("spring.datasource.url", postgres.getJdbcUrl());
        System.setProperty("spring.datasource.username", postgres.getUsername());
        System.setProperty("spring.datasource.password", postgres.getPassword());
    }

    // 테스트 메서드 작성
}
```

### 3. REST API 테스트 작성
테스트 메서드에서는 TestContainers에서 제공하는 도커 컨테이너를 사용하여 REST API를 테스트할 수 있습니다. 예를 들어, Spring Boot 애플리케이션의 `/users` 엔드포인트를 테스트하는 코드는 다음과 같습니다:

```java
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.ResponseEntity;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class MyIntegrationTest {

    private final TestRestTemplate restTemplate = new TestRestTemplate();

    @Test
    public void testGetUsers() {
        ResponseEntity<String> response = restTemplate.getForEntity("/users", String.class);
        // Assertions or validations
    }

    // 다른 테스트 메서드 작성
}
```

본 예시 코드에서는 TestRestTemplate를 사용하여 /users 엔드포인트에 GET 요청을 보내고 응답을 검증합니다. 이 외에도 다양한 방법으로 REST API를 테스트할 수 있으며, 필요에 따라 다른 테스트 코드를 작성할 수 있습니다.

## 결론
TestContainers를 사용하여 도커 컨테이너를 활용한 REST API 테스트를 작성하는 방법을 알아보았습니다. 이를 통해 좀 더 신뢰성 있고 안정적인 테스트를 작성할 수 있으며, 실제 환경과 유사한 테스트 환경을 구축할 수 있습니다. 자세한 내용은 [TestContainers 공식 문서](https://www.testcontainers.org/)를 참조하시기 바랍니다.