---
layout: post
title: "[java] Hibernate Envers에서 Audited Entity의 변경 이력을 어떻게 조회하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Audited Entity를 생성하기 위해서는 해당 엔티티 클래스에 `@Audited` 어노테이션을 추가해야 합니다. 이 어노테이션은 Envers에게 해당 엔티티의 변경 이력을 추적하도록 지시합니다. 예를 들면 다음과 같습니다:

```java
import org.hibernate.envers.Audited;

@Entity
@Audited
public class Product {
    // 엔티티의 필드와 메소드들...
}
```

이제 Audited Entity의 변경 이력을 조회하기 위해서는 `AuditReader` 인터페이스를 사용해야 합니다. 이 인터페이스는 Hibernate Envers의 핵심 API입니다. 예를 들어 특정 엔티티의 변경 이력을 조회하려면 다음과 같이 합니다:

```java
@Autowired
private EntityManager entityManager;

public List<Number> getRevisionsForProduct(Product product) {
    AuditReader auditReader = AuditReaderFactory.get(entityManager);
    List<Number> revisions = auditReader.getRevisions(Product.class, product.getId());
    return revisions;
}
```

위의 코드에서 `getRevisions()` 메서드는 `Product` 엔티티의 변경 이력을 조회하고 각 변경 이력의 식별자를 반환합니다. 이 식별자를 사용하여 변경 이력의 내용을 상세히 조회할 수도 있습니다.

Hibernate Envers를 사용하여 Audited Entity의 변경 이력을 조회하는 법에 대해 알아보았습니다. 자세한 내용은 [Hibernate Envers 공식 문서](https://docs.jboss.org/hibernate/envers/3.6/reference/en-US/html_single/#d0e170)를 참고하시기 바랍니다.