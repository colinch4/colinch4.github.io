---
layout: post
title: "[java] Hibernate Envers에서 Audited Entity의 변경 이력을 어떻게 추적하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Audited Entity는 변경 이력을 추적하고자 하는 엔티티 클래스를 의미합니다. Envers를 사용하기 위해서는 먼저 해당 엔티티를 Audited Entity로 지정해야 합니다. 이를 위해 @Audited 어노테이션을 사용합니다.

예를 들어, 다음은 User 엔티티 클래스를 Audited Entity로 지정하는 예제입니다:

```java
@Entity
@Audited
public class User {
    // 엔티티 필드와 메소드들
}
```

위의 예제에서 User 클래스는 @Audited 어노테이션을 사용하여 Audited Entity로 지정되었습니다.

이후 데이터베이스에서 Audited Entity의 변경 이력을 추적하고자 할 때, 다음과 같이 Envers를 사용합니다:

```java
AuditReader auditReader = AuditReaderFactory.get(entityManager);

List<Number> revisions = auditReader.getRevisions(User.class, userId);

for (Number revision : revisions) {
    User revisionEntity = auditReader.find(User.class, userId, revision);
    // 변경 이력 처리 로직
    // revisionEntity를 사용하여 변경 이력 정보를 추출 및 처리
}
```

위의 예제에서는 AuditReader 인터페이스를 사용하여 변경 이력을 추적합니다. getRevisions 메소드를 사용하여 특정 Audited Entity의 모든 변경 이력 버전을 조회하고, 이후 find 메소드를 사용하여 특정 버전의 Audited Entity를 조회할 수 있습니다. 이렇게 조회한 버전의 Audited Entity를 사용하여 변경 이력 정보를 추출하고 처리할 수 있습니다.

이와 같은 방법으로 Hibernate Envers를 사용하여 Audited Entity의 변경 이력을 추적할 수 있습니다.

더 자세한 내용은 Hibernate Envers의 공식 문서를 참조하시기 바랍니다.

참고 문서: [Hibernate Envers 공식 문서](https://hibernate.org/orm/envers/)