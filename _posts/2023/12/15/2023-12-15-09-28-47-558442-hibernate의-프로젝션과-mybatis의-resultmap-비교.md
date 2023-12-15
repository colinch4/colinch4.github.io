---
layout: post
title: "[java] Hibernate의 프로젝션과 MyBatis의 resultMap 비교"
description: " "
date: 2023-12-15
tags: [java]
comments: true
share: true
---

이번 글에서는 Hibernate와 MyBatis에서 데이터베이스 결과를 매핑하는 데 사용되는 두 가지 기술인 프로젝션과 resultMap에 대해 비교해보겠습니다. Hibernate는 ORM(Object-Relational Mapping) 프레임워크이며, 데이터베이스 테이블과 Java 객체를 매핑하는 데 사용됩니다. 반면에 MyBatis는 SQL과 Java 객체를 매핑하기 위한 데이터베이스 액세스 라이브러리입니다.

## Hibernate의 프로젝션

Hibernate에서 프로젝션은 SQL의 SELECT 문과 유사하게 원하는 엔티티의 일부 속성만 선택하여 조회하는 것을 의미합니다. 

예를 들어, 다음은 Hibernate 프로젝션의 예시입니다.

```java
Session session = sessionFactory.openSession();
List<Object[]> results = session.createQuery("select firstName, lastName from Employee").list();
for (Object[] obj : results) {
    String firstName = (String) obj[0];
    String lastName = (String) obj[1];
    // 처리 로직
}
```

위의 코드에서 "select firstName, lastName from Employee"는 firstName과 lastName 열만을 조회하는 쿼리를 나타냅니다. 이러한 방식으로 원하는 엔티티의 일부 속성만을 선택하여 가져올 수 있습니다.

## MyBatis의 resultMap

MyBatis에서는 resultMap을 사용하여 데이터베이스 결과를 자바 객체로 매핑할 수 있습니다. 

아래는 MyBatis resultMap의 예시입니다.

```xml
<resultMap id="employeeResultMap" type="Employee">
    <result property="firstName" column="first_name" />
    <result property="lastName" column="last_name" />
</resultMap>
<select id="selectEmployees" resultMap="employeeResultMap">
    SELECT first_name, last_name
    FROM employee
</select>
```

위의 예시에서는 resultMap을 사용하여 데이터베이스의 열과 자바 객체의 속성을 매핑하고, selectEmployees 쿼리에서 resultMap을 참조하여 결과를 매핑합니다.

## 결론

Hibernate의 프로젝션은 원하는 엔티티의 일부 속성만을 선택하여 조회하는 데 사용되며, MyBatis의 resultMap은 데이터베이스 결과를 자바 객체로 매핑하는 데 사용됩니다. 각각의 기술은 다양한 상황에서 유용하게 활용될 수 있으며, 개발자는 프로젝트의 요구사항과 환경에 적합한 기술을 선택할 수 있습니다.

이상으로 Hibernate의 프로젝션과 MyBatis의 resultMap에 대한 비교를 마치겠습니다. 부족한 점이 있을 수 있으나, 이 비교를 통해 두 기술의 차이를 이해하는 데 도움이 되었기를 바랍니다.

자세한 내용은 아래의 참고 자료들을 참조해 주세요.

## 참고 자료
- Hibernate Documentation: [Link](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html)
- MyBatis User Guide: [Link](https://mybatis.org/mybatis-3/ko/index.html)

**[Note]** 이 글은 Hibernate와 MyBatis 프로젝션 및 resultMap에 대한 비교를 다룬 것입니다. 위의 코드 및 설명은 개념을 이해하는 데 도움을 줄 수 있도록 작성되었습니다.