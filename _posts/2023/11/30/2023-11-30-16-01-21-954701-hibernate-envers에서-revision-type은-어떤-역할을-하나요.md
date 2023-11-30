---
layout: post
title: "[java] Hibernate Envers에서 Revision Type은 어떤 역할을 하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

- ADD: 새로운 엔티티가 추가됨을 나타냅니다.
- MOD: 기존 엔티티가 수정됨을 나타냅니다.
- DEL: 엔티티가 삭제됨을 나타냅니다.

Revision Type은 각각의 변경 이력 엔티티에 해당하는 타입을 저장하고 조회할 때 사용됩니다. 이를 통해 객체의 변경 이력을 추적하고 분석할 수 있습니다. 예를 들어, 어떤 객체의 변경 이력을 조회하기 위해서는 Revision Type 값이 MOD인 엔티티들을 조회하면 됩니다.

이러한 Revision Type은 Hibernate Envers의 중요한 기능 중 하나이며, 객체의 변경 이력을 관리하고 추적하는 데 도움을 줍니다. Hibernate Envers를 사용하여 애플리케이션의 데이터 접근 계층에서 변경 이력을 관리하고 분석할 수 있습니다.

(참고: [Hibernate Envers 공식 문서](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#envers))