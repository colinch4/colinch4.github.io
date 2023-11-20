---
layout: post
title: "[java] Hibernate에서 데이터베이스 컬럼(Column) 중복 제약(Constraint) 설정하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Hibernate는 객체와 관계형 데이터베이스 간의 매핑을 지원하는 자바 오픈소스 프레임워크입니다. 중복 제약(Constraint)은 데이터베이스에서 특정 컬럼에 대해 유니크한 값을 가지도록 설정하는 것을 의미합니다.

Hibernate에서 중복 제약을 설정하는 방법은 다음과 같습니다.

1. @Column(unique = true) 어노테이션 사용:
Java 클래스의 필드에 @Column 어노테이션을 사용하고, unique 속성을 true로 설정합니다. 이렇게 하면 해당 컬럼에 중복된 값이 들어올 경우 예외가 발생합니다.

```java
@Column(unique = true)
private String username;
```

2. @Table(uniqueConstraints = @UniqueConstraint(columnNames = {"column1", "column2"})) 어노테이션 사용:
Java 클래스에 @Table 어노테이션을 사용하고, uniqueConstraints 속성으로 해당 컬럼에 대한 중복 제약을 설정합니다. columnNames에 중복 제약을 걸고자 하는 컬럼들을 배열 형태로 전달합니다.

```java
@Table(uniqueConstraints = @UniqueConstraint(columnNames = {"username", "email"}))
public class User {
    // ...
}
```

이렇게 중복 제약을 설정하면 Hibernate가 데이터베이스에 테이블을 생성할 때 해당 제약 조건을 함께 생성합니다. 따라서 중복된 값을 가지는 레코드를 데이터베이스에 삽입하려고 할 때 예외가 발생하게 됩니다.

참고문서:
- Hibernate 공식 문서: https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html