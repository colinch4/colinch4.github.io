---
layout: post
title: "[java] Apache ActiveMQ와 Spring Boot의 연동"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

이번 포스트에서는 Apache ActiveMQ와 Spring Boot를 연동하는 방법에 대해 알아보겠습니다. Apache ActiveMQ는 인기 있는 오픈 소스 메시징 브로커로, 메시징 기반의 시스템 아키텍처를 구축하는 데 사용됩니다. Spring Boot는 자바 기반의 웹 애플리케이션을 개발하기 위한 프레임워크로, 간편한 설정과 개발환경을 제공합니다.

## 1. Maven 의존성 추가하기

Apache ActiveMQ와 Spring Boot를 연동하기 위해, 먼저 Maven 프로젝트에 해당 의존성을 추가해야 합니다. `pom.xml` 파일에 다음 의존성을 추가하세요:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-activemq</artifactId>
</dependency>
```

위의 의존성은 Spring Boot와 Apache ActiveMQ를 사용하기 위한 핵심 라이브러리를 가져옵니다.

## 2. ActiveMQ 설정하기

Spring Boot 프로젝트에서 ActiveMQ를 사용하기 위해, `application.properties` 파일에 다음 설정을 추가하세요:

```properties
spring.activemq.broker-url=tcp://localhost:61616
spring.activemq.user=admin
spring.activemq.password=admin
```

위의 설정에서 `broker-url`은 ActiveMQ 브로커의 주소를 지정하고, `user`와 `password`는 브로커에 연결하기 위한 인증 정보를 설정합니다.

## 3. 메시지 전송하기

이제 Spring Boot 애플리케이션에서 메시지를 전송하는 방법에 대해 알아보겠습니다. 메시지 전송을 위해 `JmsTemplate`을 사용할 수 있습니다. 다음은 메시지를 전송하는 간단한 예제 코드입니다:

```java
import org.springframework.jms.core.JmsTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MessageSender {

    @Autowired
    private JmsTemplate jmsTemplate;

    public void sendMessage(String message) {
        jmsTemplate.convertAndSend("myQueue", message);
    }
}
```

위의 코드에서 `JmsTemplate`은 ActiveMQ를 사용하여 메시지를 보내는 데 사용됩니다. `sendMessage` 메소드에서는 `convertAndSend` 메소드를 호출하여 지정된 큐(`myQueue`)로 메시지를 전송합니다.

## 4. 메시지 수신하기

메시지를 수신하는 방법도 매우 간단합니다. 다음 예제는 `@JmsListener` 어노테이션을 사용하여 큐를 두고, 메시지를 수신하는 방법을 보여줍니다:

```java
import org.springframework.jms.annotation.JmsListener;
import org.springframework.stereotype.Component;

@Component
public class MessageReceiver {

    @JmsListener(destination = "myQueue")
    public void receiveMessage(String message) {
        System.out.println("Received message: " + message);
    }
}
```

위의 코드에서 `@JmsListener` 어노테이션은 `myQueue`라는 이름의 큐를 구독하고, 메시지를 수신하는 메소드를 지정합니다.

## 결론

이번 포스트에서는 Apache ActiveMQ와 Spring Boot의 연동 방법에 대해 알아보았습니다. ActiveMQ를 사용하여 메시지를 전송하고 수신하는 방법을 살펴보았습니다. 이를 통해 복잡한 시스템 아키텍처를 구축하고 메시징 기반의 통신을 쉽게 구현할 수 있습니다.

더 자세한 내용을 알고 싶다면, 아래 참고 문서를 참조해주세요:

- [Spring Boot 공식 문서](https://spring.io/projects/spring-boot)
- [Apache ActiveMQ 공식 문서](https://activemq.apache.org/)
- [Spring JMS 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#jms)