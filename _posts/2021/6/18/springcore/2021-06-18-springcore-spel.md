---
layout: post
title: "[springcore] SpEL (스프링 Expression Language)"
description: " "
date: 2021-06-18
tags: [springboot]
comments: true
share: true
---

## SpEL (스프링 Expression Language)
- 객체 그래프를 조회하고 조작하는 기능
- Unified EL과 비슷하지만, 메소드 호출을 지원하고, 문자열 템플릿을 제공함
- 스프링 3.0부터 지원

## SpEL 구성
- `ExpressionParser parser = new SpelExpressionParser()`
- `StandardEvaluationContext context = new StandardEvaluationContext(bean)`
- `Expression expression = parser.parseExpression("SpEL표현식")`
- `String value = expression.getvalue(context, String.class)`

## 문법
- #{표현식}
    ```java
    @Value("#{1 + 1}")
    int value;

    @Value("#{1 ea 1}")
    boolean boolValue;

    @Value("#{'hello ' + 'world'}")
    String hello;

    @Value("hello")
    String constantHello;

    // Sample.java를 빈으로 등록하면 객체안의 프로퍼티도 접근 가능
    @Value("#{sample.data}")
    int sampleData;
    ```
- ${프로퍼티}
    ```java
    // applciation.properties에 등록힌 my.value값
    @Value("${my.value}")
    int myValue;
    ```
- 표현식은 프로퍼티를 가질 수 있지만 반대는 안됨
    ```java
    @Value(#{${my.value} + 1})
    int value;
    ```

## 사용처
- @Value
- @ConditionalOnExpression
- 스프링 시큐리티 
    - 메소드 시큐리티, @PreAuthorize, @PostAuthorize, @PreFilter, @PostFilter
    - XML 인터셉터 URL 설정
- 스프링 데이터 (@Query)
- Thymeleaf
