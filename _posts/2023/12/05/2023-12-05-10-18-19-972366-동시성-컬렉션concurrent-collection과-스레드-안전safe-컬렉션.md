---
layout: post
title: "[java] 동시성 컬렉션(Concurrent Collection)과 스레드 안전(Safe) 컬렉션"
description: " "
date: 2023-12-05
tags: [java]
comments: true
share: true
---

자바에서 동시성 프로그래밍을 할 때, 여러 스레드가 동시에 컬렉션을 수정할 수 있으므로 스레드 안전한 컬렉션을 사용해야 합니다. 동시성 컬렉션은 이러한 스레드 안전성을 제공하는 자료구조입니다. 이번 포스트에서는 동시성 컬렉션과 스레드 안전 컬렉션에 대해 알아보겠습니다.

## 동시성 컬렉션(Concurrent Collection)

자바 5부터 java.util.concurrent 패키지에는 동시성 컬렉션 구현체들이 추가되었습니다. 이러한 동시성 컬렉션은 다중 스레드 환경에서 안전하게 사용할 수 있도록 설계되었습니다.

동시성 컬렉션은 내부적으로 동기화 메커니즘을 사용하여 스레드 간 동기화를 처리합니다. 따라서 여러 스레드가 동시에 컬렉션을 사용하더라도 데이터의 일관성과 안정성을 보장할 수 있습니다.

동시성 컬렉션은 다음과 같은 구현체를 제공합니다:
- `ConcurrentHashMap`: Map 인터페이스를 구현한 동시성 해시 맵
- `ConcurrentSkipListMap`: NavigableMap 인터페이스를 구현한 동시성 스킵 리스트 맵
- `ConcurrentSkipListSet`: NavigableSet 인터페이스를 구현한 동시성 스킵 리스트 셋
- `ConcurrentLinkedQueue`: Queue 인터페이스를 구현한 동시성 연결 리스트 큐
- `ConcurrentLinkedDeque`: Deque 인터페이스를 구현한 동시성 연결 리스트 덱

## 스레드 안전(Safe) 컬렉션

동시성 컬렉션은 여러 스레드 간의 동시 접근을 허용하지만, 모든 컬렉션이 동시성을 위한 동기화를 수행하지는 않습니다. 따라서 스레드 안전성을 위해 동시성 컬렉션을 사용하는 것 외에도 스레드 안전한 컬렉션을 직접 구현할 수도 있습니다.

스레드 안전한 컬렉션은 다음과 같은 방법으로 구현할 수 있습니다:
- `synchronized`: 메소드나 블록에 동기화를 추가하여 여러 스레드 간의 겹침을 막을 수 있습니다. 
- `java.util.concurrent.locks`: Lock 인터페이스를 사용하여 락을 획득하고 해제할 수 있습니다.
- `java.util.concurrent.atomic`: 원자적 연산을 사용하여 원자적 조작을 수행할 수 있습니다.

## 결론

동시성 프로그래밍에서 스레드 간의 안전한 컬렉션 사용은 매우 중요합니다. 동시성 컬렉션은 여러 스레드 간의 동시 접근을 제어하며, 스레드 안전한 컬렉션은 직접 구현하여 스레드간의 겹침을 방지할 수 있습니다.

더 자세한 내용은 다음 자료를 참고하시기 바랍니다:

- [Java Concurrency in Practice by Brian Goetz, et al.](https://www.amazon.com/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601)
- [Java 동시성 프로그래밍 가이드](https://docs.oracle.com/javase/tutorial/essential/concurrency/)