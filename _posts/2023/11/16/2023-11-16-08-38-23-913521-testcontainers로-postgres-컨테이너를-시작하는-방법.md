---
layout: post
title: "[java] TestContainers로 Postgres 컨테이너를 시작하는 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers는 Java 기반의 통합 테스트 프레임워크로, 컨테이너화된 환경에서 테스트를 수행할 수 있게 해줍니다. 이번 글에서는 TestContainers를 사용하여 Postgres 컨테이너를 시작하는 방법에 대해 알아보겠습니다.

## 1. 의존성 추가

먼저, `pom.xml` 파일에 TestContainers 및 Postgres JDBC 드라이버의 의존성을 추가해야 합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>testcontainers</artifactId>
        <version>1.15.3</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>postgresql</artifactId>
        <version>1.15.3</version>
        <scope>test</scope>
    </dependency>
    <!-- additional dependencies -->
</dependencies>
```

## 2. 테스트 작성

이제 테스트 코드를 작성해보겠습니다. 다음은 TestContainers를 사용하여 Postgres 컨테이너를 시작하는 간단한 테스트입니다.

```java
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.PostgreSQLContainer;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import static org.junit.jupiter.api.Assertions.assertNotNull;

public class PostgresContainerTest {

    @Test
    public void testPostgresContainer() throws SQLException {
        try (PostgreSQLContainer<?> container = new PostgreSQLContainer<>("postgres:13")) {
            container.start();

            String jdbcUrl = container.getJdbcUrl();
            String username = container.getUsername();
            String password = container.getPassword();

            try (Connection connection = DriverManager.getConnection(jdbcUrl, username, password)) {
                assertNotNull(connection);
            }
        }
    }
}
```

위의 테스트 코드에서 `PostgreSQLContainer` 클래스를 사용하여 Postgres 컨테이너를 생성하고 시작합니다. 그런 다음, 컨테이너의 JDBC URL, 사용자 이름 및 비밀번호를 가져와서 실제로 연결을 수행합니다. 연결이 성공하는지 확인하기 위해 `assertNotNull` 메서드를 사용합니다.

## 3. 테스트 실행

테스트를 실행하려면 IDE 또는 빌드 도구를 사용할 수 있습니다. 위의 테스트 코드를 실행하면 TestContainers가 Postgres 컨테이너를 자동으로 다운로드하고 시작한 후에 테스트가 실행됩니다. 테스트가 완료된 후에는 컨테이너가 자동으로 종료됩니다.

## 결론

TestContainers를 사용하면 Postgres 컨테이너를 간단하게 시작할 수 있습니다. 이를 통해 테스트 환경을 컨테이너화하여 격리된 테스트를 실행할 수 있습니다. 자세한 내용은 [TestContainers 공식 문서](https://www.testcontainers.org/)를 참조하시기 바랍니다.