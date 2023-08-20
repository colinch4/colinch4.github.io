---
layout: post
title: "[springcore] ApplicationEventPublisher"
description: " "
date: 2021-06-18
tags: [springcore]
comments: true
share: true
---

## ApplicationEventPublisher

- 이벤트 기반 프로그래밍에 필요한 인터페이스 제공
- 옵저버 패턴의 구현체

- Spring 4.3이전
    - ApplicationEvent를 상속 받아 구현했어야 했음
    - MyEvent.java
    ```java
    public class MyEvent extends ApplicationEvent {
        private int data;
        
        public MyEvent(Object source) {
            super(source);
        }

        public MyEvent(Object source, int data) {
            super(source);
            this.data = data;
        }

        public int getData() {
            return data;
        }
    }
    ```
    - DemoAppRunner.java
    ```java
    @Component
    public class DemoAppRunner implements ApplicationRunner {
        @Autowired
        ApplicationEventPublisher eventPublisher;

        public void run(ApplicationArguments args) {
            eventPublisher.publishEvent(this, 100);
        }   
    }
    ```
    - MyEventHandler.java
    ```java
    @Component
    public class MyEventHandler implements ApplicationListener<MyEvent> {

        @Override
        public void onApplicationEvent(MyEvent event) {
            System.out.println("이벤트 받았다, "+event.getData());
        }
    }
    ```
- Spring 4.3이후
    - ApplilcationEvent를 상속받지 않고 POJO형태 가능해짐
    - Listener의 경우에도 ApplicationListener를 상속받지 않고 애노테이션을 메소드에 붙여 바로 처리 가능해짐
    - MyEvent.java
    ```java
    public class MyEvent {
        private Object source;
        private int data;

        public MyEvent(Object source, int data) {
            this.source = source;
            this.data = data;
        }

        public Object getSource() {
            return source;
        }

        public int getData() {
            return data;
        }
    }
    ```
    - MyEventHander.java
    ```java
    @Component
    public class MyEventHandler {

        @EventListener
        public void myEventListener(MyEvent event) {
            System.out.println("이벤트 받았다, "+event.getData());
        }
    }
    ```

- 기본적으로는 synchronized
- 이벤트 리스너들 중 처리 순서를 정하고 싶으면 @Order사용
```java
@EventListener
@Order(Ordered.HIGHEST_PRECEDENCE)
public void myEventListener(MyEvent event) {
    ... 생략
}
```
- 순차처리하지 않고, Async로 병렬수행 하고 싶다면 @Aync사용
    - MyEventHander.java
    ```java
    @EventListener
    @Async
    public void myEventListener(MyEvent event) {
        ... 생략
    }
    ``` 
    - 반드시 main에 @EnableAsync를 선언해놔야 동작함

