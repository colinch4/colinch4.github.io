---
layout: post
title: "[java] TestContainers와 Gatling의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers와 Gatling은 모두 개발자들에게 테스트 환경을 구성하고 실행하는 데 도움을 주는 도구입니다. TestContainers은 컨테이너 기반의 테스트 환경을 관리하는 데 사용되고, Gatling은 성능 테스트를 위한 스트레스 테스팅 도구입니다. 이 두 도구를 함께 사용하여 효과적인 테스트 시나리오를 만들고 실행할 수 있습니다.

## TestContainers로 컨테이너 기반 테스트 환경 구성하기

TestContainers는 자바 기반의 도구로, 테스트를 위해 임시 Docker 컨테이너를 시작하고 관리하는 기능을 제공합니다. 이를 통해 테스트 환경을 쉽게 구성할 수 있습니다. 다음은 TestContainers를 사용하여 PostgreSQL 컨테이너를 시작하는 예제입니다.

```java
import org.testcontainers.containers.PostgreSQLContainer;

public class TestClass {
    
    private static final PostgreSQLContainer<?> postgresContainer = new PostgreSQLContainer<>("postgres:latest");
    
    @BeforeClass
    public static void setup() {
        postgresContainer.start();
        System.setProperty("DB_URL", postgresContainer.getJdbcUrl());
        System.setProperty("DB_USERNAME", postgresContainer.getUsername());
        System.setProperty("DB_PASSWORD", postgresContainer.getPassword());
    }
    
    @AfterClass
    public static void teardown() {
        postgresContainer.stop();
    }
    
    // 테스트 메소드들...
}
```

위 예제는 `@BeforeClass` 어노테이션을 사용하여 테스트 클래스에서 컨테이너를 시작하고, `@AfterClass` 어노테이션을 사용하여 테스트 종료 후 컨테이너를 중지합니다. PostgreSQL 컨테이너의 JDBC URL, 사용자 이름 및 비밀번호는 시스템 속성으로 설정됩니다.

## Gatling을 사용하여 성능 테스트 시나리오 작성하기

Gatling은 Scala 기반의 성능 테스팅 도구로, HTTP 요청을 시뮬레이션하여 시스템의 성능을 측정합니다. 다음은 간단한 Gatling 시나리오 예제입니다.

```scala
import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class SampleScenario extends Simulation {

    val httpProtocol = http
        .baseUrl("http://localhost:8080")
        
    val scn = scenario("Sample Scenario")
        .exec(http("request_1")
            .get("/api/users"))
        .pause(1 second)
        .exec(http("request_2")
            .post("/api/users")
            .body(StringBody("""{"username": "test", "password": "password"}""")))
        
    setUp(
        scn.inject(
            rampConcurrentUsers(0) to 10 during (10 seconds),
            constantConcurrentUsers(10) during (30 seconds)
        )
    ).protocols(httpProtocol)
}
```

위 예제는 `httpProtocol`과 `scn` 변수를 선언하여 HTTP 요청에 대한 설정과 시나리오를 작성합니다. `setUp` 메소드를 사용하여 동시 사용자 수를 조정하고, `protocols` 메소드를 사용하여 http 프로토콜 설정을 정의합니다.

## TestContainers와 Gatling 통합하기

TestContainers와 Gatling을 함께 사용하기 위해서는 TestContainers에서 시작된 컨테이너의 정보를 Gatling에서 사용할 수 있도록 전달해야 합니다. 이를 위해 TestContainers에서 제공하는 System Property를 사용하여 Gatling 시나리오에서 컨테이너 정보를 가져올 수 있습니다.

```scala
class SampleGatlingSimulation extends Simulation {
    
    val httpProtocol = http
        .baseUrl("http://localhost:8080")
        
    val scn = scenario("Sample Gatling Simulation")
        .exec(session => {
            val dbUrl = System.getProperty("DB_URL")
            val dbUsername = System.getProperty("DB_USERNAME")
            val dbPassword = System.getProperty("DB_PASSWORD")
            
            // 컨테이너 정보를 사용한 로직 처리
            
            session
        })
        .exec(http("request_1")
            .get("/api/users"))
        
    setUp(
        scn.inject(
            constantUsersPerSec(10) during (30 seconds)
        )
    ).protocols(httpProtocol)
}
```

위 예제는 Gatling 시나리오에서 TestContainers에서 설정한 시스템 속성을 가져와서 사용할 수 있도록 처리한 예시입니다. 컨테이너 정보를 사용한 로직 처리는 개발자의 요구사항에 따라 유동적으로 변경할 수 있습니다.

TestContainers와 Gatling의 통합을 통해 컨테이너 기반의 테스트 환경에서 성능 테스트를 쉽게 수행할 수 있으며, 이를 통해 효과적인 테스트와 성능 최적화를 진행할 수 있습니다.

## 참고 자료
- TestContainers 공식 문서: [https://www.testcontainers.org/](https://www.testcontainers.org/)
- Gatling 공식 문서: [https://gatling.io/](https://gatling.io/)