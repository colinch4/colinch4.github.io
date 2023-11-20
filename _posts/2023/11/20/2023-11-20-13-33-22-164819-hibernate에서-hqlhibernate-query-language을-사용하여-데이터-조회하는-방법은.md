---
layout: post
title: "[java] Hibernate에서 HQL(Hibernate Query Language)을 사용하여 데이터 조회하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Hibernate는 객체 관계 매핑 (ORM) 프레임워크로서, 관계형 데이터베이스와 객체 간의 상호 변환을 도와줍니다. Hibernate Query Language (HQL)은 Hibernate에서 데이터를 조회하는 데 사용되는 강력한 쿼리 언어입니다. HQL을 사용하면 SQL을 직접 작성하지 않고도 객체를 기반으로 데이터를 쉽게 조회할 수 있습니다.

다음은 Hibernate에서 HQL을 사용하여 데이터를 조회하는 간단한 예제입니다:

```java
// Hibernate Session 객체를 얻어옵니다.
Session session = HibernateUtil.getSessionFactory().openSession();

// HQL 쿼리를 작성합니다.
String hql = "FROM Employee";

// Query 객체를 생성합니다.
Query query = session.createQuery(hql);

// 쿼리를 실행하고 결과를 얻어옵니다.
List<Employee> employees = query.list();

// 결과를 출력합니다.
for (Employee employee : employees) {
    System.out.println(employee.getName());
}

// 세션을 닫습니다.
session.close();
```

위의 예제에서는 Employee 클래스를 기반으로 "FROM Employee" HQL 쿼리를 작성하고, Query 객체를 생성한 후 실행합니다. 그런 다음 쿼리 결과를 List<Employee>에 저장하고 출력합니다.

이 예제에서는 단순한 HQL 쿼리를 사용했지만, HQL은 다양한 기능을 제공합니다. 다음은 HQL의 주요 기능 몇 가지입니다:

- 필드 선택: SELECT 절을 사용하여 특정 필드만 선택할 수 있습니다.
- 조건 필터링: WHERE 절을 사용하여 조건을 지정하여 데이터를 필터링할 수 있습니다.
- 정렬: ORDER BY 절을 사용하여 데이터를 정렬할 수 있습니다.
- 조인: 다른 엔티티와의 조인을 사용하여 관련된 데이터를 한 번에 조회할 수 있습니다.

더 자세한 내용은 Hibernate 공식 문서를 참조하시기 바랍니다.