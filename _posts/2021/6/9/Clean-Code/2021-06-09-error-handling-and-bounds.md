---
layout: post
title: "[CleanCode] 오류 처리"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---


오류 처리
---------

### 오류 코드보다 예외를 사용하라

### Try-Catch-Finally 문부터 작성하라

### 미확인 예외를 사용하라

-	확인된 예외가 반드시 필요하지 않다는 사실은 분명해졌다.
-	C#, C++, 파이썬, 루비등은 확인되 예외를 지원하지 않고 안정적인 소프트웨어를 구현하기에 무리가 없다.
-	오류가 치르는 비용에 상응하는 이익을 제공하는지 따져봐야 한다. 일반적인 애플리케이션은 의존성이라는 비용이 이익보다 크다.

### 예외에 의미를 제공하라

-	오류 메시지에 정보를 담아 예외와 함께 던진다.

### 호출자를 고려해 예외 클래스를 정의하라

-	예외 클래스를 사용한다.

### 정상 흐름을 정의하라

### null을 반환하지마라

### null을 전달하지마라

---

경계(외부 API)
--------------

### 외부 코드 사용하기

-	한 예로 java.util.Map이 제공하는 기능성과 유연성은 확실히 유용하지만 그만큼 위험도 크다.
-	Map 사용자라면 누구나 Map 내용을 지울 권한이 있다는 말이다.
-	마음만 먹으면 사용자는 어떤 객체 유형도 추가할 수 있다.
-	Map 인스턴스를 공개 API의 인수로 넘기거나 반환값으로 사용하지 않는다.

### 경계 살피고 익히기

-	간단한 테스트 케이스를 작성해 외부 코드를 익힌다.
-	학습 테스트는 API를 사용하려는 목적에 초점을 맞춘다.

### log4j 익히기

### 학습 테스트는 공짜 이상이다.

-	투자하는 노력보다 얻는 성과가 더 크다. 패키지 새 번전이 나온다면 학습 테스트를 돌려 차이가 있는지 확인한다.

### 아직 존재하지 않는 코드를 사용하기

-	ADAPTER 패턴으로 API 사용을 캡슐화래 API가 바뀔 때 수정할 코드를 한 곳으로 모은다.

### 깨끗한 경계

-	외부 패키지를 호출하는 코드를 가능한 줄여 경계를 관리한다. Map에서 봤듯이, 새로운 클래스로 경계를 감싸거나 아니면 ADAPTER 패턴을 사용해 우리가 원하는 인터페이스를 패키지가 제공하는 인터페이스로 변환한다. 어느 방법이든 코드 가독성이 높아지며, 경계 인터페이스를 사용하는 일관성도 높아지며, 외부 패키지가 변했을 때 변경할 코드도 줄어든다.
