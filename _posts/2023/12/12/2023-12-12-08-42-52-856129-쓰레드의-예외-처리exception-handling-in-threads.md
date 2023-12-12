---
layout: post
title: "[java] 쓰레드의 예외 처리(Exception Handling in Threads)"
description: " "
date: 2023-12-12
tags: [java]
comments: true
share: true
---

## 개요
Java 애플리케이션에서 멀티쓰레드를 사용할 때, 쓰레드의 예외 처리는 중요한 측면입니다. 쓰레드의 예외 처리는 쓰레드가 실행 중에 발생한 예외를 적절히 처리하여 전체 애플리케이션의 안정성을 유지하는 데에 도움이 됩니다. 쓰레드는 기본적으로 예외를 처리하기 어렵기 때문에 쓰레드 내부의 예외를 적절히 처리하는 방법을 알고 있는 것이 중요합니다.

## Runnable과 Callable 인터페이스
Java에서는 쓰레드를 생성하는 방법으로 Runnable과 Callable 두 가지 인터페이스를 제공합니다. Runnable은 예외를 던지지 않고 void를 반환하는 run() 메서드를 포함하고 있습니다. 따라서 Runnable을 구현한 쓰레드에서 예외를 처리하기 위해서는 **try-catch** 문을 사용하여 예외를 처리해야 합니다. 

```java
public class MyRunnable implements Runnable {
    @Override
    public void run() {
        try {
            // 쓰레드가 실행할 코드
        } catch (Exception e) {
            // 예외 처리
        }
    }
}
```

반면에 Callable은 예외를 던질 수 있는 call() 메서드를 포함하고 있으며 예외를 처리하기 위해 **throws** 절을 이용할 수 있습니다.

```java
public class MyCallable implements Callable<String> {
    @Override
    public String call() throws Exception {
        // 쓰레드가 실행할 코드
    }
}
```

## ExecutorService와 Future
Java에서 작업을 비동기적으로 실행하기 위한 ExecutorService와 Future 인터페이스를 제공합니다. ExecutorService를 사용하면 쓰레드로 실행할 작업을 제출하고 Future 객체를 통해 작업의 결과를 받을 수 있습니다. 쓰레드에서 발생한 예외는 Future 객체의 get() 메서드를 호출할 때 **ExecutionException**으로 감싸져 전달됩니다.

```java
ExecutorService executor = Executors.newFixedThreadPool(1);
Future<String> future = executor.submit(new MyCallable());

try {
    String result = future.get();
    // 결과 사용
} catch (InterruptedException | ExecutionException e) {
    // 예외 처리
}

executor.shutdown();
```

## Uncaught Exception Handler
쓰레드에서 발생한 예외를 처리하기 위해 Uncaught Exception Handler를 등록할 수 있습니다. Uncaught Exception Handler는 쓰레드에서 예외가 발생했을 때 호출되는 인터페이스이며, 이를 이용하여 쓰레드 내부에서 발생한 예외를 처리할 수 있습니다.

```java
Thread.setDefaultUncaughtExceptionHandler(new Thread.UncaughtExceptionHandler() {
    public void uncaughtException(Thread t, Throwable e) {
        // 예외 처리
    }
});
```

## 마무리
쓰레드에서 예외를 처리하는 것은 애플리케이션의 안정성을 높이는 데에 중요한 요소입니다. 이러한 방법들을 활용하여 쓰레드에서 발생한 예외를 적절히 처리하여 안정적인 멀티쓰레드 애플리케이션을 개발할 수 있습니다.

[참고 자료](https://docs.oracle.com/javase/tutorial/essential/concurrency/exceptions.html)