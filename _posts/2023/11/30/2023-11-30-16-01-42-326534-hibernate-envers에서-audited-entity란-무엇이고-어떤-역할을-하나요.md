---
layout: post
title: "[java] Hibernate Envers에서 Audited Entity란 무엇이고 어떤 역할을 하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Hibernate Envers는 Hibernate ORM과 함께 사용되는 확장 기능입니다. Envers는 데이터베이스의 변경 내역을 기록하고 추적할 수 있도록 도와주는 도구입니다. 이러한 변경 내역을 기록하는 대상을 Audited Entity라고 합니다.

Audited Entity는 데이터베이스의 특정 테이블과 매핑되는 Hibernate 엔티티입니다. Hibernate Envers를 사용하면 이러한 Audited Entity의 변경 내역을 추적하고 기록할 수 있습니다. Audited Entity에 대한 변경 내역은 Envers가 제공하는 기능을 통해 쉽게 조회 및 관리할 수 있습니다.

# Audited Entity의 역할은 무엇인가요?

Audited Entity의 주요 역할은 다음과 같습니다:
- 데이터베이스의 변경 내역을 추적하고 기록합니다.
- 변경 내역을 조회하여 이전 상태와 현재 상태를 비교하고 분석할 수 있습니다.
- 히스토리 기능을 제공하여 데이터의 변경 이력을 관리할 수 있습니다.
- 보안 및 규정 준수를 위해 중요한 데이터 변경을 검증하고 추적할 수 있습니다.
- 각 변경 내역에 대한 정보를 기록하여 추후 분석이나 오류 디버깅에 활용할 수 있습니다.

Audited Entity를 사용하면 데이터베이스의 변경 내역을 쉽게 관리하고 분석할 수 있어서 개발자들에게 많은 도움이 됩니다.

```java
@Entity
@Audited
@Table(name = "product")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "name")
    private String name;
    
    @Column(name = "price")
    private BigDecimal price;
    
    // Getters and Setters
}
```

위의 예시는 Audited Entity를 만드는 방법을 보여줍니다. `@Audited` 어노테이션을 통해 변경 내역을 기록하도록 지정하고, `@Table` 어노테이션을 통해 테이블과 매핑합니다. 엔티티 클래스에 `@Audited` 어노테이션을 추가하고, 필요한 열에 `@Column` 어노테이션을 이용하여 매핑합니다.

더 자세한 내용은 [Hibernate Envers 공식 문서](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#envers)를 참고하시기 바랍니다.