---
layout: post
title: "[java] JPA에서의 Entity와 MyBatis에서의 Mapper의 역할 비교"
description: " "
date: 2023-12-15
tags: [java]
comments: true
share: true
---

JPA와 MyBatis는 모두 자바 기반의 데이터 액세스 기술이지만, 각각의 역할이 다릅니다. JPA는 **엔티티(Entity)**와 **매핑(mapping)**을 중심으로 동작하며, MyBatis는 **매퍼(Mapper)**를 중심으로 동작합니다. 이번 글에서는 JPA의 엔티티와 MyBatis의 매퍼의 역할을 비교하고자 합니다.

## JPA의 Entity
JPA에서의 **엔티티(Entity)**는 데이터베이스의 테이블과 매핑됩니다. 엔티티는 데이터베이스 테이블의 레코드를 나타내는 객체입니다. 엔티티 클래스에는 데이터베이스 테이블의 컬럼을 매핑하는 어노테이션들이 사용됩니다. JPA를 사용하면 엔티티의 CRUD(Create, Read, Update, Delete) 기능을 쉽게 구현할 수 있습니다.

```java
@Entity
@Table(name = "employee")
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String department;
    // getters and setters
}
```

## MyBatis의 Mapper
MyBatis에서의 **매퍼(Mapper)**는 SQL 쿼리와 자바 메소드를 매핑시켜주는 역할을 합니다. 매퍼 인터페이스에는 데이터베이스와 관련된 메소드가 정의되어 있고, XML 파일에서 실제 SQL 쿼리를 작성합니다. 매퍼를 사용하면 SQL 쿼리의 결과를 객체로 매핑하거나 객체를 SQL 파라미터로 변환하는 작업을 쉽게 할 수 있습니다.

```java
public interface EmployeeMapper {
    Employee selectEmployeeById(Long id);
    void insertEmployee(Employee employee);
    void updateEmployee(Employee employee);
    void deleteEmployee(Long id);
}
```

## 결론
JPA의 **엔티티**는 데이터베이스 테이블과 매핑되는 객체이고, MyBatis의 **매퍼**는 SQL 쿼리와 자바 메소드를 매핑시켜주는 역할을 합니다. JPA는 객체와 데이터베이스 간의 매핑을 중점으로 하며, MyBatis는 SQL과 자바 메소드 간의 매핑을 중점으로 합니다.

이러한 차이로 인해 JPA는 객체 지향적인 프로그래밍에 적합하고, MyBatis는 SQL 쿼리를 직접 다루거나 복잡한 매핑을 할 때 유용합니다.

## References
- [JPA (Java Persistence API)](https://www.oracle.com/java/technologies/persistence-jsp.html)
- [MyBatis](https://mybatis.org/mybatis-3/)