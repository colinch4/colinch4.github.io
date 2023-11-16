---
layout: post
title: "[java] TestContainers와 Spring Cloud의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

## 소개

TestContainers는 컨테이너화된 환경에서의 테스트를 쉽게 작성할 수 있도록 도와주는 도구입니다. 이 도구를 사용하면 테스트 시에 필요한 외부 의존성을 가지는 컨테이너를 프로그래밍적으로 시작 및 종료할 수 있습니다. Spring Cloud는 분산 시스템을 구축하기 위한 일련의 프레임워크입니다. 이러한 프레임워크들은 일반적으로 여러 개의 마이크로서비스로 구성되며, 각 서비스는 서로 다른 의존성을 가질 수 있습니다.

## 문제점

Spring Cloud와 TestContainers를 함께 사용할 때, 테스트 환경 내에서 동일한 컨테이너를 공유하는 작업이 필요한 경우에 문제가 발생할 수 있습니다. 예를 들어, 여러 테스트가 같은 데이터베이스 컨테이너를 사용하는 경우 각 테스트 사이에 데이터가 충돌할 수 있습니다.

## 해결책

TestContainers에서는 컨테이너를 재사용하기 위한 여러 전략들을 제공합니다. 이 중에서 Spring Cloud와의 통합을 위한 가장 일반적인 접근 방식은 "컨테이너 공유" 전략을 사용하는 것입니다. 이 방식은 여러 테스트가 같은 컨테이너를 공유하도록 하기 때문에 데이터 충돌 문제를 해결할 수 있습니다.

이를 위해서는 TestContainers의 `@Container` 어노테이션을 사용하여 컨테이너를 정의하고, Spring의 `@ContextConfiguration` 어노테이션을 함께 사용해야 합니다. `@Container` 어노테이션은 컨테이너를 관리하기 위한 빈을 생성하며, `@ContextConfiguration` 어노테이션은 Spring 컨텍스트를 정의합니다.

아래의 예제는 MariaDB 컨테이너를 사용하는 Spring Boot 테스트의 예시입니다.

```java
@RunWith(SpringRunner.class)
@SpringBootTest
@ContextConfiguration(initializers = {MariaDbContainerContextInitializer.class})
public class MyIntegrationTest {

    @Container
    public static MariaDbContainer mariaDbContainer = new MariaDbContainer();

    @Test
    public void testDatabaseConnection() {
        // MariaDB 컨테이너를 사용하여 데이터베이스 연결 테스트를 수행합니다.
    }
}
```

위의 예제에서 `MariaDbContainerContextInitializer`는 MariaDB 컨테이너를 시작 및 종료하기 위한 클래스입니다. 이 클래스의 이름은 자유롭게 변경할 수 있으며, `ApplicationContextInitializer<ConfigurableApplicationContext>`를 구현해야 합니다.

## 결론

TestContainers와 Spring Cloud를 함께 사용하면 테스트 시에 외부 컨테이너를 쉽게 관리하고, 데이터 충돌 문제를 해결할 수 있습니다. 테스트를 보다 안정적이고 효율적으로 작성할 수 있으며, 애플리케이션의 충돌 가능성을 최소화할 수 있습니다.

## 참고 자료

- [TestContainers Documentation](https://www.testcontainers.org/)
- [Spring Cloud Documentation](https://spring.io/projects/spring-cloud)