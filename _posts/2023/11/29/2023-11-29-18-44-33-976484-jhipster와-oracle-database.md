---
layout: post
title: "[java] JHipster와 Oracle Database"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

JHipster(Java Hipster)는 Java 기반의 웹 애플리케이션을 빠르게 개발할 수 있는 도구입니다. 이번 포스트에서는 JHipster와 Oracle Database를 함께 사용하는 방법에 대해 알아보겠습니다.

## 1. Oracle Database 연동 설정

JHipster 프로젝트에서 Oracle Database를 사용하기 위해서는 몇 가지 설정을 해주어야 합니다.

### 1.1. pom.xml 파일 수정

pom.xml 파일에 다음과 같이 Oracle Database 드라이버를 추가합니다.

```xml
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc8</artifactId>
    <version>19.3.0.0</version>
    <scope>runtime</scope>
</dependency>
```

### 1.2. application-dev.yml 파일 수정

application-dev.yml 파일에 Oracle Database 연결 정보를 설정합니다.

```yaml
spring:
  datasource:
    url: jdbc:oracle:thin:@localhost:1521/{your_database_name}
    username: {your_username}
    password: {your_password}
```

위의 예시에서 `{your_database_name}`, `{your_username}`, `{your_password}`는 각각 실제 사용하는 Oracle Database의 정보로 대체되어야 합니다.

## 2. 엔티티 생성과 JPA 설정

JHipster에서는 엔티티 생성과 JPA 설정을 간편하게 할 수 있는 명령어가 제공됩니다.

```shell
yo jhipster:entity {your_entity_name}
```

위의 명령어를 실행하면 JHipster는 자동으로 엔티티와 해당하는 JPA 설정을 생성해줍니다. Oracle Database를 사용할 경우, JPA 설정에서 `dialect`을 Oracle로 설정해주어야 합니다.

## 3. 앱 실행

마지막으로 앱을 실행하여 Oracle Database와의 연동을 확인해보세요.

```shell
./mvnw
```

위의 명령어를 실행하면 JHipster 앱이 로컬환경에서 실행되며, Oracle Database와의 연동이 성공적으로 이루어집니다.

## 4. 결론

이제 JHipster와 Oracle Database를 함께 사용하는 방법에 대해 알아보았습니다. JHipster를 사용하여 빠르게 개발할 수 있고, Oracle Database와의 연동을 통해 안정적인 데이터베이스를 활용할 수 있습니다.

## 참고 자료

- [JHipster 공식 문서](https://www.jhipster.tech/)
- [Oracle Database 공식 사이트](https://www.oracle.com/database/)