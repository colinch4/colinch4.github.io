---
layout: post
title: "[java] Java Apache CXF와 AMQP(Advanced Message Queuing Protocol) 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Apache CXF는 Java에서 웹 서비스를 개발하기 위한 프레임워크입니다. AMQP(Advanced Message Queuing Protocol)는 메시지 큐잉을 위한 표준 프로토콜입니다. 이번 글에서는 Java Apache CXF와 AMQP를 통합하여 메시지 큐잉을 구현하는 방법에 대해 알아보겠습니다.

## 1. Apache CXF 설치

먼저, Apache CXF를 설치해야 합니다. 다음은 Apache CXF를 설치하는 방법입니다.

```bash
$ wget http://apache.mirror.cdnetworks.com/cxf/3.4.6/apache-cxf-3.4.6.tar.gz
$ tar -xzvf apache-cxf-3.4.6.tar.gz
$ cd apache-cxf-3.4.6
```

## 2. AMQP 라이브러리 추가

AMQP를 사용하기 위해 AMQP 라이브러리를 추가해야 합니다. 예를 들어, RabbitMQ를 사용한다면 다음과 같이 의존성을 추가할 수 있습니다.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
    <version>2.5.0</version>
</dependency>
```

## 3. AMQP 연결 설정

AMQP 연결을 설정하기 위해 `application.properties` 파일에 다음 설정을 추가해야 합니다.

```properties
spring.rabbitmq.host=your-rabbitmq-host
spring.rabbitmq.port=5672
spring.rabbitmq.username=username
spring.rabbitmq.password=password
```

## 4. Apache CXF와 AMQP 통합 예제

이제 Apache CXF와 AMQP를 통합한 예제를 살펴보겠습니다. 예를 들어, `HelloWorldService`라는 웹 서비스가 있고, 요청이 들어오면 해당 요청을 AMQP 큐에 전송하는 기능을 추가하려고 합니다.

```java
import org.springframework.amqp.core.AmqpTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.apache.cxf.helpers.IOUtils;

@Service
public class HelloWorldService {

    @Autowired
    private AmqpTemplate amqpTemplate;

    public String sayHello(String name) {
        String message = "Hello, " + name + "!";
        amqpTemplate.convertAndSend("helloQueue", message);
        return "Hello, " + name + "!";
    }
}
```

위 예제에서는 `AmqpTemplate`을 사용하여 AMQP 큐에 메시지를 전송하고 있습니다.

## 5. Apache CXF와 AMQP 통합 테스트

통합한 Apache CXF와 AMQP를 테스트해보기 위해 다음과 같은 테스트 코드를 작성할 수 있습니다.

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class HelloWorldServiceTest {

    @Autowired
    private HelloWorldService helloWorldService;

    @Test
    public void testSayHello() {
        String result = helloWorldService.sayHello("John");
        assertEquals("Hello, John!", result);
        // AMQP 큐에서 메시지 확인하는 로직 추가
    }
}
```

위 예제에서는 `HelloWorldService`를 주입받아 `sayHello()` 메서드를 호출하고, 반환값이 예상대로 나오는지를 테스트하고 있습니다. 또한, AMQP 큐에서 메시지를 확인하는 로직을 추가하여 정상적으로 메시지가 전송되었는지를 확인할 수 있습니다.

## 결론

이번 글에서는 Java Apache CXF와 AMQP 통합 방법에 대해 알아보았습니다. Apache CXF를 사용하여 웹 서비스를 개발하고, AMQP를 사용하여 메시지 큐잉을 구현할 수 있습니다. 이를 통해 서비스 간의 비동기 통신과 확장성을 개선하고, 안정적인 웹 서비스를 개발할 수 있습니다.

### 참고 자료

- [Apache CXF 공식 사이트](https://cxf.apache.org/)
- [RabbitMQ 공식 사이트](https://www.rabbitmq.com/)