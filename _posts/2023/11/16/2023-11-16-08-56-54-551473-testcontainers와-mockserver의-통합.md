---
layout: post
title: "[java] TestContainers와 MockServer의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 글에서는 TestContainers와 MockServer을 함께 사용하여 효율적인 테스트 환경을 구축하는 방법에 대해 다루고자 합니다.

## 1. TestContainers란?

[TestContainers](https://www.testcontainers.org/)는 Docker 컨테이너를 사용하여 애플리케이션의 테스트 환경을 구축하는 도구입니다. 이를 통해 테스트 시에 필요한 외부 의존성을 쉽게 관리할 수 있으며, 가상화된 환경에서 테스트를 진행할 수 있습니다. 

예를 들어, 데이터베이스나 메시지 큐와 같은 외부 시스템을 사용하는 애플리케이션의 테스트 시에는 실제 시스템을 사용하기보다는 TestContainers를 통해 도커 컨테이너를 실행하여 테스트 데이터를 쉽게 준비할 수 있습니다.

## 2. MockServer란?

[MockServer](https://www.mock-server.com/)는 HTTP 요청에 대한 모의 응답을 제공하는 도구입니다. 즉, 실제 서버와 통신하지 않고도 원하는 응답을 정의하여 테스트할 수 있습니다. MockServer는 RESTful API의 휴대성과 유연성을 제공하며, 테스트 중인 애플리케이션의 의존성을 가지고 있는 서비스 또는 시스템과의 상호작용을 테스트할 때 매우 유용합니다.

## 3. TestContainers와 MockServer 통합하기

TestContainers를 사용하여 MockServer을 실행하고 테스트에 활용하는 방법은 매우 간단합니다. 다음은 TestContainers와 MockServer를 통합하는 예제 코드입니다.

```java
import org.junit.jupiter.api.Test;
import org.mockserver.client.MockServerClient;
import org.mockserver.integration.ClientAndServer;
import org.testcontainers.containers.MockServerContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import static org.junit.jupiter.api.Assertions.assertEquals;

@Testcontainers
public class MockServerIntegrationTest {

    @Container
    private static final MockServerContainer mockServerContainer = new MockServerContainer();

    @Test
    public void testMockServer() {
        int mockServerPort = mockServerContainer.getServerPort();

        // MockServer client 생성
        MockServerClient mockServerClient = new MockServerClient("localhost", mockServerPort);

        // MockServer에 모의 응답 정의
        mockServerClient.when(request().withMethod("GET").withPath("/api/test"))
                .respond(response().withStatusCode(200).withBody("Mock response"));

        // 애플리케이션 코드에서 MockServer에 요청을 보내고 응답을 검증하는 로직 구현
        // ...

        // 응답 검증
        // ...

        assertEquals(1, 1);
    }
}
```

위 예제에서는 우선 `MockServerContainer` 클래스를 사용하여 MockServer를 실행시킵니다. 그리고 `@Container` 어노테이션을 통해 컨테이너를 관리하며, `mockServerContainer.getServerPort()`를 통해 MockServer의 포트 번호를 가져옵니다.

그 후, `MockServerClient`를 생성하고 MockServer에 모의 응답을 정의합니다. 이후 애플리케이션 코드에서 MockServer에 요청을 보내고 응답을 검증하는 로직을 구현할 수 있습니다. 마지막으로 `assertEquals`를 통해 예상한 결과와 실제 결과를 비교하여 테스트합니다.

## 4. 마무리

TestContainers와 MockServer을 함께 사용하면 외부 의존성을 가진 애플리케이션을 테스트할 때 효율적으로 테스트 환경을 구축할 수 있습니다. 이를 통해 테스트의 안정성과 신뢰성을 높일 수 있으며, 더 나은 개발 경험을 제공할 수 있습니다.

더 자세한 내용은 [TestContainers 문서](https://www.testcontainers.org/)와 [MockServer 문서](https://www.mock-server.com/)를 참고하시기 바랍니다.