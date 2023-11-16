---
layout: post
title: "[java] TestContainers로 WebFlux 애플리케이션 테스트하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers는 테스트 코드에서 Docker 컨테이너를 사용하여 환경을 구축하는 도구입니다. 이를 통해 WebFlux 애플리케이션을 테스트할 수 있습니다. 이번 블로그 포스트에서는 TestContainers를 사용하여 WebFlux 애플리케이션을 테스트하는 예제 코드를 다루고자 합니다.

## 1. 의존성 추가하기

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.15.3</version>
    <scope>test</scope>
</dependency>
```

TestContainers의 Maven 의존성을 프로젝트에 추가해야 합니다.

## 2. Testcontainers 구성하기

```java
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.containers.wait.strategy.Wait;
import org.testcontainers.utility.DockerImageName;

public abstract class AbstractContainerBaseTest {

    protected static GenericContainer<?> webFluxContainer;

    @BeforeAll
    public static void setupContainer() {
        webFluxContainer = new GenericContainer<>(DockerImageName.parse("openjdk:11-jdk-slim"))
                .withExposedPorts(8080)
                .waitingFor(Wait.forHttp("/").forStatusCode(200));
        webFluxContainer.start();
    }

    @AfterAll
    public static void tearDown() {
        webFluxContainer.stop();
    }
}
```

`AbstractContainerBaseTest` 클래스는 Testcontainers를 사용하여 Docker 컨테이너를 구성하는 클래스입니다. `BeforeAll` 어노테이션을 통해 테스트 실행 전에 컨테이너를 시작하고, `AfterAll` 어노테이션을 통해 테스트 실행 후 컨테이너를 중지합니다.

## 3. WebFlux 테스트 코드 작성하기

```java
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.reactive.function.client.WebClient;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import static org.assertj.core.api.Assertions.assertThat;

@Testcontainers
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.NONE)
public class WebFluxIntegrationTest extends AbstractContainerBaseTest {

    @Container
    private static final GenericContainer<?> webFluxContainer = webFluxContainer;

    @Test
    void testEndpoint() {
        WebClient client = WebClient.builder()
                .baseUrl("http://" + webFluxContainer.getHost() + ":" + webFluxContainer.getMappedPort(8080))
                .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .build();

        String response = client.get()
                .uri("/api/endpoint")
                .retrieve()
                .bodyToMono(String.class)
                .block();

        assertThat(response).isEqualTo("Hello, TestContainers!");
    }
}
```

위 코드에서는 Testcontainers의 `@Container` 어노테이션을 사용하여 `webFluxContainer`를 정의합니다. 이 컨테이너는 `AbstractContainerBaseTest`에서 구성한 Docker 컨테이너를 가져옵니다. 테스트 코드에서는 이 컨테이너의 호스트와 포트를 사용하여 `WebClient`를 생성하고, `/api/endpoint`로 GET 요청을 보냅니다. 응답을 받아서 예상한 결과와 일치하는지 확인합니다.

## 4. 테스트 실행하기

테스트를 실행하려면 JUnit을 실행하고 `WebFluxIntegrationTest` 클래스를 실행하면 됩니다.

```
$ mvn test
```

테스트가 실행되면 TestContainers가 Docker 컨테이너를 시작하고, 애플리케이션을 실행하여 테스트를 수행합니다.

## 결론

이번 포스트에서는 TestContainers를 사용하여 WebFlux 애플리케이션을 테스트하는 방법을 살펴보았습니다. 이를 통해 테스트 환경을 쉽게 구축하고, 독립적인 테스트를 수행할 수 있습니다. TestContainers는 다양한 데이터베이스나 메시지 큐 등에도 적용할 수 있으므로, 다양한 애플리케이션 레이어를 테스트하기에 유용한 도구입니다.

참고 자료:
- [TestContainers 공식 문서](https://www.testcontainers.org/)
- [Spring Boot 공식 문서](https://spring.io/projects/spring-boot)