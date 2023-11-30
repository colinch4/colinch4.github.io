---
layout: post
title: "[java] Hibernate Envers에서 Revision Timestamp는 어떤 역할을 하나요?"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Hibernate Envers는 Hibernate 프레임워크의 일부로서, 변경 이력을 추적하고 조회하는 데 사용하는 도구입니다. Envers는 데이터베이스의 테이블에 변경 로그를 저장하여 이전 버전의 엔티티 상태를 검색할 수 있게 해줍니다.

Revision Timestamp는 Envers에서 변경 로그를 기록할 때 사용되는 열 중 하나인데, 이 열은 각 엔티티의 변경 시간을 나타냅니다. 

Revision Timestamp를 사용하면 다음과 같은 기능을 수행할 수 있습니다:

- 변경 이력의 시간 기반 조회: 특정 시간 이후에 발생한 변경 이력만 검색하는 등의 시간에 따른 변경 이력 조회가 가능합니다.
- 변경 이력의 정확한 순서 조회: 같은 Revision Timestamp를 가진 변경 이력의 경우, Timestamp의 순서에 따라 이력을 정확하게 추적할 수 있습니다.
- 변경 이력의 시간별 분석: 일자별, 월별, 연도별로 변경 이력을 분석하고 통계를 내는 등의 작업을 수행할 수 있습니다.

하지만 Revision Timestamp는 필수적인 열은 아니며, 사용자의 요구 사항에 따라 Envers를 구성할 수 있습니다. 예를 들어, 사용자는 변경 이력을 추적하면서 시간 정보를 저장하지 않을 수도 있습니다. 

자세한 내용은 Hibernate Envers 공식 문서를 참조하시면 됩니다.

- Hibernate Envers 공식 문서: [https://docs.jboss.org/hibernate/orm/5.4/userguide/html_single/Hibernate_User_Guide.html#envers](https://docs.jboss.org/hibernate/orm/5.4/userguide/html_single/Hibernate_User_Guide.html#envers)