---
layout: post
title: "[java] Apache ActiveMQ와 Spring Batch의 연동"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Apache ActiveMQ는 오픈 소스 메시지 브로커로서, 메시지 기반 애플리케이션을 개발하는 데 사용됩니다. Spring Batch는 대용량의 데이터 처리를 위한 Batch 프레임워크입니다. 이 두 가지 기술을 함께 사용하여 간단하고 효율적인 메시지 처리 시스템을 구축할 수 있습니다.

## ActiveMQ 설정

먼저, ActiveMQ를 설치하고 실행해야 합니다. ActiveMQ는 다양한 방법으로 설치할 수 있으며, 이 예제에서는 Apache ActiveMQ의 [공식 웹사이트](https://activemq.apache.org/)에서 다운로드하여 설치합니다.

설치가 완료되면 ActiveMQ 브로커를 실행합니다. 브로커 실행은 아래의 명령으로 수행할 수 있습니다.

```bash
$ activemq start
```

브로커가 실행되면 ActiveMQ 관리 콘솔에 접속하여 큐를 생성해야 합니다. 관리 콘솔은 기본적으로 `http://localhost:8161/admin`에서 확인할 수 있습니다.

## Spring Batch 연동

Spring Batch 프로젝트에서 ActiveMQ를 연동하려면, 먼저 Spring Boot 프로젝트를 생성해야 합니다. Spring Boot는 Spring 기반 애플리케이션을 쉽게 구성할 수 있는 도구입니다. Spring Boot를 사용하여 프로젝트를 생성하려면, 다음과 같이 명령을 실행합니다.

```bash
$ spring init --dependencies=activemq my-batch-project
```

프로젝트가 생성되면, `application.properties` 파일에서 ActiveMQ와의 연동을 설정해야 합니다. 아래와 같은 설정을 추가합니다.

```properties
spring.jms.template.default-destination=your-queue-name
spring.jms.template.delivery-delay=5000
spring.jms.listener.concurrency=3
```

이 설정은 ActiveMQ 큐 이름을 지정하고, 메시지 전달 지연 시간을 설정하며, 리스너의 동시성 수를 지정합니다.

Spring Batch에서 ActiveMQ를 사용하려면, `@EnableJms` 어노테이션을 사용하여 JMS 지원을 활성화해야 합니다. `@EnableBatchProcessing` 어노테이션과 함께 사용해야 합니다. 아래는 예제 코드입니다.

```java
@SpringBootApplication
@EnableBatchProcessing
@EnableJms
public class MyBatchApplication {
    
    public static void main(String[] args) {
        SpringApplication.run(MyBatchApplication.class, args);
    }
    
    // ...
}
```

위의 예제 코드는 Spring Boot와 Spring Batch를 함께 사용할 수 있도록 구성합니다. `@EnableJms` 어노테이션은 ActiveMQ와의 JMS 연동을 활성화합니다.

## 메시지 송수신

이제 ActiveMQ 큐를 통해 메시지를 송수신할 수 있습니다. 메시지를 보내기 위해서는 `JmsTemplate`를 사용해야 합니다. 아래는 메시지를 보내는 간단한 예제 코드입니다.

```java
@Autowired
private JmsTemplate jmsTemplate;

public void sendMessage(String message) {
    jmsTemplate.convertAndSend("your-queue-name", message);
}
```

메시지를 수신하기 위해서는 `@JmsListener` 어노테이션을 사용하여 리스너를 등록해야 합니다. 아래는 메시지를 수신하는 예제 코드입니다.

```java
@JmsListener(destination = "your-queue-name")
public void receiveMessage(String message) {
    System.out.println("Received message: " + message);
}
```

위의 예제 코드는 `your-queue-name` 큐에서 메시지를 수신하여 콘솔에 출력합니다.

이와 같이 Apache ActiveMQ와 Spring Batch를 함께 사용하면, 메시지 기반의 배치 처리 시스템을 구축할 수 있습니다. ActiveMQ를 통해 메시지를 송수신하고, Spring Batch를 사용하여 대용량의 데이터를 처리할 수 있습니다.