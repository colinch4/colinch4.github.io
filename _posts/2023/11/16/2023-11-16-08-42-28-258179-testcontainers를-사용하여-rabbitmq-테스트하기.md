---
layout: post
title: "[java] TestContainers를 사용하여 RabbitMQ 테스트하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

RabbitMQ는 대규모 분산 메시징 시스템을 구축하는 데 사용되는 오픈 소스 메시징 브로커입니다. RabbitMQ를 사용하여 애플리케이션을 개발할 때 테스트를 진행해야하는데, 이를 위해 TestContainers를 사용할 수 있습니다. TestContainers는 Docker 컨테이너를 사용하여 애플리케이션을 테스트하기 위한 환경을 구축할 수 있는 도구입니다.

## TestContainers 설정

1. Maven 또는 Gradle 프로젝트에 TestContainers 의존성을 추가합니다.

Maven:
```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>rabbitmq</artifactId>
    <version>1.16.0</version>
    <scope>test</scope>
</dependency>
```

Gradle:
```groovy
testImplementation("org.testcontainers:rabbitmq:1.16.0")
```

2. 테스트 클래스에서 `@Container` 어노테이션을 사용하여 RabbitMQ 컨테이너를 설정합니다.

```java
import org.junit.ClassRule;
import org.junit.Test;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.containers.RabbitMQContainer;

public class RabbitMQTest {

    @ClassRule
    public static RabbitMQContainer rabbitMQContainer = new RabbitMQContainer();

    @Test
    public void testPublishAndConsumeMessage() {
        // RabbitMQ 컨테이너를 사용하여 테스트 로직을 작성합니다.
    }
}
```

## RabbitMQ 테스트하기

위의 설정이 완료되면 RabbitMQ 컨테이너가 자동으로 시작됩니다. 이제 테스트 로직에서 RabbitMQ에 대한 작업을 수행할 수 있습니다.

```java
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import org.junit.ClassRule;
import org.junit.Test;
import org.testcontainers.containers.RabbitMQContainer;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

public class RabbitMQTest {

    @ClassRule
    public static RabbitMQContainer rabbitMQContainer = new RabbitMQContainer();

    @Test
    public void testPublishAndConsumeMessage() throws IOException, TimeoutException {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(rabbitMQContainer.getHost());
        factory.setPort(rabbitMQContainer.getMappedPort(RabbitMQContainer.RABBITMQ_AMQP_PORT));

        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {

            // 메시지 전송
            String queueName = "test-queue";
            channel.queueDeclare(queueName, false, false, false, null);
            String message = "Hello, RabbitMQ!";
            channel.basicPublish("", queueName, null, message.getBytes());
    
            // 메시지 수신
            channel.basicConsume(queueName, true, (consumerTag, delivery) -> {
                String receivedMessage = new String(delivery.getBody());
                System.out.println("Received message: " + receivedMessage);
            }, consumerTag -> {});
        }
    }
}
```

위의 코드에서는 RabbitMQ 컨테이너의 호스트 및 포트 정보를 가져와 ConnectionFactory를 설정한 후, 메시지를 전송하고 수신하는 작업을 진행합니다.

## 마무리

TestContainers를 사용하여 RabbitMQ를 테스트하는 방법을 알아보았습니다. 이를 통해 RabbitMQ를 사용하는 애플리케이션을 개발하고 테스트하는 데 더욱 편리하게 진행할 수 있습니다.

---

**참고 자료:**
- [RabbitMQ](https://www.rabbitmq.com/)
- [TestContainers](https://www.testcontainers.org/)