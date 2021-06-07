---
layout: post
title: "[java] Iterator and For loop"
description: " "
date: 2021-06-07
tags: [java]
comments: true
share: true
---

# 📀 Iterator and For loop

> 자바 프로그래밍에서 반복문을 나타내는 두 가지!

<br >

### 1. Foor Loop 반복문

> - 조건문이 true인 경우, 주어진 횟수만큼 실행문 반복

<br>

#### - 기본 사용법

> - 변수와 증감식을 사용하여 설정한 반복 횟수이 되면 반복문을 빠져나감

```java
    for(int i = 0; i<반복 횟수; i++){
        반복 할 내용
    }
```

#### - Enhanced for loop 사용법 : 변수, 증감식 (X)

> - 배열이나 컬렉션을 더 쉽게 처리할 수 있도록함
> - 배열 및 컬렉션 내의 항목 개수만큼 반복하고 for문을 빠져나감

```java
    for(타입변수 : 배열){
        반복 할 내용
    }
```

<br>

예시

```java
//기본 반복문
// 100까지 합 구하기

int sum = 0;
for(int i =0; i =< 100; i++){
    sum++
}

//향상된 반복문
// 배열 내의 scores 합 구하기

int [] scores = {90, 71, 84, 93, 87}
int sum = 0;
for(int score : scores){
    sum+= score
}
```

<br>

### 2.Iterator 이터레이터

> - ArrayList나 HashSet같은 컬렉션 내에 반복문을 쓸 수 있는 객체
> - itertating은 looping이라는 뜻을 갖고 있음
> - java.util를 import해서 사용

<br>

#### - 사용법

```java
    Iterator<객체 타입> iteratorName = ArrayListName.iterator()
```

<br>

#### - 매소드 : 반복문 내의 요소를 받아오는 형태에 따라 달라짐

| hasNext()                | next()                             | remove()            |
| ------------------------ | ---------------------------------- | ------------------- |
| 다음 요소 존재: **true** | 다음 요소 존재 : **다음요소 반환** | 현재 위치 요소 삭제 |

<br >

[예시 출처 : w3schools ](https://www.w3schools.com/java/java_iterator.asp)

```java
// ArrayList 와 Iterator class import 해오기
import java.util.ArrayList;
import java.util.Iterator;

public class MyClass {
  public static void main(String[] args) {

    // ArrayList collection 생성
    ArrayList<String> cars = new ArrayList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");

    // ArrayList ==> iterator로 만들기
    Iterator<String> it = cars.iterator();

    // it.next() => it내의 다음 요소가 있는 동안 반복한다는 뜻.
    // it내의 모든 값들을 반환하게 됨
    System.out.println(it.next());
  }
}
```
