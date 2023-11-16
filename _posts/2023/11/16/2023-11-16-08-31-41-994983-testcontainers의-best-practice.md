---
layout: post
title: "[java] TestContainers의 Best Practice"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers는 개발 및 테스트 환경에서 독립적인 컨테이너를 사용하여 통합 테스트를 간편하게 수행할 수 있는 도구입니다. 이 글에서는 TestContainers를 사용할 때 따라야 할 Best Practice에 대해 알아보겠습니다.

## 1. 컨테이너 종료하기

테스트를 수행한 후에는 TestContainers에서 사용한 컨테이너를 명시적으로 종료해야 합니다. 이를 위해서는 `@AfterAll` 어노테이션을 사용하여 테스트 클래스가 종료될 때 컨테이너를 종료하는 메소드를 작성해야 합니다.

```java
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.PostgreSQLContainer;

public class MyTest {
    private static PostgreSQLContainer<?> container = new PostgreSQLContainer<>("postgres:latest");

    @Test
    public void myTest() {
        // 테스트 내용 작성
    }

    @AfterAll
    public static void cleanUp() {
        container.stop();
    }
}
```

## 2. 리소스 관리

TestContainers는 실제로 도커 컨테이너를 실행하여 테스트를 수행하기 때문에 많은 리소스를 사용할 수 있습니다. 이를 최적화하기 위해 테스트 클래스의 실행 범위를 제한하거나, 여러 테스트 클래스에서 사용하는 경우에는 컨테이너를 공유하는 것이 좋습니다.

```java
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.PostgreSQLContainer;

public class MyTest {
    private static PostgreSQLContainer<?> container;

    @BeforeAll
    public static void setUp() {
        container = new PostgreSQLContainer<>("postgres:latest");
        container.start();
    }

    @Test
    public void myTest() {
        // 테스트 내용 작성
    }

    @AfterAll
    public static void cleanUp() {
        container.stop();
    }
}
```

## 3. 컨테이너 재사용

컨테이너를 매번 새로 생성하고 시작하는 것은 비효율적일 수 있습니다. 따라서 `@TestInstance(Lifecycle.PER_CLASS)` 어노테이션을 사용하여 테스트 클래스 단위로 컨테이너를 재사용하는 것이 좋습니다.

```java
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.testcontainers.containers.PostgreSQLContainer;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class MyTest {
    private PostgreSQLContainer<?> container;

    @BeforeAll
    public void setUp() {
        container = new PostgreSQLContainer<>("postgres:latest");
        container.start();
    }

    @Test
    public void myTest() {
        // 테스트 내용 작성
    }

    @AfterAll
    public void cleanUp() {
        container.stop();
    }
}
```

## 참고 자료

- [TestContainers 공식 문서](https://www.testcontainers.org/)