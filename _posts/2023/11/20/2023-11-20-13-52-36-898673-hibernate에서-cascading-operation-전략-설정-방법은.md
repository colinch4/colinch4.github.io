---
layout: post
title: "[java] Hibernate에서 Cascading operation 전략 설정 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

전략을 설정하는 방법은 hibernate.cfg.xml 파일에서 다음과 같이 설정할 수 있습니다:

```xml
<hibernate-configuration>
    <session-factory>
        ...
        <mapping class="com.example.ParentEntity"/>
        ...
        <property name="hibernate.hbm2ddl.auto">update</property>
        <property name="hibernate.c3p0.min_size">5</property>
        ...
        <property name="hibernate.hbm2ddl.auto">create</property>
        <property name="hibernate.c3p0.max_size">20</property>
        ...
        <property name="hibernate.hbm2ddl.auto">update</property>
        <property name="hibernate.c3p0.timeout">300</property>
        ...
    </session-factory>
</hibernate-configuration>
```

위의 예제에서 `ParentEntity`는 부모 엔티티의 클래스를 나타냅니다. `ParentEntity`와 관계된 자식 엔티티들에 대해서도 Cascading operation이 적용되며, 설정된 옵션에 따라 데이터 변경 작업이 전파됩니다.

Hibernate에서 제공하는 Cascading operation 전략은 다양하며, 주로 사용되는 전략은 아래와 같습니다:

- `ALL`: 모든 연관 엔티티에 대해 Cascade 작업을 수행합니다.
- `PERSIST`: 새로운 부모 엔티티가 추가될 때 자식 엔티티도 함께 추가됩니다.
- `MERGE`: 부모 엔티티가 업데이트되면 자식 엔티티도 함께 업데이트됩니다.
- `REMOVE`: 부모 엔티티가 삭제되면 자식 엔티티도 함께 삭제됩니다.

각 연관 관계 필드에 대해서도 개별적으로 Cascade annotation을 설정하여 특정한 전략을 적용할 수 있습니다. 각각의 전략에 대한 자세한 내용은 [Hibernate documentation](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#associations)을 참고하시기 바랍니다.