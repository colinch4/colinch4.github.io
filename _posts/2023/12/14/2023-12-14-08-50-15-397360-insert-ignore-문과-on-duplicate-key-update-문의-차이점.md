---
layout: post
title: "[sql] INSERT IGNORE 문과 ON DUPLICATE KEY UPDATE 문의 차이점"
description: " "
date: 2023-12-14
tags: [sql]
comments: true
share: true
---

- **INSERT IGNORE**: `INSERT IGNORE` 문은 새로운 레코드를 삽입하려고 할 때, 중복된 값이 이미 존재하는 경우 해당 레코드를 무시하고 삽입을 시도합니다.

예를 들어, 아래와 같은 SQL 문을 실행할 때:

```sql
INSERT IGNORE INTO table_name (column1, column2) VALUES (value1, value2);
```

만약 `table_name`에 이미 `(value1, value2)`라는 레코드가 존재한다면, 이 삽입을 무시하고 다음 레코드로 넘어갑니다.

- **ON DUPLICATE KEY UPDATE**: `ON DUPLICATE KEY UPDATE` 문은 삽입하려는 레코드가 테이블의 기본 키나 유니크한 인덱스와 중복된 경우, 해당 레코드가 이미 존재하므로 그 레코드를 업데이트하는 동작을 수행합니다.

예를 들어, 아래와 같은 SQL 문을 실행할 때:

```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2) ON DUPLICATE KEY UPDATE column2 = value2;
```

만약 `(value1, value2)`라는 레코드가 이미 존재한다면, `column2`의 값을 `value2`로 업데이트할 것입니다.

따라서, `INSERT IGNORE`는 중복된 레코드를 무시하고, `ON DUPLICATE KEY UPDATE`는 중복된 레코드를 업데이트합니다.