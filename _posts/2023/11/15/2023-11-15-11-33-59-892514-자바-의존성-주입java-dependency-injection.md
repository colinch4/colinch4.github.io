---
layout: post
title: "[java] 자바 의존성 주입(Java dependency injection)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

자바 애플리케이션을 개발하다 보면 클래스들 사이에 종속성이 발생합니다. 이러한 종속성을 관리하고 유연한 코드를 작성하기 위해 자바 의존성 주입(Dependency Injection)이라는 개념이 사용됩니다. 

의존성 주입은 코드의 결합도를 낮추고 재사용성과 테스트 용이성을 높이는데 도움을 줍니다. 

## 의존성 주입의 개념

의존성 주입은 객체 간의 의존성을 코드 내에서 약하게 만들기 위해 사용되는 디자인 패턴입니다. 이를 통해 객체가 직접 종속하는 객체를 찾지 않고도 필요한 종속성을 전달받아 사용할 수 있습니다.

종속성 주입은 주로 생성자, 필드 또는 메서드를 통해 이루어집니다. 이 때 의존성 주입을 사용하면 클래스의 인스턴스를 생성하고 사용하는 코드와 의존성을 제공하는 코드를 분리할 수 있으며, 인터페이스를 이용하여 의존성을 주입할 수 있습니다.

## 의존성 주입 방법

1. 생성자 주입(Constructor Injection) : 클래스의 생성자를 통해 의존성을 주입하는 방법입니다. 보통 클래스의 필수적인 종속성이 있을 때 사용됩니다.

```java
public class MyClass {
    private Dependency dependency;

    public MyClass(Dependency dependency) {
        this.dependency = dependency;
    }
}
```

2. 필드 주입(Field Injection) : 클래스의 필드를 통해 의존성을 주입하는 방법입니다.

```java
public class MyClass {
    @Inject
    private Dependency dependency;
}
```

3. 메서드 주입(Method Injection) : 특정 메서드를 통해 의존성을 주입하는 방법입니다. 보통 클래스의 일부 기능을 동적으로 변경해야 할 때 사용됩니다.

```java
public class MyClass {
    private Dependency dependency;

    @Inject
    public void setDependency(Dependency dependency) {
        this.dependency = dependency;
    }
}
```

## 의존성 주입 프레임워크

의존성 주입을 구현하려면 일반적으로 의존성 주입 프레임워크를 사용합니다. 자바에서 가장 널리 사용되는 의존성 주입 프레임워크는 **Spring Framework**입니다. Spring은 생성자, 필드, 메서드 주입을 모두 지원하며, 강력한 기능과 다양한 기능을 제공합니다.

그 외에도 **Google Guice**, **Java EE**, **CDI** 등의 프레임워크도 의존성 주입을 지원합니다. 선택한 프레임워크에 따라 각각의 방법과 규칙을 따라야 합니다.

## 결론

자바 의존성 주입은 객체 간의 결합도를 낮추고 유연한 코드를 작성할 수 있는 중요한 개념입니다. 의존성 주입을 통해 코드의 품질과 유지보수성을 향상시킬 수 있습니다. 이를 위해 의존성을 주입하는 방법을 이해하고 의존성 주입 프레임워크를 활용하는 것이 좋습니다.

## 참고 문서

- [Spring Framework](https://spring.io/)
- [Google Guice](https://github.com/google/guice)
- [Java EE](https://javaee.github.io/)
- [CDI](https://www.oracle.com/java/technologies/java-ee-cdi.html)