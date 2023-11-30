---
layout: post
title: "[java] Hibernate Envers에서 Audited Entity의 변경 이력을 어떻게 저장하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

먼저, Hibernate Envers를 프로젝트에 추가해야 합니다. Maven 프로젝트의 경우, pom.xml 파일에 다음 의존성을 추가할 수 있습니다:

```xml
<dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-envers</artifactId>
    <version>5.4.x</version>
</dependency>
```

그리고, 변경 이력을 저장할 Entity 클래스에 `@Audited` 어노테이션을 추가해야 합니다. 이 어노테이션은 Hibernate에 해당 Entity의 변경 이력을 추적하도록 지시합니다.

```java
import org.hibernate.envers.Audited;

@Entity
@Audited
public class YourEntity {
    // Entity의 필드 및 메서드 정의
}
```

이제 Entity를 변경할 때 마다 Hibernate Envers는 변경 이력을 관리하는 동안 추가적인 테이블을 생성합니다. 변경 이력은 변경된 Entity의 이전 값과 현재 값을 저장하며, 변경된 필드는 어떻게 변경되었는지 추적합니다.

이력을 가져오기 위해서는 `AuditReader`를 사용해야 합니다. 예를 들어, 다음 코드는 `AuditReader`를 사용하여 `YourEntity`의 변경 이력을 가져오는 방법을 보여줍니다:

```java
@Autowired
private AuditReader auditReader;

public List<Number> getRevisionsOfEntity(Long entityId) {
    AuditQuery query = auditReader.createQuery().forRevisionsOfEntity(YourEntity.class, false, true);
    query.add(AuditEntity.id().eq(entityId));
    query.addOrder(AuditEntity.revisionNumber().desc());
    
    List<Object[]> revisions = query.getResultList();
    List<Number> revisionNumbers = new ArrayList<>();
    
    for(Object[] revision : revisions) {
        Number revisionNumber = (Number) revision[1];
        revisionNumbers.add(revisionNumber);
    }
    
    return revisionNumbers;
}
```

위의 코드는 특정 Entity의 변경 이력을 가져옵니다. `entityId` 매개 변수는 변경 이력을 가져올 Entity의 ID입니다. 결과로는 `revisionNumbers`라는 `List<Number>`가 반환되며, 이는 해당 Entity의 이력 번호 목록입니다.

이렇게 Hibernate Envers를 사용하면 Audited Entity의 변경 이력을 쉽게 추적하고 저장할 수 있습니다. 자세한 내용은 Hibernate Envers의 공식 문서를 참조하세요.

**참고 자료:**
- Hibernate Envers 공식 문서: [https://docs.jboss.org/envers/docs/](https://docs.jboss.org/envers/docs/)