---
layout: post
title: "[java] TestContainers로 Elasticsearch 컨테이너를 시작하는 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Elasticsearch는 분산된 개발 환경을 시뮬레이션하거나 테스트하기 위해 컨테이너로 실행될 수 있습니다. 이를 위해 TestContainers라는 훌륭한 도구를 사용할 수 있습니다. 이번 블로그 포스트에서는 TestContainers를 사용하여 자바 애플리케이션에서 Elasticsearch 컨테이너를 시작하는 방법에 대해 알아보겠습니다.

## 1. TestContainers 의존성 추가

먼저, 자바 프로젝트에 TestContainers 의존성을 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음과 같이 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.15.0</version>
    <scope>test</scope>
</dependency>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 다음과 같이 의존성을 추가합니다:

```groovy
testImplementation 'org.testcontainers:testcontainers:1.15.0'
```

## 2. Elasticsearch 컨테이너 시작

이제 Elasticsearch 컨테이너를 시작하기 위해 `GenericContainer` 클래스를 사용할 수 있습니다. 다음은 자바 코드 예시입니다:

```java
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.utility.DockerImageName;

public class ElasticsearchTest {

    private static final int ELASTICSEARCH_PORT = 9200;

    @Rule
    public GenericContainer<?> elasticsearchContainer = new GenericContainer<>(DockerImageName.parse("docker.elastic.co/elasticsearch/elasticsearch:7.14.0"))
            .withExposedPorts(ELASTICSEARCH_PORT);

    @Test
    public void testElasticsearchContainer() {
        String elasticsearchHost = elasticsearchContainer.getContainerIpAddress();
        int elasticsearchMappedPort = elasticsearchContainer.getMappedPort(ELASTICSEARCH_PORT);

        // Elasticsearch 호스트 및 포트를 사용하여 코드 테스트 진행
        // ...
    }
}
```

위의 코드에서 `GenericContainer`를 사용하여 컨테이너를 만들고 Docker 이미지 이름을 전달합니다. 여기서는 Elasticsearch의 공식 Docker 이미지를 사용했습니다 (버전 7.14.0). `withExposedPorts` 메서드를 사용하여 컨테이너 내부의 포트를 호스트 시스템에 노출시킬 수 있습니다.

`@Rule` 애너테이션을 사용하여 `elasticsearchContainer`를 테스트 메서드의 일부로 설정합니다. 이렇게 하면 테스트 메서드 실행 전에 컨테이너가 시작되고 테스트가 끝나면 자동으로 중지됩니다.

테스트 메서드 내에서 컨테이너의 IP 주소 및 매핑된 포트를 가져와서 코드 테스트를 진행할 수 있습니다.

## 결론

TestContainers를 사용하여 Elasticsearch 컨테이너를 시작하는 방법에 대해 살펴보았습니다. 이를 통해 실제 Elasticsearch 환경과 유사한 개발 및 테스트 환경을 구축할 수 있습니다. TestContainers는 자체적으로 Docker를 관리하므로 환경 설치 및 관리에 따른 번거로움을 줄여줍니다.

더 자세한 정보는 [TestContainers 공식 문서](https://www.testcontainers.org/)를 참조하시기 바랍니다.