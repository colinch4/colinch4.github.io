---
layout: post
title: "[java] Java Querydsl과 Spring Framework의 연동"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

Querydsl은 SQL과 NoSQL 데이터베이스에 대한 타입 안정적인 쿼리 작성을 돕는 자바 라이브러리입니다. 이번 포스트에서는 Java Querydsl을 Spring Framework와 함께 사용하는 방법에 대해 알아보겠습니다.

## 1. Querydsl 라이브러리 추가

우선, Maven 또는 Gradle을 사용하여 프로젝트 의존성에 Querydsl을 추가해야 합니다.

### Maven

```xml
<dependency>
    <groupId>com.querydsl</groupId>
    <artifactId>querydsl-core</artifactId>
    <version>4.x.x</version>
</dependency>

<dependency>
    <groupId>com.querydsl</groupId>
    <artifactId>querydsl-jpa</artifactId>
    <version>4.x.x</version>
</dependency>
```

### Gradle

```groovy
dependencies {
    implementation 'com.querydsl:querydsl-core:4.x.x'
    implementation 'com.querydsl:querydsl-jpa:4.x.x'
}
```

버전 번호는 현재 사용하고 있는 Querydsl 버전에 맞게 설정해주어야 합니다.

## 2. Querydsl 설정

Spring Framework와 함께 Querydsl을 사용하기 위해 설정 파일을 작성해야 합니다. 

### JPA 설정

JPA를 사용하는 경우, 아래와 같이 설정 파일을 작성해야 합니다.

```java
@Configuration
@EnableJpaRepositories(basePackages = "com.example.repository")
public class QuerydslConfig {

    @Autowired
    private EntityManager entityManager;

    @Bean
    public JPAQueryFactory jpaQueryFactory() {
        return new JPAQueryFactory(entityManager);
    }
}
```

`@EnableJpaRepositories` 어노테이션은 Spring Data JPA 리포지토리를 사용하는 경우에만 필요합니다. `basePackages` 속성에는 리포지토리 인터페이스가 정의되어 있는 패키지를 지정해주어야 합니다.

### MongoDB 설정

MongoDB를 사용하는 경우, 아래와 같이 설정 파일을 작성해야 합니다.

```java
@Configuration
public class QuerydslConfig {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Bean
    public MongoQueryFactory mongoQueryFactory() {
        return new MongoQueryFactory(mongoTemplate);
    }
}
```

위와 같이 설정하면 Querydsl을 사용할 준비가 끝났습니다.

## 3. Querydsl 사용

Querydsl을 사용하여 데이터베이스에서 데이터를 조회하려면 Querydsl 쿼리를 작성해야 합니다. 이는 각 데이터베이스 종류에 따라 조금씩 다를 수 있습니다. 

### JPA 사용 예제

아래는 JPA를 사용하여 데이터를 조회하는 예제입니다.

```java
@Repository
public class UserRepositoryImpl implements UserRepositoryCustom {

    @PersistenceContext
    private EntityManager entityManager;

    public List<User> findActiveUsers() {
        QUser user = QUser.user;
        return new JPAQuery<>(entityManager)
                .select(user)
                .from(user)
                .where(user.active.isTrue())
                .fetch();
    }
}
```

### MongoDB 사용 예제

아래는 MongoDB를 사용하여 데이터를 조회하는 예제입니다.

```java
@Repository
public class UserRepositoryImpl implements UserRepositoryCustom {

    private final MongoTemplate mongoTemplate;

    public UserRepositoryImpl(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    public List<User> findActiveUsers() {
        QUser user = QUser.user;
        return new MongoQuery<>(mongoTemplate)
                .select(user)
                .from(user)
                .where(user.active.isTrue())
                .fetch();
    }
}
```

위의 코드에서 `QUser`는 Querydsl이 코드 생성을 통해 생성한 엔티티 클래스입니다. 쿼리를 작성하고 실행하기 위해 Querydsl에서 제공하는 `JPAQuery` 또는 `MongoQuery` 클래스를 사용합니다.

## 결론

이렇게 함께 Querydsl과 Spring Framework를 사용하면 타입 안정적인 쿼리 작성을 통해 더 효율적으로 데이터베이스와 상호작용할 수 있습니다. Querydsl은 많은 데이터베이스 타입을 지원하고 있으므로 원하는 데이터베이스에 맞게 사용할 수 있습니다. 

관련자료:

- [Querydsl 레퍼런스 문서](http://www.querydsl.com/)
- [Spring Data JPA](https://spring.io/projects/spring-data-jpa)
- [Spring Data MongoDB](https://spring.io/projects/spring-data-mongodb)