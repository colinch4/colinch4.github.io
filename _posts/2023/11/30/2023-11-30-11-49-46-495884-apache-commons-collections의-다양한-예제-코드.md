---
layout: post
title: "[java] Apache Commons Collections의 다양한 예제 코드"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections은 자주 사용되는 자료 구조와 유틸리티 클래스를 제공하는 Java 라이브러리입니다. 이 라이브러리를 사용하여 간단하고 효율적인 코드를 작성할 수 있습니다. 이번 포스트에서는 Apache Commons Collections의 몇 가지 예제 코드를 소개하겠습니다.

## Apache Commons Collections 설치

먼저 Apache Commons Collections를 사용하기 위해 라이브러리를 설치해야 합니다. Maven 프로젝트의 경우 `pom.xml` 파일에 다음 종속성을 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-collections4</artifactId>
        <version>4.4</version>
    </dependency>
</dependencies>
```

Gradle 프로젝트의 경우 `build.gradle` 파일에 다음 종속성을 추가합니다.

```groovy
dependencies {
    implementation 'commons-collections:commons-collections:4.4'
}
```

## 예제 코드

### 1. 리스트 관련 코드

Apache Commons Collections를 사용하면 다양한 유형의 리스트를 손쉽게 다룰 수 있습니다. 아래는 몇 가지 리스트 관련 예제 코드입니다.

```java
import org.apache.commons.collections4.ListUtils;

// 두 개의 리스트를 병합하는 예제
List<Integer> list1 = Arrays.asList(1, 2, 3);
List<Integer> list2 = Arrays.asList(4, 5, 6);
List<Integer> mergedList = ListUtils.union(list1, list2);
System.out.println(mergedList); // 출력: [1, 2, 3, 4, 5, 6]

// 리스트에서 중복된 요소를 제거하는 예제
List<Integer> duplicateList = Arrays.asList(1, 2, 2, 3, 4, 4, 5);
List<Integer> uniqueList = ListUtils.removeAllOccurrences(duplicateList, 2);
System.out.println(uniqueList); // 출력: [1, 3, 4, 4, 5]
```

### 2. 맵 관련 코드

Apache Commons Collections를 사용하여 맵을 다루는 예제입니다.

```java
import org.apache.commons.collections4.MapUtils;

// 맵에서 기본값을 반환하는 예제
Map<String, String> map = new HashMap<>();
map.put("name", "John");
map.put("age", "30");
String defaultValue = "N/A";
String value = MapUtils.getString(map, "address", defaultValue);
System.out.println(value); // 출력: N/A

// 맵을 특정 값으로 정렬하는 예제
Map<String, Integer> unsortedMap = new HashMap<>();
unsortedMap.put("apple", 3);
unsortedMap.put("banana", 1);
unsortedMap.put("cherry", 2);
Map<String, Integer> sortedMap = MapUtils.sortMap(unsortedMap);
System.out.println(sortedMap); // 출력: {apple=3, banana=1, cherry=2}
```

### 3. 컬렉션 관련 코드

Apache Commons Collections를 사용하여 컬렉션을 다루는 예제입니다.

```java
import org.apache.commons.collections4.CollectionUtils;

// 두 개의 컬렉션에서 교집합을 찾는 예제
List<String> collection1 = Arrays.asList("java", "python", "c++");
List<String> collection2 = Arrays.asList("python", "javascript", "ruby");
Collection<String> intersection = CollectionUtils.intersection(collection1, collection2);
System.out.println(intersection); // 출력: [python]

// 컬렉션에서 조건을 만족하는 요소를 찾는 예제
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
Predicate<Integer> evenPredicate = number -> number % 2 == 0;
Collection<Integer> evenNumbers = CollectionUtils.select(numbers, evenPredicate);
System.out.println(evenNumbers); // 출력: [2, 4]
```

## 결론

Apache Commons Collections은 다양한 자료 구조와 유틸리티 클래스를 제공하여 Java 개발을 더 편리하게 만들어줍니다. 이번 포스트에서는 리스트, 맵, 컬렉션 관련 예제 코드를 살펴보았습니다. 추가적인 자세한 내용은 [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)를 참조하세요.