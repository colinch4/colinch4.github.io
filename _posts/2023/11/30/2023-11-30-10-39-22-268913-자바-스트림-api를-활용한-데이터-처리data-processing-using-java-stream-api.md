---
layout: post
title: "[java] 자바 스트림 API를 활용한 데이터 처리(Data processing using Java Stream API)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

자바 8부터 도입된 스트림(Stream) API는 데이터 처리를 간결하게 작성할 수 있는 기능을 제공합니다. 스트림은 데이터 요소로 이루어진 일련의 연속된 데이터를 다룰 수 있는 인터페이스입니다. 이를 통해 컬렉션, 배열 등의 데이터를 필터링, 매핑, 정렬 등 다양한 연산을 수행할 수 있습니다.

## 스트림 생성하기

스트림은 다양한 데이터 소스로부터 생성할 수 있습니다. 예를 들어, 컬렉션의 요소를 스트림으로 변환하거나, 배열로부터 직접 스트림을 생성할 수 있습니다.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

// 리스트를 스트림으로 변환하기
Stream<Integer> stream1 = numbers.stream();

// 배열로부터 스트림 생성하기
String[] fruits = {"apple", "banana", "orange"};
Stream<String> stream2 = Arrays.stream(fruits);
```

## 중간 연산과 최종 연산

스트림은 중간 연산과 최종 연산으로 구성됩니다. 중간 연산은 스트림을 반환하기 때문에 여러 개의 중간 연산을 연속해서 적용할 수 있습니다. 최종 연산은 스트림을 닫고 결과를 반환합니다.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

// 중간 연산: filter
Stream<Integer> stream = numbers.stream().filter(n -> n % 2 == 0);

// 중간 연산: map
Stream<String> mappedStream = stream.map(n -> "Number: " + n);

// 최종 연산: forEach
mappedStream.forEach(System.out::println);
```

## 스트림 연산 예제

다음은 스트림 API를 사용하여 데이터 처리하는 간단한 예제입니다.

```java
List<String> fruits = Arrays.asList("apple", "banana", "orange", "grape", "kiwi");

// 특정 문자열로 시작하는 과일 필터링하기
List<String> filteredFruits = fruits.stream()
                                   .filter(fruit -> fruit.startsWith("a"))
                                   .collect(Collectors.toList());

// 과일 이름을 대문자로 변경하기
List<String> uppercasedFruits = fruits.stream()
                                      .map(String::toUpperCase)
                                      .collect(Collectors.toList());

// 과일 이름을 정렬하기
List<String> sortedFruits = fruits.stream()
                                 .sorted()
                                 .collect(Collectors.toList());
```

위의 예제에서는 `filter`, `map`, `sorted` 등의 중간 연산을 사용하여 과일 데이터를 처리하고, `collect`를 사용하여 최종 결과를 수집합니다.

## 결론

자바의 스트림 API를 활용하면 데이터 처리를 더 간결하고 효율적으로 작성할 수 있습니다. 스트림을 사용하면 반복문이나 조건문을 작성할 필요 없이 메서드 체이닝을 통해 데이터를 변환하고 조작할 수 있습니다. 스트림을 잘 활용하면 코드의 가독성을 높이고 유지보수성을 개선할 수 있습니다.

## 참고 자료

- [Java Stream API Documentation](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/stream/package-summary.html)