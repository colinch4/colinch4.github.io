---
layout: post
title: "[Refactoring] Refactoring"
description: " "
date: 2021-06-09
tags: [Refactoring]
comments: true
share: true
---

![Refactoring-book](http://silverbullet.kr/wp-content/uploads/2017/03/21322571.jpg)

목차
----

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

-	[목차](#목차)
-	[구린내와 탈취 기법](#구린내와-탈취-기법)
-	[메서드 정리](#메서드-정리)
	-	[메서드 추출](#메서드-추출)
	-	[메서드 내용 직접 삽입](#메서드-내용-직접-삽입)
	-	[임시변수 내용 직접 삽입 / 임시변수를 메서드 호출로 전환](#임시변수-내용-직접-삽입-임시변수를-메서드-호출로-전환)
	-	[직관적 임시변수 사용](#직관적-임시변수-사용)
	-	[임시변수 분리](#임시변수-분리)
	-	[매개변수로의 값 대입 제거](#매개변수로의-값-대입-제거)
	-	[메서드를 메서드 객체로 전환](#메서드를-메서드-객체로-전환)
	-	[알고리즘 전환](#알고리즘-전환)
-	[객체 간의 기능 이동](#객체-간의-기능-이동)
	-	[메서드 이동](#메서드-이동)
	-	[필드 이동](#필드-이동)
	-	[클래스 추출](#클래스-추출)
	-	[클래스 내용 직접 삽입](#클래스-내용-직접-삽입)
	-	[대리 객체 은폐](#대리-객체-은폐)
	-	[과잉 중개 메서드 제거](#과잉-중개-메서드-제거)
	-	[외래 클래스에 메서드 추가](#외래-클래스에-메서드-추가)
	-	[국소적 상속확장 클래스 사용](#국소적-상속확장-클래스-사용)
-	[데이터 체계화](#데이터-체계화)
	-	[필드 자체 캡슐화](#필드-자체-캡슐화)
	-	[데이터 값을 객체로 전환](#데이터-값을-객체로-전환)
	-	[값을 참조로 전환](#값을-참조로-전환)
	-	[참조를 값으로 전환](#참조를-값으로-전환)
	-	[배열을 객체로 전환](#배열을-객체로-전환)
	-	[관측 데이터 복제](#관측-데이터-복제)
	-	[클래스의 단방향 연결을 양방향으로 전환](#클래스의-단방향-연결을-양방향으로-전환)
	-	[클래스의 양방향 연결을 단방향으로 전환](#클래스의-양방향-연결을-단방향으로-전환)
	-	[마법 숫자를 기호 상수로 전환](#마법-숫자를-기호-상수로-전환)
	-	[필드 캡슐화](#필드-캡슐화)
	-	[컬렉션 캡슐화](#컬렉션-캡슐화)
	-	[레코드를 데이터 클래스로 전환](#레코드를-데이터-클래스로-전환)
	-	[분류 부호를 클래스로 전환](#분류-부호를-클래스로-전환)
	-	[분류 부호를 하위 클래스로 전환](#분류-부호를-하위-클래스로-전환)
	-	[분류 부호를 상태/전략 패턴으로 전환](#분류-부호를-상태전략-패턴으로-전환)
	-	[하위클래스를 필드로 전환](#하위클래스를-필드로-전환)
-	[조건문 간결화](#조건문-간결화)
	-	[조건문 쪼개기](#조건문-쪼개기)
	-	[중복 조건식 통합](#중복-조건식-통합)
	-	[조건문의 공통 실행 코드 빼내기](#조건문의-공통-실행-코드-빼내기)
	-	[제어 플래그 제거](#제어-플래그-제거)
	-	[여러 겹의 조건문을 감시 절로 전환](#여러-겹의-조건문을-감시-절로-전환)
	-	[조건문을 재정의로 전환](#조건문을-재정의로-전환)
	-	[Null 검사를 널 객체에 위임](#null-검사를-널-객체에-위임)
	-	[어설션 넣기](#어설션-넣기)
-	[메서드 호출 단순화](#메서드-호출-단순화)
	-	[메서드명 변경](#메서드명-변경)
	-	[매개변수 추가](#매개변수-추가)
	-	[매개변수 제거](#매개변수-제거)
	-	[상태 변경 메서드와 값 반환 메세드를 분리](#상태-변경-메서드와-값-반환-메세드를-분리)
	-	[메서드를 매개변수로 전환](#메서드를-매개변수로-전환)
	-	[매개변수를 메서드로 전환](#매개변수를-메서드로-전환)
	-	[객체를 통째로 전달](#객체를-통째로-전달)
	-	[매개변수 세트를 메서드로 전환](#매개변수-세트를-메서드로-전환)
	-	[매개변수 세트를 객체로 전환](#매개변수-세트를-객체로-전환)
	-	[쓰기 메서드 제거](#쓰기-메서드-제거)
	-	[메서드 은폐](#메서드-은폐)
	-	[생성자를 팩토리 메서드로 전환](#생성자를-팩토리-메서드로-전환)
	-	[하향 타입 변환을 캡슐화](#하향-타입-변환을-캡슐화)
	-	[에러 부호를 예외 통지로 전환](#에러-부호를-예외-통지로-전환)
	-	[예외 처리를 테스트로 교체](#예외-처리를-테스트로-교체)
-	[일반화 처리](#일반화-처리)
	-	[필드 상향](#필드-상향)
	-	[메서드 상향](#메서드-상향)
	-	[생성자 내용 상향](#생성자-내용-상향)
	-	[메서드 하향](#메서드-하향)
	-	[필드 하향](#필드-하향)
	-	[하위클래스 추출](#하위클래스-추출)
	-	[상위클래스 추출](#상위클래스-추출)
	-	[인터페이스 추출](#인터페이스-추출)
	-	[계층 병합](#계층-병합)
	-	[템플릿 메서드 형성](#템플릿-메서드-형성)
	-	[상속을 위임으로 전환](#상속을-위임으로-전환)
	-	[위임을 상속으로 전환](#위임을-상속으로-전환)
-	[복합 리팩토링](#복합-리팩토링)
	-	[상속 구조 정리](#상속-구조-정리)
	-	[절차 코드를 객체로 전환](#절차-코드를-객체로-전환)
	-	[도메인 로직을 표현과 분리](#도메인-로직을-표현과-분리)
	-	[계층구조 추출](#계층구조-추출)

<!-- tocstop -->

구린내와 탈취 기법
------------------

| 구린내                        | 탈취를 위한 리팩토링 기법                                                                                                                                             |
|:------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| swich문                       | `조건문을 재정의로 전환`,`분류 부호를 하위클래스로 전환`, `분류 부호를 상태/전략 패턴으로 전환`, `매개변수를 메서드로 전환`, `Null 검사를 널 객체에 위임`             |
| 강박적 기본 타입 사용         | `데이터 값을 객체로 전환`, `클래스 추출`, `매개변수 세트를 객체로 전환`, `배열을 객체로 전환`, `분류 부호를 하위클래스로 전환`, `분류 부호를 상태/전략 패턴으로 전환` |
| 과다한 매개변수               | `매개변수 세트를 메서드로 전환`, `매개변수 세트를 객체로 전환`, `객체를 통째로 전달`                                                                                  |
| 과잉 중개 메서드              | `과잉 중개 메서드 제거`, `메서드 내용 직접 삽입`, `위임을 상속으로 전환`                                                                                              |
| 기능의 산재                   | `메서드 이동`, `필드 이동`, `클래스 내용 직접 삽입`                                                                                                                   |
| 데이터 뭉치                   | `클래스 추출`, `매개변수 세트를 객체로 전환`, `객체를 통째로 전달`                                                                                                    |
| 데이터 클래스                 | `메서드 이동`, `필드 캡슐화`, `컬렉터 캡슐화`                                                                                                                         |
| 막연한 범용 코드              | `계층 병합`, `클래스 내용 직접 삽입`, `매개변수 제거`, `메서드명 변경`                                                                                                |
| 메시지 체인                   | `대리 객체 은폐`                                                                                                                                                      |
| 미흡한 라이브러리 클래스      | `외래 클래스에 메서드 추가`, `국소적 상속확장 클래스 사용`                                                                                                            |
| 방대한 클래스                 | `클래스 추출`, `하위클래스 추출`, `인터페이스 추출`, `데이터 값을 객체로 전환`                                                                                        |
| 방치된 상속물                 | `상속을 위임으로 전환`                                                                                                                                                |
| 불필요한 주석                 | `메서드 추출`, `어설션 넣기`                                                                                                                                          |
| 수정의 산발                   | `클래스 추출`                                                                                                                                                         |
| 인터페이스가 다른 대용 클래스 | `메서드명 변경`, `메서드 이동`                                                                                                                                        |
| 임시 필드                     | `클래스 추출`, `Null 검사를 널 객체에 위임`                                                                                                                           |
| 잘못된 소속                   | `메서드 이동`, `필드 이동`, `메서드 추출`                                                                                                                             |
| 장황한 메서드                 | `메서드 추출`, `임시변수를 메서드 호출로 전환`, `메서드를 메서드 객체로 전환`, `조건문 쪼개기`                                                                        |
| 중복코드                      | `메서드 추출`, `클래스 추출`, `메서드 상향`, `템블릿 메서드 형성`                                                                                                     |
| 지나친 관여                   | `메서드 이동`, `필드 이동`, `클래스의 양방향 연결을 단방향으로 전환`, `상속을 위임으로 전환`, `대리 객체 은폐`                                                        |
| 직무유기 클래스               | `클래스 내용 직접 삽입`, `계층 병합`                                                                                                                                  |
| 평행 상속 계층                | `메서드 이동`, `필드 이동`                                                                                                                                            |

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

![대리 객체 은폐](http://silverbullet.kr/wp-content/uploads/2017/03/hide-delefate.png)

### 과잉 중개 메서드 제거

-	클래스에 자잘한 위임이 너무 많을 땐 대리 객체를 클라이언트가 직접 호출하게 한다.

![과잉 중개 메서드 제거](http://silverbullet.kr/wp-content/uploads/2017/03/remove-middle-man.png)

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

데이터 체계화
-------------

### 필드 자체 캡슐화

-	필드에 직접 접근하던 중 그 필드로의 결합에 문제가 생길 땐 그 필드용 읽기/쓰기 메서드를 작성해서 두 메서드를 통해서만 필드에 접근하게 만든다.
-	변수 직접 접근 방식을 우선적으로 고려한다.
-	`필드 자체 캡슐화를 실시해야 할 시점` : 상위 클래스 안의 필드에 접근하되 이 변수 접근을 하위클래스에서 계산된 값으로 재정의해야 할 때이다.

**수정 전**

```java
private int low , high;
boolean includes (int arg ) {
  return arg >= low && arg <= high;
}

```

**수정 후**

```java
private int low , high;
boolean includes (int arg) {
  return arg >= getLow() && arg <= getHigh();
}
int getLow() {return low;}
int getHigh() {return high;}

```

### 데이터 값을 객체로 전환

-	데이터 항목에 데이터나 기능을 더 추가해야 할 때는 데이터 항목을 객체로 만든다.

![데이터 값을 객체로 전환](http://silverbullet.kr/wp-content/uploads/2017/03/replace-data-value-with-object.png)

**수정 전**

```java
// 개발 초기 단계에서는 단순 정보를 간단한 데이터 항목으로 표현. Order 객체로 데이터 Get한다.
class Order {
  public Order (String customer) {
    customer = customer;
  }
  public String getCustomer() {
    return customer;
  }
  public void setCustomer (String arg) {
    customer = arg;
  }
  private String customer;
}

class OrderService ...
  private int numberOfOrdersFor(Collection orders, String customer) {
    int result = 0;
    Iterator iter = orders.iterator();
    while (iter.hasNext()) {
    Order each = (Order) iter.next();
    if (each.getCustomer().equals (customer)) result++;
    return result;
  }
...

```

**수정 후**

```java
// 간단한 항목이 점점 복잡해진다(ex.형식화,지역번호 추출등). 항목객체(Customer)를 추가하여 항목들을 객체로 관리한다.

// Order 객체 수정.
class Order {
  public Order (String customer) {
    customer = new Customer(customer);
  }
  public String getCustomer() {
    return customer.getName();
  }
  private Customer customer;
  public void setCustomer (String arg) {
    customer = new Customer(arg );;
  }
}

// Customer 객체 추가
class Customer {
  public Customer (String name) {
    name = name;
  }
  public String getName() {
    return name;
  }
  private final String name;
}

class OrderService ...
  private int numberOfOrdersFor(Collection orders, String customer) {
    int result = 0;
    Iterator iter = orders.iterator();
    while (iter.hasNext()) {
    Order each = (Order) iter.next();
    if (each.getCustomer().equals (customer)) result++;
    return result;
  }
...

```

### 값을 참조로 전환

-	객체는 참조객체와 값 객체로 분류 할 수 있다. 참조 객체는 고객이나 계좌 같은 것이다. - 클래스에 같은 인스턴스가 많이 들어 있어서 이것들을 하나의 객체로 바꿔야 할 땐 그 객체를 참조 객체로 전환한다. - 고객이나 계좌 같이 현실에서 한 객체 대응하는 경우, 개념상 동일한 고객에 주문이 여러 개 있을 경우 하나의 객체만 사용하게끔 수정해야한다. `생성자를 팩토리 메서드로 전환`으로 하나의 객체만 있도록 한다.

### 참조를 값으로 전환

-	`값 객체` : 아주 작고 단순한 객체이다. 객체를 마치 값처럼 사용하는 것이다. 값 5에 또다른 값 5를 더하는 오퍼레이션을 실행하면, 5가 10으로 변하는 것이 아니라 10이라는 새로운 값이 만들어지는 것처럼, 값 객체 패턴에서도 값 객체에 어떤 오퍼레이션을 가하면, 그 값 객체가 변하는 것이 아니라 새로운 값 객체를 리턴하게 된다. - 참조 객체가 작고 수정할 수 없고 관리하기 힘들 땐 그 참조 객체를 값 객체로 만든다. - 참조 객체를 사용한 작업이 복잡해지는 순간이 참조를 값으로 바꿔야 할 시점이다.

### 배열을 객체로 전환

-	배열을 구성하는 특정 원소가 별의별 의미를 지닐 땐 그 배열을 각 원소마다 필드가 하나씩 든 객체로 전환한다.

### 관측 데이터 복제

-	도메인 데이터는 GUI 컨트롤 안에서만 사용 가능한데, 도메인 메서드가 그 데이터에 접근해야 할 땐 그 데이터를 도메인 객체로 복사하고, 양측의 데이터를 동기화하는 관측 인터페이스 observer를 작성한다. - 비지니스 로직이 사용자 인터페이스 안에 들어 있는 2계층 방식으로 개발된 코드가 있다면 인터페이스에서 기능을 분리해야 한다. - `MVC 패턴`과 같이 분리해야 한다.

### 클래스의 단방향 연결을 양방향으로 전환

-	두 클래스가 서로의 기능을 사용해야 하는데 한 방향으로만 연결되어 있을 땐 역 포인터를 추가하고 두 클래스를 모두 업데이트 할 수 있게 전급 한정자를 수정한다.

### 클래스의 양방향 연결을 단방향으로 전환

-	두 클래스가 양방향으로 연결되어 있는데 한 클래스가 다른 클래스의 기능을 더 이상 사용하지 않게 됐을 땐 불필요한 방향의 연결을 끊는다. - 양방향 연결은 쓸모가 많지만 대가가 따른다. 1. 복잡함이 더해진다. 2. 좀비 객체가 발생하기 쉽다. `좀비 객체`란 참조가 삭제되지 않아 제거 되어야 함에도 남아 떠도는 객체이다. 3. 양방향 연결로 인해 두 클래스는 서로 종속된다. - 양방향 연결을 꼭 필요할 때만 사용해야 한다.

### 마법 숫자를 기호 상수로 전환

-	특수 의미를 지닌 숫자가 있을 땐 의미를 살린 이름의 상수를 작성한 후 리터럴 숫자를 그 상수로 교체한다.**수정 전**

```java
double potentialEnergy(double mass , double height) {
  return mass * 9.81 * height;
}

```

**수정 후**

```java
static final double GRAVITATIONAL_CONSTANT = 9.81;

double potentialEnergy(double mass , double height) {
  return mass * GRAVITATIONAL_CONSTANT * height;
}

```

### 필드 캡슐화

-	public 필드가 있을 땐 그 필드를 private로 만들고 필드용 읽기 메서드와 쓰기 메서드를 작성한다.

**수정 전**

```java
public String name;

```

**수정 후**

```java
private String name;
public String getName() {return name;}
public void setName(String arg) {name = arg;}

```

### 컬렉션 캡슐화

-	메서드가 컬렉션을 반환할 땐 그 메서드가 읽기전용 뷰를 반환하게 수정하고 추가 메서드와 삭제 메서드를 작성한다.

**수정 전**

```java
class Course...
  public Course (String name , boolean isAdvanced) {...};
  public boolean isAdvanced () {...};
...

class Person ...
  public Set getCourses () {
    return courses;
  }
  public void setCourses (Set arg ) {
    courses = arg;
  }
  private Set courses ;
...

// 컬렉션 사용 코드
Person kent = new Person();
Set s = new HashSet();
s.add (new Course("스몰토크 프로그래밍"， false));
s.add(new Course ("싱글몰트 위스키 음미하기"， true));
kent.setCourses(s);
Assert.equals (2, kent.getCourses().size());
Course refact = new Course ("리맥토링 true");
kent.getCourses().add(refact);
kent.getCourses().add(new Course ("지독한 빈 정 거림", false));
Assert.equals(4, kent.getCourses().size()) ;
kent.getCourses().remove(refact);
Assert.equals(3, kent.getCourses().size());

```

**수정 후**

```java
class Person {
  private Set courses = new HashSet();

  public void addCourse(Course arg) (
    courses.add(arg);
  }
  public void removeCourse(Course arg) {
    courses.remove (arg );
  }
}

// 컬렉션 사용 코드
Person kent = new Person();
kent.addCourse(new Course ("스몰토크 프로그래밍’" fal se));
kent.addCourse(new Course ("싱글몰트 위스키 음미하기’ true));
...

```

### 레코드를 데이터 클래스로 전환

-	전통적인 프로그래밍 환경에서 레코드 구조를 이용한 인터페이스를 제공해야 할 땐 레코드 구조를 저장할 덤 데이터 객체를 작성한다.

### 분류 부호를 클래스로 전환

-	기능에 영향을 미치는 숫자형 분류 부호가 든 클래스가 있을 땐 그 숫자를 새 클래스로 바꾼다.

**수정 전**

```java
public static final int 0 = 0;
public static final int A = 1;
public static final int B = 2;
public static final int AB = 3;
private int bloodGroup;

```

**수정 후**

```java
public static final BloodGroup 0 = new BloodGroup(0);
public static final BloodGroup A = new BloodGroup(1);
public static final BloodGroup B = new BloodGroup(2);
public static final BloodGroup AB = new BloodGroup(3);
private static final BloodGroup[] values = {O, A, B, AB};

private final int code;
private BloodGroup (int code ) {
code = code;

```

### 분류 부호를 하위 클래스로 전환

-	클래스 기능에 영향을 주는 변경불가 분류 부호가 있을 땐 분류 부호를 하위클래스로 만든다.

![분류 부호를 하위 클래스로 전환](http://silverbullet.kr/wp-content/uploads/2017/03/replace-type-code-with-subclasses.png)

### 분류 부호를 상태/전략 패턴으로 전환

-	분류 부호가 클래스의 영향을 주지만 하위클래스로 전환할 수 없을 땐 그 분류 부호를 상태 객체로 만든다.

![분류 부호를 상태/전략 패턴으로 전환](http://silverbullet.kr/wp-content/uploads/2017/03/replace-type-code-with-state-strategy.png)

### 하위클래스를 필드로 전환

-	여러 하위클래스가 상수 데이터를 반환하는 메서드만 다를 땐 각 하위클래스의 메서드를 상위클래스 필드로 전환하고 하위클래스는 전부 삭제한다.

![하위클래스를 필드로 전환](http://silverbullet.kr/wp-content/uploads/2017/03/replace-subclass-with-fields.png)

**수정 전**

```java
abstract class Person {
  abstract boolean isMale() ;
  abstract char getCode() ;
}
class Male extends Person {
  boolean isMale () {
    return true;
  }
  char getCode() {
    return "M";
  }
}

```

**수정 후**

```java
class Person{
  private final boolean isMale ;
  private final char code;

  protected Person (boolean isMale , char code ) {
    isMale = isMale ;
    code = code;
  }

  static Person createMale () {
    return new Person (true, "M");
  }
}
```

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

메서드 호출 단순화
------------------

### 메서드명 변경

-	메서드명을 봐도 기능을 알 수 없을 땐 메서드명을 직관적인 이름으로 바꾼다.

### 매개변수 추가

-	메서드가 자신을 호출한 부분의 정보를 더 많이 알아야 할 땐 객체에 그 정보를 전달할 수 있는 매개변수를 추가한다.

### 매개변수 제거

-	메서드가 어떤 매개변수를 더 이상 사용하지 않을 땐 그 매개변수를 삭제한다.

### 상태 변경 메서드와 값 반환 메세드를 분리

-	값 반환 기능과 객체 상태 변경 기능이 한 메서드에 들어 있을 땐 질의 메서드와 변경 메서드를 분리한다.

![상태 변경 메서드와 값 반환 메서드를 분리](http://silverbullet.kr/wp-content/uploads/2017/03/separate-query-from-modifier.png)

### 메서드를 매개변수로 전환

-	여러 메서드가 기능이 비슷하고 안에 든 값만 다를 땐 서로 다른 값을 하나의 매개변수로 전달받는 하나의 메서드를 만든다.

![메서드를 매개변수로 전환](http://silverbullet.kr/wp-content/uploads/2017/03/parameterize-method.png)

### 매개변수를 메서드로 전환

-	매개변수로 전달된 값에 따라 메서드가 다른 코드를 실행할 땐 그 매개변수로 전달될 수 있는 모든 값에 대응하는 메서드를 각각 만든다.
-	`매개변수를 메서드로 전환`은 `메서드를 매개변수로 전환`의 작업을 거꾸로 하면 된다.

### 객체를 통째로 전달

-	객체에서 가져온 여러 값을 메서드 호출에서 매개변수로 전달할 땐 그 객체를 통체로 전달한다.

### 매개변수 세트를 메서드로 전환

-	객체가 A 메서드를 호출해서 그 결과를 B 메서드에 매개변수로 전달하는데, 결과를 매개변수로 받는 B 메서드도 직접 A 메서드를 호출할 수 있을 땐 매개변수를 없애고 A 메서드를 B 메서드가 호출하게 한다.
-	메서드가 매개변수로 전달받는 값을 다른 방법으로 가져올 수 있다면, 그 방법을 택해야 한다.

### 매개변수 세트를 객체로 전환

-	여러 개의 매개변수가 항상 붙어 다닐 땐 그 매개변수를 객체로 바꾼다.

### 쓰기 메서드 제거

-	생서할 때 지정한 필드 값이 절대로 변경되지 말아야 할 땐 그 필드를 설정하는 모든 쓰기 메서드(Set)를 제거한다.

### 메서드 은폐

-	메서드가 다른 클래스에서 사용되지 않을 땐 그 메서드의 반환 타입을 private로 만든다.

### 생성자를 팩토리 메서드로 전환

-	객체를 생성할 때 단순한 생성만 수행하게 해야 할 땐 생성자를 팩토리 메서드로 교체한다.

### 하향 타입 변환을 캡슐화

-	메서드가 반환하는 객체를 호출 부분에서 하향 타입 변환해야 할 땐 하향 타입 변환 기능을 메서드 안으로 옮긴다.

### 에러 부호를 예외 통지로 전환

-	메서드가 에러를 나타내는 특수한 부호를 반환할 땐 그 부호 반환 코드를 예외 통지 코드로 바꾼다.

### 예외 처리를 테스트로 교체

-	호출 부분에 사전 검사 코드(조건문으로 해당 에러 제거 코드)를 넣으면 될 상황인데 예외 통지를 사용했을 땐 호출 부분이 사전 검사를 실시하게 수정한다.

일반화 처리
-----------

### 필드 상향

-	두 하위클래스에 같은 필드가 들어 있을 땐 필드를 상위 클래스로 옮긴다.

### 메서드 상향

-	기능이 같은 메서드가 `여러 하위클래스에 들어 있을땐` 그 메서드를 상위클래스로 옮긴다.

### 생성자 내용 상향

-	하위클래스마다 거의 비슷한 내용의 생성자가 있을 땐 상위클래스에 생성자를 작성하고 그 생성자를 하위 클래스의 메서드에 호츨한다.

### 메서드 하향

-	상위클래스에 있는 기능을 `일부 하위클래스만 사용`할 땐 그 기능을 관련된 하위클래스 안으로 옮긴다.
-	`메서드 하향`은 `메서드 상향`과 반대되는 기법.
-	클래스의 기능을 특정 하위클래스로 옮겨야 할 때 사용한다.

### 필드 하향

-	일부 하위클래스만이 사용하는 필드가 있을 땐 그 필드를 사용하는 하위클래스로 옮긴다.

### 하위클래스 추출

-	일부 인스턴스에만 사용되는 기능이 든 클래스가 있을 땐 그 기능 부분을 전담하는 하위클래스를 작성한다.
-	`하위클래스 추출` 대신 `클래스 추출`을 사용할 수 있다. `위임`이냐 `상속`이냐의 차이이다.
-	객체가 생성된 후에는 객체의 클래스 `기반 기능`을 수정할 수 없다.
-	클래스 기반 기능을 수정하려면 단순히 다른 각종 컴포넌트를 연결해서 `클래스 추출`을 실시한다.

![하위클래스 추출](http://silverbullet.kr/wp-content/uploads/2017/03/Extract-Subclass.png)

### 상위클래스 추출

-	기능이 비슷한 두 클래스가 있을 땐 상위클래스를 작성하고 공통된 기능들을 그 상위클래스로 옮긴다.

![상위클래스 추출](http://silverbullet.kr/wp-content/uploads/2017/03/Extract-Superclass.png)

### 인터페이스 추출

-	클래스 인터페이스의 같은 부분을 여러 클라이언트가 사용하거나 두 클래스에 인터페이스의 일부분이 공통으로 들어 있을 땐 공통 부분을 인터페이스로 빼낸다.
-	많은 객체지향 언어에서 이 기능은 다중 상속을 통해 구현한다.
-	자바는 하나의 클래스밖에 상속을 할 수 없고, 인터페이스를 사용하여 구현할 수 있다.

### 계층 병합

-	상위클래스와 하위클래스가 거의 다르지 않을 땐 둘을 합친다.

### 템플릿 메서드 형성

-	하위클래스 안의 두 메서드가 거의 비슷한 단계들을 같은 순서로 수행할 땐 그 단계들을 시그너처가 같은 두 개의 메서드로 만들어 두 원본 메서드를 같게 만든 후, 두 메서드를 상위클래스로 옮긴다.
-	두 메서드가 똑같지는 않지만 거의 비슷한 단계를 같은 순서로 수행하는 경우 그 순서를 상위클래스로 옮기고 재정의를 통해 각 단계가 고유의 작업을 다른 방식으로 수행하게 하면 된다. 이러한 메서드를 `템플릿 메서드`라고 한다.

![템플릿 메서드 형성](http://silverbullet.kr/wp-content/uploads/2017/03/Form-Template-Method.png)

**수정전**

```java
public class Customer {
    public String statement() {
        return new TextStatement().value(this);
    }
    public String htmlStatement() {
        return new HtmlStatement().value(this);
    }
}
```

```java
public class HtmlStatement {

    public String value(Customer customer) {
        int multiply = 10 * 8;
        String result = "HtmlStatement : 고객님 대여 기록";

        for (int i = 0; i < 6; i++) {
            result += "누적 포인트 HtmlStatement";
        }
        result += "누적 대여료 HtmlStatement";
        return result;
    }

}
```

```java
public class TextStatement {

    public String value(Customer customer) {
        int multiply = 10 * 8;
        String result = "TextStatement : 고객님 대여 기록";

        for (int i = 0; i < 6; i++) {
            result += "누적 포인트 TextStatement";
        }
        result += "누적 대여료 TextStatement";
        return result;
    }

}
```

**수정 후**

```java
public class Customer {
    public String statement() {
        return new TextStatement().value(this );
    }
    public String htmlStatement() {
        return new HtmlStatement().value(this );
    }
}
```

```java
public abstract class Statement {
    public abstract String headerString();
    public abstract String eachString();
    public abstract String footerString();

    public String value(Customer customer) {
        int multiply = 10 * 8;
        String result = headerString();

        for (int i = 0; i < 6; i++) {
            result += eachString();
        }
        result += footerString();
        return result;
    }
}
```

```java
public class HtmlStatement extends Statement{

    @Override
    public String headerString() {
        return "HtmlStatement : 고객님 대여 기록";
    }

    @Override
    public String eachString() {
        return "누적 포인트 HtmlStatement";
    }

    @Override
    public String footerString() {
        return "누적 대여료 HtmlStatement";
    }
}
```

```java
public class TextStatement extends Statement{

    @Override
    public String headerString() {
        return "TextStatement : 고객님 대여 기록";
    }

    @Override
    public String eachString() {
        return "누적 포인트 TextStatement";
    }

    @Override
    public String footerString() {
        return "TextStatement : 고객님 대여 기록";
    }
}
```

### 상속을 위임으로 전환

-	하위클래스가 상위클래스 `인터페이스의 일부`만 사용할 때나 데이터를 상속받지 않게 해야할 땐 상위클래스에 필드를 작성하고, 모든 메서드가 그 상위클래스에 위임하게 수정한 후 하위클래스를 없앤다.

### 위임을 상속으로 전환

-	위임을 이용중인데 `인터페이스 전반`에 간단한 위임으로 도배하게 될 땐 위임 클래스를 대리 객체의 하위클래스로 만든다.
-	`상속을 위임으로 전환`기법을 반대로 하면 된다.

복합 리팩토링
-------------

### 상속 구조 정리

-	하나의 상속 계층이 두 작업을 동시에 수행할 땐 상속 계층을 하나 더 만들어서 위임을 통해 다른 계층을 호출한다.

![상속 구조 정리](http://silverbullet.kr/wp-content/uploads/2017/03/Tease-Apart-Inheritance.png)

### 절차 코드를 객체로 전환

-	코드가 절차식으로 작성되어 있을 땐 데이터 레코드를 객체로 바꾸고, 기능을 쪼개서 각각의 객체로 옮긴다.

### 도메인 로직을 표현과 분리

-	도메인 로직이 들어 있는 GUI 클래스가 있을 땐 도메인 로직을 별도의 도메인 클래스로 떼어낸다.
-	MVC 패턴과 같인 표현과 분리.

### 계층구조 추출

-	한 클래스에 기능이 너무 많고 일부분에라도 조건문이 많을 땐 각 조건에 해당하는 하위클래스를 작성해서 계층구조를 만든다.

![계층구조 추출](http://silverbullet.kr/wp-content/uploads/2017/03/Extract-Hierarch.png)
