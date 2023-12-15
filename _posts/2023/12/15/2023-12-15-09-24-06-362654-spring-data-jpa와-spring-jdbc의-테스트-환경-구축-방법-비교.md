---
layout: post
title: "[java] Spring Data JPA와 Spring JDBC의 테스트 환경 구축 방법 비교"
description: " "
date: 2023-12-15
tags: [java]
comments: true
share: true
---

Spring은 데이터 액세스 레이어를 효율적으로 관리할 수 있는 여러 가지 옵션을 제공합니다. 이 포스트에서는 Spring Data JPA와 Spring JDBC를 사용하는 경우 각각의 테스트 환경을 어떻게 구축하는지에 대해 비교해보겠습니다.

## 목차
- [Spring Data JPA 테스트 환경 구축 방법](#spring-data-jpa-테스트-환경-구축-방법)
- [Spring JDBC 테스트 환경 구축 방법](#spring-jdbc-테스트-환경-구축-방법)
- [결론](#결론)

## Spring Data JPA 테스트 환경 구축 방법

Spring Data JPA를 사용하는 경우, 테스트 시에는 일반적으로 H2 데이터베이스를 내장 데이터베이스로 사용하는 것이 일반적입니다. 다음은 Spring Data JPA 기반의 테스트를 설정하는 간단한 예제입니다.

```java
import static org.junit.Assert.assertEquals;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.junit4.SpringRunner;
import com.example.demo.model.User;
import com.example.demo.repository.UserRepository;

@RunWith(SpringRunner.class)
@DataJpaTest
public class UserRepositoryIntegrationTest {

    @Autowired
    private UserRepository userRepository;

    @Test
    public void whenFindById_thenReturnUser() {
        // given
        User user = new User("John", "john@example.com");
        userRepository.save(user);

        // when
        User found = userRepository.findById(user.getId()).orElse(null);

        // then
        assertEquals(user.getName(), found.getName());
    }
}
```

위의 예제에서는 `@DataJpaTest` 어노테이션을 사용하여 JPA 테스트를 위한 구성을 활성화하고, 내장 데이터베이스를 사용하여 데이터베이스를 초기화합니다.

## Spring JDBC 테스트 환경 구축 방법

Spring JDBC를 사용하는 경우, 테스트를 위해 데이터베이스 연결을 위한 구성이 필요합니다. 최신 Spring 버전을 사용하는 경우, H2 데이터베이스를 내장 데이터베이스로 사용하는 것이 일반적입니다. 다음은 Spring JDBC를 사용한 간단한 테스트 환경 설정 예제입니다.

```java
import static org.junit.Assert.assertEquals;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.test.annotation.DirtiesContext;

@SpringBootTest
@DirtiesContext
public class JdbcUserRepositoryIntegrationTest {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Test
    public void testInsert() {
        jdbcTemplate.update("INSERT INTO users(id, name, email) VALUES (1, 'John', 'john@example.com')");
        int count = jdbcTemplate.queryForObject("SELECT count(*) FROM users", Integer.class);
        assertEquals(1, count);
    }
}
```

위의 예제에서는 `@SpringBootTest` 및 `@DirtiesContext` 어노테이션을 사용하여 Spring JDBC 테스트를 위한 구성을 활성화하고, H2 데이터베이스를 사용하여 데이터베이스를 초기화합니다.

## 결론

Spring Data JPA와 Spring JDBC 각각을 사용하는 경우, 데이터 액세스 테스트를 위한 환경 구축 방법은 약간씩 다를 수 있습니다. Spring Data JPA의 경우 `@DataJpaTest`를 사용하여 내장 데이터베이스를 초기화하고, Spring JDBC의 경우 `@SpringBootTest` 및 `@DirtiesContext`를 사용하여 H2 데이터베이스를 초기화하는 것이 일반적입니다. 이러한 환경 설정을 통해 개발자는 안정적인 데이터 액세스 레이어를 보다 쉽게 구축하고 유지할 수 있습니다.

더 많은 정보를 원하시면 [Spring Framework 공식 문서](https://spring.io/projects/spring-framework)를 참고하십시오.