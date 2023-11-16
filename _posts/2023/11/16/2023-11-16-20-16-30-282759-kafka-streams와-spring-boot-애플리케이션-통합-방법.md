---
layout: post
title: "[java] Kafka Streams와 Spring Boot 애플리케이션 통합 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Spring Boot는 많은 개발자들에게 친숙한 프레임워크이며, Kafka Streams는 대규모 실시간 데이터 처리를 위한 강력한 도구입니다. 이번 글에서는 Kafka Streams와 Spring Boot 애플리케이션을 통합하는 방법에 대해 알아보겠습니다.

## 목차
- [Kafka Streams란?](#kafka-streams란)
- [Spring Boot와 Kafka Streams 통합](#spring-boot와-kafka-streams-통합)
- [Kafka Streams와 Spring Boot 애플리케이션 개발](#kafka-streams와-spring-boot-애플리케이션-개발)
- [요약](#요약)

## Kafka Streams란?
Kafka Streams는 Apache Kafka를 기반으로 하는 실시간 스트리밍 플랫폼입니다. Kafka Streams를 사용하면 대규모의 실시간 데이터 스트림을 처리하고, 데이터를 조작하고, 계산을 수행할 수 있습니다. Kafka Streams는 Java 라이브러리로 제공되며, Spring Boot와 함께 사용할 수 있습니다.

## Spring Boot와 Kafka Streams 통합
Spring Boot는 Kafka Streams와의 통합을 위해 여러 가지 옵션을 제공합니다. 가장 간단한 방법은 Spring for Apache Kafka를 사용하는 것입니다. Spring for Apache Kafka는 Spring Boot와 Apache Kafka를 통합하는 데 도움이 되는 다양한 기능을 제공합니다.

Spring Boot와 Kafka Streams를 함께 사용할 때는 아래의 단계를 따라야 합니다:

1. build.gradle (또는 pom.xml)에 필요한 의존성을 추가합니다.

```java
dependencies {
    implementation 'org.springframework.kafka:spring-kafka'
}
```

2. Kafka에 연결하기 위한 KafkaTemplate을 생성합니다.

```java
@Configuration
public class KafkaConfiguration {

    @Bean
    public KafkaTemplate<String, String> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }

    @Bean
    public ProducerFactory<String, String> producerFactory() {
        Map<String, Object> configProps = new HashMap<>();
        configProps.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        configProps.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        configProps.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        return new DefaultKafkaProducerFactory<>(configProps);
    }
}
```

3. Kafka Streams를 사용하여 데이터를 처리하는 로직을 작성합니다. 예를 들어, 아래의 코드는 Kafka Streams를 사용하여 입력 토픽의 값을 읽고, 각 값을 대문자로 변환하여 출력 토픽에 전달하는 예입니다.

```java
@Configuration
public class KafkaStreamsConfiguration {

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;

    @Bean
    public KStream<String, String> processKafkaStreams(StreamsBuilder streamsBuilder) {
        KStream<String, String> input = streamsBuilder.stream("input-topic");
        KStream<String, String> output = input.mapValues(value -> value.toUpperCase());
        output.to("output-topic");
        return output;
    }

    @Bean
    public NewTopic inputTopic() {
        return new NewTopic("input-topic", 1, (short) 1);
    }

    @Bean
    public NewTopic outputTopic() {
        return new NewTopic("output-topic", 1, (short) 1);
    }
}
```

4. Spring Boot 애플리케이션에서 Kafka Streams를 시작하기 위해 아래의 코드를 추가합니다.

```java
@SpringBootApplication
@EnableKafkaStreams
public class KafkaStreamsApplication {

    public static void main(String[] args) {
        SpringApplication.run(KafkaStreamsApplication.class, args);
    }
}
```

## Kafka Streams와 Spring Boot 애플리케이션 개발
Kafka Streams와 Spring Boot를 통합하여 실시간 데이터 처리 애플리케이션을 개발하기 위해 다음 단계를 따릅니다:

1. Kafka에 입력 및 출력 토픽을 생성합니다.
2. Spring Boot 애플리케이션에서 Kafka Streams를 구성하고, 데이터를 처리하는 로직을 작성합니다.
3. Kafka Streams 애플리케이션을 실행하고, 데이터를 소비하고, 결과를 확인합니다.

## 요약
Kafka Streams와 Spring Boot는 대규모 실시간 데이터 처리를 위한 강력한 조합입니다. 이번 글에서는 Kafka Streams와 Spring Boot를 통합하기 위한 기본적인 단계와 코드 예제를 살펴보았습니다. Kafka Streams를 사용하여 스트리밍 데이터를 처리하고, Spring Boot를 통해 애플리케이션을 개발하는 데 도움이 되었을 것입니다.

더 자세한 내용은 아래의 참고 자료를 확인해주세요.

- [Spring for Apache Kafka](https://docs.spring.io/spring-kafka/docs/current/reference/html)
- [Kafka Streams Documentation](https://kafka.apache.org/28/documentation/streams)