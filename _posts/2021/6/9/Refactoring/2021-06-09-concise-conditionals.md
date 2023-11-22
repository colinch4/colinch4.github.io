---
layout: post
title: "[Refactoring] 조건문 간결화"
description: " "
date: 2021-06-09
tags: [개발]
comments: true
share: true
---

조건문 간결화
-------------

-	**DevOOOOOOOOP 블로그 참고 :** [좋은 분기문(if) 작성법](http://redutan.github.io/2016/04/01/good-if)

### 조건문 쪼개기

-	복잡한 조건문(if-then-else)이 있을땐 if, then, else 부분을 각각 메서드로 빼낸다.

**수정 전**

```java
if (date.before (SUMMER_START) || date.after(SUMMER_END))
  charge = quantity * winterRate + winterServiceCharge;
else charge = quantity * summerRate;
```

**수정 후**

```java
if (notSummer(date))
  charge = winterCharge(quantity);
else charge = summerCharge (quantity);
```

### 중복 조건식 통합

-	여러 조건 검사식의 결과가 같을 땐 하나의 조건문으로 합친 후 메서드를 빼낸다.

**수정 전**

```java
double disabilityAmount() {
  if (seniority < 2) return 0;
  if (monthsDisabled > 12) return 0;
  if (isPartTime) return 0;
  // 장애인 공제액 산출
}
```

**수정 후**

```java
double disabilityAmount () {
  if (isNotEligableForDisability()) return 0;
  // 장애인 공제액 산출
}
boolean isNotEligibleForDisability () {
  return ((seniority < 2) || (monthsDisabled > 12) || (isPartTime));
}
```

### 조건문의 공통 실행 코드 빼내기

-	조건문의 모든 절에 같은 실행 코드가 있을 땐 같은 부분을 조건문 밖으로 빼낸다.

**수정 전**

```java
if (isSpecialDealO) {
  total = price * 0.95;
  send() ;
} else {
  total = price * 0.98;
  send () ;
}
```

**수정 후**

```java
if (isSpecialDealO)
  total = price * 0.95;  
else
  total = price * 0.98;
send() ;
```

### 제어 플래그 제거

-	논리 연산식의 `제어 플래그 역할을 하는 변수`(논리문을 빠져나오게 하는 제어 플래그 값)가 있을 땐 그 변수를 `break`,`continue`문이나 `return`문으로 바꾼다.

### 여러 겹의 조건문을 감시 절로 전환

-	메서드에 조건문이 있어서 정상적인 실행 경로를 파악하기 힘들 땐 모든 특수한 경우에 감사 절을 사용한다.

**수정 전**

```java
double getPayAmount() {
  double result ;
  if (isDead) result = deadAmount();
  else {
    if (isSeparated) result = separatedAmount();
    else {
      if (isRetired) result = retiredAmount();
      else resul t = normalPayAmount ();
    }
  }
  return result ;
}
```

**수정 후**

```java
double getPayAmount() {
  if (isDead) return deadAmount();
  if (isSeparated) return separatedAmount();
  if (isRetired) return retiredAmount();
  return normalPay Amount();
}
```

### 조건문을 재정의로 전환

-	객체 타입에 따라 다른 기능을 실행하는 조건문이 있을 땐 조건문의 각 절을 하위클래스의 재정의 메서드 안으로 옮기고, 원본 메서드는 abstract 타입으로 수정한다.
-	자세한 내용은 DevOOOOOOOOP 블로그 참고 : [Anti-OOP : if 를 피하고 싶어서](http://redutan.github.io/2016/03/31/anti-oop-if)

### Null 검사를 널 객체에 위임

-	null 값을 검사하는 코드가 계속 나올 땐 null 값을 널 객체로 만든다.

### 어설션 넣기

-	일부 코드가 프로그램의 어떤 상태를 전제할 땐 어설션을 넣어서 그 전제를 확실하게 코드로 작성한다.
