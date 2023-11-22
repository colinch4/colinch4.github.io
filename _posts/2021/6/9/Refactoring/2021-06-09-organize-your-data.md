---
layout: post
title: "[Refactoring] 데이터 체계화"
description: " "
date: 2021-06-09
tags: [개발]
comments: true
share: true
---

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

![데이터 값을 객체로 전환](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzSGdVZW1Gdms5OGM)

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

-	두 클래스가 양방향으로 연결되어 있는데 한 클래스가 다른 클래스의 기능을 더 이상 사용하지 않게 됐을 땐 불필요한 방향의 연결을 끊는다.
-	양방향 연결은 쓸모가 많지만 대가가 따른다.
	1.	복잡함이 더해진다.
	2.	좀비 객체가 발생하기 쉽다. `좀비 객체`란 참조가 삭제되지 않아 제거 되어야 함에도 남아 떠도는 객체이다.
	3.	양방향 연결로 인해 두 클래스는 서로 종속된다. - 양방향 연결을 꼭 필요할 때만 사용해야 한다.

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

![분류 부호를 하위 클래스로 전환](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzVXVlRU8ybElHLXM)

### 분류 부호를 상태/전략 패턴으로 전환

-	분류 부호가 클래스의 영향을 주지만 하위클래스로 전환할 수 없을 땐 그 분류 부호를 상태 객체로 만든다.

![분류 부호를 상태/전략 패턴으로 전환](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzdWJFcndQNlFnejA)

### 하위클래스를 필드로 전환

-	여러 하위클래스가 상수 데이터를 반환하는 메서드만 다를 땐 각 하위클래스의 메서드를 상위클래스 필드로 전환하고 하위클래스는 전부 삭제한다.

![하위클래스를 필드로 전환](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzVC1FUk9QcUdHRUk)

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
