---
layout: post
title: "[java] Spring Framework를 이용한 메시지 큐(Messaging Queue) 구현"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

## 소개

메시지 큐는 애플리케이션 간 통신을 위해 사용되는 중간 역할을 하는 시스템입니다. 메시지 큐는 생산자(Producer)와 소비자(Consumer) 사이에서 비동기적으로 메시지를 주고받아 처리할 수 있도록 도와줍니다. 메시지 큐는 많은 양의 데이터를 안정적으로 처리하고, 시스템의 부하를 분산시킬 수 있는 장점이 있습니다.

이번 기술 블로그에서는 Spring Framework를 이용하여 메시지 큐를 구현하는 방법에 대해 알아보겠습니다.

## Spring Framework와 RabbitMQ

Spring Framework는 개발자들이 자바 기반의 애플리케이션을 더 효율적으로 개발할 수 있는 다양한 기능을 제공합니다. RabbitMQ는 Spring Framework에서 메시지 큐를 사용하기 위한 대표적인 오픈소스 솔루션입니다.

RabbitMQ는 AMQP(Advanced Message Queuing Protocol) 프로토콜을 기반으로하는 메시지 브로커로, 손쉬운 설치 및 설정, 강력한 기능 및 넓은 커뮤니티 지원으로 인기가 있습니다. Spring Framework는 RabbitMQ와의 통합을 제공하여 생산자 및 소비자를 쉽게 구현할 수 있도록 도와줍니다.

## Spring Boot 프로젝트 생성

먼저, Spring Boot 프로젝트를 생성해보겠습니다. Maven 또는 Gradle을 이용하여 Spring Boot 프로젝트를 생성할 수 있습니다.

```java
// Maven
mvn archetype:generate -DgroupId=com.example -DartifactId=message-queue-demo -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

// Gradle
gradle init --type java-application
```

## RabbitMQ 의존성 추가

생성된 Spring Boot 프로젝트에서는 `pom.xml` 또는 `build.gradle` 파일에 RabbitMQ 의존성을 추가해야 합니다.

### Maven

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

### Gradle

```groovy
implementation 'org.springframework.boot:spring-boot-starter-amqp'
```

## 메시지 큐 생성 및 구성

RabbitMQ와 통신하기 위해 연결, 큐 생성 및 메시지 전송을 위한 구성이 필요합니다. 이를 위해 Spring Framework에서는 `RabbitTemplate`과 `@RabbitListener` 어노테이션을 이용합니다.

```java
@Configuration
public class RabbitMQConfig {
    
    @Bean
    public ConnectionFactory connectionFactory() {
        CachingConnectionFactory connectionFactory = new CachingConnectionFactory();
        connectionFactory.setHost("localhost");
        connectionFactory.setUsername("guest");
        connectionFactory.setPassword("guest");
        return connectionFactory;
    }
    
    @Bean
    public RabbitTemplate rabbitTemplate(ConnectionFactory connectionFactory) {
        RabbitTemplate rabbitTemplate = new RabbitTemplate(connectionFactory);
        return rabbitTemplate;
    }

    @Bean
    public SimpleMessageListenerContainer container(ConnectionFactory connectionFactory) {
        SimpleMessageListenerContainer container = new SimpleMessageListenerContainer();
        container.setConnectionFactory(connectionFactory);
        container.setQueueNames("myQueue");
        container.setMessageListener(listenerAdapter());
        return container;
    }

    @Bean
    public MessageListenerAdapter listenerAdapter() {
        return new MessageListenerAdapter(new MyMessageListener());
    }

}
```

위의 코드에서는 RabbitMQ 연결을 위한 `ConnectionFactory`를 설정하고, `RabbitTemplate`을 통해 메시지를 전송합니다. 또한 `SimpleMessageListenerContainer`를 통해 `@RabbitListener` 어노테이션이 적용된 메시지 핸들러를 등록합니다.

## 메시지 송수신

이제 메시지 큐에 메시지를 송수신하는 코드를 작성해보겠습니다.

```java
@Component
public class MyMessageProducer {

    private final RabbitTemplate rabbitTemplate;

    public MyMessageProducer(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    public void produceMessage(String message) {
        rabbitTemplate.convertAndSend("myQueue", message);
    }
}

@Component
public class MyMessageConsumer {

  @RabbitListener(queues = "myQueue")
  public void handleMessage(String message) {
      System.out.println("Received message: " + message);
  }

}
```

위의 예시에서는 `MyMessageProducer`와 `MyMessageConsumer` 클래스가 각각 메시지를 송신하고 수신하는 역할을 합니다. `rabbitTemplate.convertAndSend()` 메소드를 통해 메시지를 송신하고, `@RabbitListener` 어노테이션이 적용된 `handleMessage()` 메소드를 통해 메시지를 수신합니다.

## 실행

메시지 큐를 구현한 코드를 실행해보겠습니다.

```java
@SpringBootApplication
public class Application {

    private final MyMessageProducer messageProducer;

    public Application(MyMessageProducer messageProducer) {
        this.messageProducer = messageProducer;
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @PostConstruct
    public void init() {
        messageProducer.produceMessage("Hello, RabbitMQ!");
    }

}
```

위의 예시에서는 `main()` 메소드가 있는 `Application` 클래스에서 `@PostConstruct` 어노테이션이 적용된 `init()` 메소드를 통해 초기화 시점에 메시지를 송신합니다.

## 결론

이번 기술 블로그에서는 Spring Framework와 RabbitMQ를 이용하여 메시지 큐를 구현하는 방법을 알아보았습니다. Spring Framework의 통합 지원을 통해 빠르고 효율적으로 메시지 큐를 구현할 수 있습니다. RabbitMQ는 안정적이고 확장 가능한 메시지 큐 솔루션으로, 대규모 애플리케이션에서 유용하게 사용될 수 있습니다.

자세한 내용은 [Spring AMQP Documentation](https://docs.spring.io/spring-amqp/docs/current/reference/html/) 및 [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)을 참조하시기 바랍니다.