---
layout: post
title: "[java] Overloading & Overriding"
description: " "
date: 2021-06-07
tags: [java]
comments: true
share: true
---

# 🌈 Overloading & Overriding

<br />

## Overlading 오버로딩

> 외부에서 제공되는 다양한 데이터로 객체를 생성하고 활용하기 위해 매소드 혹은 생성자를 중복정의 하는 것

<br>

- **생성자 오버로딩**
  > - 외부에서 받아오는 데이터에 따라 생성자를 호출할 수 있도록 하는 것
  > - 생성자를 여러 개 선언하여 사용
  > - 다른 생성자를 호출하기 위해 **this()** 를 사용

```java
public class Car{
    Car(){ ... }
    Car(String model){}
    Car(String model, String Color){};
    Car(String model, String Color, int maxSpeed){}
}
```

```java
//this 사용
public class Car{
    String model;
    String Color;
    int maxSpeed;


    Car(){ ... }
    Car(String model){
        this(model, sliver, 250)
    }
    Car(String model, String Color){
        this(model, color, 250)

    };

    //공통 실행 코드가 있는 생성자를 위에서 this로 호출할 수 있도록
    Car(String model, String Color, int maxSpeed){
        this.model = model;
        this.color = color;
        this.maxSpeed = maxSpeed;
    }
}

```

<br >

- **매소드 오버로딩**
  > - 클래스 내에 같은 매소드를 여러개 정의하여 파라미터에 따라 다른 결과값을 리턴하도록 하는 것
  > - 같은 기능, 같은 매소드이름 사용 가능 (일관성 유지)

```java

//같은 매소드지만 받는 파라미터에 따라 다르게 값을 리턴함
public class Overload{

    public String test(){
        return "리턴값이 없습니다."
    }

      public String test(int a){
        return a + "를 받았습니다."
    }

      public String test(String b){
        return b + "를 리턴합니다."
    }

}
```

<br ><br >

## Overriding 매소드 재정의

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

    @Override
    public String getDetail(){
        return super.getDetail() + person.getSsn();
        //super로 부모클래스의 메소드를 받아오고 + 추가해줌
    }
}
```

<br />
