---
layout: post
title: "[java] Hibernate Envers를 사용하여 여러 개의 Audited Entity를 동시에 변경 이력을 관리할 수 있나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Audited Entity란 변경 이력을 추적하고 저장하는 엔티티를 말합니다. Envers는 이러한 Audited Entity의 변경 이력을 자동으로 기록하여 관리할 수 있습니다.

다음은 여러 개의 Audited Entity를 동시에 변경 이력을 관리하는 방법입니다:

1. @Audited 애노테이션 사용: Audited Entity 클래스 위에 @Audited 애노테이션을 추가합니다. 이렇게 되면 해당 엔티티의 변경 내용이 자동으로 추적되고 Envers에 의해 변경 이력으로 관리됩니다.

```java
@Entity
@Audited
public class MyAuditedEntity {
    // ...
}
```

2. Hibernate Session 사용: Hibernate Session을 사용하여 여러 개의 Audited Entity를 동시에 변경하면, Envers는 자동으로 변경 이력을 관리합니다.

```java
Session session = sessionFactory.openSession();
Transaction tx = session.beginTransaction();

// Audited Entity 변경
MyAuditedEntity entity1 = session.get(MyAuditedEntity.class, id1);
entity1.setName("New Name");

MyAuditedEntity entity2 = session.get(MyAuditedEntity.class, id2);
entity2.setValue(100);

tx.commit();
session.close();
```

3. 트랜잭션 롤백: 만약 여러 개의 Audited Entity의 변경을 롤백해야한다면, Hibernate의 트랜잭션 롤백 기능을 사용하여 변경 이력을 관리할 수 있습니다.

```java
Session session = sessionFactory.openSession();
Transaction tx = session.beginTransaction();

// Audited Entity 변경
MyAuditedEntity entity1 = session.get(MyAuditedEntity.class, id1);
entity1.setName("New Name");

MyAuditedEntity entity2 = session.get(MyAuditedEntity.class, id2);
entity2.setValue(100);

tx.rollback();
session.close();
```

이렇게 하면 Hibernate Envers를 사용하여 여러 개의 Audited Entity를 동시에 변경 이력을 관리할 수 있습니다.