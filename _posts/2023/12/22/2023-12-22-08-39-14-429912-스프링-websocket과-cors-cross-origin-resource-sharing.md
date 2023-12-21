---
layout: post
title: "[스프링] 스프링 WebSocket과 CORS (Cross-Origin Resource Sharing)"
description: " "
date: 2023-12-22
tags: [스프링]
comments: true
share: true
---

웹소켓은 실시간으로 데이터를 주고 받을 수 있는 기술로, 실시간 채팅, 주식가격 모니터링 등에 활용됩니다. **스프링 프레임워크**를 사용하여 웹소켓을 구현할 때 CORS (Cross-Origin Resource Sharing) 문제가 발생할 수 있습니다. 이 문제를 해결하기 위해 **스프링**에서는 CORS를 다루는 방법을 제공하고 있습니다.

## 1. 스프링 웹소켓 설정

먼저, 스프링 웹소켓을 설정해야 합니다. 이를 위해 `@EnableWebSocketMessageBroker` 어노테이션을 사용하여 **웹소켓 메시지 브로커**를 활성화합니다. 예를 들어:

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    // 웹소켓 구성 코드
}
```

## 2. CORS 설정

**스프링**에서 CORS 문제를 해결하기 위해 `@CrossOrigin` 어노테이션을 활용할 수 있습니다. 이를 위해 **웹소켓 컨트롤러**에 `@CrossOrigin` 어노테이션을 추가합니다.

```java
@MessageMapping("/chat.sendMessage")
@SendTo("/topic/public")
@CrossOrigin
public ChatMessage sendMessage(@Payload ChatMessage chatMessage) {
    // 메시지 전송 코드
}
```

`@CrossOrigin` 어노테이션을 사용하면 **스프링**은 **웹소켓** 요청의 CORS를 자동으로 처리합니다.

## 3. CORS Filter 추가

또 다른 방법으로는 **CORS 필터**를 추가하는 것입니다. 이를 통해 보다 세밀한 **CORS** 제어가 가능하며, `WebMvcConfigurer`를 구현하여 **CORS 필터**를 추가할 수 있습니다. 

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins("http://호스트주소:포트번호");
    }
}
```

## 결론

웹소켓을 사용할 때 발생하는 **CORS** 문제는 **스프링**의 다양한 방법을 통해 해결할 수 있습니다. `@CrossOrigin` 어노테이션을 사용하거나 **CORS 필터**를 추가하여 **CORS** 문제를 효과적으로 다룰 수 있습니다.

*본 글은 스프링 프레임워크 5.3.x 기준으로 작성되었습니다.*

[참고 문서 - 스프링 공식문서](https://spring.io/guides/gs/messaging-stomp-websocket/)