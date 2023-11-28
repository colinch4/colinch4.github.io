---
layout: post
title: "[java] ActiveMQ Producer와 Consumer 생성하기"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

ActiveMQ는 오픈 소스의 메시지 브로커로, Java를 기반으로 하는 애플리케이션 간의 비동기적인 메시징을 제공합니다. 이번 포스트에서는 ActiveMQ Producer와 Consumer를 생성하는 방법에 대해 알아보겠습니다.

## 1. ActiveMQ 라이브러리 추가하기
ActiveMQ를 사용하기 위해서는 먼저 ActiveMQ 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.activemq</groupId>
    <artifactId>activemq-all</artifactId>
    <version>5.16.3</version>
</dependency>
```

Gradle을 사용하는 경우에는 `build.gradle` 파일에 다음 의존성을 추가합니다.

```groovy
implementation 'org.apache.activemq:activemq-all:5.16.3'
```

## 2. Producer 생성하기
ActiveMQ Producer를 생성하기 위해서는 `ConnectionFactory`와 `Connection` 객체를 생성해야 합니다. 그리고 `Session`과 `MessageProducer`를 통해 메시지를 전송할 수 있습니다. 아래는 Producer 생성 예제 코드입니다.

```java
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class Producer {
    public static void main(String[] args) {
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://localhost:61616");

        try {
            Connection connection = connectionFactory.createConnection();
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue("myQueue");

            MessageProducer producer = session.createProducer(destination);

            TextMessage message = session.createTextMessage();
            message.setText("Hello, ActiveMQ!");

            producer.send(message);

            session.close();
            connection.close();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `tcp://localhost:61616`을 `ConnectionFactory` 생성자에 전달하여 ActiveMQ와의 연결을 설정합니다. 그리고 `createConnection()` 메소드를 호출하여 `Connection` 객체를 얻은 후, `createSession()` 메소드를 호출하여 `Session` 객체를 생성합니다. 그리고 `createQueue()` 메소드를 통해 메시지를 전송할 대상 Queue를 생성합니다.

`MessageProducer` 객체를 생성한 후, `createTextMessage()` 메소드를 호출하여 `TextMessage` 객체를 생성하고, `setText()` 메소드를 통해 메시지를 설정합니다. 마지막으로 `send()` 메소드를 호출하여 메시지를 전송합니다.

## 3. Consumer 생성하기
ActiveMQ Consumer를 생성하기 위해서도 마찬가지로 `ConnectionFactory`와 `Connection` 객체를 생성해야 합니다. 그리고 `Session`과 `MessageConsumer`를 통해 메시지를 소비할 수 있습니다. 아래는 Consumer 생성 예제 코드입니다.

```java
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class Consumer {
    public static void main(String[] args) {
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://localhost:61616");

        try {
            Connection connection = connectionFactory.createConnection();
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue("myQueue");

            MessageConsumer consumer = session.createConsumer(destination);

            consumer.setMessageListener(message -> {
                if (message instanceof TextMessage) {
                    try {
                        TextMessage textMessage = (TextMessage) message;
                        String text = textMessage.getText();
                        System.out.println("Received message: " + text);
                    } catch (JMSException e) {
                        e.printStackTrace();
                    }
                }
            });

            Thread.sleep(3000);

            session.close();
            connection.close();
        } catch (JMSException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

Consumer 코드에서도 마찬가지로 ActiveMQ와의 연결을 설정한 후, `createConnection()` 메소드를 호출하여 `Connection` 객체를 얻고, `createSession()` 메소드를 호출하여 `Session` 객체를 생성합니다. 그리고 `createQueue()` 메소드를 통해 메시지를 수신할 Queue를 생성합니다.

`MessageConsumer` 객체를 생성한 후, `setMessageListener()` 메소드를 통해 메시지의 소비를 처리하는 로직을 작성합니다. 위의 예제에서는 `TextMessage`를 받아와서 메시지 내용을 출력하는 로직을 작성하였습니다.

Consumer는 비동기적으로 메시지를 수신하기 때문에 `Thread.sleep()`으로 메인 스레드를 적절히 대기시켜줘야 합니다.

## 결론
ActiveMQ를 사용하여 Producer와 Consumer를 생성하는 방법에 대해 알아보았습니다. Producer는 메시지를 생성하고 전송하는 역할을 하며, Consumer는 메시지를 수신하여 처리하는 역할을 합니다. 메시징을 통해 애플리케이션 간의 통신을 유연하고 확장 가능하게 만들 수 있습니다.

더 자세한 내용은 [ActiveMQ 공식 사이트](http://activemq.apache.org/)를 참조할 수 있습니다.