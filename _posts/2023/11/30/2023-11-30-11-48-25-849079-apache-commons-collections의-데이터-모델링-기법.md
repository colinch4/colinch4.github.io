---
layout: post
title: "[java] Apache Commons Collections의 데이터 모델링 기법"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 개발자들이 자주 사용하는 유용한 라이브러리입니다. 이 라이브러리는 데이터 모델링을 위한 다양한 기능을 제공하여 개발자들이 코드를 더 효율적으로 작성할 수 있게 도와줍니다. 이번 글에서는 Apache Commons Collections의 주요 데이터 모델링 기법 몇 가지를 살펴보겠습니다.

## 1. 컬렉션 변환 (Collection Transformation)

Apache Commons Collections는 여러 가지 컬렉션 타입 사이의 변환을 간편하게 해주는 기능을 제공합니다. 예를 들어, List를 Set으로 변환하거나 Set을 Map으로 변환하는 등의 작업을 손쉽게 할 수 있습니다.

```java
List<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
list.add("Orange");

Set<String> set = CollectionUtils.collect(list, TransformerUtils.invokerTransformer("toString"));
Map<String, String> map = CollectionUtils.collect(set, TransformerUtils.invokerTransformer("toString"), TransformerUtils.invokerTransformer("toString"));
```

위의 예제에서는 `CollectionUtils.collect()` 메소드를 사용하여 List를 Set으로 변환하고, 그 다음에 다시 Set을 Map으로 변환하고 있습니다. 변환을 위해 `TransformerUtils.invokerTransformer()` 메소드를 사용하며, 이 메소드는 객체의 특정 메소드를 호출하여 결과를 반환해줍니다.

## 2. Predicate와 Filter

Apache Commons Collections는 Predicate와 Filter라는 인터페이스를 제공하여 컬렉션의 요소를 조건에 맞게 필터링할 수 있습니다. Predicate는 주어진 조건에 해당하는 요소를 찾아주는 역할을 하며, Filter는 컬렉션에서 조건에 맞지 않는 요소를 제거해주는 역할을 합니다. 이를 통해 개발자들은 불필요한 반복문을 사용하지 않고도 컬렉션의 요소를 필터링할 수 있습니다.

```java
List<Integer> numbers = new ArrayList<>();
numbers.add(1);
numbers.add(2);
numbers.add(3);
numbers.add(4);
numbers.add(5);

Collection<Integer> filteredNumbers = CollectionUtils.select(numbers, new Predicate() {
    @Override
    public boolean evaluate(Object object) {
        Integer number = (Integer) object;
        return number % 2 == 0;
    }
});

CollectionUtils.filter(numbers, PredicateUtils.notPredicate(new Predicate() {
    @Override
    public boolean evaluate(Object object) {
        Integer number = (Integer) object;
        return number % 2 == 0;
    }
}));
```

위의 예제에서는 `CollectionUtils.select()` 메소드를 사용하여 짝수인 숫자만 필터링한 결과를 가져오고 있습니다. 또한, `CollectionUtils.filter()` 메소드를 사용하여 홀수인 숫자만 남기고 나머지 요소를 제거하고 있습니다. Predicate는 다양한 조건을 필터링하는데 사용할 수 있으며, 개발자는 이를 활용하여 다양한 데이터 모델링 작업을 수행할 수 있습니다.

## 3. 변환기 (Transformer)

Apache Commons Collections는 데이터 변환 작업을 지원하는 Transformer라는 인터페이스를 제공합니다. Transformer는 입력값을 받아서 원하는 형태로 변환해주는 역할을 합니다. 다양한 Transformer 구현체를 제공하므로, 개발자는 이를 활용하여 데이터의 변환 작업을 쉽게 수행할 수 있습니다.

```java
List<String> words = new ArrayList<>();
words.add("Hello");
words.add("World");

Transformer<String, Integer> lengthTransformer = new Transformer<String, Integer>() {
    @Override
    public Integer transform(String input) {
        return input.length();
    }
};

Collection<Integer> lengths = CollectionUtils.collect(words, lengthTransformer);
```

위의 예제에서는 입력값인 문자열의 길이를 반환하는 `lengthTransformer`를 생성하여 `CollectionUtils.collect()` 메소드를 사용하여 변환 작업을 수행하고 있습니다. 이를 통해 원하는 형태로 데이터를 변환할 수 있습니다.

## 결론

Apache Commons Collections를 활용하면 데이터 모델링 작업을 더 효율적으로 수행할 수 있습니다. 컬렉션 변환, Predicate와 Filter, 그리고 변환기를 사용하여 코드의 가독성을 높이고, 재사용성을 높일 수 있습니다. Apache Commons Collections 문서를 참조하여 더 다양한 기능을 알아보시기 바랍니다.

참조: [Apache Commons Collections](https://commons.apache.org/proper/commons-collections/)