---
layout: post
title: "[java] TestContainers로 InfluxDB 컨테이너를 시작하는 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 블로그 포스트에서는 Java 언어와 TestContainers 프레임워크를 사용하여 InfluxDB 컨테이너를 시작하는 방법에 대해 알아보겠습니다.

## 1. 개요

TestContainers는 테스트 환경에서 독립적인 컨테이너를 시작하고 관리하는 데 사용할 수 있는 Java 라이브러리입니다. 우리는 TestContainers를 사용하여 테스트 환경에서 InfluxDB 컨테이너를 자동으로 시작하여 개발 및 테스트를 하기 위한 환경을 구성할 것입니다.

## 2. 의존성 추가

먼저, Maven 또는 Gradle 프로젝트에 TestContainers 의존성을 추가해야 합니다.

Maven:

```xml
<dependencies>
    <!-- other dependencies... -->
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>testcontainers</artifactId>
        <version>1.15.3</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

Gradle:

```groovy
dependencies {
    // other dependencies...
    testImplementation 'org.testcontainers:testcontainers:1.15.3'
}
```

## 3. InfluxDB 컨테이너 시작하기

이제 InfluxDB 컨테이너를 시작하는 코드를 작성해 보겠습니다. 

```java
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.utility.DockerImageName;

public class InfluxDBContainer {

    private static final DockerImageName INFLUXDB_IMAGE = DockerImageName.parse("influxdb:2.0.0");

    public static GenericContainer<?> startContainer() {
        GenericContainer<?> influxDBContainer = new GenericContainer<>(INFLUXDB_IMAGE)
                .withExposedPorts(8086) 
                .withEnv("INFLUXDB_DB", "mydb") 
                .withEnv("INFLUXDB_ADMIN_USER", "admin") 
                .withEnv("INFLUXDB_ADMIN_PASSWORD", "password");

        influxDBContainer.start();
        return influxDBContainer;
    }

    // 테스트 메소드 예시
    public void testMethod() {
        try (GenericContainer<?> container = startContainer()) {
            // InfluxDB 연결 및 테스트 로직
        }
    }
}
```

위의 코드는 InfluxDB의 2.0.0 버전을 사용하는 컨테이너를 시작하는 방법을 보여줍니다. `startContainer` 메소드는 InfluxDB 컨테이너를 시작하고 필요한 환경 변수를 설정한 뒤, 컨테이너를 반환합니다.

테스트 메소드에서는 `startContainer` 메소드를 사용하여 InfluxDB 컨테이너를 시작하고, 테스트 로직을 작성할 수 있습니다.

## 4. 결론

이 글에서는 TestContainers를 사용하여 Java 언어에서 InfluxDB 컨테이너를 시작하는 방법을 알아보았습니다. TestContainers는 테스트 환경에서 독립적인 컨테이너를 시작하고 관리하는 데 유용한 도구입니다. 이를 통해 개발 및 테스트를 더 효과적으로 진행할 수 있습니다.

더 자세한 정보는 [TestContainers 공식 문서](https://www.testcontainers.org/)를 참조하십시오.