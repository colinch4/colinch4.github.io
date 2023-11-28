---
layout: post
title: "[java] Java Apache CXF와 Apache Kafka 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

## 개요
이 글에서는 Apache CXF와 Apache Kafka를 사용하여 Java 애플리케이션에서 메시지-기반 통합을 구현하는 방법에 대해 알아보겠습니다.

## Apache CXF 소개
Apache CXF는 Java에서 웹 서비스를 구현하기 위한 오픈 소스 프레임워크입니다. CXF는 다양한 프로토콜 및 데이터 포맷을 지원하여 웹 서비스의 개발 및 통합을 간편하게 할 수 있습니다.

## Apache Kafka 소개
Apache Kafka는 고성능 분산 스트리밍 플랫폼으로, 대용량의 실시간 데이터 처리를 위해 설계되었습니다. Kafka는 분산형 아키텍처와 내구성이 뛰어난 메시징 시스템을 제공하여 신속한 데이터 전송과 확장성을 보장합니다.

## Apache CXF와 Apache Kafka 통합
CXF와 Kafka를 함께 사용하면 손쉽게 메시지-기반 아키텍처를 구현할 수 있습니다. CXF는 Apache CXF의 동기 및 비동기 웹 서비스 구성 요소를 사용하여 Kafka와 통신할 수 있습니다.

Apache CXF에서 Kafka를 사용하는 방법은 다음과 같습니다:

1. Apache CXF 프로젝트를 생성하고 Maven 또는 Gradle을 사용하여 Kafka 종속성을 추가합니다.
2. CXF 구성 파일에서 Kafka 연결을 설정합니다.
3. CXF 서비스에서 Kafka 프로듀서 및 컨슈머를 생성하고 사용합니다.

아래는 Apache CXF와 Apache Kafka를 통합하는 Java 코드 예시입니다:

```java
import org.apache.cxf.jaxrs.JAXRSServerFactoryBean;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

public class CXFWithKafkaIntegrationExample {

    private Producer<String, String> kafkaProducer;
    private Consumer<String, String> kafkaConsumer;

    public CXFWithKafkaIntegrationExample() {
        // Kafka producer 초기화
        Properties producerProps = new Properties();
        producerProps.put("bootstrap.servers", "localhost:9092");
        producerProps.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        producerProps.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        this.kafkaProducer = new KafkaProducer<>(producerProps);

        // Kafka consumer 초기화
        Properties consumerProps = new Properties();
        consumerProps.put("bootstrap.servers", "localhost:9092");
        consumerProps.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        consumerProps.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        consumerProps.put("group.id", "test-group");
        this.kafkaConsumer = new KafkaConsumer<>(consumerProps);
    }

    public void sendMessage(String topic, String message) {
        ProducerRecord<String, String> record = new ProducerRecord<>(topic, message);
        kafkaProducer.send(record);
    }

    public void consumeMessage(String topic) {
        kafkaConsumer.subscribe(Collections.singletonList(topic));
        while (true) {
            ConsumerRecords<String, String> records = kafkaConsumer.poll(Duration.ofMillis(100));
            for (ConsumerRecord<String, String> record : records) {
                // 메시지 처리 로직 구현
            }
        }
    }

    public static void main(String[] args) {
        CXFWithKafkaIntegrationExample example = new CXFWithKafkaIntegrationExample();

        // Kafka 프로듀서를 통해 메시지 전송
        example.sendMessage("test-topic", "Hello, Kafka!");

        // Kafka 컨슈머를 통해 메시지 수신
        example.consumeMessage("test-topic");
    }
}
```

위의 코드는 Apache CXF와 Apache Kafka를 사용하여 메시지를 보내고 받는 간단한 예제를 보여줍니다.

추가로 CXF와 Kafka를 통합하는 방법에 대해 더 자세히 알고 싶다면 아래의 참고 자료를 참고하시기 바랍니다.

## 참고 자료
- [Apache CXF 공식 문서](https://cxf.apache.org/)
- [Apache Kafka 공식 문서](https://kafka.apache.org/)
- [Apache Kafka 클라이언트 API 가이드](https://www.confluent.io/blog/apache-kafka-clients-at-scale/)
- [Apache CXF와 Apache Kafka를 통합한 코드 예제](https://github.com/example/cxf-kafka-integration-example)