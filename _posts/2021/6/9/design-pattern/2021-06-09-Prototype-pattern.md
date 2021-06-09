---
layout: post
title: "[디자인패턴] Prototype 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Prototype 패턴
--------------

-	모범이 되는 인스턴스를 기초로 새로운 인스턴스를 만드는 패텅을 `Prototype 패턴`이라 한다.
-	Prototype 패턴 사용 이유
	-	종류가 너무 많아 클래스로 정리되지 않는 경우
	-	클래스로부터 인스턴스 생성이 어려운 경우
	-	framework와 생성할 인스턴스를 분리하고 싶은 경우
-	Prototype 패턴의 등장인물
	-	Prototype(원형)의 역할
	-	Prototype은 인스턴스를 복사하는 새로운 인스턴스를 만들기 위한 메소드를 결정한다.
	-	ConcretePrototype(구체적인 원형)의 역할
	-	ConcretePrototype은 인스턴스를 복사해서 새로운 인스턴스를 만드는 메소드를 실제로 구현한다.
	-	Client(이용자)의 역할
	-	Client는 인스턴스를 복사하는 메소드를 이용해서 새로운 인스턴스를 만든다.

![Prototype 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzU2xVYXFjc3l3Ylk)

-	예제

![Prototype 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzR3hLbTZBVFZ1Z1U)

```java
public class Main {
    public static void main(String[] args) {
        // 준비
        Manager manager = new Manager();
        UnderlinePen upen = new UnderlinePen('~');
        MessageBox mbox = new MessageBox('*');
        MessageBox sbox = new MessageBox('/');
        manager.register("strong message", upen);
        manager.register("warning box", mbox);
        manager.register("slash box", sbox);

        // 생성
        Product p1 = manager.create("strong message");
        p1.use("Hello, world.");
        Product p2 = manager.create("warning box");
        p2.use("Hello, world.");
        Product p3 = manager.create("slash box");
        p3.use("Hello, world.");
    }
}

public class Manager {
    private Hashtable showcase = new Hashtable();
    public void register(String name, Product proto) {
        showcase.put(name, proto);
    }
    public Product create(String protoname) {
        Product p = (Product)showcase.get(protoname);
        return p.createClone();
    }
}

public interface Product extends Cloneable {
    public abstract void use(String s);
    public abstract Product createClone();
}

public class MessageBox implements Product {
    private char decochar;
    public MessageBox(char decochar) {
        this.decochar = decochar;
    }
    public void use(String s) {
        int length = s.getBytes().length;
        for (int i = 0; i < length + 4; i++) {
            System.out.print(decochar);
        }
        System.out.println("");
        System.out.println(decochar + " "  + s + " " + decochar);
        for (int i = 0; i < length + 4; i++) {
            System.out.print(decochar);
        }
        System.out.println("");
    }
    public Product createClone() {
        Product p = null;
        try {
            p = (Product)clone();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
        return p;
    }
}

public class UnderlinePen implements Product {
    private char ulchar;
    public UnderlinePen(char ulchar) {
        this.ulchar = ulchar;
    }
    public void use(String s) {
        int length = s.getBytes().length;
        System.out.println("\""  + s + "\"");
        System.out.print(" ");
        for (int i = 0; i < length; i++) {
            System.out.print(ulchar);
        }
        System.out.println("");
    }
    public Product createClone() {
        Product p = null;
        try {
            p = (Product)clone();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
        return p;
    }
}
```

-	Product 인터페이스나 Manager 클래스의 소스에 MessageBox 클래스나 UnderlinePen 클래스의 클래스 이름이 전혀 나오지 않는다. 클래스 이름이 나오지 않는 다는 것은 Product와 Manager는 그들의 클래스와 독립적으로 수정할 수 있다는 것을 의미한다. **소스 안에 클래스의 이름을 쓰면 그 클래스와 밀접한 관계가 생긴다. 소스 내부에 이용할 클래스의 이름을 쓰여있으면 그 클래스와 분리해서 재이용할 수 없게 된다.**
