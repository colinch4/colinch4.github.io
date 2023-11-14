---
layout: post
title: "[java] Spring Framework를 사용하여 WebSocket을 이용한 채팅 서버 구현"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

## 개요
이번 글에서는 Spring Framework를 사용하여 WebSocket을 이용한 채팅 서버를 구현하는 방법에 대해 알아보겠습니다. WebSocket을 이용하면 실시간으로 메시지를 주고받을 수 있는 어플리케이션을 구현할 수 있습니다. Spring Framework는 WebSocket을 지원하기 위해 `spring-websocket` 모듈을 제공하고 있습니다.

## 환경 설정

### 프로젝트 생성
아래의 명령을 사용하여 Spring Boot 프로젝트를 생성합니다.
```
$ spring init --dependencies=websocket my-chat-app
```
생성한 프로젝트 디렉토리로 이동합니다.
```
$ cd my-chat-app
```

### 의존성 추가
`build.gradle` 파일에 아래의 의존성을 추가합니다.
```groovy
implementation 'org.springframework.boot:spring-boot-starter-websocket'
```

### WebSocket 구성
웹 소켓을 구성하기 위해 `WebSocketConfig` 클래스를 생성합니다.
```java
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {

    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(chatWebSocketHandler(), "/chat").setAllowedOrigins("*");
    }

    @Bean
    public WebSocketHandler chatWebSocketHandler() {
        return new ChatWebSocketHandler();
    }
}
```

### WebSocket 핸들러 구현
WebSocket 메시지를 처리하기 위한 핸들러를 구현합니다. `TextWebSocketHandler`를 상속받아 핸들러를 만들 수 있습니다.
```java
public class ChatWebSocketHandler extends TextWebSocketHandler {

    private final List<WebSocketSession> sessions = new CopyOnWriteArrayList<>();

    @Override
    public synchronized void afterConnectionEstablished(WebSocketSession session) throws Exception {
        sessions.add(session);
    }

    @Override
    public synchronized void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
        sessions.remove(session);
    }

    @Override
    protected synchronized void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
        for (WebSocketSession s : sessions) {
            s.sendMessage(message);
        }
    }
}
```
위의 코드에서는 연결이 성립되면 `afterConnectionEstablished` 메서드가 호출되어 세션을 저장하고, 연결이 종료되면 `afterConnectionClosed` 메서드가 호출되어 세션을 제거합니다. 그리고 `handleTextMessage` 메서드를 통해 메시지를 주고받습니다.

## 테스트
WebSocket에 대한 테스트를 진행하기 위해 간단한 채팅 웹 페이지를 만들어보겠습니다. `index.html` 파일을 생성하고 아래의 코드를 추가합니다.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Chat</title>
</head>
<body>
    <h1>Chat</h1>
    <div id="messages"></div>

    <form onsubmit="sendMessage(event)">
        <input type="text" id="messageInput" />
        <button type="submit">Send</button>
    </form>

    <script>
        const socket = new WebSocket("ws://localhost:8080/chat");
        socket.onmessage = function(event) {
            const message = document.createElement('p');
            message.textContent = event.data;
            document.querySelector('#messages').appendChild(message);
        };

        function sendMessage(event) {
            event.preventDefault();
            const messageInput = document.querySelector('#messageInput');
            socket.send(messageInput.value);
            messageInput.value = '';
        }
    </script>
</body>
</html>
```

프로젝트를 실행한 후 웹 브라우저에서 `http://localhost:8080`으로 접속하면 채팅 페이지가 나타납니다. 입력창에 메시지를 입력하고 Send 버튼을 클릭하면 메시지가 실시간으로 화면에 출력됩니다.

## 마무리
Spring Framework를 사용하여 WebSocket을 이용한 채팅 서버를 구현하는 방법에 대해 알아보았습니다. WebSocket을 이용하면 실시간으로 메시지를 주고받을 수 있는 채팅 어플리케이션을 개발할 수 있습니다.