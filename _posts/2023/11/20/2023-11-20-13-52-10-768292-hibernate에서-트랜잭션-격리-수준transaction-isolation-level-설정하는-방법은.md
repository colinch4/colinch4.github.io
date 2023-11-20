---
layout: post
title: "[java] Hibernate에서 트랜잭션 격리 수준(Transaction isolation level) 설정하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

```java
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.TransactionException;

// ...

Session session = HibernateUtil.getSessionFactory().openSession();
Transaction transaction = null;

try {
    transaction = session.beginTransaction();

    // 트랜잭션 격리 수준 설정
    transaction.setIsolationLevel(Connection.TRANSACTION_READ_COMMITTED);

    // 작업 수행

    session.getTransaction().commit();
} catch (TransactionException e) {
    if (transaction != null) {
        transaction.rollback();
    }
} finally {
    session.close();
}
```

위의 예제에서 `Connection.TRANSACTION_READ_COMMITTED`는 사용할 수 있는 여러 트랜잭션 격리 수준 중 하나입니다. 다른 격리 수준을 사용하고 싶다면 해당 상수를 바꾸면 됩니다.

추가적으로, 위의 예제에서는 Hibernate의 `Session`과 `Transaction` 객체를 사용하였습니다. 이는 Hibernate를 사용하여 데이터베이스 작업을 수행하기 위한 기본적인 방법입니다. Hibernate의 `SessionFactory`를 초기화하고 `Session`을 열어 해당 세션 내에서 트랜잭션을 시작하고 수행한 후 커밋하거나 롤백하는 방식입니다.

참고 자료:
- [Hibernate Documentation - Transactions and Concurrency](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#transactions)
- [Java Connection 객체의 트랜잭션 격리 수준 문서](https://docs.oracle.com/javase/8/docs/api/java/sql/Connection.html)