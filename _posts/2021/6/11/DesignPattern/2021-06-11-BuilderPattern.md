---
layout: post
title: "[디자인패턴] 생성자에 매개변수가 많다면 빌더를 고려하라"
description: " "
date: 2021-06-11
tags: [디자인패턴]
comments: true
share: true
---

## 생성자에 매개변수가 많다면 빌더를 고려하라

생성자에 선택적 매개변수가 많을 때 취해지는 3가지 방법으로 점층적 생성자 패턴, 빈즈 패턴, 빌더 패턴이 있다.

> 점층적 생성자 패턴(Telescoping Constructor Pattern)

생성자 오버로딩(Constructor Overloading)을 이용해 필수 매개변수만 받는 생성자, 필수 매개변수와 선택 매개변수 1개를 받는 생성자, ..., 선택 매개변수를 전부 받는 생성자까지 생성자를 늘려가는 방식으로서 과거에 많이 사용하였다. (코드의 중복을 피하기 위해 this()를 사용한다.)

### 단점

: 하지만 이러한 방식의 코드는 **매개변수의 개수가 많아질수록, 작성하기도 어렵고 읽기도 어렵다. 매개변수가 많다면** **코드를 읽을 때 각 값의 의미가 무엇인지 헷살리고, 매개변수가 몇 개인지도 주의깊게 세워 보아야 할 것이다.** 

또, 타입이 같은 매개변수가 많아 실수로 **매개변수의 순서를 바꿔 입력해도 컴파일오류가 안날수 있어 결국 런타임때 잘못된 값이 나오게 된다.**

```java
    public class User {
    		private String name; // 필수
    		private int age;// 필수 
    
    		private String address; //선택
    		private int level; //선택
    		private int money; //선택
    
    
    //생성자 1 : name, age, address, level , money
    User(String name, int age, String address, int level, int money){
        this.name = name;
        this.age = age;
        this.address = address;
        this.level = level;
        this.money = money;
    }
    
    //생성자 2 : name, age, address
    User(String name, int age, String address){
        this(name,age,address,0,0);
    }
    
    //생성자 3 : name, age, level
    User(String name, int age, int level){
        this(name,age,"",level,0);
    } 
    
    //생성자 4: name, age, address, money
    User(String name, int age, String address, int money){
        this(name,age,address,0,money);
    }
    
    //생성자 5 : name ,age => 필수만 모음
    User(String name, int age){
        this(name,age,"",0,0);
    }
    
    // 생성자 6 : name, age, level, money
    User(String name, int age, int level, int money){
        this(name,age,"",0,0); 
    }
    
    // 점층적 생성자 패턴으로 객체를 생성한다면 읽을때 각 값의 의미가 무엇인지
    // 헷갈릴 수 있고, 또 같은 타입의 매개변수가 많은 경우 값을 잘못 넣어
    // 결국에 런타임에 잘못된 값이 출력될 수 있다. 
    
    }

```

> 자바빈즈 패턴(JavaBeans Pattern)

- 매개변수가 없는 생성자로 객체를 만든 후, 세터(setter) 메소드들을 호출해 원하는 매개변수의 값을 설정하는 방식

### 장점

: set 메소드를 이용해 필드의 값을 초기화하므로 이 방법은 점층적 생성자 패턴의 단점을 해결한다.         

일단 매개변수가 없는 생성자로 객체를 만드므로, **매개변수에 값이 정확히 들어갔는지 조심하며 매개값을 지정하지 않아도 된다.** 또 코드를 읽을때 **값의 의미가 구체적으로 보이므로(setName("kim"), setAge(27)) 점층적 생성자 패턴보다 가독성이 뛰어나다.**

### 단점

: 하지만 이 패턴도 치명적인 단점이 있는데, **객체 하나를 만들려면 메소드를 여러 개 호출해야 하고, 객체가 완전히 생성되기 전까지는 일관성이 무너진다는 점이다.** 점층적 생성자 패턴은 new 연산자(생성자 이용)를 사용할때부터 매개변수 값들이 유효하므로 일관성이 있는데, 자바 빈즈 패턴은 매개변수 없이 객체를 만들었으므로 필드값이 default한 값, 즉 유효성이 없다가 이후 set 메소드를 통해 유효해지므로 일관성이 깨지는 것이다. 

**일관성이 깨지므로 당연히 클래스도 불변으로 만들 수 없고(final 키워드를 사용하면 컴파일 오류가 난다.)**, 이는 스레드 안정성을 얻기 위해 프로그래머가 추가 작업을 해줘야만 하는 것을 의미한다.
한마디로 사용하면 무지 골치 아프다.


```java
    public class User {
    		private String name; // 필수
    		private int age;// 필수
    
    		private String address; //선택
    		private int level; //선택
    		private int money; //선택
    
    // Beans Pattern의 예로 Name 과 age만 set 메소드를 만들었다. 
    public void setName(String name) {
        this.name = name;
    }
    
    public void setAge(int age) {
        this.age = age;
    }
    }
    
    public class UserExample{
    
    public static void main(Stirng[] args){
        User user = new User(); // 매개변수 없이 객체 생성.
        user.setName("kim");
        user.setAge(27); // 인스턴스를 만들기 쉽고, 
        // 또 각 값의 의미를 구체적으로 알 수 있기 때문에 읽기 쉽다. 
    
        // 하지만 위의 코드처럼 자바빈즈 패턴은 객체 하나를 만들려면 메소드를 여러개 호출해야 하고, 객체가 완전히 생성되기 전까지 일관성(Consistency)가 무너지게된다. 또 불변 객체를 생성할 수도 없다. 
    }
    }
```


> 빌더 패턴(Builder Pattern)

빌더 패턴은 **점층적 생성자 패턴의 안전성**과 **자바빈즈 패턴의 가독성**을 겸비한 패턴이다. 즉 둘의 단점을 모두 극복한 패턴이다.

- 빌더 패턴은 생성할 클래스 안에 **빌더(Builder)라는 정적 클래스**를 만들어 클라이언트가 필요한 객체를 직접 만드는 대신, **(1)필수 매개변수만으로 생성자를 호출해 빌더 객체를 얻은 뒤**, **(2) 빌더 객체가 제공하는 일종의 setter 메소드로 원하는 선택 매개변수를 설정하고**, **(3)마지막으로 매개변수가 없는 build 메소드를 호출해** 드디어 우리에게 필요한 객체(보통은 불변인)를 얻는 방법이다.

- 아래 코드는 빌더 패턴으로 작성한 코드인데, 보이는 것처럼 필드값에 final를 지정하여 클래스를 불변하게 만들 수 있다. 따라서 스레드 안정성을 얻으려고 추가작업을 하지 않아도 된다.

- 또 아래의 코드중 Program 클래스의 메인에서 user2 객체를 보면 빌더의 세터 메소드들이 연쇄적으로 호출이 됨을 볼 수 있는데, 이런 방식을 메서드 호출이 흐르듯 연결된다는 뜻으로 플루언트 API(fluent API) 또는 메소드 연쇄(method chaining)이라 한다.


```java
    public class User {
    		private final String name; // 필수
    		private final int age;// 필수
    
    		private final String address; //선택
    		private final int level; //선택
    		private final int money; //선택
    
    		User(Builder builder){
    	    this.name = builder.name;
    	    this.age = builder.age;
    	    this.address = builder.address;
    	    this.level = builder.level;
    	    this.money = builder.money;
    		}
    
    static class Builder{
        //필수 매개변수
        private String name;
        private int age;
    
        //선택 매개변수 - 기본값으로 초기화한다.
        private String address="";
        private int level=0;
        private int money=0; 
        
        //필수 매개변수는 생성자를 통해 얻는다.
        Builder(String name, int age) {
            this.name = name;
            this.age = age;
        }
    
        //선택 매개변수는 setter메서드를 통해 설정한다.
        Builder address(String address){
            this.address = address;
            return this;
        }
    
        Builder level(int level){
            this.level = level;
            return this;
        }
    
        Builder money(int money){
            this.money = money;
            return this;
        }
        // 마지막으로 build()메소드를 통해 우리에게 필요한 객체를 얻는다. 
        User build(){
            return new User(this);
        }
    }
    
    }

    public class Program {
    public static void main(String[] args) {
        //=============== 객체 생성===============//
        User.Builder builder = new User.Builder("Tom",42);
        builder.address("Suwon");
        builder.level(42);
        builder.money(1000);
    
        User user1 =builder.build();
        //=====================================//
    
    
        // 메소드 체인 호출 - 자기 자신의 참조를 반환하면 된다. =========//
        User user2 = new User.Builder("Kim",27)
                .address("Gimpo")
                .level(27)
                .money(2000)
                .build();
        // ==================================================//
    }
    }

```
