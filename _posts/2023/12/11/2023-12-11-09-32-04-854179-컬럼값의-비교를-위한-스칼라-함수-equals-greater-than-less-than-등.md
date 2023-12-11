---
layout: post
title: "[sql] 컬럼값의 비교를 위한 스칼라 함수 (EQUALS, GREATER THAN, LESS THAN 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

데이터베이스 쿼리에서는 현재 값을 비교하거나 다른 값과 비교해야 하는 경우가 많습니다. 이를 위해 SQL에서는 **스칼라 함수**를 사용하여 컬럼값의 비교를 수행할 수 있습니다.

### **EQUALS (같음) 비교**

특정 값과 같은지 확인하려면 **EQUALS(=)** 연산자를 사용합니다. 

예를 들어, 다음 쿼리는 `first_name` 컬럼값이 "John"인 행을 반환합니다.
```sql
SELECT *
FROM employees
WHERE first_name = 'John';
```

### **GREATER THAN (초과) 비교**

특정 값보다 큰지 확인하려면 **GREATER THAN(>)** 연산자를 사용합니다. 

예를 들어, 다음 쿼리는 `age` 컬럼값이 30보다 큰 행을 반환합니다.
```sql
SELECT *
FROM employees
WHERE age > 30;
```

### **LESS THAN (미만) 비교**

특정 값보다 작은지 확인하려면 **LESS THAN(<)** 연산자를 사용합니다.

예를 들어, 다음 쿼리는 `salary` 컬럼값이 50000보다 작은 행을 반환합니다.
```sql
SELECT *
FROM employees
WHERE salary < 50000;
```

위와 같이 스칼라 함수를 사용하여 데이터베이스 쿼리에서는 다양한 비교를 수행할 수 있습니다.

### **참고 자료**
- Microsoft SQL Server 문서: https://docs.microsoft.com/en-us/sql/t-sql/language-elements/where-transact-sql?view=sql-server-ver15