---
layout: post
title: "[java] Hibernate의 초과로딩(N+1 Selects Problem) 이슈를 해결하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

1. Fetch Join 사용: Fetch Join은 JPQL이나 Criteria API에서 사용할 수 있는 방법으로, 연관된 엔티티를 한 번에 로드하는 것입니다. 이를 통해 N+1 쿼리 문제를 해결할 수 있습니다. 예를 들어, 다음과 같이 사용할 수 있습니다.

```java
SELECT e FROM Entity e JOIN FETCH e.association
```

2. Batch Size 설정: Hibernate는 `@OneToMany` 나 `@ManyToMany` 관계에 대해 `@BatchSize` 애노테이션을 제공합니다. 이를 통해 한 번에 지정된 수의 엔티티를 로드할 수 있습니다.

```java
@BatchSize(size = 10)
@OneToMany(mappedBy = "association")
private List<ChildEntity> children;
```

3. Eager 로딩 사용: Hibernate는 기본적으로 연관된 엔티티를 지연로딩(Lazy loading)하도록 설정되어 있습니다. 이를 eager 로딩으로 변경하여 N+1 문제를 예방할 수 있습니다. 그러나, 이 방법은 데이터를 불필요하게 로드할 수 있으므로 신중하게 사용해야 합니다.

```java
@ManyToOne(fetch = FetchType.EAGER)
private AssociationEntity association;
```

이외에도 Hibernate가 제공하는 다양한 옵션과 전략을 사용하여 N+1 문제를 해결할 수 있습니다. 이를 위해 Hibernate 문서를 참고하시기 바랍니다.

참고 문서: [Hibernate Documentation](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#fetching-strategies)