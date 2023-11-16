---
layout: post
title: "[java] TestContainers로 Apache Flink 애플리케이션 테스트하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Flink는 대규모 데이터 처리를 위한 분산 스트리밍 및 배치 처리 프레임워크입니다. 효율적인 애플리케이션을 작성하려면 테스트가 매우 중요합니다. 이때 TestContainers 라이브러리를 사용하여 Apache Flink 애플리케이션을 테스트해볼 수 있습니다.

## TestContainers란?

TestContainers는 테스트에 필요한 컨테이너화된 환경을 쉽게 구축할 수 있는 라이브러리입니다. 테스트에서 필요한 외부 리소스(예: 데이터베이스, 메시지 큐 등)를 실제 환경과 동일하게 구성해줍니다. 이를 통해 실제 프로덕션 환경과 유사한 테스트를 수행할 수 있습니다.

## Apache Flink 테스트 환경 설정

먼저, Maven 또는 Gradle을 사용하여 TestContainers와 Apache Flink를 프로젝트에 추가해야 합니다. 이는 프로젝트의 `pom.xml` 또는 `build.gradle` 파일에서 수행할 수 있습니다.

Maven을 사용하는 경우 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.15.3</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>flink</artifactId>
    <version>1.15.3</version>
    <scope>test</scope>
</dependency>
```

Gradle을 사용하는 경우 다음 종속성을 추가합니다:

```groovy
testImplementation 'org.testcontainers:testcontainers:1.15.3'
testImplementation 'org.testcontainers:flink:1.15.3'
```

## Apache Flink 테스트 작성

이제 TestContainers를 사용하여 Apache Flink 애플리케이션을 테스트하는 예제를 살펴보겠습니다.

```java
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.containers.Network;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

@Testcontainers
public class FlinkApplicationTest {

    @Container
    public static final Network network = Network.newNetwork();

    @Container
    public static final GenericContainer<?> flinkContainer = new GenericContainer<>("flink:1.15.3")
            .withNetwork(network);

    @Test
    public void testFlinkApplication() throws Exception {
        StreamExecutionEnvironment executionEnvironment = StreamExecutionEnvironment.getExecutionEnvironment();
        executionEnvironment.setParallelism(1);
        executionEnvironment.setRuntimeMode(executionEnvironment.getRuntimeMode());
        executionEnvironment.execute();
    }
}
```

위의 예제에서는 `org.testcontainers.junit.jupiter.Testcontainers` 어노테이션을 사용하여 Testcontainers를 초기화합니다. `@Container` 어노테이션을 사용하여 Apache Flink와 관련된 컨테이너를 설정합니다. `testFlinkApplication` 메서드는 Apache Flink 애플리케이션을 실행하는 데 사용됩니다.

## 테스트 실행

테스트를 실행하려면 IDE 또는 빌드 도구를 사용하면 됩니다. 일반적으로 `mvn test` 또는 `gradle test` 명령을 실행하여 테스트를 실행할 수 있습니다.

## 결론

TestContainers를 사용하면 Apache Flink 애플리케이션을 테스트하는 데 필요한 외부 리소스를 쉽게 구축할 수 있습니다. 이를 통해 실제 프로덕션 환경과 유사한 테스트를 수행하여 안정성과 성능을 향상시킬 수 있습니다.

## 참고 자료

- [TestContainers 공식 문서](https://www.testcontainers.org/)
- [Apache Flink 공식 홈페이지](https://flink.apache.org/)