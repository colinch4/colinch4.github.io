---
layout: post
title: "[sql] 조인 함수 (INNER JOIN, LEFT JOIN, RIGHT JOIN 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

SQL에서 조인은 여러 테이블 간의 관계를 설정하고 연결하는 데 사용됩니다. 조인은 INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN 등 다양한 유형이 있으며, 각각 다른 방식으로 테이블을 결합합니다.

## INNER JOIN

INNER JOIN은 두 개의 테이블 간에 일치하는 행만을 반환합니다. 
```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2 ON table1.column_name = table2.column_name;
```

이 명령은 table1과 table2 간에 일치하는 column_name을 기준으로 각 테이블의 열을 반환합니다.

## LEFT JOIN

LEFT JOIN은 왼쪽 테이블의 모든 행과 오른쪽 테이블에서 일치하는 행을 반환합니다. 일치하는 행이 없는 경우에도 왼쪽 테이블의 모든 행을 반환합니다.
```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2 ON table1.column_name = table2.column_name;
```

## RIGHT JOIN

RIGHT JOIN은 LEFT JOIN과 반대로 오른쪽 테이블의 모든 행과 왼쪽 테이블에서 일치하는 행을 반환합니다. 
```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2 ON table1.column_name = table2.column_name;
```

## FULL JOIN

FULL JOIN은 양쪽 테이블의 모든 행을 반환하며, 일치하는 행이 없는 경우 널 값을 반환합니다. 
```sql
SELECT column_name(s)
FROM table1
FULL JOIN table2 ON table1.column_name = table2.column_name;
```

조인 함수는 데이터베이스에서 데이터를 효율적으로 관리하고 필요에 맞게 연결할 수 있는 강력한 도구입니다. SQL을 사용하여 데이터베이스에서 조인을 사용하는 방법을 익히면 데이터를 더욱 유연하게 다룰 수 있습니다.

[SQL 조인에 대한 자세한 내용](https://www.w3schools.com/sql/sql_join.asp)