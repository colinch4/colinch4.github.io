---
layout: post
title: "[java] Hibernate에서 Criteria Query를 사용하여 데이터 조회하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Hibernate는 객체 관계 매핑(Object Relational Mapping, ORM) 프레임워크로, 데이터베이스와 자바 객체 간의 매핑을 단순화하여 개발자가 더 효과적으로 데이터베이스와 상호작용할 수 있도록 도와줍니다. Criteria Query는 Hibernate에서 데이터를 조회하는 방법 중 하나로, SQL 쿼리를 직접 작성하는 대신에 객체 지향적인 방식으로 데이터를 조회할 수 있도록 도와줍니다.

Criteria Query를 사용하여 데이터를 조회하는 방법은 다음과 같습니다:

1. Session 객체를 얻습니다. Hibernate에서 모든 작업은 Session 객체를 통해 이루어집니다.

```java
Session session = sessionFactory.openSession();
```

2. CriteriaBuilder를 사용하여 CriteriaQuery 객체를 생성합니다. CriteriaBuilder는 Criteria Query를 생성하는 데 사용되며, CriteriaQuery는 조회할 데이터의 타입을 지정합니다.

```java
CriteriaBuilder builder = session.getCriteriaBuilder();
CriteriaQuery<EntityType> criteriaQuery = builder.createQuery(EntityType.class);
```

3. Root를 통해 데이터의 루트 엔티티를 지정합니다. Root는 CriteriaQuery에서 데이터를 조회할 엔티티를 지정하는 데 사용됩니다.

```java
Root<EntityType> root = criteriaQuery.from(EntityType.class);
```

4. CriteriaQuery 객체에 원하는 데이터를 추가합니다. 예를 들어, 조건에 맞는 데이터를 필터링하거나, 정렬 등의 작업을 수행할 수 있습니다.

```java
criteriaQuery.select(root).where(builder.equal(root.get("attribute"), value));
criteriaQuery.orderBy(builder.asc(root.get("attribute")));
```

5. Query 객체를 생성하고, CriteriaQuery 객체를 사용하여 실행합니다. Query 객체는 실제로 데이터베이스로부터 데이터를 조회하기 위해 사용되며, 결과를 반환합니다.

```java
Query<EntityType> query = session.createQuery(criteriaQuery);
List<EntityType> result = query.getResultList();
```

6. Session 객체를 닫습니다.

```java
session.close();
```

위의 단계를 따라 실행하면, Hibernate에서 Criteria Query를 사용하여 데이터를 조회할 수 있습니다. Criteria Query를 사용하면 객체 지향적인 방식으로 데이터를 조회할 수 있으므로, 더 직관적이고 유연한 코드를 작성할 수 있습니다.

참고 문서:
- Hibernate Documentation: [https://docs.jboss.org/hibernate/orm/5.4/userguide/html_single/Hibernate_User_Guide.html#criteria](https://docs.jboss.org/hibernate/orm/5.4/userguide/html_single/Hibernate_User_Guide.html#criteria)