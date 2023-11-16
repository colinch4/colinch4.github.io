---
layout: post
title: "[java] JMS(Java Message Service)란 무엇인가?"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

JMS(Java Message Service)는 자바 기반의 메시징 시스템을 개발하기 위한 API(Application Programming Interface)입니다. 메시징 시스템은 시스템 간에 비동기적으로 통신하기 위한 방법으로 사용됩니다. JMS는 이러한 메시징 시스템을 보다 쉽게 구현하고 사용할 수 있도록 해 줍니다.

JMS는 다양한 형태의 메시지를 생성, 송신, 수신 및 처리하는 기능을 제공합니다. 메시지는 일반적으로 비즈니스 데이터, 이벤트 또는 명령과 같은 정보를 가지고 있습니다. 

JMS는 큐(Queue)와 주제(Topic) 두 가지 모델을 지원합니다. 큐 모델은 메시지를 보내는 쪽과 받는 쪽이 한 쌍으로 구성되어 있는 동기적인 메시징을 지원합니다. 주제 모델은 하나의 메시지를 여러 수신자가 동시에 받을 수 있는 비동기적인 메시징을 지원합니다.

JMS를 사용하면 응용 프로그램 간 데이터를 안전하고 신뢰성 있게 교환할 수 있으며, 다른 응용 프로그램의 상태나 작업 결과 등을 실시간으로 전달할 수 있습니다. 또한, JMS는 확장성이 좋고 유연한 아키텍처를 제공하여 다양한 통신 환경에 적용할 수 있습니다.

JMS는 여러 벤더가 제공하는 메시징 시스템과 연동할 수 있는 표준화된 인터페이스를 제공하기 때문에, 다양한 메시징 시스템을 쉽게 전환하거나 대체할 수 있는 장점도 있습니다.

## JMS의 주요 구성 요소

JMS에는 다음과 같은 주요 구성 요소가 있습니다:

1. **메시지(Message)**: 데이터를 전송하는 단위로서, 일련의 바이트로 구성됩니다.
2. **프로듀서(Producer)**: 메시지를 생성하고 송신하는 역할을 합니다.
3. **컨슈머(Consumer)**: 메시지를 받아들여 처리하는 역할을 합니다.
4. **큐(Queue)**: 한 프로듀서가 생성한 메시지를 한 컨슈머가 받는 구조로 구성된 메시지 대기열입니다.
5. **주제(Topic)**: 한 프로듀서가 생성한 메시지를 여러 컨슈머가 받을 수 있는 구조로 구성된 메시지 토픽입니다.
6. **커넥션(Connection)**: 메시지를 교환하기 위한 연결을 나타냅니다.

## JMS 사용 예시

다음은 JMS를 사용하여 메시징 시나리오를 구현하는 예시 코드입니다:

```java
import javax.jms.*;
import org.apache.activemq.ActiveMQConnectionFactory;

public class JmsExample {

  public static void main(String[] args) {
    try {
      // JMS 연결
      ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://localhost:61616");
      Connection connection = connectionFactory.createConnection();
      connection.start();

      // JMS 세션 생성
      Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

      // 메시지 큐 생성
      Queue queue = session.createQueue("myQueue");

      // 프로듀서 생성
      MessageProducer producer = session.createProducer(queue);
      TextMessage message = session.createTextMessage("Hello, JMS!");

      // 메시지 전송
      producer.send(message);
      System.out.println("Message sent successfully");

      // 컨슈머 생성
      MessageConsumer consumer = session.createConsumer(queue);

      // 메시지 수신
      Message receivedMessage = consumer.receive();
      String text = ((TextMessage) receivedMessage).getText();
      System.out.println("Received Message: " + text);

      // JMS 세션 및 연결 닫기
      session.close();
      connection.close();
    } catch (JMSException e) {
      e.printStackTrace();
    }
  }

}
```

위 예제는 Apache ActiveMQ를 사용하여 JMS를 구현한 예시입니다. 리눅스 환경에서 ActiveMQ 서버를 시작하고, 위 코드를 실행하면 메시지가 성공적으로 보내지고 수신됩니다.

## 결론

JMS는 자바 기반 메시징 시스템의 개발과 활용을 도와주는 API입니다. 메시지 기반의 비동기 통신을 통해 안전하고 신뢰성 있는 데이터 교환을 할 수 있으며, 다양한 통신 환경에 적용할 수 있습니다. JMS는 큐와 주제 모델을 지원하며, 다양한 벤더가 제공하는 메시징 시스템과의 연동을 위한 표준화된 인터페이스를 제공합니다.