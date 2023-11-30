---
layout: post
title: "[java] 아파치 플링크의 창 조작(Window manipulation in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대규모 데이터 스트림 처리를 위한 오픈소스 플랫폼입니다. 이 플랫폼은 창(Window) 기반의 연산을 지원하여 데이터 스트림을 세분화하고 더 효율적으로 처리할 수 있습니다. 이번 포스트에서는 아파치 플링크에서 창을 조작하는 방법에 대해 알아보겠습니다.

## 창(Window) 개념 이해하기
창(Window)은 특정 기간 동안 데이터 스트림을 분리하고 처리하기 위해 사용됩니다. 예를 들어, 1분 단위로 도착하는 로그 데이터 스트림에서 1분간의 로그를 분석하고 집계하는 작업을 할 때, 1분을 단위로 창을 설정하여 작업을 수행할 수 있습니다.

## 시간 기반 창(Window)
시간 기반 창(Window)은 데이터 스트림에서 이벤트를 특정 시간 간격으로 나누는 기능입니다. 아파치 플링크에서는 이러한 창을 다루기 위해 WindowAssigner 인터페이스를 사용합니다. WindowAssigner 인터페이스를 구현하여 원하는 창을 정의하고 데이터를 창에 할당하게 됩니다.

아래는 일부 WindowAssigner의 예시 코드입니다:

```java
import org.apache.flink.streaming.api.windowing.assigners.*;
import org.apache.flink.streaming.api.windowing.time.Time;

// Tumbling Window
WindowAssigner<Object, TimeWindow> windowAssigner = TumblingEventTimeWindows.of(Time.minutes(1));

// Sliding Window
WindowAssigner<Object, TimeWindow> windowAssigner = SlidingProcessingTimeWindows.of(Time.seconds(10), Time.seconds(5));

// Session Window
WindowAssigner<Object, TimeWindow> windowAssigner = EventTimeSessionWindows.withGap(Time.minutes(5));
```

TimeWindow는 창의 시작 시간과 종료 시간을 표현하는 클래스입니다. TumblingEventTimeWindows, SlidingProcessingTimeWindows, EventTimeSessionWindows 등을 사용하여 어떤 시간 기반의 창을 사용할지 결정할 수 있습니다.

## 창 함수(Window Function)
창 함수(Window Function)는 각 창에서 수행되는 연산을 정의합니다. 아파치 플링크에서는 WindowFunction 인터페이스를 구현하여 창 함수를 정의할 수 있습니다. 이 인터페이스의 apply() 메서드를 오버라이딩하여 각 창에 대해 원하는 연산을 수행합니다.

아래는 일부 WindowFunction의 예시 코드입니다:

```java
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.functions.windowing.WindowFunction;
import org.apache.flink.streaming.api.windowing.windows.TimeWindow;
import org.apache.flink.util.Collector;

public class MyWindowFunction implements WindowFunction<Integer, Tuple2<String, Integer>, String, TimeWindow> {
    @Override
    public void apply(String key, TimeWindow window, Iterable<Integer> input, Collector<Tuple2<String, Integer>> out) throws Exception {
        // 각 창에 대한 연산을 수행하는 로직을 작성합니다.
    }
}
```

위의 예시 코드에서는 입력으로 key, window, input을 받고, 합계를 계산한 뒤 아웃풋으로 key와 해당 창에 대한 합계를 출력하는 로직을 작성하고 있습니다.

## 창 함수 적용하기
창 함수를 사용하기 위해서는 데이터 스트림에 대해 창 할당(Window Assign)과정을 거쳐야 합니다. 아파치 플링크에서는 keyBy()나 window() 메서드를 사용하여 창 할당과 창 함수를 적용할 수 있습니다.

아래는 창 할당과 창 함수 적용을 위한 예시 코드입니다:

```java
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

// 데이터 스트림에 대해 keyBy 후 창 할당 및 창 함수 적용
windowedStream = dataStream
    .keyBy(keySelector)
    .window(windowAssigner)
    .apply(windowFunction);
```

위의 예시 코드에서는 keyBy() 메서드를 사용하여 데이터 스트림을 특정 키(key)에 따라 그룹화합니다. 그 후 window() 메서드와 apply() 메서드를 통해 창 할당 및 창 함수를 적용합니다.

## 결론
이번 포스트에서는 아파치 플링크에서 창을 조작하는 방법에 대해 알아보았습니다. 시간 기반 창을 설정하고, 창 함수를 정의하여 데이터 스트림을 분석하고 처리하는 방법에 대해 다루었습니다. 아파치 플링크의 창 조작 기능을 사용하여 대규모 데이터 스트림 처리를 보다 효율적으로 수행할 수 있습니다.

- 참고: [아파치 플링크 공식 문서(Window API)](https://ci.apache.org/projects/flink/flink-docs-stable/dev/stream/operators/windows.html)