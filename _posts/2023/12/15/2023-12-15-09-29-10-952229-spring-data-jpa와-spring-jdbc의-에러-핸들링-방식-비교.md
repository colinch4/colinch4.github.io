---
layout: post
title: "[java] Spring Data JPA와 Spring JDBC의 에러 핸들링 방식 비교"
description: " "
date: 2023-12-15
tags: [java]
comments: true
share: true
---

Spring Data JPA와 Spring JDBC는 둘 다 데이터베이스 접근을 위한 기술이지만, 에러 핸들링에 대한 접근 방식에는 차이가 있습니다. 이 포스트에서는 두 기술의 에러 핸들링 방식을 비교하고, 각각의 특징에 대해 살펴보겠습니다.

## 목차

- [Spring Data JPA의 에러 핸들링](#spring-data-jpa의-에러-핸들링)
- [Spring JDBC의 에러 핸들링](#spring-jdbc의-에러-핸들링)
- [결론](#결론)

## Spring Data JPA의 에러 핸들링

Spring Data JPA는 JPA(Java Persistence API)의 구현체로, **예외(Exception)**를 통해 에러를 핸들링합니다. JPA를 사용할 때 발생하는 대부분의 에러는 **javax.persistence.PersistenceException**을 상속한 예외들로 처리됩니다.

예를 들어, **EntityNotFoundException**은 데이터베이스에서 엔티티를 찾지 못했을 때 발생하는 예외입니다. 또한, **OptimisticLockException**은 머지 충돌(Optimistic Locking)이 발생했을 때 발생하는 예외입니다.

Spring Data JPA는 이러한 예외를 적절히 처리하여 **롤백** 등의 작업을 수행할 수 있도록 지원합니다. 또한, **@Repository** 애노테이션을 이용하여 에러를 기록하거나 제어할 수 있습니다.

## Spring JDBC의 에러 핸들링

Spring JDBC는 **SQLExpection**과 그 하위 예외들을 통해 에러를 핸들링합니다. 데이터베이스 연동 시 발생하는 대부분의 에러는 **java.sql.SQLException**을 상속한 예외들로 처리됩니다.

Spring JDBC를 사용할 때, **DataAccessException**과 그 하위 예외들을 적절히 처리하여 데이터베이스 작업 중 발생하는 에러를 핸들링할 수 있습니다. 또한, **@Repository** 애노테이션을 이용하여 특정 예외들을 캐치하거나 로깅하는 등의 작업을 수행할 수 있습니다.

## 결론

Spring Data JPA와 Spring JDBC는 각각의 특성에 맞게 에러 핸들링을 수행하며, 사용하는 기술에 따라 적절한 방식으로 에러를 처리할 수 있습니다.

**Spring Data JPA**는 JPA의 표준에 따라 예외를 핸들링하고, **Spring JDBC**는 JDBC의 예외를 핸들링하는 특징을 가지고 있습니다. 개발자는 이러한 차이를 이해하고, 각각의 기술에 맞게 적절한 에러 핸들링을 수행해야 합니다.

이러한 에러 핸들링 방식을 이해하고 적용함으로써 안정적인 데이터베이스 작업을 수행할 수 있으며, 시스템의 신뢰성을 높일 수 있습니다.

참고 문헌:
- [Spring Data JPA Exception Handling](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#transactions)
- [Spring Framework - DataAccessException](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/dao/DataAccessException.html)