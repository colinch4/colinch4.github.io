---
layout: post
title: "[java] 아파치 플링크의 오류 처리(Error handling in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 대규모 데이터 처리를 위한 분산 처리 프레임워크입니다. 그러나 이러한 대규모 데이터 작업을 수행할 때 예기치 않은 오류가 발생할 수 있습니다. 이러한 오류에 대응하기 위해 아파치 플링크는 몇 가지 오류 처리 메커니즘을 제공합니다.

## Retry 메커니즘

Retry 메커니즘은 데이터 처리 작업이 실패하였을 때, 일정 횟수의 재시도를 통해 문제를 해결하는 방법입니다. 아파치 플링크의 Retry 메커니즘은 재시도 간격과 재시도 횟수를 설정할 수 있는 유연성을 제공합니다. 이를 통해 오류가 발생했을 때 손쉽게 복구할 수 있습니다.

```java
DataStream<Integer> dataStream = ...;

DataStream<Integer> resultStream = dataStream
    .retry(5, Time.minutes(1))
    .filter(i -> i < 10);
```

위의 예제에서 `retry(5, Time.minutes(1))`는 최대 5번의 재시도를 시도하고, 재시도 간격을 1분으로 설정하는 것을 보여줍니다.

## Dead-letter Queue

Dead-letter Queue는 오류가 발생한 이벤트나 레코드를 임시로 저장하는 메커니즘입니다. 이를 통해 오류가 발생한 데이터를 따로 처리하거나 분석할 수 있으며, 디버깅과 감시에도 도움이 됩니다. 아파치 플링크는 Dead-letter Queue를 이용하여 오류가 발생한 데이터를 저장하고, 이를 다시 처리하거나 로깅할 수 있습니다.

```java
DataStream<Integer> dataStream = ...;

dataStream
    .process(new MyProcessFunction())
    .addSink(new FlinkKafkaProducer<>())
    .name("Kafka Sink")
    .setParallelism(5)
    .getSideOutput(new OutputTag<>("error-records"))
    .addSink(new FlinkKafkaProducer<>())
    .name("Error Sink")
    .setParallelism(1);
```

위의 예제에서 `getSideOutput(new OutputTag<>("error-records"))`를 통해 오류가 발생한 데이터를 따로 처리할 수 있도록 설정하고 있습니다. 이렇게 설정된 데이터는 "Error Sink"로 전송되어 Dead-letter Queue에 저장됩니다.

## 체크포인팅 및 재시작

아파치 플링크는 체크포인팅 메커니즘을 통해 애플리케이션 상태를 주기적으로 저장합니다. 이를 통해 애플리케이션 재시작 시 이전 상태로 복원할 수 있습니다. 따라서 오류가 발생했을 때도 데이터 처리 작업을 재개할 수 있습니다.

```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
env.enableCheckpointing(30000);
env.setStateBackend(new FsStateBackend("hdfs://checkpoint-directory"));
```

위의 예제에서 `enableCheckpointing(30000)`은 30초마다 체크포인트를 생성하도록 설정하고, `setStateBackend(new FsStateBackend("hdfs://checkpoint-directory"))`는 체크포인트를 HDFS에 저장하도록 설정하는 것을 보여줍니다.

## 참고 자료

- [Apache Flink 공식 문서](https://flink.apache.org/)
- [Flink Training - Handling Application Failures](https://training.ververica.com/courses/take/flink-training-course-advanced-java/lessons/12227751-handling-application-failures)
- [Handling Failure in Apache Flink: Checkpointing and Recovery](https://www.ververica.com/blog/handling-failure-in-apache-flink-checkpointing-recovery)