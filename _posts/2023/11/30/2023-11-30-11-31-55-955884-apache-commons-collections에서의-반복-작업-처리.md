---
layout: post
title: "[java] Apache Commons Collections에서의 반복 작업 처리"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 개발자를 위한 유용한 라이브러리입니다. 이 라이브러리를 사용하면 반복 작업을 보다 쉽게 처리할 수 있습니다. 이 글에서는 Apache Commons Collections를 사용하여 반복 작업을 처리하는 방법을 살펴보겠습니다.

## 1. 반복자 (Iterator) 사용하기

Apache Commons Collections는 Iterator 인터페이스의 구현체를 제공합니다. 이를 사용하면 컬렉션의 요소들을 반복적으로 접근할 수 있습니다. 다음은 Iterator를 사용하여 리스트의 요소를 반복적으로 출력하는 예제 코드입니다.

```java
import org.apache.commons.collections4.IteratorUtils;

List<String> list = Arrays.asList("Apple", "Banana", "Orange");
Iterator<String> iterator = list.iterator();

while (iterator.hasNext()) {
    String element = iterator.next();
    System.out.println(element);
}
```

## 2. Predicate 사용하기

Apache Commons Collections는 Predicate 인터페이스의 구현체를 제공하여 조건에 맞는 요소를 필터링할 수 있습니다. 다음은 Predicate를 사용하여 해당하는 요소만 출력하는 예제 코드입니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.PredicateUtils;

List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

CollectionUtils.select(numbers, PredicateUtils.isTruePredicate())
    .forEach(System.out::println);
```

## 3. 변환자 (Transformer) 사용하기

Apache Commons Collections는 Transformer 인터페이스의 구현체를 제공하여 요소들을 변환할 수 있습니다. 다음은 Transformer를 사용하여 리스트의 요소를 변환하는 예제 코드입니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.TransformerUtils;
import org.apache.commons.collections4.iterators.TransformIterator;

List<String> list = Arrays.asList("apple", "banana", "orange");

TransformIterator<String, String> transformIterator = new TransformIterator<>(
    list.iterator(),
    TransformerUtils.stringTransformer(str -> str.toUpperCase())
);

while (transformIterator.hasNext()) {
    String element = transformIterator.next();
    System.out.println(element);
}
```

## 결론

Apache Commons Collections는 자바 개발자들이 반복 작업을 보다 편리하게 처리할 수 있도록 도와주는 유용한 라이브러리입니다. 본 글에서는 Iterator, Predicate, Transformer를 사용한 예제 코드를 살펴보았습니다. 추가적인 정보는 Apache Commons Collections의 공식 문서를 참고하시기 바랍니다.