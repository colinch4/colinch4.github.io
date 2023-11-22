---
layout: post
title: "[Refactoring] 메서드 정리"
description: " "
date: 2021-06-09
tags: [개발]
comments: true
share: true
---

메서드 정리
-----------

### 메서드 추출

-	어떤 코드를 그룹으로 묶어도 되겠다고 판단될 때 그 코드를 빼내어 목적을 잘 나타내는 직관적 이름의 메서드를 만든다.

### 메서드 내용 직접 삽입

-	메서드 기능이 단순할땐 메서드의 기능을 호출하는 메서드에 넣어버리고 그 메서드를 삭제한다.

### 임시변수 내용 직접 삽입 / 임시변수를 메서드 호출로 전환

-	간단한 수식을 대입받는 임시변수로 인해 다른 리팩토링 기법 적용이 힘들 땐 그 임시변수를 참조하는 부분을 전부 수식으로 치환한다.
-	수식의 결과를 저장하는 임시변수가 있을 땐 그 수식을 메서드로 만들고 임시변수를 모두 메서드로 교체한다.
-	메서드 추출시 임시변수로 인해 추출이 힘들고 불필요한 매개변수가 증가할 수 있는데 해당 임시변수를 `임시변수 내용 직접 삽입` 을 사용하여 임시변수를 메소드로 교체하여 리팩토링 기법 적용을 쉽게 할 수 있게할 수 있다.

**수정 전**

```java
  double basePrice = as.getBasePrice();
  return (basePrice > 1000);
```

**수정 후**

```java
  return (as.getBasePrice() > 1000);
```

### 직관적 임시변수 사용

-	사용된 수식이 복잡할 땐 수식의 결과나 수식의 일부분을 용도를 부합하는 직관적 이름의 임시변수에 대입하자.
-	조건문에서 각 조건 절을 가져와서 직관적 이름의 임시변수를 사용해 그 조건의 의미를 설명하려 할 때 주로 사용된다.

**수정 전**

```java
  if(row.getColum(0) == 'A'
    || (row.getColum(0) == 'B'
        && row.getColum(1) == 'Y'
        && row.getColum(2) == 'Y'
        )
    || row.getColum(0) == 'C')
  {        
  }
```

**수정 후**

```java
  boolean isLinkedApplication = row.getColum(0) == 'A'    //연계신청 했다
  boolean isNotLinkedApplication = row.getColum(0) == 'B' //연계신청 안했다
  boolean isSumApplication = row.getColum(0) == 'C'       //합산신청 했다
  boolean isMovingDateProper = row.getColum(1) == 'Y'     //이동일 적정
  boolean isAppropriateDueDate = row.getColum(2) == 'Y'   //신청기한 적절.
  if(isLinkedApplication || (isNotLinkedApplication && isMovingDateProper && isAppropriateDueDate) || isSumApplication) {        
  }
```

### 임시변수 분리

-	루프 변수나 값 누적용 임시변수가 아닌 임시변수에 여러 번 값이 대입될 땐 각 대입마다 다른 임시변수를 사용한다.
-	여러 기능들을 하나의 임시변수에 저장하여 하나의 임시변수를 다양한 용도로 사용하지 말고 각 용도에 맞는 임시변수를 사용하야한다.

### 매개변수로의 값 대입 제거

-	매개변수로 값을 대입하는 코드가 있을 땐 매개변수 대신 임시변수를 사용하게 수정한다.
-	매개변수에 값 할 당시 `값을 통한 전달` 과 `참조를 통한 전달` 혼동하거나 메서드 안의 코드 자체도 혼동된다.

### 메서드를 메서드 객체로 전환

-	지역변수 때문에 메서드 추출을 적용할 수 없는 긴 메서드가 있을 땐 그 메서드 자체를 객체로 전환해서 모든 지역변수를 개체의 필드로 만들자 그런 다음 그 메서드를 개체 안의 여러 메서드로 쪼개면 된다.  

### 알고리즘 전환

-	알고리즘을 더 분명한 것으로 교체해야 할 땐 해당 메서드의 내용을 새 알고리즘으로 바꾸자.
