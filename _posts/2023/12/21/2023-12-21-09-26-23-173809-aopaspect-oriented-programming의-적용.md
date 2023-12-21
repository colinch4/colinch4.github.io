---
layout: post
title: "[스프링] AOP(Aspect-Oriented Programming)의 적용"
description: " "
date: 2023-12-21
tags: [스프링]
comments: true
share: true
---

스프링 프레임워크는 AOP(Aspect-Oriented Programming)를 지원하여 애플리케이션의 모든 계층에서 **관심사**를 분리할 수 있게 해줍니다. 이로써 코드의 재사용성과 유지보수성을 향상시킬 수 있으며, **로깅**, **트랜잭션 관리**, **보안**과 같은 **부가적인 기능**을 모듈화하여 적용할 수 있습니다.

## AOP의 주요 용어

**1. Aspect(관점)** : 관심사를 구체화한 모듈로, 애플리케이션의 여러 지점에서 적용될 수 있는 **기능**을 정의합니다.

**2. Join Point(결합점)** : Aspect가 적용될 수 있는 코드의 지점을 의미합니다. 메소드 호출, 예외 발생, 변수 수정 등이 결합점에 해당합니다.

**3. Advice(조언)** : 결합점에 삽입되어 실행될 수 있는 코드 블록입니다. Before, After, Around 등의 종류가 있습니다.

**4. Pointcut(포인트컷)** : 실제 Advice가 실행될 **결합점의 패턴**입니다.

**5. Weaving(엮기)** : Aspect를 지정된 결합점에 삽입하여 **프록시 객체**를 생성하는 과정입니다. 스프링의 AOP는 컴파일, 클래스 로딩, 런타임 중의 엮기 과정 중에서 런타임 중에 엮기를 지원합니다.

## AOP 구현 방법

### 1. XML 설정을 통한 AOP 설정

```xml
<aop:config>
    <aop:aspect ref="loggingAspect">
        <aop:pointcut id="serviceExecution"
            expression="execution(* com.example.service.*.*(..))" />
        <aop:before pointcut-ref="serviceExecution" method="beforeMethod" />
        <aop:after pointcut-ref="serviceExecution" method="afterMethod" />
    </aop:aspect>
</aop:config>
```

### 2. @Aspect 어노테이션을 통한 AOP 설정 
```java
@Aspect
@Component
public class LoggingAspect {
    @Before("execution(* com.example.service.*.*(..))")
    public void beforeMethod(JoinPoint joinPoint) {
        // 메서드 실행 전에 실행될 동작 정의
    }

    @After("execution(* com.example.service.*.*(..))")
    public void afterMethod(JoinPoint joinPoint) {
        // 메서드 실행 후에 실행될 동작 정의
    }
}
```

이처럼 스프링은 AOP를 위한 다양한 방법을 제공하므로, 기능에 따라 XML 설정 또는 어노테이션 기반의 구현 방식을 선택할 수 있습니다.

AOP를 통해 관심사를 분리하면 코딩의 효율성과 유지보수성을 증가시킬 수 있으며, 애플리케이션의 핵심 비즈니스 로직과 부가적인 기능을 분리할 수 있습니다.

자세한 내용은 [공식 문서](https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/core.html#aop)를 참고하세요.