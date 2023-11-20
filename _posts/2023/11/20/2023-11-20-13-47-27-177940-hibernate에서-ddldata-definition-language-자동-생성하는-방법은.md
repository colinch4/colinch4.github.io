---
layout: post
title: "[java] Hibernate에서 DDL(Data Definition Language) 자동 생성하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Hibernate는 객체 관계 매핑(ORM)을 사용하여 데이터베이스와의 상호 작용을 용이하게 해주는 인기 있는 프레임워크입니다. Hibernate를 사용하여 DDL을 자동으로 생성하는 방법을 알아보겠습니다.

1. Hibernate 설정 파일을 만듭니다.
   Hibernate를 사용하기 위해 먼저 설정 파일을 생성해야 합니다. 일반적으로 `hibernate.cfg.xml`과 같은 이름으로 저장됩니다.

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <hibernate-configuration xmlns="http://www.hibernate.org/xsd/hibernate-configuration"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.hibernate.org/xsd/hibernate-configuration hibernate-configuration-3.0.xsd">
       <session-factory>
           <!-- 데이터베이스 연결 설정 -->
           <property name="connection.driver_class">com.mysql.jdbc.Driver</property>
           <property name="connection.url">jdbc:mysql://localhost:3306/my_database</property>
           <property name="connection.username">username</property>
           <property name="connection.password">password</property>

           <!-- DDL 자동 생성 설정 -->
           <property name="hbm2ddl.auto">update</property>

           <!-- 매핑 파일 등록 -->
           <mapping class="com.example.model.User" /> <!-- 예시 매핑 파일 -->
       </session-factory>
   </hibernate-configuration>
   ```

   위의 설정 파일에서 중요한 부분은 `hbm2ddl.auto` 속성입니다. 이를 통해 Hibernate에게 DDL을 자동으로 생성하도록 지시할 수 있습니다. 자동 생성 옵션으로는 다음과 같은 값을 사용할 수 있습니다:
   - `create`: 매번 실행할 때마다 데이터베이스 스키마를 새로 만듭니다.
   - `update`: 이미 존재하는 테이블과 컬럼을 유지하면서 스키마를 변경합니다.
   - `create-drop`: 세션 팩토리를 생성하고 종료할 때마다 데이터베이스를 생성하고 삭제합니다. 개발 중에만 사용하는 것이 좋습니다.
   - `validate`: 현재의 매핑과 데이터베이스 스키마가 일치하는지 검증합니다. 스키마 변경은 발생하지 않습니다.

2. 매핑 파일 작성
   Hibernate는 객체와 데이터베이스 테이블 간의 매핑을 위해 매핑 파일을 사용합니다. 매핑 파일은 Hibernate 설정 파일에서 등록할 수 있습니다. 예시로 `User` 클래스를 매핑하는 매핑 파일을 아래와 같이 작성합니다.

   ```java
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE hibernate-mapping PUBLIC "-//Hibernate/Hibernate Mapping DTD 3.0//EN"
       "http://www.hibernate.org/dtd/hibernate-mapping-3.0.dtd">
   <hibernate-mapping>
       <class name="com.example.model.User" table="users">
           <id name="id" column="id" type="java.lang.Long">
               <generator class="native" />
           </id>
           <property name="name" column="name" type="java.lang.String" />

           <!-- 기타 필드와 매핑 설정 -->
       </class>
   </hibernate-mapping>
   ```

   위의 매핑 파일에서는 `User` 클래스를 `users` 테이블에 매핑하고 있습니다.

3. Hibernate 세션 팩토리 생성
   Hibernate를 사용하기 위해 세션 팩토리를 생성해야 합니다. 세션 팩토리는 Hibernate와 데이터베이스 간의 연결을 관리합니다.

   ```java
   Configuration configuration = new Configuration();
   configuration.configure("hibernate.cfg.xml");
   SessionFactory sessionFactory = configuration.buildSessionFactory();
   ```

   `hibernate.cfg.xml` 파일의 경로를 `configure()` 메소드에 전달하여 설정 파일을 읽습니다.

4. DDL 자동 생성 확인
   설정 파일을 올바르게 구성하고 세션 팩토리를 생성한 후, Hibernate가 DDL을 자동으로 생성하는지 확인할 수 있습니다. 이를 확인하기 위해 다음과 같은 코드를 실행할 수 있습니다.

   ```java
   Session session = sessionFactory.openSession();
   session.close();
   ```

   위의 코드를 실행하면 Hibernate가 설정된 DDL 자동 생성 옵션에 따라 데이터베이스 스키마를 생성하거나 업데이트할 것입니다.

위의 단계에 따라 Hibernate에서 DDL을 자동으로 생성할 수 있습니다. 이를 통해 객체 지향 애플리케이션을 쉽게 데이터베이스와 연동할 수 있게 됩니다.

더 자세한 내용은 Hibernate 문서(https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html)를 참조하시기 바랍니다.