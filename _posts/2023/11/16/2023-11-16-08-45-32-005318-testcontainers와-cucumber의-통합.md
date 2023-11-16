---
layout: post
title: "[java] TestContainers와 Cucumber의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers와 Cucumber을 함께 사용하면 자바 기반의 테스트에서 더욱 강력한 테스트 환경을 구축할 수 있습니다. TestContainers는 도커 컨테이너를 사용하여 테스트를 실행할 수 있게 해주는 프레임워크이며, Cucumber는 행위 주도 개발(Behavior-Driven Development, BDD)을 위한 자바 기반의 테스트 도구입니다. 이번 글에서는 TestContainers와 Cucumber을 통합하여 효과적인 테스트 시나리오를 구현하는 방법에 대해 다루겠습니다.

## 1. TestContainers 소개

TestContainers는 도커를 사용하여 테스트 환경을 구축하는 것을 지원해주는 도구입니다. 테스트에 필요한 빠르고 일관된 환경을 구축하기 위해 테스트 메소드의 시작과 종료 시에 도커 컨테이너를 생성 및 삭제할 수 있습니다. 테스트 환경을 도커 컨테이너로 구성함으로써, 개발 환경과 실제 운영 환경이 비슷해지므로 실제 시나리오를 보다 잘 흉내낼 수 있습니다.

## 2. Cucumber 소개

Cucumber는 BDD 방법론을 기반으로 테스트를 작성하는 도구입니다. Cucumber는 테스트 시나리오를 자연어로 작성하고, 이를 기반으로 자바 코드로 변환해 실행합니다. 이러한 특징을 통해 비개발자도 테스트 코드를 이해하고 작성할 수 있어 협업과 의사소통이 원활해집니다.

## 3. TestContainers와 Cucumber 통합 방법

TestContainers와 Cucumber을 통합하여 사용하기 위해서는 다음과 같은 단계를 따라야 합니다.

### 3.1. 의존성 추가

먼저, 프로젝트의 의존성에 TestContainers와 Cucumber 관련 라이브러리를 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependencies>
  <!-- TestContainers -->
  <dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.15.3</version>
    <scope>test</scope>
  </dependency>
  
  <!-- Cucumber -->
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-java</artifactId>
    <version>6.8.0</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-junit</artifactId>
    <version>6.8.0</version>
    <scope>test</scope>
  </dependency>
</dependencies>
```

### 3.2. 테스트 클래스 작성

다음으로, TestContainers를 사용하여 도커 컨테이너를 생성하고 설정하는 테스트 클래스를 작성해야 합니다. 아래는 PostgreSQL 컨테이너를 사용하는 예시입니다.

```java
import org.junit.BeforeClass;
import org.junit.ClassRule;
import org.testcontainers.containers.PostgreSQLContainer;

public class DatabaseIntegrationTest {
  @ClassRule
  public static PostgreSQLContainer postgreSQLContainer = new PostgreSQLContainer("postgres:latest");

  @BeforeClass
  public static void setUp() {
    // 데이터베이스 초기화 등의 설정 작업 수행
  }

  // 테스트 메소드 작성
}
```

### 3.3. Cucumber 테스트 작성

마지막으로, Cucumber를 사용하여 테스트 시나리오를 작성하고 실행하는 테스트 클래스를 작성해야 합니다. 아래는 Cucumber를 사용한 예시입니다.

```java
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(features = "src/test/resources/features", glue = "com.example.steps")
public class CucumberIntegrationTest {
}
```

여기서 `features`는 Cucumber 테스트 시나리오 파일이 위치한 경로를 지정하고, `glue`는 Cucumber 스텝 정의 클래스들이 위치한 패키지를 지정합니다.

## 4. 결론

TestContainers와 Cucumber을 함께 사용함으로써 테스트 환경을 보다 쉽게 구축할 수 있고, 테스트 시나리오를 더욱 간결하게 작성할 수 있습니다. 이를 통해 개발팀과 비개발팀 간의 협업과 의사소통이 원활해지며, 품질 높은 소프트웨어를 개발할 수 있습니다.

## 5. 참고 자료

- TestContainers 공식 문서: [https://www.testcontainers.org/](https://www.testcontainers.org/)
- Cucumber 공식 문서: [https://cucumber.io/docs/cucumber/](https://cucumber.io/docs/cucumber/)