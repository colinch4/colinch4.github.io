---
layout: post
title: "[java] MyBatis와 ORM(Object-Relational Mapping)의 관계"
description: " "
date: 2023-12-21
tags: [java]
comments: true
share: true
---

ORM은 자바 객체와 관계형 데이터베이스 테이블 간의 맵핑을 자동으로 처리하는 기술입니다. ORM 프레임워크를 사용하면 SQL 쿼리를 직접 작성하지 않고도 데이터베이스와 상호 작용할 수 있습니다.

## MyBatis란 무엇인가?

**MyBatis**는 ORM 프레임워크 중 하나로, SQL 쿼리와 자바 객체 간의 맵핑을 처리합니다. MyBatis를 사용하면 개발자는 복잡한 SQL 쿼리를 작성하지 않고도 데이터베이스에 접근할 수 있습니다. 또한 MyBatis는 SQL 맵핑 파일을 사용하여 SQL 쿼리를 자바 코드와 분리할 수 있도록 지원합니다.

## ORM과의 관계

**MyBatis**는 ORM 프레임워크의 한 종류이지만, 전통적인 ORM 프레임워크인 Hibernate와는 몇 가지 차이점이 있습니다. Hibernate는 객체와 테이블 간의 매핑을 자동으로 처리하기 때문에 개발자가 직접 SQL 쿼리를 작성할 필요가 없지만, MyBatis는 XML이나 어노테이션을 사용하여 SQL 쿼리를 정의하고 매핑합니다. 따라서 MyBatis는 SQL 쿼리에 대한 높은 수준의 제어권을 제공하면서도 ORM의 이점을 살려 개발자들에게 유연성을 제공합니다.

## MyBatis의 장단점

### 장점
- **SQL 제어권**: MyBatis를 사용하면 개발자가 SQL 쿼리에 직접적인 제어권을 가질 수 있습니다.
- **성능 최적화**: SQL 쿼리를 직접 작성하기 때문에 성능 최적화가 상대적으로 쉽습니다.

### 단점
- **반복적인 작업**: SQL 쿼리 작성에 대한 반복적인 작업이 필요할 수 있습니다.
- **객체-테이블 맵핑**: Hibernate와 같은 전통적인 ORM 프레임워크보다 객체-테이블 맵핑에 대한 번거로움이 있을 수 있습니다.

MyBatis와 ORM의 관계는 개발자들에게 SQL 쿼리에 높은 수준의 제어권을 제공하면서도 객체와 테이블 간의 맵핑을 편리하게 처리할 수 있는 기술을 제공합니다.

---

참고 문헌:
- [MyBatis Documentation](https://mybatis.org/mybatis-3/ko/index.html)
- [ORM과 MyBatis](https://bamdule.tistory.com/entry/MyBatis-%EC%99%80-ORM)