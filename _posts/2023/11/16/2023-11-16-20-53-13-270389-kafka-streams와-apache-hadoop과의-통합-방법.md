---
layout: post
title: "[java] Kafka Streams와 Apache Hadoop과의 통합 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Kafka Streams는 대량의 실시간 데이터를 처리하기 위한 분산 스트리밍 플랫폼입니다. Apache Hadoop은 대규모 데이터 처리를 위한 오픈 소스 프레임워크로서, 대용량의 데이터를 안정적으로 저장하고 처리할 수 있습니다. 이 블로그 포스트에서는 Kafka Streams와 Apache Hadoop을 통합하는 방법에 대해 알아보겠습니다.

## 1. Kafka Streams를 사용하여 데이터 스트리밍하기

먼저, Kafka Streams를 사용하여 데이터 스트리밍을 설정합니다. Kafka Streams는 비동기식으로 데이터를 소비하고 처리할 수 있습니다. 아래는 Kafka Streams를 사용하여 데이터를 처리하는 Java 예제 코드입니다.

```java
import org.apache.kafka.streams.*;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.KTable;

import java.util.Arrays;
import java.util.Properties;

public class StreamingApp {

    public static void main(String[] args) {
        
        // Kafka Streams 설정
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streaming-app");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        
        // Kafka Streams 빌더 생성
        StreamsBuilder builder = new StreamsBuilder();
        
        // Input 토픽 지정
        KStream<String, String> inputTopic = builder.stream("input-topic");
        
        // 데이터 처리 로직
        KTable<String, Long> wordCounts = inputTopic
            .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\\W+")))
            .groupBy((key, word) -> word)
            .count();
        
        // 결과 출력
        wordCounts.toStream().to("output-topic", Produced.with(Serdes.String(), Serdes.Long()));
        
        // Kafka Streams 애플리케이션 실행
        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
    }
}
```

위의 코드에서는 Kafka Streams를 설정하고, 입력 토픽을 지정하고, 데이터 처리 로직을 작성한 후, 결과를 출력합니다.

## 2. Apache Hadoop과의 통합하기

Apache Hadoop과 Kafka Streams를 통합하기 위해서는 Kafka Streams의 출력 데이터를 Hadoop 파일 시스템(HDFS)에 저장해야 합니다. 아래는 Hadoop 파일 시스템에 데이터를 저장하는 예제 코드입니다.

```java
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;

import java.io.IOException;

public class HadoopIntegration {

    public static void main(String[] args) throws IOException {

        // Hadoop 파일 시스템에 저장할 디렉토리 경로
        String outputDirectory = "/user/kafka-streams/output";

        // Kafka Streams 설정
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "hadoop-integration");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");

        // Kafka Streams 빌더 생성
        StreamsBuilder builder = new StreamsBuilder();

        // Input 토픽 지정
        KStream<String, String> inputTopic = builder.stream("output-topic");

        // Hadoop 파일 시스템에 저장
        inputTopic.to("hdfs://" + outputDirectory);

        // Kafka Streams 애플리케이션 실행
        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
    }
}
```

위의 코드에서는 Kafka Streams의 출력 토픽을 Hadoop 파일 시스템에 저장하기 위해 `to()` 메서드를 사용합니다. `hdfs://` 접두사를 통해 Hadoop 파일 시스템과 연결하고, 저장할 디렉토리 경로를 지정합니다.

## 3. 실행 및 결과 확인

위의 두 예제 코드를 각각 실행하면 Kafka Streams가 작동하고 데이터가 처리되며, 그 결과가 Apache Hadoop의 파일 시스템에 저장됩니다. 저장된 데이터는 Hadoop 명령어를 사용하여 확인할 수 있습니다.

예를 들어, Hadoop 명령어 `hdfs dfs -cat`를 사용하여 저장된 데이터를 확인할 수 있습니다. 아래의 명령어는 저장된 데이터의 처음 10개 레코드를 출력합니다.

```
hdfs dfs -cat /user/kafka-streams/output/* | head -n 10
```

Kafka Streams와 Apache Hadoop을 통합하는 방법에 대해 알아보았습니다. 이를 통해 대용량의 데이터를 실시간으로 처리하고 저장할 수 있습니다.