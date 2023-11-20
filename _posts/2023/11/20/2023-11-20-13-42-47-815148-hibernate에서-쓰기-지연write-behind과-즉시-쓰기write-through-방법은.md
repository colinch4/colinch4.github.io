---
layout: post
title: "[java] Hibernate에서 쓰기 지연(Write-behind)과 즉시 쓰기(Write-through) 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

1. 쓰기 지연(write-behind):
   - Hibernate의 기본 동작 방식입니다.
   - Session의 변경 내용을 모아서 적절한 시기에 데이터베이스에 쓰기 작업을 수행합니다.
   - 데이터베이스로의 쓰기 작업이 나중에 처리되므로, 여러 개의 변경 작업을 모아서 한 번에 수행하고자 할 때 유용합니다. 이렇게 함으로써 성능을 향상시킬 수 있습니다.
   - 하지만, 변경 내용이 데이터베이스에 반영되기 전까지는 해당 데이터를 조회할 수 없습니다.

2. 즉시 쓰기(write-through):
   - Hibernate에서는 쓰기 지연 대신 즉시 쓰기를 적용할 수도 있습니다.
   - Session의 변경 내용을 즉시 데이터베이스에 반영합니다.
   - 변경 작업이 즉시 완료되므로, 변경 내용을 즉시 확인 가능합니다.
   - 하지만, 쓰기 작업이 매번 수행되므로 성능이 저하될 수 있습니다.

Hibernate에서 쓰기 지연 방법을 사용하려면, 다음과 같이 설정 파일(hibernate.cfg.xml)에 설정 내용을 추가합니다:

```xml
<property name="hibernate.jdbc.batch_size">100</property>
<property name="hibernate.jdbc.order_updates">true</property>
```

이렇게 함으로써 쓰기 작업들을 일괄 처리하고, 성능을 향상시킬 수 있습니다.

반면에 즉시 쓰기 방법을 사용하려면, 다음과 같이 설정 파일에 설정 내용을 추가합니다:

```xml
<property name="hibernate.connection.release_mode">after_transaction</property>
```

이렇게 함으로써 모든 변경 작업이 트랜잭션 완료 후 즉시 데이터베이스에 적용됩니다.

이러한 Hibernate의 쓰기 지연과 즉시 쓰기 방법은 데이터베이스와의 상호작용 방법을 유연하게 조절할 수 있어 개발자에게 편의를 제공합니다.

참고 자료:
- Hibernate Documentation: [https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#writing](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#writing)