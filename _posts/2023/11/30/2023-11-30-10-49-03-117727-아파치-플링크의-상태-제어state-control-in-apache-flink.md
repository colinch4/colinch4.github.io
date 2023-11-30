---
layout: post
title: "[java] 아파치 플링크의 상태 제어(State control in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

## 소개
아파치 플링크는 대량의 데이터를 처리하는 분산 스트리밍 및 배치 데이터 처리 엔진입니다. 플링크는 실시간으로 처리되는 데이터의 상태를 관리하기 위해 내부적으로 상태 제어 메커니즘을 제공합니다. 이 상태 제어 메커니즘을 사용하면 애플리케이션의 동작을 조정하고 데이터 처리를 멈추거나 다시 시작하는 등의 제어를 할 수 있습니다.

## 상태 제어의 기본 개념
플링크에서는 상태를 통해 데이터 처리의 상태를 추적하고, 필요에 따라 데이터를 저장하고 조회할 수 있습니다. 상태는 플링크 작업의 중간 결과물이며, 플링크 잡이 실행되는 동안 지속되는 데이터 구조입니다.

## 상태 제어 메커니즘
플링크에서는 상태 제어를 위해 다음과 같은 주요 개념을 제공합니다:

1. **키 상태(Keyed State)**: 스트림 데이터의 특정 키에 대한 상태를 저장하기 위한 메커니즘입니다. 키 상태는 마치 분산 맵과 같이 동작하며, 키별로 데이터를 저장하고 조회할 수 있습니다.

2. **연산자 상태(Operator State)**: 플링크 작업 내부의 연산자별로 상태를 저장하기 위한 메커니즘입니다. 연산자 상태는 해당 연산자의 상태를 저장하고, 필요에 따라 체크포인트와 같은 기능을 사용하여 데이터를 영속화할 수 있습니다.

## 키 상태 사용 예시

다음은 플링크에서 키 상태를 사용하는 예시 코드입니다:

```java
import org.apache.flink.streaming.api.functions.KeyedProcessFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.util.Collector;

public class KeyedStateExample {
    public static void main(String[] args) throws Exception {
        // Flink 환경 설정
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // 입력 스트림 생성
        DataStream<Tuple2<String, Integer>> inputDataStream = env.fromCollection(Arrays.asList(
            new Tuple2<>("A", 1),
            new Tuple2<>("B", 2),
            new Tuple2<>("A", 3),
            new Tuple2<>("C", 4)
        ));

        // 키 상태를 사용한 처리
        DataStream<Tuple2<String, Integer>> resultStream = inputDataStream
            .keyBy(0)
            .process(new KeyedProcessFunction<String, Tuple2<String, Integer>, Tuple2<String, Integer>>() {
                private ValueState<Integer> sumState;

                @Override
                public void open(Configuration parameters) throws Exception {
                    sumState = getRuntimeContext().getState(new ValueStateDescriptor<>("sum", Integer.class));
                }

                @Override
                public void processElement(Tuple2<String, Integer> value, Context ctx, Collector<Tuple2<String, Integer>> out) throws Exception {
                    Integer sum = sumState.value();
                    if (sum == null) {
                        sum = 0;
                    }
                    sum += value.f1;
                    sumState.update(sum);
                    out.collect(new Tuple2<>(value.f0, sum));
                }
            });

        // 결과 출력
        resultStream.print();

        // 플링크 잡 실행
        env.execute("Keyed State Example");
    }
}
```

위 코드에서는 입력 스트림을 생성하고, 특정 키에 대한 합계를 계산하는 키 상태를 사용한 처리를 수행합니다. `keyBy` 메서드를 사용하여 입력 데이터를 키별로 그룹화하고, `KeyedProcessFunction` 클래스를 상속받은 사용자 정의 함수를 통해 키 상태를 활용한 데이터 처리를 수행합니다. `open` 메서드에서는 키 상태를 초기화하고, `processElement` 메서드에서는 입력 데이터를 기반으로 키 상태를 업데이트하고 결과를 출력합니다.

## 결론
아파치 플링크의 상태 제어 메커니즘은 데이터 처리 애플리케이션의 상태를 관리하고 제어하는 데 필수적입니다. 키 상태와 연산자 상태를 적절하게 활용하여 실시간 데이터 처리 작업을 유연하게 조정할 수 있습니다.

---

## 참고 자료
- [Flink Documentation: Managing state in Flink](https://ci.apache.org/projects/flink/flink-docs-stable/dev/stream/state/index.html)
- [Flink Documentation: Keyed state](https://ci.apache.org/projects/flink/flink-docs-stable/dev/stream/state/keyed_state.html)
- [Flink Documentation: Operator state](https://ci.apache.org/projects/flink/flink-docs-stable/dev/stream/state/operator_state.html)