---
layout: post
title: "[java] 아파치 플링크의 워터마크(Watermarks in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 대규모 스트림 처리를 위한 오픈소스 분산처리 프레임워크입니다. 이 프레임워크는 스트림 처리에서 중요한 개념 중 하나인 **워터마크(Watermark)**를 지원합니다.

## 워터마크란?

워터마크는 스트림 데이터 처리에서 이벤트 시간별 업데이트를 가능하게 하는 개념입니다. 이벤트 시간은 데이터가 생성된 시간을 의미하며, 데이터 처리에서 이벤트 시간 기반의 연산(logical time-window)을 수행하기 위해 워터마크를 사용합니다. 워터마크는 이벤트 시간의 최대 손실을 나타내며, 특정 시간 이후의 이벤트는 처리되지 않도록 하기 위해 사용됩니다.

## 아파치 플링크에서의 워터마크

아파치 플링크에서 워터마크를 사용하기 위해서는 `WatermarkAssigner`를 구현해야 합니다. 이 인터페이스는 `assignWatermark` 메서드를 구현하여 입력 스트림의 각 이벤트에 워터마크를 할당합니다. 예를 들어, 아래의 코드는 시간 기반의 워터마크를 생성하는 간단한 예시입니다.

```java
public class MyWatermarkAssigner implements WatermarkAssigner<MyEvent> {
    private static final long MAX_DELAY = 5000; // 워터마크의 최대 연기 시간

    @Override
    public Watermark assignWatermark(MyEvent event, long eventTimestamp) {
        // 최대 연기 시간 전에 워터마크를 할당하도록 조정
        long watermarkTimestamp = eventTimestamp - MAX_DELAY;
        return new Watermark(watermarkTimestamp);
    }
}
```

이렇게 생성한 `WatermarkAssigner`를 사용하여 스트림 데이터에 워터마크를 할당할 수 있습니다. 예를 들어, 다음과 같이 `assignTimestampsAndWatermarks` 메서드를 사용하여 워터마크를 할당할 수 있습니다.

```java
DataStream<MyEvent> events = ...; // 입력 스트림

DataStream<MyEvent> withWatermarks = events
    .assignTimestampsAndWatermarks(new MyWatermarkAssigner());
```

## 워터마크의 활용

아파치 플링크에서 워터마크를 활용하여 다양한 기능을 수행할 수 있습니다. 다음은 일부 유용한 워터마크 활용 사례입니다.

- **이벤트 시간 기반 윈도우 처리**: 워터마크를 사용하여 이벤트 시간으로 윈도우를 구성하고 처리할 수 있습니다.
- **지연된 이벤트 처리**: 워터마크를 사용하여 지연된 이벤트를 건너뛰거나 처리를 연기할 수 있습니다.
- **타임아웃 처리**: 워터마크를 사용하여 특정 시간 이후에 처리되지 않은 이벤트를 타임아웃으로 간주할 수 있습니다.

## 결론

아파치 플링크의 워터마크는 스트림 데이터 처리에서 이벤트 시간 기반의 연산을 수행하기 위한 중요한 개념입니다. 워터마크를 활용하여 이벤트 시간에 따라 윈도우 처리와 지연된 이벤트 처리 등 다양한 작업을 수행할 수 있습니다.