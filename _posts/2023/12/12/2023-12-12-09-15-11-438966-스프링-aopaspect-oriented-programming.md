---
layout: post
title: "[java] 스프링 AOP(Aspect-Oriented Programming)"
description: " "
date: 2023-12-12
tags: [java]
comments: true
share: true
---

스프링 AOP는 관점 지향 프로그래밍을 지원하는 스프링 프레임워크의 핵심 기능 중 하나입니다. AOP는 애플리케이션에서 관심사를 분리하여 모듈화할 수 있는 기술을 말합니다. 이러한 모듈화된 관심사들을 **Aspect(관점)**이라고 하며, 스프링 AOP는 이러한 Aspects를 쉽게 정의하고 적용할 수 있게 해줍니다.

## AOP의 주요 개념

### Advice
Advice는 AOP가 동작하는 시점을 나타내며, **Before, After, Around** 등의 시간에 삽입되는 코드를 말합니다.

### Pointcut
Pointcut은 Advice가 실행될 지점을 정의하는데 사용됩니다. 어떤 메소드 호출, 필드 변경, 특정 시점 등을 나타내는데 사용됩니다.

### Join point
Join point는 애플리케이션 실행 중에 발생하는 특정 시점을 가리킵니다. Advice가 적용될 수 있는 위치로 생각할 수 있습니다.

### Aspect
Aspect는 여러 객체에 영향을 미치는 Advice, Pointcut, Join point의 조합을 가지고 있는 모듈화된 단위입니다.

### Weaving
Weaving은 Aspect를 타겟 코드에 삽입하는 과정을 말합니다. 스프링 AOP는 컴파일 타임, 클래스 로딩 타임, 런타임 중에 적용될 수 있습니다.

## AOP의 장점

스프링 AOP를 사용하면 다음과 같은 장점을 얻을 수 있습니다:
- **관점 지향** - 비즈니스 로직과는 상관없는 부가 기능(로깅, 트랜잭션 처리 등)을 모듈화하여 구현할 수 있습니다.
- **재사용성** - 여러 객체에 걸쳐 적용되는 공통 로직을 한 곳에 모듈화하여 중복을 줄일 수 있습니다.

스프링 AOP는 강력하면서도 유연한 기능을 제공하여 애플리케이션의 유지보수성을 높이고, 코드의 재사용성을 증가시킬 수 있습니다.

참조:
- [스프링 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#aop)
- 백기선, 『스프링 부트와 AWS로 혼자 구현하는 웹 서비스』, 프리렉