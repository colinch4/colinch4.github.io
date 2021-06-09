---
layout: post
title: "[디자인패턴] Adapter 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Adapter 패턴
------------

-	'이미 제공되어 있는 것'과 '필요한 것' 사이의 차이를 없애주는 디자인 패턴.
-	Adapter 패턴은 기존의 클래스를 개조해서 필요한 클래스를 만든다. 이 패턴으로 필요한 메소드를 발빠르게 만들 수 있다.
-	Adapter 패턴은 기존의 클래스(Target)를 전혀 수정하지 않고 이미 존재하는 Adaptee클래스가 있다면 사용하고 없다면 Adaptee클래스를 새로 만들어 목적한 인터페이스(API)에 맞춘다.

-	Adapter 패턴의 등장인물

	-	Target(대상)의 역할
		-	지금 필요한 메소드를 결정한다.
	-	Client(의뢰자)역할
		-	Target 역할의 메소드를 사용해서 일을 한다.
	-	Adaptee(개조되는 쪽)의 역할
		-	Adaptee는 이미 준비되어 있는 메소드를 가지고 있는 역할이다.
	-	Adapter의 역할
		-	Adapter 패턴의 주인공이다. Adaptee 역할의 메소드를 사용해서 어떻게든 Target 역할을 만족시키기 위한 것이 Adapter 패턴의 목적이며, Adapter 역할의 임무이다.

### Adapter 패턴 종류

#### 1. 상속을 사용한 Adapter 패턴

![상속을 사용한 Adapter 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzOEpsY0U2QWprWjg)

-	예제

![상속을 사용한 Adapter 패턴-1](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzTk51Q2cwTng3MzA)

```java
public class Main {
    public static void main(String[] args) {
        Print p = new PrintBanner("Hello");
        p.printWeak();
        p.printStrong();
    }
}

public interface Print {
    public abstract void printWeak();
    public abstract void printStrong();
}

public class PrintBanner extends Banner implements Print {
    public PrintBanner(String string) {
        super(string);
    }
    public void printWeak() {
        showWithParen();
    }
    public void printStrong() {
        showWithAster();
    }
}

public class Banner {
    private String string;
    public Banner(String string) {
        this.string = string;
    }
    public void showWithParen() {
        System.out.println("(" + string + ")");
    }
    public void showWithAster() {
        System.out.println("*" + string + "*");
    }
}

```

-	PrintBanner 클리스가 어댑터의 역할을 수행하고 준비된 Banner 클래스를 상속해서 메소드를 사용한다.
-	Print 인터페이스를 구현한다.

#### 2. 위임을 사용한 Adapter 패턴

![위임을 사용한 Adapter 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzRmJVZWZpX3daa0E)

-	예제

![위임을 사용한 Adapter 패턴-1](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzMVV3UDZOcHBkX1k)

```java
public abstract class Print {
    public abstract void printWeak();
    public abstract void printStrong();
}

public class PrintBanner extends Print {
    private Banner banner;
    public PrintBanner(String string) {
        this.banner = new Banner(string);
    }
    public void printWeak() {
        banner.showWithParen();
    }
    public void printStrong() {
        banner.showWithAster();
    }
}

public class Banner {
    private String string;
    public Banner(String string) {
        this.string = string;
    }
    public void showWithParen() {
        System.out.println("(" + string + ")");
    }
    public void showWithAster() {
        System.out.println("*" + string + "*");
    }
}
```

-	PrintBanner 클리스가 어댑터의 역할을 수행하고 Banner 클래스를 인스턴스로 가진다(포함관계다) 이 인스턴스는 어댑터의 생성자에서 생성된다.
