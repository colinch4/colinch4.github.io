---
layout: post
title: "[Refactoring] 복합 리팩토링"
description: " "
date: 2021-06-09
tags: [Refactoring]
comments: true
share: true
---

복합 리팩토링
-------------

### 상속 구조 정리

-	하나의 상속 계층이 두 작업을 동시에 수행할 땐 상속 계층을 하나 더 만들어서 위임을 통해 다른 계층을 호출한다.

![상속 구조 정리](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzQV80ZzhkbHNhenM)

### 절차 코드를 객체로 전환

-	코드가 절차식으로 작성되어 있을 땐 데이터 레코드를 객체로 바꾸고, 기능을 쪼개서 각각의 객체로 옮긴다.

### 도메인 로직을 표현과 분리

-	도메인 로직이 들어 있는 GUI 클래스가 있을 땐 도메인 로직을 별도의 도메인 클래스로 떼어낸다.
-	MVC 패턴과 같인 표현과 분리.

### 계층구조 추출

-	한 클래스에 기능이 너무 많고 일부분에라도 조건문이 많을 땐 각 조건에 해당하는 하위클래스를 작성해서 계층구조를 만든다.

![계층구조 추출](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzRVZpN1MyUEFPS1U)
