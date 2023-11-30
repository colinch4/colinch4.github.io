---
layout: post
title: "[java] Hibernate Envers에서 Audited Entity의 변경 이력을 어떻게 복원하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Hibernate Envers는 Hibernate를 기반으로 한 객체-관계 매핑(ORM) 라이브러리입니다. 이는 애플리케이션에서 데이터의 변경 이력을 추적하고 복원하는 데 사용될 수 있습니다. 

Audited Entity(감사 엔티티)는 Envers에 의해 변경 이력을 기록하는 대상입니다. Audited Entity의 변경 이력을 복원하려면 다음 단계를 따를 수 있습니다.

### 1. Envers 설정 추가하기

먼저, Hibernate 설정 파일에 Envers를 활성화하도록 설정해야 합니다. 이를 위해 `hibernate.cfg.xml` 파일에 다음 내용을 추가합니다:

```xml
<property name="org.hibernate.envers.audit_table_suffix" value="_AUD" />
<property name="org.hibernate.envers.revision_field_name" value="REV" />
<property name="org.hibernate.envers.revision_type_field_name" value="REVTYPE" />
<property name="org.hibernate.envers.use_revision_entity_with_native_id" value="true" />
```

### 2. Audited Entity로 변경 이력 기록하기

다음으로, Audited Entity의 변경 이력을 기록할 수 있도록 해당 엔티티 클래스에 `@Audited` 어노테이션을 추가해야 합니다. 예를 들어, 다음과 같이 사용할 수 있습니다:

```java
@Entity
@Audited
public class Customer {
    // 엔티티의 필드 및 메소드 정의
}
```

### 3. 변경 이력 복원하기

Envers는 변경 이력을 조회하고 해당 일자의 데이터를 복원하는 메소드를 제공합니다. 예를 들어, 다음 코드는 특정 일자의 Audited Entity를 조회하는 방법을 보여줍니다:

```java
Session session = sessionFactory.getCurrentSession();
AuditReader auditReader = AuditReaderFactory.get(session);

// 변경 이력 조회
List<Number> revisions = auditReader.getRevisions(Customer.class, customerId);
for (Number revision : revisions) {
    Customer customer = auditReader.find(Customer.class, customerId, revision);
    // 복원된 데이터로 작업 수행
}
```

위의 코드에서 `customerId`는 조회할 Audited Entity의 식별자입니다. `auditReader.getRevisions()` 메소드를 사용하여 변경 이력을 검색하고, `auditReader.find()` 메소드를 사용하여 특정 일자의 Audited Entity를 가져올 수 있습니다.

이를 통해 변경 이력을 복원하고 이전 상태의 데이터를 다시 가져와서 작업할 수 있습니다.

---

참고 문서: [Hibernate Envers Documentation](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#envers)