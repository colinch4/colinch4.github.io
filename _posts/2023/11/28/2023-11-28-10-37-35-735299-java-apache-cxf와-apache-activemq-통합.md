---
layout: post
title: "[java] Java Apache CXF와 Apache ActiveMQ 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Apache CXF는 Java 기반 웹 서비스 개발을 위한 오픈 소스 프레임워크입니다. Apache ActiveMQ는 메시지 브로커로서, 메시지 큐 및 토픽을 통해 애플리케이션 간에 비동기적으로 통신할 수 있는 기능을 제공합니다.

이번 블로그 포스트에서는 Java 언어를 사용하여 Apache CXF와 Apache ActiveMQ를 통합하는 방법을 알아보겠습니다. 이를 통해 웹 서비스와 메시지 기반 통신을 결합하여 더욱 유연하고 신뢰성 높은 애플리케이션을 개발할 수 있습니다.

## 1. Maven 종속성 추가

먼저, 프로젝트에 필요한 종속성을 추가해야 합니다. Maven을 사용하고 있다면, `pom.xml` 파일에 다음과 같이 Apache CXF와 Apache ActiveMQ의 종속성을 추가하세요.

```xml
<dependencies>
    <!-- Apache CXF -->
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-frontend-jaxws</artifactId>
        <version>3.3.6</version>
    </dependency>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-transports-http</artifactId>
        <version>3.3.6</version>
    </dependency>

    <!-- Apache ActiveMQ -->
    <dependency>
        <groupId>org.apache.activemq</groupId>
        <artifactId>activemq-all</artifactId>
        <version>5.16.3</version>
    </dependency>
</dependencies>
```

## 2. Apache CXF 웹 서비스 구성

Apache CXF를 사용하여 웹 서비스를 개발합니다. 이를 위해 `HelloService`라는 간단한 예제 서비스를 생성해보겠습니다. 다음과 같이 `HelloService` 인터페이스와 해당 인터페이스를 구현하는 `HelloServiceImpl` 클래스를 작성합니다.

```java
public interface HelloService {
    String sayHello(String name);
}

public class HelloServiceImpl implements HelloService {
    @Override
    public String sayHello(String name) {
        return "Hello, " + name + "!";
    }
}
```

Apache CXF에서는 이러한 서비스를 노출하기 위해 `Endpoint.publish()` 메서드를 사용합니다. 다음은 `HelloService`를 웹 서비스로 노출하는 `WebServicePublisher` 클래스의 예입니다.

```java
import javax.xml.ws.Endpoint;

public class WebServicePublisher {
    public static void main(String[] args) {
        HelloService helloService = new HelloServiceImpl();
        String address = "http://localhost:8080/hello";

        Endpoint.publish(address, helloService);

        System.out.println("Web service is published at " + address);
    }
}
```

## 3. Apache ActiveMQ 메시지 큐 설정

이제 Apache ActiveMQ를 사용하여 메시지 큐를 설정해보겠습니다. 먼저, ActiveMQ를 시작하고 기본적인 설정을 마치세요. 그런 다음, 메시지를 송신하는 `MessageSender` 클래스와 메시지를 수신하는 `MessageReceiver` 클래스를 작성합니다.

```java
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class MessageSender {
    public static void main(String[] args) throws JMSException {
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = connectionFactory.createConnection();
        connection.start();

        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination destination = session.createQueue("helloQueue");

        MessageProducer producer = session.createProducer(destination);

        TextMessage message = session.createTextMessage();
        message.setText("Hello, World!");

        producer.send(message);

        session.close();
        connection.close();
    }
}

import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class MessageReceiver {
    public static void main(String[] args) throws JMSException {
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = connectionFactory.createConnection();
        connection.start();

        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination destination = session.createQueue("helloQueue");

        MessageConsumer consumer = session.createConsumer(destination);

        Message receivedMessage = consumer.receive();

        if (receivedMessage instanceof TextMessage) {
            TextMessage textMessage = (TextMessage) receivedMessage;
            System.out.println("Received message: " + textMessage.getText());
        }

        session.close();
        connection.close();
    }
}
```

## 4. CXF 서비스에서 메시지 수신

이제 Apache CXF 웹 서비스에서 메시지를 수신하여 처리하는 방법을 알아보겠습니다. `HelloServiceImpl` 클래스를 다음과 같이 수정하여 메시지를 수신하여 처리합니다.

```java
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class HelloServiceImpl implements HelloService {
    @Override
    public String sayHello(String name) {
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = null;

        try {
            connection = connectionFactory.createConnection();
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue("helloQueue");

            MessageConsumer consumer = session.createConsumer(destination);

            Message receivedMessage = consumer.receive();

            if (receivedMessage instanceof TextMessage) {
                TextMessage textMessage = (TextMessage) receivedMessage;
                String receivedName = textMessage.getText();
                return "Hello, " + receivedName + "!";
            }

            session.close();
        } catch (JMSException e) {
            e.printStackTrace();
        } finally {
            if (connection != null) {
                try {
                    connection.close();
                } catch (JMSException e) {
                    e.printStackTrace();
                }
            }
        }

        return null;
    }
}
```

이제 `WebServicePublisher` 클래스를 실행하고 웹 서비스에 접근하면, CXF 서비스에서 메시지를 수신하여 처리하는 것을 확인할 수 있습니다.

## 결론

이번 블로그 포스트에서는 Java Apache CXF와 Apache ActiveMQ를 통합하는 방법을 알아보았습니다. 이를 통해 웹 서비스와 메시지 기반 통신을 결합하여 더욱 유연하고 신뢰성 높은 애플리케이션을 개발할 수 있습니다.

더 자세한 내용은 [Apache CXF 문서](http://cxf.apache.org/docs/)와 [Apache ActiveMQ 문서](https://activemq.apache.org/documentation)를 참고하세요.