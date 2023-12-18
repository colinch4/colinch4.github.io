---
layout: post
title: "[java] Hibernate와 JPA(Java Persistence API)"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

## 목차
1. [Hibernate란 무엇인가?](#hibernate란-무엇인가)
2. [JPA란 무엇인가?](#jpa란-무엇인가)
3. [Hibernate와 JPA의 차이](#hibernate와-jpa의-차이)
4. [Hibernate를 사용한 간단한 예제](#hibernate를-사용한-간단한-예제)
5. [참고 자료](#참고-자료)

---

## Hibernate란 무엇인가?

**Hibernate**는 Java 언어를 사용하여 관계형 데이터베이스와의 연동을 지원하는 오픈 소스 ORM(Object-Relational Mapping) 프레임워크이다. Hibernate를 사용하면 객체 지향적인 방식으로 데이터베이스를 다룰 수 있어서 복잡한 SQL 쿼리 작성을 피할 수 있고, 개발 생산성과 유지보수성을 향상시킬 수 있다.


## JPA란 무엇인가?

**JPA(Java Persistence API)**는 Java에서 관계형 데이터베이스에 데이터를 저장, 수정, 조회, 삭제할 수 있는 기능을 제공하는 API이다. JPA는 Java에서 ORM을 사용할 수 있도록 표준을 제공하며, Hibernate와 같은 ORM 프레임워크를 사용하기 위한 인터페이스를 제공한다.


## Hibernate와 JPA의 차이

**Hibernate**는 ORM의 구현체로, JPA를 지원하는 오픈 소스 중 하나이다. 따라서 Hibernate를 사용하면 JPA의 표준 기술과 함께 Hibernate 고유의 기능을 함께 사용할 수 있다. 

## Hibernate를 사용한 간단한 예제

```java
@Entity
@Table(name = "employee")
public class Employee {
    @Id
    private int id;
    private String name;
    private int salary;

    // getters and setters
}
```

위 예제는 Employee 클래스에 `@Entity`와 `@Table` 어노테이션을 통해 테이블과 매핑하고, `@Id` 어노테이션으로 기본키를 설정한 것이다. 이후 Hibernate를 사용하여 데이터베이스와의 상호작용이 가능해진다.


## 참고 자료
- [Hibernate 공식 사이트](https://hibernate.org/)
- [JPA 스펙 문서](https://docs.oracle.com/javaee/6/tutorial/doc/bnbpz.html)

---