---
layout: post
title: "[java] 아파치 플링크의 쓰레드 로컬 상태(Thread-local state in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대규모 데이터 처리 및 분석을 위한 오픈 소스 분산 처리 프레임워크입니다. 이러한 프레임워크는 많은 작업을 병렬로 실행하기 위해 다수의 쓰레드를 사용합니다. 그 중에서도 특정 작업에 대한 상태 유지를 위해 쓰레드 로컬 상태(Thread-local state)를 사용할 수 있습니다.

## 쓰레드 로컬 상태란?

쓰레드 로컬 상태는 특정 쓰레드에서만 관리되는 상태를 말합니다. 다른 쓰레드에서는 접근할 수 없으며, 해당 쓰레드의 실행 컨텍스트에서만 유효합니다. 이를 통해 각 쓰레드가 독립적인 값을 유지하며, 상태를 공유하지 않고 직접적인 접근을 제한할 수 있습니다.

아파치 플링크에서는 쓰레드 로컬 상태를 사용하여 특정 작업의 중간 결과나 계산된 값 등을 관리할 수 있습니다. 예를 들어, 맵(map) 또는 리듀스(reduce) 작업을 수행하는 동안 중간 결과를 쓰레드 로컬 상태에 저장할 수 있습니다.

## 쓰레드 로컬 상태의 활용

쓰레드 로컬 상태는 다양한 상황에서 유용하게 사용될 수 있습니다. 주요 활용 예시는 다음과 같습니다:

- **중간 결과의 저장**: 맵(map) 또는 리듀스(reduce) 작업 중에 발생하는 중간 결과를 쓰레드 로컬 상태에 저장하여 메모리 사용을 최적화하고, 다른 쓰레드와 독립적으로 값을 유지할 수 있습니다.
- **상태 유지**: 특정 작업에 필요한 상태를 쓰레드 로컬 상태에 저장하여 다른 쓰레드 간의 상태 공유 문제를 피할 수 있습니다. 이를 통해 복잡한 동기화 문제를 효과적으로 해결할 수 있습니다.

## 쓰레드 로컬 상태 사용 예시

아래는 Java 코드를 사용하여 쓰레드 로컬 상태를 활용한 예시입니다.

```java
public class MyMapper extends RichMapFunction<Integer, String> {
    private transient MapState<String, Integer> localState;

    @Override
    public void open(Configuration parameters) throws Exception {
        super.open(parameters);
        localState = getRuntimeContext().getMapState(
                new MapStateDescriptor<>("localState", String.class, Integer.class));
    }

    @Override
    public String map(Integer value) throws Exception {
        // 현재 쓰레드의 값 추출
        Integer threadValue = localState.get("thread-" + Thread.currentThread().getId());

        // 쓰레드 로컬 상태 업데이트
        if (threadValue == null) {
            threadValue = 0;
        }
        threadValue += value;
        localState.put("thread-" + Thread.currentThread().getId(), threadValue);

        // 결과 반환
        return "Thread " + Thread.currentThread().getId() + " value: " + threadValue;
    }
}
```

위의 코드에서는 `RichMapFunction`을 상속하는 `MyMapper` 클래스에서 쓰레드 로컬 상태를 활용합니다. `open()` 메서드에서 `localState` 변수를 초기화하여 현재 쓰레드의 맵 상태에 접근할 수 있습니다. `map()` 메서드에서는 중간 결과를 쓰레드 로컬 상태에 저장하고, 해당 값을 조작하여 반환합니다.

## 결론

아파치 플링크의 쓰레드 로컬 상태는 병렬 처리를 위해 사용되는 쓰레드 간의 값 공유 문제를 효과적으로 해결하는 도구입니다. 중간 결과의 저장이나 상태 유지 등 다양한 상황에서 활용할 수 있으며, Java의 예시 코드를 통해 쓰레드 로컬 상태의 사용 방법을 살펴보았습니다.

> 참고 문서: [Apache Flink - Managing State](https://ci.apache.org/projects/flink/flink-docs-release-1.14/docs/concepts/stateful-stream-processing/#managing-state)