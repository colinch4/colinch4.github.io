---
layout: post
title: "[java] Apache ActiveMQ와 Spring Framework 연동하기"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Apache ActiveMQ는 대표적인 메시지 브로커로, 복잡한 애플리케이션 간의 통신을 용이하게 도와줍니다. Spring Framework는 자바 기반의 애플리케이션을 개발할 때 사용되는 프레임워크로, 애플리케이션의 구성 요소들을 효과적으로 관리하고 통합할 수 있습니다. 이번 포스트에서는 Apache ActiveMQ와 Spring Framework를 연동하는 방법에 대해 알아보겠습니다.

## 1. Maven 종속성 추가

ActiveMQ와 Spring Framework를 연동하기 위해서는 먼저 Maven 프로젝트의 종속성에 다음과 같은 의존성을 추가해야 합니다.

```xml
<dependency>
    <groupId>org.apache.activemq</groupId>
    <artifactId>activemq-all</artifactId>
    <version>5.16.1</version>
</dependency>

<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jms</artifactId>
    <version>5.3.4</version>
</dependency>
```

## 2. Spring 설정 파일 작성

Spring Framework에서는 JMS(Java Message Service)를 사용하여 ActiveMQ와 통신할 수 있습니다. 따라서 Spring의 설정 파일에 다음과 같이 JMS 관련 빈을 설정해야 합니다.

```xml
<!-- ActiveMQ 브로커에 연결하기 위한 연결 팩토리 설정 -->
<bean id="connectionFactory" class="org.apache.activemq.ActiveMQConnectionFactory">
    <property name="brokerURL" value="tcp://localhost:61616"/>
</bean>

<!-- JMS를 사용하기 위한 템플릿 설정 -->
<bean id="jmsTemplate" class="org.springframework.jms.core.JmsTemplate">
    <property name="connectionFactory" ref="connectionFactory"/>
</bean>

<!-- 메시지 수신을 처리하는 리스너 설정 -->
<bean id="messageListener" class="com.example.MessageListener"/>

<!-- 메시지를 수신하기 위한 리스너 컨테이너 설정 -->
<bean id="messageListenerContainer" class="org.springframework.jms.listener.DefaultMessageListenerContainer">
    <property name="connectionFactory" ref="connectionFactory"/>
    <property name="destination" ref="queue"/>
    <property name="messageListener" ref="messageListener"/>
</bean>
```

위 설정에서 `brokerURL`은 ActiveMQ 브로커의 URL을 나타내며, `MessageListener`는 실제로 메시지를 수신하여 처리하는 리스너 클래스입니다.

## 3. 메시지 발송

ActiveMQ와 연동하여 메시지를 발송하려면 다음과 같은 코드를 사용할 수 있습니다.

```java
@Autowired
private JmsTemplate jmsTemplate;

public void sendMessage(String message) {
    jmsTemplate.convertAndSend("queue", message);
}
```

위 코드에서 `queue`는 메시지를 보낼 대상 큐의 이름입니다.

## 4. 메시지 수신

ActiveMQ로부터 메시지를 수신하려면 다음과 같은 코드를 사용할 수 있습니다.

```java
public class MessageListener implements MessageListener {

    @Override
    public void onMessage(Message message) {
        try {
            if (message instanceof TextMessage) {
                TextMessage textMessage = (TextMessage) message;
                String text = textMessage.getText();
                System.out.println("Received message: " + text);
            }
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}
```

위 코드에서는 `MessageListener` 인터페이스를 구현하여 `onMessage` 메소드를 재정의하여 메시지를 수신한 후 처리하는 로직을 작성합니다.

## 5. 실행 확인

위와 같이 ActiveMQ와 Spring Framework를 연동한 후, 메시지 발송과 수신을 간단히 구현하고 실행해보면, ActiveMQ를 통해 메시지가 정상적으로 발송 및 수신되는 것을 확인할 수 있습니다.

## 참고 자료

- [Apache ActiveMQ 공식 홈페이지](http://activemq.apache.org/)
- [Spring Framework 공식 홈페이지](https://spring.io/)

위 포스트에서는 Apache ActiveMQ와 Spring Framework를 연동하는 방법에 대해 알아보았습니다. 이를 통해 복잡한 애플리케이션 간의 메시지 통신을 용이하게 처리할 수 있습니다.