---
layout: post
title: "[java] Spring AOP(Aspect Oriented Programming)에 대한 이해"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

Spring AOP는 Spring 프레임워크에서 제공하는 핵심 기능 중 하나로, 관점 지향 프로그래밍(Aspect Oriented Programming)을 지원합니다. 관점 지향 프로그래밍은 어플리케이션에서 공통적으로 발생하는 부가적인 기능(관심사)을 분리하여 모듈화하는 프로그래밍 기법입니다.

## AOP의 개념

AOP는 기존의 객체 지향 프로그래밍(OOP)을 보완하기 위해 도입된 개념으로, OOP의 한계를 극복하고 코드 재사용성과 유지보수성을 향상시킵니다.

OOP는 주로 객체들의 상속 관계를 이용하여 기능을 분리합니다. 하지만 어플리케이션의 규모가 커질 경우, 여러 객체들 사이에 공통으로 발생하는 기능들이 중복되는 현상이 발생할 수 있습니다.

예를 들어, 로깅, 트랜잭션 관리, 보안 등의 기능은 어플리케이션의 여러 모듈에서 공통적으로 필요한 요소입니다.

## Spring AOP의 동작 방식

Spring AOP는 프록시를 통해 AOP 기능을 구현합니다. 원본 객체의 메서드 호출 시, 프록시 객체를 거쳐 공통 기능이 실행됩니다. 

Spring AOP는 주로 메서드 실행 전 후, 메서드 에러 발생 시, 메서드 호출 전 후 등의 시점에서 실행되는 어드바이스(Advice)를 사용하여 공통 기능을 구현합니다. 어드바이스는 별도의 클래스로 작성되며, 특정 시점에서 실행되는 로직을 구현합니다.

또한, 어드바이스가 적용되는 대상을 결정하는 방법으로 포인트컷(Pointcut)이라는 개념을 사용합니다. 포인트컷은 특정 패키지, 클래스, 메서드 등에 대한 필터링을 수행하여 어드바이스가 적용되는 대상을 선정합니다.

Spring AOP는 JDK Dynamic Proxy와 CGLIB Proxy를 사용하여 프록시 객체를 생성합니다. 인터페이스를 구현한 클래스의 경우에는 JDK Dynamic Proxy를 사용하고, 인터페이스를 구현하지 않는 클래스의 경우에는 CGLIB Proxy를 사용합니다.

## Spring AOP의 예제 코드

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

@Aspect
public class LoggingAspect {

  @Before("execution(* com.example.service.*.*(..))")
  public void beforeAdvice() {
    System.out.println("메서드 실행 전 로그 출력");
  }

}
```

위의 코드는 Spring AOP를 사용하여 메서드 실행 전에 로그를 출력하는 예제입니다. `@Aspect` 어노테이션을 사용하여 해당 클래스가 어드바이스를 포함하고 있는 클래스임을 표시하고, `@Before` 어노테이션을 통해 어드바이스를 정의합니다. `execution(* com.example.service.*.*(..))`는 포인트컷 표현식으로, `com.example.service` 패키지에 속한 모든 클래스의 모든 메서드에 어드바이스를 적용한다는 의미입니다.

## 결론

Spring AOP를 이용하면 어플리케이션에서 발생하는 공통 기능을 효율적으로 분리하여 관리할 수 있습니다. 이를 통해 코드의 재사용성과 유지보수성을 향상시킬 수 있으며, OOP의 한계를 극복할 수 있습니다.

더 자세한 내용은 [Spring AOP 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#aop)를 참고할 수 있습니다.