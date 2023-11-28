---
layout: post
title: "[java] ActiveMQ와 Java Messaging Service (JMS)"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Message-oriented middleware(MOM)는 다양한 애플리케이션 간에 비동기적으로 메시지를 교환하기 위한 중간 계층입니다. MOM을 사용하면 시스템 구성 요소 간의 결합도를 줄이고, 송신자와 수신자 간의 상호 작용을 향상시킬 수 있습니다.

ActiveMQ는 MOM의 일종으로, Apache Software Foundation에서 개발된 오픈 소스 메시징 브로커입니다. JMS(Java Messaging Service)는 Java에서 메시지를 생성, 송신 및 수신하기 위한 API를 제공하는 표준 명세입니다. ActiveMQ는 JMS를 구현하는 브로커로서, Java 애플리케이션과의 통합에 적합한 선택지입니다.

## ActiveMQ의 주요 기능

ActiveMQ는 다음과 같은 주요 기능을 제공합니다.

1. 다양한 프로토콜 지원: ActiveMQ는 다양한 프로토콜을 지원하며, JMS, AMQP, MQTT 등 다양한 프로토콜 간의 브리지 역할을 할 수 있습니다.
2. 클러스터링: ActiveMQ는 클러스터링을 지원하여 고가용성과 확장성을 제공합니다. 여러 대의 브로커로 구성된 클러스터를 사용하여 데이터의 안정성과 성능을 향상시킬 수 있습니다.
3. 메시지 필터링: ActiveMQ는 메시지를 필터링하는 기능을 제공합니다. 원하는 메시지만 수신하고 처리하도록 설정할 수 있습니다.
4. 트랜잭션 관리: ActiveMQ는 메시지 전송과 처리를 트랜잭션 단위로 관리할 수 있습니다. 메시지의 송신, 수신 및 처리를 아토믹하게 관리할 수 있습니다.
5. 메시지 마븐(Maven) 플러그인: ActiveMQ는 메시지를 마븐(Maven)을 사용하여 빌드 및 배포할 수 있도록하는 플러그인을 제공합니다.

## ActiveMQ 사용 예제

다음은 ActiveMQ를 사용하여 메시지를 보내고 받는 간단한 Java 예제입니다.

```java
import javax.jms.Connection;
import javax.jms.ConnectionFactory;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageProducer;
import javax.jms.Queue;
import javax.jms.Session;
import org.apache.activemq.ActiveMQConnectionFactory;

public class ActiveMQExample {
    public static void main(String[] args) {
        try {
            // ConnectionFactory 생성
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://localhost:61616");

            // Connection 생성
            Connection connection = connectionFactory.createConnection();

            // Session 생성
            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

            // Queue 생성
            Queue queue = session.createQueue("myQueue");

            // MessageProducer 생성
            MessageProducer producer = session.createProducer(queue);

            // Message 생성
            Message message = session.createTextMessage("Hello, ActiveMQ!");

            // Message 전송
            producer.send(message);

            // MessageConsumer 생성
            MessageConsumer consumer = session.createConsumer(queue);

            // Message 수신
            Message receivedMessage = consumer.receive();

            // 수신한 메시지 출력
            System.out.println("Received message: " + ((TextMessage) receivedMessage).getText());

            // 연결 종료
            session.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제는 ActiveMQ와 JMS를 사용하여 간단한 메시지 전송 및 수신을 수행하는 Java 애플리케이션입니다. 예제에서는 ActiveMQ에 연결하고, 메시지를 생성하여 보내고, 다시 받아오는 과정을 단계별로 수행합니다.

## 결론

ActiveMQ는 JMS를 구현하는 강력한 메시징 브로커로서, Java 애플리케이션과의 통합을 쉽게 할 수 있습니다. ActiveMQ의 다양한 기능과 간편한 사용법을 통해 비동기적인 메시지 교환을 구현할 수 있습니다.

참조:
- [Apache ActiveMQ](https://activemq.apache.org/)
- [Java Messaging Service (JMS)](https://www.oracle.com/java/technologies/java-message-service.html)