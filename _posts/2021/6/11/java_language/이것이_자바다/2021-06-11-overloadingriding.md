---
layout: post
title: "[이것이자바다] chapter . 오버로딩(Overloading) 과 오버라이딩(Overiding)"
description: " "
date: 2021-06-11
tags: [이것이자바다]
comments: true
share: true
---

## 오버로딩(Overloading) 과 오버라이딩(Overiding)

* 오버로딩(Overloading): 같은 이름의 메소드를 여러개 가지면서 매개변수의 유형과 개수를 다르도록 하는 기술.

* 오버라이딩(Overliding): 상위 클래스가 가지고 있는 메소드를 하위 클래스가 재정의 해서 사용하는 것.

### 오버로딩(Overloading)

오버로딩(Overloading)은 1.메소드 오버로딩과 생성자 오버로딩이 있다.
하지만 둘다 같은 개념이다.<br>

```java 
public class Overloadingtest{

  //test() 호출
  void test(){
    System.out.println("매개변수 없음");
  }

  //test에 매개변수로 int형 2개 호출
  void test(int a, int b){
    System.out.println("매개변수 " + a + "와" +b);
  }

  //test에 매개변수 double형 1개 호출
  void test(double d){
    System.out.println("매개변수 " + d);
	}

}
```


### 오버라이딩(Overliding)

상위 클래스가 가지고 있는 멤버변수가 하위 클래스로 상속되는 것처럼<br>
상위 클래스가 가지고 있는 메소드도 하위 클래스로 상속되어 하위 클래스에서
사용할 수 있다.<br>
하지만, 하위 클래스에서 상위 클래스의 메소드를 재정의해서 사용 할 수도 있다.<br>

==> 상속 관계에 있는 클래스 간에 같은 이름의 메소드를 정의하는 기술을 오버라이딩(Overriding)이라고 한다.<br>

```java
pulbic class Employee{

  String name;
  int age;
  
  //print() 메소드
  public void print(){
    System.out.prinln("사원의 이름은 " + this.name + "이고, 나이는 " +this.age + "입니다.");
	}
}

// Employee 상속
pulbic class Manager extends Employee{

  // 부모의 메소드를 재정의: Overriding
  @Override
  public void print(){
    System.out.prinln("매니저의 이름은 " + this.name + "이고, 나이는 " +this.age + "입니다.");
	}
}
```


