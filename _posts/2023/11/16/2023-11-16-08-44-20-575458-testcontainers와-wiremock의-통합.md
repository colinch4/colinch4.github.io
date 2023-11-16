---
layout: post
title: "[java] TestContainers와 WireMock의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers는 자바 기반의 테스트 환경을 손쉽게 구축할 수 있는 도구입니다. WireMock은 HTTP API를 가상화하여 테스트하는데 사용되는 라이브러리입니다. 이번 포스트에서는 TestContainers와 WireMock을 통합하여 효과적으로 테스트 환경을 구축하는 방법을 알아보겠습니다.

## WireMock 소개

WireMock은 HTTP API를 가상화하여 테스트할 수 있는 라이브러리입니다. 실제로는 존재하지 않는 서비스의 응답을 모방하여 테스트를 수행할 수 있습니다. WireMock은 다양한 기능을 제공하며, 특히 요청에 대한 응답을 사전에 정의할 수 있어 테스트 시나리오를 쉽게 작성할 수 있습니다.

## TestContainers 소개

TestContainers는 Docker 컨테이너를 사용하여 테스트 환경을 구축하는 스켈레톤 코드를 제공하는 도구입니다. 테스트 코드 내에서 Docker 컨테이너를 시작하고, 필요한 서비스를 실행 및 설정하고, 테스트에 사용할 수 있습니다. 이를 통해 테스트 환경의 일관성을 유지하고, 외부 종속성에 의존하지 않는 테스트를 작성할 수 있습니다.

## TestContainers와 WireMock 통합

TestContainers는 WireMock을 지원하여 테스트 환경에서 WireMock을 사용할 수 있도록 합니다. WireMock을 통합하는 방법은 간단합니다.

1. TestContainers의 의존성을 추가합니다. (예: Gradle의 경우, `testImplementation 'org.testcontainers:testcontainers:1.15.3'`)
2. WireMock 컨테이너를 시작하는 코드를 작성합니다.

```java
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.containers.wait.strategy.Wait;
import org.testcontainers.images.builder.ImageFromDockerfile;
import org.testcontainers.utility.DockerImageName;

public class WireMockContainer extends GenericContainer<WireMockContainer> {

    public static final String DEFAULT_IMAGE_TAG = "2.30.1-alpine";

    public WireMockContainer() {
        super(DockerImageName.parse("rodoufu/wiremock:" + DEFAULT_IMAGE_TAG));
        withExposedPorts(8080);
        waitingFor(Wait.forHttp("/__admin").forPort(8080));
    }
}

public class MyWireMockTest {

    @Container
    public WireMockContainer wireMockContainer = new WireMockContainer();
    
    @Test
    public void testWireMockIntegration() {
        // WireMock의 URL 가져오기
        String wireMockUrl = wireMockContainer.getWireMockUrl();
        
        // 테스트 코드 작성
    }
}
```

위의 예시 코드에서는 `WireMockContainer` 클래스를 정의하여 WireMock 컨테이너를 시작합니다. `WireMockContainer`는 `GenericContainer`를 상속받으며, WireMock 서비스를 실행하고 8080 포트에 노출시킵니다. 또한, `/__admin` 경로에 대한 HTTP 요청을 기다리도록 설정합니다.

`MyWireMockTest` 클래스에서는 `@Container` 어노테이션을 사용하여 `WireMockContainer` 인스턴스를 생성하고, 테스트 메소드에서 WireMock의 URL을 가져와 테스트 코드를 작성할 수 있습니다.

## 결론

TestContainers와 WireMock을 통합하여 테스트 환경을 구축하는 방법에 대해 알아보았습니다. 이를 통해 더 간편하게 테스트 환경을 구성하고, 외부 종속성에 의존하지 않는 테스트를 작성할 수 있습니다. WireMock의 다양한 기능을 활용하여 테스트 시나리오를 쉽게 작성할 수 있으며, TestContainers를 통해 일관된 테스트 환경을 유지할 수 있습니다.

## 참고 자료
- [TestContainers 공식 문서](https://www.testcontainers.org/)
- [WireMock 공식 문서](http://wiremock.org/)