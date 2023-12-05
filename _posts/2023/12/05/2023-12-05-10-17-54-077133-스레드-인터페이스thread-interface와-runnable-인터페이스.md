---
layout: post
title: "[java] 스레드 인터페이스(Thread Interface)와 Runnable 인터페이스"
description: " "
date: 2023-12-05
tags: [java]
comments: true
share: true
---

스레드(Thread)는 프로세스 내에서 실행되는 독립적인 실행 흐름을 말합니다. Java에서는 스레드를 생성하고 제어하기 위해 `Thread` 클래스와 `Runnable` 인터페이스를 제공합니다.

### 스레드 인터페이스(Thread Interface)

`Thread` 클래스는 `Thread` 인터페이스를 구현한 클래스입니다. 이 인터페이스를 구현하는 방법으로 스레드를 만들 수 있습니다. 

```java
public class MyThread extends Thread {
    public void run() {
        // 스레드가 실행될 코드 작성
    }
}
```

위의 코드에서 `run` 메서드는 스레드가 실행될 때 호출되는 메서드입니다. `run` 메서드에 스레드가 실행될 코드를 작성하면 됩니다.

스레드를 사용하기 위해 `MyThread` 클래스를 인스턴스화하고 `start` 메서드를 호출해야 합니다.

```java
MyThread myThread = new MyThread();
myThread.start();
```

### Runnable 인터페이스

`Runnable` 인터페이스는 스레드를 생성하기 위한 대안적인 방법입니다. `Runnable` 인터페이스를 구현한 클래스를 만들어 사용할 수 있습니다.

```java
public class MyRunnable implements Runnable {
    public void run() {
        // 스레드가 실행될 코드 작성
    }
}
```

`run` 메서드는 `Thread` 인터페이스와 마찬가지로 스레드가 실행될 때 호출되는 메서드입니다. `MyRunnable` 클래스를 사용하기 위해 `Thread` 클래스의 생성자에 `MyRunnable` 객체를 전달해야 합니다.

```java
Thread myThread = new Thread(new MyRunnable());
myThread.start();
```

### 선택적인 방법

`Runnable` 인터페이스를 구현하는 것이 `Thread` 클래스를 상속하는 것보다 유연성이 더 있습니다. `Runnable` 인터페이스를 구현하면 다른 클래스를 상속받을 수 있으며, 여러 스레드에서 같은 `Runnable` 객체를 사용할 수 있습니다.

따라서, 스레드를 생성하기 위해 `Thread` 클래스를 상속받을 필요가 없다면 `Runnable` 인터페이스를 구현하는 것이 더 좋은 선택입니다.

### 요약

이 글에서는 Java에서 스레드를 생성하고 제어하기 위해 `Thread` 클래스와 `Runnable` 인터페이스를 사용하는 방법을 알아보았습니다. `Thread` 클래스는 `Thread` 인터페이스를 구현한 클래스로 스레드를 생성할 수 있고, `Runnable` 인터페이스를 구현하는 방법으로도 스레드를 생성할 수 있습니다. `Runnable` 인터페이스를 구현하는 것이 더 유연하고 재사용 가능한 코드를 작성하는 데 도움이 됩니다.

자세한 내용은 [Java Thread Documentation](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html)를 참조하시기 바랍니다.