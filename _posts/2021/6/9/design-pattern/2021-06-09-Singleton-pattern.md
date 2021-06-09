---
layout: post
title: "[디자인패턴] Singleton 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Singleton 패턴
--------------

-	지장한 클래스의 인스턴스가 '절대로' 1개밖에 존재하지 않는 것을 '보증'하고 싶을 때, 인스턴스가 1개 밖에 존재하지 않는 것을 프로그램상에 표현하고 싶을 때 인스턴스가 한개밖에 존재하지 않는 것을 보증하는 패턴이 `Singleton 패턴`이다.
-	복수의 인스턴스가 존재하면 인스턴스들이 서로 영향을 미치고, 뜻하지 않은 버그가 발생할 가능성이 있다. 그러나 인스턴스가 1개밖에 없다라는 보증이 있으면 그 전제조건 아래에서 프로그래밍 할 수 있다.

![Singleton 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzR3JKQ0pab0pyV0E)

-	Singleton은 static 필드(클래스 변수)로서 Singleton 클래스의 인스턴스에서 초기화 된다.
-	Singleton 클래스의 생성자는 private로 되어 있다.
-	Singleton 패턴은 프로그래머가 실수를 해도 1개만 생성되도록 보증하는 패턴이다.

-	Singleton 패턴의 등장인물

	-	Singleton 패턴에는 Singleton의 역할만 존재한다. Singleton 역할은 유일한 인스턴스를 얻기 위해 static 메소드를 가지고 있다. 이 메소드는 언제나 동일한 인스턴스를 반환한다.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Start.");
        Singleton obj1 = Singleton.getInstance();
        Singleton obj2 = Singleton.getInstance();
        if (obj1 == obj2) {
            System.out.println("obj1과 obj2는 같은 인스턴스입니다.");
        } else {
            System.out.println("obj1과 obj2는 같은 인스턴스입니다.");
        }
        System.out.println("End.");
    }
}

public class Singleton {
    private static Singleton singleton = new Singleton();
    private Singleton() {                                 
        System.out.println("인스턴스를 생성했습니다.");
    }
    public static Singleton getInstance() {
        return singleton;
    }
}

```
