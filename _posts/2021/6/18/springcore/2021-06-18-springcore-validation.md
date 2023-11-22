---
layout: post
title: "[springcore] SpEL (스프링 Expression Language)"
description: " "
date: 2021-06-18
tags: [spring]
comments: true
share: true
---

## Validation 추상화

- 애플리케이션에서 사용하는 객체 검증용 인터페이스
- 특징
    - 어떠한 계증과도 관계가 없다 -> 모든 계층(웹, 서비스, 데이터)에서 사용해도 좋음
    - 구현체 중 하나로 JSR-303(Bean Validation 1.0)과 JSR-349(Bean Validation 1.1)을 지원(LocalValidatorFactoryBean)
    - DataBinder에 들어가 바인딩할 때 같이 사용되기도 함

- 인터페이스
    - boolean supports(Class clazz): 어떤 타입의 객체를 검증할 때 사용할 것인지 결정
    - void validate(Object obj, Errors e): 실제 검증 로직을 여기서 구현
        - 구현시 ValidationUtils 사용하며 편리

- 스프링 부트 2.0.5이상일때
    - LocalValidatorFactoryBean 빈으로 자동 등록
    - JSR-380(Bean Validation 2.0.1) 구현체로 hibernate-validator 사용
    - https://beanvalidation.org

