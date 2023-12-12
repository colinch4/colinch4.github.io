---
layout: post
title: "[java] 쓰레드 간의 통신(Communication between Threads)"
description: " "
date: 2023-12-12
tags: [java]
comments: true
share: true
---

쓰레드 간의 효율적인 통신은 멀티쓰레드 프로그래밍에서 매우 중요한 측면입니다. 서로 다른 쓰레드들 사이에 정보를 전송하고 동기화하는 것은 복잡할 수 있지만, 올바른 방법으로 이루어진다면 안정적인 프로그램 동작을 보장할 수 있습니다.

## **1. 공유 자원 활용**

여러 쓰레드가 특정 자원에 접근하는 경우, 해당 자원을 올바르게 동기화하지 않으면 예기치 않은 상황이 발생할 수 있습니다. 이를 방지하기 위해 공유 자원에 접근하는 부분은 **동기화** 해야 합니다. Java에서는 `synchronized` 키워드를 사용하여 메소드나 블록을 동기화할 수 있습니다.

```java
public class SharedResource {
    private int sharedData;

    public synchronized void setSharedData(int data) {
        this.sharedData = data;
    }

    public synchronized int getSharedData() {
        return sharedData;
    }
}
```

## **2. wait(), notify(), notifyAll() 메소드**

Java에서는 `wait()`, `notify()`, `notifyAll()` 메소드를 사용하여 쓰레드 간의 효율적인 통신을 할 수 있습니다. `wait()` 메소드는 쓰레드가 특정 조건을 만족할 때까지 대기하도록 만들고, `notify()` 메소드는 대기 중인 하나의 쓰레드를 깨웁니다. `notifyAll()` 메소드는 모든 대기 중인 쓰레드를 깨웁니다.

```java
public class SharedResource {
    private boolean isDataAvailable = false;

    public synchronized void produceData() {
        while (isDataAvailable) {
            try {
                wait();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        // 생산 작업 수행
        isDataAvailable = true;
        notify();
    }

    public synchronized void consumeData() {
        while (!isDataAvailable) {
            try {
                wait();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        // 소비 작업 수행
        isDataAvailable = false;
        notify();
    }
}
```

위의 예시는 생산자-소비자 문제를 해결하기 위해 `wait()`와 `notify()` 메소드를 활용한 것입니다. 

## **3. BlockingQueue 활용**

`java.util.concurrent` 패키지에 있는 `BlockingQueue`를 사용하면 쓰레드 간의 안전한 데이터 교환을 간단히 구현할 수 있습니다.

```java
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class SharedResource {
    private BlockingQueue<Integer> queue = new LinkedBlockingQueue<>();

    public void produceData(int data) {
        try {
            queue.put(data);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    public int consumeData() {
        try {
            return queue.take();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return -1;
        }
    }
}
```

`BlockingQueue`를 이용하면 쓰레드 간의 안전한 데이터 교환을 위해 별도의 동기화 작업이 필요하지 않습니다.

쓰레드 간의 효율적인 통신은 멀티쓰레드 환경에서 프로그램의 안정성과 성능에 영향을 미치므로, 적절한 방법으로 이를 구현하고 활용하는 것이 매우 중요합니다.

## **4. 참고 자료**

- [Java Documentation on synchronized methods](https://docs.oracle.com/javase/tutorial/essential/concurrency/syncmeth.html)
- [Java Documentation on wait(), notify(), and notifyAll()](https://docs.oracle.com/javase/tutorial/essential/concurrency/guardmeth.html)
- [Java Documentation on BlockingQueue](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/BlockingQueue.html)