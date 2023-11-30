---
layout: post
title: "[java] 아파치 플링크의 체크포인팅(Checkpointing in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 대용량의 데이터 처리를 위한 분산 처리 프레임워크입니다. 플링크는 신뢰성 있는 스트림 처리를 위해 체크포인팅 기능을 제공하며, 이를 통해 데이터 손실을 방지하고 정확성을 보장합니다.

## 체크포인팅이란?

체크포인팅은 플링크에서 스트림 처리를 동작하는 동안 데이터 상태를 중간에 저장하는 기능입니다. 이러한 중간 저장은 주기적으로 수행되며, 시스템 장애가 발생했을 때 손실된 데이터를 최소화하고 작업을 이어서 진행할 수 있도록 합니다.

## 체크포인팅 설정

체크포인팅을 사용하기 위해서는 먼저 플링크 잡(Job)에 대한 체크포인팅 설정을 해야 합니다. 아래는 체크포인팅을 활성화하고 주기를 5초로 설정하는 예시입니다.

```java
env.enableCheckpointing(5000);
```

이렇게 설정하면 플링크는 5초마다 체크포인트를 생성합니다.

## 체크포인트 핸들링

체크포인트를 생성할 때마다 생성된 데이터는 외부 저장소에 저장됩니다. 플링크는 여러 옵션을 제공하여 체크포인트를 관리할 수 있습니다.

* 외부 저장소 설정:

```java
env.getCheckpointConfig().setCheckpointStorage(new FsStateBackend("hdfs://localhost:9000/checkpoints"));
```
  
* 체크포인트 내부 상태 보존:

```java
env.getCheckpointConfig().enableExternalizedCheckpoints(ExternalizedCheckpointCleanup.RETAIN_ON_CANCELLATION);
```

위 예시는 체크포인트를 HDFS에 저장하고, 작업이 취소되었을 때 체크포인트 상태를 보존하는 설정입니다.

## 체크포인트 복구

장애 발생 시, 플링크는 마지막으로 생성된 체크포인트를 사용하여 작업을 복구합니다. 아래는 잡(Job) 실행 시 체크포인트를 사용하여 복구를 수행하는 예시입니다.

```java
env.setRestartStrategy(RestartStrategies.fixedDelayRestart(
    3, // 재시작 횟수
    Time.seconds(10) // 딜레이 시간
));
```

위 설정은 최대 3번의 재시작을 시도하며, 10초의 딜레이 시간을 가지고 체크포인트를 이용하여 작업을 복구합니다.

## 결론

아파치 플링크의 체크포인팅 기능을 사용하면 스트림 처리 중에 발생한 장애로 인한 데이터 손실을 방지할 수 있습니다. 마지막으로 생성된 체크포인트를 통해 작업을 복구함으로써 데이터 정확성을 보장할 수 있습니다.

## 참고 자료

1. [Apache Flink Documentation - Checkpointing](https://ci.apache.org/projects/flink/flink-docs-release-1.14/docs/concepts/streaming/checkpoints/)
2. [Apache Flink - StateFul Processing](https://flink.apache.org/features/2015/12/04/stateful-processing.html)