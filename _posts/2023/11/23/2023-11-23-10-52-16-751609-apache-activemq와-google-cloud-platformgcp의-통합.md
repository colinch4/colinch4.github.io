---
layout: post
title: "[java] Apache ActiveMQ와 Google Cloud Platform(GCP)의 통합"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Apache ActiveMQ는 대표적인 오픈 소스 메시지 브로커입니다. Google Cloud Platform(GCP)는 클라우드 컴퓨팅 서비스를 제공하는 플랫폼입니다. 이 두 가지 기술을 함께 사용하여 메시지 통신을 구현하고자 하는 경우, ActiveMQ를 GCP와 통합하는 방법에 대해 알아보겠습니다.

## 1. ActiveMQ 설치 및 구성

ActiveMQ를 사용하기 위해 먼저 설치와 구성을 진행해야 합니다. ActiveMQ의 공식 웹사이트에서 최신 버전의 ActiveMQ를 다운로드하고 설치합니다. 설치가 완료되면, ActiveMQ 구성 파일인 `activemq.xml`을 수정하여 필요한 설정을 추가합니다. 일반적으로는 호스트, 포트, 통신 프로토콜 등의 정보를 설정하게 됩니다.

## 2. GCP 프로젝트 설정

구글 클라우드 플랫폼을 사용하기 위해 GCP 프로젝트를 생성하고 설정해야 합니다. GCP 콘솔에 로그인하여 새로운 프로젝트를 생성한 후, 해당 프로젝트에서 클라우드 메시징 서비스를 활성화합니다.

## 3. ActiveMQ와 GCP 통합 구현

### 3.1 ActiveMQ Broker 설정

ActiveMQ Broker를 구성하여 GCP와 통합할 준비를 합니다. 먼저 `activemq.xml` 파일에서 GCP 연결 정보를 추가해야 합니다. GCP에서 생성한 인증 정보를 사용하여 GCP 연결 정보를 설정합니다.

```xml
<transportConnectors>
    <transportConnector name="openwire" uri="tcp://0.0.0.0:61616" />
    <transportConnector name="amqp" uri="amqp+ssl://0.0.0.0:5672" />
    <transportConnector name="mqtt" uri="mqtt+ssl://0.0.0.0:1883" />
    <transportConnector name="stomp" uri="stomp+ssl://0.0.0.0:61613" />
    <transportConnector name="ws" uri="ws://0.0.0.0:61614" />
</transportConnectors>

...

<plugins>
    <redeliveryPlugin fallbackToDeadLetter="true" sendToDlqIfMaxRetriesExceeded="true">
        <redeliveryPolicyMap>
            <redeliveryPolicyMap defaultEntry="5,5000">
                <redeliveryPolicy queue="*" maximumRedeliveries="5" redeliveryDelay="5000" />
            </redeliveryPolicyMap>
        </redeliveryPolicyMap>
    </redeliveryPlugin>
    <gcpPlugin serviceAccountKeyFile="/path/to/service/account/key.json" />
</plugins>
```

위의 예제는 ActiveMQ Broker의 연결 프로토콜 및 GCP 연결을 위한 설정을 보여줍니다. 여기서 `ws` 프로토콜은 웹 소켓 연결을 위한 것이며, 연결 프로토콜을 필요에 따라 추가하거나 제거할 수 있습니다.

### 3.2 GCP Pub/Sub 설정

GCP에서 사용할 Pub/Sub 서비스를 구성합니다. GCP 콘솔에서 새로운 토픽을 생성하고, 해당 토픽의 구독자를 추가합니다.

### 3.3 메시지 전송 및 수신

이제 ActiveMQ Broker와 GCP Pub/Sub을 통해 메시지를 전송하고 수신할 준비가 완료되었습니다. ActiveMQ Producer를 사용하여 메시지를 생성하고 GCP Pub/Sub에 전송하고, ActiveMQ Consumer를 활용하여 GCP Pub/Sub에서 메시지를 수신할 수 있습니다.

```java
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class Producer {
    public static void main(String[] args) {
        ConnectionFactory factory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = null;
        try {
            connection = factory.createConnection();
            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue("test-queue");
            MessageProducer producer = session.createProducer(destination);

            TextMessage message = session.createTextMessage("Hello, GCP Pub/Sub!");
            producer.send(message);

            System.out.println("Message sent successfully!");

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
    }
}
```

위의 예제는 ActiveMQ Producer의 간략한 예시입니다. 해당 예제에서는 ActiveMQ Broker에 연결하여 `test-queue`라는 큐에 메시지를 전송하는 과정을 보여줍니다.

```java
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;

public class Consumer {
    public static void main(String[] args) {
        ConnectionFactory factory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = null;
        try {
            connection = factory.createConnection();
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue("test-queue");
            MessageConsumer consumer = session.createConsumer(destination);

            Message message = consumer.receive();
            if (message instanceof TextMessage) {
                TextMessage textMessage = (TextMessage) message;
                System.out.println("Received message: " + textMessage.getText());
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
    }
}
```

위의 예제는 ActiveMQ Consumer의 간략한 예시입니다. `test-queue` 큐에서 메시지를 수신하여 출력하는 과정을 보여줍니다.

## 결론

본 포스트에서는 Apache ActiveMQ와 Google Cloud Platform(GCP)간의 통합에 대해 알아보았습니다. ActiveMQ 프로듀서와 컨슈머를 사용하여 GCP Pub/Sub과 연동하여 메시지 통신을 구현할 수 있습니다. 이를 통해 안정적이고 확장 가능한 메시지 통신 시스템을 구축할 수 있습니다.

---

## 참고 자료

- [Apache ActiveMQ](https://activemq.apache.org/)
- [Google Cloud Platform](https://cloud.google.com/)