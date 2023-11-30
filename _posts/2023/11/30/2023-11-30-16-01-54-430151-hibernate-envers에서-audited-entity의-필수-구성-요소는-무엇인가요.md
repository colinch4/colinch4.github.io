---
layout: post
title: "[java] Hibernate Envers에서 Audited Entity의 필수 구성 요소는 무엇인가요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

1. 엔티티 클래스에 @Audited 애노테이션을 추가해야 합니다. 이 애노테이션은 Envers가 해당 엔티티를 추적하도록 지시합니다.
```java
@Entity
@Audited
public class YourEntity {
    // 엔티티 속성과 메서드
}
```

2. 변경 이력을 추적하려는 엔티티 속성을 @Audited 애노테이션으로 표시해야 합니다. 이 애노테이션은 해당 속성이 변경될 때마다 Envers가 이력을 남기도록 합니다.
```java
@Entity
@Audited
public class YourEntity {
    @Id
    private Long id;

    @Audited
    private String name;

    // 다른 속성과 메서드
}
```

3. Envers가 변경 이력을 저장하는 테이블을 생성할 수 있도록 hibernate.envers.store_data_at_delete 속성 값을 true로 설정해야 합니다. 이렇게 하면 엔티티가 삭제될 때마다 해당 이력도 저장됩니다.
```properties
hibernate.envers.store_data_at_delete=true
```

Audited Entity의 필수 구성 요소는 위에서 소개한 것과 같습니다. Hibernate Envers를 사용하여 엔티티의 변경 이력을 추적하려면 이러한 요소를 올바르게 구성해야 합니다.