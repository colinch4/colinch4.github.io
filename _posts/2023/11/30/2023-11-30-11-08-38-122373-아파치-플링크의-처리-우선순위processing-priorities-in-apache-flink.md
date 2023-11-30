---
layout: post
title: "[java] 아파치 플링크의 처리 우선순위(Processing priorities in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대규모 데이터 스트림 및 배치 처리에 사용되는 오픈 소스 분산 처리 프레임워크입니다. 하지만 대량의 데이터를 처리하다 보면 작업들 간의 우선순위가 중요한 역할을 합니다. 이번 블로그 포스트에서는 아파치 플링크에서 제공하는 처리 우선순위에 대해 알아보겠습니다.

## 1. 처리 우선순위 개요

아파치 플링크에서는 다양한 우선순위 레벨을 사용하여 작업들 간의 우선순위를 지정할 수 있습니다. 아래는 아파치 플링크에서 제공하는 처리 우선순위 레벨입니다.

- **기본 우선순위(Default Priority)**: 모든 작업은 기본적으로 이 우선순위로 설정됩니다. 이 우선순위는 가장 많이 사용되는 우선순위이며, 대부분의 작업은 여기에 포함됩니다.
- **고 우선순위(High Priority)**: 특정 작업에 대해 높은 우선순위를 부여하고자 할 때 사용됩니다. 고 우선순위로 설정된 작업들은 기본 우선순위를 가진 작업보다 우선적으로 처리됩니다.
- **저 우선순위(Low Priority)**: 특정 작업의 우선순위를 낮추고자 할 때 사용됩니다. 저 우선순위로 설정된 작업들은 기본 우선순위를 가진 작업보다 후순위로 처리됩니다.

## 2. 처리 우선순위 설정 방법

아파치 플링크에서는 작업에 대한 우선순위를 설정하는 다양한 방법을 제공합니다. 여기서는 가장 일반적인 방법을 소개하겠습니다.

```java
ExecutionConfig config = new ExecutionConfig();
config.setLatencyTrackingInterval(5000);
config.setRestartStrategy(RestartStrategies.fixedDelayRestart(3, Time.seconds(10)));
config.setDefaultExecutionPriority(ExecutionConfig.ExecutionPriority.HIGH);
```

위의 예제에서는 `ExecutionConfig` 객체를 생성하여 `setDefaultExecutionPriority` 메서드를 사용하여 작업의 기본 우선순위를 설정하고 있습니다. 여기서는 `HIGH` 우선순위로 설정하였습니다.

## 3. 처리 우선순위 적용

아파치 플링크에서는 설정된 처리 우선순위에 따라 작업을 처리합니다. 예를 들어, 고 우선순위로 설정된 작업은 기본 우선순위를 가진 작업보다 먼저 처리됩니다.

```java
DataStream<Integer> input = ...;

input.process(new ProcessFunction<Integer, Integer>() {
    @Override
    public void processElement(Integer value, Context ctx, Collector<Integer> out) throws Exception {
        // Process element
    }
}).name("HighPriorityOperator").setPriority(ExecutionConfig.ExecutionPriority.HIGH);
```

위의 예제에서는 `setPriority` 메서드를 사용하여 연산자에 대한 우선순위를 설정하고 있습니다. `HIGH` 우선순위로 설정되었으므로 이 연산자는 다른 연산자보다 우선적으로 처리됩니다.

## 4. 결론

아파치 플링크의 처리 우선순위를 설정하고 적용하는 방법을 알아보았습니다. 우선순위를 적절히 설정하면 작업들 간의 처리 순서를 조절할 수 있어서 효율적인 데이터 처리를 할 수 있습니다.

더 자세한 내용은 [아파치 플링크 문서](https://flink.apache.org/)를 참조하시기 바랍니다.