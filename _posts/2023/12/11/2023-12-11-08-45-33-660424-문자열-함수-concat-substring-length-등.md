---
layout: post
title: "[sql] 문자열 함수 (CONCAT, SUBSTRING, LENGTH 등)"
description: " "
date: 2023-12-11
tags: [sql]
comments: true
share: true
---

SQL은 데이터베이스에서 문자열을 다루는데 유용한 다양한 함수를 제공합니다. 이 포스트에서는 그 중에서 주요 문자열 함수인 `CONCAT`, `SUBSTRING`, `LENGTH`에 대해 알아보겠습니다.

## CONCAT 함수

`CONCAT` 함수는 두 개 이상의 문자열을 이어 붙일 때 사용됩니다. 예를 들어, 다음과 같이 사용할 수 있습니다.

```sql
SELECT CONCAT('Hello', ' ', 'World');
-- 결과: Hello World
```

## SUBSTRING 함수

`SUBSTRING` 함수는 문자열을 잘라내어 부분 문자열을 반환합니다. 이 때, 시작 위치와 길이를 지정하여 원하는 부분 문자열을 얻을 수 있습니다. 예를 들어,

```sql
SELECT SUBSTRING('Hello World', 1, 5);
-- 결과: Hello
```

## LENGTH 함수

`LENGTH` 함수는 문자열의 길이를 반환합니다. 예를 들어,

```sql
SELECT LENGTH('Hello');
-- 결과: 5
```

이러한 문자열 함수들을 적절히 활용하여 SQL 쿼리를 더욱 다양하고 유연하게 작성할 수 있습니다.

더 많은 SQL 문자열 함수들에 대해 알고 싶다면, 공식 문서를 참조해보세요.

참고: [MySQL 공식 문서](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html)

---