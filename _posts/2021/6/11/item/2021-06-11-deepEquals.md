---
layout: post
title: "[java] deepEquals"
description: " "
date: 2021-06-11
tags: [java]
comments: true
share: true
---


# deepEquals

### 참조 동일성

⇒ 참조 동일성의 경우 Object a와 Object b가 있는 경우 정말 같은 객체인지 주소를 비교하는 경우를 말하며 참조타입에 대해 == 연산으로 비교하는 경우이다.

### 객체 동등성

- 객체 동등성의 경우 객체 간의 논리성 동등성을 따지는 경우이다.
- 객체 동등성은 Object 클래스의 equals 메소드를 이용하여 비교하는데, **이 때 주의해야 할 점은 equals 메소드를 반드시 재정의(Overriding)해야 한다는 점이다.**

이유는 Object 클래스의 Equals 메소드는 ==연산을 이용하기 때문에 이를 그대로 사용하면 객체 동등성이 아닌 참조 동일성을 따지기 때문이다.
(일례로, String 클래스는 equals를 오버라이딩 했기때문에 equals로 문자열 동등 비교가 가능한 것이다.)

> 배열(array)의 equals

- 배열은 참조타입으로서 배열의 equals는 Object 클래스의 equals를 그래도 사용하므로 참조 동일성을 비교한다. 따라서 같은 객체가 아니라면 false를 반환한다.
```java
    public class ArrayExample1 {
    public static void main(String[] args) {
        int[] arr1 = {1,2,3};
        int[] arr2 ={1,2,3};
    
        if (arr1 == arr2){
            System.out.println("same");
        }else{
            System.out.println("diff");
        }
    
        if(arr1.equals(arr2)){
            System.out.println("same");
        }else{
            System.out.println("diff");
        }
    }
    }
    // 실행내용 
    // diff
    // diff
```
> 클래스 Arrays의 equals

- 클래스 Arrays의 equals 메소드는 배열과 배열의 인덱스가 같은 요소(element)끼리 참조 동일성을 비교한다.

      : 아래의 코드는 각 배열의 요소들이 리터럴 상수이기 때문에(리터럴 상수는 똑같은 값이면 객체를 공유한다.) Arrays.equals를 사용하면 참조값이 같으므로 값이 true가 나온다.

 
```java
    public class ArrayExample2 {
    public static void main(String[] args) {
        int[] arr1 = {1,2,3};
        int[] arr2 = {1,2,3};
        
        if(Arrays.equals(arr1,arr2)){
            System.out.println("same");
        }
        else{
            System.out.println("diff");
        }
        
    }
    }
    // 실행내용
    // same
```
> 클래스 Arrays의 deepEquals

- 배열안에 배열이 있는 경우 즉 2차원 배열인 경우에 Arrays의 deepEquals 메소드를 사용하면 2차원 배열의 요소들의 참조 동일성을 비교할 수 있다.
```java
    public class ArrayExample3 {
    public static void main(String[] args) {
        int[][] arr1 ={{1,2},{3,4},{5,6}};
        int[][] arr2 ={{1,2},{3,4},{5,6}};
    
        if(Arrays.equals(arr1,arr2)){
            System.out.println("same");
        }
        else{
            System.out.println("diff");
        }
    
        if(Arrays.deepEquals(arr1,arr2)){
            System.out.println("same");
        }
        else{
            System.out.println("diff");
        }
    }
    }
    //실행내용
    // diff
    // same
```
- Arrays의 equals 메소드의 경우 1차원 배열의 각 요소의 참조 동일성을 비교하기 때문에 요소끼리 참조값이 달라 diff가 출력이 되지만,
- Arrays의 deepEquals 메소드는 2차원 배열의 각 요소의 참조 동일성을 비교하기 때문에 이 경우 각 요소가 리터럴 상수이고 값이 같으므로 same이 출력이 된다.
