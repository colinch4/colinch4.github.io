---
layout: post
title: "[java] TestContainers로 Cassandra 컨테이너를 시작하는 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---
TestContainers는 자바 기반의 통합 테스트 프레임워크로, 테스트 환경에서 동적으로 컨테이너를 시작하고 관리할 수 있는 기능을 제공합니다. 이번 기사에서는 TestContainers를 사용하여 Cassandra 컨테이너를 시작하는 방법에 대해 알아보겠습니다.

## TestContainers란?
TestContainers는 테스트 환경에서 독립적이고 격리된 컨테이너를 자동으로 시작하고 관리하는 자바 라이브러리입니다. 테스트 시에 필요한 다양한 종류의 컨테이너를 손쉽게 사용할 수 있으며, 테스트 환경을 더 견고하게 만들어줍니다.

## Cassandra 컨테이너 시작하기
TestContainers를 사용하여 Cassandra 컨테이너를 시작하려면 아래의 단계를 따르세요:

1. `pom.xml` 파일에 TestContainers의 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>cassandra</artifactId>
    <version>1.15.0</version>
    <scope>test</scope>
</dependency>
```

2. 테스트 클래스에 다음과 같이 어노테이션을 추가합니다:

```java
import org.junit.jupiter.api.*;
import org.testcontainers.junit.jupiter.*;

@Testcontainers
public class CassandraContainerTest {

}
```

3. Cassandra 컨테이너를 시작하려면 `GenericContainer`를 사용하고 의존성을 설정해야 합니다. 테스트 클래스 내에 다음과 같이 코드를 추가합니다:

```java
@Container
public static final GenericContainer<?> cassandraContainer =
        new GenericContainer<>("cassandra:latest")
                .withExposedPorts(9042);
```

4. 이제 테스트 메서드를 작성하고 Cassandra 컨테이너에 연결하여 테스트를 수행할 수 있습니다:

```java
@Test
public void testCassandraContainer() {
    try (Cluster cluster = Cluster.builder()
            .addContactPoint(cassandraContainer.getContainerIpAddress())
            .withPort(cassandraContainer.getMappedPort(9042))
            .build()) {
        // Cassandra에 대한 테스트 로직을 작성합니다.
    }
}
```

위의 코드에서 `Cluster` 객체를 사용하여 Cassandra에 대한 연결을 설정하고 테스트를 수행할 수 있습니다.

## 결론
이제 TestContainers를 사용하여 Cassandra 컨테이너를 시작하는 방법을 알게 되었습니다. 테스트 환경에서 동적으로 컨테이너를 시작하고 관리하는 이러한 기능은 테스트의 견고성을 높이고 테스트 작업을 더욱 쉽게 만들어줍니다. TestContainers의 다양한 기능과 종류를 활용하여 자신의 테스트 환경을 보다 효율적으로 구성해보세요.