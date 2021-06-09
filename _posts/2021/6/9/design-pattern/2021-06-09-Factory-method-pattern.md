---
layout: post
title: "[디자인패턴] Factory method 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Factory method 패턴
-------------------

-	인스턴스를 생성하는 공장을 Template Method 패턴으로 구성한 것이 Factory Method 패턴이다.
-	자바에서는 new 연산자를 사용한 단순한 방법으로 객체의 인스턴스를 생성할 수 있다. 하지만 new 연산자를 사용하여 객체를 생성하는 방법은 코드의 관리 및 갱신이 어렵다. Factory method 패턴으로 객체를 생성하는 작업을 하면 메소드로 객체를 생성하여 코드의 중복이 제거되고 나중에 관리 할 때도 한 군데만 신경을 쓰면 된다. 그리고 슈퍼클래스에 있는 클라이언트 코드와 서브 클래스에 있는 객체 생성 코드를 분리시킬 수 있다.

![Factory method 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzUG9oQm43RmJRRlk)

-	예제

![Factory method 패턴 예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzR3VrVGlwdlJoVms)

```java
public abstract class Factory {
    public final Product create(String owner) {
        Product p = createProduct(owner);
        registerProduct(p);
        return p;
    }
    protected abstract Product createProduct(String owner);
    protected abstract void registerProduct(Product product);
}

public abstract class Product {
    public abstract void use();
}

public class IDCard extends Product {
    private String owner;
    IDCard(String owner) {
        System.out.println(owner + "의 카드를 만듭니다.");
        this.owner = owner;
    }
    public void use() {
        System.out.println(owner + "의 카드를 만듭니다.");
    }
    public String getOwner() {
        return owner;
    }
}

public class IDCardFactory extends Factory {
    private Vector owners = new Vector();
    protected Product createProduct(String owner) {
        return new IDCard(owner);
    }
    protected void registerProduct(Product product) {
        owners.add(((IDCard)product).getOwner());
    }
    public Vector getOwners() {
        return owners;
    }
}
```
