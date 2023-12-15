---
layout: post
title: "[java] Hibernate의 세션과 MyBatis의 SqlSession의 역할 비교"
description: " "
date: 2023-12-15
tags: [java]
comments: true
share: true
---

Hibernate와 MyBatis는 둘 다 Java 기반의 오픈소스 ORM(Object-Relational Mapping) 프레임워크이지만, 각각의 프레임워크에는 쓰임새와 사용법이 다소 차이가 있습니다. 이들 ORM 프레임워크의 핵심 요소 중 하나인 "세션"과 "SqlSession"을 비교하여, 이 두 프레임워크의 차이점과 장단점에 대해 알아보겠습니다.

## 1. Hibernate의 세션 (Session)

Hibernate의 세션은 영속성을 제공하는 데 사용됩니다. 영속성이란 데이터가 생성된 상태를 유지하고, 데이터를 다른 시스템에 전송하여도 손상되지 않는 것을 말합니다. Hibernate 세션이 쿼리를 실행하고 데이터를 가져오는 작업을 관리하며, 데이터베이스와의 연결을 제어합니다.

### 사용 예시

```java
Session session = HibernateUtil.getSessionFactory().openSession();
session.beginTransaction();
// 데이터 조작이나 조회 작업 수행
session.getTransaction().commit();
session.close();
```

## 2. MyBatis의 SqlSession

반면에, MyBatis의 SqlSession은 데이터베이스와의 모든 상호작용에 대한 트랜잭션 처리를 수행합니다. SqlSession은 쿼리를 실행하고 매핑 구문을 실행하는 데 사용됩니다.

### 사용 예시

```java
SqlSession session = sqlSessionFactory.openSession();
// 데이터 조작이나 조회 작업 수행
session.commit();
session.close();
```

## 3. 역할 비교

- Hibernate의 세션은 영속성 관리와 쿼리 실행을 담당하는 반면, MyBatis의 SqlSession은 단순히 쿼리와 트랜잭션 처리를 담당합니다.
- Hibernate의 세션은 더 많은 기능을 자체적으로 제공하며, 개발자가 직접적으로 쿼리를 작성하지 않고도 객체를 통해 쿼리를 수행할 수 있는 반면, MyBatis는 SQL 쿼리에 집중하고 있어 개발자가 직접 SQL을 작성해야 합니다.

## 결론

두 세션의 차이점을 요약하면, Hibernate의 세션은 영속성을 제공하며 데이터를 객체 관점에서 다루는 반면, MyBatis의 SqlSession은 SQL 쿼리와 트랜잭션에 집중합니다. 따라서 프로젝트의 특성과 목적에 맞게 이 두 프레임워크를 선택하여 사용하면 됩니다.

이 글은 Hibernate와 MyBatis의 세션의 역할에 대해 비교하고자 설명했습니다. 각각의 프레임워크에 대해 더 자세히 알고 싶다면 공식 문서나 커뮤니티를 참고하시기 바랍니다.

[참고 문헌](https://dzone.com/articles/hibernate-session-v-mybatis)