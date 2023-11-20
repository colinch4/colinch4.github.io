---
layout: post
title: "[java] Hibernate에서 지연 로딩(Lazy loading)과 즉시 로딩(Eager loading)의 차이점은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

지연 로딩(Lazy loading)은 특정 객체의 연관된 데이터를 실제로 필요한 시점에 데이터베이스에서 로드하는 방식입니다. 연관된 데이터가 실제로 필요하지 않은 경우, 해당 데이터를 로드하지 않습니다. 예를 들어, `get()` 메서드를 호출하여 객체를 가져올 때, 연관된 객체들은 로드되지 않습니다. 대신에, 연관된 객체들의 프록시(Proxy) 객체를 생성하여 필요한 시점에 데이터베이스에서 로드됩니다. 이 방식은 초기 로드 시간을 줄이고 성능을 향상시킬 수 있지만, 객체를 사용할 때마다 데이터베이스에 접근하는 오버헤드가 발생할 수 있습니다.

반면에, 즉시 로딩(Eager loading)은 객체를 로드할 때 연관된 모든 데이터를 한 번에 로드하는 방식입니다. 예를 들어, `fetch = FetchType.EAGER` 속성을 사용하여 모든 연관된 객체를 한 번에 로드하도록 설정할 수 있습니다. 이 방식은 객체를 사용하는 과정에서 추가적인 데이터베이스 접근을 필요로 하지 않으므로 오버헤드는 줄어들지만, 초기 로드 시간과 성능에 영향을 줄 수 있습니다.

따라서, 지연 로딩은 필요한 시점에 데이터를 로드하여 성능을 향상시킬 수 있지만, 데이터베이스에 접근하는 오버헤드가 발생할 수 있습니다. 즉시 로딩은 초기 로드 시간을 증가시킬 수 있지만, 객체를 사용하는 과정에서 추가적인 데이터베이스 접근이 필요하지 않으므로 성능이 개선될 수 있습니다. 개발자는 프로젝트의 요구사항에 맞게 지연 로딩과 즉시 로딩을 사용해야 합니다.

**참고 자료:**
- Hibernate Documentation: [Fetching strategies](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#fetching-strategies)