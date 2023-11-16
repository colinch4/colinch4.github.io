---
layout: post
title: "[java] TestContainers로 Apache ZooKeeper 컨테이너를 시작하는 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache ZooKeeper는 분산 애플리케이션을 관리하기 위한 고성능 분산 코디네이션 서비스입니다. 이 서비스를 사용하여 애플리케이션을 개발하고 테스트하는 경우, 로컬 환경에서 ZooKeeper 컨테이너를 시작하는 것이 유용할 수 있습니다. TestContainers는 Docker를 사용하여 로컬 환경에서 컨테이너를 시작하는 데 도움을 줄 수 있는 Java 라이브러리입니다. 이번 글에서는 TestContainers를 사용하여 Apache ZooKeeper 컨테이너를 시작하는 방법에 대해 알아보겠습니다.

## 1. Maven 종속성 추가하기

먼저 Maven 프로젝트에 다음의 TestContainers 의존성을 추가해야 합니다.

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.15.2</version>
    <scope>test</scope>
</dependency>
```

## 2. 테스트 클래스 작성하기

다음으로, Apache ZooKeeper 컨테이너를 시작하는 테스트 클래스를 작성해야 합니다. 다음의 예제 코드를 참고해 주세요.

```java
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.utility.DockerImageName;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class ZooKeeperContainerTest {

    @Test
    public void testZooKeeperContainer() {
        try (GenericContainer<?> zookeeperContainer = new GenericContainer<>(DockerImageName.parse("confluentinc/cp-zookeeper:6.2.0"))) {
            zookeeperContainer.start();

            assertTrue(zookeeperContainer.isRunning());

            // ZooKeeper 컨테이너를 사용하여 테스트할 로직 추가
        }
    }
}
```

위의 코드에서는 `GenericContainer`를 사용하여 Apache ZooKeeper 컨테이너를 시작합니다. `DockerImageName.parse()`를 사용하여 컨테이너 이미지를 지정하고, `start()` 메서드를 호출하여 컨테이너를 시작합니다. `isRunning()` 메서드를 사용하여 컨테이너가 정상적으로 실행되는지 확인할 수 있습니다.

## 3. 테스트 실행하기

이제 테스트를 실행해 보세요. 테스트를 실행하면 TestContainers가 Docker를 사용하여 Apache ZooKeeper 컨테이너를 자동으로 시작하고, 테스트 코드 내에서 컨테이너를 사용할 수 있습니다.

## 결론

TestContainers를 사용하여 Apache ZooKeeper 컨테이너를 시작하는 방법에 대해 알아보았습니다. 이를 통해 로컬 환경에서 Apache ZooKeeper를 간편하게 테스트할 수 있습니다. TestContainers를 사용하면 다른 분산 시스템과의 통합 테스트 등에도 유용하게 활용할 수 있습니다.

## 참고 자료

- [TestContainers 공식 문서](https://www.testcontainers.org/)
- [Apache ZooKeeper 공식 사이트](https://zookeeper.apache.org/)
- [confluentinc/cp-zookeeper Docker 이미지](https://hub.docker.com/r/confluentinc/cp-zookeeper)