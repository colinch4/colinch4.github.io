---
layout: post
title: "[java] 아파치 플링크의 이벤트 타임 처리(Event time processing in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 대규모 실시간 데이터 처리를 위한 오픈 소스 분산 스트리밍 처리 프레임워크입니다. 이벤트 타임(event time)은 데이터 스트림 처리에서 매우 중요한 개념으로, 데이터가 생성된 실제 시간을 기준으로 처리하는 방식입니다. 이벤트 타임 처리를 올바르게 구현하기 위해서는 플링크의 내장된 기능을 활용해야 합니다.

## 이벤트 타임 처리의 필요성
데이터 스트림은 일반적으로 네트워크 지연이나 데이터 전송 지연 등으로 인해 이벤트가 입력된 순서대로 처리되지 않을 수 있습니다. 예를 들어, 센서에서 생성된 데이터가 네트워크를 통해 전송되는 동안 지연이 발생하면 먼저 생성된 이벤트보다 뒤에 생성된 이벤트가 먼저 도착할 수 있습니다.

따라서 이벤트 타임 처리는 데이터가 생성된 순서와 상관없이 데이터를 처리하는데 필요합니다. 이를 통해 정확한 분석 및 처리 결과를 얻을 수 있으며, 실시간 대시보드, 이상 탐지, 윈도우 연산 등 다양한 작업에 유용하게 활용할 수 있습니다.

## 플링크에서의 이벤트 타임 처리
아파치 플링크는 이벤트 타임 처리를 위한 다양한 내장 기능을 제공합니다. 플링크는 데이터의 생성 시간을 추적하고 관리하기 위해 워터마크(watermark)라는 개념을 도입하였습니다. 워터마크는 데이터 스트림에서 처리해야 할 이벤트의 기준 시간을 정의하며, 데이터 스트림 내의 최대 허용된 지연 시간을 나타냅니다.

플링크에서 이벤트 타임 처리를 구현하는 방법은 다음과 같습니다:

### 1. 데이터 소스 설정
플링크에서는 데이터 스트림의 소스를 정의할 때, 소스의 이벤트 타임을 명시적으로 설정해야 합니다. 이를 통해 플링크는 워터마크를 생성하고, 이벤트 타임별로 데이터를 재배치할 수 있습니다.

```java
DataStream<MyEvent> stream = env.addSource(new MySource())
    .assignTimestampsAndWatermarks(new MyTimestampExtractor());
```

### 2. 워터마크 생성
플링크는 데이터 스트림에서 워터마크를 생성하여 이벤트 타임의 진행 상황을 추적합니다. 워터마크는 특정 시간 간격으로 생성되며, 현재 처리 중인 이벤트 시간을 기준으로 지정된 지연 시간만큼 이벤트 타임을 진행시킵니다.

```java
public class MyTimestampExtractor implements AssignerWithPeriodicWatermarks<MyEvent> {

    private final long maxAllowedDelay = 5000; // 최대 허용 지연 시간

    @Override
    public long extractTimestamp(MyEvent event, long previousElementTimestamp) {
        return event.getTimestamp(); // 이벤트의 타임스탬프 반환
    }

    @Override
    public Watermark getCurrentWatermark() {
        // 현재 시간으로부터 허용된 지연 시간 이전의 이벤트까지 처리하는 데 사용되는 워터마크 생성
        return WatermarkUtil.forBoundedOutOfOrderness(maxAllowedDelay);
    }
}
```

### 3. 이벤트 타임 윈도우 연산
이벤트 타임을 기준으로 윈도우 연산을 수행할 수 있습니다. 예를 들어, 5분마다 최근 이벤트 타임 창의 합계를 계산하고 결과를 저장할 수 있습니다.

```java
DataStream<MyEvent> stream = ...;

stream
    .keyBy(MyEvent::getKey)
    .window(TumblingEventTimeWindows.of(Time.minutes(5)))
    .reduce((a, b) -> new MyEvent(a.getKey(), a.getValue() + b.getValue()))
    .addSink(new MySink());
```

위 예제에서는 `TumblingEventTimeWindows`를 사용하여 이벤트 타임을 기반으로 5분 단위로 윈도우를 생성하고, 윈도우 내의 이벤트를 더해서 합계를 계산하여 `MySink`에 저장합니다.

## 결론
아파치 플링크는 이벤트 타임 처리를 위한 강력한 도구를 제공하여 실시간 데이터 처리 작업을 더욱 간편하고 정확하게 수행할 수 있습니다. 이를 통해 실시간 대시보드, 이상 탐지, 윈도우 연산 등 다양한 작업에 유용하게 활용할 수 있습니다.