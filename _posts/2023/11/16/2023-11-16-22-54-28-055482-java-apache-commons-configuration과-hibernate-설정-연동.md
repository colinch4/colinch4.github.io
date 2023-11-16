---
layout: post
title: "[java] Java Apache Commons Configuration과 Hibernate 설정 연동"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 애플리케이션에서 설정 파일을 다루기 위한 유용한 라이브러리입니다. Hibernate은 데이터베이스와의 상호 작용을 관리하기 위한 Java ORM(Object-Relational Mapping) 프레임워크입니다. 이 두 가지를 함께 사용하면 효과적으로 설정 파일과 데이터베이스 설정을 관리할 수 있습니다.

## Apache Commons Configuration 설정

1. Apache Commons Configuration 라이브러리를 다운로드하고 프로젝트에 추가합니다. Maven 사용하는 경우, pom.xml 파일에 아래 종속성을 추가합니다.

   ```xml
   <dependency>
       <groupId>org.apache.commons</groupId>
       <artifactId>commons-configuration2</artifactId>
       <version>2.7</version>
   </dependency>
   ```

2. 설정 파일을 작성합니다. 일반적으로 XML 또는 properties 파일을 사용하며, 다양한 파일 형식을 지원합니다.

   ```xml
   <config>
       <database>
           <url>jdbc:mysql://localhost:3306/mydb</url>
           <username>root</username>
           <password>password</password>
       </database>
   </config>
   ```

3. Java 코드에서 Apache Commons Configuration 라이브러리를 사용하여 설정 파일을 읽어옵니다.

   ```java
   import org.apache.commons.configuration2.Configuration;
   import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
   import org.apache.commons.configuration2.builder.fluent.Parameters;

   // ...

   Parameters params = new Parameters();
   FileBasedConfigurationBuilder<XMLConfiguration> builder =
       new FileBasedConfigurationBuilder<>(XMLConfiguration.class)
           .configure(params.xml()
               .setFile(new File("config.xml")));

   Configuration config = builder.getConfiguration();
   String dbUrl = config.getString("config.database.url");
   String username = config.getString("config.database.username");
   String password = config.getString("config.database.password");
   ```

## Hibernate와 Apache Commons Configuration 설정 연동

1. Hibernate를 설정하기 위해 hibernate.cfg.xml 파일을 작성합니다.

   ```xml
   <hibernate-configuration>
       <session-factory>
           <!-- Hibernate 설정 -->
           <property name="hibernate.dialect">org.hibernate.dialect.MySQLDialect</property>
           <property name="hibernate.connection.driver_class">com.mysql.jdbc.Driver</property>
           ...
           <!-- 데이터베이스 연결 정보를 Apache Commons Configuration에서 가져옴-->
           <property name="hibernate.connection.url">${config.database.url}</property>
           <property name="hibernate.connection.username">${config.database.username}</property>
           <property name="hibernate.connection.password">${config.database.password}</property>
       </session-factory>
   </hibernate-configuration>
   ```

2. Java 코드에서 Hibernate를 초기화하고 설정 파일을 사용하여 데이터베이스 연결 정보를 가져옵니다.

   ```java
   import org.hibernate.SessionFactory;
   import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
   import org.hibernate.cfg.Configuration;

   // ...

   Configuration configuration = new Configuration().configure("hibernate.cfg.xml");
   StandardServiceRegistryBuilder builder = new StandardServiceRegistryBuilder()
       .applySettings(configuration.getProperties());

   SessionFactory sessionFactory = configuration.buildSessionFactory(builder.build());
   ```

Apache Commons Configuration을 사용하여 Hibernate와 설정 파일을 연동하면, 설정을 변경할 때마다 코드를 수정하지 않고도 데이터베이스 연결 정보를 쉽게 변경할 수 있습니다. 이를 통해 애플리케이션의 유연성과 유지 보수성을 향상시킬 수 있습니다.

참고 문서:
- [Apache Commons Configuration User Guide](https://commons.apache.org/proper/commons-configuration/userguide/)
- [Hibernate Official Documentation](https://hibernate.org/orm/documentation/5.5/)