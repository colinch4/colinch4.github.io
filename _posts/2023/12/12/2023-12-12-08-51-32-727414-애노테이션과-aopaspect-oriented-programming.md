---
layout: post
title: "[java] 애노테이션과 AOP(Aspect-Oriented Programming)"
description: " "
date: 2023-12-12
tags: [java]
comments: true
share: true
---

애노테이션은 자바 5부터 도입된 기능으로, **소스 코드에 메타데이터**를 추가할 수 있게 해줍니다. 메타데이터를 추가함으로써 코드를 분석하고 처리하는 일을 더 쉽게 만들어주며, AOP(Aspect-Oriented Programming)와 함께 사용되어 프로그램의 성능을 향상시킬 수 있습니다.

## 애노테이션(Annotation)

애노테이션은 `@`로 시작하여 컴파일러, 런타임 시스템 또는 개발 도구에게 특정 작업을 수행하도록 지시할 수 있습니다. 

```java
@Deprecated
public class DeprecatedClass {
    // DeprecatedClass 내용
}
```

위의 예시에서 `@Deprecated` 애노테이션은 해당 클래스가 더 이상 사용되지 않음을 표시하고, 해당 클래스를 사용하는 코드에게 경고 메시지를 출력합니다.

## AOP(Aspect-Oriented Programming)

AOP는 애노테이션과 함께 사용되어, **관심사(Concern)**를 모듈화하여 재사용 가능한 모듈로 분리시키고, 중복되는 코드를 줄일 수 있는 프로그래밍 기법입니다.

```java
@Aspect
public class LoggingAspect {
 
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        // 메서드 실행 전 로깅
    }
 
    @After("execution(* com.example.service.*.*(..))")
    public void logAfter(JoinPoint joinPoint) {
        // 메서드 실행 후 로깅
    }
}
```

위의 예시에서 `@Aspect` 애노테이션은 해당 클래스가 어드바이스(Advice)와 포인트컷(Pointcut)을 포함한다는 것을 나타내며, 메서드 실행 전후에 로깅을 수행합니다.

AOP와 애노테이션을 함께 사용하면, **관심사를 분리하여 코드를 간결하게 유지**할 수 있으며, 코드의 **가독성을 향상**시킬 수 있습니다.

애노테이션과 AOP를 이용하여 코드의 모듈화와 재사용성을 높이고, 중복 코드를 줄이며, 프로그램의 유지보수성을 향상시킬 수 있습니다.

## 결론

애노테이션과 AOP는 **자바 프로그래밍을 보다 효율적으로 만드는 중요한 기술**이며, 프로그램의 관심사를 분리하여 코드의 재사용성과 유지보수성을 향상시킬 수 있습니다. AOP를 활용하여 **선언적으로 관심사를 분리**할 수 있으며, 애노테이션을 통해 **메타데이터를 사용하여 프로그램의 기능을 향상**시킬 수 있습니다.

## 참고 자료

1. [자바 애노테이션(Annotation) 개념과 사용법](https://wikidocs.net/218)

2. [Spring AOP with Annotations](https://www.baeldung.com/spring-aop-annotation)