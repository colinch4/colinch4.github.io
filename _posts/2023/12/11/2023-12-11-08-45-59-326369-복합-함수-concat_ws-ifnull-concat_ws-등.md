---
layout: post
title: "[sql] 복합 함수 (CONCAT_WS, IFNULL, CONCAT_WS 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

복합 SQL 함수는 여러 개의 값을 조합하거나 조건을 처리하는 데 유용합니다. 주요 함수인 CONCAT_WS, IFNULL 및 CONCAT_WS에 대해 자세히 알아보겠습니다.


## CONCAT_WS 함수

`CONCAT_WS` 함수는 지정된 구분자와 함께 문자열을 결합하는 데 사용됩니다. 

예를 들어, 
```sql
SELECT CONCAT_WS(' - ', first_name, last_name) AS full_name
FROM employees;
```
위 쿼리에서는 `first_name`과 `last_name` 사이에 `" - "` 구분자를 넣어 `full_name`을 가져옵니다.


## IFNULL 함수

`IFNULL` 함수는 NULL 값을 다른 값으로 대체하는 데 사용됩니다.

예를 들어, 
```sql
SELECT product_name, IFNULL(stock, 0) AS available_stock
FROM products;
```
위 쿼리에서는 `stock`이 NULL이면 0으로 대체하여 `available_stock`을 가져옵니다.


## CONCAT_WS 함수

`CONCAT_WS` 함수는 `CONCAT` 함수와 유사하지만, 첫 번째 매개변수로 구분자를 받아들이므로 보다 간단한 방식으로 문자열을 결합할 수 있습니다.

예를 들어, 
```sql
SELECT CONCAT_WS('-', year, month, day) AS date_string
FROM orders;
```
위 쿼리에서는 `year`, `month`, `day`를 `-`로 구분하여 `date_string`을 가져옵니다.


각 함수는 데이터를 처리하거나 원하는 형식으로 표시할 때 유용하며, SQL 쿼리를 보다 유연하게 만듭니다.


---
참고: 
- MySQL 공식 문서: https://dev.mysql.com/doc/  
- PostgreSQL 공식 문서: https://www.postgresql.org/docs/