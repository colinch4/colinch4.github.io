---
layout: post
title: "[java] Hibernate에서 다중 테이블 전략(Joined Table Strategy)과 단일 테이블 전략(Single Table Strategy)의 차이점은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

**다중 테이블 전략(Joined Table Strategy)**
다중 테이블 전략은 Hibernate에서 엔티티를 여러 테이블에 분산하여 저장하는 방법입니다. 이 전략을 사용하면 엔티티의 각 속성이 별도의 테이블에 저장됩니다.

테이블 간의 관계를 표현하기 위해 외래 키(Foreign Key)가 사용됩니다. 즉, 각 속성을 저장하기 위해 별도의 테이블을 만들고, 외래 키를 사용하여 엔티티와 속성 간의 관계를 유지합니다. 이렇게 함으로써 엔티티의 상속 구조를 유지하면서 데이터를 효율적으로 관리할 수 있습니다.

**단일 테이블 전략(Single Table Strategy)**
단일 테이블 전략은 Hibernate에서 엔티티의 모든 속성을 하나의 테이블에 저장하는 방법입니다. 이 전략을 사용하면 모든 엔티티 정보가 하나의 테이블에 집중되어 저장됩니다.

단일 테이블에는 엔티티의 모든 속성이 열(Column)로 표현됩니다. 상속 구조를 갖는 엔티티의 경우, 부모 엔티티와 자식 엔티티의 속성이 함께 저장되므로, 부모 엔티티와 자식 엔티티 간의 연관 관계를 명확하게 나타낼 수 있습니다.

**차이점**
다중 테이블 전략과 단일 테이블 전략의 주요 차이점은 데이터의 저장 방식입니다. 다중 테이블 전략은 엔티티의 각 속성을 별도의 테이블에 저장하므로, 데이터의 중복을 최소화할 수 있습니다. 반면에, 단일 테이블 전략은 모든 속성을 하나의 테이블에 저장하기 때문에, 데이터의 중복이 발생할 수 있습니다.

다중 테이블 전략은 객체의 상속 구조를 유지하면서 데이터를 관리하기에 적합합니다. 반면에, 단일 테이블 전략은 단순한 구조를 가진 객체의 데이터 관리에 유리합니다.

각 전략은 사용하는 시나리오에 따라 선택되어야 하며, 데이터 모델의 복잡성과 응용 프로그램의 요구 사항을 고려해야 합니다. References 쪽에 추가 자료를 참고하시기 바랍니다.

**References**
- [Hibernate Documentation - Inheritance Mapping Strategies](https://docs.jboss.org/hibernate/orm/5.4/userguide/html_single/Hibernate_User_Guide.html#inheritance)
- [Baeldung - Hibernate Inheritance Strategies](https://www.baeldung.com/hibernate-inheritance)