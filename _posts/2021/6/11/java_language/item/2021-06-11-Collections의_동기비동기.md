---
layout: post
title: "[java] Collections의 동기, 비동기"
description: " "
date: 2021-06-11
tags: [java]
comments: true
share: true
---

# Collections의 동기, 비동기

> vector, Hashtable, StringBuffer

⇒ **동기화(synchronized)** 가 되어 있는 클래스들이다. 이들을 사용하면 멀티 스레드 환경에 안전한 특징을 갖고 있다. 하지만 동기화가 필요하지 않는 상황에서 이들을 사용한다면 이들은 여전히 동기화를 수행하므로 **불필요한 성능의 저하(오버헤드)가 있는 상황이 발생**한다. 따라서 이 클래스들을 사용하지 말고, 컬렉션의 메소드를 사용하자.<br> 

- 자바는 동기화된 클래스를 사용하지 않고 동기화되지 않는 객체를 동기화해야 할때 메소드로 **사용자가 동기화를 하도록 선택권을 제공해준다.**

> synchronizedxxx() 메소드

```java
    public class ListExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        Collections.synchronizedList(list);
    }
    }
```

⇒ 동기화되어 있지 않은 list 객체를 Collections의 synchronizedList()를 통해 동기화시켰다.<br>

⇒ 이는 메소드를 통해 객체를 감쌌다고 하여 **Decorator Pattern**이라고 한다. <br>

- 데코레이터 패턴의 특징은 **객체를 동적(dynamic)으로 서브 클래스를 이용해 확장하는 것**이다. 예를 들면, 위의 예제는 list라는 객체를 Collections의 synchronizedList()를 통해 런타임시에 동기화시켰음을 알 수 있다. 또 **객체가 새로 생긴게 아니라 원래의 객체에 적용하였기 때문에** Decorator Pattern이라고 부르는 게 적절하다. (IO 스트림도 Decorator Pattern)

## 결론:

### 1. 동기화가 필요하지 않음에도 불구하고, 동기화를 수행하므로 불필요한 성능의 저하(오버헤드)가 있다.

### 2. 동기화의 정책을 라이브러리가 결정하는 것이 아니라, 사용자가 결정해야 한다.
