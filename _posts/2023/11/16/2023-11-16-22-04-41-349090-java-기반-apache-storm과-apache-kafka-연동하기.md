---
layout: post
title: "[java] Java 기반 Apache Storm과 Apache Kafka 연동하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Storm은 분산 스트리밍 처리를 위한 오픈 소스 프레임워크입니다. Apache Kafka는 안정적이고 확장 가능한 데이터 스트리밍 플랫폼으로 알려져 있습니다. 이 블로그 포스트에서는 Java를 사용하여 Apache Storm과 Apache Kafka를 연동하는 방법에 대해 알아보겠습니다.

## 개요

- Apache Storm과 Apache Kafka는 분리된 프로젝트이지만 결합하여 대규모 실시간 데이터 처리 파이프라인을 구축할 수 있습니다.
- Storm은 Kafka로부터 데이터를 가져와서 실시간으로 처리하고 결과를 소비자에게 전달하는 역할을 수행합니다.
- Kafka는 메시지 큐와 같은 개념으로, Storm이 처리해야 할 메시지를 저장하고 전송할 수 있도록 합니다.
- 이 예시에서는 Maven을 사용하여 필요한 의존성을 관리합니다.

## 단계 1: Maven 프로젝트 설정

먼저 Maven 프로젝트를 설정해야 합니다. 프로젝트의 pom.xml 파일을 열고 다음 종속성을 추가하세요.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.storm</groupId>
        <artifactId>storm-core</artifactId>
        <version>2.2.0</version>
    </dependency>
    <dependency>
        <groupId>org.apache.storm</groupId>
        <artifactId>storm-kafka</artifactId>
        <version>2.2.0</version>
    </dependency>
</dependencies>
```

## 단계 2: Apache Storm 토폴로지 작성

이제 Apache Storm에 대한 토폴로지를 작성해보겠습니다. StormTopology 클래스를 만들고 다음 코드를 추가합니다.

```java
import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.kafka.spout.KafkaSpout;
import org.apache.storm.kafka.spout.KafkaSpoutConfig;

public class StormTopology {
    public static void main(String[] args) {
        // TopologyBuilder로 토폴로지를 생성합니다.
        TopologyBuilder builder = new TopologyBuilder();

        // KafkaSpout를 생성합니다.
        KafkaSpoutConfig<String, String> kafkaSpoutConfig =
                KafkaSpoutConfig.builder("kafka-bootstrap-servers", "kafka-topic")
                        .build();
        KafkaSpout<String, String> kafkaSpout = new KafkaSpout<>(kafkaSpoutConfig);

        // KafkaSpout를 토폴로지에 추가합니다.
        builder.setSpout("kafka-spout", kafkaSpout);

        // 토폴로지를 Storm에 제출합니다.
        LocalCluster cluster = new LocalCluster();
        Config config = new Config();
        cluster.submitTopology("kafka-storm-topology", config, builder.createTopology());
    }
}
```

## 단계 3: Kafka 주키퍼와 브로커 설정

Kafka와의 연동을 위해 주키퍼(Zookeeper)와 브로커(Broker)를 설정해야 합니다. `server.properties` 파일을 열고 다음 설정을 추가합니다.

```properties
zookeeper.connect=localhost:2181
listeners=PLAINTEXT://localhost:9092
advertised.listeners=PLAINTEXT://localhost:9092
```

## 단계 4: 실행 및 확인

모든 설정이 완료되었습니다. 이제 프로그램을 실행하고 Storm이 Kafka와 정상적으로 연동되는지 확인해보세요. 터미널에서 프로젝트의 루트 디렉토리로 이동한 다음 다음 명령어를 실행하세요.

```
mvn package
```

프로그램이 성공적으로 빌드되면 다음 명령어로 StormTopology를 실행합니다.

```
storm jar target/my-topology.jar com.example.StormTopology
```

실행 결과를 확인하고 Storm이 Kafka로부터 데이터를 가져와 제대로 처리하는지 확인하세요.

## 결론

이 블로그 포스트에서는 Java를 사용하여 Apache Storm과 Apache Kafka를 연동하는 방법에 대해 알아보았습니다. Storm을 사용하면 실시간으로 대규모 데이터를 처리할 수 있으며, Kafka를 통해 안정적이고 확장 가능한 메시지 큐를 사용할 수 있습니다. 프로젝트 설정, 토폴로지 작성 및 Kafka와의 연동 설정 방법을 확인하여 실시간 데이터 처리 파이프라인을 구축할 수 있습니다.

## 참조

- [Apache Storm Documentation](http://storm.apache.org/releases/2.2.0/index.html)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)