---
layout: post
title: "[java] Hibernate Envers에서 Revision Number는 어떤 역할을 하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Hibernate Envers는 객체의 변경 이력을 관리하는 라이브러리입니다. Envers를 사용하면 데이터베이스의 객체에 대한 모든 변경 사항을 추적하고 조회할 수 있습니다. 

Revision Number는 Envers에서 변경 이력을 식별하기 위한 고유한 식별자입니다. 즉, Revision Number는 순차적으로 증가하는 값으로서, 각각의 변경 작업마다 고유한 번호가 부여됩니다. 이를 통해 변경 이력을 시간 순으로 정렬하고, 특정 Revision Number를 이용해 특정 변경 이력을 조회할 수 있습니다.

Envers를 사용하여 Revision Number를 확인하려면, `@RevisionNumber` 어노테이션을 사용하여 엔티티 클래스에 해당 필드를 추가해야 합니다. 아래의 예시를 참고해주세요.

```java
@Entity
@Audited
public class Customer {
    @Id
    private Long id;
    
    private String name;
    
    @RevisionNumber
    private Long revisionNumber;
    
    // getters and setters
}
```

위의 예시에서 `@RevisionNumber` 어노테이션이 추가된 `revisionNumber` 필드는 Envers에 의해 자동으로 채워집니다. 이를 통해 변경 이력을 조회할 때 Revision Number를 사용할 수 있습니다.

참고로 Revision Number는 매번 변경할 때마다 증가하기 때문에, Revision Number를 통해 어떤 수정 작업이 언제 이루어졌는지를 파악할 수 있습니다.

이외에도 Envers는 다양한 기능을 제공하며, Revision Number를 기반으로 변경 이력을 조회하는 방법을 유연하게 지원합니다. 따라서 Hibernate Envers를 사용하면 개발자는 데이터베이스의 객체 변경 이력을 효율적으로 관리할 수 있습니다. 

더 자세한 내용은 Hibernate Envers 공식 문서를 참고하세요. 

- Hibernate Envers 공식 문서: [https://docs.jboss.org/envers/](https://docs.jboss.org/envers/)