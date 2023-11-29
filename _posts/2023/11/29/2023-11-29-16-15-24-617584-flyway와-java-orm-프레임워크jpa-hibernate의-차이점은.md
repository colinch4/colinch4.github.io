---
layout: post
title: "[java] Flyway와 Java ORM 프레임워크(JPA, Hibernate)의 차이점은?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

Flyway와 Java ORM 프레임워크(JPA, Hibernate)는 둘 다 데이터베이스 관련 작업을 처리하는데 사용되는 도구입니다. 하지만 각각의 목적과 기능은 다릅니다. 이 글에서는 Flyway와 JPA/Hibernate의 주요 차이점을 살펴보도록 하겠습니다.

## Flyway

Flyway는 데이터베이스 마이그레이션 도구로, 애플리케이션과 데이터베이스 스키마의 버전 관리를 지원합니다. Flyway를 사용하면 스키마 변경에 따른 데이터베이스 마이그레이션을 쉽게 관리할 수 있습니다. 스키마 파일들을 생성하고, 버전을 관리하며, 새로운 버전으로 업그레이드하거나 롤백할 수 있는 기능을 제공합니다. Flyway는 SQL 스크립트를 사용하여 데이터베이스 스키마를 변경하고 관리하는 것이 주요 목적입니다.

## Java ORM 프레임워크 (JPA, Hibernate)

Java ORM 프레임워크는 객체-관계 매핑(Object-Relational Mapping)을 위한 도구입니다. JPA(Java Persistence API)는 Java에서 ORM을 사용하기 위한 API를 제공하며, Hibernate는 JPA의 구현체 중 하나입니다. ORM은 객체와 데이터베이스 사이의 변환 작업을 자동으로 처리하여, 개발자는 SQL 쿼리를 직접 작성하지 않고도 객체 지향적인 방식으로 데이터베이스 조작을 할 수 있게 해줍니다.

JPA/Hibernate는 데이터베이스의 테이블과 자바 객체 간의 매핑을 정의하는 어노테이션(@Annotation)을 사용합니다. 이를 통해 데이터베이스 조작을 위한 SQL 쿼리를 자동으로 생성하고, 개발자가 객체를 통해 데이터베이스에 접근할 수 있게 합니다. JPA/Hibernate는 또한 캐시, 지연로딩, 트랜잭션 관리 등 다양한 기능을 제공하여 개발자의 생산성을 높여줍니다.

## 결론

Flyway는 데이터베이스 스키마의 버전 관리를 위한 도구이며, SQL 스크립트를 사용하여 스키마 변경 작업을 수행합니다. JPA/Hibernate는 객체-관계 매핑을 위한 도구로, 개발자가 SQL 쿼리를 직접 작성하지 않고도 객체를 통해 데이터베이스 조작을 할 수 있게 해줍니다. 각각의 도구는 다른 목적과 기능을 가지고 있으므로, 프로젝트의 요구사항에 맞게 적절한 도구를 선택해야 합니다.

참고 문서:
- [Flyway 공식 문서](https://flywaydb.org/documentation/)
- [Hibernate 공식 문서](https://hibernate.org/documentation/)
- [JPA 공식 문서](http://java.sun.com/developer/technicalArticles/J2EE/jpa/)

이상으로 Flyway와 JPA/Hibernate의 차이점에 대해 알아보았습니다. 감사합니다!