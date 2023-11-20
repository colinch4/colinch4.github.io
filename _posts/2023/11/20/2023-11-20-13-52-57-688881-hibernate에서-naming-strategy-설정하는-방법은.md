---
layout: post
title: "[java] Hibernate에서 Naming Strategy 설정하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

1. Hibernate Configuration 파일 작성
   먼저 Hibernate의 Configuration 파일에 Naming Strategy를 설정할 필요가 있습니다. Hibernate의 Configuration은 일반적으로 `hibernate.cfg.xml` 파일을 사용합니다. 해당 파일을 열어서 아래와 같이 Naming Strategy 설정을 추가합니다.

  ```xml
  <hibernate-configuration>
    <session-factory>
      <!-- 기존의 설정들 -->
      
      <!-- Naming Strategy 설정 -->
      <property name="hibernate.ejb.naming_strategy">[네이밍_스트래티지_클래스_이름]</property>
    </session-factory>
  </hibernate-configuration>
  ```

   `[네이밍_스트래티지_클래스_이름]` 부분에는 사용할 Naming Strategy 클래스의 이름을 작성해야 합니다.

2. Naming Strategy 클래스 작성
   Naming Strategy 클래스는 Hibernate의 `org.hibernate.cfg.DefaultNamingStrategy` 클래스나 `org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl` 클래스를 상속하여 작성할 수 있습니다. 

   예를 들어, 커스텀한 네이밍 규칙을 사용하려면 다음과 같이 클래스를 작성할 수 있습니다.

   ```java
   public class CustomNamingStrategy extends org.hibernate.cfg.DefaultNamingStrategy {
       @Override
       public String tableName(String tableName) {
           // 테이블 이름 네이밍 규칙 구현
           // 예: "user" 테이블의 경우 "tbl_user"로 변경
           return "tbl_" + tableName.toLowerCase();
       }

       @Override
       public String columnName(String columnName) {
           // 컬럼 이름 네이밍 규칙 구현
           // 예: "firstName" 컬럼의 경우 "first_name"으로 변경
           return CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, columnName);
       }
   }
   ```

   네이밍 규칙에 따라 `tableName(String tableName)` 메서드와 `columnName(String columnName)` 메서드를 오버라이딩하여 구현합니다.

3. 사용자 정의 Naming Strategy 설정
   Hibernate Configuration 파일에서 설정한 `[네이밍_스트래티지_클래스_이름]` 부분에는 사용자가 작성한 Naming Strategy 클래스의 이름을 작성합니다.

   ```xml
   <property name="hibernate.ejb.naming_strategy">com.example.CustomNamingStrategy</property>
   ```

   여기서 `com.example.CustomNamingStrategy`는 사용자가 작성한 Naming Strategy 클래스의 패키지 경로와 클래스 이름입니다.

Hibernate의 Naming Strategy 설정 방법을 알아보았습니다. Naming Strategy는 데이터베이스와의 일관된 네이밍 규칙을 유지하고, 개발자의 작업을 더욱 효율적으로 만들어줍니다. 필요에 따라 적절한 네이밍 규칙을 구현하여 Hibernate의 Naming Strategy를 사용해보세요.

참고 자료:
- Hibernate 공식 문서 - Naming Strategy: [https://docs.jboss.org/hibernate/orm/5.6/userguide/html_single/Hibernate_User_Guide.html#naming-strategy](https://docs.jboss.org/hibernate/orm/5.6/userguide/html_single/Hibernate_User_Guide.html#naming-strategy)
- Hibernate 공식 GitHub - DefaultNamingStrategy: [https://github.com/hibernate/hibernate-orm/blob/main/hibernate-core/src/main/java/org/hibernate/cfg/DefaultNamingStrategy.java](https://github.com/hibernate/hibernate-orm/blob/main/hibernate-core/src/main/java/org/hibernate/cfg/DefaultNamingStrategy.java)
- Hibernate 공식 GitHub - PhysicalNamingStrategyStandardImpl: [https://github.com/hibernate/hibernate-orm/blob/main/hibernate-core/src/main/java/org/hibernate/boot/model/naming/PhysicalNamingStrategyStandardImpl.java](https://github.com/hibernate/hibernate-orm/blob/main/hibernate-core/src/main/java/org/hibernate/boot/model/naming/PhysicalNamingStrategyStandardImpl.java)