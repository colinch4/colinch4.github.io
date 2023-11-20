---
layout: post
title: "[java] Hibernate에서 동적 쿼리(Dynamic query) 작성하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

1. Criteria API 사용: Criteria API는 Hibernate에서 동적 쿼리 작성에 사용되는 고급 프로그래밍 인터페이스입니다. 이를 사용하면 조건을 추가하고 쿼리를 동적으로 구성할 수 있습니다.

예시 코드:

```java
CriteriaBuilder cb = session.getCriteriaBuilder();
CriteriaQuery<Entity> query = cb.createQuery(Entity.class);
Root<Entity> root = query.from(Entity.class);

// 동적으로 필터링할 조건 추가
Predicate predicate = cb.equal(root.get("fieldName"), value);
query.where(predicate);

List<Entity> results = session.createQuery(query).getResultList();
```

2. HQL 사용: HQL(Hibernate Query Language)은 SQL과 유사한 Hibernate의 쿼리 언어입니다. HQL을 사용하면 동적 쿼리를 작성하고 필요한 조건을 추가할 수 있습니다.

예시 코드:

```java
String hql = "from Entity e where e.fieldName = :value";
Query<Entity> query = session.createQuery(hql, Entity.class);
query.setParameter("value", value);

List<Entity> results = query.getResultList();
```

3. Native SQL 사용: Hibernate에서는 네이티브 SQL 쿼리를 실행하는 기능도 제공합니다. 이를 사용하면 특정 데이터베이스에 특화된 쿼리를 작성할 수 있습니다.

예시 코드:

```java
String sql = "SELECT * FROM entity_table WHERE field_name = :value";
Query<Entity> query = session.createNativeQuery(sql, Entity.class);
query.setParameter("value", value);

List<Entity> results = query.getResultList();
```

위의 방법들은 Hibernate에서 동적으로 쿼리를 작성하는 일반적인 방법입니다. 각각의 상황에 따라 적절한 방법을 선택하여 쿼리를 작성할 수 있습니다.