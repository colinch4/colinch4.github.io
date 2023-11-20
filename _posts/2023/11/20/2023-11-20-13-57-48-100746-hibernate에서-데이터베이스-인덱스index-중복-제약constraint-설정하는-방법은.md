---
layout: post
title: "[java] Hibernate에서 데이터베이스 인덱스(Index) 중복 제약(Constraint) 설정하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Hibernate를 사용하여 데이터베이스에 중복 제약(Constraint)을 설정하는 방법은 다음과 같습니다.

1. @Table 주석에서 uniqueConstraints 속성 사용하기:

```java
@Entity
@Table(name = "my_table", uniqueConstraints = @UniqueConstraint(columnNames = {"column1", "column2"}))
public class MyEntity {
    // ...
}
```

2. @Column 주석에서 unique 속성 사용하기:

```java
@Entity
@Table(name = "my_table")
public class MyEntity {
    @Column(name = "column1", unique = true)
    private String column1;

    @Column(name = "column2", unique = true)
    private String column2;

    // ...
}
```

위의 예제에서는 "my_table" 테이블에서 "column1"과 "column2"에 대해 중복 제약(Constraint)을 설정하고 있습니다.

이렇게 설정된 중복 제약은 Hibernate가 데이터베이스에 테이블을 생성할 때 자동으로 인덱스를 생성해줍니다. 이제 중복 데이터가 발생하면 Hibernate는 예외를 던지게 됩니다.

참고 문서:
- Hibernate Documentation: [https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#annotations-index](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#annotations-index)