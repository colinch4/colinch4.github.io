---
layout: post
title: "[java] 자바 스트림 연산자와 아파치 플링크 연산자 비교(Comparison of Java Stream operators and Apache Flink operators)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

스트림은 자바 8부터 도입된 기능으로, 데이터를 처리하기 위한 고수준의 추상화입니다. 스트림은 데이터 처리를 수행하기 위한 다양한 연산자를 제공하는데, 이 연산자들을 사용하여 데이터를 처리하고 결과를 얻을 수 있습니다.

아파치 플링크는 대규모 분산 처리를 위한 엔진으로, 맵리듀스 작업을 보다 쉽게 구현할 수 있도록 해줍니다. 플링크도 스트림과 비슷한 개념을 사용하여 데이터 처리를 수행하며, 다양한 연산자를 제공합니다.

이번 글에서는 자바 스트림 연산자와 아파치 플링크 연산자를 비교해보고, 각각의 특징과 사용법에 대해 알아보겠습니다.

## 1. 맵(Map) 연산자 비교

맵 연산자는 스트림의 각 요소에 대해 지정된 함수를 적용하여 새로운 요소를 생성하는 연산자입니다.

### 자바 스트림에서의 맵 연산자 사용법

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> squaredNumbers = numbers.stream()
                                      .map(n -> n * n)
                                      .collect(Collectors.toList());
```

### 아파치 플링크에서의 맵 연산자 사용법

```java
DataSet<Integer> numbers = env.fromCollection(Arrays.asList(1, 2, 3, 4, 5));
DataSet<Integer> squaredNumbers = numbers.map(new MapFunction<Integer, Integer>() {
    @Override
    public Integer map(Integer value) throws Exception {
        return value * value;
    }
});
```

## 2. 필터(Filter) 연산자 비교

필터 연산자는 스트림의 각 요소를 평가하여 지정된 조건에 부합하는 요소만을 포함하는 연산자입니다.

### 자바 스트림에서의 필터 연산자 사용법

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> evenNumbers = numbers.stream()
                                   .filter(n -> n % 2 == 0)
                                   .collect(Collectors.toList());
```

### 아파치 플링크에서의 필터 연산자 사용법

```java
DataSet<Integer> numbers = env.fromCollection(Arrays.asList(1, 2, 3, 4, 5));
DataSet<Integer> evenNumbers = numbers.filter(new FilterFunction<Integer>() {
    @Override
    public boolean filter(Integer value) throws Exception {
        return value % 2 == 0;
    }
});
```

## 3. 리듀스(Reduce) 연산자 비교

리듀스 연산자는 스트림의 모든 요소를 하나로 결합하거나, 요소들을 평가하여 단일 결과를 생성하는 연산자입니다.

### 자바 스트림에서의 리듀스 연산자 사용법

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
int sum = numbers.stream().reduce(0, (a, b) -> a + b);
```

### 아파치 플링크에서의 리듀스 연산자 사용법

```java
DataSet<Integer> numbers = env.fromCollection(Arrays.asList(1, 2, 3, 4, 5));
int sum = numbers.reduce(new ReduceFunction<Integer>() {
    @Override
    public Integer reduce(Integer value1, Integer value2) throws Exception {
        return value1 + value2;
    }
});
```

## 결론

자바 스트림과 아파치 플링크는 데이터 처리를 위한 다양한 연산자를 제공하며 각각의 특징과 사용법이 있습니다. 프로젝트의 요구사항과 환경에 따라 선택적으로 사용할 수 있으며, 각각의 장단점을 고려하여 적절히 활용하는 것이 중요합니다.

## 참고 자료

- [Java 8 Streams Tutorial](https://www.baeldung.com/java-8-streams)
- [Apache Flink Documentation](https://ci.apache.org/projects/flink/flink-docs-release-1.10/)