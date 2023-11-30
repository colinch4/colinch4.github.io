---
layout: post
title: "[java] Apache Commons Collections에서의 컬렉션 조작 기능"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---
Apache Commons Collections는 Java에서 다양한 유용한 컬렉션 조작 기능을 제공하는 라이브러리입니다. 이 라이브러리는 JDK의 기본 컬렉션 프레임워크를 보완하여 보다 편리한 사용을 가능하게 해줍니다. 이번 블로그 포스트에서는 Apache Commons Collections에서의 주요 컬렉션 조작 기능에 대해 살펴보겠습니다.

## 1. 컬렉션 변환
Apache Commons Collections는 다른 형태의 컬렉션으로의 변환을 쉽게 할 수 있는 기능을 제공합니다. `CollectionUtils` 클래스의 `collect` 메서드를 사용하여 변환할 컬렉션과 변환할 타입을 지정할 수 있습니다. 다음은 ArrayList를 HashSet으로 변환하는 예제입니다.

```java
import org.apache.commons.collections4.CollectionUtils;

List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
Set<Integer> set = CollectionUtils.collect(list, HashSet::new);
```

## 2. 컬렉션 필터링
Apache Commons Collections는 컬렉션의 원소를 필터링하여 원하는 조건에 맞는 원소만 남기는 기능을 제공합니다. `CollectionUtils` 클래스의 `select` 메서드를 사용하여 필터링할 컬렉션과 필터 조건을 지정할 수 있습니다. 다음은 숫자 리스트에서 짝수만 남기는 예제입니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.Predicate;

List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
Predicate<Integer> evenPredicate = number -> number % 2 == 0;
Collection<Integer> evenNumbers = CollectionUtils.select(list, evenPredicate);
```

## 3. 컬렉션 변환 및 필터링의 조합
Apache Commons Collections는 컬렉션 변환과 필터링을 동시에 수행할 수 있는 기능도 제공합니다. `CollectionUtils` 클래스의 `collect` 메서드와 `select` 메서드를 조합하여 원하는 결과를 얻을 수 있습니다. 다음은 문자열 리스트에서 길이가 3 이하인 원소들만 남기고, HashSet으로 변환하는 예제입니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.Predicate;

List<String> list = Arrays.asList("apple", "banana", "cat", "dog");
Predicate<String> lengthPredicate = str -> str.length() <= 3;
Set<String> result = CollectionUtils.collect(CollectionUtils.select(list, lengthPredicate), HashSet::new);
```

## 4. 컬렉션의 정렬
Apache Commons Collections는 컬렉션의 정렬 기능을 제공합니다. `Comparator` 인터페이스를 구현하여 정렬할 기준을 지정하고, `ComparatorUtils` 클래스의 `collatedComparator` 메서드를 사용하여 정렬된 컬렉션을 얻을 수 있습니다. 다음은 문자열 리스트를 길이에 따라 오름차순으로 정렬하는 예제입니다.

```java
import org.apache.commons.collections4.ComparatorUtils;

List<String> list = Arrays.asList("apple", "banana", "cat", "dog");
Comparator<String> lengthComparator = (str1, str2) -> str1.length() - str2.length();
List<String> sortedList = ComparatorUtils.collated(list, lengthComparator);
```

## 마무리
Apache Commons Collections의 컬렉션 조작 기능을 활용하면 Java에서 컬렉션을 다루는 작업을 편리하게 할 수 있습니다. 이번 블로그 포스트에서는 컬렉션 변환, 컬렉션 필터링, 컬렉션 정렬 기능에 대해 알아보았습니다. Apache Commons Collections의 다양한 기능을 활용하여 코드를 더욱 간결하고 효율적으로 작성할 수 있습니다.

> 참고: [Apache Commons Collections](https://commons.apache.org/proper/commons-collections/)