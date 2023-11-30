---
layout: post
title: "[java] Java Apache Commons Collections의 예외 처리 전략"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Java Apache Commons Collections는 많은 유용한 기능을 제공하는 라이브러리입니다. 하지만 때로는 예외 상황에 대한 처리 전략을 고려해야 할 수 있습니다. 

## NullPointerException 처리

Apache Commons Collections의 메서드들은 일반적으로 null 값을 허용하지 않습니다. 그러나 때로는 null 예외를 처리해야 할 때가 있습니다. 

예를 들어, collect 함수를 사용하여 컬렉션에 null 값을 추가하려고 할 때, NullPointerException이 발생할 수 있습니다. 이러한 경우에는 try-catch 블록으로 예외를 처리해야 합니다.

```java
try {
    CollectionUtils.collect(myCollection, null);
} catch (NullPointerException e) {
    // 예외 처리 로직 작성
    e.printStackTrace();
}
```

## UnsupportedOperationException 처리

Apache Commons Collections는 변경 불가능한 컬렉션을 지원하는데, 이러한 컬렉션에 대해 수정 작업을 시도하면 UnsupportedOperationException이 발생할 수 있습니다.

이 경우에는 메서드를 호출하기 전에 해당 컬렉션이 변경 가능한지 확인해야 합니다.

```java
if (CollectionUtils.isModifiable(myCollection)) {
    myCollection.add("element");
} else {
    throw new UnsupportedOperationException("This collection does not support modification");
}
```

## 참고 자료

- [Apache Commons Collections - Exception Handling](https://commons.apache.org/proper/commons-collections/exceptionhandling.html)