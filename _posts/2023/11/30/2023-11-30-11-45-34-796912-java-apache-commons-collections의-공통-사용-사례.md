---
layout: post
title: "[java] Java Apache Commons Collections의 공통 사용 사례"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 개발자들에게 많은 유용한 데이터 구조와 알고리즘을 제공하는 라이브러리입니다. 이 라이브러리를 사용하면 다양한 상황에서 코드 작성을 간소화하고 성능을 향상시킬 수 있습니다. 이번 글에서는 Apache Commons Collections의 일반적인 사용 사례 몇 가지를 살펴보겠습니다.

## 1. Collection 변환

Apache Commons Collections를 사용하면 다양한 Collection 객체 간에 변환을 손쉽게 할 수 있습니다. 예를 들어, List를 Set으로 변환하거나, Map을 List로 변환하는 등의 작업이 가능합니다.

```java
import org.apache.commons.collections4.CollectionUtils;

List<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
list.add("Orange");

Set<String> set = CollectionUtils.collect(list.iterator(), i -> i.toString());

List<String> newList = CollectionUtils.collect(set.iterator(), i -> i.toString());
```

위의 예제에서는 `CollectionUtils.collect()` 메소드를 사용하여 List와 Set 사이를 변환하는 방법을 보여줍니다.

## 2. 컬렉션 필터링

Apache Commons Collections를 사용하면 컬렉션에서 원하는 항목만 필터링하여 추출할 수 있습니다. 예를 들어, 숫자 목록에서 짝수만 필터링하여 새로운 목록으로 추출할 수 있습니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.PredicateUtils;

List<Integer> numbers = new ArrayList<>();
numbers.add(1);
numbers.add(2);
numbers.add(3);
numbers.add(4);
numbers.add(5);

List<Integer> evenNumbers = (List<Integer>) CollectionUtils.select(numbers, PredicateUtils.dividePredicate(2));
```

위의 예제에서는 `CollectionUtils.select()` 메소드를 사용하여 숫자 목록에서 짝수를 필터링하여 추출하는 방법을 보여줍니다.

## 3. 컬렉션 변환 및 수정

Apache Commons Collections를 사용하면 컬렉션을 변환하거나 수정하는 여러 가지 유틸리티 메소드를 제공합니다. 예를 들어, 모든 항목을 대문자로 변환하거나 중복 항목을 제거하는 등의 작업이 가능합니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.TransformerUtils;

List<String> names = new ArrayList<>();
names.add("james");
names.add("john");
names.add("michael");

List<String> upperCaseNames = (List<String>) CollectionUtils.collect(names, TransformerUtils.stringValueTransformer(String::toUpperCase));
```

위의 예제에서는 `CollectionUtils.collect()`와 `TransformerUtils.stringValueTransformer()` 메소드를 사용하여 모든 이름을 대문자로 변환하는 방법을 보여줍니다.

## 결론

Apache Commons Collections는 Java 개발자들에게 다양한 상황에서 유용한 기능을 제공하는 라이브러리입니다. 이 글에서는 Collection 변환, 컬렉션 필터링, 컬렉션 변환 및 수정의 세 가지 주요 사용 사례를 살펴보았습니다. Apache Commons Collections를 사용하면 코드 작성과 유지 보수를 간소화하고 성능을 향상시킬 수 있습니다.

더 자세한 내용은 [Apache Commons Collections](https://commons.apache.org/proper/commons-collections/) 사이트를 참조하세요.