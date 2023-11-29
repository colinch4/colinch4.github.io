---
layout: post
title: "[java] Liquibase와 Spring Data JPA 통합 가이드"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

## 목차
- [소개](#소개)
- [Liquibase란 무엇인가?](#Liquibase란-무엇인가?)
- [Spring Data JPA란 무엇인가?](#Spring-Data-JPA란-무엇인가?)
- [Liquibase와 Spring Data JPA 통합하기](#Liquibase와-Spring-Data-JPA-통합하기)
- [결론](#결론)


## 소개
이 가이드는 Liquibase와 Spring Data JPA를 통합하여 데이터베이스 마이그레이션을 관리하는 방법에 대해 설명합니다.


## Liquibase란 무엇인가?
Liquibase는 데이터베이스 스키마의 버전 관리 및 마이그레이션을 지원하는 오픈 소스 도구입니다. Liquibase를 사용하면 데이터베이스 스키마의 변경 사항을 버전 관리하여 쉽게 관리할 수 있습니다. 또한, 변경 사항을 적용할 때 롤백 기능도 제공되어 안전한 스키마 업데이트가 가능합니다.


## Spring Data JPA란 무엇인가?
Spring Data JPA는 스프링 프레임워크의 일부로써 JPA(Java Persistence API)를 이용하여 데이터 액세스 기술을 추상화하는 기능을 제공합니다. Spring Data JPA를 사용하면 개발자는 반복적이고 번거로운 CRUD(Create, Read, Update, Delete) 작업을 간소화할 수 있습니다.


## Liquibase와 Spring Data JPA 통합하기
Liquibase를 Spring Data JPA와 통합하여 사용하면 데이터베이스 스키마의 버전 관리를 손쉽게 할 수 있습니다. 다음은 Liquibase와 Spring Data JPA를 통합하는 방법입니다.

1. 의존성 추가: `pom.xml` 파일에 Liquibase와 Spring Data JPA의 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
    <version>4.4.3</version>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

2. Liquibase 설정: `application.properties` 파일에 Liquibase의 설정을 추가합니다.

```properties
# 데이터베이스 JDBC URL
spring.datasource.url=jdbc:mysql://localhost:3306/mydb

# 데이터베이스 사용자명 및 비밀번호
spring.datasource.username=root
spring.datasource.password=1234

# Liquibase 변경 로그 위치 및 파일명 설정
spring.liquibase.change-log=classpath:db/changelog/db.changelog-master.xml
```

3. 변경 로그 작성: Liquibase의 변경 로그 파일을 작성하여 데이터베이스 스키마의 변경 사항을 정의합니다. 변경 로그 파일은 `db/changelog` 폴더에 위치하며, `.xml` 혹은 `.yaml` 확장자를 가지는 파일로 작성됩니다.

```xml
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                                       http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <!-- 변경 사항 정의 -->
    <changeSet id="1" author="yourname">
        <createTable tableName="users">
            <column name="id" type="bigint" autoIncrement="true">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="name" type="varchar(255)"/>
        </createTable>
    </changeSet>

</databaseChangeLog>
```

4. 스프링 부트 애플리케이션 실행: Liquibase와 Spring Data JPA가 통합되어 애플리케이션을 실행합니다. Liquibase는 변경 로그에 정의된 변경 사항을 자동으로 인식하여 데이터베이스 스키마를 업데이트합니다.

5. 데이터 액세스: Spring Data JPA를 사용하여 데이터 액세스 작업을 수행합니다. Spring Data JPA는 Liquibase로 인해 업데이트된 데이터베이스 스키마를 자동으로 인식하여 작업을 처리합니다.

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    // 사용자 조회
    Optional<User> findByUsername(String username);

    // 사용자 저장
    User save(User user);

    // 사용자 삭제
    void delete(User user);

}
```

## 결론
Liquibase와 Spring Data JPA를 통합하여 데이터베이스 마이그레이션을 관리하는 방법을 알아보았습니다. 이를 통해 데이터베이스 스키마의 변경 사항을 버전 관리하여 안전하고 효율적인 애플리케이션 개발을 할 수 있습니다.