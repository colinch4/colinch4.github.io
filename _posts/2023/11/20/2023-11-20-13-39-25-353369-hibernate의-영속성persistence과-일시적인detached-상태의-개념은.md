---
layout: post
title: "[java] Hibernate의 영속성(Persistence)과 일시적인(Detached) 상태의 개념은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

1. 영속성 (Persistence) 상태
영속성 상태란 Hibernate 세션에 의해 관리되는 객체의 상태입니다. 객체가 영속성 상태에 있다면 Hibernate는 해당 객체를 데이터베이스에 저장하거나 수정, 삭제할 수 있습니다. 객체가 영속성 상태로 전환되기 위해서는 Hibernate 세션을 통해 객체를 저장하거나 로드한 후에 해당 객체를 변경하면 됩니다. 변경된 객체는 Hibernate의 변경 감지 메커니즘에 의해 데이터베이스에 자동으로 반영됩니다. 

2. 일시적인 (Detached) 상태
일시적인 상태란 이미 데이터베이스에서 조회된 객체가 Hibernate 세션과의 연결이 끊어진 상태를 말합니다. 일시적인 상태인 객체는 Hibernate 세션의 관리 및 감시를 받지 않으며, 데이터베이스에 변경을 자동으로 반영하지 않습니다. 일시적인 상태에서는 필요한 경우 객체의 상태를 변경하여 데이터베이스와 동기화할 수 있습니다. 객체를 다시 영속성 상태로 전환하기 위해서는 Hibernate 세션을 통해 해당 객체를 다시 저장하거나 로드해야 합니다.

Hibernate의 영속성과 일시적인 상태 개념을 통해 개발자는 객체의 생명주기와 데이터베이스와의 동기화를 쉽게 관리할 수 있습니다.

주의: 위의 내용은 Hibernate 5.x에서의 개념을 기준으로 작성된 것입니다. 버전에 따라 상세 내용이 약간 다를 수 있으므로 공식 문서나 다른 참고 자료를 참조하시기를 권장합니다.

참고 자료:
- Hibernate 공식 문서: https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#entity-state-overview