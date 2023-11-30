---
layout: post
title: "[java] Apache Commons Collections의 데이터 조회 및 변경 방법"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 개발자들에게 유용한 유틸리티 클래스 및 콜렉션 구현을 제공하는 라이브러리입니다. 이 라이브러리를 사용하여 데이터를 조회하고 변경하는 방법을 살펴보겠습니다.

## 데이터 조회

Apache Commons Collections에서는 다양한 메서드를 사용하여 데이터를 조회할 수 있습니다. 아래는 일반적으로 사용되는 몇 가지 예시입니다.

### 1. List에서 아이템 조회하기

```java
import org.apache.commons.collections4.CollectionUtils;
import java.util.List;

List<String> myList = // List를 어떻게든 초기화
String searchedItem = "example";

boolean isItemPresent = CollectionUtils.contains(myList, searchedItem);
```

위의 예시에서는 CollectionUtils 클래스의 contains() 메서드를 사용하여 List에서 특정 아이템을 조회하고, 해당 아이템이 존재하는지 여부를 확인합니다.

### 2. Map에서 키를 이용하여 값 조회하기

```java
import org.apache.commons.collections4.MapUtils;
import java.util.Map;

Map<String, Integer> myMap = // Map을 어떻게든 초기화
String key = "example";

Integer value = MapUtils.getObject(myMap, key);
```

위의 예시에서는 MapUtils 클래스의 getObject() 메서드를 사용하여 Map에서 특정 키의 값을 조회합니다.

## 데이터 변경

Apache Commons Collections를 사용하여 데이터를 변경하는 방법도 간단합니다. 몇 가지 예시를 살펴보겠습니다.

### 1. List에 아이템 추가하기

```java
import org.apache.commons.collections4.ListUtils;
import java.util.List;

List<String> myList = // List를 어떻게든 초기화

List<String> newList = ListUtils.union(myList, List.of("item1", "item2"));
```

위의 예시에서는 ListUtils 클래스의 union() 메서드를 사용하여 두 개의 List를 결합하고, 새로운 List를 생성합니다.

### 2. Map에 새로운 키-값 쌍 추가하기

```java
import org.apache.commons.collections4.MapUtils;
import java.util.Map;

Map<String, Integer> myMap = // Map을 어떻게든 초기화

Map<String, Integer> newMap = MapUtils.putAll(myMap, Map.of("key1", 1, "key2", 2));
```

위의 예시에서는 MapUtils 클래스의 putAll() 메서드를 사용하여 기존의 Map에 새로운 키-값 쌍을 추가합니다.

## 결론

Apache Commons Collections의 다양한 유틸리티 클래스와 메서드를 활용하면 Java 애플리케이션에서 데이터를 쉽게 조회하고 변경할 수 있습니다. 이러한 기능을 활용하여 개발 작업을 더욱 효율적으로 수행할 수 있습니다.

더 자세한 정보를 원하시면 [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)를 참조해주세요.