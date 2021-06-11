---
layout: post
title: "[열혈C프로그래밍] chapter 6. printf 함수와 scanf 함수 정리하기"
description: " "
date: 2021-06-11
tags: [열혈C프로그래밍]
comments: true
share: true
---

# chapter 6 
## printf 함수와 scanf 함수 정리하기

6-1 printf 함수
  
  1. 자주 쓰이는 특수문자(\\)

|특수문자 | 의미 |
|--------|------|
| \n     | 개행(new line) |
| \t     | 수평 탭 |
| \'| 작은 따옴표 출력|
|\"| 큰 따옴표 출력|

  2. printf 함수의 서식문자
  %x,%d,%s ... => 이후에 정리

6-2 scanf 함수
```c
scanf("%d , &num);
```
=> scanf는 입력받은 값을 그 변수의 메모리 공간에 저장해야 한다. <br> 
 근데 scanf는 입력해야 할 변수의 주소값을 알아야 메모리 공간에 값을 저장할수 있으므로 <br>
 따라서 &을 사용하여 변수의 주소값을 scanf에게 알려줘야 하는 것이다.<br>

 1. 정수 기반의 입력 형태
   %d	: 10진수의 형태로 데이터를 입력받는다.<br>
   %o : 8진수 양의 정수의 형태로 데이터를 입력받는다.<br>
   %x : 16진수 양의 정수의 형태로 데이터를 입력받는다.<br>
 2. 실수 기반의 입력 형태
   %f  : float 자료형
   %lf : double 자료형
   %Lf : long double 자료형 
