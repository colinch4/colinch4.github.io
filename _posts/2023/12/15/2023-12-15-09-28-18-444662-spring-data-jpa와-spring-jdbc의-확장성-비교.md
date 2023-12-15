---
layout: post
title: "[java] Spring Data JPA와 Spring JDBC의 확장성 비교"
description: " "
date: 2023-12-15
tags: [java]
comments: true
share: true
---

Spring 프레임워크는 데이터 액세스 레이어를 구축하기 위한 다양한 기술을 제공합니다. 그 중에서 Spring Data JPA와 Spring JDBC는 두 가지 주요한 옵션입니다. 이 블로그는 Spring Data JPA와 Spring JDBC의 확장성을 비교하고자 합니다.

## 1. Spring Data JPA

Spring Data JPA는 JPA(Java Persistence API)의 구현체로, 객체-관계 매핑(ORM)을 지원합니다. 이를 통해 데이터베이스 테이블과 자바 객체 사이의 매핑이 용이해지며, 복잡한 SQL 쿼리 작성을 피할 수 있습니다.

Spring Data JPA는 Repository 인터페이스를 통해 CRUD(Create, Read, Update, Delete) 메서드를 자동으로 생성하고, JPQL(Java Persistence Query Language)을 사용하여 유연한 쿼리를 작성할 수 있습니다. 또한 내장된 기능을 통해 페이징, 정렬, 동적 쿼리 생성 등 다양한 데이터 액세스 요구 사항을 처리할 수 있습니다.

## 2. Spring JDBC

Spring JDBC는 JDBC(Java Database Connectivity)를 기반으로 하는 간단하고 직접적인 데이터 액세스 방법을 제공합니다. SQL 쿼리를 직접 작성하고 실행하여 데이터베이스와 상호 작용할 수 있습니다. 이를 통해 더 세밀한 제어와 최적화된 쿼리 실행이 가능합니다.

Spring JDBC는 RowMapper 및 ResultSetExtractor와 같은 개념을 사용하여 데이터를 객체로 매핑하고, PreparedStatementCreator 및 SqlParameterSource를 활용하여 파라미터화된 쿼리를 실행할 수 있습니다.

## 3. 확장성 비교

Spring Data JPA는 객체-관계 매핑과 강력한 내장 기능을 통해 개발 생산성을 높일 수 있지만, 복잡한 쿼리나 세밀한 제어를 필요로 하는 경우에는 한계가 있을 수 있습니다. 반면에 Spring JDBC는 직접적인 SQL 쿼리 작성을 통해 뛰어난 성능과 유연성을 제공하지만, 개발자가 직접 데이터베이스와의 상호작용을 모두 관리해야 합니다.

따라서 프로젝트의 요구사항과 용도에 따라 Spring Data JPA 또는 Spring JDBC 중에서 선택해야 합니다. 종종 둘을 혼합해서 사용하는 방법도 있으며, 이는 프로젝트의 특정 영역에서는 Spring Data JPA를 사용하고 다른 영역에서는 Spring JDBC를 사용하는 경우에 유용할 수 있습니다.

이러한 선택은 프로젝트의 확장성과 유지보수성을 고려하여 신중하게 결정하여야 합니다.

Spring Data JPA와 Spring JDBC에 대한 자세한 정보는 [공식 문서](https://spring.io/projects/spring-data-jpa)를 참고하시기 바랍니다.