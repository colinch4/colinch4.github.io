---
layout: post
title: "[이것이자바다] chapter 15. 컬렉션 - LIFO 와 FIFO 컬렉션"
description: " "
date: 2021-06-11
tags: [이것이자바다]
comments: true
share: true
---

## chapter15
## LIFO 와 FIFO 컬렉션

* 후입선출(LIFO: Last In First Out)은 나중에 넣은 객체가 먼저 빠져나가는 자료구조를 말한다.

* 선입선출(FIFO: First In First Out)은 먼저 넣은 객체가 먼저 빠져나가는 자료구조를 말한다. 

=> 컬렉션 프레임워크에는 LIFO 자료구조를 제공하는 **스택(Stack) 클래스**와 FIFO 자료구조를 제공하는 **큐(Queue) 인터페이스**를 제공하고 있다.<br> 
=> 스택(Stack)을 응용한 대표적인 예가 **JVM 스택 메모리**이다. **스택 메모리**에 저장된 변수는 **나중에 저장된 것부터 제거**된다. <br>
=> 큐(Queue)을 응용한 대표적인 예가 **스레드풀(ExecutorService)의 작업 큐**이다. 작업 큐는 먼저 들어온 작업부터 처리한다.<br> 

> Stack

* Stack은 LIFO이다. 

| 리턴 타입 | 메소드         | 설명                                        |
|-----------|----------------|---------------------------------------------|
| E   | push(E item) | 주어진 객체를 스택에 넣는다  | 
| E   | peek()  | 스택의 맨 위 객체를 가져온다. 객체를 스택에서 제거하지 않는다.|
| E   | pop()  | 스택의 맨 위 객체를 가져온다. 객체를 스택에서 제거한다.(LIFO) | 

```java
Stack<E> stack = new Stack<E>();
```

=> Stack에서 동전을 빼면 마지막에 넣은 동전이 먼저 나온다.<br>
=> 즉, LIFO(Last In First Out)으로 출력된다. <br>
```java
public class StackExample {

    public static void main(String[] args) {
        Stack<Coin> coinStack = new Stack<>();

        coinStack.push(new Coin(100));
        coinStack.push(new Coin(50));
        coinStack.push(new Coin(500));
        coinStack.push(new Coin(10));

        while(!coinStack.isEmpty()){
            Coin coin = coinStack.pop();
            System.out.println("꺼내온 동전 : " + coin.getValue() +"원");
            //LIFO로 출력된다. 
        }
    }
}

```

> Queue

* Queue 인터페이스는 FIFO 이다.  

| 리턴 타입 | 메소드      |  설명                                       |
|-----------|-------------|---------------------------------------------|
| boolean   | offer(E e)  | 주어진 객체를 넣는다.  |
| E | peek() | 객체 하나를 가져온다. 객체를 큐에서 제거하지 않는다. |
| E | poll() | 객체 하나를 가져온다. 객체를 큐에서 제거한다.(FIFO) | 

=> Queue 인터페이스를 구현한 대표적인 클래스는 **LinkedList**이다. LinkedList는 List 인터페이스를 구현했기 때문에 List 컬렉션이기도 하다. 다음 코드는 LinkedList 객체를 Queue 인터페이스 타입으로 변환한 것이다. 

Queue\<Message> messageQueue = new LinkedList<>();

```java
 import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
        Queue<Message> messageQueue =  new LinkedList<>();

        messageQueue.offer(new Message("sendMail", "홍길동"));
        messageQueue.offer(new Message("sendSMS", "신용권"));
        messageQueue.offer(new Message("sendKakaotalk", "홍두깨"));

        while(!messageQueue.isEmpty()){
            //FIFO로 전달됨을 알 수 있다.
            Message message = messageQueue.poll();
            switch (message.getCommand()){
                case "sendMail":
                    System.out.println(message.getTo() +"님에게 메일을 보냅니다.");
                    break;
                case "sendSMS":
                    System.out.println(message.getTo() +"님에게 SMS을 보냅니다.");
                    break;
                case "sendKakaotalk":
                    System.out.println(message.getTo() +"님에게 카카오톡을 보냅니다.");
                    break;
            }
        }
    }
}

```

## 동기화된 컬렉션

=> 컬렉션 프레임워크의 대부분의 클래스들은 싱글 스레드 환경에서 사용할 수 있도롞 설계되었기 때문에, 따라서 여러 스레드가 동시에 컬렉션에 접근한다면 의도하지 않게 요소가 변경될 수 있는 **불안전한 상태**가 된다.<br>
=> Vector와 Hashtable은 동기화된(Synchronized) 메소드로 구성되어 있기 때문에 멀티 스레드 환경에서 안전하게 요소를 처리할 수 있지만, **ArrayList와 HashSet,HashMap은 동기화된 메소드로 구성되어 있지 않아 멀티 스레드 환경에서 안전하지 않다.**<br>
=> 따라서 ArrayList, HashSet, HashMap 을 멀티 스레드 환경에서 사용할 경우 안전하게 사용하기 위해 컬렉션 프레임워크는 **비동기화된 메소드를 동기화된 메소드로 래핑하는 Collections의 synchronizedXXX() 메소드를 제공하고 있다. 매개값으로 비동기화된 컬렉션을 대입하면 동기화된 컬렉션을 리턴한다.**<br>

| 리턴 타입 | 메소드(매개 변수)                  | 설명                                         |
|-----------|------------------------------------|----------------------------------------------|
| List\<T>   | synchronizedList(List\<T> list)    | List를 동기화된 List로 리턴 |
| Map\<K,V>  | synchronizedMap(Map\<K,V> map)   | Map을 동기화된 Map으로 리턴 |
| Set\<T> | synchronizedSet(Set\<T> set)  | Set을 동기화된 Map으로 리턴 |

ArrayList<br>
```java
List<T> list = Collections.synchronizedList(new ArrayList<T>());
```
=> Collections의 synchronizedList()로 ArrayList가 동기화되었다.<br> 

HashSet<br>
```java
Set<E> set = Collections.synchronizedSet(new HashSet<T>());
```
=> Collections의 synchronizedSet()로 HashSet이 동기화되었다.<br>

HashMap<br>
```java
Map<String,Integer> map = Collections.synchronizedMap(new HashMap<>());
```
=> Collections의 synchronizedMap()로 HashMap이 동기화되었다.<br>


## 병렬처리를 위한 컬렉션 

=> 동기화(Synchronized)된 컬렉션은 멀티 스레드 환경에서 안전할지는 몰라도, 성능이 나쁘다. 왜냐하면 한 스레드가 컬렉션을 처리하면 컬렉션이 **전체잠금**이 되어 다른 스레드들은 접근할 수 없어 처리 속도가 느려지기 때문이다. 따라서 멀티 스레드의 장점은 병렬적으로 처리하는 것인데 동기화 때문에 멀티스레드가 병렬적으로 처리할 수 없다. <br> 
=> 이를 해결하기 위해 자바는 멀티 스레드가 컬렉션의 요소를 병렬적으로 처리할 수 있도록 특별한 컬렉션을 제공하고 있다. **java.util.concurrent 패키지의 ConcurrentHashMap과 ConcurrentLinkedQueue**이다. ConcurrentHashMap은 Map 구현 클래스이고, ConcurrentLinkedQueue는 Queue 구현 클래스이다. <br>

* ConcurrentHashMap을 사용하면 **스레드가 안전하면서도 멀티 스레드가 요소를 병렬적으로 처리할 수 있다.** 이것이 가능한 이유는 ConcurrentHashMap은 **부분(Segment)잠금**을 사용하기 때문이다. 
* 컬렉션에 10개의 요소가 저장되어 있을 경우, 1개를 처리할 동안 전체 10개의 요소를 다른 스레드가 처리하지 못하도록 하는 것이 **전체 잠금**이라면, **처리하는 요소가 포함된 부분만 잠금하고 나머지 부분은 다른 스레드가 변경할 수 있도록 하는 것이 부분 잠금**이다. 따라서 ConcurrentHashMap을 사용하면 안전하면서도 병렬적으로 처리할 수 있어 빠르다. 


ConcurrentHashMap 객체를 생성하는 코드<br>
```java
Map<K,V> map = new ConcurrentHashMap<K,V>();
```

* ConcurrentLinkedQueue는 락-프리(lock-free) 알고리즘을 구현한 컬렉션이다. **락-프리 알고리즘은 여러 개의 스레드가 동시에 접근할 경우, 잠금을 사용하지 않고도 최소한 하나의 스레드가 안전하게 요소를 저장하거나 얻도록 해준다.**
=> 락-프리 알고리즘을 구체적으로 몰라 지금은 아리까리한데 일단은 넘어가자. <br>

ConcurrentLinkedQueue 객체를 생성하는 코드 <br>
```java
Queue<E> queue = new ConcurrentLinkedQueue<E>();
```


