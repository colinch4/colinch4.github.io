---
layout: post
title: "[Refactoring] 객체 간의 기능 이동"
description: " "
date: 2021-06-09
tags: [Refactoring]
comments: true
share: true
---

객체 간의 기능 이동
-------------------

### 메서드 이동

-	메서드 자신이 속한 클래스보다 다른 클래스의 기능을 더 많이 이용할 땐 그 메서드가 제일 많이 이용하는 클래스 안에서 비슷한 내용의 새 메서드를 작성한다. 기존 메서드는 간단한 대리 메서드로 전환하든지 아예 삭제한다.

### 필드 이동

-	어떤 필드가 자신이 속한 클래스보다 다른 클래스에서 더 많이 사용될 때는 대상 클래스 안에 새필드를 선언하고 그 필드 참조 부분을 전부 새 필드 참조로 수정한다.

### 클래스 추출

-	두 클래스가 처리해야 할 기능이 하나의 클래스에 들어 있을 땐 새 클래스를 만들고 기존 클래스의 관련 필드와 메서드를 새 클래스로 옮긴다.
-	`필드이동`, `메서드 이동`을 사용하여 클래스를 추출한다.

### 클래스 내용 직접 삽입

-	클래스에 기능이 너무 적을 땐 그 클래스의 모든 기능을 다른 클래스로 합쳐 넣고 원래의 클래스는 삭제한다.

### 대리 객체 은폐

-	클라이언트가 객체의 대리 클래스를 호출할 땐 대리 클래스를 감추는 메서드를 서버에 작성한다.

![대리 객체 은폐](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzdklUV3NUa1QwZXc)

### 과잉 중개 메서드 제거

-	클래스에 자잘한 위임이 너무 많을 땐 대리 객체를 클라이언트가 직접 호출하게 한다.

![과잉 중개 메서드 제거](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzaGtjMmhDR1FJUE0)

### 외래 클래스에 메서드 추가

-	사용 중인 서버 클래스에 메서드를 추가해야 하는데 그 클래스를 수정할 수 없을 땐 클라이언트 클래스 안에 서버 클래스의 인스턴스를 첫 번째 인자로 받는 메서드를 작성한다.

**수정 전**

```java
Date newStart = new Date (previousEnd.getYear() , previousEnd.getMonth() , previousEnd.getDate() + 1);

```

**수정 후**

```java
Date newStart = nextDay(previousEnd);

private static Date nextDay(Date arg) {
  return new Date (arg.getYear() ,arg.getMonth() , arg.getDate() + 1);
}
```

### 국소적 상속확장 클래스 사용

-	사용 중인 서버 클래스에 여러 개의 메서드를 추가해야 하는데 클래스를 수정할 수 없을 땐 새 클래스를 작성하고 그 안에 필요한 여러 개의 메서드를 작성한다. 이 상속확장 클래스를 원본 클래스의 하위클래스나 래퍼 클래스(사용자 정의 클래스)로 만든다.
