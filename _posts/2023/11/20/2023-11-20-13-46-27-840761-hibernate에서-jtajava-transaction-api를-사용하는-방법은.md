---
layout: post
title: "[java] Hibernate에서 JTA(Java Transaction API)를 사용하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

먼저, JTA를 사용하기 위해서는 JTA 트랜잭션 관리자를 구성해야 합니다. 일반적으로 JEE 컨테이너에서 제공하는 JTA 트랜잭션 관리자를 사용하게 됩니다. 

Hibernate에서 JTA를 사용하려면 persistence.xml 파일에 아래와 같이 JTA 트랜잭션 관리자를 구성해야 합니다.

```xml
<persistence-unit name="myPersistenceUnit" transaction-type="JTA">
    <jta-data-source>java:/comp/env/jdbc/myDataSource</jta-data-source>
    <!-- other configuration properties -->
</persistence-unit>
```

여기에서 `transaction-type` 속성은 "JTA"로 설정해야 JTA 트랜잭션 관리자를 사용할 수 있습니다.

또한, Hibernate에서 JTA 트랜잭션 관리자를 사용하기 위해서는 사용하고자 하는 JTA 트랜잭션 관리자에 대한 구현체를 추가해야 합니다. 대부분의 JEE 컨테이너에서는 JTA 트랜잭션 관리자를 제공하므로 별도의 구현체를 추가할 필요는 없을 것입니다.

마지막으로, 트랜잭션을 시작하고 커밋 또는 롤백하는 코드를 작성해야 합니다. 

```java
UserTransaction userTransaction = (UserTransaction) new InitialContext().lookup("java:comp/UserTransaction");
userTransaction.begin();

// Hibernate 세션 획득
Session session = sessionFactory.getCurrentSession();

try {
    // 작업 수행

    // 커밋
    userTransaction.commit();
} catch (Exception e) {
    // 롤백
    userTransaction.rollback();
}
```

위의 예제에서는 `UserTransaction`을 사용하여 트랜잭션을 시작하고 커밋 또는 롤백하는 방법을 보여줍니다. `sessionFactory`는 Hibernate의 세션 팩토리입니다.

이렇게 구성한 Hibernate의 JTA 트랜잭션 관리자를 사용하면, JTA를 통해 분산 트랜잭션을 관리할 수 있습니다.

더 자세한 내용은 Hibernate 공식 문서나 관련 자료를 참조하시기 바랍니다.

**참고 자료:**
- Hibernate Documentation: [https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html)