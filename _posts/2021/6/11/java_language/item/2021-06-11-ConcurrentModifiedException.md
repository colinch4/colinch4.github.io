---
layout: post
title: "[java] Concurrent Modification Exception"
description: " "
date: 2021-06-11
tags: [java]
comments: true
share: true
---

- 컬렉션을 순회하는 도중에 다른 스레드가 해당 컬렉션을 수정하면 Concurrent Modification Exception이 발생한다.
- for-each문(향상된 for문)를 사용할때 Concurrent Modification Exception이 발생하는데 예외 발생의 이유는 다음 세 가지다.

      1. 파괴적인 필터링(destructive filtering)

      2. 변형(transforming)

      3. 병렬 반복(parallel iteration)

(1)하나의 스레드로 컬렉션에 요소를 계속 추가하고, 또 다른 스레드로 같은 컬렉션을 순회하면 Concurrent Modification Exception이 발생한다. 

```java
    public class ConcurrentModificationExceptionExample1 {
    
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
    
        new Thread(()->{
            for(int i=0; i<10000; i++){
                list.add(i);
    
            }
        }).start();
    
    
        for(Integer i: list){
            System.out.println(i+" ");
        }
    }
    }
```
(2)컬렉션을 순회하는 도중 컬렉션에 요소를 추가하는 경우 Concurrent Modification Exception이 발생한다.

```java
    public class ConcurrentModificationExceptionExample2 {
    
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Kim");
        list.add("Ham");
        list.add("Lim");
    
        for(String str: list){
            if(str.equals("Ham")){
                list.add("Kang");
            }
        }
    }
    }
```
(3)만약 리스트를 순회하는 도중에 리스트에 요소를 추가하고 싶다면 새로운 리스트를 사용한다. 
```java
    import java.util.ArrayList;
    import java.util.List;
    
    public class ConcurrentModificationExceptionExample1 {
    
    public static void main(String[] args) {
        List<String> newList = new ArrayList<>();
        List<String> list = new ArrayList<>();
        list.add("Kim");
        list.add("Ham");
        list.add("Lim");
    
    
        System.out.println("순회하는 중");
        System.out.println("===========================");
        for(String str: list){
            if(str.equals("Ham"))
                newList.add("Kang");
        }
        list.addAll(newList);
    
        System.out.println("===========================");
    
        System.out.println("after:");
        for(String str: list)
            System.out.print(str+" ");
        System.out.println();
    }
    }
    /* 실행내용
    순회하는 중
    ===========================
    ===========================
    after:
    Kim Ham Lim Kang 
    */

```
⇒ 참고로 for-each 문은 컬랙션과 배열은 물론 **Iterable 인터페이스를 구현한 객체라면 무엇이든 순회할 수 있다.**
