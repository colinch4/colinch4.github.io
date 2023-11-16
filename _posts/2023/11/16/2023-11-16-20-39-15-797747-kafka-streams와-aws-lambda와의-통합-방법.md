---
layout: post
title: "[java] Kafka Streams와 AWS Lambda와의 통합 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

## 소개

이 문서는 Apache Kafka와 AWS Lambda를 함께 사용하여 스트리밍 데이터 처리를 구현하는 방법에 대해 설명합니다. Kafka Streams는 스트리밍 데이터를 소비하고 처리하기 위한 클라이언트 라이브러리이며, AWS Lambda는 이벤트 기반의 서버리스 컴퓨팅 서비스입니다. 두 기술을 결합하여 실시간으로 스트림 데이터를 처리할 수 있습니다.

## Kafka Streams와 AWS Lambda 연동하기

1. **Kafka에 데이터 전송**: 먼저 Kafka Producer를 사용하여 데이터를 Kafka 클러스터로 전송해야 합니다. 데이터는 토픽에 저장됩니다.

```java
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

KafkaProducer<String, String> producer = new KafkaProducer<>(props);
ProducerRecord<String, String> record = new ProducerRecord<>("mytopic", "key", "value");

producer.send(record);
producer.close();
```

2. **AWS Lambda 함수 작성**: AWS Lambda 함수를 작성하여 Kafka 스트림 데이터를 처리합니다. 이 함수는 특정 토픽에서 데이터를 소비하고, 필요한 작업을 수행합니다.

```java
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import org.apache.kafka.clients.consumer.ConsumerRecord;

public class MyLambdaFunction implements RequestHandler<ConsumerRecord<String, String>, Void> {

    @Override
    public Void handleRequest(ConsumerRecord<String, String> record, Context context) {
        // Kafka 스트림 데이터 처리 코드 작성
        System.out.println("Received message: " + record.value());
        // 데이터를 처리하는 로직 추가

        return null;
    }
}
```

3. **AWS Lambda 함수 배포 및 구성**: AWS Lambda 함수를 배포하고, 트리거를 설정하여 Kafka Consumer와 연동합니다. Lambda 함수에서는 특정 토픽에서 데이터를 읽어옵니다.

4. **스트림 데이터 처리**: Kafka Streams를 사용하여 Kafka 스트림 데이터를 처리합니다. Kafka Streams는 스트림 데이터를 읽어와서 필요한 작업을 수행하고, 다른 토픽에 결과를 저장합니다.

```java
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.KStream;

import java.util.Properties;

public class MyStreamProcessingJob {

    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "my-stream-processing-job");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        // Kafka Streams 설정 추가

        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, String> inputTopic = builder.stream("mytopic");
        // 스트림 데이터 처리 로직 추가

        KStream<String, String> outputTopic = inputTopic.map((key, value) -> {
            // 데이터 변환 또는 필터링 등 작업 수행
            return new KeyValue<>(key, transformedValue);
        });

        outputTopic.to("outputtopic");
        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
    }
}
```

## 결론

Kafka Streams와 AWS Lambda를 통합하여 스트리밍 데이터 처리를 구현하는 방법에 대해 알아보았습니다. Kafka Streams는 스트림 처리를 위한 강력한 라이브러리이고, AWS Lambda는 이벤트 기반의 서버리스 컴퓨팅 플랫폼입니다. 이 두 기술을 함께 사용하면 실시간으로 스트림 데이터를 처리할 수 있습니다.