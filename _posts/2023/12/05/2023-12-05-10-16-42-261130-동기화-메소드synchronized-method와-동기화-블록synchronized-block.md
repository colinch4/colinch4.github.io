---
layout: post
title: "[java] 동기화 메소드(Synchronized Method)와 동기화 블록(Synchronized Block)"
description: " "
date: 2023-12-05
tags: [java]
comments: true
share: true
---

Java에서 동시에 여러 스레드가 공유하는 자원을 안전하게 처리하기 위해 동기화(synchronization) 기능을 제공합니다. 동기화 메소드와 동기화 블록은 이러한 동기화를 구현하는 방법 중 두 가지입니다.

## 동기화 메소드 (Synchronized Method)
동기화 메소드는 메소드 전체를 임계영역(critical section)으로 지정하여, 한 번에 하나의 스레드만 접근하도록 보장합니다. 다른 스레드가 이 임계영역에 접근하려면 이전 스레드가 메소드를 완료해야 합니다. 

동기화 메소드는 메소드 선언부에 `synchronized` 키워드를 추가하여 구현할 수 있습니다. 아래는 동기화 메소드의 예시 코드입니다.

```java
public synchronized void synchronizedMethod() {
    // Critical section
    // 스레드가 동시에 접근하지 못하도록 보장되는 코드
}
```

## 동기화 블록 (Synchronized Block)
동기화 블록은 메소드 내에서 일부분을 임계영역으로 지정하여, 해당 부분만 한 번에 하나의 스레드만 접근하도록 보장합니다. 동기화 블록은 객체를 기반으로 작동하며, 다른 스레드가 이 임계영역에 접근하려면 이전 스레드가 블록을 완료해야 합니다.

동기화 블록은 `synchronized` 키워드를 사용하여 구현됩니다. 아래는 동기화 블록의 예시 코드입니다.

```java
public void synchronizedBlock() {
    // Non-critical code

    synchronized (this) {
        // Critical section
        // 스레드가 동시에 접근하지 못하도록 보장되는 코드
    }

    // Non-critical code
}
```

## 메소드 동기화와 블록 동기화의 선택
- 동기화 메소드는 간편하게 구현할 수 있지만, 메소드 전체가 임계영역으로 지정되므로 세밀한 제어가 어렵습니다.
- 동기화 블록은 특정 부분만 임계영역으로 지정할 수 있으므로 제어가 더욱 세밀합니다. 하지만 코드 구현이 좀 더 복잡할 수 있습니다.
- 어떤 방법을 선택할지는 상황에 따라 다르며, 잘 판단하여 사용해야 합니다.

## 마무리
Java에서 동기화 메소드와 동기화 블록은 멀티스레드 환경에서 공유 자원을 안전하게 접근하는 방법을 제공합니다. 적절한 동기화 방법을 선택하여 스레드 간의 충돌이나 경쟁 상태를 방지하고 안정적인 프로그램을 구현해야 합니다.

---

**참고 자료:**

- [자바 동기화(Synchronization) 이해하기](https://st-lab.tistory.com/14)
- [Java Concurrency / Multithreading Tutorial](https://www.baeldung.com/java-concurrency-tutorial)