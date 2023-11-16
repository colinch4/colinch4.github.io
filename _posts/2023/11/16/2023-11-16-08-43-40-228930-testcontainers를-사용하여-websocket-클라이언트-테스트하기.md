---
layout: post
title: "[java] TestContainers를 사용하여 WebSocket 클라이언트 테스트하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 포스트에서는 TestContainers를 사용하여 Java 언어로 작성된 WebSocket 클라이언트를 테스트하는 방법에 대해 알아보겠습니다. WebSocket은 실시간 양방향 통신이 가능한 프로토콜이므로 클라이언트 테스트는 매우 중요합니다. TestContainers는 도커를 사용하여 운영 환경과 동일한 환경에서 테스트를 수행하는 도구입니다. 이를 통해 WebSocket 클라이언트의 신뢰성과 성능을 테스트할 수 있습니다.

## 1. TestContainers 소개

TestContainers는 테스트 환경을 구축할 때 도커 컨테이너를 사용하여 실제 운영 환경과 거의 동일한 환경을 제공하는 도구입니다. 테스트 도중에 도커를 사용하여 컨테이너를 실행하고, 테스트가 끝나면 컨테이너를 정리합니다. 이를 통해 테스트 환경의 일관성과 격리성을 유지할 수 있습니다.

## 2. WebSocket 클라이언트 테스트

WebSocket 클라이언트 테스트를 위해 TestContainers의 도커 컨테이너를 사용합니다. 아래는 WebSocket 클라이언트 테스트를 수행하는 예제 코드입니다.

```java
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.containers.wait.strategy.Wait;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import javax.websocket.ClientEndpoint;
import javax.websocket.CloseReason;
import javax.websocket.OnClose;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import java.net.URI;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;

@Testcontainers
public class WebSocketClientTest {

    @Container
    private static final GenericContainer<?> container = new GenericContainer<>("websocket-server:latest")
            .withExposedPorts(8080)
            .waitingFor(Wait.forListeningPort());

    @Test
    public void testWebSocketClient() throws Exception {
        URI serverUri = URI.create("ws://" + container.getContainerIpAddress() + ":" + container.getMappedPort(8080));

        TestClientEndpoint clientEndpoint = new TestClientEndpoint();
        Session session = clientEndpoint.connect(serverUri);

        CountDownLatch latch = new CountDownLatch(1);
        clientEndpoint.setLatch(latch);

        session.getBasicRemote().sendText("Hello, WebSocket Server!");

        latch.await(5, TimeUnit.SECONDS);

        session.close();
    }

    @ClientEndpoint
    public static class TestClientEndpoint {

        private CountDownLatch latch;

        public void setLatch(CountDownLatch latch) {
            this.latch = latch;
        }

        @OnOpen
        public void onOpen(Session session) {
            System.out.println("WebSocket session opened");
        }

        @OnMessage
        public void onMessage(Session session, String message) {
            System.out.println("Received message: " + message);
            latch.countDown();
        }

        @OnClose
        public void onClose(Session session, CloseReason reason) {
            System.out.println("WebSocket session closed");
        }
    }
}
```

위 예제 코드에서는 `websocket-server`라는 도커 이미지를 사용하여 WebSocket 서버를 실행하고 테스트합니다. 클라이언트는 `TestClientEndpoint` 클래스에서 정의된 WebSocket 이벤트 핸들러를 사용하여 서버에 연결하고 메시지를 보내고 받습니다. `CountDownLatch`를 사용하여 메시지 수신을 확인합니다.

## 3. 실행 및 결과 확인

위 예제 코드를 실행하기 전에 `websocket-server` 도커 이미지를 미리 빌드하고 로컬 레지스트리에 업로드해야 합니다. 그런 다음 테스트 코드를 실행하면 WebSocket 클라이언트가 서버에 연결되고 메시지를 주고 받는 것을 확인할 수 있습니다.

## 4. 결론

TestContainers를 사용하여 WebSocket 클라이언트 테스트를 수행하는 방법에 대해 알아보았습니다. 이를 통해 운영 환경과 동일한 환경에서 클라이언트를 테스트하고, 신뢰성과 성능을 확인할 수 있습니다. 테스트 환경을 도커 컨테이너로 구성함으로써 격리성과 일관성을 유지할 수 있습니다.