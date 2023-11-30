---
layout: post
title: "[java] Apache Commons Collections와 관련된 메모리 관리 기법"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java의 컬렉션을 확장하고 보완하는 다양한 유틸리티 클래스를 제공하는 라이브러리입니다. 이 라이브러리는 다양한 기능과 편의성을 제공하지만, 잘못 사용하면 메모리 관리에 문제가 발생할 수 있습니다. 이번 글에서는 Apache Commons Collections를 사용할 때 메모리 관리를 위해 고려해야 할 몇 가지 기법을 살펴보겠습니다.

## 1. 객체 참조 해제 (Object reference release)

Apache Commons Collections는 많은 유틸리티 클래스를 제공하여 객체를 추가하거나 제거하는 등의 작업을 간편하게 처리할 수 있게 해줍니다. 그러나 컬렉션에서 제거된 객체가 여전히 메모리에 남아 있는 경우, 이것은 **객체 누수 (object leak)**로 이어질 수 있습니다. 이를 방지하기 위해 사용한 객체는 명시적으로 해제해 주어야 합니다.

```java
List<String> list = new ArrayList<>();
list.add("example");

// 객체를 사용한 후 명시적으로 해제
list.remove(0);
```

## 2. Weak reference 사용하기

Apache Commons Collections는 WeakHashMap과 같은 클래스를 제공하여 **약한 참조 (weak reference)**로 객체를 저장할 수 있도록 해줍니다. 이를 통해 메모리 관리를 더욱 효과적으로 할 수 있습니다. 약한 참조는 해당 객체의 사용 여부에 따라 메모리에서 자동으로 해제됩니다.

```java
Map<String, Object> weakMap = new WeakHashMap<>();

// 약한 참조로 객체 저장
weakMap.put("key", new SomeObject());

// 객체 사용 후 GC가 실행되면 자동으로 메모리에서 해제됨
```

## 3. 큐 사용하기

Apache Commons Collections는 다양한 큐 클래스를 제공하여 메모리 관리를 도와줍니다. 큐를 사용하면 메모리에 일정량의 객체만 유지하고, 일정한 용량을 초과하는 경우 가장 오래된 객체를 자동으로 제거할 수 있습니다.

```java
Queue<String> queue = new CircularFifoQueue<>(10);

// 큐에 객체 추가
queue.add("item1");
queue.add("item2");
queue.add("item3");

// 큐의 용량을 초과하는 경우 가장 오래된 객체 자동 제거
```

## 4. Soft reference 사용하기

Apache Commons Collections는 SoftReferenceMap과 같은 클래스를 제공하여 **강한 참조 (strong reference)**와 달리 **소프트 참조 (soft reference)**로 객체를 저장할 수 있습니다. 소프트 참조는 JVM이 메모리 부족 시 자동으로 해제하는 특성을 가지고 있습니다. 이를 사용하면 메모리 관리를 더욱 효율적으로 수행할 수 있습니다.

```java
Map<String, Object> softMap = new SoftReferenceMap<>();

// 소프트 참조로 객체 저장
softMap.put("key", new SomeObject());

// 메모리 부족 시 JVM이 자동으로 객체 해제
```

## 결론

Apache Commons Collections는 자바 컬렉션을 효율적으로 사용할 수 있도록 많은 유틸리티 클래스를 제공합니다. 그러나 메모리 관리를 제대로 수행하지 않으면 메모리 누수와 같은 문제가 발생할 수 있습니다. 이를 방지하기 위해 객체 참조를 명시적으로 해제하거나, 약한 참조나 소프트 참조를 사용하여 메모리 관리를 수행해야 합니다.

Apache Commons Collections 문서에서는 더 자세한 내용과 예제를 확인할 수 있습니다. ([Apache Commons Collections 문서](https://commons.apache.org/proper/commons-collections/))

참고 문헌:
- [Java Doc: WeakHashMap](https://docs.oracle.com/javase/8/docs/api/java/util/WeakHashMap.html)
- [Java Doc: CircularFifoQueue](https://commons.apache.org/proper/commons-collections/apidocs/org/apache/commons/collections4/queue/CircularFifoQueue.html)
- [Java Doc: SoftReferenceMap](https://commons.apache.org/proper/commons-collections/apidocs/org/apache/commons/collections4/map/SoftReferenceMap.html)