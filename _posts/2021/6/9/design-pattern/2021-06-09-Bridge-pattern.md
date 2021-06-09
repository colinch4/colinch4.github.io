---
layout: post
title: "[디자인패턴] Bridge 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Bridge 패턴
-----------

-	`기능의 클래스 계층`과 `구현의 클래스 계층` 사이에 다리를 놓는 패턴.
	-	`기능의 클래스 계층` : 새로운 기능을 추가하고 싶은 경우 클래스 계층안에서 자신의 목적과 가까운 `클래스` 를 찾아내 그 `하위 클래스` 를 만들어, 목적한 기능을 추가한 새로운 클래스를 만든다는 것.
	-	`구현의 클래스 계층` : 새로운 구현을 만들기 위해서는 AbstractClass의 하위 클래스를 만들어 추상 메소드를 구현한 것.
-	Bridge 패턴의 특징은 `기능의 클래스 계층`과 `구현의 클래스 계층`을 분리하는 것이다. 두 개의 클래스 계층을 분리해 두면 각각의 클래스 계층을 독립적으로 확장할 수 있다. 기능을 추가하고 싶으면 기능의 클래스 계층에 클래스를 추가한다. 이때 구현의 클래스 계층은 전혀 수정할 필요가 없다. 새로 추가한 기능은 '모든구현'에서 이용할 수 있다.
-	어떤 프로그램이 운영체제에 의존하는 부분이 있어서 윈도우판, 맥킨토시판, 유닉스판으로 분리된다고 가정할 때 운영체제에 의존하는 부분을 Bridge 패턴의 '구현의 클래스 계층'으로 표현한다. 즉, 각 운영체제 공통의 인터페이스(API)를 정해서 Implementor 역할로 하고 ConcreteImplementor 역할로 윈도우판, 맥킨토시판, 유닉스판의 세 개의 클래스를 만든다. 이렇게 하면 '기능의 클래스 계층' 쪽에 아무리 기능을 추가한다해도 세 개의 운영체제에 동시에 대응할수있다.

> 상속은 견고한 연결이고 위임은 느슨한 연결이다. 필요에 따라서 클래스 간의 관계를 척척 바꾸고 싶을 때 '상속'이 아니라 '위임을' 사용한다.

-	Bridge 패턴의 등장인물

	-	Abstraction(추상화)의 역할
		-	'기능의 클래스 계층'의 최상위 클래스이다. Implementor 역할의 메소드를 사용해서 기본적인 기능만이 기술되어 있는 클래스이다. 이 인스턴스는 Implementor 역할을 가지고 있다. 예제 프로그램에서는 Display 클래스가 이 역할을 한다.
	-	RefinedAbstraction(개선된 추상화)의 역할
		-	Abstraction 역할에 대해 기능을 추가한 역할이다. 예제 프로그램에서는 CountDisplay 클래스가 이 역할을 한다.
	-	Implementor(구현자)의 역할
		-	'구현의 클래스 계층'의 최상위 클래스이다. Abstraction 역할의 인터페이스(API)를 구현하기 위한 메서드를 규정하는 역할이다. 예제 프로그램에서는 DisplayImpl 클래스가 이 역할을 한다.
	-	Concrete Implementor(구체적인 구현자)의 역할
		-	Implementor 역할의 인터페이스(API)를 구체적으로 구현하는 역할이다. 예제 프로그램에서는 StringDisplayImpl 클래스가 이 역할을 한다.

-	왼쪽 두 개가 기능의 클래스 계층이고 오른쪽의 두 개가 구현의 클래스 계층이다. 두 계층을 impl 필드가 중개한다.

![Bridge 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzUE0xdlV3NmR2QzQ)

-	예제

![Bridge 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzbk5nWTV3OXNjaTg)

```java
public class Main {
    public static void main(String[] args) {
        Display d1 = new Display(new StringDisplayImpl("Hello, Korea."));
        Display d2 = new CountDisplay(new StringDisplayImpl("Hello, World."));
        CountDisplay d3 = new CountDisplay(new StringDisplayImpl("Hello, Universe."));
        d1.display();
        d2.display();
        d3.display();
        d3.multiDisplay(5);
    }
}

public class Display {
    private DisplayImpl impl;
    public Display(DisplayImpl impl) {
        this.impl = impl;
    }
    public void open() {
        impl.rawOpen();
    }
    public void print() {
        impl.rawPrint();
    }
    public void close() {
        impl.rawClose();
    }
    public final void display() {
        open();
        print();                    
        close();
    }
}

public class CountDisplay extends Display {
    public CountDisplay(DisplayImpl impl) {
        super(impl);
    }
    public void multiDisplay(int times) {       // times번을 반복해서 표시한다.
        open();
        for (int i = 0; i < times; i++) {
            print();
        }
        close();
    }
}

public abstract class DisplayImpl {
    public abstract void rawOpen();
    public abstract void rawPrint();
    public abstract void rawClose();
}

public class StringDisplayImpl extends DisplayImpl {
    private String string;                              // 표시해야할 문자열
    private int width;                                  // 바이트 단위로 계산한 문자열의 "길이"
    public StringDisplayImpl(String string) {           // 생성자에서 넘어온 문자열 string를
        this.string = string;                               // 필드에 기억해 둔다.
        this.width = string.getBytes().length;              // 그리고 바이트 단위의 길이도 필드에 기억해두고 나중에 사용한다.
    }
    public void rawOpen() {
        printLine();
    }
    public void rawPrint() {
        System.out.println("|" + string + "|");         // 앞뒤에 "|"를 붙여서 표시
    }
    public void rawClose() {
        printLine();
    }
    private void printLine() {
        System.out.print("+");                          // 틀의 모퉁이를 표현하는 "+"마크를 표시한다.
        for (int i = 0; i < width; i++) {               // width개의 "-"를 표시해서
            System.out.print("-");                      // 틀의 선으로 이용한다.
        }
        System.out.println("+");                        // 틀의 모퉁이를 표현하는 "+"마크를 표시한다.
    }
}
```
