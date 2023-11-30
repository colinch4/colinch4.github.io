---
layout: post
title: "[java] 아파치 플링크의 윈도우 처리(Window processing in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대용량의 스트림 및 배치 데이터 처리를 위한 분산 처리 프레임워크입니다. 이 프레임워크는 데이터를 윈도우(Window)라는 시간 기반의 논리적인 블록으로 분할하여 처리할 수 있습니다. 윈도우 처리는 특정 시간 범위 내에서 데이터를 그룹화하고 집계하는 기능을 제공합니다.

## 윈도우 유형

플링크에서는 다양한 윈도우 유형을 지원하며, 여기에는 시간 기반 윈도우와 카운팅 기반 윈도우가 포함됩니다.

### 시간 기반 윈도우

시간 기반 윈도우는 데이터 스트림을 지정된 시간 간격으로 분할하는 윈도우입니다. 예를 들어, 5분 윈도우는 5분 동안의 데이터를 하나의 윈도우로 그룹화합니다. 플링크에서는 다음과 같은 시간 기반 윈도우 유형을 지원합니다.

- Tumbling Windows: 첫 번째 윈도우의 끝부터 지정된 간격으로 윈도우를 정렬하여 데이터를 처리합니다. 즉, 이전 윈도우가 완료되기 전에 새로운 윈도우가 시작될 수 있습니다.
- Sliding Windows: 지정된 윈도우 크기와 지정된 슬라이딩 간격을 사용하여 데이터를 처리합니다. 이 경우, 윈도우가 겹칠 수 있으므로 하나의 데이터에 대해 여러 윈도우에서 처리될 수 있습니다.
- Session Windows: 특정 간격 내에서 데이터가 동일한 키에 속하는 경우 그룹화하여 처리합니다. 이 유형의 윈도우는 정지 기간이 있는 데이터 스트림을 처리하는데 효과적입니다.

### 카운팅 기반 윈도우

카운팅 기반 윈도우는 지정된 이벤트 수나 특정 속성 값의 수에 따라 데이터를 분할하는 윈도우입니다. 예를 들어, 100개의 이벤트 윈도우는 100개의 이벤트가 도착할 때마다 윈도우를 생성합니다.

## 윈도우 처리 예제

다음은 플링크를 사용하여 간단한 윈도우 처리를 수행하는 예제 코드입니다. 이 예제에서는 5분 동안의 데이터를 단일 윈도우로 그룹화하고 해당 윈도우에서 데이터를 집계합니다.

```java
import org.apache.flink.api.common.functions.AggregateFunction;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.TumblingProcessingTimeWindows;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.streaming.api.windowing.windows.TimeWindow;

public class WindowProcessingExample {

    public static void main(String[] args) throws Exception {
        // Flink 실행 환경 생성
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // 데이터를 수신하는 데이터 스트림 생성
        DataStream<MyEvent> eventDataStream = env.addSource(new MyEventSource());

        // 5분 동안의 윈도우를 생성하고 윈도우 내에서 데이터를 집계하는 예제
        DataStream<AggregateResult> aggregatedStream = eventDataStream
            .keyBy(MyEvent::getKey)
            .window(TumblingProcessingTimeWindows.of(Time.minutes(5)))
            .aggregate(new MyAggregateFunction());

        // 결과를 출력하는 Sink 연결 및 실행
        aggregatedStream.print();

        env.execute("Window Processing Example");
    }

    // 사용자 정의 이벤트 클래스
    public static class MyEvent {
        private long timestamp;
        private String key;
        private int value;

        // 생성자, getter 및 setter는 생략

        public long getTimestamp() {
            return timestamp;
        }
    }

    // 집계 결과 클래스
    public static class AggregateResult {
        private String key;
        private int count;
        private double sum;

        // 생성자, getter 및 setter는 생략
    }

    // 사용자 정의 집계 함수
    public static class MyAggregateFunction implements AggregateFunction<MyEvent, AggregateResult, AggregateResult> {
        @Override
        public AggregateResult createAccumulator() {
            return new AggregateResult();
        }

        @Override
        public AggregateResult add(MyEvent value, AggregateResult accumulator) {
            accumulator.setKey(value.getKey());
            accumulator.setCount(accumulator.getCount() + 1);
            accumulator.setSum(accumulator.getSum() + value.getValue());
            return accumulator;
        }

        @Override
        public AggregateResult getResult(AggregateResult accumulator) {
            return accumulator;
        }

        @Override
        public AggregateResult merge(AggregateResult a, AggregateResult b) {
            a.setCount(a.getCount() + b.getCount());
            a.setSum(a.getSum() + b.getSum());
            return a;
        }
    }
}
```

위의 예제에서는 `MyEvent`라는 사용자 정의 이벤트 클래스와 `AggregateResult`라는 집계 결과 클래스를 선언하고, `MyAggregateFunction`이라는 사용자 정의 집계 함수를 구현합니다. `window` 메서드를 사용하여 5분 동안의 윈도우를 생성하고, `aggregate` 메서드를 사용하여 윈도우 내에서 데이터를 집계합니다. 마지막으로, `print` 메서드를 사용하여 결과를 출력합니다.

## 결론

아파치 플링크의 윈도우 처리 기능을 사용하면 시간 기반 또는 카운팅 기반으로 데이터를 그룹화하고 집계할 수 있습니다. 윈도우 처리는 스트림 및 배치 데이터 처리에 유연성과 효율성을 제공하는 중요한 기능입니다. 아파치 플링크의 다양한 윈도우 유형과 관련된 예제 코드를 통해 윈도우 처리의 이해도를 높일 수 있습니다.

## 참고 자료

- [Apache Flink - Windowing](https://ci.apache.org/projects/flink/flink-docs-stable/dev/stream/operators/windows.html)
- [Apache Flink - Window API](https://ci.apache.org/projects/flink/flink-docs-stable/dev/stream/operators/windows.html#window-api)