---
layout: post
title: "[java] 스프링 DI(Dependency Injection)"
description: " "
date: 2023-12-12
tags: [java]
comments: true
share: true
---

스프링 프레임워크는 의존성 주입(Dependency Injection, DI)이라는 개념을 통해 객체 간의 의존 관계를 효과적으로 관리하는 기능을 제공합니다. 

의존성 주입은 객체 간의 결합도를 낮추고 유연성과 확장성을 높여줍니다. 

의존성 주입을 사용하면 객체가 직접 생성하는 것이 아니라 외부에서 필요한 의존 객체를 전달받게 됩니다. 

이를 통해 객체 간의 결합을 낮추고, 테스트 용이성과 유지보수성을 높일 수 있습니다.

## 스프링 DI의 장점
- 코드의 재사용성이 높아짐
- 유연성이 향상되며 객체의 교체가 용이해짐
- 테스트가 용이해지고 유지보수가 쉬워짐

## 스프링 DI의 구현 방법
### 1. Setter 주입
Setter 메소드를 통해 의존 객체를 설정하는 방식
```java
public class Car {
    private Engine engine;

    public void setEngine(Engine engine) {
        this.engine = engine;
    }
}
```

### 2. 생성자 주입
생성자를 통해 의존 객체를 전달하는 방식
```java
public class Car {
    private Engine engine;

    public Car(Engine engine) {
        this.engine = engine;
    }
}
```

### 3. 필드 주입
의존 객체를 클래스의 필드로 직접 설정하는 방식
```java
public class Car {
    @Autowired
    private Engine engine;
}
```

## 스프링 DI를 사용할 때 고려할 점
스프링 DI를 사용하면서 주의할 점은 의존성 주입이 실제 필요한 곳에만 사용되도록 하는 것입니다. 모든 클래스에 대해 의존성 주입을 적용할 필요는 없고, 주로 변경이 필요한 부분이나 테스트가 필요한 부분에만 적용하는 것이 좋습니다.

의존성 주입의 잘못된 사용은 오히려 코드를 복잡하게 만들 수 있으므로 신중하게 사용해야 합니다.

## 결론
의존성 주입은 객체 지향 프로그래밍에서 중요한 개념 중 하나이며, 스프링 프레임워크에서는 이를 효과적으로 활용할 수 있도록 DI 기능을 제공합니다. 올바른 DI 사용은 유지보수가 용이한 안정적인 애플리케이션을 개발하는 데 도움을 줄 것입니다.

_참고 자료:_
- [Spring Framework Documentation](https://spring.io/projects/spring-framework)
- [Baeldung - Spring Dependency Injection](https://www.baeldung.com/spring-dependency-injection)