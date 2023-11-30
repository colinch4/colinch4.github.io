---
layout: post
title: "[java] Java에서의 Apache Commons Collections 활용 사례"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Java에서는 Apache Commons Collections 라이브러리를 사용하여 다양한 컬렉션 기능을 쉽게 구현할 수 있습니다. 이번 글에서는 Apache Commons Collections 라이브러리의 몇 가지 유용한 기능과 활용 사례에 대해 알아보겠습니다.

## 1. 단일 값 반환하기

Apache Commons Collections 라이브러리에서는 CollectionUtils 클래스의 `get` 메서드를 사용하여 컬렉션에서 단일 값을 반환할 수 있습니다. 예를 들어, 다음과 같은 리스트가 있다고 가정해봅시다.

```java
List<String> names = Arrays.asList("John", "Jane", "Alice", "Bob");
```

이 리스트에서 첫 번째 요소를 가져오기 위해 다음과 같이 코드를 작성할 수 있습니다.

```java
String firstElement = CollectionUtils.get(names, 0);
System.out.println(firstElement); // 출력: "John"
```

## 2. 컬렉션 정렬하기

Apache Commons Collections 라이브러리에서는 CollectionUtils 클래스의 `sort` 메서드를 사용하여 컬렉션을 간편하게 정렬할 수 있습니다. 예를 들어, 다음과 같은 리스트가 있다고 가정해봅시다.

```java
List<Integer> numbers = Arrays.asList(5, 2, 8, 3);
```

이 리스트를 오름차순으로 정렬하기 위해 다음과 같은 코드를 작성할 수 있습니다.

```java
CollectionUtils.sort(numbers);
System.out.println(numbers); // 출력: [2, 3, 5, 8]
```

## 3. 컬렉션 필터링하기

Apache Commons Collections 라이브러리에서는 CollectionUtils 클래스의 `filter` 메서드를 사용하여 컬렉션을 필터링할 수 있습니다. 예를 들어, 다음과 같은 리스트가 있다고 가정해봅시다.

```java
List<Integer> numbers = Arrays.asList(5, 2, 8, 3);
```

이 리스트에서 짝수만 필터링하여 새로운 리스트를 생성하기 위해 다음과 같은 코드를 작성할 수 있습니다.

```java
Predicate<Integer> evenPredicate = new Predicate<Integer>() {
    public boolean evaluate(Integer number) {
        return number % 2 == 0;
    }
};

List<Integer> evenNumbers = (List<Integer>) CollectionUtils.filter(numbers, evenPredicate);
System.out.println(evenNumbers); // 출력: [2, 8]
```

위의 코드에서는 짝수를 판별하는 Predicate를 정의하여 `filter` 메서드에 전달하였습니다.

## 결론

이번 글에서는 Java에서 Apache Commons Collections 라이브러리를 활용한 몇 가지 기능과 활용 사례를 알아보았습니다. Apache Commons Collections 라이브러리는 다양한 컬렉션 기능을 제공하여 Java 개발의 생산성을 향상시킬 수 있습니다.

더 많은 기능과 사용법에 대해서는 [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)를 참고하시기 바랍니다.

**참고 자료**
- Apache Commons Collections 공식 문서: https://commons.apache.org/proper/commons-collections/