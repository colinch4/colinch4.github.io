---
layout: post
title: "[java] TestContainers를 사용하여 모의 객체(Mock Object)를 사용한 테스트 작성하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers는 모의 객체(Mock Object)를 사용하여 테스트를 작성하는 데 도움이 되는 유용한 도구입니다. 이 도구를 사용하면 실제 환경과 유사한 모의 환경을 만들어 테스트를 수행할 수 있습니다. 특히, 데이터베이스와 같은 외부 리소스와 상호작용하는 테스트를 작성할 때 매우 유용합니다.

## 1. TestContainers 설치

먼저, 프로젝트에 TestContainers를 설치해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음의 의존성을 추가합니다.

```xml
<dependency>
  <groupId>org.testcontainers</groupId>
  <artifactId>testcontainers</artifactId>
  <version>1.15.0</version>
  <scope>test</scope>
</dependency>
```

Gradle을 사용하는 경우 `build.gradle` 파일에 다음의 의존성을 추가합니다.

```groovy
testImplementation 'org.testcontainers:testcontainers:1.15.0'
```

## 2. 모의 환경 설정

테스트를 위해 모의 환경을 설정해야 합니다. 가장 일반적인 사례는 데이터베이스 모의 환경을 설정하는 것입니다. 예를 들어, H2 데이터베이스에서 작업하는 모의 테스트를 해보겠습니다.

```java
@Container
private static final PostgreSQLContainer postgres = new PostgreSQLContainer("postgres:latest");

@BeforeAll
static void setUp() {
    postgres.start();
    
    // 실제 환경에서 사용하는 데이터베이스 연결 정보
    String jdbcUrl = postgres.getJdbcUrl();
    String username = postgres.getUsername();
    String password = postgres.getPassword();
    
    // 모의 환경에서 테스트할 때 사용할 데이터베이스 연결 정보 설정
    Database.setJdbcUrl(jdbcUrl);
    Database.setUsername(username);
    Database.setPassword(password);
}

@AfterAll
static void tearDown() {
    postgres.stop();
}

@Test
void testDatabaseOperations() {
    // 모의 데이터베이스에 테스트 데이터 삽입
    Database.insertTestData("test");
    
    // 모의 데이터베이스에서 테스트 데이터 조회
    String data = Database.getTestData();
    
    Assert.assertEquals("test", data);
}
```

위의 예시에서는 H2 데이터베이스 대신 PostgreSQL 데이터베이스를 모의 환경으로 사용했습니다. `@Container` 어노테이션을 사용하여 테스트 컨테이너를 정의하고 `@BeforeAll`과 `@AfterAll` 어노테이션을 사용하여 컨테이너의 시작 및 종료를 관리합니다.

## 3. 테스트 작성

모의 환경이 설정되었으므로, 이제 실제로 테스트를 작성할 수 있습니다. 테스트 메서드에서는 모의 객체를 사용하여 테스트하고 싶은 동작을 호출합니다.

```java
@Test
void testSomething() {
    // 테스트 대상 객체 생성
    SomeClass someClass = new SomeClass();
    
    // 모의 객체로 대체
    SomeDependency mockDependency = mock(SomeDependency.class);
    someClass.setDependency(mockDependency);
    
    // 모의 객체의 동작 정의
    when(mockDependency.someMethod()).thenReturn("mocked result");
    
    // 테스트 대상 객체 호출
    String result = someClass.doSomething();
    
    // 결과 비교
    Assert.assertEquals("mocked result", result);
}
```

위의 예제에서는 `SomeClass`라는 테스트 대상 객체를 생성하고, `SomeDependency`라는 외부 의존성 객체를 모의 객체로 대체합니다. 모의 객체를 사용하여 `when()`을 통해 메서드 동작을 정의하고, 테스트 대상 객체를 호출한 결과를 비교하여 테스트를 수행합니다.

이와 같은 방식으로 TestContainers를 사용하여 모의 객체를 사용한 테스트를 작성할 수 있습니다. TestContainers의 다양한 기능을 활용하여 더 복잡한 모의 환경을 설정하고 테스트를 수행할 수도 있습니다. 더 자세한 내용은 [공식 문서](https://www.testcontainers.org/)를 참조하시기 바랍니다.