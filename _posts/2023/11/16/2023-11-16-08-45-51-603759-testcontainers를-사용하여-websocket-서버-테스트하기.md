---
layout: post
title: "[java] TestContainers를 사용하여 WebSocket 서버 테스트하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers는 테스트 환경에서 독립적인 서비스를 실행하고 테스트하기위한 도구입니다. WebSocket 서버를 개발하고 테스트하는 경우 TestContainers를 사용하여 테스트 환경을 관리하고 WebSocket 클라이언트와 통신할 수 있습니다.

## TestContainers란?

TestContainers는 독립적인 컨테이너에서 통합 테스트를 실행할 수 있는 Java 라이브러리입니다. 테스트 환경을 신속하게 설정하고 종속성을 관리하며 독립적인 테스트 환경을 제공합니다.

## TestContainers를 사용하여 WebSocket 서버 테스트하기

1. TestContainers를 Maven 또는 Gradle 프로젝트에 추가합니다.

   ```xml
   <!-- Maven -->
   <dependency>
       <groupId>org.testcontainers</groupId>
       <artifactId>testcontainers</artifactId>
       <version>1.15.3</version>
       <scope>test</scope>
   </dependency>
   ```

   ```groovy
   // Gradle
   testImplementation 'org.testcontainers:testcontainers:1.15.3'
   ```

2. WebSocket 클라이언트와 통신하기 위해 `ClientEndpointConfig`를 구성합니다.

   ```java
   @ClientEndpoint
   public class WebSocketClientEndpoint {
   
       private Session session;
   
       @OnOpen
       public void onOpen(Session session) {
           this.session = session;
       }
   
       @OnMessage
       public void onMessage(String message) {
           // 메시지 수신 처리
       }
   
       @OnClose
       public void onClose(Session session, CloseReason closeReason) {
           // 연결 닫힘 처리
       }
   
       public void sendMessage(String message) {
           // 메시지 전송
           this.session.getBasicRemote().sendText(message);
       }
   }
   ```

3. TestContainers를 사용하여 테스트 환경을 구성합니다. 예를 들어, Docker 컨테이너에서 실행중인 WebSocket 서버와 연결하는 테스트를 구성합니다.

   ```java
   public class WebSocketServerTest {
   
       @ClassRule
       public static final WebSocketContainerResource SERVER_CONTAINER = new WebSocketContainerResource();
   
       @Test
       public void testWebSocketServer() throws Exception {
           ClientEndpointConfig clientConfig = ClientEndpointConfig.Builder.create()
                   .build();
   
           WebSocketContainer container = SERVER_CONTAINER.getWebSocketContainer();
           container.connectToServer(WebSocketClientEndpoint.class, clientConfig, new URI(SERVER_CONTAINER.getWebSocketServerUrl()));
   
           // 테스트 로직 실행
   
           container.close();
       }
   }
   ```

4. 테스트를 실행합니다. TestContainers는 Docker 컨테이너를 시작하고 WebSocket 클라이언트를 통해 서버와 상호 작용합니다.

## 결론

TestContainers를 사용하여 WebSocket 서버를 테스트하는 것은 손쉬운 작업입니다. TestContainers는 독립적인 테스트 환경을 제공하고 WebSocket 클라이언트와 통신할 수 있도록 지원합니다. 이를 통해 안정적이고 견고한 WebSocket 서버를 개발하고 테스트할 수 있습니다.

## 참고 자료

- [TestContainers 공식 문서](https://www.testcontainers.org/)