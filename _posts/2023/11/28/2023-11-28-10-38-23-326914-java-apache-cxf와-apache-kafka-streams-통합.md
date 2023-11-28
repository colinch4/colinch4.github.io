---
layout: post
title: "[java] Java Apache CXF와 Apache Kafka Streams 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

이 블로그 포스트에서는 Java에서 Apache CXF와 Apache Kafka Streams를 통합하는 방법에 대해 알아보겠습니다. Apache CXF는 웹 서비스를 개발하기 위한 오픈 소스 프레임워크이며, Apache Kafka는 분산 스트리밍 플랫폼입니다.

Apache CXF와 Apache Kafka Streams를 함께 사용하면, 웹 서비스를 생성하고 데이터를 Kafka 주제로 스트리밍할 수 있습니다. 이를 통해 웹 서비스에서 전달되는 데이터를 실시간으로 처리하고 분석할 수 있습니다.

## Apache CXF 설정

먼저 Apache CXF를 설치하고 설정해야 합니다. 다음은 Maven을 사용하여 CXF를 프로젝트에 추가하는 방법입니다. `pom.xml` 파일에 다음 의존성을 추가하세요.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-core</artifactId>
        <version>3.3.7</version>
    </dependency>
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-frontend-jaxws</artifactId>
        <version>3.3.7</version>
    </dependency>
</dependencies>
```

그리고 CXF를 사용하여 웹 서비스를 생성하세요. 다음은 간단한 웹 서비스 예제입니다.

```java
package com.example.webservice;

import javax.jws.WebService;

@WebService
public interface HelloWorld {
    String sayHello(String name);
}
```

## Apache Kafka Streams 설정

이제 Apache Kafka Streams를 설치하고 설정해야 합니다. 다음은 Maven을 사용하여 Kafka Streams를 프로젝트에 추가하는 방법입니다. `pom.xml` 파일에 다음 의존성을 추가하세요.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.kafka</groupId>
        <artifactId>kafka-streams</artifactId>
        <version>2.8.0</version>
    </dependency>
</dependencies>
```

그리고 Kafka Streams를 사용하여 데이터를 스트리밍하세요. 다음은 간단한 스트리밍 예제입니다.

```java
package com.example.streaming;

import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.KStream;

import java.util.Properties;

public class StreamProcessor {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "stream-processor");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");

        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, String> stream = builder.stream("input-topic");
        stream.foreach((key, value) -> {
            System.out.println("Received message: " + value);
            // Process the message
        });

        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
    }
}
```

위 예제에서는 `localhost:9092`라는 Kafka 브로커를 사용하고, "input-topic"이라는 주제로부터 데이터를 스트리밍합니다.

## Apache CXF와 Apache Kafka Streams 통합

Apache CXF와 Apache Kafka Streams를 통합하기 위해서는 CXF 서비스에서 Kafka Streams를 사용하여 데이터를 스트리밍하면 됩니다. 이를 위해 CXF 서비스 내에서 Kafka Producer를 생성하고, Kafka Consumer를 사용하여 데이터를 처리할 수 있습니다.

```java
package com.example.webservice;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import javax.jws.WebService;
import java.util.Properties;

@WebService(endpointInterface = "com.example.webservice.HelloWorld")
public class HelloWorldImpl implements HelloWorld {
    private KafkaProducer<String, String> producer;

    public HelloWorldImpl() {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        producer = new KafkaProducer<>(props);
    }

    public String sayHello(String name) {
        ProducerRecord<String, String> record = new ProducerRecord<>("output-topic", name);
        producer.send(record);
        return "Hello, " + name + "!";
    }
}
```

위 코드에서는 `output-topic`이라는 Kafka 주제로 데이터를 전송하고, 사용자에게 "Hello, {name}!"과 같은 응답을 반환합니다. Kafka Consumer를 사용하여 `output-topic`에서 데이터를 처리할 수 있습니다.

## 결론

이렇게 Apache CXF와 Apache Kafka Streams를 통합하여 Java로 개발된 웹 서비스를 실시간으로 데이터를 처리하고 분석할 수 있습니다. 이렇게 구성된 시스템은 대규모 데이터 처리와 실시간 분석에 적합하며, 확장성과 유연성을 제공합니다.

**참고 자료:**
- [Apache CXF](http://cxf.apache.org/)
- [Apache Kafka](https://kafka.apache.org/)
- [Apache Kafka Streams](https://kafka.apache.org/documentation/streams/)