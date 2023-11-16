---
layout: post
title: "[java] TestContainers와 Liquibase의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 포스트에서는 TestContainers와 Liquibase를 사용하여 Java 애플리케이션의 테스트 데이터베이스를 관리하는 방법을 알아보겠습니다.

## TestContainers 소개

TestContainers는 도커 컨테이너를 사용하여 테스트 환경을 구성하는 도구입니다. 테스트할 때마다 실제 데이터베이스 서버를 실행하고 관리할 필요가 없으므로 테스트 케이스를 더 쉽게 작성할 수 있습니다.

TestContainers는 여러 종류의 데이터베이스에 대한 지원을 제공하며, 사용자가 테스트에 필요한 데이터베이스 종류와 버전을 선택할 수 있습니다.

## Liquibase 소개

Liquibase는 데이터베이스 스키마 관리 도구로, 데이터베이스의 구조를 변경하는 스키마 마이그레이션을 관리합니다. XML 또는 YAML 형식으로 변경 내용을 정의하고, Liquibase가 변경을 적용하고 롤백하는 작업을 수행합니다.

Liquibase는 데이터베이스의 스키마 변경 내역을 추적하므로, 여러 환경에서 일관된 스키마를 유지하고 버전 관리를 할 수 있습니다.

## TestContainers와 Liquibase 연동

TestContainers와 Liquibase를 함께 사용하면 테스트 환경에서 데이터베이스 스키마를 효과적으로 관리할 수 있습니다. 다음은 TestContainers와 Liquibase의 연동 방법입니다.

1. TestContainers를 사용하여 도커 컨테이너에서 데이터베이스 서버를 실행합니다.
2. Liquibase를 사용하여 스키마 변경 내용을 정의하고, TestContainers에서 실행 중인 데이터베이스에 적용합니다.
3. 테스트를 실행하면 동적으로 생성된 데이터베이스에 스키마 변경이 적용됩니다.

아래는 예시 코드입니다.

```java
public class DatabaseSetupTest {

  @ClassRule
  public static PostgreSQLContainer postgresContainer =
    new PostgreSQLContainer("postgres:11.1")
    .withDatabaseName("test")
    .withUsername("test")
    .withPassword("test");

  @BeforeClass
  public static void setup() {
    // TestContainers에서 실행 중인 데이터베이스에 Liquibase 적용
    Liquibase liquibase = new Liquibase(
      "changelog.xml",
      new ClassLoaderResourceAccessor(),
      new JdbcConnection(
        postgresContainer.getJdbcUrl(),
        postgresContainer.getUsername(),
        postgresContainer.getPassword()
      )
    );
    liquibase.update("");
  }

  @Test
  public void testDatabase() {
    // 테스트 로직 실행
  }
}
```

위의 예시 코드에서는 TestContainers를 사용하여 PostgreSQL 데이터베이스 서버를 실행하고, Liquibase로 정의된 변경 내용을 적용합니다. `@BeforeClass` 메소드에서 Liquibase 객체를 생성하고, 스키마 변경을 수행하는 `liquibase.update("")`를 호출합니다.

이제 `testDatabase()` 메소드에서는 테스트 케이스를 작성하면 됩니다. 이 메소드는 TestContainers에서 실행 중인 데이터베이스를 사용하여 테스트를 진행할 수 있습니다.

## 결론

TestContainers와 Liquibase를 통합하여 테스트 데이터베이스를 관리하는 것은 애플리케이션 개발과 테스트에 많은 도움이 됩니다. 이들 도구를 사용하면 테스트 환경을 더욱 효과적으로 구성하고, 스키마 관리를 간편하게 할 수 있습니다.

더 자세한 내용은 아래의 참고 자료를 확인해주세요.

- TestContainers GitHub 저장소: [링크](https://github.com/testcontainers/testcontainers-java)
- Liquibase 공식 문서: [링크](https://www.liquibase.org/documentation)

감사합니다.