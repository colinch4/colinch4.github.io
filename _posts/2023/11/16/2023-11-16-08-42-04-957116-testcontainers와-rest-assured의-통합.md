---
layout: post
title: "[java] TestContainers와 REST Assured의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers는 도커를 사용하여 테스트 환경을 구축할 수 있는 도구입니다. REST Assured는 RESTful API를 테스트하기 위한 자동화된 테스트 프레임워크입니다. 이 두 가지 도구를 함께 사용하면 테스트 시나리오를 더 쉽게 작성하고 관리할 수 있습니다.

## TestContainers

TestContainers는 자바 기반의 테스트 환경을 위해 docker 컨테이너를 자동으로 관리하는 도구입니다. 테스트를 실행하기 전에 필요한 데이터베이스나 메시지 큐 등의 외부 환경을 컨테이너로 실행하고, 테스트 종료 후에는 컨테이너를 자동으로 정리해줍니다.

아래는 TestContainers의 사용 예시입니다.

```java
@Testcontainers
class MyTestClass {

    @Container
    private static final MySQLContainer<?> mysqlContainer = new MySQLContainer<>(DockerImageName.parse("mysql:latest"));
    
    @Container
    private static final GenericContainer<?> rabbitmqContainer = new GenericContainer<>(DockerImageName.parse("rabbitmq:latest"));

    @Test
    void myTestMethod() {
        // mysqlContainer 및 rabbitmqContainer를 사용하여 테스트 실행
    }
}
```

위의 예시에서는 MySQL 컨테이너와 RabbitMQ 컨테이너를 생성하여, `myTestMethod` 메소드에서 테스트에 활용할 수 있습니다.

## REST Assured

REST Assured는 RESTful API를 테스트하기 위한 자동화된 테스트 프레임워크입니다. HTTP 요청을 쉽게 생성하고 응답을 검증할 수 있는 강력한 기능을 제공합니다.

아래는 REST Assured를 사용하여 API를 테스트하는 예시입니다.

```java
@Test
void myApiTest() {
    given()
        .baseUri("https://api.example.com")
        .contentType(ContentType.JSON)
        .header("Authorization", "Bearer {token}")
    .when()
        .get("/users")
    .then()
        .statusCode(200)
        .body("size()", equalTo(3));
}
```

위의 예시에서는 `https://api.example.com` 주소로 GET 요청을 보내고, 응답으로 받은 결과를 검증합니다. `statusCode(200)`은 응답 상태 코드가 200이어야 함을 검증하고, `.body("size()", equalTo(3))`는 응답 결과 배열의 크기가 3이어야 함을 검증합니다.

## 통합

TestContainers와 REST Assured를 함께 사용하면, 외부 환경을 컨테이너로 실행하고 테스트 시나리오를 작성하여 API를 테스트할 수 있습니다.

아래는 TestContainers와 REST Assured를 통합하여 API 테스트를 하는 예시입니다.

```java
@Testcontainers
class MyApiTest {

    @Container
    private static final PostgreSQLContainer<?> postgresContainer = new PostgreSQLContainer<>(DockerImageName.parse("postgres:latest"));

    @BeforeAll
    static void setup() {
        // 테스트 전에 외부 환경 컨테이너를 실행하고 설정
        String jdbcUrl = postgresContainer.getJdbcUrl();
        Configuration.baseUrl = jdbcUrl;
        Configuration.username = postgresContainer.getUsername();
        Configuration.password = postgresContainer.getPassword();
    }

    @Test
    void getUsersTest() {
        given()
            .baseUri(Configuration.baseUrl)
            .contentType(ContentType.JSON)
        .when()
            .get("/users")
        .then()
            .statusCode(200)
            .body("size()", equalTo(3));
    }
}
```

위의 예시에서는 PostgreSQL 컨테이너를 생성하여, `setup` 메소드에서 API 테스트에 필요한 환경을 설정합니다. 그리고 `getUsersTest` 메소드에서는 TestContainers로 실행한 컨테이너와 REST Assured를 함께 이용하여 API 테스트를 수행합니다.

## 결론

TestContainers와 REST Assured를 통합하여 API 테스트 환경을 구축하면, 테스트 시나리오를 쉽게 작성하고 관리할 수 있습니다. 이를 통해 효율적인 QA 과정을 거쳐 안정적인 애플리케이션을 개발할 수 있습니다.

참고 문서:  
- [TestContainers 공식 문서](https://www.testcontainers.org/)
- [REST Assured 공식 문서](https://rest-assured.io/)