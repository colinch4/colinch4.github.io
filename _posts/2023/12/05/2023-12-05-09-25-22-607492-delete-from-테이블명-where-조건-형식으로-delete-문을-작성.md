---
layout: post
title: "[sql] DELETE FROM 테이블명 WHERE 조건; 형식으로 DELETE 문을 작성"
description: " "
date: 2023-12-05
tags: [sql]
comments: true
share: true
---

```sql
DELETE FROM 테이블명 WHERE 조건;
```

위의 문법에서 "테이블명"은 삭제할 레코드가 있는 테이블의 이름을 지정하고, "조건"은 삭제할 레코드를 선택하기 위한 조건식입니다.

예를 들어, "Customers" 테이블에서 고객 ID가 100인 레코드를 삭제하고 싶다면 다음과 같이 DELETE 문을 작성할 수 있습니다:

```sql
DELETE FROM Customers WHERE CustomerID = 100;
```

위의 DELETE 문을 실행하면 "Customers" 테이블에서 CustomerID가 100인 레코드가 삭제됩니다.

조건은 여러 개의 조건식을 조합하여 지정할 수도 있습니다. 예를 들어, CustomerID가 100이고 City가 'Seoul'인 레코드를 삭제하려면 다음과 같이 DELETE 문을 작성할 수 있습니다:

```sql
DELETE FROM Customers WHERE CustomerID = 100 AND City = 'Seoul';
```

이렇게 DELETE 문을 사용하면 필요한 레코드를 삭제할 수 있습니다.

참고문헌:
- [W3Schools - SQL DELETE 문](https://www.w3schools.com/sql/sql_delete.asp)
- [MySQL Documentation - DELETE 문](https://dev.mysql.com/doc/refman/8.0/en/delete.html)