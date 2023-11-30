---
layout: post
title: "[java] Apache Commons Collections의 데이터 조작 기능"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 개발자들이 자주 사용하는 유용한 라이브러리입니다. 이 라이브러리에는 다양한 데이터 조작 기능이 제공되어, 개발자들이 데이터 컬렉션을 손쉽게 다룰 수 있도록 도와줍니다. 이번 블로그 포스트에서는 Apache Commons Collections의 유용한 데이터 조작 기능에 대해 알아보겠습니다.

## 컬렉션 변환 함수

Apache Commons Collections는 `Transformer` 인터페이스를 사용하여 컬렉션의 요소를 변환하는 기능을 제공합니다. 예를 들어, 문자열로 이루어진 리스트가 있을 때 이를 정수로 변환하고 싶다면 `Transformer` 인터페이스를 구현한 클래스를 사용하여 변환 함수를 정의할 수 있습니다.

```java
import org.apache.commons.collections4.Transformer;
import org.apache.commons.collections4.CollectionUtils;

public class StringToIntTransformer implements Transformer<String, Integer> {
    public Integer transform(String input) {
        return Integer.parseInt(input);
    }
}

...

List<String> strings = Arrays.asList("1", "2", "3");
List<Integer> integers = CollectionUtils.collect(strings, new StringToIntTransformer());
```

위의 예제 코드에서는 `StringToIntTransformer` 클래스를 구현하여 `Transformer` 인터페이스의 `transform` 메서드를 오버라이드합니다. `CollectionUtils.collect` 메서드를 사용하여 `strings` 리스트의 모든 요소를 `StringToIntTransformer`를 이용해 정수로 변환한 후 `integers` 리스트에 저장합니다.

## 컬렉션 필터링 함수

Apache Commons Collections는 `Predicate` 인터페이스를 사용하여 컬렉션의 요소를 필터링하는 기능을 제공합니다. 예를 들어, 숫자로 이루어진 리스트가 있을 때 양수인 숫자만 필터링하고 싶다면 `Predicate` 인터페이스를 구현한 클래스를 사용하여 필터링 함수를 정의할 수 있습니다.

```java
import org.apache.commons.collections4.Predicate;
import org.apache.commons.collections4.CollectionUtils;

public class PositiveNumberPredicate implements Predicate<Integer> {
    public boolean evaluate(Integer number) {
        return number > 0;
    }
}

...

List<Integer> numbers = Arrays.asList(-1, 0, 1, 2, 3);
Collection<Integer> positiveNumbers = CollectionUtils.select(numbers, new PositiveNumberPredicate());
```

위의 예제 코드에서는 `PositiveNumberPredicate` 클래스를 구현하여 `Predicate` 인터페이스의 `evaluate` 메서드를 오버라이드합니다. `CollectionUtils.select` 메서드를 사용하여 `numbers` 리스트에서 양수인 숫자만 필터링한 후 `positiveNumbers` 컬렉션에 저장합니다.

## 참고 자료

- Apache Commons Collections 공식 홈페이지: [https://commons.apache.org/proper/commons-collections/](https://commons.apache.org/proper/commons-collections/)