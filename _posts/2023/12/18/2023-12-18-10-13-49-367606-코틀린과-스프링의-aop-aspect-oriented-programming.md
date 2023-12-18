---
layout: post
title: "[kotlin] 코틀린과 스프링의 AOP (Aspect-Oriented Programming)"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

## 개요
스프링 프레임워크는 AOP (Aspect-Oriented Programming)를 지원하여 여러 모듈을 개발하고 유지보수하기 쉽게 해줍니다. AOP는 프로그램 코드에 흩어진 관심사를 모듈화할 수 있는 개념을 지원하며, 코틀린 언어도 AOP를 적용하여 관리하기 쉬운 코드를 작성할 수 있습니다.

## AOP의 주요 개념
AOP는 관심사를 모듈화하기 위한 여러가지 개념을 포함하고 있습니다.

### Advice (충고)
Advice는 특정한 JointPoint에서 실행되는 코드 블록을 지칭합니다. `@Before`, `@After`, `@Around`과 같은 어노테이션을 사용하여 언제 Advice를 실행할지를 정의할 수 있습니다.

### JoinPoint (결합점)
JoinPoint는 Advice가 적용될 수 있는 특정한 지점을 가리킵니다. 메서드 호출, 필드 접근, 객체 생성 등이 JoinPoint의 예시입니다.

### Pointcut (적절한 지점)
Pointcut은 실제로 Advice가 실행될 JoinPoint를 선택할 수 있는 표현식입니다. 스프링에서는 AspectJ 표현식을 사용하여 Pointcut을 정의할 수 있습니다.

### Aspect (관심)
Aspect는 Advice와 Pointcut을 결합하여 실제로 적용되는 기능을 나타냅니다. 여러 개의 Advice와 Pointcut을 모아 한 가지 기능으로 정의할 수 있습니다.

### Target Object (대상 객체)
Target Object는 AOP가 적용되는 실제 객체를 말합니다.

## 스프링에서 AOP 사용하기
스프링에서 AOP를 사용하기 위해서는 다음 단계를 따릅니다.

1. Aspect 클래스 작성
2. Pointcut 정의
3. Advice 작성
4. AOP 설정

```kotlin
@Aspect
@Component
class LoggingAspect {
    @Pointcut("execution(* com.example.service.*.*(..))")
    fun serviceMethods() {}

    @Before("serviceMethods()")
    fun beforeServiceMethods(execution: JoinPoint) {
        // 메서드 호출 전 로깅
    }
}
```

위 예시에서 `@Aspect` 어노테이션을 사용하여 Aspect 클래스를 정의하고, `@Pointcut` 어노테이션을 사용하여 Pointcut을 정의합니다. `@Before` 어노테이션을 사용하여 `beforeServiceMethods` 메서드가 `serviceMethods` Pointcut에서 실행될 수 있도록 합니다.

## 결론
코틀린과 스프링에서 AOP를 적용하면 코드를 모듈화하고 유지보수하기 쉬운 구조로 개발할 수 있습니다. AOP는 코드의 재사용성을 증가시키고 중복을 줄여주며, 시스템 전체의 가독성을 향상시키는데 도움을 줍니다.

## References
- [Spring Framework Documentation](https://spring.io/projects/spring-framework)
- [Aspect Oriented Programming with Spring](https://www.baeldung.com/spring-aop)