---
layout: post
title: "[java] 타입 인수 추론(Type Argument Inference)과 와일드카드 캡처(Wildcard Capture)"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

자바에서는 제네릭 메서드나 제네릭 클래스를 사용할 때, **타입 인수 추론**이라는 개념을 이용해 코드를 보다 간결하게 작성할 수 있습니다. 타입 인수 추론이란, 제네릭 메서드를 호출할 때 타입 인수를 명시하지 않아도 컴파일러가 이를 추론하여 타입 안전성을 유지하는 것입니다.

예를 들어, 아래와 같은 제네릭 메서드가 있다고 가정해봅시다.

```java
public <T> T getFirstElement(List<T> list) {
    if (list.isEmpty()) {
        throw new IllegalArgumentException("리스트가 비어있습니다.");
    }
    return list.get(0);
}
```

이때, 다음과 같이 메서드를 호출할 수 있습니다.

```java
List<String> stringList = Arrays.asList("Java", "Kotlin", "Scala");
String firstElement = getFirstElement(stringList); // 타입 인수를 명시하지 않아도 컴파일러가 추론하여 String 형으로 변환
```

이처럼, 타입 인수 추론은 제네릭 메서드나 제네릭 클래스를 사용할 때 번거로운 타입 인수 명시를 줄여주고, 코드의 가독성을 높여주는 장점이 있습니다.

# 와일드카드 캡처(Wildcard Capture)

와일드카드는 **제한된 제네릭 타입**을 나타내며, **와일드카드 캡처**는 **메서드 호출 결과로부터 발생하는 임시적 와일드카드 타입**의 캡처를 의미합니다.

예를 들어, 다음과 같이 와일드카드를 사용한 메서드가 있다고 가정해봅시다.

```java
public void processElements(List<? extends Number> elements) {
    // 메서드 내용
}
```

이때, 다음과 같이 메서드를 호출하면, 와일드카드 캡처가 발생합니다.

```java
List<Integer> intList = Arrays.asList(1, 2, 3, 4, 5);
processElements(intList); // 와일드카드 캡처 발생
```

와일드카드 캡처는 메서드 호출로부터 발생하는 임시적인 와일드카드 타입을 캡처하며, 이를 통해 제네릭 타입을 유지하면서 유연한 타입 처리가 가능합니다.

위와 같이 타입 인수 추론과 와일드카드 캡처는 자바의 제네릭 타입 시스템을 보다 효과적으로 활용할 수 있게 해줍니다.

## 참고 자료
- [Oracle Java Documentation on Generic Methods](https://docs.oracle.com/javase/tutorial/extra/generics/methods.html)
- [Wildcard Capture in Java Generics](https://www.baeldung.com/java-generic-wildcards-capture)