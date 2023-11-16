---
layout: post
title: "[java] TestContainers로 Grafana 컨테이너를 시작하는 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 블로그 포스트에서는 TestContainers를 사용하여 Grafana 컨테이너를 시작하는 방법에 대해 알아보겠습니다. Grafana는 대시보드 및 시각화 도구로 널리 사용되며, 개발 및 테스트 환경에서의 사용을 쉽게하도록 TestContainers를 활용할 수 있습니다.

## TestContainers란?

TestContainers는 테스트용 컨테이너 인스턴스를 동적으로 생성하고 관리하는 도구입니다. 이를 사용하면 테스트 환경에서 더 신속하고 격리된 테스트를 수행할 수 있습니다. TestContainers는 다양한 컨테이너화된 서비스와 통합되어 있으며, 사용하기 쉽고 강력한 API를 제공합니다.

## Grafana 컨테이너 시작하기

먼저, TestContainers를 Maven 또는 Gradle 프로젝트에 추가해야합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음 종속성을 추가하세요:

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.15.0</version>
    <scope>test</scope>
</dependency>
```

Gradle을 사용하는 경우 `build.gradle` 파일에 다음 종속성을 추가하세요:

```groovy
testImplementation 'org.testcontainers:testcontainers:1.15.0'
```

이제 Grafana 컨테이너를 시작하는 테스트를 작성해보겠습니다. 다음은 테스트 클래스의 예입니다.

```java
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.containers.wait.strategy.Wait;
import org.testcontainers.utility.DockerImageName;

public class GrafanaContainerTest {

    @Test
    public void testGrafanaContainer() {
        // Grafana Docker 이미지 정의
        DockerImageName grafanaImage = DockerImageName.parse("grafana/grafana:latest");

        // Grafana 컨테이너 시작
        GenericContainer<?> grafanaContainer = new GenericContainer<>(grafanaImage)
                .withExposedPorts(3000)
                .waitingFor(Wait.forHttp("/"));

        // Grafana URL 가져오기
        String grafanaUrl = "http://" + grafanaContainer.getHost() + ":" + grafanaContainer.getMappedPort(3000);

        // 테스트 코드 작성
        // ...

        // Grafana 컨테이너 종료
        grafanaContainer.stop();
    }
}
```

이 예제에서는 `grafana/grafana:latest` Docker 이미지를 사용하여 Grafana 컨테이너를 시작합니다. 컨테이너는 3000 포트를 노출하며 `/` 에서 HTTP 요청을 기다립니다. 그리고 컨테이너의 호스트 및 포트 정보를 사용하여 Grafana URL을 생성합니다.

테스트 코드를 작성한 후, 원하는 테스트 시나리오를 구현하면 됩니다. 테스트가 끝나면 Grafana 컨테이너를 종료합니다.

이제 TestContainers를 사용하여 Grafana 컨테이너를 시작하는 방법을 알게 되었습니다. 이를 활용하여 테스트 환경에서 Grafana를 쉽게 사용할 수 있습니다. 테스트 중에는 실제 Grafana 인스턴스를 사용하며 격리되어 있으므로 다른 테스트나 환경에 영향을 주지 않습니다.

## 참고 자료

- [TestContainers 공식 문서](https://www.testcontainers.org/)
- [Grafana 공식 웹사이트](https://grafana.com/)