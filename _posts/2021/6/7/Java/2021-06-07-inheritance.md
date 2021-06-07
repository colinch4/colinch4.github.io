---
layout: post
title: "[java] Inheritance 상속"
description: " "
date: 2021-06-07
tags: [java]
comments: true
share: true
---


# 👨‍👩‍👧‍👦 Inheritance 상속

## Inheritance 상속

> - 상속 : 부모 클래스에서 자식클래스에게 물려주는 것. 중복되는 속성과 메소드를 더 효율적으로 활용할 수 있음

#### 상속의 특징

    1. 자식 클래스는 단 하나의 부모클래스만 상속받을 수 있음.
    2. 부모클래스의 private field는 상속대상 제외 / 다른 패키지에 존재시, defualt 값도 상속에서 제외

<br />

- 부모 클래스

```java
public class Parent{
    int field1;
    void method(){}
}
```

- 자식 클래스
  extends로 부모 클래스를 상속받음 ( ⛳️ 상속받을 부모클래스는 단 1개만 )

```java
public class Child extends Parent{
    String field 2;
}
```

<br />

#### 부모 생성자의 호출

> 모든 객체는 클래스의 생성자를 호출해야만 생성되므로, 자식 class에서 부모 객체를 생성하기 위해서는 부모 생성자를 호출해야함
> **Constructor super** ==> 부모 기본생성자 호출

<br />

- 부모 클래스 생성자 : 공통적으로 사용될 인자값들을 선언하고, 생성자에서 자식클래스로 넘겨준다.

```java
public class Parent{

    public String name;
    public String ssn;

    public People(String name, String ssn){
        this.name = name;
        this.ssn = ssn;
    }
}
```

- 자식 클래스 생성자 : super()로 부모클래스의 값들을 상속받고, 내부적인 field값은 따로 정의해준다.

```java
// public Child(int 부모class에서 받은 인자){
//     super(부모class에서 받은 인자);
// }

public class Child extends Parent{
    public int studentNo;

    public Child(String name, String ssn){
        super(name, ssn); // 부모 클래스에서 물려받은 것
        this.studentNo = studentNo; // 자식클래스 내부 field값
    }
}

```

<br />

#### Override 매소드 재정의

> 부모클래스에서 받은 메소드를 자식클래스에서 더 적합하게 재정의하는 것
> super()로 부모클래스 매소드에 접근해서 호출

<br/>

⛔️ **Override 주의사항** ⛔️

1. 부모 매소드와 동일한 시그니처 (리턴타입, 메소드이름, 매개변수목록)을 가져야함.
2. 접근 제한을 더 강하게 재정의 ❌
   예) 부모매소드가 public인데 자식매소드는 dafualt나 private으로 할 수는 없음
   <=> 반대는 가능 (부모 : default , 자식: public ⭕️)

   <br />

- 부모클래스 매소드

```java
public class Parent{
    public String getDetail(){
        return person.getName() + person.getAge();
    }
}
```

- 자식클래스 매소드 : 부모클래스 매소드를 받아온 후 오버라이드 함

```java
public class Child extends Parent{

    @Overrid
    public String getDetail(){
        return super.getDetail() + person.getSsn();
        //super로 부모클래스의 메소드를 받아오고 + 추가해줌
    }
}
```

<br />

#### ✂️ Final 클래스, 필드, 매소드

> 클래스, 필드, 매소드 선언시 final로 선언하면 해당 선언이 최종상태이며 수정될 수 없음을 의미
> **final** == 상속 관련

1. final class = 최종 클래스로 자식클래스한테 상속 할 수 없음.
   ```java
   public final class FianlClass {}
   ```
2. fianl method = 자식클래스에서 Override 할 수 없음
   ```java
   public final String method () {}
   ```
