---
layout: post
title: "[java] 쓰레드 전역 변수(Thread Global Variables)"
description: " "
date: 2023-12-12
tags: [java]
comments: true
share: true
---

쓰레드를 사용하는 프로그램을 작성할 때 전역 변수를 사용하는 경우가 있습니다. 이러한 변수를 **쓰레드 전역 변수** 라고 합니다. 쓰레드 전역 변수를 사용하면 여러 쓰레드에서 변수를 공유할 수 있으므로 편리합니다. 그러나 쓰레드 전역 변수를 올바르게 사용하려면 몇 가지 주의할 점이 있습니다.

## 쓰레드 전역 변수의 문제점

쓰레드 전역 변수를 사용하면 여러 쓰레드에서 변수를 공유할 수 있지만, 이로 인해 동시성 문제가 발생할 수 있습니다. 여러 쓰레드가 동시에 전역 변수를 읽거나 쓰려고 할 때 예기치 않은 결과가 나타날 수 있습니다. 이러한 문제를 방지하기 위해 쓰레드 동기화를 고려해야 합니다.

## 쓰레드 동기화(Thread Synchronization)

쓰레드 동기화는 여러 쓰레드가 공유 자원에 안전하게 접근할 수 있도록 하는 것을 말합니다. Java에서 쓰레드 동기화를 위해 **synchronized** 키워드나 **Lock** 인터페이스를 사용할 수 있습니다. 이를 통해 쓰레드 전역 변수에 안전하게 접근할 수 있게 됩니다.

```java
public class SharedResource {
    private int count;

    public synchronized void increment() {
        count++;
    }
}
```

위의 예시에서는 **synchronized** 키워드를 사용하여 **increment** 메서드를 동기화하고 있습니다.

## 결론

쓰레드 전역 변수는 여러 쓰레드에서 변수를 공유하기 위해 유용하지만, 동시성 문제에 대비하여 적절한 쓰레드 동기화를 고려해야 합니다. 이를 통해 안전하고 효율적으로 쓰레드 전역 변수를 활용할 수 있습니다.

이상으로 *쓰레드 전역 변수* 에 대한 내용을 마치겠습니다.

참고문헌:
- [Java Concurrency in Practice](https://www.amazon.com/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601)