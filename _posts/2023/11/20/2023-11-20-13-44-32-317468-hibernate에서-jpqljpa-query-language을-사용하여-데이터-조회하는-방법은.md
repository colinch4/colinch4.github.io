---
layout: post
title: "[java] Hibernate에서 JPQL(JPA Query Language)을 사용하여 데이터 조회하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

1. @Query 어노테이션을 사용하는 방법

```java
@Query("SELECT e FROM Employee e WHERE e.department = :department")
List<Employee> findByDepartment(@Param("department") String department);
```

2. NamedQuery를 정의하고 EntityManager에서 실행하는 방법

```java
@Entity
@NamedQuery(name = "Employee.findBySalaryRange", query = "SELECT e FROM Employee e WHERE e.salary BETWEEN :minSalary and :maxSalary")
public class Employee {
   //...
}

// EntityManager에서 실행
Query query = entityManager.createNamedQuery("Employee.findBySalaryRange");
query.setParameter("minSalary", 2000);
query.setParameter("maxSalary", 5000);
List<Employee> employees = query.getResultList();
```
 
3. Criteria API를 사용하는 방법

```java
CriteriaBuilder builder = entityManager.getCriteriaBuilder();
CriteriaQuery<Employee> query = builder.createQuery(Employee.class);
Root<Employee> root = query.from(Employee.class);
query.select(root).where(builder.equal(root.get("department"), "IT"));
List<Employee> employees = entityManager.createQuery(query).getResultList();
```

이러한 방법을 사용하여 Hibernate에서 JPQL을 사용하여 데이터를 조회할 수 있습니다. JPQL은 SQL과 유사한 문법을 가지고 있어 객체 지향적인 데이터 조회를 할 수 있습니다. Hibernate는 JPQL을 SQL로 변환하여 데이터베이스에 쿼리를 전달합니다.

더 자세한 정보는 Hibernate 공식 문서를 참고하시기 바랍니다.

- Hibernate 공식 문서: [https://hibernate.org/](https://hibernate.org/)
- JPA Query Language (JPQL) 소개: [https://docs.oracle.com/javaee/7/tutorial/persistence-querylanguage.htm](https://docs.oracle.com/javaee/7/tutorial/persistence-querylanguage.htm)