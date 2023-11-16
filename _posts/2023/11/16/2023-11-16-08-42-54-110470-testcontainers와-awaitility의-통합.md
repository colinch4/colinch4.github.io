---
layout: post
title: "[java] TestContainers와 Awaitility의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers와 Awaitility는 테스트 코드 작성을 더욱 쉽고 간편하게 만들어주는 라이브러리입니다. TestContainers는 도커를 사용하여 테스트 환경을 구축하고 관리할 수 있게 해주며, Awaitility는 비동기 처리 테스트를 보다 쉽게 작성할 수 있도록 지원해줍니다.

이 블로그에서는 TestContainers와 Awaitility를 함께 사용하는 방법에 대해 알아보겠습니다.

## 1. 의존성 추가하기

먼저, Maven 또는 Gradle 프로젝트에 TestContainers와 Awaitility 의존성을 추가해야 합니다. 다음은 Maven 프로젝트의 `pom.xml` 파일에 의존성을 추가하는 예시입니다.

```xml
<dependency>
   <groupId>org.testcontainers</groupId>
   <artifactId>testcontainers</artifactId>
   <version>1.15.3</version>
   <scope>test</scope>
</dependency>

<dependency>
   <groupId>org.awaitility</groupId>
   <artifactId>awaitility</artifactId>
   <version>4.0.3</version>
   <scope>test</scope>
</dependency>
```

Gradle 프로젝트를 사용하는 경우는 `build.gradle` 파일에 다음과 같이 의존성을 추가합니다.

```groovy
testImplementation 'org.testcontainers:testcontainers:1.15.3'
testImplementation 'org.awaitility:awaitility:4.0.3'
```

## 2. TestContainers를 이용한 도커 컨테이너 구성

TestContainers를 사용하여 도커 컨테이너를 구성합니다. 예를 들어, MySQL 데이터베이스를 사용하는 테스트를 작성한다고 가정해봅시다.

```java
import org.junit.ClassRule;
import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.containers.wait.strategy.Wait;

public class MyTest {

    @ClassRule
    public static MySQLContainer mysql = new MySQLContainer<>()
            .withUsername("test")
            .withPassword("test")
            .withDatabaseName("test")
            .waitingFor(Wait.forHealthcheck());

    // 테스트 코드 작성
}
```

위의 코드에서 `@ClassRule`을 사용하여 MySQLContainer를 정의하고 컨테이너를 시작합니다. `withUsername()`, `withPassword()`, `withDatabaseName()`과 같은 메소드를 사용하여 컨테이너를 구성하고, `waitingFor()`를 호출하여 컨테이너의 준비상태를 확인합니다.

## 3. Awaitility를 이용한 비동기 테스트

Awaitility를 사용하여 비동기 테스트를 작성해봅시다. 예를 들어, 비동기로 작업을 수행하는 메소드가 있는 클래스가 있다고 가정해봅시다.

```java
public class MyClass {

    public CompletableFuture<String> doAsyncTask() {
        return CompletableFuture.supplyAsync(() -> {
            // 비동기 작업 수행
            return "Completed";
        });
    }
}
```

이제 Awaitility를 사용하여 `doAsyncTask()` 메소드의 결과가 "Completed"가 되기를 기다리는 테스트 코드를 작성해보겠습니다.

```java
import static org.awaitility.Awaitility.await;
import static org.hamcrest.Matchers.equalTo;

public class MyTest {

    @Test
    public void testAsyncTask() {
        MyClass myClass = new MyClass();

        CompletableFuture<String> futureResult = myClass.doAsyncTask();

        await().until(() -> futureResult.join(), equalTo("Completed"));
    }
}
```

위의 코드에서 `await().until()` 메소드를 사용하여 `futureResult`가 "Completed"가 될 때까지 기다립니다. 

## 결론

TestContainers를 이용하여 도커 컨테이너를 구성하고, Awaitility를 이용하여 비동기 테스트를 작성하는 방법을 알아보았습니다. 이제 TestContainers와 Awaitility를 조합하여 편리하게 테스트 코드를 작성할 수 있게 되었습니다. 명확하고 안정적인 테스트 코드를 작성하여 애플리케이션의 품질을 높이는데 도움이 될 것입니다.

---

* [TestContainers GitHub](https://github.com/testcontainers/testcontainers-java)
* [Awaitility GitHub](https://github.com/awaitility/awaitility)