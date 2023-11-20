---
layout: post
title: "[java] Hibernate에서 스키마 생성(Schema Generation) 설정하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Hibernate는 Java 기반의 ORM(Object-Relational Mapping) 프레임워크로서, 데이터베이스와 자바 객체 간의 매핑을 도와줍니다. 스키마 생성은 Hibernate를 사용하여 데이터베이스 테이블을 자동으로 생성하는 과정을 의미합니다. 이를 통해 개발자는 별도의 SQL 스크립트 작성 없이도 데이터베이스 스키마를 자동으로 만들 수 있습니다.

Hibernate에서 스키마 생성을 설정하기 위해 다음과 같은 방법을 따를 수 있습니다:

1. **hbm2ddl.auto 속성을 설정하는 방법:**

   Hibernate의 설정 파일(보통 hibernate.cfg.xml 또는 persistence.xml)에서 hbm2ddl.auto 속성을 설정합니다. hbm2ddl.auto 속성은 다음과 같은 값을 가질 수 있습니다:

   - `none`: 스키마 생성을 비활성화합니다.
   - `create`: 애플리케이션 시작 시 스키마를 생성합니다. 기존의 스키마가 이미 존재할 경우 삭제됩니다.
   - `create-drop`: 애플리케이션 시작 시 스키마를 생성하며, 애플리케이션 종료 시 삭제합니다.
   - `update`: 기존 스키마를 업데이트합니다. 추가된 테이블 또는 컬럼을 자동으로 생성합니다. 기존의 데이터는 보존됩니다.
   - `validate`: 현재 스키마와 자바 객체 간의 일치성을 확인합니다. 스키마에 대한 검증만 수행하고, 변경하지는 않습니다.

   예를 들어, `update` 속성으로 스키마 생성을 설정하려면 다음과 같이 설정 파일에 추가합니다:

   ```xml
   <property name="hibernate.hbm2ddl.auto">update</property>
   ```

   이제 Hibernate가 실행될 때 자동으로 스키마를 업데이트할 것입니다.

2. **Hibernate의 자바 API를 사용하는 방법:**

   Hibernate의 Configuration 객체를 사용하여 스키마 생성을 설정할 수도 있습니다. 아래 예시 코드는 `update` 속성으로 스키마 생성을 설정하는 방법을 보여줍니다:

   ```java
   Configuration configuration = new Configuration();
   configuration.setProperty("hibernate.hbm2ddl.auto", "update");
   ```

   이후에는 Hibernate Session Factory를 구성할 때 설정된 속성이 적용됩니다.

위 방법 중 어느 방법을 사용하더라도, 스키마 생성 설정은 개발 환경에서 주의해서 사용해야 합니다. 실제 운영 환경에서는 스키마를 수동으로 관리하는 것이 좋습니다.

더 자세한 내용은 [Hibernate 공식 문서](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#configurations)를 참고하십시오.