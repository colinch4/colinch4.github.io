---
layout: post
title: "[java] 아파치 플링크의 결과 소비(Result consumption in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대규모 데이터 처리를 위한 분산 처리 시스템으로, 데이터를 효과적으로 처리하고 분석하는 데에 사용됩니다. 이 글에서는 플링크에서의 결과 소비에 대해 알아보겠습니다. 결과 소비는 플링크의 실행 결과를 실제로 사용하는 것을 의미합니다.

## 결과 소비 방법

### Collect

`collect()` 메서드를 사용하면 플링크의 결과를 로컬 컬렉션으로 수집할 수 있습니다. 이 메서드는 플링크의 데이터스트림 동작을 끝내고, 최종 결과를 로컬 컬렉션으로 모아 반환합니다.

```java
DataStream<Integer> stream = ...; // 플링크 데이터스트림 생성
List<Integer> result = stream.collect();
```

### Write

`write()` 메서드를 사용하면 플링크의 결과를 외부 저장소로 저장할 수 있습니다. 예를 들어, 파일 시스템, 데이터베이스, 메시지 큐 등의 저장소에 결과를 쓰는 것이 가능합니다.

```java
DataStream<String> stream = ...; // 플링크 데이터스트림 생성
stream.writeAsText("/path/to/file");
```

### Sink

Sink 함수를 사용하여 결과를 특정 장치나 시스템으로 전송할 수 있습니다. 예를 들어, 외부 API 호출, 웹 소켓 연결, 이메일 등의 기능을 통해 결과를 외부로 전송할 수 있습니다.

```java
DataStream<Event> stream = ...; // 플링크 데이터스트림 생성
stream.addSink(new EventSink());
```

## 후속 동작

결과 소비 이후에는 다른 동작을 수행할 수 있습니다. 예를 들어, 결과를 다른 플링크 작업에 사용하거나 통계 정보를 계산하는 등의 후속 동작을 수행할 수 있습니다.

```java
DataStream<Integer> stream = ...; // 플링크 데이터스트림 생성

DataStream<Double> average = stream.windowAll() // 모든 요소에 대한 윈도우 생성
    .trigger(CountTrigger.of(100)) // 100개의 요소를 받으면 트리거
    .apply(new AverageFunction()); // 평균을 계산하는 사용자 정의 함수 적용
```

## 결론

아파치 플링크에서는 다양한 방법으로 결과를 소비할 수 있습니다. `collect()`, `write()`, `Sink` 함수를 사용하여 결과를 로컬 컬렉션에 저장하거나 외부 저장소로 쓰거나 외부로 전송할 수 있습니다. 이후 결과에 대한 후속 동작을 수행하여 데이터를 분석하거나 추가 처리할 수 있습니다.