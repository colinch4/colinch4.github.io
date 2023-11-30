---
layout: post
title: "[java] 아파치 플링크의 트리거(Triggers in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대용량 데이터 처리를 위한 분산 스트리밍 및 배치 처리 엔진입니다. 이러한 데이터 처리 작업을 효과적으로 제어하기 위해 플링크는 트리거(Triggers)라는 개념을 제공합니다.

## 트리거란?

트리거는 플링크의 스트림 작업에서 어떤 이벤트가 발생하면 해당 작업을 실행하기 위한 규칙을 정의하는 메커니즘입니다. 예를 들어, 매 5분마다 스트림 작업을 실행하도록 트리거를 설정할 수 있습니다.

## 플링크에서의 트리거 종류

1. 프로세스 타임 트리거(Process Time Triggers): 플링크의 프로세스 타임은 이벤트가 수신된 시점을 기준으로 합니다. 프로세스 타임 트리거는 특정 시간 간격 또는 특정 시점에서 작업을 트리거하도록 정의할 수 있습니다.

2. 이벤트 타임 트리거(Event Time Triggers): 플링크는 이벤트에 기록된 타임스탬프를 사용하여 이벤트 타임을 추적합니다. 이벤트 타임 트리거는 특정 이벤트 시간 또는 특정 시간 간격에 따라 작업을 트리거하도록 정의할 수 있습니다.

3. 워터마크 타임 트리거(Watermark Time Triggers): 플링크는 이벤트의 지연을 처리하기 위해 워터마크를 사용합니다. 워터마크 타임 트리거는 특정 워터마크 범위에서 작업을 트리거하도록 정의할 수 있습니다.

## 예시 코드

다음은 아파치 플링크에서 트리거를 설정하는 예시 코드입니다.

```java
StreamExecutionEnvironment env =
    StreamExecutionEnvironment.getExecutionEnvironment();

DataStream<String> input = env.addSource(new YourEventSource());

// Process Time Trigger: 매 5분마다 작업 실행
TriggerResult triggerResult = input
    .windowAll(TumblingEventTimeWindows.of(Time.minutes(5)))
    .trigger(ProcessingTimeTrigger.create())
    .process(new YourProcessFunction());

// Event Time Trigger: 이벤트 시간이 현재 시간보다 10초 이전인 경우 작업 실행
TriggerResult triggerResult = input
    .windowAll(TumblingEventTimeWindows.of(Time.minutes(1)))
    .trigger(EventTimeTrigger.before(Time.seconds(10)))
    .process(new YourProcessFunction());

// Watermark Time Trigger: 워터마크가 현재 시간보다 1분 이후인 경우 작업 실행
TriggerResult triggerResult = input
    .windowAll(TumblingProcessingTimeWindows.of(Time.seconds(10)))
    .trigger(WatermarkTrigger.afterEndOfWindow())
    .process(new YourProcessFunction());
```

## 마무리

아파치 플링크의 트리거는 데이터 처리 작업의 제어를 위해 중요한 개념입니다. 프로세스 타임, 이벤트 타임 및 워터마크 타임 트리거를 이용하여 작업을 효율적으로 실행할 수 있습니다. 플링크는 트리거 설정에 많은 유연성을 제공하므로 다양한 요구 사항에 맞춰 작업을 설정할 수 있습니다.

더 자세한 내용은 [아파치 플링크 공식 문서](https://ci.apache.org/projects/flink/flink-docs-stable/)를 참조하시기 바랍니다.