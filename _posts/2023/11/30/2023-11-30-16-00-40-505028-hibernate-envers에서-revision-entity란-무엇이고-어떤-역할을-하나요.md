---
layout: post
title: "[java] Hibernate Envers에서 Revision Entity란 무엇이고 어떤 역할을 하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Hibernate Envers는 Hibernate를 이용하여 데이터베이스의 변경 이력을 관리하는 라이브러리입니다. Hibernate Envers의 중요한 개념 중 하나는 Revision Entity입니다.

Revision Entity는 Envers가 생성하는 변경 이력 테이블과 엔티티 테이블 간의 연결 역할을 담당합니다. Envers는 각 엔티티의 변경 이력을 추적하기 위해 이 변경 이력 테이블을 생성합니다. 변경 이력 테이블에는 엔티티의 식별자, 변경된 속성의 값, 변경한 사용자 등의 정보가 저장됩니다.

Revision Entity는 실제 엔티티 클래스와는 별개로 정의되어야 합니다. 이는 엔티티의 변경 이력을 추적하기 위한 테이블이므로 Envers에 의해 생성 및 관리되기 때문입니다. Revision Entity는 @RevisionEntity 애노테이션을 이용하여 정의됩니다.

Revision Entity는 일반적으로 엔티티 클래스와 비슷한 형태를 가집니다. 엔티티의 변경자, 변경 일자, 변경 시점 등의 정보를 저장하는 필드를 포함할 수 있습니다. 또한, 필요에 따라서 커스텀한 필드를 추가하여 변경 이력에 대한 추가 정보를 저장할 수도 있습니다.

Revision Entity의 역할은 주로 변경 이력의 관리와 추적입니다. Envers는 엔티티의 변경 시점마다 Revision Entity를 생성하고 변경 이력 테이블에 해당 변경 정보를 저장합니다. 이를 통해 개발자는 엔티티의 변경 이력을 쉽게 조회하고 관리할 수 있습니다.

이렇게 Revision Entity를 사용하면 데이터베이스의 변경 이력을 보다 효율적으로 관리할 수 있으며, 엔티티의 변경 이력을 추적하여 필요한 경우에 손쉽게 조회할 수 있습니다.

참고 자료:
- Hibernate Envers 공식 문서: [https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#envers-revisionlog](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#envers-revisionlog)