---
layout: post
title: "[java] 데몬 스레드(Daemon Thread)와 일반 스레드(Normal Thread)"
description: " "
date: 2023-12-05
tags: [java]
comments: true
share: true
---

## 스레드(Thread)란?
스레드는 프로그램 내에서 실행되는 일련의 코드 블록입니다. 각각의 스레드는 독립적으로 실행되며, 여러 개의 스레드가 동시에 실행될 수 있습니다.

## 일반 스레드(Normal Thread)
일반 스레드는 프로그램의 주 스레드(Main Thread)를 포함하여 프로그래머가 만들고 제어하는 일반적인 스레드입니다. 일반 스레드는 프로그램이 실행 중인 동안에 계속해서 실행되며, 다른 스레드의 작업과 상호작용할 수 있습니다. 일반 스레드는 프로그램이 종료될 때까지 실행되며, 모든 작업이 완료될 때까지 기다릴 수 있습니다.

```java
public class NormalThreadExample {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Normal Thread: " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        thread.start();
    }
}
```

위의 예제는 하나의 일반 스레드를 생성하고 실행하는 예시입니다. 스레드는 1부터 5까지 숫자를 출력하고 1초 동안 대기한 후 다음 숫자를 출력하는 작업을 수행합니다.

## 데몬 스레드(Daemon Thread)
데몬 스레드는 백그라운드에서 실행되는 스레드로, 일반 스레드의 보조 역할을 합니다. 데몬 스레드는 일반 스레드가 종료될 때 함께 종료되며, 주로 프로그램의 각종 보조 작업을 처리하는 데 사용됩니다. 예를 들어, 가비지 컬렉션(Garbage Collection)과 같은 자동화된 작업을 수행하는 스레드는 데몬 스레드로 만들어 사용될 수 있습니다.

```java
public class DaemonThreadExample {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Daemon Thread: " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        // 스레드를 데몬 스레드로 설정
        thread.setDaemon(true);
        thread.start();

        // 메인 스레드 대기
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제는 하나의 데몬 스레드를 생성하고 실행하는 예시입니다. 데몬 스레드는 1부터 5까지 숫자를 출력하는 작업을 수행하며, 메인 스레드는 3초 동안 대기한 후에 프로그램을 종료합니다.

## 결론
데몬 스레드와 일반 스레드는 스레드의 종류에 따라 다르게 동작합니다. 일반 스레드는 프로그램이 실행되는 동안 계속해서 작업을 수행하고, 데몬 스레드는 일반 스레드의 보조로 백그라운드에서 동작합니다. 데몬 스레드는 주로 프로그램의 보조 작업을 처리하는 데 사용되며, 일반 스레드가 종료될 때 함께 종료됩니다.