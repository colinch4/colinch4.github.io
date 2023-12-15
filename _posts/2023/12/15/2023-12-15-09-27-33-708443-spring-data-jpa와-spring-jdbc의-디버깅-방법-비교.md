---
layout: post
title: "[java] Spring Data JPA와 Spring JDBC의 디버깅 방법 비교"
description: " "
date: 2023-12-15
tags: [java]
comments: true
share: true
---

Spring Data JPA와 Spring JDBC는 모두 데이터베이스와 상호 작용하는 Spring 프레임워크의 데이터 액세스 계층 기술입니다. 이 두 기술을 사용할 때 발생할 수 있는 문제를 해결하기 위해서는 각각의 디버깅 방법을 알고 있어야 합니다. 이번 포스트에서는 Spring Data JPA와 Spring JDBC의 디버깅 방법을 비교해보겠습니다.

## Spring Data JPA 디버깅 방법

Spring Data JPA를 사용하는 경우, 다음과 같은 방법을 사용하여 디버깅할 수 있습니다.

1. **Logging 설정**: Spring Data JPA는 내부적으로 SLF4J와 Commons Logging을 사용하므로, 적절한 로깅 설정을 통해 JPA 쿼리의 실행 내역과 성능을 확인할 수 있습니다.

    ```java
    logging.level.org.hibernate.SQL=DEBUG
    logging.level.org.hibernate.type.descriptor.sql.BasicBinder=TRACE
    ```

2. **@Query 애노테이션 활용**: 사용자 정의 쿼리 메소드에 @Query 애노테이션을 사용하여 실제 실행되는 SQL 쿼리를 확인할 수 있습니다.

    ```java
    @Query("SELECT u FROM User u WHERE u.status = :status")
    List<User> findByStatus(@Param("status") String status);
    ```

## Spring JDBC 디버깅 방법

Spring JDBC를 사용하는 경우, 아래의 방법을 활용하여 디버깅할 수 있습니다.

1. **DataSource 설정**: 데이터베이스 연결 정보 및 쿼리 수행과 관련된 로깅을 위해 DataSource의 설정을 활용할 수 있습니다.

2. **JdbcTemplate 디버깅**: JdbcTemplate을 활용하여 쿼리를 수행할 경우 SQL 쿼리와 파라미터 값을 로깅하여 디버깅할 수 있습니다.

    ```java
    jdbcTemplate.query("SELECT * FROM users WHERE status = ?", new Object[] { "active" }, new UserRowMapper());
    ```

이렇게 Spring Data JPA와 Spring JDBC는 각각의 방법으로 디버깅이 가능합니다. 적절한 디버깅을 통해 데이터 액세스 계층에서 발생하는 문제를 신속하게 해결할 수 있습니다.

참고 문헌:
- [Spring Data JPA - Debugging](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#core.debugging)
- [Spring Framework - JDBC](https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/data-access.html#jdbc)