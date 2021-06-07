---
layout: post
title: "[java] Interface 인터페이스"
description: " "
date: 2021-06-07
tags: [java]
comments: true
share: true
---

# 🙍‍♀️ Interface 인터페이스

> - 객체의 사용방법을 정의한 타입으로 개발코드와 객체가 서로 통신하는 접점
> - 개발코드가 인터페이스의 매소드를 호출하면 인터페이스는 객체의 매소드를 호출함
> - **따라서,** 개발 코드는 객체의 내부 구조를 알 필요가 없고 인터페이스의 매소드만으로 코드 변경없이 내용과 리턴값을 다양하게 받을 수 있음

<br >

### 인터페이스 선언

```java
public interface InterfaceName{ }
```

<br>

### 추상 매소드 선언

> - 인터페이스를 통해 호출된 매소드는 객체에서 실행되기에 인터페이스 내에서 실행블록은 따로 필요 없음 ==> **추상매소드로 선언**
> - 인터페이스에서 선언된 추상 매소드는 public abstract를 defualt로 갖기 때문에 생략 가능

<br>

[예시]

```java
public interface Pet {
	 String getName() ;
	 void setName(String name) ;
	 void play ();
}
```

<br>
<br >

### 인터페이스 구현 클래스

> - 개발 코드가 인터페이스 매소드를 호출하면 인터페이스는 객체의 매소드를 호출
> - 따라서 객체는 인터페이스의 매소드와 같은 매소드를 갖고 있어야함

[선언 방법]

```java
public class Cat extends Animal implements Pet{
	String name;


	public Cat(String name) {
		super(4);
		this.name = name;

	}

    //인터페이스의 매소드 실제 구현
	public void play() {
		System.out.println( name + "is playing with a puppy");
	}

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}



}
```

<br >

### 인터페이스를 활용한 출력 class

> 같은 매소드지만 각각의 인스턴스에 따라서 매소드 결과가 다르게 리턴됨

```java
public class TestAnimals {
	public static void main(String[] args) {

		Fish d = new Fish();
		Cat c = new Cat("Fluffy");
		Animal a = new Fish();
		Animal e = new Spider();
		Pet p = new Cat();

		d.eat();
		d.walk();
		d.play();

        //  A fish eats plankton
        // Fish cannot walk cause they don't have legs
        // A Fish plays with Sponge Bob

	System.out.println(" ");
		c.walk();
		c.eat();

        // the number of legs is  4
        // Fluffy loves chewrr

	System.out.println(" ");

		((Cat) p).eat();
		((Cat) p).play();
		((Cat) p).walk();

        //interface Pet 을 Cat으로 형변환하여 method 호출

        // Aeyong loves chewrr
        // Aeyongis playing with a puppy
        // the number of legs is  4

	}
}
```
